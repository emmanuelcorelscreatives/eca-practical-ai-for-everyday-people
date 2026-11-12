from pathlib import Path
p=Path(__file__).parent
s=(p/'02-sanitised-input.txt').read_text();d=(p/'04-example-draft.txt').read_text()
required=('[CUSTOMER_NAME]','replacement desk lamp','18 October 2026','21 October 2026')
forbidden=('Amina Solano','DEMO-4827','amina.solano@example.invalid','14 Sample Street','North Gate concierge')
def valid(text, sender=False):
 return all(token in text for token in required) and not any(token in text for token in forbidden) and (not sender or ('[SENDER_NAME]' in text and 'NOT SENT' in text))
assert valid(s) and valid(d,True)
prompt=(p/'03-structured-prompt.txt').read_text()
assert valid(prompt)
for token in required:
 assert not valid(d.replace(token,'CORRUPTED'),True),token
for identity in forbidden:
 assert not valid(d+' '+identity,True),identity
for token in ('[SENDER_NAME]','NOT SENT'):
 assert not valid(d.replace(token,'CORRUPTED'),True),token
answer=(p/'10-independent-answer-key.txt').read_text()
for token in ('replacement reading light','5 November 2026','8 November 2026','[CUSTOMER_NAME]','[SENDER_NAME]','NOT SENT'):
 assert token in answer,token
worksheet=(p/'05-review-worksheet.md').read_text()
assert '09-independent-practice.txt' in worksheet and 'from this exercise' in worksheet
print('PASS: valid source prompt and draft; four required-field corruptions, five returned identifiers and two sender/send-state corruptions rejected by the same validator')
print('PASS: independent answer key facts and source-relative worksheet; fixture checks only, no real-file redaction or assistant execution asserted')
