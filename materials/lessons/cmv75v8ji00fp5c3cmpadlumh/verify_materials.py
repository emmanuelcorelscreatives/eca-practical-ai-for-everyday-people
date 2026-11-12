from pathlib import Path
import csv,datetime
p=Path(__file__).parent
assert datetime.date(2026,10,17).strftime('%A')=='Saturday'
assert datetime.date(2026,10,15).strftime('%A')=='Thursday'
rows=list(csv.DictReader(open(p/'detail-checklist.csv',encoding='utf8')))
assert len(rows)==9 and len({r['detail'] for r in rows})==9
for name in ['explanation-es-draft.md','accessible-summary-es-draft.md']:
 text=(p/name).read_text()
 for term in ['17 de octubre de 2026','9:45','10:00','delantal','zapatos cerrados','organizador','frutos secos','dieciséis','15 de octubre de 2026','a más tardar']:
  assert term in text,(name,term)
 assert 'BORRADOR SIN REVISAR' in text
activity=(p/'practice-activity.md').read_text()
assert all(('\n'+str(i)+'. ')in activity for i in range(1,5))
gloss=list(csv.DictReader(open(p/'glossary.csv',encoding='utf8')))
assert next(r for r in gloss if r['english']=='nuts')['status'].startswith('UNRESOLVED')
assert 'before Thursday' in (p/'correction-log.md').read_text()
for f,status in [('review-record.csv','NOT REVIEWED'),('listening-record.csv','NOT TESTED')]:
 assert all(r['status']==status for r in csv.DictReader(open(p/f,encoding='utf8')))
print('PASS: 9 protected source details, 2 dates, 4 situations, draft/uncertainty flags and unclaimed review/listening records. Translation and audio quality require actual human checks.')
