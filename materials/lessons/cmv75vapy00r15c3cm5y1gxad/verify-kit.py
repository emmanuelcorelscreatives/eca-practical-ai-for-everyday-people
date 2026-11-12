from pathlib import Path
import json,wave,hashlib
r=Path(__file__).resolve().parent;a=json.loads((r/'alignment.json').read_text());rate=a['sampleRate'];rows=a['segments']
def wav(name):
 with wave.open(str(r/'audio'/name),'rb')as w:
  assert(w.getnchannels(),w.getsampwidth(),w.getframerate())==(1,2,rate)
  return w.readframes(w.getnframes())
original=wav('community_update_practice.wav');edited=wav('community_update_edited_review.wav');cut=rows[2];start,end=cut['startFrame'],cut['endFrame'];assert edited==original[:2*start]+original[2*end:];assert rows[0]['startFrame']==0 and rows[-1]['endFrame']*2==len(original);assert all(x['endFrame']==y['startFrame']for x,y in zip(rows,rows[1:]));assert(r/'transcript-original.txt').read_text().strip()==' '.join(x['text']for x in rows);assert(r/'transcript-edited.txt').read_text().strip()==' '.join(x['text']for x in rows if not x['removable']);assert 'If the weather changes, check the posted update.'in(r/'transcript-edited.txt').read_text();print(json.dumps({'pass':True,'originalFrames':len(original)//2,'editedFrames':len(edited)//2,'removedFrames':[start,end],'exactRetainedPcm':True,'sourceSha256':hashlib.sha256((r/'audio/community_update_practice.wav').read_bytes()).hexdigest(),'scope':'Physical and exact-script exercise checks only, no ASR or listening verdict'},indent=2))
