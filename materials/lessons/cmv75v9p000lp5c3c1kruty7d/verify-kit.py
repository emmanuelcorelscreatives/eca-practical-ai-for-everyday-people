import csv,json,pathlib
p=pathlib.Path(__file__).parent
rows=list(csv.DictReader((p/'expected-register.csv').open(newline='')))
assert len(rows)==4
assert rows[0]['Total']=='48.6' and rows[0]['Reference']=='NS-1042'
assert rows[1]['Total']=='' and '2026-10-18' in rows[1]['Action or Deadline']
assert rows[2]['Total']=='73.2' and rows[2]['Reference']=='RR-7719'
assert rows[3]['Status']=='Exception' and 'Obtain complete page' in rows[3]['Action or Deadline']
for r in rows: assert (p/'Admin Routine'/'Originals'/r['Source File']).is_file()
d=json.loads((p/'ocr-draft-fixtures.json').read_text())
assert d['Riverbend']['total']=='78.20' and d['Riverbend']['reference']=='RR-771g'
import zipfile,xml.etree.ElementTree as E,hashlib
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
def readxlsx(f):
 with zipfile.ZipFile(f) as z:
  assert z.testzip() is None
  tree=E.fromstring(z.read('xl/worksheets/sheet1.xml'))
  out=[]
  for r in tree.findall('s:sheetData/s:row',ns):
   row=['']*9
   for c in r.findall('s:c',ns):
    col=ord(c.attrib['r'][0])-65
    row[col]=''.join(c.itertext())
   out.append(row)
  return out
expected=list(csv.reader((p/'expected-register.csv').open(newline='')))
assert readxlsx(p/'expected-register.xlsx')==expected
starter=list(csv.reader((p/'starter-register.csv').open(newline='')))
assert readxlsx(p/'Admin Routine/Monthly_Admin_Register.xlsx')==starter
for r in rows:
 a=p/'Admin Routine/Originals'/r['Source File'];b=p/'Admin Routine/01_Inbox'/r['Source File']
 assert hashlib.sha256(a.read_bytes()).digest()==hashlib.sha256(b.read_bytes()).digest()
print('PASS selected CSV/draft fields, both XLSX-to-CSV exact contents, source existence and four duplicate hashes; no image/PDF reading, OCR or learner link-test claim')
