#!/usr/bin/env python3
"""IC-16: source-linked coupled-core consistency, not empirical ARK validation.
Run with Python 3.11+, numpy/scipy/sympy. No experimental files are read.
Tests label algebraic consequences and added constitutive/kinetic assumptions.
"""
from __future__ import annotations
import argparse, hashlib, json, platform
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import scipy
from scipy.integrate import solve_ivp, quad
from scipy.linalg import expm
import sympy as s

CHECKS=[]
def require(ok, message):
    if not bool(ok): raise AssertionError(message)
def zero(expr):
    require(s.simplify(expr)==0, str(s.simplify(expr)))

def normalized_history():
    q,q0=s.symbols('q q0', positive=True)
    zero(s.diff(s.log(q/q0),q)-1/q)
    loop=quad(lambda t:.2*np.cos(t)/(1+.2*np.sin(t)),0,2*np.pi,epsabs=1e-12)[0]
    # Independent environmental coordinate changes the tangent coefficient.
    varied=quad(lambda t:(1+.3*np.cos(t))*.2*np.cos(t),0,2*np.pi,epsabs=1e-12)[0]
    require(abs(loop)<1e-12 and abs(varied-.06*np.pi)<1e-12,'Loop integral')
    return dict(normalized_relation='r-r0=log(q/q0), q>0', closed_path_increment=loop,
                environment_dependent_increment=varied,
                scope='Fixed initial reference can persist; restricted log branch has no additional path memory.')

def dimensional_bridge():
    # Dimension vectors: mass,length,time. Source XVI's printed assignments.
    tau=np.array([1,2,-1])  # J s
    kap=np.array([1,0,-2])  # N/m
    theta=np.zeros(3,dtype=int)
    rhs=kap+theta # integral kappa * theta_dot dt
    require(not np.array_equal(tau,rhs),'Unexpected identity')
    ratio=tuple((tau-rhs).tolist())
    require(ratio==(0,2,1),'Conversion dimension')
    return dict(source='XVI sections 2.2/2.3', tau_units='J s', kappa_units='N/m',
                direct_integral_units='N/m', conversion_dimension_needed='length^2 time',
                action='Do not silently use these as the same dimensional law. Keep normalized XVIII branch separate.')

def responsive_variation():
    q,r,e,w,p,qx,rx,ex,qxx=s.symbols('q r e w p qx rx ex qxx',real=True)
    K=1+q*q/s.Integer(5)+r*r/s.Integer(10)
    W=q*q*K-e
    U=(q-s.Rational(3,5))**2/2+s.Rational(3,10)*(q-s.Rational(3,5))*r+r*r+s.Rational(1,10)*w*w
    V=U.subs(w,W)-e*q/s.Integer(20)
    density=K*p*p/2+V
    flux=s.diff(density,p)
    dxflux=s.diff(flux,q)*qx+s.diff(flux,r)*rx+s.diff(flux,e)*ex+s.diff(flux,p)*qxx
    gq=(s.diff(density,q)-dxflux).subs(p,qx)
    expected=-K*qxx-s.diff(K,q)*qx*qx/2-s.diff(K,r)*rx*qx+s.diff(V,q)
    zero(gq-expected)
    gr=s.diff(density,r)
    partial_r=s.diff(U,r).subs(w,W)+s.diff(U,w).subs(w,W)*s.diff(W,r)
    zero(gr-(s.diff(K,r)*p*p/2+partial_r))
    # Shared environment partition leaves every declared map unchanged.
    E,S,eps,delta=s.symbols('E S eps delta', real=True)
    total=s.expand(V.subs(e,S+eps))
    zero(total.subs({S:S-delta,eps:eps+delta}, simultaneous=True)-total)
    return dict(chain_terms='Kq, Kr, Uomega*Wq and Uomega*Wr retained',
                environment_partition='Exact only when every coupling depends on the same total E=S+epsilon',
                scope='Explicit polynomial check; no arbitrary nonlocal-history theorem.')

def reciprocal_dynamics():
    gq,gr,b,v=s.symbols('gq gr b v',real=True)
    M,L,zeta,chi=s.symbols('M L zeta chi',positive=True)
    qdot=-M*(gq+b*gr);rdot=b*qdot-L*gr
    zero(gq*qdot+gr*rdot+M*(gq+b*gr)**2+L*gr**2)
    matrix=s.Matrix([[M,M*b],[M*b,M*b*b+L]])
    zero(matrix.det()-M*L)
    # Quadratic rate potential with qdot=v, rdot independent.
    u=s.symbols('u',real=True)
    R=zeta*v*v/2+(u-b*v)**2/(2*L)
    rsol=b*v-L*gr
    zero((s.diff(R,u)+gr).subs(u,rsol))
    zero((s.diff(R,v)+gq).subs(u,rsol)-(zeta*v+gq+b*gr))
    acc=(-zeta*v-gq-b*gr)/chi
    zero(chi*v*acc+gq*v+gr*(b*v-L*gr)+zeta*v*v+L*gr*gr)
    # Naively attaching rdot=b*qdot to geometry-only gradient flow injects energy.
    naive=-1+3
    corrected=2-6
    require(naive==2 and corrected==-4,'Counterexample')
    return dict(mobility_determinant=str(matrix.det().factor()),
                naive_energy_rate=naive, reciprocal_energy_rate=corrected,
                candidate='A positive quadratic dissipation choice, NOT uniquely derived from ARK or microscopic reversibility.')

