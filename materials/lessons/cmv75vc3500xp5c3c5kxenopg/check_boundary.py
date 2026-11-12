"""Functional checks, including negative cases that could otherwise bypass approval."""
import copy
import json
from pathlib import Path
from boundary_lab import run

cases = json.loads(Path(__file__).with_name('cases.json').read_text())
history, rows = run(cases)
assert len(rows) == 1 and rows[0]['case_id'] == 'CONTROL-204-A'
assert [r['action'] for r in history] == ['Completed', 'Not run', 'Not run']
assert history[1]['validation'] == 'Complete' and history[1]['decision'] == 'Reject'
assert history[2]['missing_fields'] == ['destination'] and history[2]['decision'] == 'Approve'
for name, change in [
    ('Changed reviewed version', {'proposal_version':2}),
    ('Content changed without version increment', {'final_content':'Different unreviewed content'}),
    ('Context changed without version increment', {'supporting_information':'Different unreviewed context'}),
    ('Case ID changed without version increment', {'case_id':'CONTROL-204-OTHER'}),
    ('Unknown decision', {'decision':'Response received'}),
    ('Production mode', {'test_mode':False}),
    ('Other destination', {'destination':'Production records'}),
    ('Wrong action', {'proposed_action':'Send email'}),
    ('Whitespace content', {'final_content':'   '})]:
    altered=copy.deepcopy(cases[0]);altered.update(change)
    h,r=run([altered]);assert not r and h[0]['action']=='Not run', name
try:
    run([cases[0],cases[0]])
except ValueError:
    pass
else:
    raise AssertionError('Duplicate case IDs must not create duplicate records')
print('PASS: 3 authored outcomes, 9 bypass guards including equal-version content/context/ID changes, duplicate ID refusal')
