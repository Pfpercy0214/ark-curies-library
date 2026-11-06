#!/usr/bin/env python3
"""IC-17: energy/response compatibility, not empirical validation of ARK.
Read README.md and source-map.json for source versus candidate distinctions.
Run: python check_energy_map.py --output new-results.json
Requires numpy, scipy, sympy. Does not read experimental data or overwrite output.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import expm
import sympy as sp

CHECKS: list[dict] = []
def require(ok: bool, msg: str) -> None:
    if not bool(ok):
        raise AssertionError(msg)
def zero(expr) -> None:
    require(sp.simplify(expr) == 0, str(sp.simplify(expr)))
def near(a, b, tol=1e-10) -> None:
    require(np.allclose(a, b, atol=tol, rtol=tol), f'{a} != {b}')


def variable_energy_coefficient():
    q,q0=sp.symbols('q q0', positive=True)
    K=sp.Function('K')(q);d=q-q0
    U=K*d**2/2
    zero(sp.diff(U,q)-(K*d+sp.diff(K,q)*d**2/2))
    zero(sp.diff(U,q,2)-(K+2*d*sp.diff(K,q)+d**2*sp.diff(K,q,2)/2))
    literal=sp.simplify(U.subs({K:1/q,q0:0}))
    zero(literal-q/2);zero(sp.diff(literal,q,2))
    return {'quadratic_coefficient_tangent_relation':'Kt=KE+2*Delta*KE_q+Delta^2*KE_qq/2',
            'restricted_pointwise_substitution':'K=1/q and flat-reference U=K*q^2/2 give U=q/2, U_qq=0',
            'interpretation':'A conflict only if K is also claimed to be this tangent curvature in the same regime. It is not a whole-framework refutation.'}


def reconstruct_from_tangent():
    q,q0,u,r,T0,U0=sp.symbols('q q0 u r T0 U0',real=True)
    K=2+u*u+r*r/3
    T=T0+sp.integrate(K,(u,q0,q))
    U=U0+T0*(q-q0)+sp.integrate((q-u)*K,(u,q0,q))
    zero(sp.diff(U,q)-T);zero(sp.diff(T,q)-K.subs(u,q))
    zero(U.subs(q,q0)-U0);zero(T.subs(q,q0)-T0)
    checks=[]
    for target in [-.5,.2,1.7]:
        ref=.4; rr=.3; t0=.7; u0=.2
        k=lambda z:2+z*z+rr*rr/3
        direct=u0+t0*(target-ref)+quad(lambda z:(target-z)*k(z),ref,target)[0]
        nested=u0+quad(lambda z:t0+quad(k,ref,z)[0],ref,target)[0]
        near(direct,nested)
        checks.append({'q':target,'energy':direct,'nested_integral_error':abs(direct-nested)})
    return {'constructive_formula':'U=U0(r,E)+T0(r,E)*Delta+integral_q0^q (q-u)Kt(u,r,E)du',
            'numerical_integrations':checks,'conditions':'fixed r,E and fixed reference q0; reversible energy derivative, not total dissipative measured force'}


def log_branch_and_means():
    q,q0=sp.symbols('q q0',positive=True)
    U=q*sp.log(q/q0)-q+q0;T=sp.log(q/q0)
    zero(sp.diff(U,q)-T);zero(sp.diff(T,q)-1/q)
    Ksec=T/(q-q0);Kenergy=2*U/(q-q0)**2
    near(float(sp.limit(Ksec,q,q0).subs(q0,1)),1)
    near(float(sp.limit(Kenergy,q,q0).subs(q0,1)),1)
    x=2.;ref=1.;d=x-ref
    ks=quad(lambda s:1/(ref+s*d),0,1)[0]
    ke=2*quad(lambda s:(1-s)/(ref+s*d),0,1)[0]
    near(ks,np.log(2));near(ke,2*(2*np.log(2)-1))
    require(abs(ke-ks)>.05 and abs(ks-1/x)>.1,'Nonlinear responses accidentally equated')
    for x0 in [.3,.7,1.,2.,5.]:require(float(U.subs({q:x0,q0:1}))>=-1e-14,'Convex reference energy')
    return {'chosen_reference':'q0=1,T0=0,U0=0, dimensionless candidate',
            'q':2,'tangent':.5,'secant':ks,'energy_coefficient':ke,
            'energy':'q*log(q/q0)-q+q0',
            'scope':'Conditional work-conjugate completion of the restricted tangent law; not a replacement of the archived quadratic expression.'}


def reference_functions_are_not_optional():
    q,r,e=sp.symbols('q r e',real=True)
    U1=q*q/2+r*r/2+e*e/2
    U2=U1+3*r*r+2*e
    zero(sp.diff(U1,q)-sp.diff(U2,q));zero(sp.diff(U1,q,2)-sp.diff(U2,q,2))
    zero(sp.diff(U2,r)-sp.diff(U1,r)-6*r)
    U3=U1+r*q
    zero(sp.diff(U3,q,2)-sp.diff(U1,q,2))
    require(sp.diff(U3,q)!=sp.diff(U1,q),'Reference force lost')
    return {'same_geometry_force_and_tangent':'U1 and U1+3r^2+2E',
            'different_retained_force':'difference=6r',
            'different_environment_work':'difference in U_E=2',
            'consequence':'A tangent surface alone leaves two reference functions of other states, not just two universal numbers.'}


def reversible_integrability():
    q,r=sp.symbols('q r',real=True)
    T=2*q+sp.Rational(3,10)*r
    A=sp.Rational(3,10)*q+2*r
    zero(sp.diff(T,r)-sp.diff(A,q))
    wrong=sp.Rational(1,2)*q+2*r
    loop=sp.integrate(T.subs(r,0),(q,0,1))+sp.integrate(wrong.subs(q,1),(r,0,1))+sp.integrate(T.subs(r,1),(q,1,0))+sp.integrate(wrong.subs(q,0),(r,1,0))
    zero(loop-sp.Rational(1,5))
    return {'compatible_mixed_partials':True,'incompatible_rectangle_work':float(loop),
            'scope':'Necessary local exactness test for a smooth reversible potential in complete chosen state; projected hysteretic work need not vanish.'}


def mode_reduction():
    G,a,L=2.,3.,2.;rows=[]
    ks=[]
    for n in [1,2,3]:
        wave=n*np.pi/L
        h=lambda x:np.sin(wave*x)
        hx=lambda x:wave*np.cos(wave*x)
        numerical=quad(lambda x:G*hx(x)**2+a*h(x)**2,0,L,epsabs=1e-11)[0]
        analytic=L/2*(a+G*wave*wave)
        near(numerical,analytic);ks.append(numerical)
        amp=.12
        energy=quad(lambda x:.5*G*(amp*hx(x))**2+.5*a*(amp*h(x))**2,0,L)[0]
        near(energy,.5*numerical*amp*amp)
        rows.append({'mode':n,'mode_stiffness':numerical,'energy_at_amplitude_0p12':energy})
    # Off-diagonal terms vanish for this homogeneous, fixed-boundary choice.
    cross=quad(lambda x:G*(np.pi/L*np.cos(np.pi*x/L))*(2*np.pi/L*np.cos(2*np.pi*x/L))+a*np.sin(np.pi*x/L)*np.sin(2*np.pi*x/L),0,L)[0]
    near(cross,0)
    recovered=np.linalg.solve(np.array([[L/2,(L/2)*(n*np.pi/L)**2] for n in [1,2]]),ks[:2])
    near(recovered,[a,G]);predict=L/2*(recovered[0]+recovered[1]*(3*np.pi/L)**2);near(predict,ks[2])
    scale=2.7;near(.5*(ks[0]*scale**2)*(.12/scale)**2,rows[0]['energy_at_amplitude_0p12'])
    return {'field_inputs':{'G':G,'a':a,'length':L,'cross_section':1},'modes':rows,
            'offdiagonal':cross,'two_mode_generated_recovery':recovered.tolist(),'third_mode_generated_prediction':predict,
            'scope':'Chosen dimensionless homogeneous modes. Independently specified spatial shape is required; no domain-specific fitting or physical ARK assignment.'}


def spatial_shape_is_not_whole_identity():
    G,a=2.,3.;L=2.
    # Both scalar-field profiles have q=0 at both ends, but different bulk energy/tractions.
    rows=[]
    for A in [.1,.2]:
        energy=A*A*L/4*(a+G*(np.pi/L)**2)
        flux0=-G*A*np.pi/L
        rows.append({'amplitude':A,'boundary_values':[0.,0.],'energy':energy,'outward_field_flux_at_left':flux0})
    require(rows[0]['energy']!=rows[1]['energy'],'Unexpected uniqueness from boundary values')
    return {'profiles':rows,'scope':'Boundary values alone do not specify arbitrary interior profiles. This does not deny uniqueness for a well-posed boundary-value equation with sufficient data.'}


def boundary_mode_work():
    # Outward applied traction p*n. Positive inward environmental pressure changes sign.
    p,R,R0=2.,3.,1.2
    u,w=np.polynomial.legendre.leggauss(48);phi=2*np.pi*np.arange(96)/96
    sint=np.sqrt(1-u*u)
    nx=sint[:,None]*np.cos(phi);ny=sint[:,None]*np.sin(phi);nz=np.broadcast_to(u[:,None],nx.shape)
    weights=R*R*w[:,None]*np.ones((1,len(phi)))*(2*np.pi/len(phi))
    net=np.array([np.sum(weights*p*n) for n in [nx,ny,nz]])
    load=np.sum(weights*p*R0*(nx*nx+ny*ny+nz*nz))
    near(net,[0,0,0],1e-10);near(load,4*np.pi*p*R*R*R0)
    theta=R/R0-1;h=1e-5
    volume=lambda t:4*np.pi/3*(R0*(1+t))**3
    fd=p*(volume(theta+h)-volume(theta-h))/(2*h)
    near(fd,load,1e-9)
    return {'net_force':net.tolist(),'dimensionless_radial_coordinate_load':float(load),
            'virtual_work_derivative_error':abs(fd-load),
            'scope':'Outward traction; a dimensionless radial mode yields an energy-like load. It is not automatically the scalar stress integral in XXV A.3.'}


def shape_stress_and_transport():
    p=np.array([.3,-.2,.4]);G=2.4;v=.7
    H=np.array([[.2,.1,-.05],[.07,-.15,.02],[.03,-.04,.1]])
    w=.5*G*np.dot(p,p)+v
    stress=w*np.eye(3)-G*np.outer(p,p)
    exact=np.sum(stress*H)
    def U(e):
        F=np.eye(3)+e*H
        pp=np.linalg.solve(F.T,p)
        return np.linalg.det(F)*(.5*G*np.dot(pp,pp)+v)
    errors=[]
    for e in [.08,.04,.02]:errors.append(abs((U(e)-U(-e))/(2*e)-exact))
    require(errors[0]>3.5*errors[1] and errors[1]>3.5*errors[2],'Affine shape derivative refinement')
    n,V=sp.symbols('n V',positive=True);f=sp.Function('f')
    N=sp.symbols('N',positive=True)
    conserved_pressure=-sp.diff(V*f(N/V),V)
    zero(conserved_pressure-(N/V*sp.diff(f(n),n).subs(n,N/V)-f(N/V)))
    label_pressure=-f(n)
    # Same current-volume function, different transport/held-fixed contracts.
    fn=lambda z:.5*z*z
    n0=2.;p_density=n0*n0-fn(n0);p_label=-fn(n0)
    require(p_density==2 and p_label==-2,'Transport-rule distinction')
    return {'advected_scalar_shape_stress':'w*I-G*grad(q) tensor grad(q)',
            'affine_derivative_errors':errors,'density_pressure':p_density,'fixed_label_pressure':p_label,
            'scope':'Alternative assumed advection rules, not interchangeable physical media. A full Cauchy stress requires the actual material transport/metric/deformation coupling.'}


def energy_density_baseline():
    q,V,C=sp.symbols('q V C',real=True)
    f=q*q/2
    zero(sp.diff(f+C,q)-sp.diff(f,q))
    zero(sp.diff(V*(f+C),V)-sp.diff(V*f,V)-C)
    pin,pout=sp.symbols('pin pout')
    zero((pin+C)-(pout+C)-(pin-pout))
    return {'fixed_domain_field_equation':'unchanged by spatially constant density shift',
            'variable_volume_energy_derivative_shift':'C',
            'common_background_pressure_difference':'unchanged',
            'scope':'Volume coupling and matching exterior reference must be declared. Does not make arbitrary energy-zero choices into new measured pressures.'}


def retained_state_to_response_chart():
    H=np.array([[3.,.4],[.4,2.]])
    b,L=.6,.3;M=np.array([[1.,b],[b,b*b+L]])
    J=np.array([[1.,0.],[3.,.4]]);Ji=np.linalg.inv(J)
    Hy=Ji.T@H@Ji;My=J@M@J.T
    Ax=-M@H;Ay=-My@Hy
    near(Ay,J@Ax@Ji)
    x0=np.array([.15,-.08]);y0=J@x0;rows=[]
    for t in [0.,.2,1.,3.]:
        x=expm(Ax*t)@x0;y=expm(Ay*t)@y0
        near(y,J@x);near(.5*x@H@x,.5*y@Hy@y)
        near(Hy@y,Ji.T@H@x)
        rows.append({'time':t,'transformation_error':float(np.max(np.abs(y-J@x)))})
    wrong=expm(-M@Hy)@y0;right=expm(Ay)@y0
    require(np.max(np.abs(wrong-right))>1e-3,'Naive variable substitution unexpectedly equivalent')
    q,r=sp.symbols('q r',real=True);h=sp.Function('h')(r)
    # Assuming an independent retained coordinate r is identically U_q is restrictive.
    U=q*r+h;H_bad=sp.hessian(U,(q,r));zero(H_bad.det()+1)
    return {'coordinate_map':'(q,r) -> (q,T=3q+0.4r)',
            'transformed_mobility':My.tolist(),'trajectory_checks':rows,
            'naive_untransformed_mobility_error':float(np.max(np.abs(wrong-right))),
            'global_assumption_T_equals_r_local_hessian_determinant':-1,
            'scope':'Constant-Jacobian overdamped reduction of IC16. Inertial/state-dependent transformations require their own chain rules. Singular T_r prevents this chart.'}


def full_tension_derivative():
    q,r,e,dq,dr,de=sp.symbols('q r e dq dr de',real=True)
    U=(1+r*r+e)*q*q/2+r*r/2
    T=sp.diff(U,q);Kt=sp.diff(T,q)
    total=sp.diff(T,q)*dq+sp.diff(T,r)*dr+sp.diff(T,e)*de
    zero(total-(Kt*dq+2*r*q*dr+q*de))
    require(total.subs({q:1,r:1,e:1,dq:0,dr:.1,de:0})!=0,'History-only change lost')
    return {'law':'T_dot=Kt*q_dot+T_r*r_dot+T_E*E_dot',
            'scope':'Fixed-coordinate local reversible energy derivative; along a physical path memory/environment contribute even with q fixed.'}


def physical_scales():
    # Dimension vectors (mass,length,time), angle dimensionless but normalization retained.
    energy=np.array([1,2,-2]);length=np.array([0,1,0]);time=np.array([0,0,1])
    force=energy-length;stress=energy-3*length;gradient_coefficient=energy-length
    near(stress+2*length+length,energy)
    require(not np.array_equal(gradient_coefficient,energy),'Global/gradient stiffness units collapsed')
    require(not np.array_equal(energy,energy+time),'Actionlike tau not energylike load')
    H=np.array([[2.,.2],[.2,1.]])
    M=np.array([[1.,0],[0,.5]]);lam=7.
    near(-M@H,-(M/lam)@(lam*H))
    return {'global_angle_stiffness':'E0/theta0^2',
            'gradient_coefficient_3D':'E0/(L0*theta0^2)',
            'local_energy_density_curvature':'E0/(L0^3*theta0^2)',
            'work_conjugate_load':'E0/theta0',
            'kinetic_scale_ambiguity':'U -> lambda U, M -> M/lambda preserves overdamped trajectories but rescales forces',
            'consequence':'Independent energy/stress and geometry anchors required; normalization is explicit, not forbidden calibration.'}


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True);args=parser.parse_args()
    require(not args.output.exists(),'Refusing to overwrite output')
    tests=[('variable_quadratic_coefficient',variable_energy_coefficient),
           ('constructive_energy_from_tangent',reconstruct_from_tangent),
           ('normalized_log_branch_and_three_responses',log_branch_and_means),
           ('reference_function_nonidentifiability',reference_functions_are_not_optional),
           ('reversible_integrability',reversible_integrability),
           ('field_to_mode_energy_bridge',mode_reduction),
           ('boundary_values_vs_interior_state',spatial_shape_is_not_whole_identity),
           ('boundary_traction_mode_projection',boundary_mode_work),
           ('deformation_stress_and_transport_contract',shape_stress_and_transport),
           ('energy_density_and_exterior_baseline',energy_density_baseline),
           ('retained_state_vs_response_coordinate',retained_state_to_response_chart),
           ('complete_response_differential',full_tension_derivative),
           ('units_and_absolute_energy_anchor',physical_scales)]
    for name,fn in tests:
        try:CHECKS.append({'name':name,'status':'PASS','detail':fn()})
        except Exception as error:CHECKS.append({'name':name,'status':'FAIL','error':repr(error)})
    result={'study':'IC-17','utc':datetime.now(timezone.utc).isoformat(),
            'source_parent':'fd5663bf5cae6f8c99b63b63fdc349ca99ee07ae',
            'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__,
            'scope':'Conditional source compatibility and generated mathematical checks; no empirical fit, physical ARK identification, new detector analysis or independent reviewer.',
            'passed':sum(t['status']=='PASS' for t in CHECKS),'total':len(CHECKS),'checks':CHECKS}
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
    raise SystemExit(0 if result['passed']==result['total'] else 1)
if __name__=='__main__':main()
