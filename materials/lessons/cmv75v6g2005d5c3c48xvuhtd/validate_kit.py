from pathlib import Path
import zipfile,xml.etree.ElementTree as ET
r=Path(__file__).parent
for n in range(1,7):
 files=list((r/'sections').glob(f'S{n:02}_*.md'));assert len(files)==1
for p in r.glob('*.odt'):
 with zipfile.ZipFile(p) as z:
  assert z.testzip() is None
  assert z.read('mimetype')==b'application/vnd.oasis.opendocument.text'
  ET.fromstring(z.read('content.xml'))
t=(r/'checked-public-information-sheet.md').read_text()
for x in ['17 May 2030','10:00','step-free route','does not promise','advanced seed-saving workshop','volunteer arrival','unconfirmed']:
 assert x in t,x
print('PASS: six sections, eight readable ODTs and worked qualification checks; semantic source review still required')
