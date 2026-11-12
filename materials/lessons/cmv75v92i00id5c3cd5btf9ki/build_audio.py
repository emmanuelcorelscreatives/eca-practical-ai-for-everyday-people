from pathlib import Path
import json,subprocess,wave,tempfile,argparse,hashlib
K=Path(__file__).parent
segments=json.loads((K/'corrected-transcript.json').read_text())['segments']
parser=argparse.ArgumentParser(description='Reproduce only the supplied synthetic fictional practice recording.');parser.add_argument('--output',type=Path,default=K/'Community_Event_Planning.regenerated.wav');args=parser.parse_args();rate=22050; audio=bytearray(rate*246*2)
with tempfile.TemporaryDirectory() as tmp:
 for x in segments:
  out=Path(tmp)/'sentence.wav'
  subprocess.run(['espeak-ng','-v','en-us','-s','155','-w',str(out),x['speaker']+': '+x['text']],check=True)
  with wave.open(str(out)) as w:
   assert w.getframerate()==rate and w.getnchannels()==1 and w.getsampwidth()==2
   data=w.readframes(w.getnframes())
  begin=x['seconds']*rate*2
  assert begin+len(data)<=len(audio)
  audio[begin:begin+len(data)]=data
with wave.open(str(args.output),'wb') as w:
 w.setparams((1,2,rate,0,'NONE','not compressed'));w.writeframes(audio)
reference=K/'Community_Event_Planning.wav'
assert hashlib.sha256(args.output.read_bytes()).digest()==hashlib.sha256(reference.read_bytes()).digest(), 'Regenerated audio differs from supplied fixture; inspect eSpeak version rather than treating it as an exact reproduction.'
print('Synthetic lesson fixture reproduced exactly; 246 seconds, mono 22050 Hz PCM16; original unchanged.')
