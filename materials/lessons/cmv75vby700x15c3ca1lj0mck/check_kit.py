import json,pathlib,datetime,csv,xml.etree.ElementTree as ET
p=pathlib.Path(__file__).resolve().parent
b=json.loads((p/'event-brief.json').read_text()); a=json.loads((p/'approval-request-v1.json').read_text())
assert datetime.date.fromisoformat(b['date']).strftime('%A')==b['day']
assert b['fictional'] and a['fictional'] and b['publicPostingEnabled'] is False
assert b['accessibilityDetails'] is None and b['contactMethod'] is None
assert a['decision'] is None and a['decisionTime'] is None and a['externalAction']=='Disabled'
assert not a['reviewerAuthorityConfirmed'] and len(a['missingInformation'])==2
cfg=json.loads((p/'test-destination-action-config.json').read_text());assert cfg['destinationId']==a['destination']['id'] and cfg['publishingEnabled'] is False and cfg['externalConnection'] is None
assert a['destination']==b['destination'] and a['destination']['visibility']=='Non-public test'
assert '24 October 2026' in a['body'] and b['time'] in a['body'] and b['location'] in a['body']
assert all(x.lower() in a['body'].lower() for x in b['activities'])
assert all((p/x).is_file() for x in a['supportingRecords']+[a['attachment']])
ET.parse(p/'garden-open-day-banner-v1.svg');assert (p/a['attachment']).read_bytes()[:8]==bytes([137,80,78,71,13,10,26,10])
r=list(csv.DictReader((p/'review-register.csv').open()))[0]
assert r['Decision']==r['Decision time']=='' and r['External action']=='Disabled'
html=(p/'approval-practice.html').read_text();assert 'fetch(' not in html and 'XMLHttpRequest' not in html
print('PASS: fictional event chronology, exact draft facts, complete linked records, unresolved gaps, empty decision, disabled external action, no network code')
