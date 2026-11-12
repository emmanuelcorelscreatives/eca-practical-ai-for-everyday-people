"""Execute source-matching practice checks using only the Python standard library."""
import csv
import pathlib
from duplicate_practice import Practice


def main():
    p = Practice()
    first = p.receive('REQ-1047', 'Room setup', 'Arrange twelve chairs.', '2026-10-15 13:10 UTC', 'RUN-001')
    repeat = p.receive('REQ-1047', 'Room setup', 'Arrange twelve chairs.', '2026-10-15 13:14 UTC', 'RUN-002')
    assert first['state'] == repeat['state'] == 'recorded'
    assert len(p.tasks) == 1 and len(p.log) == 2
    assert p.tasks['TASK-031']['status'] == 'Awaiting review'
    assert p.tasks['TASK-031']['details'] == 'Arrange twelve chairs.'
    with pathlib.Path(__file__).with_name('decision-log-expected.csv').open(newline='', encoding='utf-8') as handle:
        assert p.log == list(csv.DictReader(handle))
    before = (len(p.tasks), len(p.log))
    assert p.receive('REQ-1047', 'Room setup', 'Arrange sixteen chairs.', 'fictional later time', 'RUN-003')['state'] == 'held'
    assert p.receive('', 'Room setup', 'Arrange twelve chairs.', 'fictional later time', 'RUN-004')['state'] == 'held'
    assert p.receive('REQ-1100', 'Room setup', 'Arrange ten chairs.', 'fictional later time', 'RUN-005', False)['state'] == 'held'
    assert (len(p.tasks), len(p.log)) == before
    assert p.receive('REQ-1088', 'Room setup', 'Arrange twelve chairs.', 'fictional later time', 'RUN-006')['state'] == 'recorded'
    assert len(p.tasks) == 2 and len(p.log) == 3
    p.log = [row for row in p.log if row['Source ID'] != 'REQ-1047']
    assert p.receive('REQ-1047', 'Room setup', 'Arrange twelve chairs.', 'fictional later time', 'RUN-007')['state'] == 'held'
    assert len(p.tasks) == 2
    p.tasks.pop('TASK-032')
    assert p.receive('REQ-1088', 'Room setup', 'Arrange twelve chairs.', 'fictional later time', 'RUN-008')['state'] == 'held'
    print('PASS: exact two-run log; one task; changed-content hold; missing-ID hold; lookup-failure hold; separate-ID; partial-write reconciliation; missing-destination reconciliation')

if __name__ == '__main__':
    main()
