"""Lesson 213 deterministic local exercise; no network, AI or external actions."""
import csv
import hashlib
import datetime
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQUIRED = ("Request ID", "Contact name", "Contact email", "Requested date", "Request details")

def validate(record):
    missing = [key for key in REQUIRED if not record.get(key, "").strip()]
    if missing:
        return {"validation": "Missing required field", "review": "Needs information", "action": "Stopped", "reason": "Missing " + ", ".join(key.lower() for key in missing)}
    if record.get("Permission to contact") != "Yes":
        return {"validation": "Permission not confirmed", "review": "Needs information", "action": "Stopped", "reason": "Permission to contact must equal Yes"}
    email = record["Contact email"]
    if email.count("@") != 1 or not all(email.split("@")) or " " in email:
        return {"validation": "Invalid contact format", "review": "Needs information", "action": "Stopped", "reason": "Check contact email"}
    try:
        datetime.date.fromisoformat(record["Requested date"])
    except ValueError:
        return {"validation": "Invalid date", "review": "Needs information", "action": "Stopped", "reason": "Check requested date"}
    return {"validation": "Valid", "review": "Awaiting review", "action": "Paused for human review", "reason": ""}

def decide(record, proposal, decision, note):
    state = validate(record)
    if state["validation"] != "Valid":
        return dict(state, proposal="")
    if decision not in ("Approved", "Rejected") or not note.strip():
        raise ValueError("A reviewer must choose Approved or Rejected and record a note")
    return dict(state, proposal=proposal, review=decision, reason=note, action="Internal task update only" if decision == "Approved" else "Stopped")

def review_package(record, proposal, destination="Workshop planning task list"):
    return {"source": dict(record), "proposal": proposal, "intendedAction": "Update internal task", "destination": destination, "assumptions": "None stated"}

def package_key(package):
    return hashlib.sha256(json.dumps(package, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()

def approve_package(package, note):
    state = decide(package["source"], package["proposal"], "Approved", note)
    return {"reviewedPackageSha256": package_key(package), "state": state}

def assess_current_package(package, previous_decision):
    # A training representation only: never a production permission token.
    fresh = validate(package["source"])
    if fresh["validation"] != "Valid":
        return fresh
    if previous_decision["reviewedPackageSha256"] != package_key(package):
        return dict(fresh, reason="Material change requires fresh validation and human review")
    return dict(previous_decision["state"])

def main():
    with (ROOT / "requests.csv").open(newline="", encoding="utf-8") as handle:
        records = {row["Request ID"]: row for row in csv.DictReader(handle)}
    with (ROOT / "review-queue.csv").open(newline="", encoding="utf-8") as handle:
        queue = {row["Request ID"]: row for row in csv.DictReader(handle)}
    assert set(records) == set(queue) == {"EVT-104", "EVT-105", "EVT-106"}
    expected = {"EVT-104": ("Valid", "Awaiting review"), "EVT-105": ("Missing required field", "Needs information"), "EVT-106": ("Valid", "Awaiting review")}
    observations = {}
    for request_id, record in records.items():
        state = validate(record)
        assert (state["validation"], state["review"]) == expected[request_id]
        assert queue[request_id]["Validation result"] == state["validation"]
        assert queue[request_id]["Review status"] == state["review"]
        observations[request_id] = state
    assert records["EVT-105"]["Requested date"] == queue["EVT-105"]["Proposal"] == ""
    approved = decide(records["EVT-104"], queue["EVT-104"]["Proposal"], "Approved", "Checked against source")
    assert approved["action"] == "Internal task update only"
    rejected = decide(records["EVT-106"], queue["EVT-106"]["Proposal"], "Rejected", "Unsupported accessibility confirmation")
    assert rejected["validation"] == "Valid" and rejected["action"] == "Stopped"
    incomplete = decide(records["EVT-105"], "must not proceed", "Approved", "Not a valid override")
    assert incomplete["review"] == "Needs information" and incomplete["proposal"] == "" and incomplete["action"] == "Stopped"
    assert validate(dict(records["EVT-104"], **{"Contact email": ""}))["action"] == "Stopped"
    assert validate(dict(records["EVT-104"], **{"Permission to contact": "No"}))["action"] == "Stopped"
    assert validate(dict(records["EVT-104"], **{"Requested date": "2026-02-30"}))["validation"] == "Invalid date"
    package = review_package(records["EVT-104"], queue["EVT-104"]["Proposal"])
    original_decision = approve_package(package, "Checked against source")
    assert assess_current_package(package, original_decision)["review"] == "Approved"
    changed_packages = [
        dict(package, proposal=package["proposal"] + " Changed wording for review."),
        dict(package, destination="Different internal task list"),
        dict(package, source=dict(package["source"], **{"Requested date": "2026-10-23"})),
        dict(package, source=dict(package["source"], **{"Contact email": "other@example.org"})),
        dict(package, intendedAction="Different internal action"),
    ]
    for changed in changed_packages:
        state = assess_current_package(changed, original_decision)
        assert state["validation"] == "Valid" and state["review"] == "Awaiting review" and state["action"] == "Paused for human review"
    missing_after_review = dict(package, source=dict(package["source"], **{"Requested date": ""}))
    assert assess_current_package(missing_after_review, original_decision)["action"] == "Stopped"
    print(json.dumps({"passed": True, "sourceRecords": observations, "approved": approved, "rejected": rejected, "externalActions": 0, "note": "Local deterministic exercise assertions; no platform run or AI generation claimed"}, indent=2))

if __name__ == "__main__":
    main()
