#!/usr/bin/env python3
"""IC-14: retrospective timing-marginal transfer, not decay-rate inference.
Reads original NIST ZIP members in memory, preserves blank energy, hashes inputs.
Requires numpy/scipy. See frozen analysis-contract.json before interpretation.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, platform, zipfile
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import scipy
from scipy.optimize import minimize_scalar
from scipy.special import xlogy

HERE=Path(__file__).resolve().parent
C=json.loads((HERE/'analysis-contract.json').read_text())
PAIR={int(k):v for k,v in C['pairing'].items()}
CAL=C['timing_calibration_groups']; EVAL=C['evaluation_groups']

def digest(b): return hashlib.sha256(b).hexdigest()
def require(ok,msg):
    if not bool(ok): raise ValueError(msg)

def read_member(z,name,manifest):
    b=z.read(name)
    expected=next(r for r in manifest['members'] if r['archive']==Path(z.filename).name and r['member']==name)
    require(digest(b)==expected['sha256'],'Member hash mismatch '+name)
    return b

def parse_events(b):
    lines=b.decode('utf-8-sig').splitlines()
    k=next(i for i,s in enumerate(lines) if s.lower().startswith('energy ('))
    a=np.genfromtxt(io.StringIO('\n'.join(lines[k+1:])),delimiter=',')
    require(a.ndim==2 and a.shape[1]==2,'Event schema')
    require(np.all(np.isfinite(a[:,1])),'Missing time not allowed')
    return a

def edges(): return np.round(np.linspace(-6,60,111),9)
def masks(e,baseline=30.):
    return ((e[:-1]>=0)&(e[1:]<=8.4),
            (e[:-1]>=8.4)&(e[1:]<=30),
            (e[:-1]>=baseline)&(e[1:]<=60))

def shifted_counts(e,s,delta):
    """Integrate original piecewise-constant bin masses into shifted output bins.
    Beyond provided edges, extend only with mean late-template density.
    """
    e0=edges(); cum=np.r_[0,np.cumsum(s)]; x=e-delta
    side=np.mean(s[e0[:-1]>=30])/.6
    y=np.interp(x,e0,cum)
    y=np.where(x<e0[0],(x-e0[0])*side,y)
    y=np.where(x>e0[-1],cum[-1]+(x-e0[-1])*side,y)
    return np.diff(y)

def control_normalize(n,s,e,baseline=30.):
    early,tail,bg=masks(e,baseline)
    M=np.array([[s[early].sum(),early.sum()],[s[bg].sum(),bg.sum()]],float)
    require(abs(np.linalg.det(M))>1e-10,'Normalization rank deficient')
    a,b=np.linalg.solve(M,[n[early].sum(),n[bg].sum()])
    mu=a*s+b
    require(a>0 and np.min(mu)>0,'Nonpositive affine-template prediction')
    return mu,float(a),float(b)

def deviance(n,mu):
    return float(2*np.sum(xlogy(n,n/mu)-(n-mu)))

def fit_shift(hists,sims,e,baseline=30.):
    early,_,_=masks(e,baseline)
    def objective(delta):
        try:
            return sum(deviance(hists[r][early],control_normalize(hists[r],shifted_counts(e,sims[r],delta),e,baseline)[0][early]) for r in CAL)
        except ValueError: return 1e100
    grid=np.linspace(-1.2,1.2,97); vals=np.array([objective(d) for d in grid]); k=int(np.argmin(vals))
    lo=grid[max(0,k-1)]; hi=grid[min(len(grid)-1,k+1)]
    opt=minimize_scalar(objective,bounds=(lo,hi),method='bounded',options={'xatol':1e-10})
    require(opt.success and opt.fun<1e99,'Shift optimization failed')
    candidates=[(float(opt.fun),float(opt.x)),(float(vals[k]),float(grid[k]))]
    score,d=min(candidates)
    return d,dict(shift_us=d,early_deviance=score,nominal_zero_early_deviance=objective(0),
        bound_reached=abs(d)>1.1999,grid_scan=[dict(delta_us=float(x),deviance=float(v)) for x,v in zip(grid,vals)])

def metrics(n,s,e,delta,baseline=30.):
    ss=shifted_counts(e,s,delta); mu,a,b=control_normalize(n,ss,e,baseline)
    early,tail,bg=masks(e,baseline); ne=float(n[early].sum()); obs=float(n[tail].sum()); pred=float(mu[tail].sum())
    M=np.array([[ss[early].sum(),early.sum()],[ss[bg].sum(),bg.sum()]])
    Z=np.c_[ss[tail],np.ones(tail.sum())]@np.linalg.inv(M)
    cov=np.diag(np.maximum(mu[tail],1e-12))+Z@np.diag([ne,float(n[bg].sum())])@Z.T
    r=n[tail]-mu[tail]
    q=float(r@np.linalg.solve(cov,r))
    ones=np.ones(tail.sum()); sd=float(np.sqrt(ones@cov@ones))
    return dict(scale=a,additive_offset_counts_per_bin=b,
        early_count=int(ne),baseline_count=int(n[bg].sum()),tail_observed=int(obs),tail_predicted=pred,
        signed_tail_fractional_residual=(obs-pred)/pred,tail_residual=obs-pred,
        count_only_sd_total_residual_fixed_shift=sd,
        absolute_tail_residual_per_early_count=float(np.abs(r).sum()/ne),
        maximum_cumulative_tail_discrepancy_per_early_count=float(np.max(np.abs(np.cumsum(r)))/ne),
        tail_quadratic_form_fixed_shift=q,tail_bins=int(tail.sum()),
        early_deviance=deviance(n[early],mu[early]),
        minimum_expected_bin=float(mu.min()),
        warning='Quadratic form is a count-only discrepancy diagnostic, not a calibrated p-value; ignores template/systematic/cycle uncertainty'),mu

def closure_tests(hists,sims,e):
    out=[]
    def test(name,fn):
        fn();out.append({'name':name,'status':'PASS'})
    def t0():
        for s in sims.values(): require(np.allclose(shifted_counts(e,s,0),s,rtol=1e-11,atol=1e-8),'Shift identity')
    def t1():
        s=np.ones(110)*7
        for d in [-1.2,0,.173,1.2]: require(np.allclose(shifted_counts(e,s,d),s),'Flat shift')
    def t2():
        for r,s in sims.items():
            n=1.3*s+20;mu,a,b=control_normalize(n,s,e)
            require(np.allclose(mu,n) and abs(a-1.3)<1e-12 and abs(b-20)<1e-8,'Affine recovery')
    def t3():
        r=CAL[0];s=sims[r];n=hists[r].copy();tail=masks(e)[1]
        first=control_normalize(n,s,e)[1:]; n[tail]+=10000
        require(np.allclose(first,control_normalize(n,s,e)[1:]),'Target leaked into normalization')
    def t4():
        hh={r:(1.1+.1*i)*shifted_counts(e,s,.19)+40 for i,(r,s) in enumerate(sims.items())}
        d,_=fit_shift(hh,sims,e); require(abs(d-.19)<1e-6,'Injected shift recovery')
    def t5():
        d,_=fit_shift(hists,sims,e); hh={r:n.copy() for r,n in hists.items()}
        for r in EVAL:hh[r]+=10000
        d2,_=fit_shift(hh,sims,e);require(d==d2,'Evaluation groups leak into shift')
    def t6():
        n=np.array([0.,2.,3.]);require(deviance(n,np.array([1.,2.,3.]))==2,'Zero count likelihood')
    def t7():
        e2=e[::2]
        for s in sims.values():require(np.allclose(shifted_counts(e2,s,0),s.reshape(-1,2).sum(1)),'Coarse integral')
    def t8():
        try: control_normalize(np.ones(110),np.ones(110),e)
        except ValueError:return
        raise AssertionError('No rejection of degenerate template')
    def t9():
        for r in EVAL:
            ss=sims[r];early,tail,bg=masks(e);n=hists[r].astype(float)
            M=np.array([[ss[early].sum(),early.sum()],[ss[bg].sum(),bg.sum()]])
            v=np.array([ss[tail].sum(),tail.sum()])@np.linalg.inv(M)
            _,mu0=metrics(n,ss,e,0)
            for j,m in enumerate([early,bg]):
                a=n.copy();a[np.flatnonzero(m)[0]]+=.01
                _,mu1=metrics(a,ss,e,0)
                require(np.allclose((mu1[tail].sum()-mu0[tail].sum())/.01,v[j],rtol=1e-6),'Control derivative')
    for name,fn in [('shift_identity',t0),('constant_extension',t1),('affine_recovery',t2),('tail_excluded_from_normalization',t3),('synthetic_shift_recovery',t4),('evaluation_groups_excluded_from_shift',t5),('zero_count_deviance',t6),('coarse_mass_integration',t7),('singular_design_rejected',t8),('control_covariance_derivative',t9)]: test(name,fn)
    return out

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--data-dir',type=Path,required=True);parser.add_argument('--output-dir',type=Path,required=True);parser.add_argument('--bootstrap',type=int,default=200)
    args=parser.parse_args();out=args.output_dir
    require(not (out/'results.json').exists(),'Refusing to overwrite existing results')
    out.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((args.data_dir/'NIST_mds2-3859_manifest.json.txt').read_text())
    for fname,key in [('BL2data.zip','data_zip_sha256'),('BL2Simulations.zip','simulation_zip_sha256')]:
        require(digest((args.data_dir/fname).read_bytes())==C[key],fname+' hash mismatch')
    with zipfile.ZipFile(args.data_dir/'BL2Simulations.zip') as z:
        sb=read_member(z,C['simulation_member'],manifest)
        sim=np.loadtxt(io.StringIO(sb.decode('utf-8-sig')),delimiter=',',skiprows=4)
    e=edges(); centers=(e[:-1]+e[1:])/2
    require(np.allclose(sim[:,0],centers),'Simulation grid mismatch')
    sims={r:sim[:,j] for r,j in PAIR.items()};hists={};records={}
    with zipfile.ZipFile(args.data_dir/'BL2data.zip') as z:
        for r in PAIR:
            b=read_member(z,f'Series_{r}.txt',manifest); events=parse_events(b)
            t=np.round(0.1*events[:,1]-53.6,9) if r in [537,538,954,978,1030] else np.round(events[:,1],9); inside=(t>=e[0])&(t<e[-1]); n=np.histogram(t[inside],bins=e)[0]
            missing=~np.isfinite(events[:,0]);mh=np.histogram(t[inside&missing],bins=e)[0]
            hists[r]=n
            records[r]=dict(member_sha256=digest(b),rows=len(events),in_range=int(inside.sum()),before_range=int((t<e[0]).sum()),after_range=int((t>=e[-1]).sum()),missing_energy=int(missing.sum()),missing_energy_times_in_range=int((inside&missing).sum()),role='calibration' if r in CAL else 'evaluation' if r in EVAL else 'zero-ramp diagnostic')
            if missing.any():
                records[r]['missing_energy_timing_counts']={'early':int(mh[masks(e)[0]].sum()),'tail':int(mh[masks(e)[1]].sum()),'late':int(mh[masks(e)[2]].sum()),'before_zero':int(mh[centers<0].sum())}
                np.savetxt(out/f'missing-energy-timing-{r}.csv',np.c_[centers,mh],delimiter=',',header='time_center_us,missing_energy_event_count',comments='')
    d,shift=fit_shift(hists,sims,e)
    # Measurement-tail comparisons occur only after the common shift is fixed.
    comparison={};mus={}
    for r in PAIR:
        met,mu=metrics(hists[r],sims[r],e,d);comparison[r]=met;mus[r]=mu
    sensitivity={}
    dlate,lateinfo=fit_shift(hists,sims,e,40)
    e2=e[::2];h2={r:n.reshape(-1,2).sum(1) for r,n in hists.items()};d2,coarseinfo=fit_shift(h2,sims,e2)
    for label,hh,ee,delta,base in [('zero_shift',hists,e,0.,30.),('late_baseline_40_to_60',hists,e,dlate,40.),('coarse_1p2us',h2,e2,d2,30.)]:
        sensitivity[label]={'shift_us':delta,'evaluation':{r:metrics(hh[r],sims[r],ee,delta,base)[0] for r in EVAL}}
    tests=closure_tests(hists,sims,e)
    rng=np.random.default_rng(1401); samples=[];failed=0
    for _ in range(args.bootstrap):
        hh={r:rng.poisson(n) for r,n in hists.items()}
        try:
            dd,_=fit_shift(hh,sims,e)
            vals=[dd]
            for r in EVAL:
                _,mu=metrics(hh[r],sims[r],e,dd)
                vals.append(float(hh[r][masks(e)[1]].sum()-mu[masks(e)[1]].sum()))
            samples.append(vals)
        except ValueError:failed+=1
    bs=np.asarray(samples)
    bootstrap={'replicates':args.bootstrap,'seed':1401,'success':len(samples),'failed':failed,'scope':'Poisson plug-in resampling of observed histograms. Estimates counting variation conditional on this model/data; not a null-distribution goodness-of-fit test. No template/systematic/cycle covariance.', 'columns':['common_shift_us']+[f'{r}_tail_residual' for r in EVAL]}
    if len(bs)>1:bootstrap.update(mean=bs.mean(0).tolist(),sd=bs.std(0,ddof=1).tolist(),quantiles_025_975=np.quantile(bs,[.025,.975],axis=0).tolist())
    with (out/'timing-comparison.csv').open('w',newline='') as f:
        writer=csv.writer(f); writer.writerow(['series','role','nominal_ramp_V','template_ramp_V','bin_left_us','bin_right_us','observed_triggers','released_template','control_normalized_prediction'])
        for r in PAIR:
            for i in range(110):writer.writerow([r,records[r]['role'],C['nominal_measured_ramp_V'][str(r)],C['released_simulation_ramp_V'][str(r)],e[i],e[i+1],int(hists[r][i]),float(sims[r][i]),float(mus[r][i])])
    result={'study':'IC-14 candidate-coordinate comparison','utc':datetime.now(timezone.utc).isoformat(),'code_sha256':digest(Path(__file__).read_bytes()),'contract_sha256':digest((HERE/'analysis-contract.json').read_bytes()),'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'candidate_contract_sha256':digest((HERE/'candidate-coordinate-contract.json').read_bytes()),'mapping_status':'INFERRED_NOT_INDEPENDENTLY_CONFIRMED','scope':'Conditional mapped actual event timing marginal compared with released adjusted apparatus templates; no energy fit, exposure/lifetime inference, epsilon or ARK coupling','records':records,'shift_calibration':shift,'comparisons':comparison,'sensitivity':sensitivity,'count_only_bootstrap':bootstrap,'software_checks':tests,'checks_passed':len(tests),'independent_review':False}
    (out/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'shift_us':d,'calibration':{k:shift[k] for k in ['early_deviance','nominal_zero_early_deviance']},'records':records,'comparisons':{r:{k:v for k,v in met.items() if k in ['tail_observed','tail_predicted','signed_tail_fractional_residual','tail_quadratic_form_fixed_shift']} for r,met in comparison.items()},'bootstrap':bootstrap,'checks':len(tests)},indent=2))
if __name__=='__main__':main()
