from pathlib import Path
import csv,json,wave,datetime
K=Path(__file__).parent
rows=list(csv.DictReader(open(K/'reviewed-actions.csv')))
assert len(rows)==6
assert rows[1]['Owner']==rows[2]['Owner']=='Not stated — confirm'
assert rows[3]['Owner']=='Mateo' and rows[3]['Due date']=='Not stated — confirm'
assert 'Conditional' in rows[4]['Status'] and 'budget' in rows[4]['Evidence']
assert rows[5]['Owner']=='Sofia' and '03:20' in rows[5]['Evidence'] and '03:48' in rows[5]['Evidence']
for day,weekday in [(16,4),(19,0),(20,1),(21,2)]:assert datetime.date(2026,10,day).weekday()==weekday
with wave.open(str(K/'Community_Event_Planning.wav')) as w:assert w.getnframes()==246*22050 and w.getnchannels()==1
print(json.dumps({'state':'PASS','sixEvidenceRows':True,'missingOwnersPreserved':True,'conditionPreserved':True,'datesAndWeekdaysCorrect':True,'syntheticAudioSeconds':246}))
