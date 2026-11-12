"""Read-only local checks of self-authored fictional lesson fixtures."""
from pathlib import Path
import csv
from collections import Counter
from datetime import date
ROOT=Path(__file__).resolve().parent
FIELDS=['Record ID','Date','Item','Quantity','Note','Source reference']
def load(name):
 with (ROOT/name).open(newline='',encoding='utf-8') as f:
  reader=csv.DictReader(f);assert reader.fieldnames==FIELDS,(name,reader.fieldnames);return list(reader)
def controls(rows):
 dates=[date.fromisoformat(r['Date']) for r in rows]
 return len(rows),min(dates).isoformat(),max(dates).isoformat(),sum(int(r['Quantity']) for r in rows)
def differences(source,output):
 a={r['Record ID']:r for r in source};counts=Counter(r['Record ID'] for r in output)
 return {'missing':sorted(set(a)-set(counts)),'unexpected':sorted(set(counts)-set(a)),
 'duplicates':sorted(k for k,v in counts.items() if v!=1),
 'fields':[(r['Record ID'],f,a[r['Record ID']][f],r[f]) for r in output if r['Record ID'] in a for f in FIELDS if a[r['Record ID']][f]!=r[f]]}
source=load('source.csv');assert controls(source)==(6,'2026-11-03','2026-11-18',53)
assert len(set(r['Record ID'] for r in source))==6
omitted=load('output-1-omitted.csv');assert controls(omitted)[0]==5 and controls(omitted)[3]==49
assert differences(source,omitted)=={'missing':['EV-104'],'unexpected':[],'duplicates':[],'fields':[]}
wrong=load('output-2-date-error.csv');assert controls(wrong)==controls(source)
assert differences(source,wrong)['fields']==[('EV-105','Date','2026-11-18','2026-11-08')]
for name in ['checked-transformation.csv','destination.csv']:
 assert load(name)==source;assert controls(load(name))==controls(source)
duplicate=[r for r in source if r['Record ID']!='EV-104']+[dict(source[0])]
assert len(duplicate)==len(source)
assert differences(source,duplicate)['missing']==['EV-104'] and differences(source,duplicate)['duplicates']==['EV-101']
prose=(ROOT/'unsupported-prose.txt').read_text();assert 'confirmed for delivery' in prose
assert source[4]['Note']=='Delivery status missing' and 'confirmed' not in source[4]['Note'].lower()
print('PASS: six source IDs; source controls 6 / 2026-11-03 / 2026-11-18 / 53.')
print('PASS: output 1 missing EV-104; 5 rows and quantity 49.')
print('PASS: output 2 EV-105 date differs; summaries still match and fail to detect it.')
print('PASS: duplicate-ID counterexample caught despite matching row count.')
print('PASS: checked and destination references equal every original field.')
print('PASS: missing delivery status preserved; deliberate unsupported prose isolated.')
