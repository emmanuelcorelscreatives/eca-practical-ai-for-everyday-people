#!/usr/bin/env python3
"""Offline, self-authored Academy practice workflow. No network or sending."""
import argparse,json
from pathlib import Path

RUN='RUN-205-017'
STAMP='2026-10-15T10:00:00Z' # fixed fictional exercise time, not a live capture timestamp

def read(p): return json.loads(Path(p).read_text())
def write(p,value): Path(p).write_text(json.dumps(value,indent=2)+'\n')
def initial(): return {'request_log':[],'drafts':[],'runs':[],'sent':[]}
def run(state,form,faulty_category_mapping=False):
    # Deliberately no duplicate protection: inspect before replaying.
    row={'spreadsheet_row':18+len(state['request_log']),**form}
    if faulty_category_mapping: row['category']='Sports'
    state['request_log'].append(row)
    steps=[{'step':1,'name':'Form submission','status':'Completed','input':dict(form)},
           {'step':2,'name':'Add row to Request Log','status':'Completed','input':dict(form),'output':{'created_row':row['spreadsheet_row']}}]
    if not form.get('event_details','').strip():
        steps.append({'step':3,'name':'Generate review draft','status':'Failed','input':{'event_details':''},'error':'Required event details are missing','output':None})
        status='Failed'
    else:
        draft={'test_input_id':form['test_input_id'],'event':form['event'],'details':form['event_details'],'category':row['category'],'status':'For review — not sent'}
        state['drafts'].append(draft);steps.append({'step':3,'name':'Generate review draft','status':'Completed','output':dict(draft)});status='Successful'
    receipt={'run_id':RUN,'time':STAMP,'fictional':True,'status':status,'steps':steps}
    state['runs'].append(receipt);return receipt

def recover(state,detail):
    matches=[r for r in state['request_log'] if r['test_input_id']==detail['test_input_id']]
    if len(matches)!=1: raise ValueError('Expected exactly one existing record; inspect duplicates before recovery')
    if detail.get('authorized_for_practice') is not True or not detail.get('event_details','').strip(): raise ValueError('Authorized supplied details required')
    row=matches[0]
    if any(d['test_input_id']==row['test_input_id'] for d in state['drafts']): raise ValueError('Existing draft found; inspect instead of creating another')
    draft={'test_input_id':row['test_input_id'],'event':row['event'],'contact':row['contact'],'details':detail['event_details'],'source_row':row['spreadsheet_row'],'status':'For review — not sent','manual':True,'checked':False}
    row['event_details']=detail['event_details'];state['drafts'].append(draft)
    return {'decision':'Preserve row 18; finish draft manually','disposition':'Manual draft created; awaiting checking; not sent','original_run_status':state['runs'][0]['status']}

def confirm_check(state):
    if len(state['drafts'])!=1:raise ValueError('Expected one draft for comparison')
    draft=state['drafts'][0];rows=[r for r in state['request_log'] if r['test_input_id']==draft['test_input_id']]
    if len(rows)!=1:raise ValueError('Expected one matching source row')
    row=rows[0]
    if any(draft[k]!=row[j] for k,j in [('event','event'),('contact','contact'),('details','event_details'),('source_row','spreadsheet_row')]):raise ValueError('Draft differs from source; correct and inspect')
    if draft['status']!='For review — not sent' or state['sent']:raise ValueError('Draft must remain unsent')
    draft['checked']=True
    return {'disposition':'Manual draft created and checked; not sent','comparison':'identifier, event, contact, details, source row and unsent status match saved source'}

def main():
    a=argparse.ArgumentParser(description=__doc__);a.add_argument('action',choices=['reset','run','inspect','recover','check']);a.add_argument('--state',default='practice-state.json');a.add_argument('--input',default='test-input.json');a.add_argument('--detail',default='authorized-practice-detail.json');args=a.parse_args()
    if args.action=='reset':state=initial();result={'state':'reset','fictional':True}
    else:
        state=read(args.state)
        if args.action=='run': result=run(state,read(args.input))
        elif args.action=='recover':result=recover(state,read(args.detail))
        elif args.action=='check':result=confirm_check(state)
        else:result=state
    if args.action!='inspect':write(args.state,state)
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
