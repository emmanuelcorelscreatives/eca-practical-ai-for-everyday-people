"""Exact arithmetic for fictional lesson examples. Keep closed during attempts."""
from fractions import Fraction
from statistics import median
import json

CASES = [
    ('worked', [2, 3, 3, 4, 18], 30, Fraction(6), 3),
    ('first', [4, 5, 5, 6, 20], 40, Fraction(8), 5),
    ('second', [3, 4, 4, 5, 19], 35, Fraction(7), 4),
    ('comparison', [5, 5, 6, 6, 7], 29, Fraction(29, 5), 6),
]
results = []
for name, values, expected_sum, expected_mean, expected_median in CASES:
    total = sum(values)
    mean = Fraction(total, len(values))
    middle = median(values)
    assert (total, mean, middle) == (expected_sum, expected_mean, expected_median)
    results.append(dict(example=name, ordered_values=sorted(values), total=total,
                        observations=len(values), mean=str(mean), median=middle))
print(json.dumps({'checks': 'PASS', 'examples': results}, indent=2))
