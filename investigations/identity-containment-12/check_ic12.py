#!/usr/bin/env python3
"""Offline unit fixtures, not NIST events. Includes likelihood factorization checks."""
import copy
import hashlib
import io
import json
import math
from pathlib import Path
import platform
import stat
import tempfile
import unittest
from unittest.mock import patch
import warnings
import zipfile
from datetime import datetime, timezone
import nist_intake as tool

HERE = Path(__file__).resolve().parent
SPEC = json.loads((HERE/'analysis-contract.json').read_text())

class Fixture(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
    def tearDown(self):
        self.temp.cleanup()
    def archive(self, entries):
        p = self.root/'fixture.zip'
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with zipfile.ZipFile(p, 'w') as z:
                for name, data in entries:
                    z.writestr(name, data)
        return p
    def ready(self):
        data = self.root/'events.fixture.txt'
        data.write_text('TEST FIXTURE; NOT NIST DATA\n')
        spec = copy.deepcopy(SPEC)
        for key, value in spec.items():
            if value is None:
                spec[key] = 'Offline fixture assertion, not scientific evidence'
        spec['inputs'] = [{'path': data.name, 'sha256': tool.digest(data), 'role': 'observed_events'}]
        spec['calibration_groups'] = ['fixture-run-a']
        spec['evaluation_groups'] = ['fixture-run-b']
        return spec
    def test_01_archive_hashes(self):
        p = self.archive([('folder/events.txt', b'not real data')])
        result = tool.inspect(p)
        self.assertEqual(result['members'][0]['sha256'], hashlib.sha256(b'not real data').hexdigest())
        self.assertIsNone(result['publisher_checksum'])
        self.assertFalse((self.root/'folder').exists())
    def test_02_traversal_and_absolute(self):
        for name in ['../outside', '/absolute', 'C:/file', 'dir\\file']:
            with self.assertRaises(ValueError):
                tool.inventory_zip(self.archive([(name, b'a')]))
    def test_03_link(self):
        info = zipfile.ZipInfo('link'); info.create_system = 3
        info.external_attr = (stat.S_IFLNK | 0o777) << 16
        with self.assertRaises(ValueError):
            tool.inventory_zip(self.archive([(info, b'../outside')]))
    def test_04_duplicates(self):
        with self.assertRaises(ValueError):
            tool.inventory_zip(self.archive([('a', b'1'), ('a', b'2')]))
    def test_05_unpacked_limit(self):
        with self.assertRaises(ValueError):
            tool.inventory_zip(self.archive([('a', b'12345')]), limit=4)
    def test_06_text_error(self):
        p = self.root/'README.txt'; p.write_text('<html>Error</html>')
        with self.assertRaises(ValueError): tool.inspect(p)
    def test_07_source_restrictions(self):
        tool.check_url(tool.BASE+'README.txt')
        for url in ['http://data.nist.gov/a', 'https://example.com/a', 'https://x@data.nist.gov/a']:
            with self.assertRaises(ValueError): tool.check_url(url)
    def test_08_mock_fetch_and_no_overwrite(self):
        response = io.BytesIO(b'fixture readme\n'); response.geturl = lambda: tool.BASE+'README.txt'
        with patch.object(tool.urllib.request, 'build_opener') as opener:
            opener.return_value.open.return_value = response
            result = tool.fetch_file('README.txt', self.root)
        self.assertEqual(result['sha256'], hashlib.sha256(b'fixture readme\n').hexdigest())
        with self.assertRaises(FileExistsError): tool.fetch_file('README.txt', self.root)
    def test_09_mock_download_limit_cleanup(self):
        response = io.BytesIO(b'123456'); response.geturl = lambda: tool.BASE+'README.txt'
        with patch.object(tool.urllib.request, 'build_opener') as opener:
            opener.return_value.open.return_value = response
            with self.assertRaises(ValueError): tool.fetch_file('README.txt', self.root, limit=4)
        self.assertEqual(list(self.root.iterdir()), [])
    def test_10_corrupted_crc(self):
        p = self.archive([('a', b'unique-payload')])
        data = p.read_bytes().replace(b'unique-payload', b'broken-payload', 1)
        p.write_bytes(data)
        with self.assertRaises(zipfile.BadZipFile): tool.inventory_zip(p)
    def test_11_actual_contract_blocked(self):
        status = tool.readiness(SPEC, self.root)
        self.assertEqual(status['status'], 'BLOCKED')
        self.assertIn('no observed-event input declared', status['issues'])
    def test_12_fixture_contract_only_ready_for_review(self):
        self.assertEqual(tool.readiness(self.ready(), self.root)['status'], 'READY_FOR_REVIEW')
    def test_13_group_overlap(self):
        spec = self.ready(); spec['evaluation_groups'] = ['fixture-run-a']
        self.assertIn('calibration and evaluation groups overlap', tool.readiness(spec, self.root)['issues'])
    def test_14_missing_mapping_and_hash(self):
        spec = self.ready(); spec['energy_mapping'] = None; spec['inputs'][0]['sha256'] = 'not-a-hash'
        errors = tool.readiness(spec, self.root)['issues']
        self.assertIn('energy_mapping unresolved', errors)
        self.assertTrue(any('hash mismatch' in x for x in errors))
    def test_15_absolute_rate_requires_independent_anchors(self):
        spec = self.ready(); spec['target'] = 'absolute_decay_rate'
        for k in ('absolute_exposure', 'absolute_efficiencies', 'channel_completeness', 'upstream_invariance'):
            spec[k] = None
        self.assertEqual(len(tool.readiness(spec, self.root)['issues']), 4)
    def test_16_poisson_multinomial_factorization(self):
        counts = [5, 2, 9]; weights = [.3, .1, .4]; scale = 30.
        means = [scale*w for w in weights]; total = sum(counts); mean = sum(means)
        direct = sum(k*math.log(mu)-mu-math.lgamma(k+1) for k, mu in zip(counts, means))
        poisson = total*math.log(mean)-mean-math.lgamma(total+1)
        multinomial = math.lgamma(total+1)-sum(math.lgamma(k+1) for k in counts)
        multinomial += sum(k*math.log(w/sum(weights)) for k,w in zip(counts, weights))
        self.assertAlmostEqual(direct, poisson+multinomial, places=12)
    def test_17_normalization_erases_common_scale(self):
        weights = [.3, .1, .4]
        for scale in [1., 8., 100.]:
            p = [scale*w/sum(scale*x for x in weights) for w in weights]
            for a,b in zip(p, [.375, .125, .5]): self.assertAlmostEqual(a,b)
    def test_18_independently_fixed_background_exception(self):
        w = [.3, .1, .4]; background = [2., .1, .3]
        p1 = [a+b for a,b in zip(w, background)]; p1 = [x/sum(p1) for x in p1]
        p2 = [8*a+b for a,b in zip(w, background)]; p2 = [x/sum(p2) for x in p2]
        self.assertGreater(max(abs(a-b) for a,b in zip(p1,p2)), .1)

class Recorded(unittest.TextTestResult):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs); self.records=[]
    def addSuccess(self,test):
        super().addSuccess(test); self.records.append({'test': test._testMethodName, 'status':'PASS'})
    def addFailure(self,test,err):
        super().addFailure(test,err); self.records.append({'test':test._testMethodName,'status':'FAIL','error':str(err[1])})
    def addError(self,test,err):
        super().addError(test,err); self.records.append({'test':test._testMethodName,'status':'ERROR','error':str(err[1])})

if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2,resultclass=Recorded).run(unittest.defaultTestLoader.loadTestsFromTestCase(Fixture))
    report = {'study':'IC-12','utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),
              'scope':'Offline fixture/software checks and elementary likelihood identities. No NIST event analysis.',
              'input_hashes':{n:tool.digest(HERE/n) for n in ['nist_intake.py','check_ic12.py','analysis-contract.json']},
              'total':result.testsRun,'passed':sum(r['status']=='PASS' for r in result.records),'checks':result.records,
              'real_analysis_readiness':tool.readiness(SPEC, HERE)}
    (HERE/'test-results.json').write_text(json.dumps(report,indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
