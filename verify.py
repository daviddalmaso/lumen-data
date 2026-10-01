"""Verify offline snapshots without making network requests."""
import csv, hashlib, io, json
from pathlib import Path
root = Path(__file__).parent
manifest = json.loads((root/'manifest.json').read_text())
checked = 0
for dataset in manifest['datasets']:
    for extension, digest in dataset['sha256'].items():
        path = root/'data'/f"{dataset['id']}.{extension}"
        raw = path.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == digest, path
        records = list(csv.DictReader(io.StringIO(raw.decode(), newline=''))) if extension == 'csv' else json.loads(raw)
        assert len(records) == dataset['row_count'], path
        checked += 1
print(f'Verified {checked} files from release {manifest["version"]}.')
