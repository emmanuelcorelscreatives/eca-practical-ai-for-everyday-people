#!/usr/bin/env python3
"""Offline training simulation. No network, real waiting, sending, or paid requests."""
import csv,json,argparse
from pathlib import Path
from datetime import datetime,timedelta
ROOT=Path(__file__).resolve().parent
ERROR_FIELDS=['Run or Input ID','Time','Failed Step','Attempts','Plain-language Error','Input Reference','Status','Suggested Manual Action']
def simulate(settings, rows):
    timeout=settings['timeout_seconds']; maximum=settings['maximum_total_attempts']; delays=settings['delays_before_retries_seconds']
    if not isinstance(maximum,int) or maximum<1 or maximum>10: raise ValueError('Set a finite total attempt count from 1 to 10')
    if timeout<=0 or len(delays)<maximum-1 or any(d<0 for d in delays): raise ValueError('Use a positive timeout and a nonnegative delay for each retry')
    if settings['external_actions_enabled']: raise ValueError('External actions must stay disabled')
    histories=[];errors=[];drafts={};now=datetime.fromisoformat(settings['fictional_start_time'])
    for row in rows:
        ident=row['Input ID']; scenario=row['Scenario']; ref=row['Safe input reference']; attempts=[];elapsed=0
        if ident in drafts: raise ValueError('Duplicate input identifier')
        if scenario not in ['Normal','Temporary failure','Persistent failure','Missing permission','Timeout']: raise ValueError('Unknown simulation scenario')
        for number in range(1,maximum+1):
            wait=0 if number==1 else delays[number-2];elapsed+=wait
            success=scenario=='Normal' or (scenario=='Temporary failure' and number==2)
            duration=8 if scenario=='Normal' else (9 if success else (timeout if scenario=='Timeout' else 2))
            timed_out=duration>timeout or scenario=='Timeout'
            if timed_out: duration=timeout;success=False
            elapsed+=duration
            message='' if success else ('Missing permission' if scenario=='Missing permission' else ('Timeout: no confirmation; inspect destination before repeating' if timed_out else 'Service temporarily unavailable'))
            attempts.append({'attempt':number,'step':'Create draft','outcome':'Completed' if success else 'Failed','simulated_duration_seconds':duration,'simulated_wait_before_seconds':wait,'error':message})
            if success:
                drafts[ident]=f'{ident}\nFor review\nFictional draft for {ref}. External actions disabled.\n'; break
            # Access failures and ambiguous confirmations must be routed to a human, not blindly repeated.
            if scenario in ['Missing permission','Timeout'] or timed_out: break
        completed=ident in drafts
        if not completed:
            error='Service unavailable after three attempts' if len(attempts)==3 and scenario=='Persistent failure' else attempts[-1]['error']
            errors.append(dict(zip(ERROR_FIELDS,[ident,(now+timedelta(seconds=elapsed)).isoformat(),'Create draft',len(attempts),error,ref,'Needs human review','Check service access; then create draft manually if appropriate'])))
        histories.append({'input_id':ident,'scenario':scenario,'safe_reference':ref,'status':'Completed' if completed else 'Stopped after maximum attempts' if len(attempts)==maximum else 'Stopped for human review','attempts':attempts,'save_for_review':'Completed' if completed else 'Not run','simulated_elapsed_seconds':elapsed,'simulation':True})
    return histories,errors,drafts

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',default='generated');a=p.parse_args()
    settings=json.loads((ROOT/'settings.json').read_text());rows=list(csv.DictReader((ROOT/'inputs.csv').open()))
    histories,errors,drafts=simulate(settings,rows);out=Path(a.out).resolve()
    # Refuse existing output to prevent stale drafts falsely supporting an observation.
    out.mkdir(exist_ok=False);(out/'Review Drafts').mkdir()
    (out/'run-history.json').write_text(json.dumps(histories,indent=2)+'\n')
    with (out/'Error Log.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=ERROR_FIELDS);w.writeheader();w.writerows(errors)
    for ident,text in drafts.items():(out/'Review Drafts'/f'{ident}-draft.txt').write_text(text)
    with (out/'Test Summary.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['Input ID','Expected training result','Observed simulator result','Evidence type'])
        for h in histories:w.writerow([h['input_id'],{'Normal':'Success on attempt 1','Temporary failure':'Recovery on attempt 2','Persistent failure':'Stop after attempt 3'}[h['scenario']],h['status'],'Executed offline simulation; not a real service observation'])
    print(json.dumps({'simulation':True,'histories':len(histories),'drafts':len(drafts),'error_rows':len(errors),'output':str(out)}))
if __name__=='__main__':main()
