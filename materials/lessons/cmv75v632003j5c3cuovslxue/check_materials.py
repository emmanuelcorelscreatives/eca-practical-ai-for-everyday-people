from pathlib import Path
import json, zipfile, xml.etree.ElementTree as E
D=Path(__file__).parent
p=json.loads((D/'draft-paragraphs.json').read_text())
for key,expected,name in [('draft1',137,'Volunteer Welcome — Draft 1'),('draft2',134,'Volunteer Welcome — Draft 2 — Tone Revision')]:
 paragraphs=p[key]; assert len(paragraphs)==4
 body=' '.join(paragraphs); assert len(body.split())==expected
 for fact in ['08:45','community hall side entrance','reusable bottle','Sam']: assert fact in body
 assert 'Free parking is available behind the hall.' not in body
 md=(D/(name+'.md')).read_text(); assert sum(x.startswith('- ') for x in md.splitlines())==3
 with zipfile.ZipFile(D/(name+'.odt')) as z:
  assert z.testzip() is None
  root=E.fromstring(z.read('content.xml'));ns={'t':'urn:oasis:names:tc:opendocument:xmlns:text:1.0'}
  assert len(root.findall('.//t:list-item',ns))==3
  assert ' '.join(''.join(x.itertext()) for x in root.findall('.//t:p',ns))==body
 print(key,expected,'words; three bullets; required facts preserved; ODT matches: PASS')
print('Tone requires manual comparison against the brief; no automatic tone verdict.')
