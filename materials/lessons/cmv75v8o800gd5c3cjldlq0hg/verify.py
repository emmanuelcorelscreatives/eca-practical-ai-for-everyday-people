import json,csv,pathlib,datetime
p=pathlib.Path(__file__).parent
x=json.load(open(p/'sources.json'))['sources']; f,q,s=x
assert f['source_date']=='2026-09-02' and q['source_date']=='2026-09-20'
assert q['period_start']<f['period_start']<f['period_end']<q['period_end']
assert all(s[k] is None for k in ['source_date','period_start','period_end','definition','audience','activities'])
assert 'Derivative' in s['relationship']
rows=list(csv.DictReader(open(p/'comparison-expected.csv'))); assert len(rows)==3 and rows[2]['Classification']=='Not comparable yet'
for page in ['index.html','notes.html','flyer.html','faq.html','summary.html']:
 t=(p/page).read_text();assert '<script' not in t and 'http://' not in t and 'https://' not in t
print('PASS: source dates, nesting, explicit unknowns, relationships, expected rows and offline pages')
