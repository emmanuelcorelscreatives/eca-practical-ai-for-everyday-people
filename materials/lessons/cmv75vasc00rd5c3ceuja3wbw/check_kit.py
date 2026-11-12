from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parent
expected="The Riverside Community Garden open morning begins at ten o’clock this Saturday. Please bring a reusable cup."
assert (ROOT/"announcement.txt").read_text().strip()==expected
schemas={"rights-register.csv":["asset","owner_or_provider","intended_use","actual_terms_url","checked_date","plan_and_region","permission_evidence","restrictions_or_unknowns","decision"],"listening-review.csv":["take","script_phrase","actually_heard","issue_or_observation","action","recheck_observation","playback_device","reviewer","date"]}
for name,fields in schemas.items():
    with (ROOT/name).open(newline="") as f:
        r=csv.DictReader(f);assert r.fieldnames==fields
        rows=list(r);assert rows
        if name=="listening-review.csv":assert all(not any(row.values()) for row in rows), "Blank observation worksheet required"
assert "Narration generated with an authorized synthetic voice." in (ROOT/"disclosure.txt").read_text()
print("PASS: exact announcement, schemas, blank observation evidence and disclosure; no audio or permissions judged")
