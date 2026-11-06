#!/usr/bin/env python3
"""IC-19: pressure work as a bounded environment-to-identity coupling.
Source-law compatibility and constructed verification, not measured ARK physics.
Python 3.11+, numpy/scipy/sympy. Refuses to overwrite a result file.
"""
from __future__ import annotations
import argparse, hashlib, json, platform
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
import sympy as s

CHECKS=[]
def require(ok, message):
    if not bool(ok): raise AssertionError(message)
def zero(expr): require(s.simplify(expr)==0,str(s.simplify(expr)))
def close(a,b,rtol=1e-10,atol=1e-11):
    require(np.allclose(a,b,rtol=rtol,atol=atol), f'{a} != {b}')

def pressure_work_and_surface():
    # Smooth ellipsoid; integrate area-vector pullback from a unit sphere.
    q,r,P=.2,-.1,2.3
    axes=np.array([np.exp(q),np.exp(r),np.exp(-q/2)])
    da=np.array([axes[0],0.,-.5*axes[2]])
    db=np.array([0.,axes[1],0.])
    z,w=np.polynomial.legendre.leggauss(24); phi=2*np.pi*np.arange(48)/48
    normal=np.stack(np.broadcast_arrays(np.sqrt(1-z[:,None]**2)*np.cos(phi),
                    np.sqrt(1-z[:,None]**2)*np.sin(phi),z[:,None]),axis=-1)
    area_vector=np.prod(axes)*normal/axes
    weight=w[:,None]*(2*np.pi/48)
    net=np.sum(-P*area_vector*weight[...,None],axis=(0,1))
    load_q=float(np.sum(-P*np.sum(area_vector*(normal*da),axis=-1)*weight))
    load_r=float(np.sum(-P*np.sum(area_vector*(normal*db),axis=-1)*weight))
    V=4*np.pi*np.prod(axes)/3
    close(net,np.zeros(3));close([load_q,load_r],[-P*.5*V,-P*V])
    return dict(net_translation_force=net.tolist(),mode_loads=[load_q,load_r],
                expected=[-P*.5*V,-P*V],scope='Hydrostatic traction and specified deformation; no medium exclusion hypothesis.')

def source_projection_and_integrability():
    q,r,P,E0=s.symbols('q r P E0',positive=True)
    V=3-2*q+q*q/5+q*r/3+r*r/7
    Jq=-P*s.diff(V,q)/E0;Jr=-P*s.diff(V,r)/E0
    zero(s.diff(Jq,r)-s.diff(Jr,q))
    # Deleting the history-coordinate pressure load loses integrability.
    missing=s.diff(Jq,r)
    zero(missing+P/(3*E0))
    # A state-dependent generalized force must be integrated, not multiplied by q.
    c=s.symbols('c',positive=True);J=P*c/q
    exact=-P*c*s.log(q)
    zero(-s.diff(exact,q)-J)
    naive=-J*q
    zero(s.diff(naive,q))
    require(s.simplify(-s.diff(naive,q)-J)!=0,'False force agreement')
    # Reduced source coefficient equals the pressure-work derivative, not P alone.
    Vstar,alpha=s.symbols('Vstar alpha',positive=True)
    Va=Vstar*(1-alpha*q)
    zero(-s.diff(P*Va/E0,q)-P*Vstar*alpha/E0)
    return dict(full_pressure_load_integrable=True,omitted_r_cross_derivative=str(missing),
       state_dependent_product_counterexample='-Pi(q)*q is constant for Pi=P*c/q, whereas correct potential is -P*c*log(q)',
       affine_mode_source='Pi_mode=P*Vstar*alpha/E0',
       note='Pi_mode is not the source field Pi itself or a measured Delta S_t.')

def quadratic_pressure_compatibility():
    q,qref,qe,E0,P0,k,Vref=s.symbols('q qref qe E0 P0 k Vref',positive=True)
    U=E0*k*(q-qe)**2/2;Pint=P0*k*q*q
    V=Vref-E0/P0*(s.log(q/qref)+qe*(1/q-1/qref))
    zero(s.diff(V,q)+s.diff(U,q)/Pint)
    # Flat energy-reference sector, q>0: geometry map is logarithmic.
    V0=V.subs(qe,0);U0=U.subs(qe,0)
    zero(-s.diff(U0,q)/s.diff(V0,q)-Pint)
    P=s.symbols('P',positive=True);G=U0+P*V0
    qeq=s.sqrt(P/(P0*k))
    zero(s.diff(G,q).subs(q,qeq))
    zero(s.diff(G,q,2).subs(q,qeq)-2*E0*k)
    return dict(general_required_volume=str(V),flat_reference='V=Vref-(E0/P0)*log(q/qref)',
       equilibrium='q^2=P/(P0*k)',loaded_curvature='2*E0*k',
       assumptions='same positive constant k on a fixed retained-state branch; early energy identified with reversible fixed-T potential; pressure mechanically conjugate to V',
       reference_limit='V_q=0 at q=qe if qe>0: pressure-as-ratio chart singular there; q=0 excluded.')

