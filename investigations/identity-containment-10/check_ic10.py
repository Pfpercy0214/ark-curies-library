#!/usr/bin/env python3
"""IC-10: apparatus-aware inference, not an ARK neutron-lifetime prediction.
Synthetic constant-hazard/counting and product-trap comparators; no empirical fit.
Run: python check_ic10.py --output test-results.json
"""
from __future__ import annotations
import argparse, hashlib, json, platform
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import solve_ivp, quad
import sympy as sp

CHECKS=[]
def require(value, message):
    if not bool(value): raise AssertionError(message)
def close(a,b,rtol=1e-9,atol=1e-12):
    require(np.allclose(a,b,rtol=rtol,atol=atol),f'{a} != {b}')
def record(name, fn):
    try: CHECKS.append(dict(name=name,status='PASS',detail=fn()))
    except Exception as exc: CHECKS.append(dict(name=name,status='FAIL',error=repr(exc)))
def probabilities(d,ell,T,eta=(.9,.65,.7),hidden=0.):
    eta=np.asarray(eta,float)
    if min(d,ell,hidden)<0 or T<=0 or eta.shape!=(3,) or np.any(eta<=0) or np.any(eta>1):
        raise ValueError('Require nonnegative rates, positive time, three efficiencies in (0,1]')
    lam=d+ell+hidden
    if lam<=0: raise ValueError('No events: constant two-channel inversion is singular')
    lost=-np.expm1(-lam*T)
    physical=np.array([np.exp(-lam*T),d/lam*lost,ell/lam*lost])
    observed=eta*physical
    return np.r_[observed,1-observed.sum()]
def recover(observed,T,eta=(.9,.65,.7)):
    c=np.asarray(observed,float)/np.asarray(eta,float)
    if c.shape!=(3,) or np.any(c<0) or c[0]<=0 or c[1:].sum()<=0 or T<=0:
        raise ValueError('Positive survivor and removal totals required; no clipping')
    s,b,l=c; total=b+l
    lam=np.log1p(total/s)/T
    return np.array([lam*b/total,lam*l/total])
def expected(N,d,ell,T,eta=(.9,.65,.7),hidden=0.):
    return N*probabilities(d,ell,T,eta,hidden)[:3]
def finite_jac(fn,x):
    x=np.asarray(x,float); out=np.atleast_1d(fn(x)); J=np.empty((len(out),len(x)))
    for k in range(len(x)):
        h=1e-5*max(abs(x[k]),1e-5); hi=x.copy(); lo=x.copy(); hi[k]+=h; lo[k]-=h
        J[:,k]=(fn(hi)-fn(lo))/(2*h)
    return J

def source_partition():
    S,e,z,g0,c=sp.symbols('S e z g0 c',real=True)
    require(sp.expand((g0+c*((S-z)+(e+z)))-(g0+c*(S+e)))==0,'bookkeeping invariance')
    J=sp.Matrix([g0+c*(S+e)]).jacobian([S,e]); require(J.rank()==1,'one total cannot separate partition')
    return dict(result='Same additive influence can be relabeled; epsilon and unresolved baseline are not separately identified',scope='A supplied local response model, not a measured ARK susceptibility')

def survival_degeneracy():
    t=np.linspace(0,1500,101); models=[(.001,.00008),(.00104,.00004)]
    a=np.exp(-sum(models[0])*t); b=np.exp(-sum(models[1])*t); close(a,b)
    d,l=sp.symbols('d l'); require(sp.Matrix([d+l]).jacobian([d,l]).rank()==1,'survival rank')
    return dict(rate_pairs=models,max_survival_difference=float(np.max(abs(a-b))),distinction='More survival precision alone does not separate constant competing hazards')

def detection_drift():
    lam=.0011; delta=.000013; t1,t2=100.,900.; eta=lambda t:.92*np.exp(-delta*t)
    y=lambda t:eta(t)*np.exp(-lam*t)
    naive=np.log(y(t1)/y(t2))/(t2-t1)
    corrected=naive+np.log(eta(t2)/eta(t1))/(t2-t1)
    close(naive,lam+delta); close(corrected,lam)
    # Historical round numbers only: demonstrate effect size, not a fit or present world average.
    dg=1/878-1/888; ratio=np.exp(-dg*1000)
    return dict(actual_total_rate=lam,naive_rate=naive,corrected_rate=corrected,
                illustrative_878_888_rate_difference=dg,efficiency_ratio_over_1000_s=ratio,
                caveat='Not evidence that any actual experiment has this efficiency error')

