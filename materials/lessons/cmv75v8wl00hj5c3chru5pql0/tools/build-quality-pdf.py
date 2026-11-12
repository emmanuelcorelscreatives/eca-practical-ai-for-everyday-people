"""Rebuild image-only three-page PDF from exact supplied JPEGs, stdlib only."""
from pathlib import Path
import sys,json,hashlib
p=Path(__file__).resolve().parents[1]; objects=[]
def add(b):objects.append(b);return len(objects)
add(b'<< /Type /Catalog /Pages 2 0 R >>');add(b'PLACEHOLDER')
pages=[]
for n in range(1,4):
 data=(p/('source-quality/page-2.jpg' if n==2 else f'source/page-{n}.jpg')).read_bytes();im=add(b'<< /Type /XObject /Subtype /Image /Width 1240 /Height 1754 /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length '+str(len(data)).encode()+b' >>\nstream\n'+data+b'\nendstream');cmd=b'q 595 0 0 842 0 0 cm /Im0 Do Q';content=add(b'<< /Length '+str(len(cmd)).encode()+b' >>\nstream\n'+cmd+b'\nendstream');pages.append(add(f'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /XObject << /Im0 {im} 0 R >> >> /Contents {content} 0 R >>'.encode()))
objects[1]=('<< /Type /Pages /Count 3 /Kids ['+' '.join(f'{n} 0 R' for n in pages)+'] >>').encode();out=bytearray(b'%PDF-1.4\n%\xe2\xe3\xcf\xd3\n');offsets=[0]
for i,b in enumerate(objects,1):offsets.append(len(out));out+=f'{i} 0 obj\n'.encode()+b+b'\nendobj\n'
x=len(out);out+=f'xref\n0 {len(objects)+1}\n0000000000 65535 f \n'.encode()
for off in offsets[1:]:out+=f'{off:010d} 00000 n \n'.encode()
out+=f'trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{x}\n%%EOF\n'.encode();destination=Path(sys.argv[1]) if len(sys.argv)>1 else p/'scan-quality-exercise.pdf';expected=(p/'scan-quality-exercise.pdf').read_bytes() if len(sys.argv)>1 else None;destination.write_bytes(out)
if expected is not None:assert bytes(out)==expected,'Rebuilt PDF differs from exact supplied source'
print(json.dumps({'state':'PASS','exactSourcePDFMatch':expected is not None,'outputSha256':hashlib.sha256(out).hexdigest(),'output':str(destination)}))
