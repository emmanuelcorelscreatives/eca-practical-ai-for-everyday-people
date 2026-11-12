"""Fictional sequential Academy exercise; no network or external task writes."""
import argparse
import csv
import sys

COLUMNS = ['Source ID', 'Checked at', 'Run reference', 'Decision', 'Reason', 'Output reference']

class Practice:
    def __init__(self):
        self.tasks = {}
        self.log = []

    def receive(self, source_id, request_type, details, checked_at, run_reference, lookup_available=True):
        source_id = source_id.strip()
        if not source_id:
            return {'state': 'held', 'reason': 'Stable source identifier required'}
        if not lookup_available:
            return {'state': 'held', 'reason': 'Lookup unavailable; inspect manually before creation'}
        matches = [row for row in self.log if row['Source ID'] == source_id]
        if matches:
            output = matches[0]['Output reference']
            task = self.tasks.get(output)
            if task is None:
                return {'state': 'held', 'reason': 'Logged destination missing; reconcile before retry'}
            if task['details'] != details or task['request_type'] != request_type:
                return {'state': 'held', 'reason': 'Same source ID has changed content; human review required', 'output': output}
            decision, reason = 'Duplicate — no new output', 'Existing Source ID found'
        else:
            # Detect an interrupted prior write even if its log row is missing.
            orphan = next((key for key, task in self.tasks.items() if task['source_id'] == source_id), None)
            if orphan:
                return {'state': 'held', 'reason': 'Destination exists without log; reconcile before retry', 'output': orphan}
            output = 'TASK-' + str(31 + len(self.tasks)).zfill(3)
            self.tasks[output] = {'title': 'Review room-setup request', 'request_type': request_type,
                                  'details': details, 'source_id': source_id, 'status': 'Awaiting review'}
            decision, reason = 'New — sent for review', 'No existing Source ID found'
        row = dict(zip(COLUMNS, [source_id, checked_at, run_reference, decision, reason, output]))
        self.log.append(row)
        return {'state': 'recorded', 'row': dict(row), 'task_count': len(self.tasks)}


def demo():
    practice = Practice()
    practice.receive('REQ-1047', 'Room setup', 'Arrange twelve chairs.', '2026-10-15 13:10 UTC', 'RUN-001')
    practice.receive('REQ-1047', 'Room setup', 'Arrange twelve chairs.', '2026-10-15 13:14 UTC', 'RUN-002')
    writer = csv.DictWriter(sys.stdout, fieldnames=COLUMNS, lineterminator='\n')
    writer.writeheader()
    writer.writerows(practice.log)
    print('Review tasks:', len(practice.tasks), file=sys.stderr)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--demo', action='store_true', help='Print the lesson two-run fictional demonstration')
    args = parser.parse_args()
    if args.demo:
        demo()
    else:
        parser.print_help()