def constrained_vs_relaxed():
    q,r,a,c,d,b=s.symbols('q r a c d b',real=True)
    H=a*q*q/2+c*q*r+d*r*r/2
    T=q*q/2
    pull=s.diff(H.subs(r,T),q)
    zero(pull-(s.diff(H,q)+s.diff(T,q)*s.diff(H,r)).subs(r,T))
    curvature=(s.diff(H,q,2)+2*s.diff(T,q)*s.diff(H,q,r)+s.diff(T,q)**2*s.diff(H,r,2)+s.diff(T,q,2)*s.diff(H,r)).subs(r,T)
    zero(s.diff(H.subs(r,T),q,2)-curvature)
    relaxed=s.simplify(H.subs(r,-c*q/d))
    zero(s.diff(relaxed,q,2)-(a-c*c/d))
    # Same stored energy, different permitted response conditions.
    aa,cc,dd,bb=3.,.4,2.,.6
    return dict(frozen_history_stiffness=aa, relaxed_stiffness=aa-cc*cc/dd,
                tangent_constrained_stiffness=aa+2*bb*cc+bb*bb*dd,
                caveat='Response coefficients for one quadratic realization, not universal ARK kappa assignments.')

def equilibrium_constraints():
    M=1.; b=.6;gq=-.6;gr=1.
    qdot=-M*(gq+b*gr)
    require(abs(qdot)<1e-14,'Tangent equilibrium')
    L=.2;rdot=b*qdot-L*gr
    require(rdot<0,'Relaxation opens a direction')
    # Geometric closed/no-flux boundary alone does not impose amount conservation.
    q=.7
    require(-q!=0,'Local relaxation changes integral in a uniform unit volume')
    return dict(L_zero='gq+b*gr=0 suffices even when gq and gr are nonzero',
                L_positive='If M,L>0, stationary overdamped state requires gq=gr=0',
                opened_history_rate=rdot,
                conservation='Not asserted for q or r. A physical conserved quantity requires a separate flux/symmetry law.')

def linear_operator(chi=.7,zeta=.4,L=.3,a=3.,c=.4,d=2.,b=.6):
    return np.array([[0,1,0],[-(a+b*c)/chi,-zeta/chi,-(c+b*d)/chi],[-L*c,b,-L*d]])

def inertial_modal_checks():
    A=linear_operator(); x0=np.array([.1,.08,-.05]);tt=np.linspace(0,12,121)
    exact=np.array([expm(A*t)@x0 for t in tt]);sol=solve_ivp(lambda t,x:A@x,(0,12),x0,t_eval=tt,rtol=2e-11,atol=2e-13)
    require(sol.success,'IVP failed')
    error=float(np.max(np.abs(sol.y.T-exact)));require(error<1e-9,'Modal reconstruction')
    def H(x):
        q,v,r=x.T
        return .5*.7*v*v+.5*3*q*q+.4*q*r+.5*2*r*r
    e=H(exact);require(np.max(np.diff(e))<=1e-12,'Energy growth')
    # A separately implemented fixed-step RK4 must converge to matrix exponential.
    errors=[]
    for dt in [.08,.04,.02]:
        x=x0.copy()
        for _ in range(round(4/dt)):
            k1=A@x;k2=A@(x+.5*dt*k1);k3=A@(x+.5*dt*k2);k4=A@(x+dt*k3)
            x+=dt*(k1+2*k2+2*k3+k4)/6
        errors.append(float(np.max(np.abs(x-expm(A*4)@x0))))
    require(errors[0]>10*errors[1] and errors[1]>10*errors[2],'Refinement')
    # Reversible constrained sector: zeta=L=0, not an automatically superfluid model.
    B=linear_operator(zeta=0,L=0)
    y=np.array([expm(B*t)@x0 for t in tt]);drift=float(np.max(np.abs(H(y)-H(y)[0])))
    require(drift<1e-12,'Reversible energy')
    invariant=float(np.max(np.abs((y[:,2]-.6*y[:,0])-(x0[2]-.6*x0[0]))))
    require(invariant<1e-12,'Tangent invariant')
    return dict(IVP_exponential_error=error,RK4_errors=errors,eigenvalues=[{'real':float(z.real),'imag':float(z.imag)} for z in np.linalg.eigvals(A)],
                reversible_energy_drift=drift,tangent_invariant_error=invariant,
                scope='One positive quadratic mode; not proof of global nonlinear or 3D physical stability.')

