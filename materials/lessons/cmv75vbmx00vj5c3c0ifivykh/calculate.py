"""Reproduce duration arithmetic; never infer acceptance or missing timing evidence."""
import csv
import re
import statistics
import sys


def seconds(value):
    if not re.fullmatch(r'\d+:[0-5]\d', value):
        raise ValueError('Expected nonnegative minutes:seconds, seconds00–59')
    minutes, secs = map(int, value.split(':'))
    return 60 * minutes + secs


def evaluate(rows):
    results = []
    for row in rows:
        manual = seconds(row['manual'])
        raw = seconds(row['raw_assisted'])
        check = seconds(row['checking_correction'])
        total = seconds(row['total_assisted'])
        if total != raw + check:
            raise ValueError('Total mismatch for ' + row['case'])
        if row['acceptance'] != 'pass':
            results.append({'case': row['case'], 'comparable': False,
                            'total_seconds': total, 'difference_seconds': None})
        else:
            results.append({'case': row['case'], 'comparable': True,
                            'total_seconds': total, 'difference_seconds': manual-total})
    return results


if __name__ == '__main__':
    import json
    with open(sys.argv[1], newline='', encoding='utf8') as f:
        result = evaluate(list(csv.DictReader(f)))
    values = [x['difference_seconds'] for x in result if x['comparable']]
    print(json.dumps({'results': result, 'accepted_count': len(values),
                      'mean_difference_seconds': statistics.mean(values) if values else None,
                      'median_difference_seconds': statistics.median(values) if values else None,
                      'range_seconds': [min(values), max(values)] if values else None}, indent=2))
