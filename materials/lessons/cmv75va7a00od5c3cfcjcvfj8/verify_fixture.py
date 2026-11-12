#!/usr/bin/env python3
"""Structural/arithmetic check for a newly authored fictional Academy fixture.
Does not execute Calc or decide real duplicates.
"""
from pathlib import Path
from decimal import Decimal
from datetime import date
from collections import Counter,defaultdict
import csv,json
P=Path(__file__).parent
with (P/'events-original.csv').open(newline='',encoding='utf-8-sig') as f:reader=csv.DictReader(f);assert reader.fieldnames==['ID','Date','Group','Item','Amount'];original=list(reader)
with (P/'analysis-copy.csv').open(newline='',encoding='utf-8-sig') as f:analysis=list(csv.DictReader(f))
assert len(original)==8 and len(analysis)==7
assert Counter(r['Group'] for r in original)=={'Group A':2,'Group B':3,'Group C':1,'':2}
assert sum(r['Amount']=='' for r in original)==2 and sum(r['Amount']=='' for r in analysis)==2
for r in original:date.fromisoformat(r['Date']);assert r['Group'] in ['Group A','Group B','Group C','']
def totals(rows):
 result=defaultdict(Decimal)
 for r in rows:
  if r['Amount']!='':result[r['Group']]+=Decimal(r['Amount'])
 return dict(result)
assert totals(original)=={'Group A':Decimal(42),'Group B':Decimal(43),'Group C':Decimal(18),'':Decimal(15)}
assert sum(totals(original).values())==118 and sum(totals(analysis).values())==100
assert analysis==[r for i,r in enumerate(original) if i!=5], 'Only originalrow7 exclusion is authorized by fictional author decision'
a,b=original[2],original[5];assert a['ID']==b['ID']=='EVT-104' and a['Date']!=b['Date'] and a['Amount']!=b['Amount'];assert a['Amount']=='25' and b['Amount']=='18'
assert [Decimal(r['Amount']) for r in original if r['Amount']!='']==list(map(Decimal,['30','12','25','18','18','15']))
monthly=sum((Decimal(r['Amount']) for r in original if r['Group']=='Group A' and date(2026,10,1)<=date.fromisoformat(r['Date'])<date(2026,11,1) and r['Amount']!=''),Decimal(0));assert monthly==42
assert sum((Decimal(r['Amount']) for r in original if r['Group']=='Group A' and date.fromisoformat(r['Date'])==date(2026,10,1) and r['Amount']!=''),Decimal(0))==30, 'Exactdate equality differs from wholemonth42'
print(json.dumps({'state':'PASS','kind':'Fictionalfixture structural/Decimal arithmetic, not native Calc execution','rowsOriginal':8,'rowsAnalysis':7,'blankAmountsOriginalAndAnalysis':2,'groupCounts':dict(Counter(r['Group'] for r in original)),'originalTotals':{k:str(v) for k,v in totals(original).items()},'analysisTotals':{k:str(v) for k,v in totals(analysis).items()},'totalOriginal':118,'totalAnalysis':100,'OctoberGroupA':42,'October1OnlyGroupA':30},indent=2))
