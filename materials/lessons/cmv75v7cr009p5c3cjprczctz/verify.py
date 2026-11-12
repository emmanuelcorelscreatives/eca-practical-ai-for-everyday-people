#!/usr/bin/env python3
"""Offline arithmetic replay; no AI, browser or spreadsheet execution."""
import csv
from decimal import Decimal as D
from pathlib import Path
P=Path(__file__).resolve().parent

def rows(name):
    with (P/name).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def main():
    count=0
    def check(name,condition):
        nonlocal count
        if not condition:
            raise ValueError(name)
        count+=1
        print('PASS '+name)
    s=rows('source-input.csv')
    check('source fixture',len(s)==1 and D(s[0]['quantity'])==48 and D(s[0]['unit_price'])==D('19.75') and s[0]['price_unit']=='unspecified units per item')
    q=D(s[0]['quantity']); p=D(s[0]['unit_price']); exact=q*p
    check('estimate and strict bounds',D(50)*20==1000 and q*19<exact<q*20 and (q*19,q*20,exact)==(D(912),D(960),D(948)))
    check('split multiplication',p*40==790 and p*8==158 and p*40+p*8==exact)
    check('authored error fixtures',D(s[0]['illustrative_wrong_answer'])==exact*10 and D(s[0]['plausible_wrong_answer'])==954 and q*19<D(954)<q*20 and D(954)!=exact)
    r=rows('quantity-check.csv'); products=[D(x['Quantity'])*D(x['Unit price']) for x in r]
    check('five table products',len(r)==5 and products==[D(x) for x in ['948','120','270','100','48']] and products==[D(x['Total']) for x in r])
    template=rows('quantity-check-template.csv')
    check('template and omitted row',len(template)==5 and all(x['Total']=='' for x in template) and [(x['Quantity'],x['Unit price']) for x in template]==[(x['Quantity'],x['Unit price']) for x in r] and sum(products[:4])==1438 and sum(products)==1486 and sum(products)-sum(products[:4])==48)
    check('unit conversion',D(12)+D(800)/1000==D('12.8'))
    v=[D(x['value']) for x in rows('mean-values.csv')]
    check('mean bounds and exact mean',v==[12,15,18,20,25] and sum(v)==90 and sum(v)/len(v)==18 and not min(v)<=D(31)<=max(v))
    c=rows('practice-cases.csv')
    check('practice fixture and scale',len(c)==3 and [x['case'] for x in c]==['A','B','C'] and [D(x['proposed_answer']) for x in c]==[10150,271,82] and D(203)*5==1015 and D(9)*30==270 and D(82)>70)
    print(str(count)+' deterministic checks passed; no software UI or source provenance verified.')

if __name__=='__main__':
    main()
