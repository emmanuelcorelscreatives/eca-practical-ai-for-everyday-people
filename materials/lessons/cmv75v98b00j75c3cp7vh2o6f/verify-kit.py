import csv
from pathlib import Path
r=list(csv.DictReader((Path(__file__).parent/'expected-comparison.csv').open(newline='',encoding='utf-8')))
assert len(r)==22, len(r)
assert all(x['Status'] in {'Verified','Unknown','Conflict'} and x['Evidence location'] and x['Evidence date'] for x in r)
prices={x['Option']:x['Value'] for x in r if x['Criterion']=='Total four-hour price'}
assert prices=={'Harbor Room':'240 CU','Maple Hall':'265 CU','Cedar Studio':'Unknown'}
assert {(x['Value'],x['Unit or scope']) for x in r if x['Option']=='Maple Hall' and x['Criterion']=='Maximum seated capacity'}=={('60','theatre layout'),('36','tables')}
assert len([x for x in r if x['Status']=='Conflict'])==2
assert next(x for x in r if x['Option']=='Harbor Room' and x['Criterion']=='Accessible toilet information')['Value']=='Unknown'
print('PASS: 22 source-aligned answer rows; price, layout, uncertainty and conflict invariants')

draft=list(csv.DictReader((Path(__file__).parent/'generated-extraction-unverified.csv').open(newline='',encoding='utf-8')))
assert len(draft)==22 and all(x['Status']=='Not yet verified' and 'Pending independent source checking' in x['Notes'] for x in draft)
assert next(x for x in draft if x['Option']=='Harbor Room' and x['Criterion']=='Accessible toilet information')['Value']=='Yes'
print('PASS: every deliberately generated draft row remains not yet verified until independent source checking')
