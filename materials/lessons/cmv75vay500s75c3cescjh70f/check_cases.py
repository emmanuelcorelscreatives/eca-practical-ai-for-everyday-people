from pathlib import Path
import json
root = Path(__file__).resolve().parent
cases = json.loads((root / "cases.json").read_text(encoding="utf-8"))
expected = {"A": "supported", "B": "unsupported", "C": "incorrect", "D": "unsupported", "E": "supported-with-uncertainty"}
assert len(cases) == 5 and {c["id"] for c in cases} == set(expected)
for case in cases:
    assert case["classification"] == expected[case["id"]]
    assert (root / case["image"]).is_file()
original = (root / "poster-original.svg").read_text(encoding="utf-8")
low = (root / "poster-low-detail.svg").read_text(encoding="utf-8")
assert "Room B • 14:30 • 21 June" in original
assert "Room B" not in low and "14:30" not in low and "21 June" not in low
assert "Small-print region intentionally obscured" in low
print("PASS: 5 fictional cases classified; supplied text and uncertainty preserved.")
