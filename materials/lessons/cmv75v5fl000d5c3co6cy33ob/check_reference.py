from pathlib import Path
import re,sys
p=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).with_name("expected-checklist.md")
s=p.read_text(encoding="utf-8"); low=s.lower()
phrases=("wipe shelves","label spice jars","sort papers","place umbrella basket","timing not supplied")
missing=[x for x in phrases if x not in low]
actions=[x.strip().lower() for x in re.findall(r"^- \[ \] (.+)$",s,re.M)]
extra=[x for x in actions if x not in phrases[:4]]
deadline=bool(re.search(r"\b(friday|monday|tuesday|wednesday|thursday|saturday|sunday|deadline|by tomorrow)\b|\d{4}-\d{2}-\d{2}",low))
if missing or extra or deadline:
 print({"missing_exact_phrases":missing,"extra_checklist_items":extra,"possible_invented_deadline":deadline,"manual_review_required":True});sys.exit(1)
print("Reference phrase checks passed. Compare every item, category and missing detail manually; this is not semantic or safety approval.")
