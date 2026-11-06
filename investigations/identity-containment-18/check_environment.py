#!/usr/bin/env python3
"""IC-18: responsive environment, reference offsets and scale.
Declared local quadratic extension; no empirical inputs or ARK scalar identification.
Python 3.11+, numpy/scipy/sympy. Run --output new-results.json; no overwrite.
"""
from __future__ import annotations
import argparse, hashlib, json, platform
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import scipy
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm
from scipy.optimize import minimize
import sympy as sp

CHECKS=[]
def require(ok, message):
    if not bool(ok): raise AssertionError(message)
def zero(expr): require(sp.simplify(expr)==0, str(sp.simplify(expr)))
def close(a,b,rtol=1e-10,atol=1e-12):
    require(np.allclose(a,b,rtol=rtol,atol=atol),f'{a} != {b}')

def background_vs_reference():
    q,u,z0,C,g,B=sp.symbols('q u z0 C g B',real=True)
    A=3+z0*z0/5
    F=C+A*q*q/2+B*u*u/2-g*q*u
    zero(sp.diff(F,q)-sp.diff(F-C,q))
    zero(sp.diff(F,u)-sp.diff(F-C,u))
    H=sp.hessian(F,(q,u))
    require(H[0,0].diff(z0)!=0,'Physical background falsely disappeared')
    # An additive energy offset at fixed volume is different from pressure work.
    R,P=sp.symbols('R P',positive=True)
    zero(sp.diff(P*4*sp.pi*R**3/3,R)-4*sp.pi*P*R**2)
    return dict(reference_offset_changes_forces=False,background_curvature=str(A),
                example_relaxed_curvatures=[3-.8**2/2,3.2-.8**2/2],
                scope='Local deviations about a jointly stationary supported reference; no gravitational metric variation.')

def block_elimination():
    A=np.array([[3.,.4],[.4,2.]])
    B=np.array([[2.,.2],[.2,1.5]])
    C=np.array([[.6,.1],[.2,.5]])
    h=np.array([.2,-.1]);j=np.array([.05,.08])
    K=A-C@np.linalg.solve(B,C.T)
    H=np.block([[A,-C],[-C.T,B]])
    x=np.linalg.solve(K,h+C@np.linalg.solve(B,j))
    y=np.linalg.solve(B,C.T@x+j)
    full=np.linalg.solve(H,np.r_[h,j]);close(full,np.r_[x,y])
    result=minimize(lambda w:.5*w@H@w-np.r_[h,j]@w,np.zeros(4),
                    jac=lambda w:H@w-np.r_[h,j],method='BFGS',options={'gtol':1e-11})
    close(result.x,full,atol=1e-9)
    require(np.linalg.eigvalsh(K).min()>0 and np.linalg.eigvalsh(A-K).min()>=0,'Schur stability')
    return dict(clamped_matrix=A.tolist(),relaxed_matrix=K.tolist(),
                equilibrium=x.tolist(),full_minimizer_difference=float(np.max(abs(result.x-full))),
                environment_is_new_resolved_coordinate=True)

def reference_partition():
    q,A,B,g,E,S,eps,d=sp.symbols('q A B g E S eps d', real=True)
    Fe=A*q*q/2-(g*q+E)**2/(2*B)
    split=Fe.subs(E,S+eps)
    zero(split.subs({S:S-d,eps:eps+d},simultaneous=True)-split)
    # Three output anchors still cannot resolve four independent controls.
    C=np.array([[1,0,0,1],[0,1,0,1],[0,0,1,1]],float)
    n=np.array([-1,-1,-1,1.]);close(C@n,np.zeros(3))
    require(np.linalg.matrix_rank(C)==3,'Three independent outputs')
    return dict(sum_partition_invariant=True,three_anchor_map_rank=3,
                unobserved_environment_direction=n.tolist(),
                scope='Sum-only coupling assumption; not proof of sufficiency of any ARK scalar set.')

def scalar_environment_sufficiency():
    C=np.array([[1.,0.],[0.,2.]])
    z1=np.array([1.,0.]);z2=np.array([0.,1.])
    require(z1.sum()==z2.sum() and not np.allclose(C@z1,C@z2),'Scalar-total counterexample')
    c=np.array([1.,2.]);w=np.array([3.,-1.]);rank1=np.outer(c,w)
    dz=np.array([1.,3.]);close(rank1@dz,np.zeros(2))
    # A rank-one statement is only local unless nonlinear fibers are checked.
    return dict(equal_totals=[float(z1.sum()),float(z2.sum())],
                responses=[(C@z1).tolist(),(C@z2).tolist()],
                rank2_requires_more_than_one_smooth_local_control=True,
                rank1_example=np.linalg.matrix_rank(rank1).item())

