#!/usr/bin/env python3
import csv,json
from simulator import ROOT,simulate
s=json.loads((ROOT/'settings.json').read_text());rows=list(csv.DictReader((ROOT/'inputs.csv').open()));h,e,d=simulate(s,rows)
assert [len(x['attempts']) for x in h]==[1,2,3]
assert [x['simulated_duration_seconds'] for x in h[0]['attempts']]==[8]
assert [x['simulated_wait_before_seconds'] for x in h[1]['attempts']]==[0,10]
assert [x['simulated_duration_seconds'] for x in h[1]['attempts']]==[2,9]
assert [x['simulated_wait_before_seconds'] for x in h[2]['attempts']]==[0,10,30]
assert set(d)=={'REQ-101','REQ-102'} and len(e)==1
assert e[0]['Run or Input ID']=='REQ-103' and e[0]['Attempts']==3
assert e[0]['Plain-language Error']=='Service unavailable after three attempts'
assert e[0]['Status']=='Needs human review'
for scenario in ['Missing permission','Timeout']:
 hh,ee,dd=simulate(s,[{'Input ID':'CHECK-1','Scenario':scenario,'Safe input reference':'Synthetic check'}]);assert len(hh[0]['attempts'])==1 and not dd and len(ee)==1
hh,ee,dd=simulate(dict(s,timeout_seconds=1),rows[:1]);assert not dd and len(hh[0]['attempts'])==1 and ee[0]['Attempts']==1
try:simulate(dict(s,external_actions_enabled=True),rows)
except ValueError:pass
else:raise AssertionError('External action guard missing')
print('PASS: normal, temporary recovery, persistent stop, bounded delays, in-memory draft/error agreement, permission stop, ambiguous timeout stop, external action guard')
