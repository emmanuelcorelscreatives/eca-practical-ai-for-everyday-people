from pathlib import Path
import csv,json,sys
root=Path(__file__).parent
target=Path(sys.argv[1]) if len(sys.argv)>1 else root/'translation-es-example.txt'
text=target.read_text(encoding='utf-8')
with (root/'glossary-en-es.csv').open(encoding='utf-8',newline='') as f: rows=list(csv.DictReader(f))
print(json.dumps({'file':target.name,'literal_counts':{r['Approved Spanish']:text.count(r['Approved Spanish']) for r in rows},'limitation':'Literal presence only; no semantic, grammar, approval or pronunciation verdict.'},ensure_ascii=False,indent=2))
