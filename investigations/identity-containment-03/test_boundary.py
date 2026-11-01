#!/usr/bin/env python3
"""IC-03: conventional boundary-work and retained-state benchmarks.
No experimental data; no identification of s/T/K/z with ARK scalars.
Run: python test_boundary.py [--output test-results.json]
Dependencies: sympy, numpy. Each named check must pass; failures exit nonzero.
"""
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


def run_checks() -> dict:
    checks: list[dict] = []
    def check(name: str, ok: bool, detail: str = "") -> None:
        passed = bool(ok)
        checks.append({"name": name, "passed": passed, "detail": detail})
        if not passed:
            raise AssertionError(name + ": " + detail)
    def zero(name: str, expression: sp.Expr) -> None:
        residual = sp.simplify(expression)
        check(name, residual == 0, str(residual))

    # Conducting spherical boundary in vacuum; Q is signed, R is positive.
    R, R0, eps, V = sp.symbols("R R0 eps V", positive=True)
    Q = sp.symbols("Q", real=True)
    s = sp.symbols("s", positive=True)
    E = Q / (4 * sp.pi * eps * R**2)
    pressure = eps * E**2 / 2
    U = Q**2 / (8 * sp.pi * eps * R)
    area = 4 * sp.pi * R**2
    F = pressure * area
    zero("spherical pressure and fixed-charge virtual work", F + sp.diff(U, R))
    zero("charge reversal leaves pressure unchanged", pressure.subs(Q, -Q) - pressure)
    zero("charge reversal reverses electric field", E.subs(Q, -Q) + E)
    zero("signed electric flux recovers charge", eps * E * area - Q)

    a, b = sp.symbols("a b", real=True)
    normal = [sp.sin(a)*sp.cos(b), sp.sin(a)*sp.sin(b), sp.cos(a)]
    for i, component in enumerate(normal):
        integral = sp.integrate(component * sp.sin(a), (b, 0, 2*sp.pi), (a, 0, sp.pi))
        zero(f"uniform pressure has zero vector resultant component {i}", integral)
    Ts = sp.simplify((F * R0).subs(R, R0*s))
    zero("nonzero dilation load equals mode-weighted work", Ts + sp.diff(U.subs(R, R0*s), s))
    check("dilation load is positive despite zero resultant", Ts.subs(Q, 1).is_positive)

    # Source-connected environment: use U-VQ, not field energy alone.
    C = 4*sp.pi*eps*R
    Uv = C*V**2/2
    Gv = -C*V**2/2
    Fv = -sp.diff(Gv, R)
    zero("fixed-voltage force agrees at the matched state", F.subs(Q, C*V) - Fv)
    zero("field-energy-only fixed-voltage sign is wrong", -sp.diff(Uv, R) + Fv)
    zero("fixed-Q tangent includes inverse-square change", sp.diff(F, R) + 2*F/R)
    zero("fixed-V spherical force has zero radial tangent", sp.diff(Fv, R))

    # Work-conjugate response transforms with the deformation coordinate.
    u, k = sp.symbols("u k", positive=True)
    Psi = k*s**2/2
    T = sp.diff(Psi, s)
    s_u = u**2
    T_u = T.subs(s, s_u)*sp.diff(s_u, u)
    zero("coordinate change preserves virtual work", T_u - sp.diff(Psi.subs(s, s_u), u))
    K_u = sp.diff(T_u, u)
    zero("stiffness transformation includes the preload term", K_u - (sp.diff(T, s).subs(s, s_u)*sp.diff(s_u, u)**2 + T.subs(s, s_u)*sp.diff(s_u, u, 2)))
    check("omitting preload term changes nonlinear-coordinate stiffness", sp.simplify(K_u - k*sp.diff(s_u, u)**2) != 0)

    # Standard-linear-solid comparator, in a generalized dimensionless mode.
    # Ke,Km,T have energy units; z and s are dimensionless; tr is time.
    Ke, Km, tr, t, s0, rate = sp.symbols("Ke Km tr t s0 rate", positive=True)
    z, sd = sp.symbols("z sd", real=True)
    energy = Ke*s**2/2 + Km*(s-z)**2/2
    response = sp.diff(energy, s)
    memory = Km*(s-z)
    zd = (s-z)/tr
    power_balance = response*sd - (sp.diff(energy, s)*sd + sp.diff(energy, z)*zd)
    zero("stored energy plus nonnegative dissipation balances work", power_balance - memory**2/(Km*tr))
    check("dissipation is nonnegative", (memory**2/(Km*tr)).is_nonnegative)
    zero("instantaneous stiffness holds memory configuration fixed", sp.diff(response, s) - (Ke+Km))
    zero("relaxed stiffness follows z=s", sp.diff(response.subs(z, s), s) - Ke)
    response_rate = sp.diff(response, s)*sd + sp.diff(response, z)*zd
    zero("total response law retains relaxation term", response_rate - ((Ke+Km)*sd-memory/tr))
    check("same geometry can retain different response", sp.simplify(response.subs(z, 0)-response.subs(z, s)) != 0)

    hold_memory = Km*s0*sp.exp(-t/tr)
    hold_response = Ke*s0 + hold_memory
    zero("held-shape relaxation solves memory ODE", sp.diff(hold_memory, t)+hold_memory/tr)
    check("held-shape response is not constant", sp.diff(hold_response, t).is_negative)
    zero("held-shape mechanical power is zero", (response*sd).subs(sd, 0))
    # IC-02's uncorrected dT=K ds would infer a geometry change here.
    q = (Ke+Km)*s0
    log_H_wrong = (hold_response-(Ke+Km)*s0)/q
    zero("explicit relaxation correction restores constant geometry rate", (sp.diff(hold_response, t)+hold_memory/tr)/q)
    wrong_ratio = float(sp.exp(log_H_wrong).subs({Ke:2, Km:3, tr:1.5, t:1.5, s0:0.02}))
    check("uncorrected tangent rule fails the held-geometry control", 0 < wrong_ratio < 0.9)

    # Synthetic step calibration; separate ramp trajectory for evaluation.
    true = (2.0, 3.0, 1.5)
    amplitude = 0.02
    plateau = true[0]*amplitude
    initial = sum(true[:2])*amplitude
    t1, t2 = 0.4, 1.3
    y1 = plateau+true[1]*amplitude*math.exp(-t1/true[2])
    y2 = plateau+true[1]*amplitude*math.exp(-t2/true[2])
    recovered = (plateau/amplitude, (initial-plateau)/amplitude,
                 (t2-t1)/math.log((y1-plateau)/(y2-plateau)))
    check("step data recover the three declared comparator parameters", np.allclose(recovered, true, rtol=1e-12, atol=0))
    check("no memory amplitude leaves relaxation time unidentifiable", sp.diff(hold_response.subs(Km, 0), tr) == 0)
    ramp_memory = Km*rate*tr*(1-sp.exp(-t/tr))
    zero("separate ramp response solves memory ODE", sp.diff(ramp_memory,t)-Km*rate+ramp_memory/tr)

    def ramp_numeric(n: int) -> float:
        if n <= 0:
            raise ValueError("n must be positive")
        duration, v, state = 2.0, 0.015, 0.0
        dt = duration/n
        def rhs(time: float, zz: float) -> float:
            return (v*time-zz)/true[2]
        for j in range(n):
            time = j*dt
            k1 = rhs(time,state)
            k2 = rhs(time+dt/2,state+dt*k1/2)
            k3 = rhs(time+dt/2,state+dt*k2/2)
            k4 = rhs(time+dt,state+dt*k3)
            state += dt*(k1+2*k2+2*k3+k4)/6
        return true[0]*v*duration+true[1]*(v*duration-state)
    v, duration = 0.015, 2.0
    prediction = recovered[0]*v*duration + recovered[1]*v*recovered[2]*(-math.expm1(-duration/recovered[2]))
    errors = [abs(ramp_numeric(n)-prediction) for n in (16,32,64)]
    check("ramp implementation converges under refinement", errors[0] > errors[1] > errors[2])
    check("frozen step calibration reproduces separate manufactured ramp", errors[-1] < 1e-9)

    # Same endpoints and integrated relaxation do NOT determine a spectrum.
    f_one = sp.exp(-t/sp.Rational(5,4))
    f_two = (sp.exp(-t/sp.Rational(1,2))+sp.exp(-t/2))/2
    zero("different memory spectra can share initial stress", (f_one-f_two).subs(t,0))
    zero("different memory spectra can share final stress", sp.limit(f_one-f_two,t,sp.oo))
    zero("different memory spectra can share integrated relaxation", sp.integrate(f_one-f_two,(t,0,sp.oo)))
    spectrum_gap = abs(float((f_one-f_two).subs(t,1)))
    check("those shared summaries do not identify the time history", spectrum_gap > 0.05)

    return {
        "study": "IC-03", "status": "PASS", "checks_passed": len(checks),
        "checks": checks,
        "diagnostics": {"wrong_geometry_ratio_at_one_relaxation_time":wrong_ratio,
                        "synthetic_parameters":list(true), "recovered_parameters":list(recovered),
                        "separate_ramp_response":prediction,
                        "ramp_absolute_errors_n16_n32_n64":errors,
                        "memory_spectrum_gap_at_t1":spectrum_gap},
        "limitations": ["No experimental data or physical ARK scalar estimates.",
                        "Classical comparators, not an ARK mechanism validation.",
                        "No equality between deformation s and clock-defined theta assumed.",
                        "One-mode model and parameter identifiability are conditional.",
                        "No independent reviewer; no claim these tests run in GitHub CI."]}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_checks()
    result.update({"executed_utc":datetime.now(timezone.utc).isoformat(),
                   "python":platform.python_version(), "numpy":np.__version__, "sympy":sp.__version__,
                   "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()})
    text = json.dumps(result, indent=2, ensure_ascii=False)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text)

if __name__ == "__main__":
    main()
