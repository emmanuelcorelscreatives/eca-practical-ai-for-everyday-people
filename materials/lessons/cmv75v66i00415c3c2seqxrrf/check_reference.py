from pathlib import Path
p=Path(__file__).with_name("checked-notice.txt").read_text(encoding="utf-8").strip()
heading, body=p.split("\n",1)
assert heading=="Community Garden Cleanup"
assert "\n" not in body
assert len(p.split())==78
assert 70<=len(p.split())<=90
for fact in ["17 May 2027","09:00 to 11:00","Riverside Community Garden","Bring gloves","20 places","Missing information:"]:
    assert fact in p, fact
assert p.endswith("Register by 12 May 2027.")
for invented in ["refreshments provided","fun for the whole family"]:
    assert invented not in p.lower()
print("PASS: stored reference mechanical checks; compare all claims with source manually.")