def affine_volume_alternative():
    q,Lam,P0,k,P=s.symbols('q Lam P0 k P',positive=True)
    U=Lam*P0*k*q**3/3;V=3-Lam*q
    zero(-s.diff(U,q)/s.diff(V,q)-P0*k*q*q)
    G=U+P*V;qeq=s.sqrt(P/(P0*k))
    zero(s.diff(G,q).subs(q,qeq))
    zero(s.diff(G,q,2)-2*Lam*P0*k*q)
    return dict(volume='V=Vref-Lambda*(q-qref)',required_energy='Lambda*P0*k*q^3/3 + reference',
       source_drive='P*Lambda',same_pressure_equilibrium=True,
       caveat='Alternative completion, not simultaneous identity with the quadratic energy branch.')

def branches(q):
    if not np.isfinite(q) or q<=0: raise ValueError('q must be positive')
    # All quantities in this witness use declared normalized energy/volume/pressure units.
    E0=P0=1.;k=2.;qref=.5;Vref=3.;Lam=E0/(P0*qref)
    Uq=E0*k*q*q/2;Vq=Vref-E0/P0*np.log(q/qref)
    Ua=Lam*P0*k*q**3/3+E0*k*qref*qref/2-Lam*P0*k*qref**3/3
    Va=Vref-Lam*(q-qref)
    if min(Vq,Va)<=0: raise ValueError('Volume chart left admissible region')
    P=P0*k*q*q
    return dict(q=q,pressure=P,quadratic=dict(energy=Uq,volume=Vq,response=E0*k*q,loaded_stiffness=2*E0*k,
              bulk_modulus=2*P*Vq/(E0/P0)),
              affine=dict(energy=Ua,volume=Va,response=Lam*P0*k*q*q,loaded_stiffness=2*Lam*P0*k*q,
              bulk_modulus=2*P0*k*q*Va/Lam))

def matched_reference_distinct_transfer():
    start=branches(.5)
    for key in ['energy','volume','response','loaded_stiffness','bulk_modulus']:
        close(start['quadratic'][key],start['affine'][key])
    end=branches(1.)
    require(abs(end['quadratic']['volume']-end['affine']['volume'])>.3,'Transfer failed to separate branches')
    results=[]
    for P in [.5,.8,1.2,2.]:
        qe=np.sqrt(P/2)
        for name in ['quadratic','affine']:
            result=minimize_scalar(lambda q:branches(q)[name]['energy']+P*branches(q)[name]['volume'],
                       bounds=(.15,1.3),method='bounded',options={'xatol':1e-13})
            require(result.success,'Minimum failed');close(result.x,qe,atol=2e-8)
            results.append(dict(pressure=P,branch=name,q_numeric=float(result.x),q_exact=float(qe)))
    return dict(matched_reference=start,distinct_later_state=end,minimization=results,
       scope='Finite candidate laws deliberately matched at one state; no theorem that three anchors fail within an already fixed model.')

def energy_from_pressure_quadrature():
    q0=.5;q1=1.;E0=P0=1.;k=2.;Lam=2.
    pressure=lambda q:P0*k*q*q
    work_log=quad(lambda q:-pressure(q)*(-E0/(P0*q)),q0,q1,epsabs=1e-13)[0]
    work_affine=quad(lambda q:-pressure(q)*(-Lam),q0,q1,epsabs=1e-13)[0]
    close(work_log,branches(q1)['quadratic']['energy']-branches(q0)['quadratic']['energy'])
    close(work_affine,branches(q1)['affine']['energy']-branches(q0)['affine']['energy'])
    return dict(energy_changes_from_independent_work_integrals=[work_log,work_affine],
                operation='Isothermal reversible, fixed retained state; not unrestricted entropy production.')

