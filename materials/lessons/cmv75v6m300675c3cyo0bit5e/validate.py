"""Reproduce numerical checks from the supplied fictional CSV, offline."""
from pathlib import Path
import csv,json
rows=list(csv.DictReader((Path(__file__).parent/'rooms.csv').open(newline='')))
def eligible(people):
 return [r['Room'] for r in rows if int(r['Capacity'])>=people and int(r['Fee credits'])<=120 and r['Available 18:00–20:00']=='yes' and r['Step-free']=='yes']
assert eligible(24)==['Riverside Room']
assert eligible(22)==['Riverside Room','Garden Studio']
assert rows[1]['Projector']=='unknown'
assert int(rows[0]['Fee credits'])-120==25
assert 120-int(rows[1]['Fee credits'])==10
assert 24-int(rows[2]['Capacity'])==2
print(json.dumps({'people_24_eligible':eligible(24),'people_22_eligible':eligible(22),'Riverside_projector':'unknown','Maple_over_budget':25,'Garden_places_short_at_24':2,'result':'PASS'},indent=2))
