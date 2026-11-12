import json
from pathlib import Path
ROOT = Path(__file__).resolve().parent
REQUIRED = ("event_name", "date", "time", "location", "audience", "approved_description", "response_method", "review_owner")
def check(brief):
    missing = [name for name in REQUIRED if not str(brief.get(name, "")).strip()]
    return {"may_begin_draft": brief.get("readiness") == "READY FOR DRAFTING" and not missing, "missing": missing, "human_checks_required": ["confirmed usable fields", "contradictions", "compare generated facts", "review owner before sharing"]}
if __name__ == "__main__":
    for name in ("complete-brief.json", "incomplete-brief.json"):
        print(name, json.dumps(check(json.loads((ROOT / name).read_text(encoding="utf-8")))))
