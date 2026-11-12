from pathlib import Path
import csv,json
r=Path(__file__).resolve().parent
def load(n):
 with (r/n).open(newline="") as f:return list(csv.DictReader(f))
s=load("source-cards.csv");e=load("expected-corrections.csv");t=load("simulated-transcripts.csv")
assert {x["id"] for x in s}=={"lamp","name","quantity","date"}
assert len(s)==len(e)==len(t)==4
assert {x["id"]:x["intended_text"] for x in s}=={x["id"]:x["corrected_text"] for x in e}
assert all("simulated" in x["status"] for x in t)
assert "Maara" in e[1]["corrected_text"] and "50" in e[2]["corrected_text"] and "6 July 2027" in e[3]["corrected_text"]
print(json.dumps({"status":"PASS","rows":4,"scope":"fixture and expected answers only; no ASR or device observation"}))
