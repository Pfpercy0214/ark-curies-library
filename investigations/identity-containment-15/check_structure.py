#!/usr/bin/env python3
"""IC-15 source-form compatibility checks. Algebra only, not physical validation.
Run: python check_structure.py --output results.json
Requires sympy. Original ARK paper text is not altered.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sympy as s


def check_zero(expr: s.Expr) -> None:
    value = s.simplify(expr)
    if value != 0:
        raise AssertionError(str(value))


def run_checks() -> list[dict]:
    out: list[dict] = []
    q, p, r, k, kx, tau, omega, drive, spatial, forcing = s.symbols(
        'q p r k kx tau omega drive spatial forcing', real=True)
    D = s.symbols('D', positive=True)
    U = s.Function('U')
    G = -spatial + s.diff(U(q, tau, omega), q) - drive

    # XXV E6 and E16 agree at an equilibrium only with this source relation.
    f_equilibrium = D * (drive-s.diff(U(q, tau, omega), q))
    check_zero((D*spatial+f_equilibrium).subs(spatial, s.diff(U(q,tau,omega),q)-drive))
    out.append({'name':'matching_stationary_sources','status':'PASS',
        'scope':'Necessary matching at a shared equilibrium; no global forcing law inferred.'})

    # Extending the matching source to all states is an explicit optional closure.
    check_zero(D*spatial+f_equilibrium+D*G)
    out.append({'name':'optional_gradient_evolution','status':'PASS',
        'scope':'Checks the declared extension, not its physical status or uniqueness.'})

    # First variation for prescribed k(x), fixed tau/omega and prescribed drive.
    density = k*p**2/2 + U(q,tau,omega)-drive*q
    el = s.diff(density,q)-kx*p-k*r
    check_zero(el-(-kx*p-k*r+s.diff(U(q,tau,omega),q)-drive))
    out.append({'name':'fixed_coefficient_first_variation','status':'PASS',
        'scope':'Bulk Euler derivative; boundary term remains k*dq/dn*delta(q).'})

    # Differentiate the constrained functional after making fields q-dependent.
    K, T, W = s.Function('K'), s.Function('T'), s.Function('W')
    density2=K(q)*p**2/2+U(q,T(q),W(q))-drive*q
    flux=s.diff(density2,p)
    el2=s.diff(density2,q)-(s.diff(flux,q)*p+s.diff(flux,p)*r)
    expected=-K(q)*r-s.diff(K(q),q)*p**2/2+s.diff(U(q,T(q),W(q)),q)-drive
    check_zero(el2-expected)
    # Multivariate chain contributions checked with an explicit symbolic
    # polynomial. This avoids treating equivalent unevaluated Subs objects
    # as unequal; it is not a CAS proof for every possible constitutive law.
    a0,a1,a2,a3=s.symbols('a0 a1 a2 a3', real=True)
    Uexample=a0*q**2+a1*q*tau+a2*omega**2+a3*tau*omega
    mapped=Uexample.subs({tau:T(q),omega:W(q)})
    partial=s.diff(Uexample,q).subs({tau:T(q),omega:W(q)})
    response=s.diff(Uexample,tau).subs({tau:T(q),omega:W(q)})*s.diff(T(q),q)
    response+=s.diff(Uexample,omega).subs({tau:T(q),omega:W(q)})*s.diff(W(q),q)
    check_zero(s.diff(mapped,q)-partial-response)
    out.append({'name':'coupled_variation_chain_terms','status':'PASS',
        'scope':'General K(q) variation plus a symbolic polynomial check of tau/omega chain terms; local substitutions only, not history closure.'})

    # If coefficients/drive are fixed and boundary work vanishes, this is the
    # bulk energy-production integrand of the optional gradient evolution.
    R=s.symbols('R',real=True)
    check_zero(R*(-D*R)+D*R**2)
    out.append({'name':'conditional_bulk_energy_decay','status':'PASS',
        'scope':'Nonpositive only for D>0; not a total physical energy balance, nor proof of stability of every stationary state.'})

    # Closed spatial boundary need not conserve q with stabilization/source term.
    t=s.symbols('t',real=True)
    q0=s.symbols('q0',positive=True)
    solution=q0*s.exp(-D*t)
    check_zero(s.diff(solution,t)+D*solution)
    if s.simplify(s.diff(solution,t))==0:
        raise AssertionError('Reaction must not be reported as amount-conserving')
    out.append({'name':'no_flux_is_not_reaction_conservation','status':'PASS',
        'scope':'Uniform illustrative U=q^2/2, drive=0, unit volume. Not proposed as ARK microphysics.'})
    return out


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite previous results')
    checks=run_checks()
    result={'study':'IC-15','date':'2026-11-04',
        'scope':'Source-based structural reconstruction and exact algebra; no data fitting, no numerical PDE solve, no empirical validation.',
        'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'python':platform.python_version(),'sympy':s.__version__,
        'passed':len(checks),'total':6,'checks':checks,
        'prior_IC_suites_rerun':False,'independent_second_review':False}
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