def pressure_reference_accounting():
    q,p,c=s.symbols('q p c',real=True);V=3-q+q*q/5;F=q*q+q**4/4
    zero((F-c*V)+(p+c)*V-(F+p*V))
    only_pressure_shift=s.diff(F+(p+c)*V,q)-s.diff(F+p*V,q)
    zero(only_pressure_shift-c*s.diff(V,q))
    return dict(consistent_repartition_invariant=True,
                changing_pressure_alone_changes_force=str(only_pressure_shift),
                lesson='Moving a baseline between potentials is different from physically changing pressure at fixed identity energy.')

def finite_environment_curvature():
    q,r,C,VT=s.symbols('q r C VT',positive=True)
    V=3-2*q+q*q/5+q*r/3+r*r/7;Ve=VT-V;Fenv=-C*s.log(Ve)
    v=s.Matrix([s.diff(V,q),s.diff(V,r)]);h=s.hessian(V,(q,r));P=C/Ve
    expected=P*h+C/Ve**2*(v*v.T)
    diff=s.hessian(Fenv,(q,r))-expected
    for item in diff:zero(item)
    subs={q:s.Rational(1,2),r:s.Rational(1,10),C:2,VT:8}
    extra=np.array((C/Ve**2*(v*v.T)).subs(subs),float)
    eig=np.linalg.eigvalsh(extra);require(eig.min()>-1e-13,'Reservoir correction not PSD')
    return dict(formula='H_environment=P*H_V+(K_env/V_env)*grad(V) outer grad(V)',
                extra_eigenvalues=eig.tolist(),
                scope='Constrained complementary volume at fixed T,N, not the unconstrained Schur relaxation of IC-18.')

def finite_environment_minimum():
    # Same mean pressure and branch at reference; finite surrounding volume adds curvature.
    qref=.5;Vtot=8.;C=2.5
    V=lambda q:3-np.log(q/qref)
    Vp=lambda q:-1/q
    identity=lambda q:q*q
    total=lambda q,VT:identity(q)-C*np.log(VT-V(q))
    derivative=lambda q,VT:2*q+C/(VT-V(q))*Vp(q)
    root=brentq(lambda q:derivative(q,Vtot),.2,1.2);close(root,qref)
    exact=4+.5/5*(1/qref)**2
    hs=[.01,.005,.0025];errors=[]
    for h in hs:
        fd=(total(qref+h,Vtot)-2*total(qref,Vtot)+total(qref-h,Vtot))/h**2
        errors.append(abs(fd-exact))
    require(errors[0]>3.5*errors[1] and errors[1]>3.5*errors[2],'Reservoir finite-difference refinement')
    newtotal=7.8;newroot=brentq(lambda q:derivative(q,newtotal),.2,1.2)
    mini=minimize_scalar(lambda q:total(q,newtotal),bounds=(.2,1.2),method='bounded',options={'xatol':1e-13})
    require(mini.success,'Finite bath minimization');close(newroot,mini.x,atol=2e-8)
    return dict(reference_q=root,ideal_pressure_stiffness=4.,finite_environment_stiffness=exact,
        finite_difference_errors=errors,new_total_volume=newtotal,new_equilibrium=float(newroot),
        independent_minimizer=float(mini.x),
        assumptions='Fenv=-C log(Venv), C fixed; illustrative calibrated equation of state, not ARK background entropy.')

def equilibrium_sensitivity():
    # A two-coordinate nonlinear identity with independently prescribed geometry map.
    A=np.array([[3.,.4],[.4,2.]])
    Hvol=np.array([[.2,.1],[.1,.3]])
    v=np.array([-.6,.2]);P=.5;f=np.array([.1,-.05])
    state=lambda p:np.linalg.solve(A+p*Hvol,f-p*v)
    x=state(P);H=A+P*Hvol;vg=v+Hvol@x
    slope=-np.linalg.solve(H,vg);volume_slope=float(vg@slope)
    require(np.linalg.eigvalsh(H).min()>0 and volume_slope<0,'Local stability/response')
    errors=[]
    for h in [.04,.02,.01]:errors.append(float(np.linalg.norm((state(P+h)-state(P-h))/(2*h)-slope)))
    require(errors[0]>3.5*errors[1] and errors[1]>3.5*errors[2],'Sensitivity refinement')
    predicted=x+.01*slope;observed=state(P+.01)
    return dict(equilibrium=x.tolist(),pressure_sensitivity=slope.tolist(),dVdP=volume_slope,
       derivative_errors=errors,linearized_transfer_error=float(np.linalg.norm(observed-predicted)),
       scope='Generated-model intervention; H dx/dP=-grad V, not evidence of measured ARK response.')

