import csv,pathlib,datetime
p=pathlib.Path(__file__).parent
read=lambda n:list(csv.DictReader((p/n).open()))
r=read('reviews.csv');c=read('comparison-completed.csv')
assert len(r)==9 and len({x['Review ID'] for x in r})==9
recent=[x for x in r if x['Exact model']=='TrailSip 500' and '2026-10-01'<=x['Date']<='2026-10-14']
assert {x['Review ID'] for x in recent}=={'R1','R2','R3','R4','R5','R6','R7'}
assert r[5]['Review text']==r[6]['Review text']
assert r[4]['Disclosure']=='Product provided free for evaluation'
assert c[0]['Quoted claim']=='Capacity: 500 mL' and c[0]['Confidence']=='Directly stated'
assert c[1]['Confidence']=='Undefined claim'
assert c[4]['Quoted claim']==c[5]['Quoted claim']==''
assert all(x['Date checked']=='14 October 2026' for x in c)
assert all(x['Exact model']=='TrailSip 500' for x in c)
assert list(c[0])==['Exact model','Claim type','Quoted claim','Evidence opened','Date checked','Confidence','Unresolved question']
for x in r:
 datetime.date.fromisoformat(x['Date'])
 assert 1<=int(x['Synthetic stars out of 5'])<=5
for n in ['official-listing.html','manual.html','seller.html','reviews.html']:
 assert (p/'sources'/n).exists()
print('PASS: fictional sources; exact-model/date filters; duplication/disclosure; seven-column claim boundaries; unknown values blank')
