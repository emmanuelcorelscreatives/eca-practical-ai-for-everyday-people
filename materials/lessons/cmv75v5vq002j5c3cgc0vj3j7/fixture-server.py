from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import json, subprocess, os, hashlib, threading
D=Path(__file__).parent
EXPORT_LOCK=threading.Lock()
def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def fixture_manifest():
 proof=json.loads((D/'fixture-production-proof.json').read_text());approved={Path(x['path']).name:x['sha256'] for x in proof['files']}
 files={name:digest(D/name) for name in ['self_created_banner.jpg','practice_narration.wav','recording-script.txt','practice_narration.srt']}
 if any(files[n]!=approved[n] for n in files):raise ValueError('On-disk fixture changed after synthesis; export refused')
 return {'imageSHA256':files['self_created_banner.jpg'],'audioSHA256':files['practice_narration.wav'],'sourceTextSHA256':files['recording-script.txt'],'captionSRTSHA256':files['practice_narration.srt'],'source':'Actual eSpeak NG neutral synthetic fixture; no real person imitated'}
class H(SimpleHTTPRequestHandler):
 def __init__(self,*args,**kwargs):super().__init__(*args,directory=str(D),**kwargs)
 def send_json(self,value):
  body=json.dumps(value).encode();self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
 def do_GET(self):
  if self.path=='/fixture-manifest':
   try:self.send_json(fixture_manifest())
   except Exception as error:self.send_error(409,str(error))
   return
  super().do_GET()
 def do_POST(self):
  if self.path!='/export':self.send_error(404);return
  try:
   data=json.loads(self.rfile.read(int(self.headers['Content-Length'])));expected=(D/'recording-script.txt').read_text().strip();manifest=fixture_manifest()
   if data.get('captionText','').strip()!=expected:self.send_error(400,'Restore exact verified narration text before exporting');return
   if data.get('imageSHA256')!=manifest['imageSHA256'] or data.get('audioSHA256')!=manifest['audioSHA256']:self.send_error(400,'Selected image/audio hashes do not match the cleared on-disk fixture; export refused');return
   with EXPORT_LOCK:
    # Recheck the exact fixture after entering the serialized export section.
    if fixture_manifest()!=manifest:raise ValueError('Fixture changed before export')
    out=D/'Edited Output';out.mkdir(exist_ok=True);os.chmod(out,0o700);commands=[]
    def run_checked(cmd):
     completed=subprocess.run(cmd,check=True,capture_output=True,text=True,timeout=120);commands.append({'argv':cmd,'returncode':completed.returncode,'stdout':completed.stdout,'stderr':completed.stderr})
    run_checked(['ffmpeg','-nostdin','-hide_banner','-loglevel','error','-y','-loop','1','-i',str(D/'self_created_banner.jpg'),'-i',str(D/'practice_narration.wav'),'-vf',"scale=1280:720,subtitles='"+str(D/'practice_narration.srt')+"':force_style='FontName=DejaVu Sans,FontSize=22,Outline=1'",'-c:v','libx264','-preset','fast','-threads','2','-pix_fmt','yuv420p','-c:a','aac','-shortest','-movflags','+faststart',str(out/'practice_event_clip.mp4')])
    run_checked(['ffmpeg','-nostdin','-v','error','-xerror','-threads','2','-i',str(out/'practice_event_clip.mp4'),'-f','null','-'])
    run_checked(['ffmpeg','-nostdin','-v','error','-y','-i',str(out/'practice_event_clip.mp4'),'-c:v','libvpx','-deadline','realtime','-cpu-used','8','-threads','2','-c:a','libopus',str(out/'practice_event_clip-preview.webm')])
    for filename in ['practice_event_clip.mp4','practice_event_clip-preview.webm']:os.chmod(out/filename,0o600)
    if fixture_manifest()!=manifest:raise ValueError('Source fixture changed during export; result held')
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(out/'practice_event_clip.mp4')]));b=(out/'practice_event_clip.mp4').read_bytes();r={'path':'Edited Output/practice_event_clip.mp4','sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b),'duration':probe['format']['duration'],'previewPath':'Edited Output/practice_event_clip-preview.webm','previewCaveat':'Actual WebM preview transcoded from saved MP4; this exact MP4 was separately fully decoded with a checked command.','actualOutputMode':oct((out/'practice_event_clip.mp4').stat().st_mode & 0o777),'actualDirectoryMode':oct(out.stat().st_mode & 0o777),'actualOwnerUID':out.stat().st_uid,'sharing':'No network publication operation exists','probe':probe,'selectedInputSHA256':{'image':data['imageSHA256'],'audio':data['audioSHA256']},'verifiedSourceManifest':manifest,'actualCheckedCommands':commands,'fullMP4DecodeChecked':True};(D/'actual-export-proof.json').write_text(json.dumps(r,indent=2));self.send_json(r)
  except Exception as error:self.send_error(500,str(error))
server=ThreadingHTTPServer(('127.0.0.1',0),H);(D/'server-port.txt').write_text(str(server.server_address[1]));server.serve_forever()
