#!/usr/bin/env python3
"""IC-11: published simulation-response benchmark, NOT event-data validation.
NIST/Caylor arXiv:2506.01682v2 Tables 2/3, transcribed from accessible HTML.
Run: python check_ic11.py --output test-results.json
Requires numpy, scipy, sympy. Never converts simulation rows into measurements.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import itertools
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import sympy as sp

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'published_response.csv'
BL1_DATA = ROOT / 'bl1_response.csv'
CHECKS: list[dict] = []
P_KEYS = ('p_ruth_pct', 'p_below_threshold_pct', 'p_stopped_pct')
H_KEYS = ('h_both_ruth_pct', 'h_below_threshold_pct', 'h_both_stopped_pct', 'h_cross_term_pct')
with DATA.open(encoding='utf-8', newline='') as stream:
    ROWS = [{k: float(v) for k, v in row.items()} for row in csv.DictReader(stream)]

with BL1_DATA.open(encoding='utf-8', newline='') as stream:
    BL1 = [{k: float(v) for k, v in row.items()} for row in csv.DictReader(stream)]

def require(ok, message):
    if not bool(ok):
        raise AssertionError(message)

def close(a, b, rtol=1e-10, atol=1e-13):
    require(np.allclose(a, b, rtol=rtol, atol=atol), f'{a} != {b}')

def row(au, voltage):
    matches = [r for r in ROWS if r['au_ug_cm2'] == au and r['acceleration_kv'] == voltage]
    if len(matches) != 1:
        raise ValueError('Configuration absent or duplicated')
    return matches[0]

def efficiencies(r, mode='printed'):
    if mode == 'printed':
        ep, eh = r['p_eff_reported_pct']/100, r['h_eff_reported_pct']/100
    elif mode == 'components':
        ep, eh = 1-sum(r[k] for k in P_KEYS)/100, 1-sum(r[k] for k in H_KEYS)/100
    else:
        raise ValueError('Unknown coefficient source')
    if not 0 < ep <= 1 or not 0 < eh <= 1:
        raise ValueError('Invalid efficiencies')
    return ep, eh

def contrast(r, mode='printed'):
    ep, eh = efficiencies(r, mode)
    return eh/ep-1

def lifetime_bias(f, ep, eh):
    if not 0 <= f <= 1 or not 0 < ep <= 1 or not 0 < eh <= 1:
        raise ValueError('Invalid fraction or efficiency')
    return 1/(1+f*(eh/ep-1))-1

def infer(z, k):
    """Return intercept Gamma and fraction from two exposure-normalized rates.
    No physical clipping of unconstrained noisy estimates is performed.
    """
    k = np.asarray(k, float)
    z = np.asarray(z, float)
    if k.shape != (2,) or z.shape != (2,) or abs(k[1]-k[0]) < 1e-12:
        raise ValueError('Two distinct, calibrated response contrasts required')
    a, b = np.linalg.solve(np.c_[np.ones(2), k], z)
    if a <= 0:
        raise ValueError('Nonpositive rate estimate')
    return float(a), float(b/a)

def component_flags():
    flags = []
    for r in ROWS:
        for species, keys, reported in [('p', P_KEYS, 'p_eff_reported_pct'),
                                        ('h2', H_KEYS, 'h_eff_reported_pct')]:
            # A diagnostic assuming nearest rounding of each printed decimal.
            center = 100-sum(r[k] for k in keys)
            lo = 100-sum(r[k]+.0005 for k in keys)
            hi = 100-sum(max(0., r[k]-.0005) for k in keys)
            printed_lo = max(0., r[reported]-.05)
            printed_hi = min(100., r[reported]+.05)
            if hi < printed_lo-1e-10 or lo > printed_hi+1e-10:
                flags.append(dict(au_ug_cm2=r['au_ug_cm2'], voltage_kv=r['acceleration_kv'],
                    species=species, component_sum_eff_pct=center,
                    component_rounding_interval_pct=[lo, hi],
                    printed_eff_pct=r[reported], printed_rounding_interval_pct=[printed_lo, printed_hi]))
    return flags

def schema_and_pairing():
    require(len(ROWS) == 30, 'Expected 30 paired configurations')
    require(len({(r['au_ug_cm2'], r['acceleration_kv']) for r in ROWS}) == 30, 'duplicates')
    for r in ROWS:
        close(2*r['h_half_energy_kev'], r['acceleration_kv'])
        efficiencies(r)
    return dict(rows=30, threshold_kev=6.0, half_energy_pairing='checked',
        provenance='Published SRIM+Monte Carlo point estimates; not experimental observations')

def audit_inputs():
    flags = component_flags()
    require(len(flags) == 4, 'Changed source-consistency finding')
    require(all(f['species'] == 'h2' for f in flags), 'Unexpected proton-table flag')
    ep, eh = efficiencies(row(0, 32.5), 'components')
    require(eh < 1 and row(0,32.5)['h_eff_reported_pct'] == 100, 'Rounded 100 is not exact')
    return dict(unresolved_flags=flags,
        decision='Retain both columns; use printed efficiencies as primary, components as sensitivity branch. No error adjudication without source check.')

def bias_sign_and_size():
    examples = []
    for au, voltage in [(0,25),(20,25),(40,25),(60,25),(80,25),(100,25),(100,35)]:
        r = row(au,voltage); ep,eh=efficiencies(r)
        examples.append(dict(au_ug_cm2=au,voltage_kv=voltage,eta_p=ep,eta_h2=eh,
            imposed_f=.05,relative_lifetime_bias=lifetime_bias(.05,ep,eh)))
    require(examples[1]['relative_lifetime_bias'] < 0, 'Thin response sign')
    require(examples[-2]['relative_lifetime_bias'] > .01, 'Thick low-voltage response')
    require(0 < examples[-1]['relative_lifetime_bias'] < .001, 'Thick high-voltage response')
    q, p, h = sp.symbols('q p h', positive=True)
    expression=p/((1-q)*p+q*h)-1
    require(sp.simplify(expression + q*(h-p)/(p+q*(h-p))) == 0, 'Bias algebra')
    values=[]
    for voltage in [25,35]:
        k=contrast(row(100,voltage)); target=.01
        f=(1/(1+target)-1)/k
        values.append(dict(voltage_kv=voltage,imposed_upward_bias=target,required_f=f))
    return dict(examples=examples,required_fraction_for_one_percent=values,
        scope='Hypothetical matched admixture; not an estimate or correction of any published neutron lifetime')

def observed_vs_trapped():
    records=[]
    for au, voltage in [(20,25),(100,25),(100,35)]:
        ep,eh=efficiencies(row(au,voltage)); f=.05
        detected=f*eh/((1-f)*ep+f*eh)
        recovered=detected*ep/(eh*(1-detected)+detected*ep)
        close(recovered,f)
        records.append(dict(au=au,voltage=voltage,trapped_fraction=f,detected_fraction=detected))
    return dict(cases=records,scope='A fitted detected admixture requires an efficiency map before interpreting it as a trapped fraction')

def reconstruction_rank():
    k=np.array([contrast(row(100,25)),contrast(row(100,35))])
    gamma=.001; f=.04; z=gamma*(1+f*k)
    found=infer(z,k); close(found,[gamma,f])
    a,b,k1,k2=sp.symbols('a b k1 k2')
    M=sp.Matrix([[1,k1],[1,k2]])
    require(sp.simplify(M.det()-(k2-k1))==0,'rank')
    record=[]
    for au in [20,100]:
        kk=np.array([contrast(row(au,25)),contrast(row(au,35))])
        record.append(dict(au=au,contrasts=kk.tolist(),separation=float(kk[1]-kk[0]),
            design_condition_number=float(np.linalg.cond(np.c_[np.ones(2),kk]))))
    return dict(injected_Gamma=gamma,injected_fraction=f,recovered=found,designs=record,
        input_contract='Absolute exposure and each efficiency characterized; upstream fraction/rate invariant across readout settings')

def unused_setting_transfer():
    gamma=.001; f=.04
    endpoints=[row(100,25),row(100,35)]
    k=np.array([contrast(r) for r in endpoints]); z=gamma*(1+f*k)
    a,ff=infer(z,k)
    r=row(100,30); ep,eh=efficiencies(r)
    predicted=ep*a*(1+ff*contrast(r))
    generated=gamma*((1-f)*ep+f*eh)
    close(predicted,generated)
    wrong=generated*1.01
    mismatch=(wrong-predicted)/predicted
    close(mismatch,.01)
    return dict(voltage_calibration=[25,35],unused_voltage=30,
        predicted_yield=predicted,independently_evaluated_generation=generated,
        deliberately_added_midpoint_recording_change=.01,relative_residual=mismatch,
        warning='Synthetic transfer with known coefficients, not a blind holdout or validation on measured events')

def uncertainty_and_covariance():
    k=np.array([contrast(row(100,25)),contrast(row(100,35))]); M=np.c_[np.ones(2),k]
    a=.001; f=.04; z=a*(1+f*k); frac_sigma=.001
    D=np.diag((frac_sigma*z)**2); inv=np.linalg.inv(M)
    covab=inv@D@inv.T; J=np.array([[1,0],[-f/a,1/a]])
    covariance=J@covab@J.T
    rng=np.random.default_rng(1101); noise=rng.normal(size=(40000,2))*frac_sigma*z
    ab=(z+noise)@inv.T; samples=np.c_[ab[:,0],ab[:,1]/ab[:,0]]
    actual=np.cov(samples,rowvar=False); ratio=np.sqrt(np.diag(actual)/np.diag(covariance))
    require(np.all(abs(ratio-1)<.02),'Delta-method Monte Carlo comparison')
    coverage=np.mean(abs(samples-[a,f])<=1.96*np.sqrt(np.diag(covariance)),axis=0)
    require(np.all((coverage>.94)&(coverage<.96)),'Generated coverage')
    scaled=infer(1.002*z,k); close(scaled,[1.002*a,f])
    skewed=infer(z*np.array([1.001,.999]),k)
    return dict(replicas=40000,seed=1101,assumed_independent_relative_sigma=frac_sigma,
        delta_standard_deviations=np.sqrt(np.diag(covariance)).tolist(),
        simulation_standard_deviations=np.sqrt(np.diag(actual)).tolist(),
        approximate_95percent_coverage=coverage.tolist(),
        common_gain_reconstruction=scaled,opposed_gain_reconstruction=skewed,
        warning='Invented measurement errors for design verification; excludes real response-model calibration uncertainty')

def weak_design():
    results=[]
    for au in [20,100]:
        k=np.array([contrast(row(au,25)),contrast(row(au,35))]); M=np.c_[np.ones(2),k]
        a=.001; f=.04; z=a*(1+f*k); inv=np.linalg.inv(M)
        J=np.array([[1,0],[-f/a,1/a]])
        cov=J@inv@np.diag((.001*z)**2)@inv.T@J.T
        results.append(dict(au=au,sigma_fraction=float(np.sqrt(cov[1,1]))))
    require(results[0]['sigma_fraction']>50*results[1]['sigma_fraction'],'weak contrast')
    return dict(designs=results,warning='Full rank does not imply useful precision; no clipping of unphysical noisy inversions')

def coefficient_rounding_and_branch():
    endpoints=[row(100,25),row(100,35)]
    nominal=[efficiencies(r) for r in endpoints]; k=np.array([h/p-1 for p,h in nominal])
    a=.001; f=.04; y=np.array([a*((1-f)*p+f*h) for p,h in nominal])
    estimates=[]
    for bits in itertools.product([-1,1],repeat=4):
        v=np.array(nominal).ravel()+.0005*np.array(bits)
        p=v[::2];h=v[1::2]; kk=h/p-1
        estimates.append(infer(y/p,kk))
    estimates=np.asarray(estimates)
    component=[efficiencies(r,'components') for r in endpoints]
    p=np.array([v[0] for v in component]);h=np.array([v[1] for v in component])
    alt=infer(y/p,h/p-1)
    require(np.all(np.isfinite(estimates)),'rounding vertices')
    return dict(printed_efficiency_rounding_halfwidth=.0005,
        tested_rounding_vertex_Gamma_range=[float(min(estimates[:,0])),float(max(estimates[:,0]))],
        tested_rounding_vertex_fraction_range=[float(min(estimates[:,1])),float(max(estimates[:,1]))],
        component_branch_reconstruction=alt,
        scope='Sensitivity at 16 rounding vertices only; not a total systematic confidence interval or global physical bound')

def remaining_aliases():
    k=np.array([contrast(row(100,v)) for v in [25,27.5,30,32.5,35]])
    gamma=.001; f=.04; z=gamma*(1+f*k)
    # Any common missed fraction rescales the rate while preserving this line.
    close(.98*z,(.98*gamma)*(1+f*k))
    # Detector-dependent upstream back-action can exactly mimic composition.
    f_alt=.01; gamma_by_setting=z/(1+f_alt*k)
    close(gamma_by_setting*(1+f_alt*k),z)
    # Two settings always fit two unknowns: no residual degrees of freedom.
    recovered=infer(z[[0,-1]],k[[0,-1]])
    close(recovered,[gamma,f])
    return dict(common_missing_fraction=.02,indistinguishable_rate=.98*gamma,
        alternative_fraction=f_alt,indistinguishable_setting_dependent_rates=gamma_by_setting.tolist(),
        scope='More readout settings cannot rule out a perfectly common loss or unconstrained upstream changes')

def birth_average(z):
    if z<0: raise ValueError('Negative hazard-time product')
    if z<1e-5: return 1-z/2+z*z/6-z**3/24
    return -np.expm1(-z)/z

def reaction_transfer():
    r=8.0; times=[.002,.01,.05]
    out=[]
    for T in times:
        f=1-birth_average(r*T)
        sol=solve_ivp(lambda t,x:[1-r*x[0],r*x[0]],(0,T),[0,0],rtol=1e-11,atol=1e-14)
        close(sol.y[1,-1]/T,f,rtol=1e-9)
        inferred=brentq(lambda value:1-birth_average(value*T)-f,0,1000,xtol=1e-12)
        close(inferred,r)
        out.append(dict(T_seconds=T,f=f,recovered_reaction_rate=inferred))
    # A rate inferred from f is NOT an independent measurement of gas density.
    return dict(imposed_reaction_rate_s_inverse=r,cases=out,
        warning='Independent uniform production and reaction assumptions required; a measured gas pressure is not ARK epsilon')

def bl1_specific_configuration():
    require(len(BL1)==13 and len({r['series'] for r in BL1})==13,'Thirteen original settings')
    require(all(r['au_ug_cm2']<100 for r in BL1),'Thick benchmark was not a BL1 setting')
    differences=[]
    for r in BL1:
        nominal=r['p_eff_reported_pct']-r['h_eff_reported_pct']
        # Three printed one-decimal quantities can differ by at most .15 pp under nearest rounding.
        require(abs(nominal-r['difference_reported_pct'])<=.15+1e-12,'Difference-column audit')
        ep,eh=efficiencies(r)
        differences.append(dict(series=int(r['series']),threshold_kev=r['threshold_kev'],
            imposed_f=.01,relative_lifetime_bias=lifetime_bias(.01,ep,eh)))
    return dict(settings=13,threshold_range_kev=[min(r['threshold_kev'] for r in BL1),max(r['threshold_kev'] for r in BL1)],
        hypothetical_individual_series_biases=differences,
        warning='No averaging: original event weights, covariance and backscatter extrapolation not analyzed. Not a reproduction of the authors lifetime correction.')

def threshold_transfer_counterexample():
    selected=next(r for r in BL1 if r['series']==149)
    generic=row(selected['au_ug_cm2'],selected['acceleration_kv'])
    ep,eh=efficiencies(generic); ep1,eh1=efficiencies(selected)
    generic_bias=lifetime_bias(.01,ep,eh); specific_bias=lifetime_bias(.01,ep1,eh1)
    require(generic_bias<0<specific_bias,'Loss of transfer across acquisition conditions')
    return dict(series=149,generic_threshold_kev=6.,series_threshold_kev=selected['threshold_kev'],
        generic_contrast=eh/ep-1,series_contrast=eh1/ep1-1,
        imposed_f=.01,generic_bias=generic_bias,series_bias=specific_bias,
        scope='Source-specific response differs; cannot attribute entire difference to threshold alone without rerunning detector simulation')

def invalid_inputs():
    rejected=0
    for args in [(-.1,.9,.8),(1.1,.9,.8),(.1,0,.8),(.1,.9,1.1)]:
        try: lifetime_bias(*args)
        except ValueError: rejected+=1
    try: infer([.001,.001],[.01,.01])
    except ValueError: rejected+=1
    try: row(100,26)
    except ValueError: rejected+=1
    require(rejected==6,'Reject invalid or missing data, do not interpolate implicitly')
    return dict(rejected=rejected)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',default='test-results.json');args=parser.parse_args()
    tests=[('source_schema_and_half_energy_pairing',schema_and_pairing),
       ('source_rounding_consistency_flags',audit_inputs),('signed_response_benchmark',bias_sign_and_size),
       ('detected_vs_trapped_fraction',observed_vs_trapped),('conditional_rate_fraction_rank',reconstruction_rank),
       ('synthetic_unused_setting_transfer',unused_setting_transfer),('synthetic_covariance_and_calibration',uncertainty_and_covariance),
       ('practical_weak_identifiability',weak_design),('coefficient_rounding_sensitivity',coefficient_rounding_and_branch),
       ('unresolved_loss_and_backaction_aliases',remaining_aliases),('reaction_residence_time_ODE',reaction_transfer),
       ('bl1_configuration_and_difference_audit',bl1_specific_configuration),
       ('threshold_transfer_counterexample',threshold_transfer_counterexample),('invalid_inputs',invalid_inputs)]
    for name,fn in tests:
        try: CHECKS.append(dict(name=name,status='PASS',detail=fn()))
        except Exception as error: CHECKS.append(dict(name=name,status='FAIL',error=repr(error)))
    report=dict(study='IC-11',utc=datetime.now(timezone.utc).isoformat(),
       code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       table_sha256=hashlib.sha256(DATA.read_bytes()).hexdigest(),
       bl1_table_sha256=hashlib.sha256(BL1_DATA.read_bytes()).hexdigest(),python=platform.python_version(),
       numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,
       scope='Published simulation-response benchmark plus constructed inference tests. Event files inaccessible. No measured-data fit, ARK validation or independent review.',
       input_consistency_status='Four HTML table rows unresolved under nearest-rounding audit; both representations preserved.',
       passed=sum(c['status']=='PASS' for c in CHECKS),total=len(CHECKS),checks=CHECKS)
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['passed']==report['total'] else 1)

if __name__=='__main__': main()
