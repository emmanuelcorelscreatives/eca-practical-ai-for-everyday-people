from pathlib import Path
import csv,json,importlib.util,wave
p=Path(__file__).parent
rows=list(csv.DictReader((p/"event-costs.csv").open()))
assert len(rows)==3
assert [int(r["Estimated Cost"]) for r in rows]==[24,18,12]
assert sum(int(r["Estimated Cost"]) for r in rows)==54
source=(p/"community-garden-source.txt").read_text().strip()
assert (p/"transcript-corrected.txt").read_text().strip()==source
assert (p/"transcript-before.txt").read_text().strip()==source.replace("three seed tables","free seed tables",1)
assert "Location: Not provided" in (p/"poster-copy.txt").read_text()
with wave.open(str(p/"community-garden-afternoon.wav"),"rb") as w: assert w.getnframes()>0 and w.getframerate()>0
spec=importlib.util.spec_from_file_location("review",p/"workflow-review.py");m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
results=[m.evaluate(x) for x in ["approve","reject","hold"]]
assert all(r["externalActionExecuted"] is False for r in results)
assert [r["status"] for r in results]==["approved_draft_only","stopped_after_review","awaiting_review"]
assert all(r["draft"]=="event-brief.md" and len(r["draftSha256"])==64 for r in results)
print(json.dumps({"state":"PASS","estimated_total_USD":54,"source_transcript_exact":True,"seeded_text_error":"free -> three","audio_word_accuracy":"learner listening required; no acoustic verdict claimed","workflow_paths":results},indent=2))
