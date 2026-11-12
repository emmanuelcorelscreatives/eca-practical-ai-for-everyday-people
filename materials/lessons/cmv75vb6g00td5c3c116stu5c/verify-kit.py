from pathlib import Path
import csv,zipfile,xml.etree.ElementTree as E,json
p=Path(__file__).parent
rows=list(csv.DictReader((p/'reviewed-queue.csv').open()))
assert [r['Request number'] for r in rows]==['R-002','R-003','R-001','R-004']
expected={'R-001':('Booking or administration','Human review'),'R-002':('Safety or service issue','Urgent human review'),'R-003':('Unclear','Suspicious human review'),'R-004':('Unclear','Human clarification')}
for r in rows:
 assert (r['Category'],r['Attention flag'])==expected[r['Request number']]
 assert r['Evidence phrase'] in (p/r['Original message path']).read_text()
 assert not r['Reviewer decision'] and not r['Correction']
 assert r['Status'] in ['Unresolved','Needs immediate review','Quarantined for review','Awaiting clarification']
blank=list(csv.DictReader((p/'practice-queue.csv').open()));assert len(blank)==4
assert all(not any(r[k] for k in r if k not in ['Request number','Original message path']) for r in blank)
with zipfile.ZipFile(p/'request-triage.ods') as z:
 assert z.testzip() is None
 E.fromstring(z.read('content.xml')); E.fromstring(z.read('META-INF/manifest.xml'))
print(json.dumps({'status':'PASS','four_source_ids':True,'evidence_phrases_exact':True,'reviewer_decisions_blank':True,'ods_xml_crc':'PASS'}))
