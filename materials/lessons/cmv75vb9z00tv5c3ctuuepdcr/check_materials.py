"""Local consistency check of fixed fictional exercise data; no AI or user-work grading."""
from pathlib import Path
import csv, datetime
root = Path(__file__).parent
assert datetime.date(2026, 11, 14).strftime("%A") == "Saturday"
rows = list(csv.DictReader((root / "field-review.csv").open(encoding="utf-8", newline="")))
assert len(rows) == 9 and len({r["Field"] for r in rows}) == 9
by = {r["Field"]: r for r in rows}
assert by["Date"]["Approved input"] == "Saturday, 14 November 2026"
assert by["Date"]["Practice draft"] == "Saturday, 14 November 2027"
assert by["Capacity"]["Approved input"] == "Maximum 20 participants"
assert by["Capacity"]["Practice draft"] == "Maximum 25 participants"
assert by["Registration fee"]["Practice draft"] == "£5"
final = (root / "checked-review-copy.md").read_text(encoding="utf-8")
for value in ("Saturday, 14 November 2026", "10:00–12:00", "Community learning room", "Maximum 20 participants", "Contact: MISSING", "Accessibility: MISSING"):
    assert value in final, value
assert "£5" not in final and "2027" not in final and "Maximum 25" not in final
print("PASS: 9 fixture fields, supported corrections, exact date and both visible gaps; human document review still required.")
