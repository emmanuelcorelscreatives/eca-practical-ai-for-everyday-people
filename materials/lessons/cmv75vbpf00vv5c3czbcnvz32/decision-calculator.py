"""Offline arithmetic aid. Inputs are minutes, not measured unless you measured them."""
import json,math,sys
REQUIRED=("runs","manual_minutes_per_run","setup_minutes","testing_minutes","review_minutes_per_run","correction_minutes_per_run","monitoring_minutes_per_run","maintenance_minutes_per_period")
def compare(d):
    for key in REQUIRED:
        value=d[key]
        if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value) or value<0:
            raise ValueError(key+" must be a finite nonnegative number; unknown is not zero")
    if int(d["runs"])!=d["runs"]: raise ValueError("runs must be a whole number")
    manual=d["runs"]*d["manual_minutes_per_run"]
    automation=d["setup_minutes"]+d["testing_minutes"]+d["runs"]*(d["review_minutes_per_run"]+d["correction_minutes_per_run"]+d["monitoring_minutes_per_run"])+d["maintenance_minutes_per_period"]
    return {"manual_total_minutes":manual,"automation_total_minutes":automation,"manual_minus_automation_minutes":manual-automation,"interpretation":"Arithmetic comparison only; assess risk, uncertainty, cost and manual fallback separately."}
if __name__=="__main__":
    if len(sys.argv)!=2: raise SystemExit("Usage: python3 decision-calculator.py INPUT.json")
    with open(sys.argv[1],encoding="utf-8") as stream: data=json.load(stream)
    print(json.dumps(compare(data),indent=2))
