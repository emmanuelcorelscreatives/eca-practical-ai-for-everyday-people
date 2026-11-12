"""Check supplied teaching fixtures; no network, model, or learner grading."""
import csv
from pathlib import Path

root = Path(__file__).resolve().parent
source = (root / 'source-notes.txt').read_text(encoding='utf-8')
with (root / 'practice-claims.csv').open(encoding='utf-8', newline='') as handle:
    claims = list(csv.DictReader(handle))
with (root / 'answer-fixtures.csv').open(encoding='utf-8', newline='') as handle:
    answers = list(csv.DictReader(handle))

expected_labels = [
    'Directly stated', 'Interpretation', 'Directly stated', 'Interpretation',
    'Interpretation', 'Directly stated', 'Interpretation', 'Interpretation',
    'Missing information', 'Missing information', 'Missing information',
    'Directly stated', 'Interpretation', 'Missing information',
    'Directly stated', 'Interpretation', 'Interpretation', 'Missing information',
]
assert len(claims) == len(answers) == len(expected_labels) == 18
assert len({row['claim_id'] for row in claims}) == 18
for claim, answer, expected in zip(claims, answers, expected_labels):
    assert claim['claim_id'] == answer['claim_id']
    assert answer['label'] == expected, claim['claim_id']
    quotation = answer['exact_source_support']
    if expected == 'Directly stated':
        assert quotation and quotation == claim['claim'] and quotation in source
    else:
        assert quotation == ''

assert (8 * 60 + 25) - (8 * 60 + 10) == 15
assert 12 - 8 == 4
print('PASS: 18 fixture classifications; 2 arithmetic checks; exact source quotations')
