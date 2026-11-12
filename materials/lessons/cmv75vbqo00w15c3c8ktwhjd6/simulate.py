"""Academy fictional classroom simulation. No network, mail, deletion or purchases."""
import json
from pathlib import Path

REQUIRED = ('Submission ID', 'Name', 'Reply address', 'Request type', 'Message')
MAPPING = {'Name': 'Contact name', 'Reply address': 'Reply address', 'Message': 'Enquiry summary'}

def route(record):
    missing = [field for field in REQUIRED if not str(record.get(field, '')).strip()]
    if missing:
        return {'route': 'Manual clarification', 'missing': missing, 'record': dict(record)}
    match = record['Request type'] == 'Workshop request'
    output = {'Submission ID': record['Submission ID'], 'Category': record['Request type']}
    output.update({destination: record[source] for source, destination in MAPPING.items()})
    if not match:
        output['Review instruction'] = 'Review category manually'
    return {'route': 'Workshop review draft' if match else 'Manual-review record', 'record': output}

if __name__ == '__main__':
    inputs = json.loads(Path(__file__).with_name('fictional-submissions.json').read_text())
    print(json.dumps([route(row) for row in inputs], indent=2))
