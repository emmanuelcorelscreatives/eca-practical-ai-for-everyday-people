"""Check the lesson's actual routing outputs, not a claimed external action."""
import json,csv,io
from pathlib import Path
from route_engine import route
root=Path(__file__).parent
cases=json.loads((root/"cases.json").read_text())
expected={r["record_id"]:r for r in csv.DictReader((root/"expected-results.csv").open())}
results=[]
for record in cases:
    out=route(record); exp=expected[record["id"]]
    assert out["status"]==exp["expected_status"],out
    assert str(out["actionReached"]).lower()==exp["action_reached"],out
    assert out["realExternalAction"] is False,out
    results.append(out)
assert len(results)==9 and sum(r["actionReached"] for r in results)==1
assert route(dict(cases[0],decision="approved"))["actionReached"] is False
assert route(dict(cases[0],decision=None))["actionReached"] is False
negative=0
for key in ("reviewedVersion","currentVersion","reviewedDestination","currentDestination","reviewedContent","currentContent","reviewedAttachments","currentAttachments"):
    for value in (None, ""):
        bad=dict(cases[0]);bad[key]=value
        assert not route(bad)["actionReached"],(key,value)
        negative+=1
    missing=dict(cases[0]);missing.pop(key)
    assert not route(missing)["actionReached"],key
    negative+=1
both_missing={"id":"MISSING","decision":"Approved"}
assert not route(both_missing)["actionReached"]
rejected=route(cases[1])
assert rejected["archiveRecord"]["reason"]=="Start time is missing"
assert rejected["decisionRecord"]["reviewerRole"]=="Event communications reviewer"
assert rejected["simulatedOwnerNotification"].startswith("SIMULATED ONLY")
print(json.dumps({"state":"COMPLETE","pass":True,"cases":results,"extraUnknownCaseChecks":2,"incompleteApprovalNegativeChecks":negative+1,"rejectionReasonAndNotificationRetained":True},indent=2))
