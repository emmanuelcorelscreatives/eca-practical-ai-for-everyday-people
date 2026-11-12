"""Validate the supplied fictional timing fragment, not a real event."""
import csv,json
from pathlib import Path
root=Path(__file__).parent
rows=list(csv.DictReader((root/'example-timeline.csv').open()))
by={r['task']:r for r in rows}
for r in rows:
    for k in ('start_minute','end_minute','active_minutes'):r[k]=int(r[k])
    assert 0<=r['start_minute']<r['end_minute']
    assert 0<=r['active_minutes']<=r['end_minute']-r['start_minute']
p,c,s=(by[n] for n in ('Prepare food','Cooling','Print signs'))
assert c['start_minute']>=p['end_minute']
assert s['start_minute']>=c['start_minute']
active=[r for r in rows if r['resource']=='organizer']
for i,a in enumerate(active):
    for b in active[i+1:]:assert max(a['start_minute'],b['start_minute'])>=min(a['end_minute'],b['end_minute']), 'Organizer collision'
result={'active_minutes':sum(r['active_minutes'] for r in rows),'elapsed_minutes':max(r['end_minute'] for r in rows)-min(r['start_minute'] for r in rows),'summed_row_durations':sum(r['end_minute']-r['start_minute'] for r in rows),'printing_cooling_overlap_minutes':max(0,min(c['end_minute'],s['end_minute'])-max(c['start_minute'],s['start_minute'])),'complete_picnic_plan':False,'unresolved':['route and transport timing','venue confirmation','transition allowance','recovery allowance','other task durations']}
expected=json.loads((root/'expected-checks.json').read_text())
assert result==expected,(result,expected)
print(json.dumps(result,indent=2))
