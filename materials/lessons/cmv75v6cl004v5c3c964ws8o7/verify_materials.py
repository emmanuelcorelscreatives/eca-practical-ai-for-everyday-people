from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,csv
k=Path(__file__).parent
for stem in ['Riverside_Reading_Picnic_Brief','Example_Announcement']:
 with zipfile.ZipFile(k/(stem+'.docx')) as z:
  assert z.testzip() is None
  tree=ET.fromstring(z.read('word/document.xml'))
  text='\n'.join(e.text or '' for e in tree.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))+'\n'
  assert text==(k/(stem+'.txt')).read_text()
answer=' '.join(l[2:] for l in (k/'answer-key.md').read_text().splitlines() if l.startswith('> '))
assert len(answer.split())==37 and len(answer.split())<=120
for required in ['18 October 2026','10:00','12:00','Maple Community Garden','registration','cup','picnic mat','East Gate','[NOT SUPPLIED]']:assert required in answer
assert 'lantern' not in answer and '@' not in answer
rows=list(csv.DictReader((k/'claim-check.csv').open()));assert len(rows)==11 and sum(r['status']=='reject' for r in rows)==2
print('PASS: DOCX/text exact parity and ZIP CRC, 37-word faithful answer, eleven claim rows with two explicit rejections.')
