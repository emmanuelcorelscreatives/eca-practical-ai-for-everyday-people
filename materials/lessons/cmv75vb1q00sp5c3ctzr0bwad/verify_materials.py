from pathlib import Path
import csv, json
p=Path(__file__).resolve().parent
facts=json.loads((p/'expected-checks.json').read_text())
source=(p/'reminder-source.txt').read_text().strip()
assert source==facts['source']
assert facts['fictional'] is True and facts['usability_result'] is None
assert facts['day']=='Thursday' and facts['time']=='14:30' and facts['action']=='bring a notebook'
assert source in (p/'reminder-card.html').read_text()
rows=list(csv.DictReader((p/'route-observations.csv').open()))
assert [r['route'] for r in rows]==['CAMERA ROUTE','MANUAL ROUTE']
assert all(v=='' for row in rows for k,v in row.items() if k!='route')
assert ' '.join((p/'actual-ocr.txt').read_text().split())==source
assert (p/'source-card.png').read_bytes().startswith(b'\x89PNG')
assert 'speechSynthesis' in (p/'practice-workbook.html').read_text()
print('PASS: exact fictional source, preserved facts, and two blank observation rows; no usability result invented.')
