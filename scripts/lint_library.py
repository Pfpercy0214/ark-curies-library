#!/usr/bin/env python3
"""Lightweight local hygiene; not a scientific validator."""
from pathlib import Path
import re,sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
for p in ROOT.rglob('*.md'):
 if 'raw' in p.relative_to(ROOT).parts:continue # source text may contain any historical link shape
 s=p.read_text(encoding='utf8')
 for dest in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',s):
  target=dest.split('#')[0].split('?')[0].strip()
  if not target or '://' in target or target.startswith(('mailto:','#')):continue
  if not (p.parent/target).resolve().exists():errors.append(f'{p.relative_to(ROOT)}: broken link {target}')
if errors:
 print('\n'.join(errors));sys.exit(1)
print('Markdown local link check passed (non-raw files).')
