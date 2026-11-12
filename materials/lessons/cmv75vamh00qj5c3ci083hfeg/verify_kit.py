from pathlib import Path
import json,xml.etree.ElementTree as E
r=Path(__file__).parent;e=json.loads((r/'expected-checks.json').read_text());d=(r/'poster-draft.svg').read_text();c=(r/'poster-checked.svg').read_text()
for name,s in [('draft',d),('checked',c)]:
 E.fromstring(s)
 assert e['origin'] in s,(name,'missing origin qualifier')
for x in e['draftRequired']:assert x in d,x
for x in e['checkedRequired']:assert x in c,x
for x in e['checkedForbidden']:assert x not in c,x
for name,s,bottom in [('draft',d,e['draftBookBottom']),('checked',c,e['checkedBookBottom'])]:
 root=E.fromstring(s);book=next(x for x in root.iter() if x.get('id')=='right-book');assert int(book.get('y'))+int(book.get('height'))==bottom
assert e['draftBookBottom']<e['tableTop'] and e['checkedBookBottom']==e['tableTop']
print('PASS: supplied SVG/text fixtures match expected checks. Human content, representation and export review still required.')
