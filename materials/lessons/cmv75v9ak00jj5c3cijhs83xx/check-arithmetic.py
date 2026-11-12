from decimal import Decimal as D
scores={'Cedar Hall':[6,9,8,8],'River Room':[8,6,7,5],'Market Studio':[7,7,9,8]}
def total(s,w): return sum(D(str(a))*D(str(b)) for a,b in zip(s,w))
w=[.25,.25,.30,.20]; changed=[.25,.30,.25,.20]
a={n:total(s,w) for n,s in scores.items()};b={n:total(s,changed) for n,s in scores.items()}
assert a=={'Cedar Hall':D('7.75'),'River Room':D('6.60'),'Market Studio':D('7.80')}
assert b=={'Cedar Hall':D('7.80'),'River Room':D('6.55'),'Market Studio':D('7.70')}
assert total([6,9,7,8],w)==D('7.45') and total([6,9,9,8],w)==D('8.05')
print('Original assumptions:',a);print('Changed assumptions:',b)
print('Arithmetic checks passed; judgments remain unsupported.')
