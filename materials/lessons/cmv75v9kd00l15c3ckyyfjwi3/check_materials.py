from pathlib import Path
import json,csv,datetime
from decimal import Decimal
p=Path(__file__).parent
f=json.loads((p/'receipt-facts.json').read_text()); rows=list(csv.DictReader((p/'register-checked.csv').open())); c=list(csv.DictReader((p/'register-candidate.csv').open()))
assert len(rows)==3 and len(c)==3
assert Decimal('24.00')+Decimal('2.40')==Decimal('26.40')
for r,z in zip(rows,f['receipts']):
 assert r['Source file']==z['source'];assert r['Date as printed']==z['date'];assert r['Normalized date']==z['normalized'];assert Decimal(r['Total'])==Decimal(z['total']);assert r['Currency']==z['currency'];datetime.date.fromisoformat(r['Normalized date'])
assert c[0]['Total']=='13.30' and c[1]['Total']=='24.00'
assert c[2]['Date as printed']=='' and c[2]['Normalized date']=='' and c[2]['Verification status']=='Needs review'
print('PASS source facts, separate currencies, all dates, subtotal arithmetic and staged uncertainty')
missing=[z['source'] for z in f['receipts'] if not (p/z['source']).is_file()]
if missing:raise SystemExit('DRAFT: final JPG originals not yet produced: '+', '.join(missing))
print('PASS final JPG originals present')
