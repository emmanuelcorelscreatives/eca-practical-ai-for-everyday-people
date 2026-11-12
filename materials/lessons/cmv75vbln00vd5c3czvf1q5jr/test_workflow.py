import json, unittest
from pathlib import Path
from workflow import evaluate
class Checks(unittest.TestCase):
    def setUp(self): self.cases=json.loads(Path(__file__).with_name('cases.json').read_text())
    def test_normal_draft_only(self):
        r=evaluate(self.cases[0]); self.assertTrue(r['draft_created']); self.assertFalse(r['final_created']); self.assertEqual(r['status'],'Awaiting human review')
    def test_missing_exact(self):
        r=evaluate(self.cases[1]); self.assertEqual(r['missing'],['start_time']); self.assertFalse(r['draft_created'])
    def test_conflict_sources(self):
        r=evaluate(self.cases[2]); self.assertEqual(r['conflicts']['date'],[{'source':'signed event form','value':'2027-06-12'},{'source':'flyer draft','value':'2027-06-19'}]); self.assertEqual(r['owner'],'Event coordinator'); self.assertFalse(r['draft_created'])
    def test_outside_scope(self): self.assertEqual(evaluate(self.cases[3])['status'],'Outside scope')
    def test_manual_fallback(self): self.assertEqual(evaluate(self.cases[4])['status'],'Manual fallback; awaiting human review')
    def test_check_prior_outcome(self):
        c=dict(self.cases[4],prior_outcome_checked=False); self.assertEqual(evaluate(c)['status'],'Prior outcome unknown')
    def test_single_retry(self):
        c=dict(self.cases[4],later_retries=0); self.assertEqual(evaluate(c)['status'],'One later retry allowed')
    def test_final_always_blocked(self):
        for c in self.cases: self.assertFalse(evaluate(c)['final_created'])
if __name__ == '__main__': unittest.main()
