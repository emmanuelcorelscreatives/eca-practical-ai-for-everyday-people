"""Checks fictional fixtures only; never calls an app or AI service."""
import csv,json,pathlib
p=pathlib.Path(__file__).resolve().parent
r=json.loads((p/'fictional-records.json').read_text())
e=json.loads((p/'expected-checks.json').read_text())
f=json.loads((p/'simulation-fixtures.json').read_text())
with (p/'fictional-records.csv').open(newline='') as h:
 assert list(csv.DictReader(h))==r
assert len(r)==len(e)==len(f)==2
assert r[0]['source_id']=='TEST-197-001' and r[1]['source_id']=='TEST-197-002'
assert r[0]['event_date']=='22 October 2026' and r[0]['location']=='Cedar Room'
assert r[0]['notes']=='Bring closed-toe shoes'
assert r[1]['event_title']=='Seed Swap Table' and r[1]['notes']=='Label seed packets'
assert [k for k,v in r[1].items() if not v]==['event_date','location','accessibility']
for a,b,c in zip(r,e,f):
 assert b['source_id']==c['source_id']==a['source_id']
 assert b['preserve']=={k:v for k,v in a.items() if v}
 assert b['unresolved']==[k for k,v in a.items() if not v]
 assert b['real_trigger']=='OFF' and b['external_action_performed'] is False
 assert c['step_1_received']==c['step_2_input']==a
 assert c['proposed_draft']['draft_title']==a['event_title']
 assert c['proposed_draft']['safety_note']==a['notes']
 assert c['external_action_status']=='NOT RUN; proposed row only'
 assert 'HUMAN-AUTHORED' in c['provenance']
 assert 'Accessibility requirements not provided' in c['proposed_draft']['missing_information']
assert 'Event date not provided' in f[1]['proposed_draft']['missing_information']
assert 'Location not provided' in f[1]['proposed_draft']['missing_information']
assert '22 October 2026' not in f[1]['proposed_draft']['draft_summary']
assert 'Cedar Room' not in f[1]['proposed_draft']['draft_summary']
print('PASS: 2 fictional inputs, expected gaps and manual fixtures; no external action performed.')
