"""Offline checks for self-authored lesson fixtures; Python 3 standard library only."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parent
names = ["first-weak-output.txt", "v1-factual-correction.txt", "v2-selected-notice.txt", "v3-optional-closing.txt"]
texts = {name: (ROOT / name).read_text(encoding="utf-8") for name in names}
required = ["Riverside Reading Circle", "Saturday, 24 October 2026", "14:00–16:00", "Maple Room, Eastside Community Centre", "Free", "one short public-domain poem", "Register by 20 October", "Registration method not supplied"]
assert "Everyone is welcome" in texts[names[0]]
assert "Register by 20 October" not in texts[names[0]]
for name in names[1:]:
    t = texts[name]
    for fact in required:
        assert fact.casefold() in t.casefold(), (name, fact)
    assert "Everyone is welcome" not in t
    assert len(t.split()) <= 90, name
assert "\nRegister by 20 October.\n" in texts[names[2]]
assert texts[names[3]].startswith(texts[names[2]].rstrip())
assert len(texts[names[3]].split()) > len(texts[names[2]].split())
print(json.dumps({"fixtureChecks": "PASS", "wordCountDefinition": "Python str.split whitespace-separated tokens", "wordCounts": {n: len(t.split()) for n,t in texts.items()}, "registrationMethod": "not supplied; real release held"}, indent=2))
