from pathlib import Path
import csv,datetime
p=Path(__file__).parent
s=(p/'Community_Garden_Open_Day_Brief.txt').read_text()
assert 'Seed swap begins at 10:15. Bring labelled seed packets.' in s
assert datetime.date(2026,11,7).strftime('%A')=='Saturday'
assert len(list(csv.DictReader(open(p/'decision-worksheet.csv'))))==4
assert (p/'Community_Garden_Open_Day_Brief.pdf').read_bytes().startswith(b'%PDF-1.4')
print('PASS: fixture, authored date and four worksheet tasks; no external claims verified')
