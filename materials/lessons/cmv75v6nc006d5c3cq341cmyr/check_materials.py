from pathlib import Path
import csv, datetime, json
p=Path(__file__).resolve().parent
assert datetime.date(2026,10,17).strftime("%A")=="Saturday"
with (p/"comparison-answer.csv").open(newline="",encoding="utf-8") as f:
    rows=list(csv.DictReader(f))
assert len(rows)==6
assert rows[3]["STATUS"]=="UNRESOLVED"
assert rows[5]["GENERATED CRITIQUE"]=="Not mentioned"
assert all(r["OPENED EVIDENCE"] and r["CORRECTION"] for r in rows)
with (p/"comparison-diagnosis-only.csv").open(newline="",encoding="utf-8") as f:
    diagnosis=list(csv.DictReader(f))
assert len(diagnosis)==5
assert all(not r[k] for r in diagnosis for k in ["OPENED EVIDENCE","STATUS","CORRECTION"])
r=(p/"checked-revision.md").read_text(encoding="utf-8")
count=len(r.split()); assert count<=120
assert sum(line.startswith("- ") for line in r.splitlines())==5
for exact in ["Saturday, 17 October 2026", "10:00–13:00", "meeting room", "15 October", "one small household item", "repair is not guaranteed"]:
    assert exact in r, exact
assert "parking" not in r.lower() and "accessibility" not in r.lower()
print(json.dumps({"state":"PASS", "fictionalExerciseOnly":True,"answerRows":len(rows),"revisionWhitespaceWordsIncludingBulletMarkers":count,"weekday":"Saturday","diagnosisEvidenceBlank":True},indent=2))
