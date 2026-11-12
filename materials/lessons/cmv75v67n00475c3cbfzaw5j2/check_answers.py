#!/usr/bin/env python3
"""Optional exact-field exercise checks; not a prose/model quality verifier."""
import json
import pathlib
import sys

DATA = json.loads(pathlib.Path(__file__).with_name("practice-data.json").read_text())

def check(response):
    expected = DATA["structured_response"]
    issues = []
    if not isinstance(response, dict):
        return ["Response must be a JSON object"]
    for key in expected:
        if response.get(key) != expected[key]:
            issues.append(f"{key}: expected {expected[key]!r}, received {response.get(key)!r}")
    return issues

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 check_answers.py --demo | response.json")
    response = DATA["structured_response"] if sys.argv[1] == "--demo" else json.loads(pathlib.Path(sys.argv[1]).read_text())
    issues = check(response)
    print(json.dumps({"exact_structured_fields_pass": not issues, "issues": issues,
        "scope": "Only these exact structured practice fields; manually check prose, sentence structure, facts and meaning."}, indent=2))
    raise SystemExit(1 if issues else 0)
