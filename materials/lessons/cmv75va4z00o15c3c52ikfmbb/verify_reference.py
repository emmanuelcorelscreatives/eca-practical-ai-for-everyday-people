#!/usr/bin/env python3
"""Check the fictional course reference, or a learner CSV supplied as argv[1].
This structural checker does not replace contextual human review or claim app import.
"""
from pathlib import Path
import csv,json,sys,zipfile,xml.etree.ElementTree as ET
P=Path(__file__).parent
original=[['EV-101','12 vegetarian lunch boxes','FOOD'],['EV-102','Need a van for folding tables','Transprt'],['EV-103','Ramp access near side entrance','Access'],['EV-104','Markers and tape','Equipment'],['EV-105','Two people for check-in desk','volunteers'],['EV-106','Pickup','Pickup']]
allowed=['Food','Transport','Accessibility','Supplies','Volunteer','Other'];headers=['Request ID','Request text','Category original','Suggested category','Review status','Confirmed category','Review note']
def read(n):
 with (P/n).open(newline='',encoding='utf-8-sig') as f:return list(csv.DictReader(f))
def require(ok,message):
 if not ok:raise SystemExit('FAIL: '+message)
raw=read('original.csv');require([[r[k] for k in headers[:3]] for r in raw]==original,'Original exact ID/text/category values must be preserved')
require([r['Allowed category'] for r in read('allowed-categories.csv')]==allowed,'Approved list must have exactly six labels in order')
rows=read(sys.argv[1] if len(sys.argv)>1 else 'review-expected.csv');require(len(rows)==6,'Expected exactly six data rows');require(len({r['Request ID'] for r in rows})==6 and {r['Request ID'] for r in rows}=={r[0] for r in original},'Exactly six unique original request identifiers required')
byid={r[0]:r for r in original}
require(all([r[k] for k in headers[:3]]==byid[r['Request ID']] for r in rows),'Do not rewrite request IDs, texts, counts or original categories')
for r in rows:
 i=[r[0] for r in original].index(r['Request ID'])
 if i<5:require(r['Suggested category']==allowed[i] and r['Confirmed category']==allowed[i] and r['Review status']=='Clear' and bool(r['Review note'].strip()),'Supported row '+r['Request ID']+' must have the expected category/status plus an evidence note')
 else:require(r['Suggested category']=='' and r['Confirmed category']=='' and r['Review status']=='Needs review' and r['Review note']=='What is being picked up, and is transport required?','EV-106 must remain unresolved with its exact clarification question')
ns={'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
with zipfile.ZipFile(P/'Community_Event_Requests.xlsx') as z:
 require(z.testzip() is None,'Workbook CRC integrity');allxml={n:ET.fromstring(z.read(n)) for n in z.namelist() if n.endswith('.xml') or n.endswith('.rels')};wb=allxml['xl/workbook.xml'];require([e.attrib['name'] for e in wb.findall('s:sheets/s:sheet',ns)]==['Original','Review Copy','Category List'],'Workbook tab names/order');require(wb.find('s:definedNames/s:definedName',ns).text=="'Category List'!$A$2:$A$7",'Approved-category named range');sheet=allxml['xl/worksheets/sheet2.xml'];dv=sheet.find('s:dataValidations/s:dataValidation',ns);require(dv is not None and dv.attrib['sqref']=='F2:F7' and dv.attrib['allowBlank']=='1' and dv.find('s:formula1',ns).text=='ApprovedCategories','Dropdown scope/source/blank policy');orig=allxml['xl/worksheets/sheet1.xml'];values=[[c.find('s:is/s:t',ns).text or '' for c in row.findall('s:c',ns)] for row in orig.findall('s:sheetData/s:row',ns)];require(values[1:]==original,'Workbook Original cells must match CSV exactly');require(not any('vba' in n.lower() or 'externalLinks' in n for n in z.namelist()),'No macro/external-link payloads')
print(json.dumps({'state':'PASS','rows':6,'clear':5,'needsReview':1,'confirmed':5,'unresolved':'EV-106','sourcePreserved':True,'xlsxCRCAndXMLVerified':True,'applicationImportOrUI':'NOT TESTED; structural checks only','meaningApproval':'Reference exercise only; learner context review still required'},indent=2))
