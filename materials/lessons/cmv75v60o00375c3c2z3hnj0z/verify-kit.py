from pathlib import Path
import json
p=Path(__file__).resolve().parent
required={'README.md','answer-key.md','brief-template.md','corrected-notice.md','fictional-source-notes.txt','original-draft.md','prompt.txt','verify-kit.py'}
assert all((p/name).is_file() for name in required), 'Missing required lesson file'
original=(p/'original-draft.md').read_text().split('# Community Garden Open Morning\n\n',1)[1]
corrected=(p/'corrected-notice.md').read_text().split('# Community Garden Open Morning\n\n',1)[1]
assert original.count('enjoy the amazing garden!')==1
assert corrected.count('spend time in the garden.')==1
assert corrected==original.replace('enjoy the amazing garden!','spend time in the garden.')
assert original.count('!')==1 and corrected.count('!')==0
for body in (original,corrected):
    assert sum(line.startswith('- ') for line in body.splitlines())==3
    assert len([block for block in body.strip().split('\n\n') if not block.startswith('- ')])==2
    assert 90<=len(body.replace('- ','').split())<=110
assert 'Self-created fictional example' in (p/'fictional-source-notes.txt').read_text()
print(json.dumps({'status':'PASS','exact_single_edit':True,'paragraphs':2,'bullets':3,'whitespace_body_counts':[len(x.replace('- ','').split()) for x in (original,corrected)],'google_docs_observation':'not performed by this script','writer_ui_observation':'separate genuine capture proof; not executed by this verifier'}))
