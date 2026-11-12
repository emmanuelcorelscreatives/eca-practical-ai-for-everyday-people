"""Offline deterministic exercise only: no network, file writes, AI or external action."""
import json
from pathlib import Path
REQUIRED = ('event_name','date','start_time','end_time','venue','audience','contact','approved_facts')
def evaluate(case):
    result = dict(case=case['case'], case_id=case['case_id'], draft_created=False, final_created=False)
    if case.get('request') != 'event_information_sheet':
        return dict(result, status='Outside scope', owner='Authorized reviewer', response='Explain boundary; retain request; redirect to appropriate qualified local provider', recovery='Authorized review or supported task')
    sources = case.get('sources', [])
    missing = [field for field in REQUIRED if not sources or any(not source.get('fields', {}).get(field) for source in sources)]
    if missing:
        return dict(result,status='Incomplete',owner='Request owner',missing=missing,response='Ask for missing fields: '+', '.join(missing),recovery='Return to complete input check after clarification')
    conflicts = {field:[{'source':source['name'],'value':source['fields'][field]} for source in sources] for field in REQUIRED if len({source['fields'][field] for source in sources}) > 1}
    if conflicts:
        return dict(result,status='Unresolved conflict',owner='Event coordinator',conflicts=conflicts,response='Preserve every value/source; ask coordinator; no finished sheet',recovery='Authorized decision then complete input check')
    if case.get('technical_failure'):
        if not case.get('prior_outcome_checked'):
            return dict(result,status='Prior outcome unknown',owner='Workflow operator',response='Check prior action before retry',recovery='Verify whether draft already exists')
        if case.get('later_retries',0) < 1:
            return dict(result,status='One later retry allowed',owner='Workflow operator',response='Record interruption and retry at most once',recovery='Retry once or manual fallback')
        return dict(result,status='Manual fallback; awaiting human review',owner='Workflow operator',response='Use same template with verified facts; compare each field',recovery='Human review of manual draft')
    return dict(result,status='Awaiting human review',owner='Human reviewer',draft_created=True,draft=sources[0]['fields'].copy(),response='Compare draft against opened source; no publishing',recovery='Separate human review')
if __name__ == '__main__':
    for case in json.loads(Path(__file__).with_name('cases.json').read_text()):
        print(json.dumps(evaluate(case),sort_keys=True))
