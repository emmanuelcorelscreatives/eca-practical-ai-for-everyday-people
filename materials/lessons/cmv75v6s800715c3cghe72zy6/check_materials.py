from pathlib import Path
import json
p = Path(__file__).resolve().parent
blank = (p / "blank-master.txt").read_text()
filled = (p / "filled-practice-copy.txt").read_text()
missing = (p / "missing-date-copy.txt").read_text()
data = json.loads((p / "fictional-event-inputs.json").read_text())
assert data["fictional"] is True
for key, value in {**data["required"], **data["optional"]}.items():
    assert "[" + key + "]" in blank
    assert value in filled
assert "[" not in filled
assert "Event date: \n" in missing
assert "Event date: 7 November 2026" not in missing
example = (p / "human-written-practice-announcement.txt").read_text().split("\n\n", 1)[1]
count = len(example.split())
assert 80 <= count <= 120, count
print(f"PASS: supplied blank, complete and missing-date fixtures; human-written example {count} words")
