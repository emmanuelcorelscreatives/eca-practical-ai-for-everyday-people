from pathlib import Path
import csv
root=Path(__file__).resolve().parent
with (root/'reading-day-attendance.csv').open(newline='') as f:
 reader=csv.DictReader(f); assert reader.fieldnames==['Session','Room','Attendees']; rows=list(reader)
assert len(rows)==4
assert [int(r['Attendees']) for r in rows]==[18,22,17,23]
assert sum(int(r['Attendees']) for r in rows)==80
with (root/'additional-attendance.csv').open(newline='') as f: extra=list(csv.DictReader(f))
assert len(extra)==1 and int(extra[0]['Attendees'])==9
assert sum(int(r['Attendees']) for r in rows+extra)==89
source=(root/'riverside-reading-day.txt').read_text()
assert 'Lantern table' in source and 'Venue: Not decided.' in source
assert '24 people' not in source
assert '24 people' in (root/'room-notes-cedar.txt').read_text()
print('PASS: four records=80; expanded five=89; Cedar capacity absent from current document and present only in separate sample.')
