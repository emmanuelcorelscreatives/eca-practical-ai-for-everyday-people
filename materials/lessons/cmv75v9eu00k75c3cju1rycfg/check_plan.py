"""Validate this fictional lecture example offline with the Python standard library."""
import csv,json,pathlib
P=pathlib.Path(__file__).resolve().parent
def load(n):
 with (P/n).open(newline='',encoding='utf-8') as f:return list(csv.DictReader(f))
def minute(s):
 h,m=map(int,s.split(':'));assert 0<=h<24 and 0<=m<60;return h*60+m
w=load('available-windows.csv'); t=load('requested-and-selected-tasks.csv'); p=load('reviewed-draft.csv'); alloc=load('capacity-allocation.csv')
assert all(minute(r['end'])-minute(r['start'])==int(r['minutes']) for r in w+p+alloc)
assert sum(int(r['minutes']) for r in w)==780
assert sum(int(r['requested_minutes']) for r in t)==840
assert sum(int(r['selected_minutes']) for r in t)==600
assert sum(int(r['minutes']) for r in p)==600
assert 600<=780-120
for r in p+alloc:
 assert any(x['day']==r['day'] and minute(x['start'])<=minute(r['start'])<minute(r['end'])<=minute(x['end']) for x in w),r
for i,a in enumerate(p+alloc):
 for b in (p+alloc)[i+1:]:
  assert a['day']!=b['day'] or max(minute(a['start']),minute(b['start']))>=min(minute(a['end']),minute(b['end'])),(a,b)
assert sum(int(r['minutes']) for r in alloc if r['allocation'].startswith('Protected buffer'))==120
assert sum(int(r['minutes']) for r in alloc if r['allocation'].startswith('Unassigned usable capacity'))==60
expected={'Study':240,'Groceries':90,'Laundry':90,'Essential cleaning only':60,'Administration':60,'Family call':60}
assert {name:sum(int(r['minutes']) for r in p if r['task']==name) for name in expected}==expected
assert len(p)==7
assert (minute('12:00')-minute('11:30'))==30
print(json.dumps({'verdict':'PASS','available_minutes':780,'buffer_minutes':120,'usable_minutes':660,'requested_minutes':840,'initial_overload_minutes':180,'scheduled_minutes':600,'spare_usable_minutes':60,'deferred_project_minutes':180,'removed_cleaning_scope_minutes':60,'calendar_events_saved':False},indent=2))
