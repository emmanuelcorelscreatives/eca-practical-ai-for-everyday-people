import json,csv,sys
from pathlib import Path
r=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent
x=json.loads((r/'verified-study-set.json').read_text())['items']
assert len(x)==8 and len({i['id'] for i in x})==8
assert [sum(i['type']==t for i in x) for t in ['short-answer','multiple-choice','flashcard']]==[3,2,3]
source=dict(line.split(': ',1) for line in (r/'source-passage.txt').read_text().splitlines() if line.startswith(('S1:','S2:','S3:','S4:','S5:')))
a=next(i for i in x if i['id']=='SA3');assert a['answer']=='400 liters.' and a['calculation']=='2 × 200 liters = 400 liters; total is inferred by arithmetic, not directly stated.' and a['status']=='Supported calculation'
rows={a['Item']:a for a in csv.DictReader((r/'verification-table.csv').open())};assert len(rows)==8
workspace=(r/'source-study-workspace.html').read_text();manual=(r/'manual-study-set.html').read_text();embedded=json.loads(workspace.split('const items=',1)[1].split(';const sources=',1)[0]);assert embedded==x
for i in x:
 assert i['question'] and i['answer'] and 'installed' not in i['question']
 assert all(k in source for k in i['evidence'])
 if 'correct' in i: assert i['options'][i['correct']]==i['answer']
 expected={'Item':i['id'],'Question':i['question'],'Proposed answer':i['answer'],'Supporting passage':'; '.join(f'{k}: {source[k]}' for k in i['evidence']),'Status':i['status'],'Correction':i.get('correction',i.get('calculation',''))};assert rows[i['id']]==expected
 assert i['question'] in manual and i['answer'] in manual
 if i.get('calculation'):assert 'Supported calculation: '+i['calculation'] in manual
print('PASS: structural/source-ID checks, actual SA3 calculation fields, exact JSON/CSV/app agreement, manual questions/keys/calculation labels. Semantic source support requires independent human/model review.')