def exact_channel_inverse():
    N=2e5; T=700.; eta=(.9,.65,.7); d,ell=.001,.00008
    c=expected(N,d,ell,T,eta); r=recover(c,T,eta); close(r,[d,ell])
    close(recover(c*3.7,T,eta),r)
    close(recover(c,T,np.array(eta)*.8),r) # only common efficiency scale cancels
    S,B,L=c/np.array(eta); close(S+B+L,N)
    return dict(mean_counts=c.tolist(),recovered_rates=r.tolist(),reconstructed_initial=N,
                common_scale_cancels=True,relative_efficiencies_required=True,
                assumptions='Constant hazards, exhaustive disjoint channels, no influx, matched exposures and response calibrations')

def rank_and_unknown_efficiency():
    # Parametrize by logs so the singular-value test uses comparable relative scales.
    T=700.; N=2e5; d=.001; ell=.00008; eta=np.array([.9,.65,.7])
    fn=lambda x: np.log(expected(*np.exp(x),T,eta))
    J=finite_jac(fn,np.log([N,d,ell])); sv=np.linalg.svd(J,compute_uv=False)
    require(np.min(sv)>.01,'three-channel local rank')
    c=expected(N,d,ell,T,eta)
    wrong=recover(c,T,[.9,.5,.7]); require(abs(wrong[0]-d)>1e-4,'unknown relative efficiency')
    return dict(log_jacobian_singular_values=sv.tolist(),rate_inferred_with_wrong_beta_efficiency=wrong.tolist())

def channel_ode():
    N=2e5; d=.001; ell=.00008; T=700.
    def rhs(t,y): return [-(d+ell)*y[0],d*y[0],ell*y[0]]
    errors=[]
    p=probabilities(d,ell,T,(1,1,1))[:3]*N
    for tol in [1e-5,1e-7,1e-9]:
        sol=solve_ivp(rhs,(0,T),[N,0,0],rtol=tol,atol=tol*.01)
        errors.append(float(np.max(abs(sol.y[:,-1]-p))/N))
        close(sol.y[:,-1].sum(),N,rtol=1e-13)
    require(errors[-1]<errors[0]/1000 and errors[-1]<1e-9,'ODE refinement')
    return dict(relative_errors=errors,endpoint=p.tolist())

def multinomial_uncertainty():
    rng=np.random.default_rng(1001); N=200000; T=700.; eta=np.array([.9,.65,.7])
    rates=np.array([.001,.00008]); p=probabilities(*rates,T,eta); mu=N*p[:3]
    draws=rng.multinomial(N,p,size=30000)[:,:3]
    corrected=draws/eta; total=corrected[:,1:].sum(axis=1)
    lam=np.log1p(total/corrected[:,0])/T
    estimates=np.column_stack([lam*corrected[:,1]/total,lam*corrected[:,2]/total])
    C=N*(np.diag(p[:3])-np.outer(p[:3],p[:3])); J=finite_jac(lambda x:recover(x,T,eta),mu)
    theory=J@C@J.T; actual=np.cov(estimates,rowvar=False)
    close(np.diag(actual),np.diag(theory),rtol=.04,atol=0)
    err=estimates-rates; coverage=np.mean(np.abs(err)<=1.96*np.sqrt(np.diag(theory)),axis=0)
    require(np.all((coverage>.94)&(coverage<.96)),'approximate normal coverage')
    # Common efficiency-scale uncertainty cancels to first order, unlike a channel-specific shift.
    Jeta=finite_jac(lambda e:recover(mu,T,e),eta)
    require(np.max(abs(Jeta@eta))<1e-11,'common scale cancellation')
    rel=.003; channel_variance=Jeta[:,1]**2*(rel*eta[1])**2
    return dict(seed=1001,replicates=len(draws),mean_bias=(estimates.mean(axis=0)-rates).tolist(),
                count_only_sd=np.sqrt(np.diag(theory)).tolist(),MC_sd=np.sqrt(np.diag(actual)).tolist(),
                covariance_offdiagonal=float(theory[0,1]),coverage_95=coverage.tolist(),
                extra_sd_for_0p3pct_beta_efficiency=np.sqrt(channel_variance).tolist(),
                caveat='Synthetic multinomial events; no empirical confidence interval')

