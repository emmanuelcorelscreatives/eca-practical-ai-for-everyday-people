from decimal import Decimal as D
scores={'Cedar Hall':[6,7,7,9],'River Room':[8,5,7,5],'Market Studio':[7,5,9,8]}
def total(s,w): return sum(D(str(a))*D(str(b)) for a,b in zip(s,w))
w=[.40,.30,.20,.10];changed=[.40,.35,.15,.10]
assert sum(map(lambda x:D(str(x)),w))==D('1.00')
assert sum(map(lambda x:D(str(x)),changed))==D('1.00')
a={n:total(s,w) for n,s in scores.items()};b={n:total(s,changed) for n,s in scores.items()}
assert a=={'Cedar Hall':D('6.80'),'River Room':D('6.60'),'Market Studio':D('6.90')}
assert b=={'Cedar Hall':D('6.80'),'River Room':D('6.50'),'Market Studio':D('6.70')}
assert total([6,7,6,9],w)==D('6.60') and total([6,7,8,9],w)==D('7.00')
assert D('6.60')<=a['Market Studio']<=D('7.00')
print('Original assumptions: Cedar Hall=6.80; River Room=6.60; Market Studio=6.90')
print('Changed assumptions: Cedar Hall=6.80; River Room=6.50; Market Studio=6.70')
print('Cedar equipment6–8 sensitivity:6.60–7.00, overlapping Market6.90')
print('PASS: exact totals, weights100%, rank reversal, overlapping range; assumptions remain unjustified.')
