"""Offline parser/safety checks; not experimental validation."""
import unittest
import zipfile
from audit_received import parse_table, safe_member, joint_table_ready, ranges, sha256

class AuditTests(unittest.TestCase):
    def test_finite_header_and_units(self):
        x=parse_table(b'Series: 1\nenergy (arb.),time (microseconds)\n1,2\n')
        self.assertEqual(x['columns'][0],'energy (arb.)');self.assertEqual(x['complete_finite_rows'],1)
    def test_missing_preserved_and_blocked(self):
        x=parse_table(b'energy (arb.),time (microseconds)\n,5.3\n0,2\n')
        self.assertEqual(x['rows'],2);self.assertEqual(x['complete_finite_rows'],1)
        self.assertFalse(joint_table_ready(x));self.assertEqual(x['issue_examples'][0]['literal_fields'],['','5.3'])
    def test_zero_is_not_missing(self):
        x=parse_table(b'energy (arb.),time (microseconds)\n0,0\n')
        self.assertTrue(joint_table_ready(x))
    def test_bom_interpretation_preserves_hash(self):
        b=b'\xef\xbb\xbfSeries: 1\nenergy (arb.),time (microseconds)\n1,2\n'
        x=parse_table(b);self.assertTrue(x['utf8_bom']);self.assertEqual(x['sha256'],sha256(b))
        self.assertEqual(x['metadata']['Series'],'1')
    def test_fractional_histogram(self):
        x=parse_table(b'time (microseconds),counts\n1,0.25\n')
        self.assertEqual(x['fractional_values_by_1based_column']['2'],1);self.assertTrue(joint_table_ready(x))
    def test_negative_rga_values_kept(self):
        x=parse_table(b'Mass (amu),Ion Current (A)\n1,-2e-14\n')
        self.assertTrue(x['complete_numeric_table']);self.assertEqual(x['negative_values_by_1based_column']['2'],1)
    def test_nonfinite_and_nonnumeric(self):
        x=parse_table(b'energy (arb.),time (microseconds)\nNaN,2\n1,inf\nx,2\n')
        self.assertEqual(x['rows_with_missing_or_invalid_values'],3)
    def test_wrong_width(self):
        x=parse_table(b'energy (arb.),time (microseconds)\n1,2,3\n')
        self.assertEqual(x['issue_counts']['column_count'],1)
    def test_blank_row_blocks_default_input(self):
        x=parse_table(b'energy (arb.),time (microseconds)\n1,2\n\n')
        self.assertEqual(x['blank_lines_after_header'],1);self.assertFalse(joint_table_ready(x))
    def test_unsafe_paths(self):
        for name in ['../a','/a','C:/a','a\\b','a/../b']:
            self.assertFalse(safe_member(zipfile.ZipInfo(name)))
    def test_symlink_and_regular(self):
        bad=zipfile.ZipInfo('x');bad.external_attr=(0o120777<<16)
        self.assertFalse(safe_member(bad));self.assertTrue(safe_member(zipfile.ZipInfo('a.txt')))
    def test_line_ranges(self):
        self.assertEqual(ranges([2,3,4,7,9,10]),[[2,4],[7,7],[9,10]])
    def test_missing_header_rejected(self):
        with self.assertRaises(ValueError):parse_table(b'1,2\n3,4\n')

if __name__=='__main__':unittest.main(verbosity=2)
