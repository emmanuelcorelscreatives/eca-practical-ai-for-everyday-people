from decimal import Decimal
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--reveal-fresh", action="store_true", help="Use only after your fresh attempt; reveals its result")
args = parser.parse_args()
root = Path(__file__).parent
data = json.loads((root / "practice-data.json").read_text())
for item in [data["worked"], *data["boundaryExamples"]]:
    actual = Decimal(str(item["percent"])) / 100 * Decimal(str(item["whole"]))
    assert actual == Decimal(str(item["expected"])), (item, actual)
assert Decimal(80) / 4 == 20
print("PASS: worked example and boundary checks passed.")
if args.reveal_fresh:
    item = json.loads((root / "answer-key-data.json").read_text())["fresh"]
    actual = Decimal(str(item["percent"])) / 100 * Decimal(str(item["whole"]))
    assert actual == Decimal(str(item["expected"]))
    assert (Decimal(50) / 10) * 3 == actual
    print(f"POST-ATTEMPT CHECK: {item['percent']}% of {item['whole']} = {actual}.")
