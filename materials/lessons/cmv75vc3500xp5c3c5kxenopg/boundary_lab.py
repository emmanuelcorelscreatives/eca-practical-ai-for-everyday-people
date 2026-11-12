"""Academy offline boundary model; NOT a Zapier or Google Sheets integration."""
import csv
import json
from datetime import datetime, timezone
from pathlib import Path
import argparse

DESTINATION = 'Approval Boundary Test Log'
REQUIRED = ('case_id', 'proposed_action', 'destination', 'final_content')
REVIEWED_FIELDS = ('case_id', 'proposed_action', 'destination', 'final_content', 'supporting_information', 'test_mode', 'proposal_version')


def run(cases):
    history, rows, seen = [], [], set()
    for case in cases:
        case_id = case.get('case_id', '')
        if not case_id or case_id in seen:
            raise ValueError('Every case needs a unique nonempty case_id')
        seen.add(case_id)
        missing = [key for key in REQUIRED if not isinstance(case.get(key), str) or not case[key].strip()]
        complete = not missing
        decision = case.get('decision')
        reviewed = case.get('reviewed_proposal')
        unchanged = (isinstance(reviewed, dict)
                     and all(key in reviewed and key in case and reviewed[key] == case[key] for key in REVIEWED_FIELDS)
                     and case.get('proposal_version') == case.get('reviewed_version')
                     and type(case.get('proposal_version')) is int)
        test_safe = case.get('test_mode') is True and case.get('destination') == DESTINATION and case.get('proposed_action') == 'Add a test record'
        allowed = complete and decision == 'Approve' and unchanged and test_safe
        timestamp = datetime.now(timezone.utc).isoformat()
        status = {'timestamp': timestamp, 'case_id': case_id, 'validation': 'Complete' if complete else 'Incomplete',
                  'decision': decision, 'missing_fields': missing, 'reviewed_version_unchanged': unchanged,
                  'test_destination_allowed': test_safe, 'gate': 'Passed' if allowed else 'Stopped',
                  'action': 'Completed' if allowed else 'Not run', 'destination': case.get('destination', '')}
        history.append(status)
        if allowed:
            rows.append({'timestamp': timestamp, 'case_id': case_id, 'validation': 'Complete', 'decision': decision,
                         'proposed_action': case['proposed_action'], 'result': case['final_content']})
    return history, rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cases', type=Path, default=Path(__file__).with_name('cases.json'))
    parser.add_argument('--output', type=Path, required=True, help='New directory only: preserves every earlier evidence run')
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text(encoding='utf-8'))
    history, rows = run(cases)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / 'run-history.json').write_text(json.dumps(history, indent=2)+'\n', encoding='utf-8')
    with (args.output / 'test-log.csv').open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['timestamp','case_id','validation','decision','proposed_action','result'])
        writer.writeheader(); writer.writerows(rows)
    summary = {'evidence_scope': 'Actual local Python model execution only; not vendor history or online spreadsheet evidence',
               'total_records': len(rows), 'counts_by_case': {case['case_id']: sum(row['case_id'] == case['case_id'] for row in rows) for case in cases},
               'external_actions': 'Disabled: this program imports no network or messaging client and only writes its new output directory'}
    (args.output / 'summary.json').write_text(json.dumps(summary, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