def hidden_channel():
    N=2e5; d=.001; ell=.00008; h=.00005; T=700.; eta=np.array([.9,.65,.7])
    c=expected(N,d,ell,T,eta,hidden=h); r=recover(c,T,eta); Nalt=np.sum(c/eta)
    close(expected(Nalt,*r,T,eta),c,rtol=1e-10)
    require(N-Nalt>1000 and abs(r[0]-d)>1e-5,'hidden channel matters')
    return dict(true_rates=[d,ell,h],two_channel_apparent_rates=r.tolist(),
                independent_initial_inventory_deficit=N-Nalt,
                alternate_initial_inventory=Nalt,
                result='Without independent initial inventory or a third mark, identical observed totals admit a wrong two-channel model')

def heterogeneous_population():
    w=np.array([.5,.5]); rates=np.array([.00102,.0012]); T=np.array([100.,600.,1200.])
    S=np.exp(-T[:,None]*rates)@w; eff=-np.diff(np.log(S))/np.diff(T)
    require(eff[1]<eff[0],'selection changes effective hazard')
    t=500.; weights=w*np.exp(-rates*t); weights/=weights.sum()
    H=weights@rates; derivative=-(weights@(rates-H)**2)
    dt=.01
    hazard=lambda tt:(w*np.exp(-rates*tt))@rates/((w*np.exp(-rates*tt)).sum())
    close((hazard(t+dt)-hazard(t-dt))/(2*dt),derivative,rtol=1e-6,atol=1e-14)
    return dict(interval_rates=eff.tolist(),instantaneous_derivative=derivative,
                result='Time dependence of aggregate removal can arise from selection with each component rate fixed')

def transfer():
    N=2e5; T=700.; eta=np.array([.9,.65,.7]); rate=lambda x:.001+.00002*x
    loss=lambda x:.00003+.00004*x
    xs=np.array([0.,.5]); recovered=np.array([recover(expected(N,rate(x),loss(x),T,eta),T,eta) for x in xs])
    coeff=np.linalg.solve(np.column_stack([np.ones(2),xs]),recovered[:,0]); xeval=1.2
    pred=coeff@[1,xeval]; close(pred,rate(xeval))
    # A change only in detector acceptance is corrected without creating a physical rate shift.
    eta2=np.array([.9,.85,.7]); c2=expected(N,rate(xeval),loss(xeval),T,eta2)
    recovered_eval=recover(c2,T,eta2); close(pred,recovered_eval[0])
    corrupted=recover(c2,T,eta); require(abs(corrupted[0]-pred)>1e-4,'unmodeled detector response')
    # Known loss at x_eval is permitted input to a distinct product-count prediction, not fitted to beta counts.
    expected_beta=expected(N,pred,loss(xeval),T,eta2)[1]
    close(expected_beta,c2[1])
    return dict(calibration_controls=xs.tolist(),frozen_coefficients=coeff.tolist(),evaluation_control=xeval,
                evaluation_rate=pred,unmodeled_detection_rate=corrupted[0],predicted_beta_counts=expected_beta,
                scope='Constructed affine response; not a derived epsilon coupling, blind holdout, or actual data prediction')

def pressure_extrapolation():
    p=np.array([0.,1.,2.]); gamma0=.001; loss0=.00003; chi=.00002; loss_slope=.00004
    total=gamma0+loss0+(chi+loss_slope)*p
    fit=np.polyfit(p,total,1); close(fit,[chi+loss_slope,gamma0+loss0])
    alt=gamma0+loss0+(.00001+.00005)*p; close(total,alt)
    return dict(naive_extrapolated_intercept=fit[1],true_reference_beta_rate=gamma0,
                fitted_total_slope=fit[0],result='Zero-pressure intercept can retain pressure-independent loss; scan alone does not separate beta and loss slopes')

