from pathlib import Path
import subprocess,sys,time,webbrowser
D=Path(__file__).parent
if not (D/'practice_narration.wav').is_file():raise SystemExit('Generate the cleared synthetic fixture first, or use the manual fallback.')
portfile=D/'server-port.txt'
if portfile.exists():raise SystemExit('Existing server receipt preserved; use a new private copy or inspect its owner before restarting.')
child=subprocess.Popen([sys.executable,str(D/'fixture-server.py')])
try:
 for _ in range(100):
  if child.poll() is not None:raise RuntimeError('Owned local server exited')
  if portfile.exists():break
  time.sleep(.1)
 else:raise RuntimeError('Local server address unavailable')
 url='http://127.0.0.1:'+portfile.read_text().strip()+'/index.html';print('Actual local URL:',url,flush=True);webbrowser.open(url);input('Press Enter to stop this exact local server. ')
finally:
 if child.poll() is None:child.terminate();child.wait(timeout=10)
