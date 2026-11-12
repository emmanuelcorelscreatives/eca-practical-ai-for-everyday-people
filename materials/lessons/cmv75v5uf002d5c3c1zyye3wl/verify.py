"""Offline kit checks; no requests or credentials."""
import json,zipfile,hashlib
from pathlib import Path
p=Path(__file__).parent
d=json.loads((p/'garden-schedule.json').read_text())
assert [(x['event'],x['date']) for x in d['events']]==[('Seed swap','2026-04-11'),('Planting session','2026-04-18'),('Compost workshop','2026-04-25')]
with zipfile.ZipFile(p/d['document']) as z:
 assert z.testzip() is None
 text=z.read('word/document.xml').decode()
 for x in d['events']:assert x['date'] in text and x['event'] in text
 assert 'Lunch is provided' not in text
s=(p/'permission-simulator.html').read_text()
for forbidden in ['fetch(', 'XMLHttpRequest', 'WebSocket(', 'sendBeacon(', 'https://', 'http://', 'document.cookie', 'localStorage']:assert forbidden not in s,forbidden
for required in ['No real accounts','View selected file','Cannot edit, send, publish, or delete','No source changes or external actions','Future account access stopped','Previously created drafts and information already received may remain.','Missing from source — remove or confirm']:assert required in s,required
for x in d['events']:assert x['date'] in s
print(json.dumps({'state':'PASS','sourceDates':3,'docxCRC':'PASS','networkCalls':0,'note':'Static content checks; browser flow evidence is recorded separately.'},indent=2))
