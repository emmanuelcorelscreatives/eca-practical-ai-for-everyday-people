from pathlib import Path
import json,csv
p=Path(__file__).parent;x=json.loads((p/'shortlist-fixture.json').read_text());assert x['fictional'] and x['preparedNotLiveSearch']
a,b,c=x['options'];assert a['menuEUR']+a['serviceEUR']==a['knownSubtotalEUR']==55
assert b['serviceEUR'] is None and b['knownSubtotalEUR'] is None and not b['publishedContactInFixture']
assert c['menuEUR']+c['serviceEUR']==c['knownSubtotalEUR']==66 and 66-x['budgetEUR']==6
assert not any(o['accessConfirmed'] or o['availableConfirmed'] or o['fullUnavoidableCostKnown'] for o in x['options'])
assert all(x['brief'][k] is None for k in ['actualCalendarDate','city','exactAddress','travelMode'])
for o in x['options']: assert (p/o['source']).is_file()
with(p/'comparison-worked.csv').open(newline='') as f: rows=list(csv.DictReader(f))
assert len(rows)==3 and all(len(r)==9 for r in rows)
assert all(r['Checked date']=='Fill only after YOU open the source' for r in rows)
print(json.dumps({'fixtureArithmetic':'PASS','knownUnknowns':'PASS','unconfirmedFixtureFlags':'PASS','sourcesPresent':3,'comparisonRows':3,'checkedDatesRemainLearnerInput':'PASS'}))
