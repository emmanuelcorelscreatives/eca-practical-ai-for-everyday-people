import csv
import unittest
from pathlib import Path
from calculate import seconds, evaluate


class MeasurementChecks(unittest.TestCase):
    def rows(self):
        with Path(__file__).with_name('lecture-demo-results.csv').open(newline='') as f:
            return list(csv.DictReader(f))

    def test_all_four_source_totals_and_differences(self):
        result = evaluate(self.rows())
        self.assertEqual([x['total_seconds'] for x in result], [510,720,920,1110])
        self.assertEqual([x['difference_seconds'] for x in result], [350,250,200,-90])

    def test_mismatched_total_is_rejected(self):
        rows=self.rows(); rows[0]['total_assisted']='8:31'
        with self.assertRaises(ValueError): evaluate(rows)

    def test_failed_fast_draft_is_not_comparable(self):
        rows=self.rows(); rows[0]['acceptance']='revise'
        result=evaluate(rows)
        self.assertFalse(result[0]['comparable'])
        self.assertIsNone(result[0]['difference_seconds'])

    def test_invalid_duration_and_missing_evidence_rejected(self):
        for value in ['4:60','-1:30','','4.10','4:1']:
            with self.assertRaises(ValueError): seconds(value)


if __name__=='__main__': unittest.main()
