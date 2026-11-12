from pathlib import Path
import zipfile,xml.etree.ElementTree as E,hashlib,json
p=Path(__file__).parent
src=p/'Riverside_Event_Source.odt'; copy=p/'Riverside_Event_Working_Copy.odt'
assert src.read_bytes()==copy.read_bytes(), 'working copy differs'
with zipfile.ZipFile(src) as z:
 assert z.testzip() is None
 body=z.read('content.xml').decode();meta=z.read('meta.xml').decode()
 assert 'Mina Okafor' in meta
 root=E.fromstring(body)
 for element in list(root.iter()):
  for child in list(element):
   if child.tag.endswith('}annotation'):element.remove(child)
 assert 'Mina Okafor' not in ''.join(root.itertext())
 assert 'office:annotation' in body and 'ari@example.invalid' in body
 assert '480 units' in body and 'Please do not circulate this.' in body
 E.fromstring(body);E.fromstring(meta)
with zipfile.ZipFile(p/'Riverside_Clean_Setup_Notes.odt') as z:
 assert z.testzip() is None
 clean=z.read('content.xml').decode(); meta=z.read('meta.xml').decode()
 for token in ['08:00','Twelve folding tables','Twenty-four chairs','Entrance sign','Two waste stations','Quiet rest area']:assert token in clean,token
 for token in ['480','Ari Example','Jo Example','Mina Okafor','example.invalid','family appointment','office:annotation']:assert token not in clean,token
 assert 'Mina Okafor' not in meta
print(json.dumps({'state':'PASS','scope':'packaged fictional examples only; not a general privacy scanner','sourceSha256':hashlib.sha256(src.read_bytes()).hexdigest(),'workingCopyIdentical':True,'realOdfComment':True,'fictionalAuthorMetadata':True,'cleanFactsPreserved':True,'excludedDetailsAbsent':True},indent=2))
