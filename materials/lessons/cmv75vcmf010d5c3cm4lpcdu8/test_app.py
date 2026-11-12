"""Actual local tool execution tests, using an isolated temporary kit copy."""
import tempfile
import unittest
import shutil
from pathlib import Path
from app import run_scenario, save_draft, ROOT, DEST


class BoundaryPracticeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ('approved-event-brief.pdf', 'checklist-template.md'):
            shutil.copyfile(ROOT / name, self.root / name)

    def test_normal_observed_read_and_exclusive_write(self):
        result = run_scenario('normal', self.root)
        self.assertEqual(result['activity'], ['Opened approved-event-brief.pdf', 'Read checklist template'])
        self.assertFalse((self.root / DEST).exists())
        for exact in ('Community Skills Afternoon', '18 April 2027', 'Riverside Community Hall',
                      'welcome desk, repair demonstration and shared reading corner',
                      'Keep the entrance route clear and provide seating near each activity.',
                      'coordinator', 'final attendance estimate', 'Awaiting confirmation'):
            self.assertIn(exact, result['draft'])
        saved = save_draft(result, self.root)
        self.assertTrue(saved['saved'])
        self.assertEqual((self.root / DEST).read_text(), result['draft'])
        self.assertNotIn('not yet saved', (self.root / DEST).read_text())
        self.assertIn('save completion is reported separately', (self.root / DEST).read_text())
        before = (self.root / DEST).read_bytes()
        with self.assertRaises(FileExistsError):
            save_draft(result, self.root)
        self.assertEqual((self.root / DEST).read_bytes(), before)
        self.assertEqual(saved['externalActionsExecuted'], [])

    def test_actual_template_sections_and_marker_are_used(self):
        template = self.root / 'checklist-template.md'
        template.write_text(template.read_text() + '\nHuman review note: preserve this approved template marker.\n')
        result = run_scenario('normal', self.root)
        self.assertIn('preserve this approved template marker', result['draft'])
        self.assertIn('## Tool activity / status', result['draft'])
        self.assertNotIn('| Confirm date and venue | | |', result['draft'])

    def test_changed_input_after_preview_requires_fresh_review(self):
        result = run_scenario('normal', self.root)
        template = self.root / 'checklist-template.md'
        template.write_text(template.read_text() + '\nChanged after preview.\n')
        with self.assertRaisesRegex(PermissionError, 'changed after preview'):
            save_draft(result, self.root)
        self.assertFalse((self.root / DEST).exists())

    def test_every_stop_creates_no_file(self):
        for case in ('missing', 'conflict', 'prohibited', 'permission', 'unverified'):
            with self.subTest(case=case):
                result = run_scenario(case, self.root)
                self.assertIsNone(result['draft'])
                self.assertFalse(result['saved'])
                self.assertEqual(result['externalActionsExecuted'], [])
                with self.assertRaises(PermissionError):
                    save_draft(result, self.root)
                self.assertFalse((self.root / DEST).exists())

    def test_conflict_retains_both_values_and_selects_neither(self):
        result = run_scenario('conflict', self.root)
        for text in ('80', '120', 'neither value selected'):
            self.assertIn(text, result['message'])

    def test_unknown_case_and_path_cannot_be_selected(self):
        for case in ('../private', '/etc/passwd', '', 'send', None):
            with self.assertRaises(ValueError):
                run_scenario(case, self.root)

    def test_missing_approved_file_does_not_fall_back(self):
        (self.root / 'approved-event-brief.pdf').unlink()
        with self.assertRaises(Exception):
            run_scenario('normal', self.root)
        self.assertFalse((self.root / DEST).exists())

    def test_linked_sandbox_refused(self):
        target = self.root / 'other'
        target.mkdir()
        (self.root / 'sandbox').symlink_to(target, target_is_directory=True)
        with self.assertRaises(PermissionError):
            save_draft(run_scenario('normal', self.root), self.root)
        self.assertEqual(list(target.iterdir()), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
