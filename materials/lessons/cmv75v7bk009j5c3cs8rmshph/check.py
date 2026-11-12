"""Verify fictional fixed fixture arithmetic; no chart/application certification."""
import csv, json
from pathlib import Path
R=Path(__file__).resolve().parent
with (R/'visits.csv').open(newline='') as f: visits=list(csv.DictReader(f))
with (R/'attendance.csv').open(newline='') as f: attendance=list(csv.DictReader(f))
assert [r['Week'] for r in visits]==['Week 1','Week 2','Week 3','Week 4']
v=[int(r['Visits']) for r in visits]
assert [r['Month'] for r in attendance]==['June','July']
a=[[int(r[c]) for c in ['Morning','Evening','Total']] for r in attendance]
assert all(m+e==t for m,e,t in a)
result={'visits':v,'week1_to_week2_difference':v[1]-v[0], 'week1_to_week2_percent_rounded':round((v[1]-v[0])/v[0]*100,2),'week3_to_week4_difference':v[3]-v[2],'week3_to_week4_percent_rounded':round((v[3]-v[2])/v[2]*100,2),'monthly_totals':[r[2] for r in a],'morning_change':a[1][0]-a[0][0],'evening_change':a[1][1]-a[0][1],'evening_share_percentage_point_change':round((a[1][1]/a[1][2]-a[0][1]/a[0][2])*100)}
expected=json.loads((R/'expected-checks.json').read_text())
assert result==expected,(result,expected)
print(json.dumps({'state':'PASS','checks':result},indent=2))
