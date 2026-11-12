from pathlib import Path
import csv
r=Path(__file__).parent
source=(r/'source-brief.md').read_text();draft=(r/'announcement-draft.txt').read_text();correct=(r/'announcement-corrected.txt').read_text()
assert 'Day: Friday' in source and 'Thursday' in draft and 'Friday' in correct
assert 'guaranteed a place' in draft and 'Free refreshments' in draft
assert 'internal-planning@example.invalid' in draft and 'internal-planning@example.invalid' not in correct
assert 'workshop@example.invalid' in correct and 'confirmed booking' in correct
assert (17*60+30)-(16*60)==90
assert 'overflow:hidden' in (r/'export-clipped.html').read_text()
assert 'overflow-wrap:anywhere' in (r/'export-corrected.html').read_text()
for name in ['export-clipped.html','export-corrected.html']:
    page=(r/name).read_text()
    assert 'DRAFT-189-v2' in page and 'Price, organizer name and accessibility details: not provided' in page
    assert all(word in page for word in ['Everyday Digital Skills Workshop','Friday, 16:00–17:30','Community Learning Room','confirmed booking','workshop@example.invalid'])
rows=list(csv.DictReader((r/'review-checklist.csv').open()))
assert set(x['section'] for x in rows)=={'Brief','Evidence','Meaning','Destination','Action'}
assert len(rows)==11 and all(x['observable_test'] and x['evidence'] and x['pass_criterion'] and x['owner'] for x in rows)
assert all(x['decision']=='NOT_REVIEWED' for x in rows)
assert len(list(csv.DictReader((r/'review-log.csv').open())))==0
assert 'HOLD' in (r/'action-review.md').read_text()
print('PASS: fictional fixture facts, draft defects, checklist and review boundaries')
