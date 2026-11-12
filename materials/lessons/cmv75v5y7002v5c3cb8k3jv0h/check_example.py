from pathlib import Path
r=Path(__file__).parent
notes=(r/'notes.txt').read_text().strip()
expected=['Put the water bottle by the door.','Pack the phone charger.','Download the route map.','Leave at 08:15.','Check that the windows are closed.']
assert notes==' '.join(expected)
lines=[x for x in (r/'checklist.md').read_text().splitlines() if x.startswith('- [ ] ')]
assert lines==['- [ ] '+x for x in expected]
assert '08:50' not in '\n'.join(lines)
print('PASS: five exact source actions, five checkboxes, no additions, 08:15 preserved')
