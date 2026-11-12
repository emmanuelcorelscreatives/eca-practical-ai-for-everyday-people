"""Check supplied fictional CSV; standard Python3 only, no network or accounts."""
import csv
from pathlib import Path
from datetime import datetime,date
r=Path(__file__).parent
original=list(csv.DictReader((r/'original-plan.csv').open(newline='')))
revision=list(csv.DictReader((r/'revision-example.csv').open(newline='')))
assert len(original)==len(revision)==6
assert len({x['Task ID'] for x in revision})==6
for o,n in zip(original,revision):
    for key in ('Task ID','Task','Original date','Current status'):assert o[key]==n[key],key
    if o['Current status']=='Complete':assert not n['Revised start'] and not n['Revised end']
parse=lambda s:datetime.strptime(s,'%Y-%m-%d %H:%M')
a=[(parse(x['Revised start']),parse(x['Revised end'])) for x in revision[2:5]]
assert [(e-s).total_seconds()/60 for s,e in a]==[30,120,180]
assert (a[2][0]-a[1][1]).total_seconds()/60==30
assert a[0][1]<=a[1][0] and a[1][1]<=a[2][0]
assert a[0][0].hour==15 and a[-1][1].hour==21
assert revision[-1]['Revised start']=='2026-10-24 10:00'
assert revision[-1]['Revised end']=='2026-10-24 12:00'
assert date(2026,10,23).strftime('%A')=='Friday'
assert date(2026,10,24).strftime('%A')=='Saturday'
print('PASS: six preserved records; completed work untouched; conditional Friday arithmetic/dependencies; Saturday unchanged. No external availability or agreement verified.')
