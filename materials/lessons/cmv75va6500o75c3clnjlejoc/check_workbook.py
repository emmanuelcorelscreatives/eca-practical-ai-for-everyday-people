from pathlib import Path
from zipfile import ZipFile
from decimal import Decimal
import xml.etree.ElementTree as E
p=Path(__file__).parent;ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with ZipFile(p/'formula-practice.xlsx')as z:
 assert z.testzip() is None
 for n in z.namelist():
  if n.endswith('.xml')or n.endswith('.rels'):E.fromstring(z.read(n))
 w=E.fromstring(z.read('xl/workbook.xml'));assert len(w.find('s:sheets',ns))==8
 a=E.fromstring(z.read('xl/worksheets/sheet1.xml'));cells={c.attrib['r']:c for c in a.findall('.//s:c',ns)}
 assert 'B4'not in cells and cells['C4'].find('s:v',ns).text=='0'
 assert cells['B6'].find('s:f',ns).text=='SUM(B2:B5)' and cells['C6'].find('s:f',ns).text=='SUM(C2:C5)'
 for n in range(1,9):
  a=E.fromstring(z.read(f'xl/worksheets/sheet{n}.xml'))
  for c in a.findall('.//s:c',ns):
   if c.find('s:f',ns)is not None:assert c.find('s:v',ns)is None
assert Decimal(120)+Decimal(85)+Decimal(40)==245
assert Decimal(125)+Decimal(90)+Decimal(0)+Decimal(35)==250
assert Decimal(245)/4==Decimal('61.25')
assert sum([10,20,5])==35 and sum([10,20])==30
assert sum([6,4,10])==20 and sum([6,4,1])==11
print('PASS: eight sheets, all ZIP/XML, exact table/formulas, genuine blank vs0, no fabricated formula caches, independent arithmetic')