def joint_energy_balance():
    q,u,qd,ud,A,B,g,M,L=sp.symbols('q u qd ud A B g M L',real=True)
    F=A*q*q/2+B*u*u/2-g*q*u
    fq=sp.diff(F,q);fu=sp.diff(F,u)
    zero(fq*(-M*fq)+fu*(-L*fu)+M*fq*fq+L*fu*fu)
    aa,bb,gg,mm,ll=3.,2.,.8,.7,.3
    H=np.array([[aa,-gg],[-gg,bb]]);D=np.diag([mm,ll]);J=-D@H
    x0=np.array([.2,-.1]);t=np.linspace(0,10,101)
    exact=np.array([expm(J*tt)@x0 for tt in t])
    sol=solve_ivp(lambda tt,x:J@x,(0,10),x0,t_eval=t,rtol=1e-11,atol=1e-13)
    require(sol.success,'ODE')
    err=float(np.max(abs(sol.y.T-exact)));require(err<1e-10,'Separate solver')
    energy=np.einsum('ni,ij,nj->n',exact,H,exact)/2
    require(np.max(np.diff(energy))<=1e-12,'Energy increased')
    return dict(ODE_exponential_error=err,initial_energy=float(energy[0]),
                final_energy=float(energy[-1]),
                caveat='Relaxational effective energy, not demonstrated microscopic total-energy dynamics.')

def memory_and_rate_response():
    A,B,g,L,w,amp=3.,2.,.8,.3,1.1,.02
    lam=L*B;u0=.03
    # Prescribed q, independently integrate u and compare to explicit convolution.
    times=[.1,.8,2.,5.]
    errs=[]
    sol=solve_ivp(lambda t,y:[-lam*y[0]+L*g*amp*np.sin(w*t)],(0,5),[u0],
                  dense_output=True,rtol=1e-12,atol=1e-14)
    for t in times:
        conv=np.exp(-lam*t)*u0+quad(lambda s:np.exp(-lam*(t-s))*L*g*amp*np.sin(w*s),0,t,epsabs=1e-13)[0]
        errs.append(float(abs(sol.sol(t)[0]-conv)))
    require(max(errs)<1e-11,'Convolution equivalence')
    period=2*np.pi/w;tt=np.linspace(18*period,20*period,1001)
    out=solve_ivp(lambda t,y:[-lam*y[0]+L*g*amp*np.sin(w*t)],(0,20*period),[0],
                  t_eval=tt,rtol=1e-11,atol=1e-13,max_step=period/50)
    K=A-g*g/(B+1j*w/L)
    force=A*amp*np.sin(w*tt)-g*out.y[0]
    theory=amp*(K.real*np.sin(w*tt)+K.imag*np.cos(w*tt))
    err=float(np.max(abs(force-theory)));require(err<1e-10,'Frequency law')
    return dict(slow_stiffness=A-g*g/B,fast_stiffness=A,
                response_angular_rate=w,complex_stiffness=[float(K.real),float(K.imag)],
                memory_integral_max_error=max(errs),sinusoid_error=err,
                two_environments_same_equilibrium_and_static_response_different_times=[1/(.3*B),1/(3*B)])

def normalization_degeneracy():
    A,B,g,G,L=3.,2.,.8,8.,.3;alpha=4.
    def obs(B,g,G,L):
        return np.array([A-g*g/B,np.sqrt(G/B),1/(L*B),
                         (A-g*g/(B+1j/L)).real,(A-g*g/(B+1j/L)).imag])
    old=obs(B,g,G,L);new=obs(B/alpha**2,g/alpha,G/alpha**2,L*alpha**2)
    close(old,new)
    return dict(observables=old.tolist(),rescaled_observables=new.tolist(),
                unresolved='u rescaling requires an independent environment measurement/normalization; these responses do not fix absolute entropy.')

