"""Check the fixed fictional exercise's source consistency; no network/browser."""
import csv,json,pathlib
p=pathlib.Path(__file__).parent;d=json.loads((p/'fixture-data.json').read_text())
assert d['selectedDate']=='2026-10-15' and d['returnDeadline']=='18:00'
assert d['externalActionsCompleted']==[] and 'not current' in d['notice']
a,b=d['routes'];assert a['estimateMinutes']>b['estimateMinutes'] and a['transfers']<b['transfers'] and a['walkingMinutes']<b['walkingMinutes']
assert d['generatedClaims']['openingHours']!=d['venue']['specialHours']
assert int(d['generatedClaims']['routeAEstimate'].split()[0])!=a['estimateMinutes']
assert 'not stated' in d['venue']['lift'] and len(d['unresolved'])==3
with (p/'route-comparison-blank.csv').open(newline='') as f:r=list(csv.reader(f))
assert len(r)==3 and all(len(x)==6 for x in r)
assert r[1][0]=='ROUTE A' and r[2][0]=='ROUTE B' and all(v=='UNKNOWN' for x in r[1:] for v in x[1:])
with (p/'venue-evidence-example.csv').open(newline='') as f:r=list(csv.DictReader(f))
assert r[0]['Generated draft']!=r[0]['Opened practice evidence'] and r[2]['Status']=='UNRESOLVED'
h=(p/'index.html').read_text();assert 'fetch(' not in h and 'XMLHttpRequest' not in h
assert 'disabled>DO NOT COMPLETE BOOKING' in h
for section in ['brief','draft','visit','access','tickets','planner','manual']:assert f'<section id="{section}"' in h
assert len(d['additionalUnresolved'])==4
a=d['conditionalTimelineAssumptions'];assert 13*60-(75+15+20)==11*60+10 and 13*60+90+15+80+25==16*60+30 and 16*60+30<=18*60
print('PASS: fixed fictional data, changed-hours/estimate corrections, unresolved essentials, all-UNKNOWN starter, offline/no-transaction app source. Browser interaction and independent reviews remain separate requirements.')
