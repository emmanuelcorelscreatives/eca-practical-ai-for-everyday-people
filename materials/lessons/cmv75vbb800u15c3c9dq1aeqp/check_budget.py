"""Optional exact arithmetic check for fictional workshop data; Python 3 standard library."""
from decimal import Decimal
from pathlib import Path
import csv
rows=list(csv.DictReader((Path(__file__).parent/'expected-budget.csv').open()))
amounts=[]
for row in rows[:3]:
 amount=Decimal(row['Quantity'])*Decimal(row['Unit cost'])
 assert amount==Decimal(row['Calculated cost']),row['Item']
 amounts.append(amount)
assert amounts==[Decimal('180'),Decimal('12'),Decimal('84')]
assert sum(amounts)==Decimal(rows[3]['Calculated cost'])==Decimal('276')
assert Decimal('180')+Decimal('12')+Decimal('40')*Decimal('2.40')==Decimal('288')
print('PASS: three rows, 180 + 12 + 84 = 276 credits; 40-attendee variant = 288 credits')