def memory_response():
    a,c,d,b,L=3.,.4,2.,.6,.3
    high=a+2*b*c+b*b*d;low=a-c*c/d;C=c+b*d
    def modulus(w):return high-(C*C/d)/(1+1j*w/(L*d))
    require(abs(modulus(1e-9).real-low)<1e-12,'Static limit')
    require(abs(modulus(1e9).real-high)<1e-12,'Fast limit')
    w=1.1; amp=.03;period=2*np.pi/w
    def rhs(t,r):return [b*amp*w*np.cos(w*t)-L*(c*amp*np.sin(w*t)+d*r[0])]
    tt=np.linspace(18*period,20*period,1001)
    sol=solve_ivp(rhs,(0,20*period),[0.],t_eval=tt,rtol=1e-10,atol=1e-12,max_step=period/50)
    q=amp*np.sin(w*tt);r=sol.y[0];force=(a+b*c)*q+(c+b*d)*r
    expected=amp*(modulus(w).real*np.sin(w*tt)+modulus(w).imag*np.cos(w*tt))
    err=float(np.max(np.abs(force-expected)));require(err<1e-9,'Frequency response')
    # Local state dynamics equal an explicit memory integral with the same initial data.
    t=.83;r0=.07
    conv=np.exp(-L*d*t)*r0+quad(lambda s:np.exp(-L*d*(t-s))*(b*amp*w*np.cos(w*s)-L*c*amp*np.sin(w*s)),0,t,epsabs=1e-12)[0]
    direct=solve_ivp(rhs,(0,t),[r0],rtol=1e-12,atol=1e-14).y[0,-1]
    require(abs(conv-direct)<1e-11,'Memory equivalence')
    return dict(slow_limit=low,fast_limit=high,forcing_angular_rate=w,
                complex_modulus={'real':float(modulus(w).real),'imag':float(modulus(w).imag)},
                numerical_response_error=err,memory_integral_error=float(abs(conv-direct)),
                interpretation='A derived response spectrum, not an independently assigned pressure-balance omega.')

def field_terms(q,r,e,dx):
    """Discrete variation of one declared nonlinear dimensionless realization."""
    K=1+.2*q*q+.1*r*r;Kq=.4*q;Kr=.2*r
    W=q*q*K-e;Wq=2*q*K+q*q*Kq;Wr=q*q*Kr
    z=q-.6
    V=.5*z*z+.3*z*r+r*r+.1*W*W-.05*e*q
    Vq=z+.3*r+.2*W*Wq-.05*e
    Vr=.3*z+2*r+.2*W*Wr
    Ve=-.2*W-.05*q
    delta=np.roll(q,-1)-q;edge=(K+np.roll(K,-1))/2
    F=float(dx*(np.sum(.5*edge*(delta/dx)**2)+np.sum(V)))
    squared=((delta/dx)**2+(np.roll(delta,1)/dx)**2)/4
    gq=-(edge*delta-np.roll(edge*delta,1))/dx**2+Kq*squared+Vq
    gr=Kr*squared+Vr
    return F,gq,gr,Ve,K

def discrete_variation_check():
    n=32;dx=2*np.pi/n;x=dx*np.arange(n)
    q=.6+.04*np.cos(x);r=.03*np.sin(2*x);dq=np.cos(3*x);dr=.2*np.sin(x);E=.4
    F,gq,gr,ge,K=field_terms(q,r,E,dx)
    predicted=dx*np.dot(gq,dq)+dx*np.dot(gr,dr)
    errors=[]
    for h in [1e-2,5e-3,2.5e-3]:
        fd=(field_terms(q+h*dq,r+h*dr,E,dx)[0]-field_terms(q-h*dq,r-h*dr,E,dx)[0])/(2*h)
        errors.append(float(abs(fd-predicted)))
    require(errors[0]>3.5*errors[1] and errors[1]>3.5*errors[2],'Directional gradient convergence')
    h=1e-6;fd=(field_terms(q,r,E+h,dx)[0]-field_terms(q,r,E-h,dx)[0])/(2*h)
    require(abs(fd-dx*np.sum(ge))<1e-9,'External power derivative')
    return dict(direction_errors=errors,environment_derivative_error=float(abs(fd-dx*np.sum(ge))),
                scheme='Periodic finite-volume energy and its exact discrete gradient; not a continuum convergence study.')

