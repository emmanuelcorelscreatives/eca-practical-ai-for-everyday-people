#!/usr/bin/env python3
"""Optional local arithmetic helper. No claim verification, network or writes."""
import json
import pathlib
import sys


def calculate(data):
    for key in ("attendees", "badgesPerPack", "draftPacks"):
        if key not in data or type(data[key]) is not int:
            raise ValueError(key + " must be an integer")
    attendees, size, draft = (data[k] for k in ("attendees", "badgesPerPack", "draftPacks"))
    if attendees < 0 or size <= 0 or draft < 0:
        raise ValueError("attendees/draftPacks must be nonnegative; badgesPerPack must be positive")
    packs = (attendees + size - 1) // size
    return {"attendees": attendees, "badgesPerPack": size,
            "requiredPacks": packs, "suppliedBadges": packs * size,
            "spareBadges": packs * size - attendees, "draftPacks": draft,
            "draftBadges": draft * size, "draftShortfall": max(0, attendees - draft * size)}


def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage: python3 badge_check.py badge-inputs.json")
    data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    print(json.dumps(calculate(data), sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, TypeError) as error:
        print("Input error: " + str(error), file=sys.stderr)
        sys.exit(2)
