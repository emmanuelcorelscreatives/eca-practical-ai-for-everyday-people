from pathlib import Path
import hashlib,json,zipfile,xml.etree.ElementTree as E,re
p=Path(__file__).parent;m=json.loads((p/'fixture-manifest.json').read_text())
for n,h in m.items():
 assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h, 'Changed file: '+n
with zipfile.ZipFile(p/'Event-Workbook.xlsx') as z:
 assert z.testzip() is None
 ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
 w=E.fromstring(z.read('xl/workbook.xml'))
 assert [x.attrib['name'] for x in w.findall('s:sheets/s:sheet',ns)]==['Overview','Schedule','Contacts']
 s=E.fromstring(z.read('xl/worksheets/sheet2.xml'));cells=s.findall('s:sheetData/s:row/s:c',ns)
 assert {c.attrib['r'] for c in cells}=={f'{c}{r}' for c in 'ABCD' for r in range(1,7)}
 expected=[['Time', 'Activity', 'Room', 'Lead'], ['9:00 AM', 'Registration', 'Lobby', 'Maya Chen'], ['10:00 AM', 'Welcome Session', 'Hall A', 'Daniel Okafor'], ['11:30 AM', 'Workshop', 'Room 204', 'Sofia Reyes'], ['1:00 PM', 'Lunch', 'Terrace', 'Amir Haddad'], ['2:30 PM', 'Closing Panel', 'Hall A', 'Elena Rossi']]
 actual={c.attrib['r']:''.join(c.itertext()) for c in cells}
 assert [[actual[f'{c}{r}'] for c in 'ABCD'] for r in range(1,7)]==expected, 'Schedule table must match the authored Room/Lead example'
b=(p/'Inspection-Pack.pdf').read_bytes();assert len(re.findall(rb'/Type\s*/Page\b',b))==4
print('PASS: four-file fixture hashes and structural markers verified')