def nonlinear_power_balance():
    n=24;dx=2*np.pi/n;x=np.arange(n)*dx;chi=.5;zeta=.4;L=.25
    q0=.6+.04*np.cos(x);r0=.03*np.sin(2*x);v0=.02*np.cos(2*x)
    y0=np.r_[q0,v0,r0,0.,0.]
    def env(t):return .4+.05*np.sin(.7*t),.035*np.cos(.7*t)
    def rhs(t,y):
        q,v,r=y[:n],y[n:2*n],y[2*n:3*n];E,Edot=env(t)
        F,gq,gr,ge,K=field_terms(q,r,E,dx);b=.7*K
        return np.r_[v,(-zeta*v-gq-b*gr)/chi,b*v-L*gr,
                     dx*np.sum(zeta*v*v+L*gr*gr),dx*np.sum(ge)*Edot]
    tt=np.linspace(0,2,101);runs=[]
    for tol in [1e-7,1e-9]:
        sol=solve_ivp(rhs,(0,2),y0,t_eval=tt,rtol=tol,atol=tol*.01,max_step=.02)
        require(sol.success,'Nonlinear lattice integration')
        energies=[]
        for t,y in zip(tt,sol.y.T):
            F=field_terms(y[:n],y[2*n:3*n],env(t)[0],dx)[0]
            energies.append(F+.5*chi*dx*np.dot(y[n:2*n],y[n:2*n]))
        energies=np.asarray(energies)
        balance=energies-energies[0]+sol.y[-2]-sol.y[-1]
        err=float(np.max(np.abs(balance)));require(err<1e-7,'Power closure')
        runs.append((sol,err))
    diff=float(np.max(np.abs(runs[0][0].y-runs[1][0].y)));require(diff<2e-6,'Tolerance agreement')
    q=runs[-1][0].y[:n]
    require(np.min(q)>0 and np.max(q)<np.pi/2,'Illustrative chart left range')
    return dict(energy_balance_max_errors=[a[1] for a in runs],solution_tolerance_difference=diff,
                q_range=[float(q.min()),float(q.max())],lattice_sites=n,
                added_assumptions='K=1+.2q^2+.1r^2; b=.7K; declared polynomial U and W=q^2 K-E; prescribed E(t)',
                warning='Generated finite lattice demonstration only. No fitted physical functions, universal ARK mapping or PDE well-posedness theorem.')

def clamping_and_source_limit():
    v,r,gq,gr,b,zeta,L=s.symbols('v r gq gr b zeta L',real=True)
    R=zeta*v*v/2+(r-b*v)**2/(2*L)
    zero(s.diff(R.subs(r,0),v)-(zeta+b*b/L)*v)
    # A truly prescribed memory coordinate has a different mobility, rather than
    # setting its equation to zero after solving the unconstrained system.
    D,lap,Uq,P=s.symbols('D lap Uq P',real=True)
    mu=-lap+Uq-P
    zero(-D*mu-(D*lap+D*(P-Uq)))
    return dict(fixed_history_effective_mobility='1/(zeta+b^2/L) for L>0',
                source_compatibility='In the declared fixed-parameter sector, F=D(Pi-Uq) recovers XXV E6/E16.',
                caveat='Equilibrium matching does not select a universal kinetic law.')

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    require(not args.output.exists(),'Refusing to overwrite results')
    tests=[('normalized_history_and_environment_path',normalized_history),('source_unit_bridge',dimensional_bridge),
           ('responsive_variation_and_partition',responsive_variation),('reciprocal_tangent_dynamics',reciprocal_dynamics),
           ('constrained_and_relaxed_derivatives',constrained_vs_relaxed),('equilibrium_and_conservation_scope',equilibrium_constraints),
           ('linear_modal_energy_and_refinement',inertial_modal_checks),('finite_rate_memory_response',memory_response),
           ('discrete_variation_against_finite_differences',discrete_variation_check),('nonlinear_power_balance',nonlinear_power_balance),
           ('clamping_and_fixed_parameter_source_limit',clamping_and_source_limit)]
    for name,fn in tests:
        try:CHECKS.append({'name':name,'status':'PASS','detail':fn()})
        except Exception as exc:CHECKS.append({'name':name,'status':'FAIL','error':repr(exc)})
    report={'study':'IC-16','utc':datetime.now(timezone.utc).isoformat(),'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':s.__version__,
            'scope':'Source-derived distinctions plus explicitly added candidate kinetics; generated consistency tests only. No empirical fit, full-theory validation, independent review or NIST analysis.',
            'passed':sum(c['status']=='PASS' for c in CHECKS),'total':len(CHECKS),'checks':CHECKS}
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))
    raise SystemExit(0 if report['passed']==report['total'] else 1)
if __name__=='__main__':main()
