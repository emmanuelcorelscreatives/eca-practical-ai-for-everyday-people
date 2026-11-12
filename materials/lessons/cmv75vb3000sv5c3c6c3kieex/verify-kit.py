from pathlib import Path
import json,csv
p=Path(__file__).parent
b=json.loads((p/'brief.json').read_text())
a=list(csv.DictReader((p/'claim-review-answer.csv').open(newline='')))
assert b['service_name']=='ClearDesk Document Support'
assert b['delivery']==['editable document','PDF']
assert len(a)==9
assert {r['Status'] for r in a}=={'Supported','Unsupported','Needs confirmation'}
assert next(r for r in a if r['Draft claim']=='Delivered within 24 hours')['Brief evidence']==''
assert next(r for r in a if r['Draft claim']=='Available for new projects')['Status']=='Needs confirmation'
assert len(list(csv.DictReader((p/'claim-review-blank.csv').open(newline=''))))==9
print('PASS: service name, deliverables, nine-row CSV counts, status vocabulary, empty 24-hour evidence and availability status assertions.')
