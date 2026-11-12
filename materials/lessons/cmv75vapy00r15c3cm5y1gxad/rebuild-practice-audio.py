import pathlib,json,subprocess,wave,hashlib,base64,struct
R=pathlib.Path(__file__).parent;K=R;K.mkdir(exist_ok=True); A=K/'audio';A.mkdir(exist_ok=True)
phrases=['The workshop begins at ten.','Bring a reusable container.','Um, I was just thinking aloud.','The entrance is beside the library.','If the weather changes, check the posted update.']
parts=[];rows=[];at=0
for i,text in enumerate(phrases):
 f=A/f'segment-{i+1}.wav';tf=A/f'segment-{i+1}.txt';tf.write_text(text)
 if not f.exists():subprocess.run(['ffmpeg','-v','error','-f','lavfi','-i',f'flite=textfile={tf}:voice=slt','-ar','24000','-ac','1','-c:a','pcm_s16le',str(f)],check=True)
 with wave.open(str(f))as w:b=w.readframes(w.getnframes())
 b+=b'\0\0'*6000;parts.append(b);rows.append(dict(id=i+1,text=text,startFrame=at,endFrame=at+len(b)//2,removable=i==2));at+=len(b)//2
for name,b in [('community_update_practice.wav',b''.join(parts)),('community_update_edited_review.wav',b''.join(parts[:2]+parts[3:]))]:
 with wave.open(str(A/name),'wb')as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(24000);w.writeframes(b)
data={'sampleRate':24000,'segments':rows,'audioBase64':base64.b64encode((A/'community_update_practice.wav').read_bytes()).decode(),'provenance':'Academy-authored fictional workshop message. Synthetic demonstration voice generated locally by FFmpeg/libflite slt. Not an instructor recording, ASR result, or real community announcement.'}
(K/'demo-data.js').write_text('window.DEMO='+json.dumps(data)+';')
(K/'transcript-original.txt').write_text(' '.join(phrases)+'\n');(K/'transcript-edited.txt').write_text(' '.join(phrases[:2]+phrases[3:])+'\n');(K/'alignment.json').write_text(json.dumps({'sampleRate':24000,'segments':rows,'provenance':data['provenance']},indent=2))
report={'sourceSha256':hashlib.sha256((A/'community_update_practice.wav').read_bytes()).hexdigest(),'removedOnlyFrames':[rows[2]['startFrame'],rows[2]['endFrame']],'originalFrames':at,'editedFrames':sum(len(b)//2 for i,b in enumerate(parts)if i!=2),'retainedPcmExact':True,'originalUntouched':True,'generation':'FFmpeg/libflite synthetic course practice, not EC cloned voice','commands':'ffmpeg -f lavfi -i flite=text=<exact phrase>:voice=slt -ar 24000 -ac 1 -c:a pcm_s16le segment-N.wav'}
with wave.open(str(A/'community_update_edited_review.wav'))as w:assert w.readframes(w.getnframes())==b''.join(parts[:2]+parts[3:])
(K/'execution-proof.json').write_text(json.dumps(report,indent=2));print(json.dumps(report))
