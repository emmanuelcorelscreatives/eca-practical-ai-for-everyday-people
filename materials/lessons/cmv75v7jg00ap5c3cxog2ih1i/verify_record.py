"""Offline exact-string exercise. Does not assess legal meaning or urgency."""
import json
from pathlib import Path


def main():
    data = json.loads(Path(__file__).with_name("source-comparison.json").read_text(encoding="utf-8"))
    original = data["original"]
    results = {}
    for item in data["transcriptions"]:
        changed = [field for field in ("printed_response_date", "wording")
                   if item[field] != original[field]]
        if changed != item["expected_changed_fields"]:
            raise SystemExit("FAIL: changed fields do not match expected fixture")
        results[item["id"]] = changed
    passed = results.get("faulty") == ["printed_response_date", "wording"] and results.get("corrected") == []
    print(json.dumps({"passed": passed, "cases_checked": len(results),
                      "faulty_detected": bool(results.get("faulty")),
                      "corrected_preserved": results.get("corrected") == []}))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
