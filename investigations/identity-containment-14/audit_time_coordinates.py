#!/usr/bin/env python3
"""Audit recorded coordinates, not event physics; do not silently convert units."""
import argparse, hashlib, io, json, zipfile
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
assert not a.output.exists(), 'Refusing overwrite'
b=(a.data_dir/'BL2data.zip').read_bytes()
assert hashlib.sha256(b).hexdigest()=='ac95e2e141a62c1ea507c764cd6ce6f3db3e0236e509dc3b56d1714f4de8b6f9'
rows=[]
with zipfile.ZipFile(io.BytesIO(b)) as z:
 for name in z.namelist():
  text=z.read(name).decode('utf-8-sig').splitlines();k=next(i for i,s in enumerate(text) if s.lower().startswith('energy ('))
  x=np.genfromtxt(io.StringIO('\n'.join(text[k+1:])),delimiter=',');t=x[:,1];good=np.isfinite(x[:,0]);assert np.isfinite(t).all()
  r={'member':name,'rows':len(t),'minimum':float(t.min()),'maximum':float(t.max()),'integer_time_rows':int(np.isclose(t,np.round(t),atol=1e-9,rtol=0).sum()),'fractional_time_rows':int((~np.isclose(t,np.round(t),atol=1e-9,rtol=0)).sum()),'negative_time_rows':int((t<0).sum()),'missing_energy':int((~good).sum())}
  if (~good).any():r['complete_time_range']=[float(t[good].min()),float(t[good].max())];r['missing_time_range']=[float(t[~good].min()),float(t[~good].max())]
  rows.append(r)
a.output.write_text(json.dumps(rows,indent=2)+'\n');print('Audited',len(rows),'unmodified member time coordinates')
