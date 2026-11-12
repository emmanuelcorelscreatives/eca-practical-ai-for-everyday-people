import json,csv,pathlib
p=pathlib.Path(__file__).parent
s=json.loads((p/'source-notes.json').read_text()); d=(p/'generated-practice-draft.txt').read_text(); r=(p/'revised-practice-script.txt').read_text()
assert s['fictional_practice_only'] and not s['publish_ready']
for key in ['date','time','place','contact']: assert s[key] in d and s[key] in r
assert 'and the question you most want answered' in d and 'and the question you most want answered' not in r
assert 'Bring one device.' in r and 'free community device-help session' in r
assert r.count('To register, contact [CONTACT].')==1
assert d.replace(' and the question you most want answered','')==r
rows=list(csv.DictReader((p/'read-through-log.csv').open())); assert len(rows)==2 and all(not row['actual_seconds'] for row in rows)
assert len(r.strip().split('\n\n'))==4
print('PASS: fictional source, four unresolved placeholders, supported facts, exact scoped deletion, one action, four paragraphs and blank actual-timing log')
