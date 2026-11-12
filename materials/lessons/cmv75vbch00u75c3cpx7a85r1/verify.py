import csv,json,pathlib
p=pathlib.Path(__file__).parent
a=json.loads((p/'handoff-completed.json').read_text(encoding='utf-8'))['records']
b=list(csv.DictReader((p/'handoff-completed.csv').open(newline='',encoding='utf-8')))
assert a==b and len(a)==4 and len({r['Item ID'] for r in a})==4
assert a[0]['Verified value']=='2026-11-14, 10:00–15:00'
assert a[1]['Verified value']=='Harbor Hall, 18 Cedar Lane'
assert a[2]['Verified value']=='East entrance'
assert a[3]['Status']=='MISSING' and a[3]['Verified value']=='[MISSING]'
f=(p/'handoff-plain-text.txt').read_text(encoding='utf-8')
labels=['ITEM ID','FIELD','VALUE','SOURCE','SOURCE LOCATION','SOURCE DATE','STATUS','NOTES']
blocks=f.split('RECORD ')[1:]
assert len(blocks)==4
for r,block in zip(a,blocks):
 lines=block.splitlines()
 assert lines[0]==r['Item ID']
 parsed=dict(line.split(': ',1) if ': ' in line else (line.rstrip(':'),'') for line in lines[1:] if line)
 assert parsed==dict(zip(labels,r.values()))
print('PASS: four records, stable IDs, exact values, missing admission and all fallback fields retained.')
