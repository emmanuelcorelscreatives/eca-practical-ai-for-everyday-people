"""Export caption edits without overwriting source or previous exports.
Requires ffmpeg with libflite/libx264/libvpx/libopus. All media are fictional Academy samples.
"""
from pathlib import Path
import argparse,subprocess,json,hashlib,re
p=Path(__file__).resolve().parent
ap=argparse.ArgumentParser();ap.add_argument('--output-dir',default=str(p));ap.add_argument('--caption',default='caption-correct.srt');ap.add_argument('--output',default='learner-corrected.mp4');ap.add_argument('--fixture-build',action='store_true');ap.add_argument('--replace-fixtures',action='store_true');args=ap.parse_args();outdir=Path(args.output_dir).resolve();outdir.mkdir(parents=True,exist_ok=True)
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def run(a):subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-threads','1','-filter_threads','1',*a],check=True)
def safefile(n,base):
 f=(base/n).resolve()
 if f.parent!=base or "'" in str(f):raise ValueError('Use a simple filename in the kit directory')
 return f
script=p/'approved-script.txt'
if not script.exists():raise FileNotFoundError('Retain approved-script.txt; the builder never invents or overwrites your source.')
# Build actual audio from the provided editable script. Textfile avoids filter string injection.
def voice(out):run(['-f','lavfi','-i',f"flite=textfile='{script}':voice=slt",'-ar','24000',str(out)])
def make_ass(srt,out):
 blocks=re.split(r'\n\s*\n',srt.read_text().strip());events=[]
 def tm(t):
  h,m,s=map(int,t[:8].split(':'));cs=int(t[9:12])//10
  return f'{h}:{m:02}:{s:02}.{cs:02}'
 for block in blocks:
  lines=block.splitlines()
  if len(lines)<3 or not re.fullmatch(r'\d\d:\d\d:\d\d,\d{3} --> \d\d:\d\d:\d\d,\d{3}',lines[1]):raise ValueError('Expected numbered plain SRT cues')
  start,end=lines[1].split(' --> ');text='\\N'.join(lines[2:])
  if any(ch in ''.join(lines[2:]) for ch in ['{','}','\\']):raise ValueError('Use plain caption text; ASS override syntax is unsupported')
  events.append(f'Dialogue: 0,{tm(start)},{tm(end)},Default,,0,0,0,,{text}')
 out.write_text('[Script Info]\nScriptType: v4.00+\nPlayResX: 1280\nPlayResY: 720\n[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding\nStyle: Default,DejaVu Sans,34,&H00000000,&H00000000,&H00FFFFFF,&H00FFFFFF,0,0,0,0,100,100,0,0,3,1,0,2,40,40,80,1\n[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n'+'\n'.join(events)+'\n')
def export(caption,out,audio):
 ass=out.with_suffix('.captions.ass');make_ass(caption,ass)
 vf=f"drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='FICTIONAL PRACTICE CLIP':fontsize=34:fontcolor=black:x=(w-tw)/2:y=70,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='SOURCE AND EXPORT':fontsize=55:fontcolor=black:x=(w-tw)/2:y=280,drawtext=fontfile=/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf:text='Keep both versions':fontsize=40:fontcolor=black:x=(w-tw)/2:y=360,ass='{ass}'"
 run(['-f','lavfi','-i','color=c=0xf0f7fa:s=1280x720:r=24:d=20','-i',str(audio),'-vf',vf,'-af','apad','-t','20','-c:v','libx264','-preset','ultrafast','-crf','22','-threads','2','-c:a','aac','-movflags','+faststart',str(out)])
 webm=out.with_suffix('.webm');run(['-i',str(out),'-c:v','libvpx-vp9','-b:v','450k','-threads','2','-deadline','realtime','-cpu-used','6','-c:a','libopus',str(webm)])
 proof={'approvedScriptSha256':sha(script),'captionFile':caption.name,'captionSha256':sha(caption),'audioFile':audio.name,'audioSha256':sha(audio),'mp4Sha256':sha(out),'webmSha256':sha(webm),'scope':'Actual local fictional export; no human listening or destination-device approval claimed'};out.with_suffix('.build.json').write_text(json.dumps(proof,indent=2))
if args.fixture_build:
 targets=[outdir/f'practice-{m}.mp4' for m in ['faulty','correct']]
 if any(f.exists() for f in targets) and not args.replace_fixtures:raise FileExistsError('Existing fixture exports retained; use a new --output for learner changes. Reproducibility only: --replace-fixtures.')
 audio=p/'practice-voice.wav'
 timing=json.loads((p/'fixture-source-timing.json').read_text())
 if timing['approvedScriptSha256']!=sha(script) or timing['voiceSha256']!=sha(audio):raise ValueError('Supplied script/audio changed; retain approved sources or explicitly prepare a new aligned fixture.')
 for mode in ['faulty','correct']:export(p/f'caption-{mode}.srt',outdir/f'practice-{mode}.mp4',audio)
else:
 out=safefile(args.output,outdir);caption=safefile(args.caption,p)
 if out.exists() or out.with_suffix('.webm').exists():raise FileExistsError('Choose a new output name to retain previous exports')
 audio=p/'practice-voice.wav'
 timing=json.loads((p/'fixture-source-timing.json').read_text())
 if timing['approvedScriptSha256']!=sha(script) or timing['voiceSha256']!=sha(audio):raise ValueError('Recording and approved source no longer match supplied fixture construction; restore source or explicitly prepare new source audio.')
 export(caption,out,audio)
meta={f.name:{'sha256':sha(f),'bytes':f.stat().st_size} for f in outdir.glob('*') if f.is_file() and f.suffix in ['.mp4','.webm','.srt','.wav','.txt','.ass','.json'] and f.name not in ['sample-hashes.json','current-kit-inventory.json','sample-verification.json']};(outdir/'sample-hashes.json').write_text(json.dumps(meta,indent=2))
