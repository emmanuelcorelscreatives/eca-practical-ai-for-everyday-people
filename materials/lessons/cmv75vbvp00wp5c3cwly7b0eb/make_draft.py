"""Optional local manual-simulation utility; no network or cloud service."""
import json
import pathlib
import sys

def render(record):
    required = ('name', 'email', 'workshop_topic', 'question', 'preferred_month')
    if any(key not in record or not isinstance(record[key], str) for key in required):
        raise ValueError('All five submitted fields must be strings, including an empty optional month.')
    month = record['preferred_month'] or 'Not supplied — reviewer must confirm'
    return ('DRAFT — NOT SENT\n\nHello ' + record['name'] + ',\n\n'
            + 'Workshop topic: ' + record['workshop_topic'] + '\n'
            + 'Question: ' + record['question'] + '\n'
            + 'Preferred month: ' + month + '\n\nReviewer notes:\n\n')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python3 make_draft.py INPUT.json NEW_OUTPUT.md')
    text = render(json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')))
    destination = pathlib.Path(sys.argv[2])
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open('x', encoding='utf-8', newline='') as handle:
        handle.write(text)
    print('Local manual simulation saved; no message sent: ' + str(destination))
