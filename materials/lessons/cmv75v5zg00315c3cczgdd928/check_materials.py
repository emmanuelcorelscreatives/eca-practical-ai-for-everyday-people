from pathlib import Path
import csv
p=Path(__file__).parent
notes=(p/'source-notes.txt').read_text()
rows=list(csv.DictReader((p/'traceability.csv').open(newline='')))
assert len(rows)==7
for r in rows:
 assert r['source_note'] in notes
 assert r['audit_result']=='Supported'
 assert r['checklist_action'] in (p/'final-checklist.txt').read_text()
assert '09:30' in rows[0]['checklist_action']
assert all('gloves' not in r['checklist_action'].lower() for r in rows)
assert 'Do not move marked electrical boxes; leave them untouched' in [r['checklist_action'] for r in rows]
assert 'Ask the coordinator before lifting heavy boxes' in [r['checklist_action'] for r in rows]
print('PASS: seven supported source-matched actions; exact arrival and safety boundaries preserved')
