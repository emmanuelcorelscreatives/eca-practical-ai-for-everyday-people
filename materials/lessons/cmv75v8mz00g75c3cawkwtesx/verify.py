from pathlib import Path
import csv,re
p=Path(__file__).parent
rows=list(csv.DictReader((p/'answer-key.csv').open(encoding='utf-8')))
assert len(rows)==4
for row in rows: assert (p/row['opened_source']).is_file()
assert '6:00 p.m.' in rows[0]['support_found']
assert 'school groups' in rows[1]['support_found']
assert 'North Gate' in rows[2]['support_found']
assert 'main garden remains open' in rows[3]['support_found']
for f in [p/'index.html',*(p/'pages').glob('*.html')]:
 for link in re.findall(r'href="([^"]+)"',f.read_text(encoding='utf-8')): assert (f.parent/link).resolve().is_file(),(f,link)
print('PASS: four source-bound findings, required qualifiers and every local link verified; no external facts checked.')
