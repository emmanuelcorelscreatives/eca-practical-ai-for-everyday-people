from pathlib import Path
import csv
r=list(csv.DictReader((Path(__file__).parent/'reference/comparison.csv').open()))
assert [x['Option'] for x in r]==['Northstar Basic','Harbor Plus','Cedar Flex']
assert int(r[0]['Monthly price'])*12+int(r[0]['Installation fee'])+int(r[0]['Equipment fee'])==596
assert int(r[1]['Monthly price'])*12+int(r[1]['Installation fee'])+int(r[1]['Equipment fee'])==646
assert int(r[2]['Monthly price'])*12==624
assert r[2]['Equipment fee']==r[2]['Installation fee']==r[2]['Contract']=='unknown'
assert '07:00' in r[2]['Install timing']
print('PASS: supplied reference arithmetic, unknown fees and Cedar installation boundary. This is not a real-offer verification or learner judgment.')
