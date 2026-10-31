"""Read-only approved-addition checks; does not replace archive-guard or source review."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[2]
old=json.loads((R/'history/ingestion/manifest-baseline-before-papers.json').read_text())
new=json.loads((R/'raw/MANIFEST.json').read_text())
assert {k:v for k,v in old.items() if k!='items'}=={k:v for k,v in new.items() if k!='items'},'Manifest metadata changed'
for p,v in old['items'].items():
 assert new['items'][p]==v, 'Old manifest record changed: '+p
 assert hashlib.sha256((R/p).read_bytes()).hexdigest()==v['sha256'], 'Old raw bytes changed: '+p
prepared=json.loads((R/'history/ingestion/prepared-papers.json').read_text())
paths={x['path'] for x in prepared}
assert len(paths)==len(prepared),'Duplicate prepared path'
assert set(new['items'])-set(old['items'])==paths,'Unaccounted archive additions'
for x in prepared:
 p=x['path'];b=(R/p).read_bytes();v=new['items'][p]
 assert hashlib.sha256(b).hexdigest()==x['sha256']==v['sha256'],'Prepared hash mismatch: '+p
 assert len(b)==x['size_bytes']==v['size_bytes'],'Prepared size mismatch: '+p
 assert (R/x['audit']).is_file() and (R/x['independent_verification']).is_file(),'Missing review records: '+p
 assert x['status']=='IMPORT_PREPARED_UNMERGED','Unexpected status: '+p
for x in json.loads((R/'history/ingestion/paper-001-evidence-assets.json').read_text()):
 b=(R/x['path']).read_bytes()
 assert hashlib.sha256(b).hexdigest()==x['sha256'] and len(b)==x['size_bytes'],'Pilot evidence changed'
assert (R/'investigations/conversions/paper-001/draft.md').read_bytes()==(R/'raw/papers/paper-001-temporal-geometry-conv-01.md').read_bytes(),'Pilot copy changed'
print(f'Prepared batch verified: {len(prepared)} new paper files; all {len(old["items"])} prior records/bytes unchanged; review records and original pilot evidence present.')
print('Integrity/provenance gates only; source reviews are recorded separately. Not a merge or scientific validation.')
