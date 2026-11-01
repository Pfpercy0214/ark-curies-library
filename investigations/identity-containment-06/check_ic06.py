#!/usr/bin/env python3
"""IC-06 conditional derivation checks. No empirical data or ARK parameter fit.
Run: python check_ic06.py --output test-results.json
Requires Python 3.11+, NumPy, SciPy, SymPy. Assertions remain enabled via explicit checks.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
import sympy as sp

CHECKS: list[dict] = []

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def zero(expr: sp.Expr) -> None:
    require(sp.simplify(sp.expand_trig(expr)) == 0, str(expr))

def check(name):
    def decorate(fn):
        try:
            detail = fn()
            CHECKS.append({'name': name, 'status': 'PASS', 'detail': detail or {}})
        except Exception as exc:
            CHECKS.append({'name': name, 'status': 'FAIL', 'error': repr(exc)})
    return decorate

q, z = sp.symbols('q z', real=True)
v, K, a, chi = sp.symbols('v K a chi', positive=True)
x = sp.symbols('x', real=True)
ell = sp.sqrt(2*K/(a*v**2))
wall = v*sp.tanh(x/ell)
V = a*(q*q-v*v)**2/4
p = {'K': 2.0, 'a': 3.0, 'v': 0.4, 'chi': 5.0}
ell_n = math.sqrt(2*p['K']/(p['a']*p['v']**2))
sigma_n = 2*math.sqrt(2*p['K']*p['a'])*p['v']**3/3
speed_n = math.sqrt(p['K']/p['chi'])
gap_n = math.sqrt(2*p['a']*p['v']**2/p['chi'])

@check('01_fixed_coefficient_first_variation')
def _():
    Q = sp.Function('Q')(x); KK = sp.Function('K')(x); J = sp.Function('J')(x)
    f = KK*sp.diff(Q,x)**2/2 + a*(Q**2-v**2)**2/4 - J*Q
    el = sp.diff(f,Q)-sp.diff(sp.diff(f,sp.diff(Q,x)),x)
    zero(el-(-sp.diff(KK*sp.diff(Q,x),x)+a*Q*(Q**2-v**2)-J))
    zero(sp.diff(f,sp.diff(Q,x))-KK*sp.diff(Q,x))
    return {'boundary_conjugate': 'K times outward normal derivative, not pressure'}

@check('02_state_dependent_gradient_coefficient_extra_term')
def _():
    Q = sp.Function('Q')(x); k0,k1 = sp.symbols('k0 k1', positive=True)
    KK=k0+k1*Q**2; f=KK*sp.diff(Q,x)**2/2+Q**2/2
    el=sp.diff(f,Q)-sp.diff(sp.diff(f,sp.diff(Q,x)),x)
    naive=-sp.diff(KK*sp.diff(Q,x),x)+Q
    zero(el-naive-k1*Q*sp.diff(Q,x)**2)
    require(sp.simplify(el-naive)!=0,'Missing term was not detected')
    return {'negative_control': 'omitting partial_K/partial_q * |grad q|^2 / 2 fails'}

@check('03_first_variation_numeric_energy_difference')
def _():
    aa,vv,J=3.0,.4,.03
    def profile(t,e):
        return .2+.1*math.sin(math.pi*t)+e*math.sin(math.pi*t)
    def slope(t,e):
        return .1*math.pi*math.cos(math.pi*t)+e*math.pi*math.cos(math.pi*t)
    def energy(e):
        return quad(lambda t:(2+t)*slope(t,e)**2/2+aa*(profile(t,e)**2-vv**2)**2/4-J*profile(t,e),0,1,epsabs=1e-12)[0]
    def integrand(t):
        qq=profile(t,0); qp=slope(t,0); qpp=-.1*math.pi**2*math.sin(math.pi*t)
        return (-(2+t)*qpp-qp+aa*qq*(qq**2-vv**2)-J)*math.sin(math.pi*t)
    predicted=quad(integrand,0,1,epsabs=1e-12)[0]
    errors=[abs((energy(e)-energy(-e))/(2*e)-predicted) for e in [.02,.01,.005]]
    require(errors[-1]<errors[0]/10,'Variation check did not converge')
    return {'epsilon':[.02,.01,.005],'absolute_errors':errors}

@check('04_single_minimum_nonlinear_counterexample')
def _():
    r=sp.symbols('r', real=True); U=r**2/2+r**4/4
    zero(sp.diff(U,r)-r*(1+r*r))
    zero(sp.diff(U,r,2)-(1+3*r*r))
    require(sp.diff(U,r,2).is_positive is True,'Not strictly convex')
    return {'counterexample':'U=q^2/2+q^4/4 is nonlinear, strictly convex, one minimum'}

@check('05_double_well_kink_satisfies_equilibrium')
def _():
    zero(-K*sp.diff(wall,x,2)+a*wall*(wall**2-v**2))
    zero(K*sp.diff(wall,x)**2/2-V.subs(q,wall))
    return {'boundary_conditions':'q(-infinity)=-v, q(+infinity)=v; zero drive'}

@check('06_interface_energy_symbolic_and_quadrature')
def _():
    r=sp.symbols('r', real=True)
    exact=sp.integrate(sp.sqrt(K*a/2)*(v**2-r**2),(r,-v,v))
    zero(exact-2*sp.sqrt(2*K*a)*v**3/3)
    def energy_density(t):
        qq=p['v']*math.tanh(t/ell_n)
        qp=p['v']/ell_n/math.cosh(t/ell_n)**2
        return p['K']*qp*qp/2+p['a']*(qq*qq-p['v']**2)**2/4
    numeric=quad(energy_density,-12*ell_n,12*ell_n,epsabs=1e-12)[0]
    require(abs(numeric-sigma_n)<1e-10,'Interface energy mismatch')
    return {'analytic':sigma_n,'quadrature':numeric,'absolute_error':abs(numeric-sigma_n)}

@check('07_kink_linear_stability_factorization')
def _():
    y=sp.symbols('y',real=True); f=sp.Function('f')(y)
    A=sp.diff(f,y)+2*sp.tanh(y)*f
    AdA=-sp.diff(A,y)+2*sp.tanh(y)*A
    zero(AdA-(-sp.diff(f,y,2)+(4-6/sp.cosh(y)**2)*f))
    h=1/sp.cosh(y)**2
    zero(sp.diff(h,y)+2*sp.tanh(y)*h)
    return {'scope':'nonnegative planar second variation; translation zero mode; no closed-bubble stability claim'}

@check('08_kink_finite_difference_residual_refinement')
def _():
    errors=[]
    for n in [129,257,513]:
        xx=np.linspace(-8*ell_n,8*ell_n,n); dx=xx[1]-xx[0]
        qq=p['v']*np.tanh(xx/ell_n)
        d2=(qq[2:]-2*qq[1:-1]+qq[:-2])/dx**2
        residual=-p['K']*d2+p['a']*qq[1:-1]*(qq[1:-1]**2-p['v']**2)
        errors.append(float(np.max(np.abs(residual))))
    require(errors[0]/errors[1]>3.5 and errors[1]/errors[2]>3.5,'Not second-order refinement')
    return {'grid_sizes':[129,257,513],'max_residuals':errors}

@check('09_wave_dispersion_and_width_rate_relation')
def _():
    k,Om=sp.symbols('k Om',real=True)
    B=sp.diff(V,q,2).subs(q,v)
    zero(B-2*a*v*v)
    dispersion=(K*k*k+B)/chi
    zero(chi*dispersion-K*k*k-B)
    zero(sp.sqrt(B/chi)*ell-2*sp.sqrt(K/chi))
    return {'ell':ell_n,'propagation_characteristic':speed_n,'zero_wavenumber_angular_rate':gap_n,'Omega0_ell_over_2u':gap_n*ell_n/(2*speed_n)}

@check('10_same_static_boundary_different_inertia_rates')
def _():
    old=math.sqrt(2*p['a']*p['v']**2/p['chi'])
    new=math.sqrt(2*p['a']*p['v']**2/(4*p['chi']))
    require(math.isclose(new/old,.5),'Inertia scaling failed')
    return {'chi_multiplier':4,'rate_and_characteristic_speed_multiplier':new/old,'unchanged':'equilibrium wall, width, interface energy'}

@check('11_periodic_mode_spatial_refinement')
def _():
    k=3.0; B=2*p['a']*p['v']**2
    continuum=math.sqrt((p['K']*k*k+B)/p['chi']); errors=[]
    for n in [32,64,128,256]:
        dx=2*math.pi/n
        ev=4*math.sin(k*dx/2)**2/dx**2
        errors.append(abs(math.sqrt((p['K']*ev+B)/p['chi'])-continuum))
    require(all(errors[i]/errors[i+1]>3.8 for i in range(3)),'Dispersion convergence failed')
    return {'grid_sizes':[32,64,128,256],'angular_rate_errors':errors}

@check('12_mode_time_integration_vs_closed_solution')
def _():
    Om=math.sqrt((p['K']*.7**2+2*p['a']*p['v']**2)/p['chi'])
    times=np.linspace(0,40,401)
    sol=solve_ivp(lambda t,y:[y[1],-Om*Om*y[0]],(0,40),[1.,0.],t_eval=times,rtol=1e-11,atol=1e-13)
    require(sol.success,sol.message)
    error=float(np.max(np.abs(sol.y[0]-np.cos(Om*times))))
    require(error<1e-8,'Independent ODE integration mismatch')
    return {'max_amplitude_error':error,'data':'manufactured, not physical observations'}

@check('13_damping_energy_and_overdamped_limit')
def _():
    s,gam,b=sp.symbols('s gam b',positive=True)
    slow=(-gam+sp.sqrt(gam**2-4*chi*b))/(2*chi)
    zero(sp.limit(slow,chi,0,dir='+')+b/gam)
    return {'slow_mode_limit':'-(K k^2+B)/gamma','diffusion_coefficient':'K/gamma','caution':'diffusion approximation is not a finite-front-speed proof'}

@check('14_environmental_tilt_stationary_branches')
def _():
    jc=2*p['a']*p['v']**3/(3*math.sqrt(3)); counts=[]; gaps=[]
    for factor in [.5,2.]:
        J=factor*jc
        roots=np.roots([1.,0.,-p['v']**2,-J/p['a']])
        rr=sorted(float(r.real) for r in roots if abs(r.imag)<1e-9)
        minima=[r for r in rr if p['a']*(3*r*r-p['v']**2)>0]
        counts.append({'factor':factor,'real_stationary_points':len(rr),'local_minima':len(minima)})
        if len(minima)==2:
            energies=[p['a']*(r*r-p['v']**2)**2/4-J*r for r in minima]
            gaps.append(abs(energies[0]-energies[1]))
    require(counts[0]['local_minima']==2 and counts[1]['local_minima']==1,'Tilt threshold mismatch')
    require(gaps[0]>0,'Tilted wells incorrectly treated as equal-energy coexistence')
    return {'critical_drive':jc,'branches':counts,'unequal_well_energy_gap':gaps[0]}

@check('15_closed_bubble_fixed_pressure_negative_control')
def _():
    R,sig,dp=sp.symbols('R sig dp',positive=True)
    E=4*sp.pi*sig*R**2-4*sp.pi*dp*R**3/3
    rc=2*sig/dp
    zero(sp.diff(E,R).subs(R,rc))
    zero(sp.diff(E,R,2).subs(R,rc)+8*sp.pi*sig)
    return {'critical_radius':'2 sigma / delta_p','second_derivative':'-8 pi sigma < 0','scope':'thin wall, fixed surface tension and reservoir pressure; not a no-go for all identities'}

@check('16_memory_relaxed_and_frozen_hessians')
def _():
    h,b=sp.symbols('h b',positive=True)
    U=V+h*(z-b*q)**2/2
    qq=sp.diff(U,q,2).subs(q,v); qz=sp.diff(U,q,z); zz=sp.diff(U,z,2)
    zero(qq-(2*a*v*v+h*b*b))
    zero(qq-qz*qz/zz-2*a*v*v)
    require(sp.simplify(qq-(qq-qz*qz/zz)).is_positive is True,'Relaxation did not soften')
    return {'static_minimizer':'z=b q leaves the same wall','frozen_curvature':'2 a v^2+h b^2','relaxed_curvature':'2 a v^2'}

@check('17_memory_and_drive_energy_budget')
def _():
    qt,qx,qxt,qxx,qqtt,zt=sp.symbols('qt qx qxt qxx qqtt zt',real=True)
    Uq,Uz,J,gam,M=sp.symbols('Uq Uz J gam M',real=True)
    edot=chi*qt*qqtt+K*qx*qxt+Uq*qt+Uz*zt
    actual=edot.subs({qqtt:(K*qxx-Uq+J-gam*qt)/chi,zt:-M*Uz})
    fluxdiv=K*(qt*qxx+qx*qxt)
    zero(actual-fluxdiv-J*qt+gam*qt**2+M*Uz**2)
    return {'budget':'dE0/dt=boundary power+integral(J q_t-gamma q_t^2-M U_z^2)','requirements':'constant K, chi; frozen material parameters; gamma,M nonnegative'}

@check('18_memory_loss_frequency_response')
def _():
    w,tr,h,b=sp.symbols('w tr h b',positive=True)
    extra=h*b*b*(1-1/(1-sp.I*w*tr))
    zero(sp.re(extra)-h*b*b*(w*tr)**2/(1+(w*tr)**2))
    zero(sp.im(extra)+h*b*b*w*tr/(1+(w*tr)**2))
    zero(sp.limit(extra,w,0))
    zero(sp.limit(extra,w,sp.oo)-h*b*b)
    return {'time_convention':'exp(-i Omega t)','outcome':'low/high frequency limits differ; imaginary part is dissipative with this convention'}

@check('19_memory_energy_numerical_budget')
def _():
    B0=.96; h=.7; b=.6; M=.8; gam=.12; inertia=5.
    def rhs(t,y):
        qq,vel,zz,loss=y; Uz=h*(zz-b*qq)
        Uq=B0*qq-b*Uz
        return [vel,(-Uq-gam*vel)/inertia,-M*Uz,gam*vel*vel+M*Uz*Uz]
    times=np.linspace(0,60,601)
    sol=solve_ivp(rhs,(0,60),[.2,.05,-.1,0],t_eval=times,rtol=1e-11,atol=1e-13)
    require(sol.success,sol.message)
    qq,vel,zz,loss=sol.y
    E=inertia*vel**2/2+B0*qq**2/2+h*(zz-b*qq)**2/2
    err=float(np.max(np.abs(E+loss-E[0])))
    require(err<1e-9 and loss[-1]>0,'Energy budget failed')
    return {'max_budget_error':err,'total_dissipation':float(loss[-1])}

@check('20_one_mode_is_not_universal_clock_scaling')
def _():
    base=np.sqrt(np.array([.96,2.])/np.array([5.,3.]))
    common=np.sqrt(np.array([.96,2.])/(4*np.array([5.,3.])))
    differential=np.sqrt(np.array([.96,4.])/(4*np.array([5.,3.])))
    require(np.allclose(common/base,.5),'Common scaling control failed')
    ratios=differential/base
    require(not np.allclose(ratios,ratios[0]),'Species-dependent effect passed universality')
    return {'common_factor_control':(common/base).tolist(),'differential_counterexample':ratios.tolist(),'scope':'manufactured two-mode example, not atomic clocks'}


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path(__file__).with_name('test-results.json'))
    args=parser.parse_args()
    result={'study':'IC-06','status':'PASS' if all(c['status']=='PASS' for c in CHECKS) else 'FAIL',
            'executed_utc':datetime.now(timezone.utc).isoformat(),'python':sys.version,
            'versions':{'sympy':sp.__version__,'numpy':np.__version__,'scipy':scipy.__version__},
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'checks_passed':sum(c['status']=='PASS' for c in CHECKS),'checks_total':len(CHECKS),
            'scope':'Conditional symbolic and manufactured-data verification. No empirical fit; no independent second reviewer; tests designed with derivation visible.',
            'checks':CHECKS}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'status':result['status'],'passed':result['checks_passed'],'total':len(CHECKS),'output':str(args.output)},indent=2))
    for row in CHECKS:
        if row['status']=='FAIL': print(row)
    return 0 if result['status']=='PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