def thermal_channel_is_distinct():
    q,r,T,P,C,T0=s.symbols('q r T P C T0',positive=True)
    F0=q*q+2*r*r+q*r/5-C*T*s.log(T/T0)-T*(q+2*r)
    Sth=-s.diff(F0,T);V=3-q+r/3
    G=F0+P*V
    for x in [q,r]:zero(s.diff(G,x,T)+s.diff(Sth,x))
    loadT=s.Matrix([s.diff(Sth,q),s.diff(Sth,r)])
    loadP=-s.Matrix([s.diff(V,q),s.diff(V,r)])
    matrix=loadT.row_join(loadP)
    require(matrix.det()!=0,'Independent control channels lost')
    return dict(thermal_pressure_load_matrix=str(matrix),rank=2,
        condition='No universal scalar combination of T,P follows; ordinary thermal entropy is not ARK Delta S_t.',
        thermal_status='Restricted derivative identity only; no thermometric calibration or added thermal research branch.')

def normalization_and_unknown_map():
    # Pressure work can fix a generalized contribution without identifying latent entropy.
    P=2e5;Vq=-3e-12;E0=2e-6
    drive=-P*Vq/E0;close(drive,.3)
    # Phi(s)=a*s: independent a is still needed to infer s from this drive.
    a1,a2=2.,5.;s1,s2=drive/a1,drive/a2
    close(a1*s1,a2*s2);require(s1!=s2,'Latent scale not exposed')
    return dict(pressure_Pa=P,volume_derivative_m3=Vq,energy_scale_J=E0,
        dimensionless_mode_drive=drive,distinct_latent_assignments=[s1,s2],
        statement='Known resolved mechanical contribution is not a measured absolute entropy or epsilon unless its entry map and normalization are fixed.')

def invalid_and_nonconstant_kappa():
    q,qref,E0,P0=s.symbols('q qref E0 P0',positive=True);k=1+q*q
    F=E0*k*q*q/2;Vq_required=-s.diff(F,q)/(P0*k*q*q)
    constant_k_shortcut=-E0/(P0*q)
    difference=s.simplify(Vq_required-constant_k_shortcut)
    require(difference!=0,'State-dependent k ignored')
    for qbad in [0.,-1.,float('nan')]:
        try:branches(qbad)
        except ValueError:pass
        else:raise AssertionError('Invalid state accepted')
    return dict(extra_volume_derivative=str(difference),
        source_warning='Chosen constant-k branches do not extend unchanged to responsive k(q,r). Full derivative of the stored-energy coefficient is required.',
        no_claims=['equation of state for ordinary water','gravity','universal clock shift','entropy calibration','empirical scalar identification'])

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    require(not args.output.exists(),'Refusing to overwrite output')
    tests=[('surface_pressure_and_mode_work',pressure_work_and_surface),
       ('source_projection_and_integrability',source_projection_and_integrability),
       ('quadratic_energy_square_pressure_compatibility',quadratic_pressure_compatibility),
       ('affine_volume_cubic_energy_alternative',affine_volume_alternative),
       ('matched_reference_distinct_continuation',matched_reference_distinct_transfer),
       ('independent_pressure_work_quadrature',energy_from_pressure_quadrature),
       ('pressure_reference_accounting',pressure_reference_accounting),
       ('finite_environment_response_curvature',finite_environment_curvature),
       ('finite_environment_equilibrium_and_refinement',finite_environment_minimum),
       ('coupled_identity_pressure_sensitivity',equilibrium_sensitivity),
       ('temperature_pressure_distinction',thermal_channel_is_distinct),
       ('normalized_load_not_absolute_entropy',normalization_and_unknown_map),
       ('invalid_states_and_variable_stiffness',invalid_and_nonconstant_kappa)]
    for name,fn in tests:
        try:CHECKS.append(dict(name=name,status='PASS',detail=fn()))
        except Exception as e:CHECKS.append(dict(name=name,status='FAIL',error=repr(e)))
    report=dict(study='IC-19',utc=datetime.now(timezone.utc).isoformat(),
       code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=s.__version__,
       scope='Conditional source-law compatibility and constructed checks only. No empirical calibration, full-core selection, detector work or independent review.',
       passed=sum(c['status']=='PASS' for c in CHECKS),total=len(CHECKS),checks=CHECKS)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2));raise SystemExit(report['passed']!=report['total'])
if __name__=='__main__':main()
