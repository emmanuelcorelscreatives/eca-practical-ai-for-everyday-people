from pathlib import Path
import json,csv
root=Path(__file__).resolve().parent
expected={"Name placeholder":"Sample Person","Event choice":"Morning session","Note":"Please provide accessibility information."}
assert json.loads((root/"sample-response.json").read_text())==expected
with (root/"sample-response.csv").open(newline="") as f:
    assert list(csv.DictReader(f))==[expected]
with (root/"permission-cases.csv").open(newline="") as f:
    rows=list(csv.DictReader(f))
assert [r["Case"] for r in rows]==list("ABCDEF")
assert all(not r["Your decision"] and not r["Your reason"] for r in rows)
assert (root/"practice.html").is_file()
print("PASS: exact fictional three-field sample, six blank decision cases, local practice page present. No live access checked.")
