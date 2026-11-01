#!/usr/bin/env python3
"""Verify the user-supplied NIST mds2-3859 package without extracting ZIPs.
Intake/schema audit only: no cuts, imputation, calibration, spectrum fit or rates.
Python 3.11+, standard library. Acquisition hashes are NOT publisher certificates.
"""
from __future__ import annotations
import argparse
import collections
import csv
import hashlib
import io
import json
import math
from pathlib import Path, PurePosixPath
import re
import stat
import zipfile

MANIFEST_NAME = 'NIST_mds2-3859_manifest.json.txt'
NOTES_NAME = 'NIST_mds2-3859_acquisition_notes.txt'
EXPECTED_FILES = {'README.txt', 'BL2data.zip', 'BL2Simulations.zip',
                  'BL1simanddata.zip', 'RGA_data.txt'}
MAX_MEMBER = 100_000_000
MAX_TOTAL = 500_000_000

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)

def safe_member(info: zipfile.ZipInfo) -> bool:
    name = info.filename
    p = PurePosixPath(name)
    return (bool(name) and not p.is_absolute() and '..' not in p.parts
            and '\\' not in name and ':' not in name and '\x00' not in name
            and not info.is_dir() and not stat.S_ISLNK(info.external_attr >> 16)
            and not (info.flag_bits & 1) and 0 <= info.file_size <= MAX_MEMBER)

