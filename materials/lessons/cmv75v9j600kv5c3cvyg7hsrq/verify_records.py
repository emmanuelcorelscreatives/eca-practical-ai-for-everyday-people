"""Validate these self-authored Academy fixtures; not arbitrary user documents."""
from pathlib import Path
import json,csv,copy,re
ROOT=Path(__file__).parent
PAGES=json.loads((ROOT/'source-pages.json').read_text())
SOURCE=' '.join(' '.join(p['lines']) for p in PAGES)
COND='Please respond by 23 October 2026 only if your telephone number, email address, or preferred contact method has changed.'
NOCHANGE='If nothing has changed, no response is required.'
PROHIB='Do not email identity documents.'
GAP='The notice does not state whether previous email addresses should be repeated when only a telephone number changed.'
def validate(rows):
    if len(rows)!=2:return False
    for i,row in enumerate(rows):
        if row['document_date']!='6 October 2026' or row['source_file']!='Maple-Court-Notice.pdf':return False
        if row['alternative']!='Online updates remain available' or row['contact']!='records@example.org':return False
        if row['prohibition_quote']!=PROHIB or PROHIB not in SOURCE:return False
        if 'do not email identity documents' not in row['exception_or_condition']:return False
        prov=json.loads(row['field_source_pages'])
        if prov['alternative']!=[2] or prov['contact']!=[2] or prov['prohibition_quote']!=[2]:return False
        if row['source_pages']!='1;2':return False
        if i==0:
            if (row['event_or_deadline'],row['action'],row['who_acts'])!=('23 October 2026','Send updated contact details','People whose listed details changed'):return False
            if row['condition_quote']!=COND or row['no_change_quote']!=NOCHANGE or row['unresolved_question']!=GAP:return False
            if row['verification_status']!='Verified against pages 1–2' or prov['event_or_deadline']!=[1]:return False
        else:
            if (row['event_or_deadline'],row['action'],row['who_acts'])!=('19 October 2026, 10:00–12:00','None stated','None stated'):return False
            if row['verification_status']!='Verified against page 2' or prov['event_or_deadline']!=[2]:return False
    return COND in SOURCE and NOCHANGE in SOURCE and 'The reception desk will be unavailable during this maintenance period.' in SOURCE
if __name__=='__main__':
    rows=json.loads((ROOT/'checked-records.json').read_text());assert validate(rows)
    with (ROOT/'checked-register.csv').open(newline='') as f:assert validate(list(csv.DictReader(f)))
    bad=json.loads((ROOT/'unchecked-extraction.json').read_text());assert not validate(bad['rows']);assert all('UNVERIFIED' in r['verification_status'] for r in bad['rows'])
    cases=[(0,'event_or_deadline','28 October 2026'),(0,'who_acts','All residents'),(0,'condition_quote',''),(0,'no_change_quote',''),(0,'prohibition_quote',''),(0,'alternative','Unavailable'),(0,'contact','invented@example.org'),(0,'unresolved_question','No gap'),(1,'event_or_deadline','19 October 2026, 10:00–17:00')]
    for i,key,val in cases:
        changed=copy.deepcopy(rows);changed[i][key]=val;assert not validate(changed),(i,key)
    wrong=copy.deepcopy(rows);p=json.loads(wrong[0]['field_source_pages']);p['contact']=[1];wrong[0]['field_source_pages']=json.dumps(p);assert not validate(wrong)
    summary=(ROOT/'checked-summary.txt').read_text()
    for clause in ['23 October 2026 only when they have changed','No response is required when nothing changed','10:00 to 12:00 on 19 October 2026','online updates remain available','Do not email identity documents']:assert clause in summary
    assert len(PAGES)==2
    print('PASS: coherent source/JSON/CSV/summary, exact conditions and page provenance; unchecked status; ten date/actor/condition/prohibition/contact/gap/provenance corruptions rejected.')
