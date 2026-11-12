import csv,pathlib
p=pathlib.Path(__file__).parent
read=lambda n:list(csv.DictReader((p/n).open(encoding='utf-8',newline='')))
s=read('source-register.csv');q=read('questions.csv');a=read('reviewed-tracker.csv')
assert len(q)==len(a)==6
assert {x['source_id'] for x in s if x['public_use']=='Yes'}=={'S1','S2'}
assert sum(x['decision']=='Approved' for x in a)==3
assert sum(x['decision']=='Returned for edit' for x in a)==1
assert sum(x['evidence_status']=='Unanswered' for x in a)==2
assert sum(x['evidence_status']=='Conflicting' for x in a)==1
assert 'subject to volunteer availability' in a[0]['draft_answer']
assert 'depends on available skills, tools, and safe working conditions' in a[2]['draft_answer']
assert a[3]['draft_answer']==a[4]['draft_answer']==''
assert a[5]['evidence_status']=='Unanswered' and a[5]['decision']=='Returned for edit'
f=(p/'reviewed-faq.md').read_text(encoding='utf-8')
assert 'Parking is available' not in f and 'Yes, we repair toasters' not in f
assert '10:00–14:00' in f and 'A team member will review your request.' in f
print('PASS: 6 questions; outcomes 3 approved / 1 returned / 1 unanswered / 1 conflict; 2 Unanswered evidence rows; source and public FAQ integrity')
