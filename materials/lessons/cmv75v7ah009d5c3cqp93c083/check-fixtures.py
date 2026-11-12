#!/usr/bin/env python3
"""Offline fixture arithmetic check; does not inspect any spreadsheet application."""
from pathlib import Path
import csv,json,hashlib
from decimal import Decimal
P=Path(__file__).resolve().parent
EXPECTED=[('Venue','120'),('Printing','45'),('Refreshments','80'),('Transport','35'),('Name badges','20'),('Equipment rental','90'),('Accessibility materials','50'),('Volunteer meals','60')]
def load(name):
 with (P/name).open(newline='') as f:
  r=csv.DictReader(f); assert r.fieldnames==['Date','Item','Amount']; rows=list(r)
 assert all(x['Date']=='' for x in rows)
 return [(x['Item'],x['Amount']) for x in rows]
s=load('source-notes.csv');f=load('faulty-sheet.csv');c=load('corrected-sheet.csv')
assert s==EXPECTED and c==EXPECTED
assert f==[(a,'' if a=='Transport' else b) for a,b in EXPECTED if a!='Accessibility materials']
num=lambda rows:[Decimal(b) for a,b in rows if b!='']
assert len(f)==7 and len(num(f))==6
assert f[3]==('Transport','') and f[6]==('Volunteer meals','60')
assert sum(num(f[:6]))==355 and sum(num(f))==415
assert sum(num(c))==500 and len(num(c))==8
assert c[6]==('Accessibility materials','50') and c[7]==('Volunteer meals','60')
assert Decimal(30)/2==15 and Decimal(30)/3==10
print(json.dumps({'state':'PASS','scope':'Supplied CSV fixtures and deterministic arithmetic only','initial_range_C2_C7':355,'all_existing_rows':415,'corrected_total':500,'initial_COUNT':6,'initial_COUNTA':7,'corrected_counts':8,'blank_average':15,'zero_average':10},sort_keys=True))