def response_scale():
    x=np.array([0,.5,1.2]); alpha=2.; chi=1e-5; gamma0=.001
    a=gamma0+chi*(alpha*x); b=gamma0+(chi/7)*(7*alpha*x); close(a,b)
    return dict(observed_slope=alpha*chi,result='Apparatus-to-epsilon normalization and rate susceptibility remain separately unidentified from rate response alone')

def birth_average(x):
    x=float(x)
    if x<0: raise ValueError('Nonnegative charge-exchange rate-time product required')
    if x<1e-6: return 1-x/2+x*x/6-x*x*x/24
    return -np.expm1(-x)/x

def product_trap():
    R=5.; r=20.; ep=.9; eh=.55; Ts=[.002,.01,.05]; rows=[]
    for T in Ts:
        a=birth_average(r*T); eff=eh+(ep-eh)*a; signal=R*T*eff
        sol=solve_ivp(lambda t,y:[R-r*y[0],r*y[0]],(0,T),[0.,0.],rtol=1e-11,atol=1e-13)
        P,M=sol.y[:,-1]; close(ep*P+eh*M,signal,rtol=1e-9); close(P+M,R*T)
        avg=quad(lambda age:np.exp(-r*age),0,T,epsabs=1e-13)[0]/T; close(avg,a)
        rows.append(dict(storage_s=T,average_unconverted_fraction=a,effective_efficiency=eff,
                         apparent_lifetime_ratio=ep/eff,expected_signal=signal))
    require(rows[-1]['apparent_lifetime_ratio']>rows[0]['apparent_lifetime_ratio'],'dwell trend')
    close(birth_average(0),1.); close(birth_average(1e-12),1-5e-13)
    close(ep+(ep-ep)*birth_average(.2),ep)
    return dict(input_status='Illustrative collision rate and efficiencies, not NIST values',rows=rows,
                result='Post-decay charge exchange can change recorded yield with constant beta production; equal ion and proton efficiencies cancel the yield shift')

def causal_time_order():
    # Simple factorization: produced decays = rate*neutron exposure; later response changes count only.
    beta=.001; exposure=5e6; eta=np.array([.5,.8,.9]); counts=beta*exposure*eta
    close(counts/(exposure*eta),np.full(3,beta))
    require(np.ptp(counts/(exposure*.8))>4e-4,'later acceptance masquerades as rate')
    return dict(corrected_beta_rates=(counts/(exposure*eta)).tolist(),
                requirement='A downstream-only intervention must be independently shown not to alter upstream fields, exposure, or acceptance elsewhere')

def invalid_inputs():
    rejected=0
    for args in [(-1.,.1,1),(.1,.1,0),(.1,.1,1,(.9,0,.8))]:
        try: probabilities(*args)
        except ValueError: rejected+=1
    try: recover([0,1,1],1)
    except ValueError: rejected+=1
    try: birth_average(-1)
    except ValueError: rejected+=1
    require(rejected==5,'reject invalid inputs')
    return dict(rejected=rejected,limitations='Background estimates must be modeled jointly at low counts; no silent clipping or treating negative corrected counts as physical')

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',default='test-results.json'); args=p.parse_args()
    for name,fn in [('environment_partition',source_partition),('survival_nonidentifiability',survival_degeneracy),
      ('detection_drift_scale',detection_drift),('exhaustive_channel_inversion',exact_channel_inverse),
      ('rank_and_relative_efficiency',rank_and_unknown_efficiency),('independent_ODE_and_refinement',channel_ode),
      ('multinomial_covariance_and_calibration',multinomial_uncertainty),('unmonitored_channel_counterexample',hidden_channel),
      ('population_selection_counterexample',heterogeneous_population),('frozen_calibrated_transfer',transfer),
      ('pressure_extrapolation_limits',pressure_extrapolation),('epsilon_susceptibility_scale',response_scale),
      ('product_trap_response',product_trap),('causal_order_control',causal_time_order),('invalid_inputs',invalid_inputs)]: record(name,fn)
    report=dict(study='IC-10',utc=datetime.now(timezone.utc).isoformat(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,
                scope='Symbolic and synthetic-data verification only; no actual lifetime fit, apparatus calibration, epsilon identification or independent review',
                passed=sum(x['status']=='PASS' for x in CHECKS),total=len(CHECKS),checks=CHECKS)
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8'); print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['passed']==len(CHECKS) else 1)
if __name__=='__main__': main()
