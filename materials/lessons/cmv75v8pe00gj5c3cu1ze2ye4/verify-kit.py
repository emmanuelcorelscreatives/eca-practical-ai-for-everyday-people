from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote
import csv
D=Path(__file__).parent
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for key,value in attrs:
   if key in ('href','src') and value and not value.startswith(('http:','https:','mailto:','#','data:')):
    assert (D/unquote(value.split('#')[0])).is_file(), (tag,value)
for p in D.glob('*.html'): Links().feed(p.read_text())
r=list(csv.DictReader((D/'claim-table.csv').open(newline='')))
assert len(r)==3 and [x['Status'] for x in r]==['Supported','Excluded from exact-rule finding','Unresolved conflict']
assert 'Visitors may bring closed reusable water bottles into study rooms.' in (D/'visitor-rules.html').read_text()
assert 'Open cups are not permitted.' in (D/'visitor-rules.html').read_text()
assert 'No drinks in quiet rooms.' in (D/'older-guide.html').read_text()
assert 'not provided' in (D/'blog.html').read_text()
b=(D/'completed-brief.html').read_text()
for s in ['Question and scope','Key findings and links','Interpretation or practical takeaway','Caveats or conflicts','Unanswered questions','Checked date','appears consistent','do not confirm','has not been inspected']: assert s in b,s
assert '2026-11-12' in b and 'own actual inspection date' in b
print('PASS: local source links, three evidence dispositions, exact rule and exception, six-part brief, uncertainty and inspection-date separation.')

assert 'Simulated worked-example checked date' in b
for n in ['search-request.html','lateral-check.html','publisher-about.html','community-directory.html']: assert (D/n).is_file()
