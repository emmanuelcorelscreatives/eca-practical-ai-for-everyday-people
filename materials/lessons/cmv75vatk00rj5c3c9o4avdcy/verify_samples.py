"""Read actual bytes, probe, full-decode all five media and bind results to exact file SHA."""
from pathlib import Path
import subprocess,json,hashlib,argparse
p=Path(__file__).resolve().parent;ap=argparse.ArgumentParser();ap.add_argument('--report',default=str(p/'sample-verification.json'));a=ap.parse_args();proof={}
for name in ['practice-faulty.mp4','practice-correct.mp4','practice-faulty.webm','practice-correct.webm','practice-voice.wav']:
 f=p/name;d=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)]));types=[s['codec_type'] for s in d['streams']]
 assert types==(['audio'] if f.suffix=='.wav' else ['video','audio']);duration=float(d['format']['duration']);assert (0<duration<=20) if f.suffix=='.wav' else (19.9<duration<20.2)
 pcm=subprocess.check_output(['ffmpeg','-v','error','-threads','1','-filter_threads','1','-i',str(f),'-map','0:a:0','-f','s16le','-'])
 subprocess.run(['ffmpeg','-v','error','-threads','1','-filter_threads','1','-i',str(f),'-f','null','-'],check=True)
 proof[name]={'fileSha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size,'duration':duration,'streams':[(s['codec_type'],s['codec_name']) for s in d['streams']],'audioDecodedSha256':hashlib.sha256(pcm).hexdigest(),'fullDecode':'PASS'}
assert proof['practice-faulty.mp4']['audioDecodedSha256']==proof['practice-correct.mp4']['audioDecodedSha256'];assert proof['practice-faulty.webm']['audioDecodedSha256']==proof['practice-correct.webm']['audioDecodedSha256']
manifest=json.loads((p/'sample-hashes.json').read_text());assert all(hashlib.sha256((p/n).read_bytes()).hexdigest()==m['sha256'] for n,m in manifest.items())
proof['manifest']='All listed exact hashes checked';proof['limits']='No human listening, ASR or actual phone testing claimed. Source/caption words and rendered frames need independent review.';Path(a.report).write_text(json.dumps(proof,indent=2));print(json.dumps(proof))
