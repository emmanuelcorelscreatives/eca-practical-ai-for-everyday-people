"""Read-only checks of the fictional lesson fixtures; standard library only."""
import csv
import json
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent
with (root / "registrations.csv").open(newline="", encoding="utf-8") as handle:
    registrations = list(csv.DictReader(handle))
assert [r["Registration ID"] for r in registrations] == [f"REG-{i:03d}" for i in range(1, 37)]
with (root / "claim-table-answers.csv").open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))
assert len(rows) == 8
counts = dict(Counter(r["Verification result"] for r in rows))
assert counts == {"Supported": 3, "Corrected": 3, "Unresolved": 1, "Unsupported": 1}
assert all(all(value.strip() for value in row.values()) for row in rows)
capacity = 48
percentage = len(registrations) / capacity * 100
assert percentage == 75
assert "Capacity: 48" in (root / "event-brief.md").read_text(encoding="utf-8")
assert "confirmation pending" in (root / "facilities-note.md").read_text(encoding="utf-8")
revision = (root / "checked-revision.md").read_text(encoding="utf-8").split("\n\n")[1]
assert all(value in revision for value in ["Harbour Room", "75%", "21 October 2026", "awaiting confirmation"])
assert all(value not in revision for value in ["Riverside", "70%", "22 October", "refreshments"])
print(json.dumps({"passed": True, "registrations": len(registrations), "capacity": capacity, "percentage": percentage, "results": counts}, sort_keys=True))
