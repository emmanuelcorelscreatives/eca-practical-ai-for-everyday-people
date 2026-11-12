from pathlib import Path
import csv
p=Path(__file__).parent
notice=(p/'originals/Appointment notice.txt').read_text(); notes=(p/'originals/Personal notes.txt').read_text(); scan=(p/'originals/Record scan-source.txt').read_text()
assert '18 October 2026' in notice and '20 October 2026' in notes
assert '18 October 2026' in scan and '[unreadable]' in scan
assert '18 October 2028' in (p/'ocr/tentative.txt').read_text()
assert '18 October 2026' in (p/'ocr/corrected.txt').read_text()
rows=list(csv.DictReader((p/'expected/evidence-table.csv').open()))
assert [r['Status'] for r in rows]==['Verified','Missing','Conflict','Verified','Missing']
assert '2028' in rows[3]['Supplied information'] and 'unclear' in rows[4]['Supplied information']
assert 'Attachment A' in notice and not any(f.name=='Attachment A' for f in p.rglob('*'))
assert all('01 Originals/' in r['Source file'] for r in rows)
assert 'not supplied' in (p/'expected/sample-draft.md').read_text()
print('PASS: fictional source/date conflict/OCR correction/status/source links/missing attachment preserved')
