"""Academy self-authored offline simulator: no network or publishing operations."""
import json
from pathlib import Path

def route(record):
    decision = record.get("decision", "")
    complete = all(isinstance(record.get(k),str) and record[k].strip() for k in ("reviewedVersion","currentVersion","reviewedDestination","currentDestination","reviewedContent","currentContent")) and all(isinstance(record.get(k),list) and all(isinstance(x,str) and x.strip() for x in record[k]) for k in ("reviewedAttachments","currentAttachments"))
    same = bool(complete) and all(record.get(a) == record.get(b) for a,b in [
        ("reviewedVersion","currentVersion"),("reviewedDestination","currentDestination"),
        ("reviewedContent","currentContent"),("reviewedAttachments","currentAttachments")])
    if decision == "Rejected": status,queue="Blocked","Rejected archive"
    elif decision == "Edit": status,queue="Review required","Changes requested"
    elif decision == "Approved" and same: status,queue="Simulated action","Simulated action log"
    elif decision == "Approved": status,queue="Review required","Pending review"
    elif decision == "": status,queue="Pending","Pending review"
    else: status,queue="Manual review required","Pending review"
    accountability = {k:record.get(k,"") for k in ("reviewerRole","decisionTime","decision","reason","reviewedVersion","reviewedDestination")}
    accountability["supportingInformationReference"] = record.get("reviewedAttachments",[])
    return {"decisionRecord":accountability,"archiveRecord":dict(accountability, id=record["id"]) if decision=="Rejected" else None,"simulatedOwnerNotification":"SIMULATED ONLY: workflow owner notified of rejection" if decision=="Rejected" else None,"approvalFieldsComplete":bool(complete),"id":record["id"],"status":status,"queue":queue,"actionReached":status=="Simulated action","realExternalAction":False,"versionDestinationContentAttachmentsMatch":same}

if __name__ == "__main__":
    root=Path(__file__).parent
    cases=json.loads((root/"cases.json").read_text())
    print(json.dumps([route(r) for r in cases],indent=2))
