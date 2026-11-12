import json,sys,hashlib
from pathlib import Path
VALID={"approve":"approved_draft_only","reject":"stopped_after_review","hold":"awaiting_review"}
def evaluate(decision):
    if decision not in VALID: raise ValueError("Use approve, reject or hold")
    draft=Path(__file__).with_name("event-brief.md").read_bytes()
    return {"exercise":"Academy offline metadata-only state model; not Zapier", "decision":decision,"status":VALID[decision],"externalActionExecuted":False,"draft":"event-brief.md","draftSha256":hashlib.sha256(draft).hexdigest(),"proposedDestination":"local review folder; no folder is created or file copied","sideEffects":"prints metadata only"}
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Usage: python3 workflow-review.py approve|reject|hold")
    print(json.dumps(evaluate(sys.argv[1]),indent=2))
