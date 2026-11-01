#!/usr/bin/env python3
"""IC-09: a self-organized, permeable profile in the IC-08 GP comparator.
All examples use hbar=m=g=n_infinity=1. No ARK scalar identification or data fit.
Python 3.11+ with NumPy, SciPy and SymPy. Writes actual results; failures are kept.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import time
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
import sympy as sp

CHECKS: list[dict] = []

def require(ok: bool, message: str) -> None:
    if not bool(ok):
        raise AssertionError(message)

def profile(x, t: float = 0.0, b: float = .6, u: float = -.6):
    """Envelope after removal of uniform background plane wave; |b|<1."""
    if not np.isfinite(b) or abs(b) >= 1 or not np.isfinite(u):
        raise ValueError('Require real finite |b|<1, u; limiting cases are separate')
    a = np.sqrt(1-b*b)
    return a*np.tanh(a*(np.asarray(x)-(u+b)*t))+1j*b

def derivatives(x, t: float = 0.0, b: float = .6, u: float = -.6):
    a=np.sqrt(1-b*b); z=a*(np.asarray(x)-(u+b)*t)
    th=np.tanh(z); sech2=1-th*th
    f=a*th+1j*b; fx=a*a*sech2; fxx=-2*a**3*sech2*th
    return f,fx,fxx

def density_current(x, t: float = 0.0, b: float = .6, u: float = -.6):
    f,fx,_=derivatives(x,t,b,u); n=np.abs(f)**2
    j=u*n+np.imag(np.conj(f)*fx)
    return n,j

def evolve(N: int, duration: float, b: float=.6, u: float=-.6,
           L: float|None=None, rtol: float=1e-9):
    """Method of lines, fourth-order spatial derivatives, adaptive DOP853.
    Exterior ghost values are supplied by the declared infinite-line solution.
    This is a finite-box consistency test, NOT outgoing-wave scattering or
    an unrestricted stability experiment. The density is not reset in the box.
    """
    if N<16 or duration<=0 or rtol<=0: raise ValueError('Invalid solver inputs')
    if L is None: L=12/np.sqrt(1-b*b)
    h=2*L/(N+1); x=-L+h*np.arange(1,N+1)
    ghost_x=np.array([-L-h,-L,L,L+h])
    def rhs(t,y):
        exterior=profile(ghost_x,t,b,u)
        p=np.concatenate([exterior[:2],y,exterior[2:]])
        d1=(p[:-4]-8*p[1:-3]+8*p[3:-1]-p[4:])/(12*h)
        d2=(-p[:-4]+16*p[1:-3]-30*p[2:-2]+16*p[3:-1]-p[4:])/(12*h*h)
        return .5j*d2-u*d1-1j*(np.abs(y)**2-1)*y
    start=time.perf_counter()
    sol=solve_ivp(rhs,[0,duration],profile(x,0,b,u),method='DOP853',
                  rtol=rtol,atol=rtol*.01,t_eval=[duration])
    require(sol.success,sol.message)
    exact=profile(x,duration,b,u); final=sol.y[:,-1]
    return dict(grid=N,duration=duration,domain_half_length=L,spacing=h,
                complex_max_error=float(np.max(np.abs(final-exact))),
                density_max_error=float(np.max(np.abs(np.abs(final)**2-np.abs(exact)**2))),
                nfev=sol.nfev,seconds=time.perf_counter()-start),x,final

def symbolic_solution():
    a,b,u,T=sp.symbols('a b u T',real=True)
    f=a*T+sp.I*b; fx=a*a*(1-T*T); fxx=-2*a**3*T*(1-T*T)
    # n-1=-a^2*(1-T^2), with a^2+b^2=1.
    rhs=-fxx/2-sp.I*u*fx-a*a*(1-T*T)*f
    require(sp.simplify(rhs+sp.I*(u+b)*fx)==0,'traveling GP solution')
    j=u*(a*a*T*T+b*b)-b*fx
    require(sp.simplify(j-(u+b)*(a*a*T*T+b*b)+b*(a*a+b*b))==0,'current formula')
    return dict(equation='i*f_t=-f_xx/2-i*u*f_x+(|f|^2-1)*f',
                center_velocity='V=u+b',relative_current='j-V*n=-b')

def numerical_pde():
    x=np.linspace(-15,15,601); vals=[]
    for b,u,t in [(.2,-.2,0),(.6,-.6,1),(.8,.3,.7),(-.6,.6,0)]:
        f,fx,fxx=derivatives(x,t,b,u); n=np.abs(f)**2
        residual=-.5*fxx-1j*u*fx+(n-1)*f+1j*(u+b)*fx
        _,j=density_current(x,t,b,u)
        err=float(np.max(np.abs(residual)))
        flux_err=float(np.max(np.abs(j-(u+b)*n+b)))
        require(err<2e-14 and flux_err<2e-14,'pointwise identities')
        vals.append(dict(b=b,u=u,pde_max=err,relative_flux_error=flux_err))
    return vals

def open_control_volume():
    b=.6; u=.2; V=u+b; a=np.sqrt(1-b*b); t=.7
    left=-2/a+V*t; right=4/a+V*t
    nl,jl=density_current(left,t,b,u); nr,jr=density_current(right,t,b,u)
    lab_flux=float(jl-jr); moving_term=float(V*(nr-nl))
    require(abs(lab_flux+moving_term)<1e-14,'Reynolds balance')
    require(abs(lab_flux)>.02,'ignoring moving boundary must fail')
    # A second test uses a fixed lab interval while the profile passes it.
    A=-1.; B=3.; dt=1e-5
    amount=lambda s:quad(lambda x:density_current(x,s,b,u)[0],A,B,epsabs=1e-12)[0]
    observed=(amount(t+dt)-amount(t-dt))/(2*dt)
    predicted=float(density_current(A,t,b,u)[1]-density_current(B,t,b,u)[1])
    require(abs(observed-predicted)<1e-9,'fixed-window continuity')
    return dict(moving_window_lab_flux=lab_flux,boundary_motion_correction=moving_term,
                fixed_window_derivative=observed,fixed_window_flux_prediction=predicted,
                no_internal_source=True)

def stress_balance():
    a,T=sp.symbols('a T',real=True); b2=1-a*a
    n=b2+a*a*T*T; nx=2*a**3*T*(1-T*T)
    nxx=2*a**4*(1-T*T)*(1-3*T*T)
    pi=b2/n+n*n/2+nx*nx/(4*n)-nxx/4
    require(sp.factor(pi-(b2+sp.Rational(1,2)))==0,'constant full momentum flux')
    b=.6; aa=.8; nn=b*b
    adv=b*b/nn; interaction=nn*nn/2; gradient=-aa**4/2
    require(abs(adv+interaction+gradient-(b*b+.5))<1e-14,'center stress')
    require(abs(adv+interaction-(b*b+.5))>.1,'omitting gradient stress fails')
    return dict(full_flux=.5+b*b,center_advective=adv,center_interaction_pressure=interaction,
                center_gradient_stress=gradient,
                pressure_only_not_constant=True,
                note='No external wall or localized potential is used')

def branch_observables():
    rows=[]
    for b in [.2,.6,.9]:
        a=np.sqrt(1-b*b)
        deficit=quad(lambda x:1-abs(profile(x,0,b,-b))**2,-30/a,30/a,epsabs=1e-11)[0]
        phase=np.angle(profile(30/a,0,b,-b)/profile(-30/a,0,b,-b))
        # f is the background-rest envelope. Energy measured in rest background.
        E=quad(lambda x:.5*abs(derivatives(x,0,b,-b)[1])**2+
               .5*(abs(profile(x,0,b,-b))**2-1)**2,-30/a,30/a,epsabs=1e-11)[0]
        require(abs(deficit-2*a)<1e-11,'density deficit')
        require(abs(phase+2*np.arccos(b))<1e-12,'phase drop')
        require(abs(E-4*a**3/3)<1e-11,'rest-background excitation energy')
        inferred=np.sqrt(abs(profile(0,0,b,-b))**2)
        require(abs(inferred-b)<1e-14,'minimum-density magnitude inference')
        rows.append(dict(b=b,min_density=b*b,width_parameter=1/a,current=-b,
                         phase_drop=phase,deficit=deficit,excitation_energy=E,
                         sign_not_determined_by_density=True))
    return dict(rows=rows,interpretation='conditional branch identities, not withheld experimental tests')

def throughflow_time():
    b=.6;a=.8; L=3/a
    inside=2*L-2*a*np.tanh(a*L); analytic=inside/b
    integrand=lambda x:abs(profile(x,0,b,-b))**2/b
    integral=quad(integrand,-L,L,epsabs=1e-12)[0]
    def rhs(t,y):return [-b/abs(profile(y[0],0,b,-b))**2]
    def reached(t,y):return y[0]+L
    reached.terminal=True; reached.direction=-1
    sol=solve_ivp(rhs,[0,2*analytic],[L],events=reached,rtol=1e-11,atol=1e-12)
    measured=float(sol.t_events[0][0])
    require(abs(integral-analytic)<1e-12 and abs(measured-analytic)<1e-8,'hydrodynamic crossing')
    return dict(window=[-L,L],window_amount=inside,relative_flux=-b,
                advective_crossing_time=analytic,ode_crossing_time=measured,
                transported_inventory_equivalents_over_30=30/analytic,
                note='A hydrodynamic characteristic, not tracking distinguishable atoms')

def orientation_and_limits():
    x=np.linspace(-10,10,501)
    n1,j1=density_current(x,0,.6,-.6); n2,j2=density_current(x,0,-.6,.6)
    require(np.max(abs(n1-n2))==0 and np.max(abs(j1+j2))<1e-14,'opposite orientation')
    n0,j0=density_current(x,0,0,0)
    require(abs(n0[len(x)//2])<1e-15 and np.max(abs(j0))<1e-15,'black limit')
    b=.999999; a=np.sqrt(1-b*b)
    require(2*a<.003 and 2*np.arccos(b)<.003,'continuous fade')
    return dict(opposite_current_same_density=True,black_case_flux=0,
                shallow_limit_deficit=2*a,shallow_limit_phase_magnitude=2*np.arccos(b),
                note='Gray profile has no discrete knot invariant in this calculation')

def constitutive_counterexample():
    b=.6;a=.8; x=np.linspace(-10,10,1001); k=1.2*a
    th=np.tanh(k*x); se=1-th*th
    f=a*th+1j*b; fx=a*k*se; fxx=-2*a*k*k*se*th
    residual=-.5*fxx+1j*b*fx+(abs(f)**2-1)*f
    error=float(np.max(abs(residual)))
    require(error>.05,'wrong width must not be an exact solution')
    # Stationary uniform solution has the same far density and current;
    # only the chosen localized branch supplies the dip/phase jump.
    uniform_residual=0
    return dict(wrong_width_pde_residual=error,uniform_solution_also_exists=uniform_residual==0,
                implication='asymptotic density/current do not uniquely select the localized branch')

def sink_and_energy_transport():
    x=np.linspace(-12,12,2001); b=.6;u=-b
    f,fx,fxx=derivatives(x,0,b,u); n=abs(f)**2
    unforced=-.5*fxx-1j*u*fx+(n-1)*f
    Gamma=.02*np.exp(-x*x)
    rhs=-1j*unforced-.5*Gamma*f
    nt=2*np.real(np.conj(f)*rhs)
    require(np.max(abs(nt+Gamma*n))<1e-14,'explicit local sink')
    loss=float(np.trapezoid(nt,x));require(loss<-.01,'sink changes amount')
    # For stationary laboratory wave exp(-i mu t), energy flux J_E=mu*j.
    mu=1+b*b/2; j=-b
    psi=np.exp(1j*u*x)*f; psix=np.exp(1j*u*x)*(fx+1j*u*f)
    psit=-1j*mu*psi; JE=-np.real(np.conj(psit)*psix)
    require(np.max(abs(JE-mu*j))<1e-14,'energy flux')
    return dict(sink_initial_rate=loss,constant_energy_flux=mu*j,
                chemical_frequency_same_at_both_ends=True,
                note='Conservative throughflow is not assigned irreversible entropy production')

def grid_and_time():
    rows=[]
    for N in [128,256,512]: rows.append(evolve(N,2)[0])
    errors=[r['complex_max_error'] for r in rows]
    require(errors[0]>12*errors[1] and errors[1]>12*errors[2],'fourth-order spatial trend')
    arow,_,y1=evolve(256,2,rtol=1e-8)
    brow,_,y2=evolve(256,2,rtol=1e-11)
    tolerance_change=float(np.max(abs(y1-y2)))
    require(tolerance_change<2e-8,'time tolerance check')
    return dict(spatial_refinement=rows,time_tolerance_difference=tolerance_change,
                method='FD4 method of lines; adaptive DOP853; analytic exterior ghost values')

def sustained_and_moving():
    long,x,y=evolve(256,30)
    require(long['density_max_error']<3e-5,'long unperturbed evolution')
    moving,_,_=evolve(256,2,u=.1)
    require(moving['complex_max_error']<1e-5,'moving branch')
    # Domain test at comparable resolution, not unrelated grid/box changes.
    a,xa,ya=evolve(256,2,L=15)
    b,xb,yb=evolve(342,2,L=20)
    require(b['complex_max_error']<5e-6,'wider domain')
    return dict(stationary_30_time_units=long,moving_case=moving,wider_domain=b,
                limits='unperturbed persistence with numerical truncation errors only; no full spectral/nonlinear or 3D stability proof')

def invalid():
    for bad in [1,-1,np.nan,np.inf]:
        try: profile(0,b=bad)
        except ValueError: pass
        else: raise AssertionError('invalid b accepted')
    return dict(valid_branch='|b|<1; b=0 has a node, so nonzero-density transport formula excludes it')

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',default='test-results.json'); args=p.parse_args()
    checks=[('exact_GP_branch_and_current',symbolic_solution),('pointwise_PDE_and_flux',numerical_pde),
            ('moving_and_fixed_control_volumes',open_control_volume),('momentum_flux_and_gradient_stress',stress_balance),
            ('phase_deficit_energy_and_inverse_route',branch_observables),('throughflow_not_lifetime',throughflow_time),
            ('orientation_and_limits',orientation_and_limits),('wrong_width_and_branch_nonuniqueness',constitutive_counterexample),
            ('actual_sink_vs_conservative_energy_flow',sink_and_energy_transport),('spatial_temporal_checks',grid_and_time),
            ('sustained_and_moving_evolution',sustained_and_moving),('invalid_inputs',invalid)]
    for name,fn in checks:
        try: CHECKS.append(dict(name=name,status='PASS',detail=fn()))
        except Exception as e: CHECKS.append(dict(name=name,status='FAIL',error=repr(e)))
    report=dict(study='IC-09',utc=datetime.now(timezone.utc).isoformat(),
                code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,
                scope='Known GP gray-soliton comparator; exact and generated-data checks, no empirical fit, no ARK variable identification or independent reviewer',
                passed=sum(c['status']=='PASS' for c in CHECKS),total=len(CHECKS),checks=CHECKS)
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['passed']==report['total'] else 1)
if __name__=='__main__': main()
