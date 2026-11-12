from pathlib import Path
import csv,re,wave,json,hashlib
p=Path(__file__).parent
notes=(p/'event-notes.txt').read_text(); draft=(p/'chat-draft.txt').read_text().splitlines()[1]
assert len(draft.split())==80
for f in ['Willow Park Book Swap','24 October 2026','14:00','Hall B']: assert f.lower() in draft.lower() and f.lower() in notes.lower()
assert 'Entry is free.' in draft and 'free entry' in notes
passage='Volunteers may enter Hall B from 13:15 through the east entrance.'
for f in ['event-brief.html','room-rules.html']: assert passage in (p/'source-pack'/f).read_text()
assert 'id="page-2"' in (p/'source-pack/event-brief.html').read_text()
assert 'Organizer contact: missing' in (p/'handout-reviewed.html').read_text()
a=(p/'media-source-transcript.txt').read_text(); b=(p/'media-edited-transcript.txt').read_text(); phrase='Welcome to the Willow Park Book Swap.'
assert a.count(phrase)==2 and b.count(phrase)==1
assert a.replace(phrase+' ', '', 1)==b
assert 'Hall D' in (p/'caption-draft-deliberate-error.txt').read_text() and 'Hall B' in (p/'caption-corrected.txt').read_text()
row=list(csv.DictReader((p/'transport-evidence-log.csv').open()))[0]
assert row['status']=='UNRESOLVED' and not row['official_url'] and not row['confirmed_detail']
provenance=json.loads((p/'audio-provenance.json').read_text()); raw=(p/'practice-recording.wav').read_bytes();assert hashlib.sha256(raw).hexdigest()==provenance['sha256']
with wave.open(str(p/'practice-recording.wav')) as w: assert w.getnframes()>0 and w.getnchannels()==1
print('PASS: source fixtures, 80-word draft, exact volunteer anchors, blank transport evidence, preserved transcript edit and audio integrity. No arbitrary model output or real timetable verified.')
