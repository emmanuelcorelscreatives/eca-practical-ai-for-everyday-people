from pathlib import Path
import json,csv,hashlib
p=Path(__file__).parent
m=json.loads((p/'current-kit-inventory.json').read_text())
for f in m['files']:
 b=(p/f['name']).read_bytes(); assert len(b)==f['bytes'];assert hashlib.sha256(b).hexdigest()==f['sha256'],f['name']
r=list(csv.DictReader((p/'answer-key.csv').open()));assert len(r)==4
assert r[1]['Judgment']=='Unsupported as written'
assert 'scheduled volunteer hours' in (p/'source-text.txt').read_text()
assert 'volunteer ours' in (p/'ocr-draft.txt').read_text()
s=json.loads((p/'source-record.json').read_text());assert s['quotationViewerPage']==2 and s['numberingExample']=={'viewerPosition':6,'printedPage':5}
print('PASS: all inventory hashes, four expected judgments and page/OCR source facts')
