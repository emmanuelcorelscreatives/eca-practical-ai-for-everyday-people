from pathlib import Path
import json,csv,xml.etree.ElementTree as ET
from html.parser import HTMLParser
p=Path(__file__).parent;x=json.loads((p/'source-pack.json').read_text())
with(p/'attendance.csv').open(newline='') as f: rows=list(csv.DictReader(f))
assert [(r['session'],int(r['people'])) for r in rows]==[(r['session'],r['people']) for r in x['attendance']]
assert [r['people'] for r in x['attendance']]==[48,36,24]
assert x['steps']==['Bring reusable bottle','Check in','Choose a session','Return borrowed tools']
ns={'s':'http://www.w3.org/2000/svg'};chart=ET.parse(p/'attendance-chart.svg').getroot();bars=[q for q in chart.findall('s:rect',ns) if q.get('data-session')]
assert [(b.get('data-session'),int(b.get('data-value'))) for b in bars]==[(r['session'],r['people']) for r in x['attendance']]
assert [int(b.get('width')) for b in bars]==[960,720,480] and all(b.get('x')=='450' for b in bars)
texts=[''.join(e.itertext()) for e in chart.findall('s:text',ns)]
assert all(str(v) in texts for v in [0,12,24,36,48]) and 'People' in texts
process=ET.parse(p/'participation-diagram.svg').getroot();nodes=[q for q in process.findall('s:rect',ns) if q.get('data-step')]
assert [q.get('data-label') for q in nodes]==x['steps']
assert len([q for q in process.findall('s:path',ns) if q.get('marker-end')])==3
class Fixture(HTMLParser):
 def __init__(self):super().__init__();self.in_fixture=False;self.data='';self.links=[]
 def handle_starttag(self,t,a):
  d=dict(a)
  if t=='script' and d.get('id')=='fixture':self.in_fixture=True
  for key in ('src','href','action'):
   if d.get(key,'').startswith(('http:','https:','//')):self.links.append(d[key])
 def handle_endtag(self,t):
  if t=='script':self.in_fixture=False
 def handle_data(self,d):
  if self.in_fixture:self.data+=d
z=Fixture();z.feed((p/'clearslide.html').read_text());fixture=json.loads(z.data)
assert fixture['attendance']==x['attendance'] and fixture['steps']==x['steps'] and not z.links
print(json.dumps({'sourceRowsAndSteps':'PASS','nativeBarWidthsAndZeroBaseline':'PASS','nativeDiagramOrderAndThreeForwardArrows':'PASS','HTMLFixtureMatchesSources':'PASS','externalResourceLinks':0,'scope':'STATIC_SOURCE_AND_VECTOR_CHECK_ONLY; actual browser interaction/PDF export QA remains required'}))
