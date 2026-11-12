from pathlib import Path
import csv, datetime
root = Path(__file__).resolve().parent
text = (root / "corrected-checklist.md").read_text()
assert text.count("- [ ] ") == 6
assert text.count("Owner to confirm.") == 4
for phrase in ("3 folding tables", "13:30", "40 blank name labels", "2 black markers", "Do not buy refreshments", "Mateo printed 20 signs already.", "If rain is forecast on Friday evening", "Ask Lina whether", "step-free entrance", "21 October 2026", "24 October 2026", "14:00–16:00"):
    assert phrase in text, phrase
assert datetime.date(2026, 10, 24).strftime("%A") == "Saturday"
assert datetime.date(2026, 10, 21).strftime("%A") == "Wednesday"
with (root / "two-way-audit.csv").open(newline="") as f:
    rows = list(csv.DictReader(f))
assert [int(r["source_line"]) for r in rows] == list(range(1,10))
with (root / "correction-record.csv").open(newline="") as f:
    assert len(list(csv.DictReader(f))) == 8
print("PASS: six actions, four owner gaps, nine source lines, eight corrections, dates and exact reference details")
