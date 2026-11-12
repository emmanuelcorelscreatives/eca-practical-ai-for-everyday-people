"""Offline arithmetic and fixture-preservation check; no accounts/network."""
import csv
from pathlib import Path
root=Path(__file__).parent
def read(name):
    with (root/name).open(newline='') as f:return list(csv.DictReader(f))
def minute(t):
    h,m=map(int,t.split(':'));return h*60+m
def overlap(a,b,c,d):return max(0,min(minute(b),minute(d))-max(minute(a),minute(c)))
a=read('schedule-original.csv'); b=read('schedule-revised.csv')
old=next(r for r in a if r['status']=='faulty draft');new=next(r for r in b if r['action']=='Quick chickpea-spinach rice')
v=overlap(old['start'],old['end'],'17:40','19:50');travel=overlap(old['start'],old['end'],'17:40','18:00')
cook=minute(new['end'])-minute(new['start']);eat=next(r for r in b if r['action']=='Eat or pack meal');ed=minute(eat['end'])-minute(eat['start'])
same=[r for r in a if r['day']!='Tuesday']==[r for r in b if r['day']!='Tuesday'];fixed=[r for r in a if r['status']=='fixed']==[r for r in b if r['status']=='fixed']
print(f'original_overlap_minutes={v}');print(f'travel_only_overlap_minutes={travel}');print(f'revised_cooking_minutes={cook}');print(f'eat_or_pack_minutes={ed}');print(f'monday_wednesday_unchanged={same}');print(f'fixed_blocks_preserved={fixed}')
assert (v,travel,cook,ed,same,fixed)==(30,20,35,15,True,True)
assert minute(new['end'])<=minute('17:35')
print('PASS')
