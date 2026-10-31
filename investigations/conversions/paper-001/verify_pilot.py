"""Read-only byte/page-accounting check for this exact pilot revision; no approval implied."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
errors = []
def check(rel, sha, size=None):
    path = ROOT / rel
    if not path.is_file():
        errors.append('Missing: ' + rel)
        return
    data = path.read_bytes()
    if hashlib.sha256(data).hexdigest() != sha:
        errors.append('SHA-256 mismatch: ' + rel)
    if size is not None and len(data) != size:
        errors.append('Size mismatch: ' + rel)

check('investigations/conversions/paper-001/draft.md',
      'b2b53855a34301c8930c2e24e469f0e53a3bf819ee941d9e5bdb714b0e81a8be', 71441)
assets = json.loads((ROOT / 'history/ingestion/paper-001-evidence-assets.json').read_text())
for asset in assets:
    check(asset['path'], asset['sha256'], asset['size_bytes'])
baseline = json.loads((ROOT / 'history/ingestion/raw-baseline-sha256.json').read_text())
for rel, sha in baseline.items():
    check(rel, sha)
actual_raw = {p.relative_to(ROOT).as_posix() for p in (ROOT / 'raw').rglob('*') if p.is_file()}
if actual_raw != set(baseline):
    errors.append('Raw path set changed from pilot baseline')
pages = json.loads((ROOT / 'history/ingestion/volume-page-coverage.json').read_text())
pairs = [(p['volume'], p['pdf_page']) for p in pages]
expected = {('V1', n) for n in range(1, 275)} | {('V2', n) for n in range(1, 204)}
if len(pairs) != 477 or len(set(pairs)) != 477 or set(pairs) != expected:
    errors.append('Compiled-volume page coverage is incomplete or duplicated')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('Pilot verified: draft bytes, 3 evidence assets, unchanged raw baseline, 477 unique source pages.')
print('This is not source-fidelity validation, scientific validation, rendering certification, or owner approval.')
