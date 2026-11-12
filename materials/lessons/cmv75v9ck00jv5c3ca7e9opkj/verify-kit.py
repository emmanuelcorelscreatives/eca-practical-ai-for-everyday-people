import csv
from pathlib import Path
r=Path(__file__).parent
rows=list(csv.DictReader((r/'checklist.csv').open(newline='')))
assert len(rows)==9 and len({x['id'] for x in rows})==9
assert all(x['action'] and x['done_when'] and x['completed']=='false' for x in rows)
assert 'leave unresolved' in rows[4]['unknown_or_condition']
assert 'Discard none' in rows[2]['unknown_or_condition']
assert len({x['action'].strip().casefold() for x in rows})==9
assert 'nothing else is on the desktop' in rows[-1]['final_review']
assert rows[6]['action']=='Return the notebook' and rows[7]['action']=='Place the lamp'
assert len(list(csv.DictReader((r/'flawed-draft.csv').open(newline=''))))==5
print('PASS: 9 unchecked reference rows, protected-paper and unresolved-reach constraints; not physical verification')
