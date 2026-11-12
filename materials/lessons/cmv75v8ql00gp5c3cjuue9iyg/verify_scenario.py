import json
from pathlib import Path
from html.parser import HTMLParser
r=Path(__file__).parent
s=json.loads((r/'scenario.json').read_text())
assert s['fictional'] is True and s['quantity']==2
assert s['initial']['adultAdmission']*2==s['initial']['subtotal']==36
assert s['refreshed']['adultAdmission']*2==s['refreshed']['subtotal']==40
assert s['refreshed']['subtotal']-s['initial']['subtotal']==4
assert s['initial']['dateSpecificHours']==s['refreshed']['dateSpecificHours']=='10:00–16:00'
for phase in ['initial','refreshed']:
    assert s[phase]['arrival']<'11:00'
    assert s[phase]['serviceCharge'] is None and s[phase]['finalTotal'] is None
assert all(s['liveStatus'][x] is None for x in ['departure','platform','serviceStatus','alerts'])
class Links(HTMLParser):
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key=='href': assert (r/value).is_file(), value
for p in r.glob('*.html'): Links().feed(p.read_text())
print('PASS: source arithmetic, date-specific hours, arrival target, unresolved fields and all local links')
