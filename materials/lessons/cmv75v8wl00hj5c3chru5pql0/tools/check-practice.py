from pathlib import Path
from decimal import Decimal
import csv,json,hashlib,xml.etree.ElementTree as E
p=Path(__file__).resolve().parents[1];pdf=(p/'original-scan.pdf').read_bytes();assert pdf.count(b'/Subtype /Image')==3;assert b'/Font' not in pdf
rows=list(csv.DictReader((p/'answers/correction-log.csv').open()));r={x['region_or_field']:x for x in rows};assert r['Paper rate']['source_value']=='3.50';assert r['Folders units']['source_value']=='8';assert r['Optional field']['status']=='uncertain';assert r['Approved adjustment']['source_value']=='-3.50';assert r['Two-column notes A and B']['source_value']=='A left, then B right';assert r['Reference line punctuation']['source_value'].endswith('.');assert r['Adjustment line punctuation']['source_value'].endswith('.')
ns={'s':'http://www.w3.org/2000/svg'};root=E.fromstring((p/'source/page-3.svg').read_text());table=root.find('.//s:g[@id="source-table"]',ns);cells=table.findall('s:text',ns);assert len(cells)==9
for row in range(3):assert [int(c.attrib['x']) for c in cells[row*3:row*3+3]]==[100,650,920];assert len({c.attrib['y'] for c in cells[row*3:row*3+3]})==1
root2=E.fromstring((p/'source/page-2.svg').read_text());notes=[c for c in root2.findall('.//s:text',ns) if (c.text or '').startswith('Two-column note')];assert [c.attrib['x'] for c in notes]==['100','660'];assert notes[0].attrib['y']==notes[1].attrib['y']
total=Decimal('12')*Decimal('3.50')+Decimal('8')*Decimal('4.00');assert total==Decimal('74.00');print(json.dumps({'state':'PASS','pages':3,'imageOnly':True,'originalSha256':hashlib.sha256(pdf).hexdigest(),'checkedReferenceRows':len(rows),'positionedTableColumns':True,'trueTwoColumnNotes':True,'separateCalculatedTotal':str(total),'doesNotCertifyLearnerLogOrFullVisualFidelity':True}))
