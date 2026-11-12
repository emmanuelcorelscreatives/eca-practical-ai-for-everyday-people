"""Build actual self-authored training PDF/DOCX plus scan SVG.
Rasterize scan-source.svg to Record scan.jpg under the guarded capture/build helper.
No scanner/OCR/AI execution is implied by creating these supplied exercise sources.
"""
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib,json,textwrap
p=Path(__file__).parent; out=p/'Appointment Prep'/'01 Originals';out.mkdir(parents=True,exist_ok=True)
lines=[part for line in (p/'originals/Appointment notice.txt').read_text().splitlines() for part in (textwrap.wrap(line,68) or [''])]
def pdf_escape(x):return x.replace('\\','\\\\').replace('(','\\(').replace(')','\\)')
stream='BT /F1 13 Tf 48 790 Td 21 TL\n'+'\n'.join(('' if i==0 else 'T*\n')+'('+pdf_escape(line)+') Tj' for i,line in enumerate(lines))+'\nET'
objects=['<< /Type /Catalog /Pages 2 0 R >>','<< /Type /Pages /Kids [3 0 R] /Count 1 >>','<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 842] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>','<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',f'<< /Length {len(stream.encode())} >>\nstream\n{stream}\nendstream']
b=bytearray(b'%PDF-1.4\n');offsets=[0]
for i,obj in enumerate(objects,1):offsets.append(len(b));b.extend(f'{i} 0 obj\n{obj}\nendobj\n'.encode())
xref=len(b);b.extend(f'xref\n0 {len(objects)+1}\n0000000000 65535 f \n'.encode());b.extend(''.join(f'{n:010} 00000 n \n' for n in offsets[1:]).encode());b.extend(f'trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode());(out/'Appointment notice.pdf').write_bytes(b)
paras=''.join('<w:p><w:r><w:t xml:space="preserve">'+escape(line)+'</w:t></w:r></w:p>' for line in (p/'originals/Personal notes.txt').read_text().splitlines())
with ZipFile(out/'Personal notes.docx','w',ZIP_DEFLATED) as z:
 z.writestr('[Content_Types].xml','<?xml version="1.0"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/></Types>')
 z.writestr('_rels/.rels','<?xml version="1.0"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>')
 z.writestr('word/document.xml','<?xml version="1.0"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>'+paras+'<w:sectPr/></w:body></w:document>')
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="900" viewBox="0 0 1400 900"><rect width="1400" height="900" fill="white"/>']
for i,line in enumerate((p/'originals/Record scan-source.txt').read_text().splitlines()):
 if '[unreadable]' in line:line='Reference word:'
 svg.append(f'<text x="70" y="{100+90*i}" font-family="DejaVu Sans" font-size="31" fill="#152335">{escape(line)}</text>')
 if line=='Reference word:':svg.append(f'<rect x="330" y="{72+90*i}" width="160" height="35" fill="#777"/><text x="520" y="{100+90*i}" font-size="24" font-family="DejaVu Sans">unclear—confirm</text>')
svg.append('</svg>');(p/'originals/Record scan-source.svg').write_text(''.join(svg))
print('Built real PDF and DOCX and source SVG. JPEG rasterization/native opening proof still required.')

# Finished one-page human-reviewed worked artifact; no model response claimed.
text=(p/'expected/final-reviewed-sheet.md').read_text().replace('—','-').replace('–','-').replace('’',"'")
lines=[part for line in text.splitlines() for part in (textwrap.wrap(line.replace('`','').replace('#',''),95) or [''])]
assert len(lines)<=55, 'Final sheet exceeds single-page line budget'
stream='BT /F1 10 Tf 36 800 Td 13 TL\n'+'\n'.join(('' if i==0 else 'T*\n')+'('+pdf_escape(line)+') Tj' for i,line in enumerate(lines))+'\nET'
objects=['<< /Type /Catalog /Pages 2 0 R >>','<< /Type /Pages /Kids [3 0 R] /Count 1 >>','<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 842] /Resources << /Font << /F1 4 0 R >> >> /Contents 5 0 R >>','<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',f'<< /Length {len(stream.encode())} >>\nstream\n{stream}\nendstream']
b=bytearray(b'%PDF-1.4\n');offsets=[0]
for i,obj in enumerate(objects,1):offsets.append(len(b));b.extend(f'{i} 0 obj\n{obj}\nendobj\n'.encode())
xref=len(b);b.extend(f'xref\n0 {len(objects)+1}\n0000000000 65535 f \n'.encode());b.extend(''.join(f'{n:010} 00000 n \n' for n in offsets[1:]).encode());b.extend(f'trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode());(p/'expected/final-reviewed-sheet.pdf').write_bytes(b)
