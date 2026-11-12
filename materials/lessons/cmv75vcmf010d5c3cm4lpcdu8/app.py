"""Loopback-only Academy deterministic boundary practice. No external tools or AI."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import json
import subprocess
import threading
import sys
import hashlib
import secrets

ROOT = Path(__file__).resolve().parent
LOCK = threading.Lock()
PENDING = {}
BRIEF = 'approved-event-brief.pdf'
TEMPLATE = 'checklist-template.md'
DEST = 'sandbox/event-checklist-draft.md'
SCENARIOS = {'normal', 'missing', 'conflict', 'prohibited', 'permission', 'unverified'}


def run_scenario(scenario, root=ROOT):
    if scenario not in SCENARIOS:
        raise ValueError('Unknown practice scenario')
    root = Path(root)
    # Fixed filenames, no client-selected path, shell or command.
    result = subprocess.run(['pdftotext', str(root / BRIEF), '-'],
                            capture_output=True, text=True, timeout=10, check=True)
    brief = result.stdout.strip()
    template = (root / TEMPLATE).read_text(encoding='utf-8')
    log = ['Opened approved-event-brief.pdf', 'Read checklist template']
    common = {'scenario': scenario, 'brief': brief, 'template': template,
              'activity': log, 'draft': None, 'saved': False,
              'externalActionsExecuted': [], 'practice': 'Deterministic Academy sandbox — not a language model'}
    stops = {
        'missing': ('STOPPED — REQUIRED INFORMATION MISSING', 'What is the confirmed event start time?'),
        'conflict': ('STOPPED — CONFLICTING INFORMATION', 'Training sources: approved section A capacity 80; approved section B capacity 120. Request confirmation; neither value selected.'),
        'prohibited': ('ACTION NOT PERMITTED', 'I can prepare a draft supply list and draft message for human review. No purchase or message was executed.'),
        'permission': ('STOPPED — SANDBOX PERMISSION UNAVAILABLE', 'Selected training condition: approved access unavailable. Restore approved access or use manual template. No file saved.'),
        'unverified': ('STOPPED — EVIDENCE UNVERIFIED', 'Venue provides audio equipment is unsupported by the approved brief. Remove the claim or label it unverified; ask for confirmation.'),
    }
    if scenario in stops:
        status, message = stops[scenario]
        return {**common, 'status': status, 'message': message}
    fields = dict(line.split(': ', 1) for line in brief.splitlines() if ': ' in line)
    needed = ['Event', 'Date', 'Venue', 'Activities', 'Accessibility']
    if any(not fields.get(key) for key in needed):
        return {**common, 'status': 'STOPPED — REQUIRED INFORMATION MISSING',
                'message': 'An expected supplied field could not be read. Inspect the approved PDF manually.'}
    rows = [
        ('Date and venue', f"{fields['Date']} · {fields['Venue']}", 'None'),
        ('Activities', fields['Activities'], 'None'),
        ('Accessibility', fields['Accessibility'], 'None'),
        ('Coordinator', 'Not supplied', 'Awaiting confirmation'),
        ('Final attendance estimate', 'Not supplied', 'Awaiting confirmation'),
        ('Start time if required', 'Not supplied', 'Awaiting confirmation'),
    ]
    # Populate the actual supplied template, retaining all its required sections.
    draft = template.replace('# Event preparation checklist', f"# {fields['Event']} — Event preparation checklist", 1)
    template_labels = ['Confirm date and venue', 'Confirm activities', 'Check accessibility wording',
                       'Confirm coordinator', 'Confirm final attendance estimate', 'Confirm start time if required']
    for label, row in zip(template_labels, rows):
        placeholder = f'| {label} | | | Awaiting human review |'
        if placeholder not in draft:
            raise ValueError('Approved template changed; inspect it before continuing')
        draft = draft.replace(placeholder, f'| {label} | {row[1]} | {row[2]} | Awaiting human review |', 1)
    draft = draft.replace('## Tool activity / status\nRecord actual reads and actual draft-save result. Do not claim contact, purchase, publication or other external execution.',
                          '## Tool activity / status\nOpened approved-event-brief.pdf; read checklist template. Draft prepared for review; save completion is reported separately. No external action occurred.')
    draft = draft.replace('| Task |', 'FROM APPROVED BRIEF\n\n| Task |', 1)
    return {**common, 'status': 'DRAFT READY FOR REVIEW — NOT SAVED',
            'message': 'Compare the draft with the approved brief before saving. No external action occurred.',
            'draft': draft, 'reviewToken': secrets.token_urlsafe(24),
            'inputSha256': {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in (BRIEF, TEMPLATE)}}


def save_draft(result, root=ROOT):
    if result.get('scenario') != 'normal' or not result.get('draft'):
        raise PermissionError('No approved-path draft to save')
    if any(hashlib.sha256((Path(root) / name).read_bytes()).hexdigest() != digest
           for name, digest in result.get('inputSha256', {}).items()) or not result.get('inputSha256'):
        raise PermissionError('Approved input changed after preview. Run and review a fresh draft before saving.')
    dest = Path(root) / DEST
    # This app creates a new sandbox directory only; never follow a linked destination.
    sandbox = Path(root) / 'sandbox'
    if sandbox.is_symlink() or dest.is_symlink():
        raise PermissionError('Linked destination refused')
    sandbox.mkdir(exist_ok=True)
    with dest.open('x', encoding='utf-8') as output:
        output.write(result['draft'])
    return {**result, 'saved': True, 'status': 'DRAFT CREATED — NOT SENT OR PUBLISHED',
            'destination': DEST,
            'activity': [*result['activity'], 'Saved sandbox/event-checklist-draft.md']}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        paths = {'/': ('index.html', 'text/html; charset=utf-8'),
                 '/approved-event-brief.pdf': (BRIEF, 'application/pdf'),
                 '/boundary-card.md': ('boundary-card.md', 'text/plain; charset=utf-8'),
                 '/checklist-template.md': (TEMPLATE, 'text/plain; charset=utf-8')}
        if self.path not in paths:
            self.send_error(404)
            return
        name, mime = paths[self.path]
        data = (ROOT / name).read_bytes()
        self.send_response(200)
        self.send_header('Content-Type', mime)
        self.send_header('Content-Length', str(len(data)))
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        # Loopback listening is not an origin check. Refuse browser cross-origin requests.
        if self.headers.get('Origin') not in (None, 'http://127.0.0.1:8765', 'http://localhost:8765'):
            self.send_error(403)
            return
        if self.path not in ('/run', '/save'):
            self.send_error(404)
            return
        try:
            size = int(self.headers.get('Content-Length', '0'))
            if not 0 < size <= 1024:
                raise ValueError('Request too large or empty')
            payload = json.loads(self.rfile.read(size))
            scenario = payload.get('scenario')
            with LOCK:
                if self.path == '/save':
                    token = payload.get('reviewToken')
                    pending = PENDING.get(token) if isinstance(token, str) else None
                    if not pending or scenario != 'normal':
                        raise PermissionError('No matching previously reviewed draft. Run and inspect a fresh draft first.')
                    result = save_draft(pending)
                    del PENDING[token]
                else:
                    result = run_scenario(scenario)
                    if result.get('draft'):
                        if len(PENDING) >= 32:
                            PENDING.pop(next(iter(PENDING)))
                        PENDING[result['reviewToken']] = result
            code = 200
        except (ValueError, OSError, subprocess.SubprocessError) as error:
            code = 409
            result = {'status': 'STOPPED — NO NEW SAVE CONFIRMED', 'message': str(error),
                      'externalActionsExecuted': []}
        data = json.dumps(result, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == '__main__':
    if sys.argv[1:] == ['--self-test']:
        import unittest
        import test_app
        result = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromModule(test_app))
        raise SystemExit(0 if result.wasSuccessful() else 1)
    if sys.argv[1:]:
        raise SystemExit('Usage: python3 app.py [--self-test]')
    print('Academy deterministic boundary practice: http://127.0.0.1:8765 — Ctrl+C to stop', flush=True)
    ThreadingHTTPServer(('127.0.0.1', 8765), Handler).serve_forever()
