from pathlib import Path
import subprocess,json,hashlib,wave,re,shutil,os
D=Path(__file__).parent;os.chmod(D,0o700)
if (D/'practice_narration.wav').exists() or (D/'fixture-production-proof.json').exists():raise SystemExit('Existing runtime fixture preserved; use a new private copy')
text=(D/'recording-script.txt').read_text().strip();sentences=re.split(r'(?<=[.!?])\s+',text);parts=[];allframes=[];pos=0;srt=[]
def stamp(seconds):
 ms=round(seconds*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
for i,s in enumerate(sentences):
 (D/f'part-{i}.txt').write_text(s);subprocess.run(['espeak-ng','-v','en-us','-s','150','-w',str(D/f'part-{i}.wav'),'-f',str(D/f'part-{i}.txt')],check=True)
 with wave.open(str(D/f'part-{i}.wav'),'rb') as w:
  params=w.getparams();b=w.readframes(w.getnframes());frames=w.getnframes();rate=w.getframerate()
 allframes.append(b);start=pos/rate;pos+=frames;end=pos/rate;srt.append(f'{i+1}\n{stamp(start)} --> {stamp(end)}\n{s}\n');parts.append({'text':s,'startFrame':pos-frames,'endFrame':pos,'frames':frames,'sampleRate':rate,'sha256':hashlib.sha256(b).hexdigest()})
with wave.open(str(D/'practice_narration.wav'),'wb') as w:w.setparams(params);w.writeframes(b''.join(allframes))
(D/'practice_narration.srt').write_text('\n'.join(srt));orig=D/'Originals';orig.mkdir()
for n in ['self_created_banner.jpg','practice_narration.wav']:shutil.copyfile(D/n,orig/n)
proof={'state':'COMPLETE','application':'eSpeak NG','version':subprocess.check_output(['espeak-ng','--version'],text=True).strip(),'sourceText':text,'actualSyntheticVoice':'en-us default machine voice, not trained to imitate or identify a real person','rightsScope':'Self-authored Academy text/banner; installed eSpeak NG libre software execution. No original human recording, instructor identity, cleared person or external permission claimed. Supplied copyright file retained for independent review.','generatedAudio':'practice_narration.wav','actualPCMFrames':pos,'actualPCMSampleRate':rate,'actualDurationSec':pos/rate,'parts':parts,'captionMethod':'Exact self-authored text synthesized per sentence. Each SRT boundary measured from actual source PCM sentence frame lengths. No ASR or invented audio transcript. Caption comparison and playback remain actual app actions.','files':[]}
assert (D/'espeak-ng-copyright.txt').is_file()
for n in ['recording-script.txt','self_created_banner.jpg','practice_narration.wav','practice_narration.srt','index.html','fixture-server.py','espeak-ng-copyright.txt']:
 p=D/n;proof['files'].append({'path':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size})
(D/'fixture-production-proof.json').write_text(json.dumps(proof,indent=2))
