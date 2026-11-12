"""Reproducible fictional sentence recordings and frame-bound captions, without ASR.
Explicit fixture creation replaces practice-voice.wav and fixture caption sources; use only to rebuild the supplied exercise, not for learner caption edits.
"""
from pathlib import Path
import tempfile,subprocess,wave,re,json,hashlib,argparse
p=Path(__file__).resolve().parent;ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(p));a=ap.parse_args();out=Path(a.output_dir).resolve();out.mkdir(parents=True,exist_ok=True);script=p/'approved-script.txt';sentences=re.split(r'(?<=[.!?])\s+',script.read_text().strip());rate=24000;cursor=0;rows=[];pcm=[]
with tempfile.TemporaryDirectory(prefix='academy167-fixture-') as tmp:
 for i,s in enumerate(sentences):
  text=Path(tmp)/f'{i}.txt';wav=Path(tmp)/f'{i}.wav';text.write_text(s)
  subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-threads','1','-filter_threads','1','-f','lavfi','-i',f"flite=textfile='{text}':voice=slt",'-ar',str(rate),str(wav)],check=True)
  with wave.open(str(wav),'rb') as w: assert w.getnchannels()==1 and w.getsampwidth()==2;frames=w.readframes(w.getnframes());n=len(frames)//2
  rows.append({'index':i,'text':s,'startFrame':cursor,'speechEndFrame':cursor+n,'endFrame':cursor+n+int(.4*rate),'pcmSha256':hashlib.sha256(frames).hexdigest()});pcm.extend([frames,bytes(int(.4*rate)*2)]);cursor+=n+int(.4*rate)
with wave.open(str(out/'practice-voice.wav'),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(rate);w.writeframes(b''.join(pcm))
def tm(sec):
 ms=round(sec*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
cues=[(rows[0]['startFrame']/rate,rows[0]['endFrame']/rate,rows[0]['text']),(rows[1]['startFrame']/rate,rows[1]['endFrame']/rate,rows[1]['text']),(rows[2]['startFrame']/rate,rows[3]['endFrame']/rate,rows[2]['text']+' '+rows[3]['text']),(rows[4]['startFrame']/rate,rows[4]['endFrame']/rate,rows[4]['text']),(rows[5]['startFrame']/rate,20,rows[5]['text'])]
def srt(cues):return '\n\n'.join(f'{i+1}\n{tm(a)} --> {tm(b)}\n{text}' for i,(a,b,text) in enumerate(cues))+'\n'
(out/'caption-correct.srt').write_text(srt(cues));bad=list(cues);a,b,text=bad[0];bad[0]=(.6,b,text.replace('fifteen','fifty'));(out/'caption-faulty.srt').write_text(srt(bad))
proof={'sampleRate':rate,'approvedScriptSha256':hashlib.sha256(script.read_bytes()).hexdigest(),'voiceSha256':hashlib.sha256((out/'practice-voice.wav').read_bytes()).hexdigest(),'sentenceNativeFrames':rows,'captionCues':cues,'middleCaptureTime':cues[2][0]+.3,'limits':'Synthetic training speech assembled by exact known sentence source/frame bounds. No recognition/forced speech verification. Final caption intentionally remains visible after speech for reading.'};(out/'fixture-source-timing.json').write_text(json.dumps(proof,indent=2));print(json.dumps(proof))