def ranges(numbers: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    for n in numbers:
        if result and n == result[-1][1] + 1:
            result[-1][1] = n
        else:
            result.append([n, n])
    return result

def parse_table(data: bytes) -> dict:
    # Decode BOM for interpretation only; the bytes and raw hash are unchanged.
    lines = data.decode('utf-8-sig').splitlines()
    start = None
    for i, line in enumerate(lines):
        first = line.split(',')[0].strip().lower()
        if ',' in line and first.startswith(('energy (', 'time (', 'sim time (', 'mass (')):
            start = i
            break
    require(start is not None, 'No documented column header found')
    headers = lines[:start + 1]
    columns = next(csv.reader([lines[start]], strict=True))
    ncols = len(columns)
    counts = collections.Counter()
    missing = collections.Counter()
    negative = collections.Counter()
    fractional = collections.Counter()
    bad_lines: list[int] = []
    examples: list[dict] = []
    rows = complete = blanks = 0
    for line_no, text in enumerate(lines[start + 1:], start=start + 2):
        if not text.strip():
            blanks += 1
            continue
        row = next(csv.reader([text], strict=True))
        rows += 1
        reasons = []
        if len(row) != ncols:
            reasons.append('column_count')
        else:
            for k, value in enumerate(row, 1):
                label = str(k)
                if not value.strip():
                    missing[label] += 1
                    reasons.append('missing_column_' + label)
                    continue
                try:
                    number = float(value)
                    if not math.isfinite(number):
                        reasons.append('nonfinite_column_' + label)
                        continue
                    negative[label] += int(number < 0)
                    fractional[label] += int(not number.is_integer())
                except ValueError:
                    reasons.append('nonnumeric_column_' + label)
        if reasons:
            bad_lines.append(line_no)
            counts.update(reasons)
            item = {'source_line_1based': line_no, 'reasons': reasons, 'literal_fields': row}
            if len(examples) < 4:
                examples.append(item)
            last_example = item
        else:
            complete += 1
    if bad_lines and len(bad_lines) > len(examples):
        examples.append(last_example)
    metadata = {}
    for line in headers[:-1]:
        if ':' in line:
            key, value = line.split(':', 1)
            metadata[key.strip()] = value.strip()
    return {
        'size_bytes': len(data), 'sha256': sha256(data),
        'utf8_bom': data.startswith(b'\xef\xbb\xbf'),
        'header_lines': headers, 'columns': [c.strip() for c in columns],
        'metadata': metadata, 'rows': rows, 'complete_finite_rows': complete,
        'rows_with_missing_or_invalid_values': len(bad_lines),
        'blank_lines_after_header': blanks, 'issue_counts': dict(counts),
        'missing_values_by_1based_column': dict(missing),
        'negative_values_by_1based_column': {k:v for k,v in negative.items() if v},
        'fractional_values_by_1based_column': {k:v for k,v in fractional.items() if v},
        'issue_source_line_ranges_1based_inclusive': ranges(bad_lines),
        'issue_examples': examples,
        'complete_numeric_table': len(bad_lines) == 0,
    }

def classify(archive: str, name: str) -> str:
    if archive == 'BL2data.zip':
        return 'measured_event_pairs'
    if archive == 'BL2Simulations.zip':
        return 'simulation_histogram'
    if '125' in name:
        return 'simulation_event_pairs' if 'simulation' in name else 'measured_event_pairs'
    return 'simulation_histogram' if 'simulation' in name else 'measured_histogram'

def joint_table_ready(record: dict) -> bool:
    return record['complete_numeric_table'] and record['blank_lines_after_header'] == 0

def audit(data_dir: Path) -> dict:
    manifest_bytes = (data_dir / MANIFEST_NAME).read_bytes()
    manifest = json.loads(manifest_bytes)
    files = manifest['files']
    require(len(files) == len(EXPECTED_FILES), 'Unexpected distribution record count')
    require({r['filename'] for r in files} == EXPECTED_FILES, 'Unexpected distribution names')
    file_records = []
    for source in files:
        path = data_dir / source['filename']
        data = path.read_bytes()
        require(len(data) == source['size_bytes'], 'Size mismatch: ' + path.name)
        require(sha256(data) == source['sha256'], 'Hash mismatch: ' + path.name)
        file_records.append({k: source[k] for k in ('filename', 'size_bytes', 'sha256', 'requested_url', 'final_url')}
                            | {'matches_supplied_acquisition_manifest': True, 'publisher_checksum_verified': False})
    member_ref = {(r['archive'], r['member']): r for r in manifest['members']}
    require(len(member_ref) == len(manifest['members']), 'Duplicate manifest member')
    member_records = []
    archive_records = []
    for name in sorted(n for n in EXPECTED_FILES if n.endswith('.zip')):
        with zipfile.ZipFile(data_dir / name) as z:
            infos = z.infolist()
            require(len({i.filename for i in infos}) == len(infos), 'Duplicate ZIP member')
            require(all(safe_member(i) for i in infos), 'Unsafe ZIP member')
            require(sum(i.file_size for i in infos) <= MAX_TOTAL, 'Uncompressed size limit')
            expected = {m for a, m in member_ref if a == name}
            require({i.filename for i in infos} == expected, 'ZIP member set mismatch')
            # ZipFile.read also validates CRC for each read member.
            for info in infos:
                data = z.read(info)
                ref = member_ref[name, info.filename]
                require(sha256(data) == ref['sha256'], 'Member hash mismatch: ' + info.filename)
                rec = parse_table(data)
                require(rec['size_bytes'] == ref['size_bytes'], 'Member size mismatch')
                require(rec['rows'] == ref['data_rows'], 'Row count mismatch: ' + info.filename)
                require(len(rec['columns']) in ref['column_counts'], 'Column schema mismatch')
                require(rec['header_lines'] == ref['header_lines'], 'Interpreted header mismatch')
                member_records.append({'archive': name, 'member': info.filename,
                    'kind': classify(name, info.filename), 'matches_acquisition_member_hash': True,
                    'joint_numeric_input_ready': joint_table_ready(rec)} | rec)
            archive_records.append({'filename': name, 'members': len(infos),
                'uncompressed_bytes': sum(i.file_size for i in infos), 'crc_check': 'PASS',
                'safe_names': True, 'extracted_or_executed': False})
    rga = parse_table((data_dir / 'RGA_data.txt').read_bytes())
    require(rga['rows'] == manifest['rga_inspection']['data_rows'], 'RGA row count')
    bl2 = [r for r in member_records if r['archive'] == 'BL2data.zip']
    issues = [r for r in member_records if not r['complete_numeric_table']]
    return {
        'study': 'IC-13', 'dataset': manifest['dataset'],
        'status': 'ACQUIRED_HASH_MATCHED; SCHEMA_ISSUE_RECORDED; NO_PHYSICS_FIT',
        'audit_code_sha256': sha256(Path(__file__).read_bytes()),
        'supplied_manifest_sha256': sha256(manifest_bytes),
        'supplied_acquisition_notes_sha256': sha256((data_dir / NOTES_NAME).read_bytes()),
        'integrity_scope': 'Receipt hashes independently recomputed against supplied acquisition manifest; not publisher authentication.',
        'data_access_scope': 'Every numeric row read for schema/finite-value validation and issue masks. No spectrum, timing trend, calibration, holdout evaluation or fit computed.',
        'distributions': file_records, 'archives': archive_records, 'members': member_records, 'rga': rga,
        'summary': {'distributions_hash_matched': len(file_records), 'members_hash_matched': len(member_records),
            'bl2_series': len(bl2), 'bl2_listed_rows': sum(r['rows'] for r in bl2),
            'bl2_complete_finite_pairs': sum(r['complete_finite_rows'] for r in bl2),
            'members_with_numeric_issues': len(issues),
            'rows_with_numeric_issues': sum(r['rows_with_missing_or_invalid_values'] for r in issues),
            'prior_test_suites_rerun': False, 'experimental_fit': False},
        'interpretation_limits': [
            'BL2 energy is arbitrary units; no implicit keV conversion.',
            'Trap duration is not acquisition exposure.',
            'Blank energy is not zero and is not silently imputed or discarded.',
            'Time-present incomplete events remain distinct; energy-selected timing analysis requires a missingness rule.',
            'RGA negative currents and fractional histogram values are retained, not corrected or rounded.',
            'No absolute neutron lifetime, ARK epsilon, or additional physical coupling inferred.'],
    }

def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data-dir', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    require(not args.output.exists(), 'Refusing to overwrite existing audit output')
    result = audit(args.data_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(result['summary'], indent=2))
    print('Numeric issues are reported, not repaired. See output for analysis gates.')

if __name__ == '__main__':
    main()
