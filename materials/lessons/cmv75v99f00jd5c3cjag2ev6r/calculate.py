#!/usr/bin/env python3
"""Reproducible fictional Academy worksheet; no real product claims."""
from pathlib import Path
import csv
from decimal import Decimal
root=Path(__file__).resolve().parent
fields=['ease','reliability','cost','support']
with (root/'scores.csv').open(newline='') as f: scores=list(csv.DictReader(f))
with (root/'weights.csv').open(newline='') as f: weights=list(csv.DictReader(f))
expected={'equal':['4.00','4.00','4.00'],'convenience':['4.15','4.20','3.65'],'reliability_exercise':['4.30','3.80','3.90']}
for w in weights:
    assert sum(Decimal(w[f]) for f in fields)==1, 'Weights must sum to 100%'
    totals=[sum(Decimal(row[f])*Decimal(w[f]) for f in fields) for row in scores]
    assert [format(t,'.2f') for t in totals]==expected[w['scenario']]
    eligible=[(row['option'],t) for row,t in zip(scores,totals) if row['offline_required_pass']=='yes']
    best=max(t for _,t in eligible)
    print(w['scenario'], ', '.join(row['option']+'='+format(t,'.2f') for row,t in zip(scores,totals)), 'eligible leaders:', ', '.join(n for n,t in eligible if t==best))
assert scores[2]['support_cost']=='unknown'
print('PASS: exact totals, 100% weights, hard offline exclusion and visible unknown preserved.')
