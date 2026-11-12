#!/usr/bin/env python3
"""Exercise checks run in memory; no external actions or learner state changes."""
import json
from pathlib import Path
from workflow import initial,run,recover,confirm_check
from copy import deepcopy
p=Path(__file__).parent
form=json.loads((p/'test-input.json').read_text());detail=json.loads((p/'authorized-practice-detail.json').read_text())
s=initial();r=run(s,form)
assert r['status']=='Failed'
assert [x['status'] for x in r['steps']]==['Completed','Completed','Failed']
assert len(s['request_log'])==1 and s['request_log'][0]['spreadsheet_row']==18
assert s['request_log'][0]['event_details']=='' and s['drafts']==[]
result=recover(s,detail)
assert len(s['request_log'])==1 and len(s['drafts'])==1
assert s['drafts'][0]['details']=='discussion begins at 18:00'
assert s['drafts'][0]['source_row']==18 and s['sent']==[]
assert s['drafts'][0]['checked'] is False
assert 'awaiting checking' in result['disposition']
confirm_check(s);assert s['drafts'][0]['checked'] is True
assert s['drafts'][0]['test_input_id']==form['test_input_id']
assert s['drafts'][0]['event']==form['event'] and s['drafts'][0]['contact']==form['contact']
assert r['steps'][0]['input']['event_details']=='' and r['steps'][1]['input']['event_details']==''
assert r['status']=='Failed' and result['original_run_status']=='Failed'
try:recover(s,detail)
except ValueError:pass
else:raise AssertionError('Duplicate manual draft was permitted')
# Independent scratch example: unsafe whole-run replay really creates two rows.
t=initial();run(t,form);run(t,form);assert len(t['request_log'])==2 and len(t['drafts'])==0
# Successful operations do not ensure a correct mapped category.
u=initial();correct={**form,'event_details':detail['event_details']}
assert run(u,correct,faulty_category_mapping=True)['status']=='Successful'
assert correct['category']=='Community discussion'
assert u['request_log'][0]['category']=='Sports' and u['drafts'][0]['category']=='Sports'
assert u['drafts'][0]['category']!=correct['category']
# Rejected recovery is atomic: no row edit or draft creation.
for kind in ['unauthorized','blank','missing','duplicate','existing-draft']:
 v=initial();run(v,form);d=deepcopy(detail)
 if kind=='unauthorized':d['authorized_for_practice']=False
 elif kind=='blank':d['event_details']='  '
 elif kind=='missing':v['request_log']=[]
 elif kind=='duplicate':v['request_log'].append(deepcopy(v['request_log'][0]))
 elif kind=='existing-draft':recover(v,d)
 before=deepcopy(v)
 try:recover(v,d)
 except ValueError:pass
 else:raise AssertionError('Invalid recovery accepted: '+kind)
 assert v==before,kind
# Incorrect edited draft must not acquire a checked claim.
w=initial();run(w,form);recover(w,detail);w['drafts'][0]['contact']='Wrong name';before=deepcopy(w)
try:confirm_check(w)
except ValueError:pass
else:raise AssertionError('Mismatched draft marked checked')
assert w==before
print('PASS: partial failure, row 18, no draft, scoped manual recovery, unsent output, retained failure status, duplicate hazard and wrong-category success')
