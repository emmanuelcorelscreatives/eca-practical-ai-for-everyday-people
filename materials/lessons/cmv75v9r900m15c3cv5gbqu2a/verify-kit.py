from pathlib import Path
from decimal import Decimal as D
import json,csv,datetime
p=Path(__file__).parent;d=json.loads((p/'fixture-data.json').read_text());a=d['NorthstarOutfitters'];h=d['hotel'];r=list(csv.DictReader((p/'comparison-expected.csv').open(newline='')))
assert D(str(a['unit']))*2==D(str(a['items']))
assert a['items']+a['delivery']+a['mandatoryService']==a['totalWithoutOptional']==106
assert a['totalWithoutOptional']+a['optionalGiftWrap']==112
assert h['baseStay']+h['mandatory']==h['totalWithoutOptional']==204
assert h['totalWithoutOptional']+h['optionalBreakfast']==234
assert (datetime.date.fromisoformat(h['checkOut'])-datetime.date.fromisoformat(h['checkIn'])).days==2
assert all(datetime.date.fromisoformat(z)<datetime.date.fromisoformat(d['shoppingRequirement']['requiredBy']) for z in a['estimatedArrival'])
assert len(r)==3 and r[0]['Total']=='106.00' and r[1]['Total']=='' and r[2]['Total']=='204.00'
assert d['TrailMarket']['usableTotalForTwo'] is None and d['TrailMarket']['availableCorrect']==1
assert all(x['Checked time']==d['fixtureCheckedTime'] for x in r)
print('PASS fictional fixture arithmetic, dates, availability failure, timestamps and expected CSV; no live-price verification claim')
