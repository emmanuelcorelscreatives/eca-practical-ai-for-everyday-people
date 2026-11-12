from pathlib import Path
from decimal import Decimal as D
import csv,json,zipfile,xml.etree.ElementTree as E
p=Path(__file__).parent;d=json.loads((p/'expected-results.json').read_text())
for name,key,n in [('original-five.csv','five',5),('range-check-six.csv','six',6),('comparison-seven.csv','seven',7)]:
 rows=list(csv.DictReader((p/name).open(newline='')));assert len(rows)==n;assert sum((D(r['Amount']) for r in rows),D(0))==D(d[key]['total'])
assert sum(map(D,d['seven']['groups'].values()),D(0))==D('730.00')
assert d['six']['lastRow']==7 and d['six']['unassignedAmount']=='35.00'
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
for name,formula,total in [('Original-do-not-edit.xlsx',None,None),('Working-Copy-practice.xlsx','SUM(D2:D6)','615.00'),('Range-check-six.xlsx','SUM(D2:D7)','650.00'),('Independent-comparison-seven.xlsx','SUM(D3:D9)','730.00')]:
 with zipfile.ZipFile(p/name) as z:
  assert z.testzip() is None
  for n in z.namelist():E.fromstring(z.read(n))
  t=E.fromstring(z.read('xl/worksheets/sheet1.xml'));fs=t.findall('.//s:f',ns)
  if formula:
   assert len(fs)==1 and fs[0].text==formula
   cell=next(c for c in t.findall('.//s:c',ns) if c.find('s:f',ns) is not None);assert D(cell.find('s:v',ns).text)==D(total)
  else:assert not fs
print('PASS fictional CSV counts/arithmetic, group reconciliation and actual XLSX XML/CRC/formula ranges; no named-app or learner-copy observation claim')

for name,csvname,offset,n in [('Original-do-not-edit.xlsx','original-five.csv',2,5),('Working-Copy-practice.xlsx','original-five.csv',2,5),('Range-check-six.xlsx','range-check-six.csv',2,6),('Independent-comparison-seven.xlsx','comparison-seven.csv',3,7)]:
 with zipfile.ZipFile(p/name) as z:
  t=E.fromstring(z.read('xl/worksheets/sheet1.xml'));amounts={c.attrib['r']:c.find('s:v',ns).text for c in t.findall('.//s:c',ns) if c.find('s:v',ns) is not None}
  rows=list(csv.DictReader((p/csvname).open(newline='')))
  assert [D(amounts['D'+str(i+offset)]) for i in range(n)]==[D(r['Amount']) for r in rows]
print('PASS all actual workbook Amount cells equal their CSV fixture and cached formula totals equal independent Decimal sums')

for name,csvname,offset,n in [('Original-do-not-edit.xlsx','original-five.csv',2,5),('Working-Copy-practice.xlsx','original-five.csv',2,5),('Range-check-six.xlsx','range-check-six.csv',2,6),('Independent-comparison-seven.xlsx','comparison-seven.csv',3,7)]:
 with zipfile.ZipFile(p/name) as z:
  root=E.fromstring(z.read('xl/worksheets/sheet1.xml'));cells={c.attrib['r']:c for c in root.findall('.//s:c',ns)}
  data_rows=sorted(int(ref[1:]) for ref,c in cells.items() if ref.startswith('D') and c.find('s:v',ns) is not None and c.find('s:f',ns) is None)
  assert data_rows==list(range(offset,offset+n))
  rows=list(csv.DictReader((p/csvname).open(newline='')))
  for i,r in enumerate(rows,offset):
   for col,key in [('A','Item'),('B','Category')]:assert ''.join(cells[col+str(i)].itertext())==r[key]
   for col,key in [('C','Quantity'),('D','Amount')]:assert D(cells[col+str(i)].find('s:v',ns).text)==D(r[key])
groups={}
for r in csv.DictReader((p/'comparison-seven.csv').open(newline='')):
 key=r['Category'].strip() or 'Unassigned';groups[key]=groups.get(key,D(0))+D(r['Amount'])
assert groups=={k:D(v) for k,v in d['seven']['groups'].items()}
print('PASS exact workbook record counts and Item/Category/Quantity/Amount semantics, plus independently source-derived category memberships/totals')
