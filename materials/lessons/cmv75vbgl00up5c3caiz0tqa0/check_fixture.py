from pathlib import Path
import csv
p=Path(__file__).resolve().parent
before={r['Field']:r for r in csv.DictReader((p/'handoff-before.csv').open())}
after={r['Field']:r for r in csv.DictReader((p/'handoff-after.csv').open())}
assert before['Date']['Source value']=='' and before['Date']['Action']=='STOP'
assert before['Contact permission']['Action']=='OMIT AND ASK'
assert after['Date']['Source value']=='18 November 2026'
assert after['Contact permission']['Action']=='Omit'
for field in ['Event name','Time','Venue','Capacity','Audience']:
 assert before[field]['Source value']==after[field]['Source value'],field
slide=(p/'checked-slide-content.md').read_text().split('<!--')[0]
assert slide.splitlines()==['# Riverside Skills Workshop','Smartphone photography for adult beginners','18 November 2026','10:00–12:00','Community Room B','Capacity: 24','']
print('PASS: fixture consistency only; final editor/export still requires human inspection.')
