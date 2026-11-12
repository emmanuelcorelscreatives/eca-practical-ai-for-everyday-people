from pathlib import Path
from datetime import date
import json
r=Path(__file__).resolve().parent
source=(r/'source.txt').read_text()
adult=(r/'adult-email-draft.txt').read_text()
phone=(r/'phone-message-draft.txt').read_text()
assert date(2026,10,17).strftime('%A')=='Saturday'
assert date(2026,10,15).strftime('%A')=='Thursday'
for s in (source,adult,phone):
    for fact in ('River Room','arts@example.org','2026','14:00','16:00','17','15'):
        assert fact in s, fact
for s in (adult,phone):
    assert 'BORRADOR GENERADO' in s
    assert 'Biblioteca Central' in s and 'octubre' in s and 'lápiz' in s
assert all(x in adult for x in ('Le invitamos','Traiga','Inscríbase'))
assert all(x in phone for x in ('Trae','Regístrate'))
print(json.dumps({'status':'PASS','scope':'fixture integrity and calendar only; not semantic or human-review certification','source':'fictional course example','date':'2026-10-17 Saturday','deadline':'2026-10-15 Thursday'},ensure_ascii=False))
