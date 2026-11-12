import copy, json, pathlib
HERE = pathlib.Path(__file__).resolve().parent
source = json.loads((HERE / "sample-input.json").read_text())
good = json.loads((HERE / "simulated-draft.json").read_text())
required = ["Request ID", "Category", "Title", "Date", "Time", "Location"]
labels = ["Request ID", "Event details", "Draft summary", "Assumptions", "Missing information", "Review status"]
def input_errors(record):
    errors = ["Missing " + key for key in required if not isinstance(record.get(key), str) or not record[key].strip()]
    if record.get("Category") not in ["Workshop", "Meeting"]: errors.append("Category not allowed")
    return errors
def draft_errors(record, draft):
    errors = input_errors(record)
    errors += ["Missing label " + key for key in labels if key not in draft]
    if draft.get("Request ID") != record["Request ID"]: errors.append("Changed ID")
    details = draft.get("Event details", {})
    for key in ["Title", "Date", "Time", "Location"]:
        if not isinstance(details, dict) or details.get(key) != record[key]: errors.append("Changed " + key)
    summary = draft.get("Draft summary", "")
    if not isinstance(summary, str) or len(summary.split()) >= 70: errors.append("Summary too long or invalid")
    # Finite fixture check only: unfamiliar wording always needs human source review.
    if summary != good["Draft summary"]: errors.append("Summary requires human source comparison")
    if draft.get("Assumptions") != "None": errors.append("Assumptions require review")
    if draft.get("Missing information") != "Accessibility details: Not supplied.": errors.append("Missing information changed")
    if draft.get("Review status") != "Draft only — human review required.": errors.append("Invalid review boundary")
    return errors
assert not draft_errors(source, good)
results = [{"case": "authored-valid-simulation", "result": "accepted"}]
for name in ["missing-time", "wrong-category", "changed-date", "unsupported-claim", "missing-label", "invented-access"]:
    record, draft = copy.deepcopy(source), copy.deepcopy(good)
    if name == "missing-time": record["Time"] = ""
    if name == "wrong-category": record["Category"] = "workshop"
    if name == "changed-date": draft["Event details"]["Date"] = "Wednesday 21 October 2026"
    if name == "unsupported-claim": draft["Draft summary"] += " Suitable for all bicycles."
    if name == "missing-label": del draft["Missing information"]
    if name == "invented-access": draft["Missing information"] = "Accessibility is guaranteed."
    errors = draft_errors(record, draft)
    assert errors, name
    results.append({"case": name, "result": "rejected", "reasons": errors})
print(json.dumps({"state": "PASS", "scope": "local finite fixtures, not AI or platform validation", "results": results}, indent=2))
