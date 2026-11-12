import csv, pathlib, zipfile, xml.etree.ElementTree as E, hashlib, json, posixpath
p=pathlib.Path(__file__).parent
facts=list(csv.DictReader((p/'approved-public-facts.csv').open()))
assert len(facts)==9
m={r['Field']:r['Approved teaching fact or explicit gap'] for r in facts}
expected={'Event name':'Riverside Skills Day','Date':'Saturday, 14 November 2026','Time':'10:00–15:00','Venue':'Riverside Community Hall','Entry':'Free entry','Registration':'Registration required','Public contact':'events@riverside.example','Accessibility information':'Venue has step-free entrance. Contact the event team for other requirements.','Parking information':'Not supplied — confirm before publication'}
assert m==expected
assert m['Date']=='Saturday, 14 November 2026' and m['Time']=='10:00–15:00'
assert m['Public contact']=='events@riverside.example' and m['Parking information']=='Not supplied — confirm before publication'
r=list(csv.DictReader((p/'restricted-working-register-FICTIONAL.csv').open()));assert len(r)==5
assert all(x['Contact Method']=='contact withheld' for x in r)
for name in ['approved-public-facts.docx','public-announcement-model.docx','announcement-inspection-copy.docx','restricted-working-register-FICTIONAL.xlsx']:
 with zipfile.ZipFile(p/name) as z:
  assert z.testzip() is None
  for n in z.namelist():
   if n.endswith(('.xml','.rels','.vml')):E.fromstring(z.read(n))
   if n.endswith('.rels'):
    for rel in E.fromstring(z.read(n)):
     if rel.attrib.get('TargetMode')=='External':continue
     target=rel.attrib['Target'];base=posixpath.dirname(posixpath.dirname(n)) if n!='_rels/.rels' else ''
     resolved=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join(base,target))
     assert resolved in z.namelist(),(name,n,resolved)
with zipfile.ZipFile(p/'announcement-inspection-copy.docx') as z:
 d=z.read('word/document.xml').decode();assert 'w:del ' in d and 'w:vanish' in d and 'w:commentReference' in d;assert 'FICTIONAL internal comment' in z.read('word/comments.xml').decode()
with zipfile.ZipFile(p/'restricted-working-register-FICTIONAL.xlsx') as z:
 assert 'state="hidden"' in z.read('xl/workbook.xml').decode()
 assert any('comment' in n for n in z.namelist())
 assert 'hidden="1"' in z.read('xl/worksheets/sheet1.xml').decode()
print(json.dumps({'status':'PASS','scope':'sample facts and OOXML structural/review-artifact checks only','files':len(list(p.iterdir())),'certifiesHumanReviewOrAccessControl':False}))
