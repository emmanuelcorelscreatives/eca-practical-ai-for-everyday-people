from pathlib import Path
import csv,datetime,json
from zoneinfo import ZoneInfo
r=Path(__file__).parent
rows=list(csv.DictReader((r/'expected-occurrences.csv').open()))
dates=[datetime.date.fromisoformat(x['date']) for x in rows]
assert len(dates)==10 and dates[0]==datetime.date(2026,11,18) and dates[-1]==datetime.date(2027,3,24)
assert all(d.weekday()==2 for d in dates)
assert all((b-a).days==14 for a,b in zip(dates,dates[1:]))
start=datetime.datetime(2026,11,18,15,tzinfo=ZoneInfo('Europe/London'))
end=start+datetime.timedelta(hours=1)
a=start.astimezone(ZoneInfo('Asia/Singapore')); b=end.astimezone(ZoneInfo('Asia/Singapore'))
assert (a.hour,a.day,b.hour,b.day)==(23,18,0,19)
print(json.dumps({'pass':True,'occurrences':len(dates),'first':str(dates[0]),'last':str(dates[-1]),'singaporeStart':a.isoformat(),'singaporeEnd':b.isoformat()}))
