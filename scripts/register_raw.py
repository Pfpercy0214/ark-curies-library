#!/usr/bin/env python3
"""Human-only tool: register additional paper bytes without ever replacing older records."""
import argparse,json,hashlib
from pathlib import Path
from datetime import date
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'raw'
MAN=RAW/'MANIFEST.json'
p=argparse.ArgumentParser(description='Register new human-reviewed source files; never modify existing archive hashes.')
p.add_argument('files',nargs='+',help='existing raw/papers/*.md paths')
p.add_argument('--origin',default='Human-provided Markdown conversion; confirm full source provenance in history/ files')
a=p.parse_args()
d=json.loads(MAN.read_text(encoding='utf8')); records=d['items']; staged={}
for name in a.files:
 f=(ROOT/name).resolve()
 if not f.is_relative_to((RAW/'papers').resolve()) or not f.is_file() or f.suffix.lower()!='.md': p.error('Only raw/papers/*.md imports are allowed: '+name)
 rel=f.relative_to(ROOT).as_posix()
 val={'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'size_bytes':f.stat().st_size,'origin':a.origin,'ingested_date':date.today().isoformat(),'locked':True}
 if rel in records:
  if records[rel]['sha256']!=val['sha256']:p.error('existing source has changed. Refusing registration: '+rel)
  print('Already registered: '+rel)
 else:staged[rel]=val
# Do not approve a replacement hash under the guise of a new registration
records.update(staged)
MAN.write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n',encoding='utf8')
print(f'Registered {len(staged)} new paper(s). Now run python scripts/check_archive.py and review history/provenance.')
