#!/usr/bin/env python3
"""IC-12: bounded public-file intake and fail-closed analysis contract.
Standard library only. Does not infer the unseen NIST event schema or fit data.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import stat
import tempfile
import urllib.parse
import urllib.request
import zipfile

BASE = 'https://data.nist.gov/od/ds/mds2-3859/'
FILES = ('README.txt', 'BL2data.zip', 'BL2Simulations.zip', 'BL1simanddata.zip', 'RGA_data.txt')
HOSTS = {'data.nist.gov', 'nist-oar-cache.s3.amazonaws.com'}
CHUNK = 1024 * 1024

def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(CHUNK), b''):
            h.update(block)
    return h.hexdigest()

def check_url(url: str) -> None:
    p = urllib.parse.urlsplit(url)
    if p.scheme != 'https' or p.hostname not in HOSTS or p.username or p.password:
        raise ValueError('URL outside the declared HTTPS source/redirect hosts')

class PublicRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def inventory_zip(path: Path, limit: int = 1024**3) -> list[dict]:
    """Read and hash members, checking CRC; never extract or execute them."""
    rows = []
    seen = set()
    with zipfile.ZipFile(path) as archive:
        entries = archive.infolist()
        if len(entries) > 10000 or sum(i.file_size for i in entries) > limit:
            raise ValueError('Archive inventory exceeds declared resource limit')
        for item in entries:
            p = PurePosixPath(item.filename)
            mode = item.external_attr >> 16
            if (p.is_absolute() or '..' in p.parts or '\\' in item.filename
                    or ':' in item.filename or stat.S_ISLNK(mode) or item.flag_bits & 1):
                raise ValueError('Unsafe or encrypted archive member')
            name = p.as_posix()
            if name in seen:
                raise ValueError('Duplicate normalized archive path')
            seen.add(name)
            if item.is_dir():
                continue
            h = hashlib.sha256()
            with archive.open(item) as stream:
                for block in iter(lambda: stream.read(CHUNK), b''):
                    h.update(block)
            rows.append({'path': name, 'size_bytes': item.file_size, 'sha256': h.hexdigest()})
    return rows

def inspect(path: Path, limit: int = 1024**3) -> dict:
    result = {'filename': path.name, 'size_bytes': path.stat().st_size,
              'sha256': digest(path), 'publisher_checksum': None}
    if path.suffix.lower() == '.zip':
        result['members'] = inventory_zip(path, limit)
    else:
        if path.stat().st_size > limit:
            raise ValueError('Text exceeds declared resource limit')
        text = path.read_text(encoding='utf-8-sig')
        if not text.strip() or text.lstrip().lower().startswith(('<!doctype html', '<html')):
            raise ValueError('Empty text or HTML error page')
        result['text_lines'] = len(text.splitlines())
    result['interpretation'] = 'Byte integrity/format only; schema and scientific provenance still require review'
    return result

def fetch_file(name: str, directory: Path, limit: int = 512*1024**2) -> dict:
    if name not in FILES:
        raise ValueError('Unknown distribution filename')
    directory.mkdir(parents=True, exist_ok=True)
    target = directory / name
    if target.exists():
        raise FileExistsError('Refusing to replace an existing source file')
    url = BASE + name
    check_url(url)
    opener = urllib.request.build_opener(PublicRedirect())
    temp = None
    try:
        with opener.open(urllib.request.Request(url, headers={'User-Agent': 'ARK-IC12-intake/1'}), timeout=20) as source:
            check_url(source.geturl())
            with tempfile.NamedTemporaryFile(dir=directory, suffix=Path(name).suffix, delete=False) as out:
                temp = Path(out.name)
                size = 0
                for block in iter(lambda: source.read(CHUNK), b''):
                    size += len(block)
                    if size > limit:
                        raise ValueError('Download exceeds declared byte limit')
                    out.write(block)
            result = inspect(temp)
            # Same-filesystem link is atomic and refuses a concurrent overwrite.
            os.link(temp, target)
            result.update(filename=name, url=url, final_url=source.geturl(),
                          retrieved_utc=datetime.now(timezone.utc).isoformat())
            return result
    finally:
        if temp is not None:
            temp.unlink(missing_ok=True)

def readiness(spec: dict, root: Path) -> dict:
    """A mechanical gate, not certification that declared mappings are true."""
    issues = []
    target = spec.get('target')
    if target not in ('spectral_composition', 'absolute_decay_rate'):
        issues.append('target must be explicitly selected')
    for key in ('schema_evidence', 'energy_mapping', 'timing_mapping', 'selection_rule',
                'background_model', 'response_model', 'calibration_evidence',
                'prior_exposure_record', 'evaluation_rule', 'grouping_evidence'):
        value = spec.get(key)
        if not isinstance(value, str) or not value.strip() or value in ('UNKNOWN', 'TBD'):
            issues.append(f'{key} unresolved')
    groups = []
    for key in ('calibration_groups', 'evaluation_groups'):
        value = spec.get(key)
        if not isinstance(value, list) or not value or not all(isinstance(x, str) and x.strip() for x in value):
            issues.append(f'{key} absent or invalid')
            value = []
        if len(value) != len(set(value)):
            issues.append(f'{key} has duplicates')
        groups.append(set(value))
    if groups[0] & groups[1]:
        issues.append('calibration and evaluation groups overlap')
    inputs = spec.get('inputs')
    if not isinstance(inputs, list) or not inputs:
        issues.append('no input files registered')
        inputs = []
    if not any(isinstance(i, dict) and i.get('role') == 'observed_events' for i in inputs):
        issues.append('no observed-event input declared')
    resolved_root = root.resolve()
    for item in inputs:
        if not isinstance(item, dict) or not isinstance(item.get('path'), str):
            issues.append('invalid input record')
            continue
        path = (root/item['path']).resolve()
        if not path.is_relative_to(resolved_root) or not path.is_file():
            issues.append(f'input missing or outside root: {item["path"]}')
        elif digest(path) != item.get('sha256'):
            issues.append(f'input hash mismatch: {item["path"]}')
    if target == 'absolute_decay_rate':
        for key in ('absolute_exposure', 'absolute_efficiencies', 'channel_completeness', 'upstream_invariance'):
            value = spec.get(key)
            if not isinstance(value, str) or not value.strip() or value in ('UNKNOWN', 'TBD'):
                issues.append(f'{key} unresolved')
    return {'status': 'BLOCKED' if issues else 'READY_FOR_REVIEW', 'issues': issues,
            'qualification': 'Self-declared evidence fields must be checked; this tool grants no empirical approval'}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    f = sub.add_parser('fetch')
    f.add_argument('directory', type=Path)
    f.add_argument('--files', nargs='+', choices=FILES, default=['README.txt'])
    f.add_argument('--max-download-mb', type=int, default=512)
    i = sub.add_parser('inspect')
    i.add_argument('file', type=Path)
    i.add_argument('--max-unpacked-mb', type=int, default=1024)
    v = sub.add_parser('validate')
    v.add_argument('spec', type=Path)
    v.add_argument('--root', type=Path, required=True)
    args = parser.parse_args()
    if args.command == 'fetch':
        reports = []
        for name in args.files:
            try:
                reports.append({'status': 'RETRIEVED', **fetch_file(name, args.directory, args.max_download_mb*1024**2)})
            except Exception as error:
                reports.append({'filename': name, 'status': 'FAILED', 'error': f'{type(error).__name__}: {error}'})
        print(json.dumps({'attempt_utc': datetime.now(timezone.utc).isoformat(), 'files': reports}, indent=2))
        raise SystemExit(0 if all(x['status']=='RETRIEVED' for x in reports) else 2)
    if args.command == 'inspect':
        print(json.dumps(inspect(args.file, args.max_unpacked_mb*1024**2), indent=2))
    else:
        result = readiness(json.loads(args.spec.read_text()), args.root)
        print(json.dumps(result, indent=2))
        raise SystemExit(2 if result['status']=='BLOCKED' else 0)

if __name__ == '__main__':
    main()
