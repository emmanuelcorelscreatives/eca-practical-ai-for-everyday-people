#!/usr/bin/env python3
"""Optional local literal check; does not approve meaning, additions or truth."""
import json, pathlib, sys
root=pathlib.Path(__file__).resolve().parent
protected=json.loads((root/'protected-details.json').read_text())['exactStrings']
path=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else root/'faithful-draft.txt'
text=path.read_text(encoding='utf-8')
body=text.split('\n',1)[1] if text.startswith('AI DRAFT —') else text
missing=[value for value in protected if value not in body]
print(json.dumps({'missing_exact_strings':missing,'whitespace_word_count':len(body.split()),'human_review_required':['meaning','unsupported additions','quotation context','source facts']},indent=2))
sys.exit(1 if missing else 0)