def fourier_environment():
    A,B,g,Gq,Gu=3.,2.,.8,.4,8.
    N=64;length=2*np.pi;dx=length/N;x=np.arange(N)*dx
    eye=np.eye(N);lap=(np.roll(eye,1,axis=1)+np.roll(eye,-1,axis=1)-2*eye)/dx**2
    operator=B*eye-Gu*lap
    q=np.cos(x)+.1*np.sin(3*x)
    u=np.linalg.solve(operator,g*q)
    k=np.fft.fftfreq(N,d=1/N);symbol=B+Gu*4*np.sin(k*dx/2)**2/dx**2
    fft=np.fft.ifft(g*np.fft.fft(q)/symbol).real
    close(u,fft,atol=1e-11)
    effective=A*eye-Gq*lap-g*g*np.linalg.inv(operator)
    H=np.block([[A*eye-Gq*lap,-g*eye],[-g*eye,operator]])
    require(np.linalg.eigvalsh(H).min()>0,'Joint stability')
    correction=[]
    for kk in [0,.5,1,2,5]:correction.append(dict(k=kk,relaxed_correction=g*g/(B+Gu*kk*kk)))
    return dict(dense_Fourier_error=float(np.max(abs(u-fft))),response_length=float(np.sqrt(Gu/B)),
                effective_curvature_min=float(np.linalg.eigvalsh(effective).min()),
                corrections=correction,scope='Specified periodic discretization; not a measured medium.')

def spherical_response():
    r,R,B,G,g,q0=sp.symbols('r R B G g q0',positive=True)
    ell=sp.sqrt(G/B);t=r/ell;x=R/ell
    inside=g*q0/B*(1-(x+1)*sp.exp(-x)*sp.sinh(t)/t)
    outside=g*q0/B*(x*sp.cosh(x)-sp.sinh(x))*sp.exp(-t)/t
    zero((inside-outside).subs(r,R))
    zero((sp.diff(inside,r)-sp.diff(outside,r)).subs(r,R))
    zero(B*inside-G*(sp.diff(inside,r,2)+2*sp.diff(inside,r)/r)-g*q0)
    zero(B*outside-G*(sp.diff(outside,r,2)+2*sp.diff(outside,r)/r))
    ratios=[]
    for x0 in [.1,.5,1.,3.,5.]:
        analytic=-np.expm1(-x0)-x0*np.exp(-x0)
        integral=quad(lambda t:t*np.exp(-t),0,x0,epsabs=1e-13)[0]
        close(analytic,integral)
        ratios.append(dict(R_over_ell=x0,center_response_fraction=analytic))
    xx=sp.symbols('x',positive=True)
    small=sp.series(1-(1+xx)*sp.exp(-xx),xx,0,4)
    return dict(center_ratios=ratios,small_source_series=str(small),
                interface='field and normal gradient continuous; no impermeable boundary inserted',
                source='uniform prescribed q0 inside sphere, zero outside; not a solved self-bound identity',
                far_field='exp(-r/ell)/r; not an unscreened gravity derivation')

def sphere_fd_refinement():
    # On an aligned radial grid solve y=r*u. Midpoint source at jump gives
    # second-order discretization; the distant Dirichlet value uses the analytic exterior.
    from scipy.linalg import solve_banded
    B,G,g,q0,R,L=2.,8.,.8,.1,2.,12.
    ell=np.sqrt(G/B);exact=g*q0/B*(1-(1+R/ell)*np.exp(-R/ell))
    errors=[]
    for N in [240,480,960]:
        h=L/N;r=np.arange(1,N)*h;m=N-1
        src=g*q0*r*np.where(r<R-1e-12,1.,np.where(abs(r-R)<1e-12,.5,0.))
        # Far endpoint y(L) is replaced by exact analytic exterior value,
        # leaving this an independently solved interior verification.
        x=R/ell;yL=g*q0/B*ell*(x*np.cosh(x)-np.sinh(x))*np.exp(-L/ell)
        ab=np.zeros((3,m));ab[1]=2*G/h**2+B;ab[0,1:]=-G/h**2;ab[2,:-1]=-G/h**2
        src[-1]+=G*yL/h**2
        y=solve_banded((1,1),ab,src)
        u0=(4*(y[0]/h)-(y[1]/(2*h)))/3
        errors.append(float(abs(u0-exact)))
    require(errors[0]>3.5*errors[1] and errors[1]>3.5*errors[2],'Radial grid convergence')
    return dict(center_exact=exact,grid_sizes=[240,480,960],errors=errors,
                boundary='analytic distant Dirichlet value, not independent external boundary measurement')

