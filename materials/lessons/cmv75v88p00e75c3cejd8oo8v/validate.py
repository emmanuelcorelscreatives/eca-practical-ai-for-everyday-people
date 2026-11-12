from pathlib import Path
import json
from html.parser import HTMLParser
p=Path(__file__).parent
x=json.loads((p/'checks.json').read_text())
assert 24*3==x['arithmetic'][0]['expected']==sum(x['arithmetic'][0]['parts'])
assert 36*4==x['arithmetic'][1]['expected']==sum(x['arithmetic'][1]['parts'])
source=(p/'source-garden.txt').read_text()
for term in x['sourceSupport']: assert term in source
class Page(HTMLParser):
 def __init__(self): super().__init__();self.details=0;self.open=0;self.external=[];self.scripts=0;self.textareas=0
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='details': self.details+=1;self.open+=('open' in a)
  if t=='script': self.scripts+=1
  if t=='textarea': self.textareas+=1
  for k in ('src','href','action'):
   if a.get(k,'').startswith(('http:','https:','//')):self.external.append(a[k])
z=Page();z.feed((p/'practice.html').read_text())
assert z.details==7 and z.open==0 and z.scripts==0 and z.textareas==4 and not z.external
print(json.dumps({'arithmetic':'PASS','sourceTerms':'PASS','initiallyCollapsedDisclosures':z.details,'externalRequests':z.external,'clientScripts':z.scripts,'textareaCount':z.textareas}))
