from pathlib import Path
import csv
p=Path(__file__).parent
notes=(p/'supplied-notes.txt').read_text();draft=(p/'corrected-draft.txt').read_text();bad=(p/'generated-draft-to-check.txt').read_text()
assert 'priya.shah@example.org' in notes and 'priya.shah@example.org' in draft
assert 'priya.shaw@example.org' in bad
assert '22 October 2026 at 14:00' in draft
assert 'whether receiving the print-ready signs by 18 October 2026 would work?' in draft
assert "I'll deliver the printed signs by 9:00" in bad and "I'll deliver" not in draft
assert len(list(csv.DictReader((p/'recipient-directory.csv').open())))==2
for name in ['Room-Setup-v2.pdf','Room-Setup-v3.pdf']:assert (p/name).read_bytes().startswith(b'%PDF-')
print('PASS: local practice file consistency. This does not verify real recipients, attachments or cloud permissions.')