def stability_and_massless_limit():
    A,g=3.,.8
    vals=[]
    for B in [2.,.3,.1]:
        eig=np.linalg.eigvalsh(np.array([[A,-g],[-g,B]]))
        vals.append(dict(B=B,determinant=A*B-g*g,lowest_curvature=float(eig[0])))
    require(vals[0]['lowest_curvature']>0 and vals[-1]['lowest_curvature']<0,'Stability boundary')
    return dict(cases=vals,condition='AB>g^2 for unconstrained uniform two-field branch',
                limitation='B -> 0 at fixed finite A,g != 0 is unstable in this candidate. Conserved/forbidden modes or alternative couplings require a different analysis.')

def assembly_and_equilibrium():
    # Local g=0 corner: two controls can leave one phase-selection condition
    # unchanged but cannot be assumed equivalent for response.
    A=3.;g=.8;B1=2.;B2=4.
    k1=A-g*g/B1;k2=A-g*g/B2
    require(k1!=k2,'Same mean confused with same response')
    # For distinct sources linear environmental response superposes; energy
    # after elimination has pair cross terms rather than additive energies.
    L=np.array([[3.,-.5],[-.5,2.]])
    j1=np.array([1.,0.]);j2=np.array([0.,1.])
    e=lambda j:-.5*j@np.linalg.solve(L,j)
    cross=e(j1+j2)-e(j1)-e(j2)
    close(cross,-j1@np.linalg.solve(L,j2))
    return dict(same_zero_equilibrium_different_stiffness=[k1,k2],
                induced_interaction_cross_term=float(cross),
                caution='Assembly effects require a specified source map and spatial arrangement; not proportionality to mass or an exclusion volume.')

def conditional_environment_recovery():
    A,g=3.,.8
    B,G,L=2.,8.,.3
    slow=A-g*g/B; ell=np.sqrt(G/B); te=1/(L*B)
    inferred_B=g*g/(A-slow)
    inferred_G=ell*ell*inferred_B
    inferred_L=1/(inferred_B*te)
    close([inferred_B,inferred_G,inferred_L],[B,G,L])
    k=1.7; predicted=A+.4*k*k-g*g/(inferred_B+inferred_G*k*k)
    actual=A+.4*k*k-g*g/(B+G*k*k);close(predicted,actual)
    return dict(independent_supplied_anchors={'clamped_A':A,'calibrated_g':g,'relaxed_response':slow,'response_length':ell,'response_time':te},
                inferred_parameters=[inferred_B,inferred_G,inferred_L],
                additional_generated_spatial_response=predicted,
                scope='Generated reconstruction plus unused-mode consistency check. Requires independent coupling/energy calibration; not measured entropy or an absolute background.')

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    require(not args.output.exists(),'Refusing to overwrite existing result')
    tests=[('background_vs_arbitrary_reference',background_vs_reference),('joint_equilibrium_and_elimination',block_elimination),
      ('partition_and_three_anchor_ambiguity',reference_partition),('scalar_environment_sufficiency',scalar_environment_sufficiency),
      ('joint_power_balance_and_solver',joint_energy_balance),('memory_and_dynamic_response',memory_and_rate_response),
      ('environment_normalization_ambiguity',normalization_degeneracy),('spatial_operator_response',fourier_environment),
      ('spherical_profile_and_matching',spherical_response),('radial_refinement',sphere_fd_refinement),
      ('joint_stability_and_massless_limit',stability_and_massless_limit),('assembly_and_response_equivalence',assembly_and_equilibrium),('conditional_environment_recovery',conditional_environment_recovery)]
    for name,fn in tests:
        try:CHECKS.append(dict(name=name,status='PASS',detail=fn()))
        except Exception as exc:CHECKS.append(dict(name=name,status='FAIL',error=repr(exc)))
    report=dict(study='IC-18',utc=datetime.now(timezone.utc).isoformat(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=sp.__version__,
       scope='Conditional structural extension and generated tests. No experiment, entropy calibration, gravitational derivation or independent review.',
       passed=sum(c['status']=='PASS' for c in CHECKS),total=len(CHECKS),checks=CHECKS)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2));raise SystemExit(report['passed']!=report['total'])
if __name__=='__main__':main()
