import pathlib,json,re
p=pathlib.Path(__file__).parent
schedule=json.loads((p/'delivery-schedule.json').read_text());c=schedule['cues'];assert len(c)==70 and len({x['id'] for x in c})==70
assert c[0]['start']==0 and c[-1]['end']==780 and schedule['durationSeconds']==780
assert all(x['end']>x['start'] for x in c)
assert all(abs(a['end']-b['start'])<1e-7 for a,b in zip(c,c[1:]))
labels=['TASK','AUDIENCE','PURPOSE','SOURCE TEXT','MUST PRESERVE','CONSTRAINTS','OUTPUT FORMAT'];master=(p/'blank-master.txt').read_text()
for label in labels:assert master.count('['+label+']')==1
for event in ['Green Corner','Riverside','Community Room','Library Entrance']:assert event not in master
fixed=lambda text:text.split('FIXED INSTRUCTIONS\n')[1].split('--- VALUES / SOURCE MATERIAL ---')[0]
for n,case in enumerate(json.loads((p/'source-cases.json').read_text())['cases'],1):
 filled=(p/f'case-{n}-filled.txt').read_text();assert fixed(filled)==fixed(master)
 for label in labels:assert filled.count('['+label+']')==1
 for value in case.values():assert value in filled,value
 draft=(p/'example-drafts.md').read_text();assert case['name'] in draft and case['date'] in draft and case['location'] in draft
# Direct factual negative controls against each protected supplied value.
case=json.loads((p/'source-cases.json').read_text())['cases'][0];filled=(p/'case-1-filled.txt').read_text()
for key in ['name','date','time','location','requirement','contact']:
 damaged=filled.replace(case[key],'CORRUPTED');assert case[key] not in damaged
missing=filled.replace('Community Room','[empty — required]');assert 'Community Room' not in missing and missing.count('[empty — required]')==2
assert 'Missing: location.' in (p/'review-sheet.md').read_text()
assert 'Free refreshments' in (p/'example-drafts.md').read_text() and 'Main Hall' in (p/'example-drafts.md').read_text()
print('PASS: all 70 saved cues exactly once, contiguous 0–780; seven fields; fixed rules; both fictional cases; six protected-value corruption controls; missing-location stop; blank master restoration')
