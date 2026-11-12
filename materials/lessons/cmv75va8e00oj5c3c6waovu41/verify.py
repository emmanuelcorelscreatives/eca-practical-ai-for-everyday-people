"""Local structural/arithmetic checks; does not prove spreadsheet/chart execution."""
from pathlib import Path
import csv,json,zipfile,xml.etree.ElementTree as E
K=Path(__file__).parent
rows=list(csv.reader((K/'refreshments.csv').open()));expected=[['Refreshment table','Cups served'],['Water station','84'],['Tea table','61'],['Coffee table','47'],['Juice table','72']];assert rows==expected
values=[int(r[1]) for r in rows[1:]];assert sum(values)==264 and max(values)==84 and rows[1+values.index(max(values))][0]=='Water station'
a=json.load(open(K/'answer-key.json'));assert a['sourceRange']=='Refreshments!A1:B5' and a['baseline']==0 and a['totalInCategoryChart'] is False
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(K/'Community Event Refreshments.xlsx') as z:
 assert z.testzip() is None
 root=E.fromstring(z.read('xl/worksheets/sheet1.xml'));cells={c.attrib['r']:''.join(c.itertext()) for c in root.findall('.//s:c',ns)}
 for i,row in enumerate(expected,1):
  for col,value in zip(['A','B'],row):assert cells[col+str(i)]==value,(col,i,cells)
 root=E.fromstring(z.read('xl/worksheets/sheet2.xml'));formulas=[x.text for x in root.findall('.//s:f',ns)];assert formulas==['SUM(Refreshments!B2:B5)','MAX(Refreshments!B2:B5)']
 assert all(c.find('s:v',ns) is None for c in root.findall('.//s:c',ns) if c.find('s:f',ns) is not None)
print('PASS structural only: exact four rows/headers, source XLSX types and formulas, CRC; manual arithmetic total264/max84/Water station. Actual named spreadsheet calculation, chart creation, labels/range/scale and error-state interactions still require real application QA.')
