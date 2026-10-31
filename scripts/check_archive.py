#!/usr/bin/env python3
"""Verify every archived byte matches an explicitly registered SHA-256; stdlib only."""
from pathlib import Path
import json,hashlib,sys
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'raw'
MAN=RAW/'MANIFEST.json'
try: m=json.loads(MAN.read_text(encoding='utf-8'))['items']
except (OSError,ValueError,KeyError) as e: raise SystemExit(f'FAIL: manifest missing/invalid: {e}')
found={p.relative_to(ROOT).as_posix() for p in RAW.rglob('*') if p.is_file() and p.name not in {'.gitkeep','MANIFEST.json'}}
registered=set(m)
issues=[]
for rel in sorted(registered|found):
 if rel not in found: issues.append('MISSING: '+rel);continue
 if rel not in registered:issues.append('UNREGISTERED: '+rel);continue
 data=(ROOT/rel).read_bytes(); item=m[rel]
 actual=hashlib.sha256(data).hexdigest()
 if actual!=item.get('sha256'):issues.append('HASH MISMATCH: '+rel)
 if len(data)!=item.get('size_bytes'):issues.append('SIZE MISMATCH: '+rel)
 if not rel.startswith('raw/'):issues.append('INVALID PATH: '+rel)
if issues:
 print('Archive integrity FAILED:');print('\n'.join(issues));sys.exit(1)
print(f'Archive verified: {len(registered)} registered files, exact hashes and sizes.')
