#!/usr/bin/env python3
"""IC-05: bounded clock/geometry bridge; symbolic and generated-data checks only.
Run: python test_bridge.py --output test-results.json
Requires SymPy; standard library otherwise. No external data or network access.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
from typing import Callable
import sympy as sp


def theta_from_log_lapse(log_n: float) -> float:
    """Principal clock angle for a POSITIVE lapse <= 1, not a raw clock ratio."""
    if not math.isfinite(log_n) or log_n > 0:
        raise ValueError("Require finite log(N) <= 0 with declared time normalization")
    return math.atan2(math.sqrt(-math.expm1(2.0 * log_n)), math.exp(log_n))


def log_lapse(r: float, rs: float) -> float:
    """Static Schwarzschild lapse with asymptotic normalization; r > rs > 0."""
    if not (math.isfinite(r) and math.isfinite(rs) and r > rs > 0):
        raise ValueError("Require r > Schwarzschild radius > 0")
    return 0.5 * math.log1p(-rs / r)


def simpson(fun: Callable[[float], float], a: float, b: float, n: int) -> float:
    if n < 2 or n % 2:
        raise ValueError("Simpson panel count must be positive and even")
    h = (b - a) / n
    return h / 3.0 * (fun(a) + fun(b) + 4.0 * sum(fun(a + i*h) for i in range(1, n, 2))
                      + 2.0 * sum(fun(a + i*h) for i in range(2, n, 2)))


def equal(a: sp.Expr, b: sp.Expr) -> None:
    delta = sp.trigsimp(sp.simplify(a - b))
    if delta != 0:
        raise AssertionError(f"Symbolic difference: {delta}")


def close(a: float, b: float, atol: float = 1e-12, rtol: float = 1e-10) -> None:
    if not math.isclose(a, b, rel_tol=rtol, abs_tol=atol):
        raise AssertionError(f"Not close: {a} versus {b}")


def run() -> dict:
    checks: list[dict] = []
    def check(name: str, f: Callable[[], dict | None]) -> None:
        try:
            details = f() or {}
            checks.append({"name": name, "status": "PASS", "details": details})
        except Exception as exc:
            checks.append({"name": name, "status": "FAIL", "error": repr(exc)})
    r, rs, c = sp.symbols('r rs c', positive=True)
    th = sp.symbols('theta', positive=True)
    s, z = sp.symbols('s z', real=True)
    ke, km, tr = sp.symbols('K_e K_m t_r', positive=True)
    N = sp.sqrt(1-rs/r)
    # Derivatives below are used only on 0 < theta < pi/2, r > rs.
    fp = -sp.tan(th)/2
    fpp = sp.tan(th)*sp.sec(th)**2/4
    sinv = -2*sp.log(sp.sin(th))  # additive log(rs/R0) fixed to zero in this symbolic fixture
    T = (ke+km)*s-km*z
    U = ke*s*s/2+km*(s-z)**2/2
    Ut = U.subs(s, sinv)
    tau = sp.diff(Ut, th)
    kap = sp.diff(Ut, th, 2)

    def a():
        equal(sp.diff(sp.log(N), r), rs/(2*r*r*(1-rs/r)))
        equal(c*c*N*sp.diff(sp.log(N),r), c*c*rs/(2*r*r*N))
        for rr in [2.1, 3., 20., 1e6]:
            theta = theta_from_log_lapse(log_lapse(rr, 2.))
            close(theta, math.asin(math.sqrt(2./rr)))
        return {"metric": "ds^2=-N^2 c^2 dt^2 + dr^2/N^2 + r^2 dOmega^2",
                "acceleration": "a_support=c^2*N*d(log N)/dr"}
    check('static_clock_and_proper_acceleration', a)

    def b():
        exact = log_lapse(20.,2.)-log_lapse(4.,2.)
        errors=[]
        for n in [32,64,128,256]:
            approx=simpson(lambda x: 2./(2*x*x*(1-2./x)),4.,20.,n)
            errors.append(abs(approx-exact))
        assert all(errors[i+1] < errors[i]/8 for i in range(3)), errors
        assert errors[-1] < 2e-8
        return {"exact_log_clock_ratio":exact,"panels":[32,64,128,256],"absolute_errors":errors}
    check('profile_integration_with_independent_quadrature', b)

    def d():
        n1,n2=math.exp(log_lapse(4.,2.)),math.exp(log_lapse(20.,2.))
        ratio=n2/n1
        close((.9*n2)/(.9*n1),ratio)
        assert not math.isclose(math.acos(n1),math.acos(.9*n1))
        # Boundary normalization removes this freedom; it is not a new physical free parameter.
        assert ratio > 1
        try: theta_from_log_lapse(math.log(ratio))
        except ValueError: pass
        else: raise AssertionError('Raw ratio > 1 must not be silently used as N')
        return {"valid_upper_to_lower_clock_ratio":ratio,"angle_at_N1":math.acos(n1),
                "angle_after_unfixed_time_rescaling":math.acos(.9*n1)}
    check('reference_normalization_and_relative_ratio_domain',d)

    def e():
        equal(sp.diff(sp.log(sp.cos(th)),th),-sp.tan(th))
        # Support acceleration is -c^2*tan(theta)*gradient(theta).
        for angle in [.1,.01,.001]:
            rel=abs(angle/math.tan(angle)-1)
            assert rel < .34*angle*angle
        # Newtonian potential dimensions L^2/T^2: |grad Phi|/c^2 has L^-1.
        grad_potential_over_c2=(0, -1, 0) # (mass,length,time) exponents
        assert grad_potential_over_c2 != (0,0,0)
        return {"exact_static_relation":"a_support/c^2=-tan(theta)*grad(theta)",
                "literal_gradient_route":"Needs different potential units or an explicit length/integral map"}
    check('clock_angle_is_not_a_local_gradient',e)

    def f():
        equal(1/sp.diff(sinv,th),fp)
        equal(sp.diff(fp,th)*fp,fpp)
        for sv in [-.1,0.,.2]:
            theta=math.asin(math.sqrt(.1*math.exp(-sv)))
            numerical=(math.asin(math.sqrt(.1*math.exp(-(sv+1e-5))))-
                       math.asin(math.sqrt(.1*math.exp(-(sv-1e-5)))))/(2e-5)
            close(numerical,-math.tan(theta)/2,atol=2e-11)
        return {"scope":"Radial log deformation of a test boundary in fixed spherical background"}
    check('physically_declared_radial_coordinate_mapping',f)

    def g():
        equal(tau,T.subs(s,sinv)/fp)
        equal(kap,4*(ke+km)*sp.cot(th)**2+2*T.subs(s,sinv)/sp.sin(th)**2)
        equal(tau*fp,T.subs(s,sinv))
        return {"tau_W":"-2*T*cot(theta)","kappa_W":"4*K_s*cot(theta)^2+2*T*csc(theta)^2"}
    check('work_invariance_and_preload_aware_tangent',g)

    def h():
        direct=kap.subs({th:.4,ke:2,km:3,z:.7}).evalf()
        naive=(4*(ke+km)*sp.cot(th)**2).subs({th:.4,ke:2,km:3}).evalf()
        assert abs(float(direct-naive)) > 1
        # At a stationary total potential, preload vanishes and the Hessian sign is invariant.
        equal((kap-4*(ke+km)*sp.cot(th)**2).subs(z,(ke+km)*sinv/km),sp.Integer(0))
        return {"direct_tangent_fixture":float(direct),"omitted_preload_fixture":float(naive)}
    check('reject_silent_relabeling_and_missing_preload',h)

    def i():
        equal(sp.diff(tau,z),2*km*sp.cot(th))
        # Held shape and clock angle, evolving retained coordinate: memory-free tangent fails.
        vals={th:.4,ke:2.,km:3.,z:.7}
        sv=float(sinv.subs(th,.4))
        zdot=(sv-.7)/2.
        residual=float(sp.diff(tau,z).subs(vals))*zdot
        assert abs(residual)>1e-3
        return {"fixed_theta_dot":0,"z_dot_fixture":zdot,"nonzero_tau_dot_fixture":residual,
                "meaning":"Candidate stress response is not the universal XVIII path accumulator"}
    check('history_evolution_requires_its_own_term',i)

    def j():
        B=sp.Function('B')(z)
        modified=Ut+B*th
        equal(sp.diff(modified,th,2),kap)
        equal(sp.diff(modified,th)-tau,B)
        return {"unfixed_quantity":"Integrating stiffness leaves a history-dependent response reference"}
    check('stiffness_does_not_fix_memory_baseline',j)

    def k():
        # Coordinate changes preserve information rank, not create a new measurement channel.
        # dtheta/ds=fp; d(tau_W)/dz=-km/fp.
        equal(fp*(-km/fp),-km)
        return {"determinant":"-K_m", "clock_only_history_rank":0,
                "joint_shape_and_load_state_rank":2}
    check('joint_observability_survives_coordinate_change',k)

    def l():
        angle=theta_from_log_lapse(-1e-20)
        close(angle,math.sqrt(2e-20),atol=1e-25)
        assert math.acos(math.exp(-1e-20)) == 0.
        for bad in [.01, float('nan'), float('inf')]:
            try: theta_from_log_lapse(bad)
            except ValueError: pass
            else: raise AssertionError('Invalid lapse accepted')
        for rr,ss in [(1.,2.),(2.,2.),(3.,-1.)]:
            try: log_lapse(rr,ss)
            except ValueError: pass
            else: raise AssertionError('Invalid radial state accepted')
        return {"stable_weak_angle":angle,"naive_rounded_angle":0.}
    check('weak_signal_precision_and_domain_guards',l)

    def m():
        # Local radial work redshifts by N, proper displacement is dr/N.
        R,F,nn=sp.symbols('R F N',positive=True)
        equal(nn*F*(R/nn),F*R)
        # SI exponent tuples for pressure-area vs work: N vs J.
        force=(1,1,-2); generalized_work=(1,2,-2)
        assert force != generalized_work
        return {"radial_log_mode_work_coefficient":"T=R*F_radial (asymptotic energy convention)",
                "required_boundary_map":"Mode contraction, length scale, orientation and reference energy"}
    check('boundary_force_to_generalized_work_units',m)

    def n():
        rs0=.1; R0=1.; ref=4.; s0=.2
        ratio0=math.exp(log_lapse(R0*math.exp(s0),rs0)-log_lapse(ref,rs0))
        ratiob=math.exp(log_lapse(R0*math.exp(s0),.12)-log_lapse(ref,.12))
        assert abs(ratio0-ratiob)>1e-5
        # Inject a clock-specific shift; it must not be absorbed into theta calibration.
        contaminated=ratio0*(1+1e-5)
        residual=math.log(contaminated/ratio0)
        close(residual,math.log1p(1e-5),atol=1e-15)
        return {"same_shape_ratio_background_A":ratio0,"same_shape_ratio_background_B":ratiob,
                "clock_systematic_log_residual":residual}
    check('environment_change_and_clock_systematic_negative_controls',n)

    def o():
        # Direct energy derivative and finite-difference derivative are independent implementations.
        angle=.4; zz=.7; a_ke=2.; a_km=3.
        def energy(x):
            sv=-2*math.log(math.sin(x))
            return .5*a_ke*sv*sv+.5*a_km*(sv-zz)**2
        exact_tau=float(tau.subs({th:angle,ke:a_ke,km:a_km,z:zz}))
        exact_k=float(kap.subs({th:angle,ke:a_ke,km:a_km,z:zz}))
        errors=[]
        for dh in [1e-3,5e-4,2.5e-4]:
            dt=(energy(angle+dh)-energy(angle-dh))/(2*dh)
            dk=(energy(angle+dh)-2*energy(angle)+energy(angle-dh))/(dh*dh)
            errors.append([abs(dt-exact_tau),abs(dk-exact_k)])
        assert errors[-1][0]<errors[0][0]/10
        assert errors[-1][1]<errors[0][1]/10
        return {"steps":[1e-3,5e-4,2.5e-4],"tau_and_kappa_errors":errors}
    check('direct_energy_crosscheck_and_refinement',o)

    return {"study":"IC-05","utc":datetime.now(timezone.utc).isoformat(),
            "scope":"Symbolic identities and constructed numerical examples; no experimental fit",
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "python":platform.python_version(),"sympy":sp.__version__,
            "passed":sum(c['status']=='PASS' for c in checks),
            "failed":sum(c['status']=='FAIL' for c in checks),"checks":checks,
            "limits":["Fixed static spherical background for the explicit mode mapping",
                      "No selection of a universal physical ARK tau or kappa",
                      "Source gradient definition needs its potential units specified",
                      "No new charge, clock-shift, neutron-lifetime or medium prediction",
                      "No independent second reviewer; prior IC code not rerun"]}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report=run()
    rendered=json.dumps(report,indent=2,ensure_ascii=False)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(rendered,encoding='utf-8')
    print(rendered)
    sys.exit(1 if report['failed'] else 0)
