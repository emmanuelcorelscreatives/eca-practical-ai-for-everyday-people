import pathlib,json,csv,datetime
R=pathlib.Path(__file__).resolve().parent
f=json.loads((R/'source-facts.json').read_text());assert f['fictional'] and len(f['facts'])==9
assert datetime.date(2026,10,17).strftime('%A')=='Saturday'
o=json.loads((R/'worked-outputs.json').read_text())['outputs']
need=['Neighborhood Book Swap','17 October 2026','10:00','12:00','Cedar Room','Harbor Library','free','30','14 October 2026','one labeled book','under 12','adult']
for name,text in o.items():
 for word in need: assert word.casefold() in text.casefold(),(name,word)
assert o['v2-detail'].count('14 October 2026')==2
assert o['final'].count('14 October 2026')==1
for name in ['v1-scope','v2-detail','v3-tone','v4-structure','final']:
 for claim in ['exciting','wonderful community event','Meet other readers','discover new favorites','memorable morning']:assert claim.casefold() not in o[name].casefold(),(name,claim)
assert o['v2-detail'].startswith(o['v1-scope'])
assert o['v3-tone'].startswith('You’re welcome to take part')
assert len([x for x in o['v4-structure'].splitlines() if x.startswith('- ')])==7
h=['Version','Dimension changed','Desired result','Observed change','Unintended change','Facts preserved','Keep or revert']
for file in ['worksheet-blank.csv','worksheet-worked.csv']:
 with (R/file).open(newline='') as z:
  rows=list(csv.reader(z));assert rows[0]==h
  assert len(rows)==(1 if 'blank' in file else 6)
assert set(o)=={'baseline','v1-scope','v2-detail','v3-tone','v4-structure','final'}
comparison=(R/'worked-comparison.md').read_text()
for name,text in o.items(): assert '## '+name+'\n\n'+text in comparison
print('PASS: source category count, calendar weekday, six exact output keys, required substrings, scope phrase exclusions, V2 prefix/V3 opening/V4 bullet count, matching Markdown examples, worksheet shape and deadline counts. Human semantic review remains required.')
