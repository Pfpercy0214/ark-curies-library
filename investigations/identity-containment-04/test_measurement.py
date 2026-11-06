#!/usr/bin/env python3
"""IC-04: conditional electromechanical observation tests; no experimental data."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import platform
from datetime import datetime, timezone
from pathlib import Path
import numpy as np
import sympy as sp


def recover(q: float, voltage: float, load: float, c0: float, ke: float, km: float) -> tuple[float, float, float]:
    """Recover log stretch, excess response and internal coordinate in this model.

    q is stored electrode charge, not total charge passed through a leaky circuit.
    load is the complete quasistatic external mechanical generalized load.
    """
    vals = (q, voltage, load, c0, ke, km)
    if not all(math.isfinite(float(x)) for x in vals):
        raise ValueError('Inputs must be finite.')
    if c0 <= 0 or ke <= 0 or km <= 0 or q == 0 or voltage == 0 or q * voltage <= 0:
        raise ValueError('Require positive coefficients and nonzero same-sign charge/voltage.')
    shape = (math.log(abs(q)) - math.log(abs(voltage)) - math.log(c0)) / 4
    memory = load + 2 * q * voltage - ke * shape
    return shape, memory, shape - memory / km


def run() -> dict:
    checks = []
    def check(name: str, condition: bool) -> None:
        if not bool(condition):
            raise AssertionError(name)
        checks.append({'name': name, 'passed': True})
    def zero(expr: sp.Expr) -> bool:
        return sp.simplify(expr) == 0

    s, z, Q = sp.symbols('s z Q', real=True)
    C0, Ke, Km, tr = sp.symbols('C0 Ke Km tr', positive=True)
    sd, Qd = sp.symbols('sd Qd', real=True)
    C = C0 * sp.exp(4*s)
    m = Km*(s-z)
    energy = Ke*s**2/2 + Km*(s-z)**2/2 + Q**2/(2*C)
    voltage = sp.diff(energy, Q)
    load = sp.diff(energy, s)
    zd = (s-z)/tr
    edot = sp.diff(energy,s)*sd + sp.diff(energy,z)*zd + sp.diff(energy,Q)*Qd
    check('work balance and nonnegative-dissipation identity', zero(load*sd + voltage*Qd - edot - m**2/(Km*tr)))
    check('voltage and required mechanical load derivatives', zero(voltage-Q/C) and zero(load-(Ke*s+m-2*Q*voltage)))
    check('frozen-state mixed-response reciprocity', zero(sp.diff(load,Q)-sp.diff(voltage,s)))
    U = sp.symbols('U', real=True)
    enthalpy = Ke*s**2/2 + Km*(s-z)**2/2 - C*U**2/2
    load_v = sp.diff(enthalpy,s)
    kq, kv = sp.diff(load,s), sp.diff(load_v,s)
    check('matched loads but different fixed-charge/fixed-voltage tangents',
          zero(load_v.subs(U,voltage)-load) and zero(kq-(Ke+Km+8*Q*voltage)) and zero(kv-(Ke+Km-8*C*U**2)))
    optical_electrical = sp.Matrix([s, voltage]).jacobian([s,z])
    electrical_load = sp.Matrix([voltage,load]).jacobian([s,z])
    check('electrical-only memory blindness and joint-channel local rank',
          zero(optical_electrical.det()) and zero(electrical_load.det()-4*Km*voltage))

    # Unit-consistent, illustrative coefficients; not material measurements.
    ke, km, t_r, c0, q0 = 2., 3., .8, 1., .2
    shape, z1, z2 = .1, 0., .1
    cap = c0*math.exp(4*shape)
    v0 = q0/cap
    memories = [km*(shape-zz) for zz in (z1,z2)]
    loads = [ke*shape+mm-2*q0*v0 for mm in memories]
    for zz, mm, ll in zip((z1,z2), memories, loads):
        got = recover(q0,v0,ll,c0,ke,km)
        if not np.allclose(got,(shape,mm,zz),atol=1e-13,rtol=0):
            raise AssertionError('state reconstruction')
    check('same geometry and voltage distinguishable through load history', abs(loads[0]-loads[1]-.3)<1e-13)
    check('charge reversal leaves mechanical state unchanged', np.allclose(recover(-q0,-v0,loads[0],c0,ke,km),recover(q0,v0,loads[0],c0,ke,km)))
    for invalid in [(0.,v0),(q0,0.),(q0,-v0)]:
        try:
            recover(*invalid,loads[0],c0,ke,km)
            raise AssertionError('invalid inversion accepted')
        except ValueError:
            pass
    check('zero and inconsistent-sign inputs rejected', True)
    check('zero excess memory does not imply zero restoring stiffness', memories[1]==0 and ke>0 and ke+8*q0*v0>0)
    check('adapted internal configuration remains visible on rapid unloading', memories[1]==0 and z2!=0 and abs(km*(0-z2)+.3)<1e-13)

    # Reconstruct only the initial memory; subsequent targets use an independent
    # RK4 integration of z. No later force target is used as a predictor input.
    s0, ramp, initial_memory, end = .03, .06, .12, 2.
    V0 = q0/(c0*math.exp(4*s0))
    L0 = ke*s0+initial_memory-2*q0*V0
    recovered_initial_memory = recover(q0,V0,L0,c0,ke,km)[1]
    def exact_load(t: float) -> float:
        ss = s0+ramp*t
        mm = recovered_initial_memory*math.exp(-t/t_r)+km*ramp*t_r*(-math.expm1(-t/t_r))
        qq = q0*(1+.1*math.sin(t))
        return ke*ss+mm-2*qq**2/(c0*math.exp(4*ss))
    errors = {}
    for steps in (32,64,128):
        dt, zz, err = end/steps, s0-initial_memory/km, 0.
        rhs = lambda tt, zv: (s0+ramp*tt-zv)/t_r
        for i in range(steps):
            tt=i*dt
            k1=rhs(tt,zz); k2=rhs(tt+dt/2,zz+dt*k1/2)
            k3=rhs(tt+dt/2,zz+dt*k2/2); k4=rhs(tt+dt,zz+dt*k3)
            zz += dt*(k1+2*k2+2*k3+k4)/6
            tn=(i+1)*dt; ss=s0+ramp*tn; qq=q0*(1+.1*math.sin(tn))
            target=ke*ss+km*(ss-zz)-2*qq**2/(c0*math.exp(4*ss))
            err=max(err,abs(target-exact_load(tn)))
        errors[str(steps)]=err
    check('initial-state reconstruction transfers to a new imposed trajectory', errors['128']<1e-9 and errors['32']>errors['64']>errors['128'])

    # An omitted permittivity change is misread as shape; baseline load offsets
    # are misread as memory. These are positive controls for false inference.
    drift=1.01
    drifted_v=q0/(cap*drift)
    actual_m=.3
    actual_l=ke*shape+actual_m-2*q0*drifted_v
    biased = recover(q0,drifted_v,actual_l,c0,ke,km)
    expected_bias=math.log(drift)/4
    check('permittivity-drift alias is detected, not called identity change', abs((biased[0]-shape)-expected_bias)<1e-14 and abs((biased[1]-actual_m)+ke*expected_bias)<1e-14)
    offset=.05
    biased_load=recover(q0,v0,loads[0]+offset,c0,ke,km)
    check('unknown load offset aliases retained response', abs(biased_load[1]-memories[0]-offset)<1e-13)

    # Error propagation from actual measured channels retains their covariance.
    L, VV, CC, EE, QQ=sp.symbols('L VV CC EE QQ', real=True, positive=True)
    shape_hat=sp.log(QQ/(CC*VV))/4
    memory_hat=L+2*QQ*VV-EE*shape_hat
    obs=sp.Matrix([L,QQ,VV,CC,EE])
    jac=sp.Matrix([shape_hat,memory_hat]).jacobian(obs)
    expected=sp.Matrix([[0,1/(4*QQ),-1/(4*VV),-1/(4*CC),0],
                        [1,2*VV-EE/(4*QQ),2*QQ+EE/(4*VV),EE/(4*CC),-shape_hat]])
    check('joint measurement uncertainty Jacobian includes shared channels', all(zero(x) for x in jac-expected))
    jn=np.array(jac.subs({L:loads[0],QQ:q0,VV:v0,CC:c0,EE:ke})).astype(float)
    sigma=np.diag([1e-6,1e-8,1e-8,1e-6,1e-6]); sigma[1,2]=sigma[2,1]=4e-9
    cov=jn@sigma@jn.T
    check('correlated covariance remains positive and changes uncertainty', np.min(np.linalg.eigvalsh(cov))>=0 and not np.allclose(cov,jn@np.diag(np.diag(sigma))@jn.T,rtol=1e-6,atol=1e-14))

    # New coordinate does not preserve response or stiffness by relabeling.
    f=sp.Rational(1,5)+sp.Rational(4,5)*s+sp.Rational(3,10)*s**2
    fp=sp.diff(f,s)
    tau_coord=load/fp
    k_coord=(kq*fp-load*sp.diff(fp,s))/fp**3
    check('coordinate transformation retains work and preload term', zero(tau_coord*fp-load) and zero(sp.diff(tau_coord,s)/fp-k_coord))
    sample={s:.1,z:0,Q:q0,C0:c0,Ke:ke,Km:km}
    changed_product=float((f*k_coord-s*kq).subs(sample))
    check('geometry response cannot be relabeled clock product unchanged', abs(changed_product)>1e-3)

    return {'status':'PASS', 'groups_passed':len(checks), 'groups':checks,
            'scope':'Exact/constructed comparator verification only; no experimental fit, ARK scalar identification, clock prediction, independent reviewer, or charge-origin derivation.',
            'example':{'shape':shape,'capacitance':cap,'voltage':v0,'memories':memories,'loads':loads,
                       'trajectory_max_absolute_error_J':errors,'one_percent_permittivity_logshape_bias':expected_bias,
                       'coordinate_product_difference':changed_product},
            'runtime':{'utc':datetime.now(timezone.utc).isoformat(),'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('test-results.json'))
    args=parser.parse_args()
    report=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))
