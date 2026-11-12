import csv, sys, json
from pathlib import Path
p=Path(sys.argv[1] if len(sys.argv)>1 else Path(__file__).with_name('illustrative-agenda.csv'))
with p.open(encoding='utf-8',newline='') as f:
    reader=csv.DictReader(f)
    assert reader.fieldnames==['Time','Topic','Intended outcome','Key question','Lead'], 'Wrong columns'
    rows=list(reader)
assert len(rows)==7, 'Expected seven authored example rows'
minutes=[int(r['Time']) for r in rows]
assert minutes==[3,7,5,4,4,4,3], 'Changed example allocation: review your independent draft manually'
assert sum(minutes)==30
assert all(r['Lead']=='To confirm' for r in rows), 'Unsupported lead'
assert all(r['Topic'] and r['Intended outcome'] and r['Key question'] for r in rows)
print(json.dumps({'rows':len(rows),'minutes':minutes,'totalMinutes':sum(minutes),'limitMinutes':30,'differenceMinutes':sum(minutes)-30,'allLeadsUnconfirmed':True,'scope':'Arithmetic and structure only; organizer review still required'},indent=2))
