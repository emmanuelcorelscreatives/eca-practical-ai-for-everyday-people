import csv,json,zipfile,xml.etree.ElementTree as E
from pathlib import Path
p=Path(__file__).parent
r=list(csv.DictReader((p/'September_Request_Register_RAW.csv').open())); u={x['Request ID']:x for x in r}
a=list(csv.DictReader((p/'August_Request_Register.csv').open()));v=list(csv.DictReader((p/'Volunteer_Log.csv').open()))
assert len(r)==51 and len(u)==50 and sum(x['Request ID']=='REP-094' for x in r)==2
assert sum(x['Status']=='Completed' for x in u.values())==42
assert sum(x['Status']=='Unresolved' for x in u.values())==8
av=list(csv.DictReader((p/'August_Volunteer_Log.csv').open()));assert sum(float(x['Confirmed hours']) for x in av)==71
assert len(a)==44 and sum(x['Status']=='Completed' for x in a)==35
assert sum(float(x['Confirmed hours']) for x in v if x['End'])==76
assert sum(not x['End'] for x in v)==1 and (42-35)/35==.2
with zipfile.ZipFile(p/'Repair_Event_Records.xlsx') as z:
 assert z.testzip() is None
 for n in z.namelist():
  if n.endswith('.xml') or n.endswith('.rels'):E.fromstring(z.read(n))
print(json.dumps({'status':'PASS','rawSeptember':51,'uniqueSeptember':50,'completed':42,'unresolved':8,'confirmedHours':76,'incompleteShifts':1,'completionChange':.2}))
