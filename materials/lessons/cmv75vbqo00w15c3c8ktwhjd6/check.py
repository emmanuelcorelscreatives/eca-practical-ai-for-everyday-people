import json
from pathlib import Path
from simulate import route

rows = json.loads(Path(__file__).with_name('fictional-submissions.json').read_text())
actual = [route(r) for r in rows]
assert [r['route'] for r in actual] == ['Workshop review draft', 'Manual-review record', 'Workshop review draft', 'Manual-review record', 'Manual clarification']
for source, result in zip(rows[:4], actual[:4]):
    target = result['record']
    assert target['Submission ID'] == source['Submission ID']
    assert target['Contact name'] == source['Name']
    assert target['Reply address'] == source['Reply address']
    assert target['Enquiry summary'] == source['Message']
    assert target['Category'] == source['Request type']
assert actual[4]['missing'] == ['Reply address']
assert route({**rows[0], 'Request type': 'workshop request'})['route'] == 'Manual-review record'
assert route(rows[0]) == route(rows[0])
print('PASS: five routes, exact source mapping, missing reply address, case-sensitive equality, repeatable output')
