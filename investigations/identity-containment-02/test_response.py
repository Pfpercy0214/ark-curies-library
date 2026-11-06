#!/usr/bin/env python3
"""IC-02: conditional trajectory reconstruction and clock-ratio calibration.

All numerical inputs below are manufactured test fixtures, NOT laboratory data.
This tests a proposed common-regime combination of XVIII 2.2, XXII II, XXV A.1.
It does not establish that their state meanings/units agree in a real apparatus.
Requires numpy and sympy. No network access; only an optional JSON report write.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import unittest

import numpy as np
import sympy as sp

BASE = "6ba49695728756d7359b8551f2118da8befa6896"


def response_factor(q: np.ndarray, tau: np.ndarray) -> np.ndarray:
    """Approximate H=exp integral(d tau/q), using endpoint-mean q per interval.

    Arrays are co-sampled, in path order; time is not inferred here. Positive q,
    finite arrays and compatible units are prerequisites, not fitted choices.
    For smooth paths this quadrature is second order; uncertainty is separate.
    """
    q, tau = np.asarray(q, float), np.asarray(tau, float)
    if q.ndim != 1 or tau.shape != q.shape or len(q) < 2:
        raise ValueError("q and tau must be matching 1-D arrays with at least 2 points")
    if not np.all(np.isfinite(q)) or not np.all(np.isfinite(tau)) or np.any(q <= 0):
        raise ValueError("finite tau and strictly positive q required on this branch")
    log_h = np.r_[0.0, np.cumsum(np.diff(tau) / ((q[:-1] + q[1:]) / 2))]
    with np.errstate(over="raise", invalid="raise", under="raise"):
        return np.exp(log_h)


def clock_deficit(a: float, h: float) -> float:
    """d=1-cos(h*a)/cos(a), evaluated without subtracting two near-unity rates.

    Restricted branch: h>1, 0<=a<pi/(2h). 'a' is theta at the reference state,
    not the reference clock's own scalar. Actual measurements need reference
    drift and clock systematic corrections before using this function.
    """
    if not (math.isfinite(a) and math.isfinite(h) and h > 1 and 0 <= a < math.pi/(2*h)):
        raise ValueError("need h>1 and 0<=a<pi/(2h)")
    return 2*math.sin((h+1)*a/2)*math.sin((h-1)*a/2)/math.cos(a)


def calibrate_theta0(h: float, deficit: float) -> float:
    """Invert the strictly increasing clock deficit on the stated branch.

    Calibration uses one designated ratio change, not a later evaluation target.
    No clipping, branch selection from the desired answer, or zero replacement.
    """
    if not (math.isfinite(h) and h > 1 and math.isfinite(deficit) and 0 < deficit < 1):
        raise ValueError("need h>1 and 0<deficit<1; no signal is not an anchor")
    lo, hi = 0.0, math.nextafter(math.pi/(2*h), 0.0)
    for _ in range(180):
        mid = (lo + hi)/2
        if clock_deficit(mid, h) < deficit:
            lo = mid
        else:
            hi = mid
        if hi-lo <= 2e-14*max(mid, 1e-300):
            break
    return (lo+hi)/2


def fixture(n: int = 801, memory_drift: float = 0.0) -> dict[str, np.ndarray]:
    """Smooth dimensionless constructed path; evaluator truth is labeled explicitly."""
    t = np.linspace(0.0, 1.0, n)
    q = 2.0 + t
    h = np.exp(.15*t + .02*np.sin(t))
    theta = .2*h
    tau = 5 + .15*(2*t + t*t/2) + .02*((2+t)*np.sin(t)+np.cos(t)-1)
    tau += memory_drift*t  # deliberately violates the selected constitutive branch
    return dict(t=t, q=q, tau=tau, truth_h=h, truth_theta=theta, truth_kappa=q/theta)


def log_h_jacobian(q: np.ndarray, tau: np.ndarray) -> np.ndarray:
    """Gradient of endpoint log H wrt [q_0..q_n, tau_0..tau_n]."""
    q, tau = np.asarray(q, float), np.asarray(tau, float)
    response_factor(q, tau)  # shared input validation
    mean = (q[:-1]+q[1:])/2
    dq, dtau = np.zeros_like(q), np.zeros_like(tau)
    contribution = -np.diff(tau)/(2*mean**2)
    dq[:-1] += contribution
    dq[1:] += contribution
    dtau[:-1] -= 1/mean
    dtau[1:] += 1/mean
    return np.r_[dq, dtau]


def sensitivity(a: float, h: float) -> tuple[float, float]:
    """(partial deficit/partial a, partial deficit/partial h)."""
    da = (h*math.sin(h*a)*math.cos(a)-math.cos(h*a)*math.sin(a))/math.cos(a)**2
    dh = a*math.sin(h*a)/math.cos(a)
    return da, dh


def demonstrations() -> dict:
    f = fixture()
    h = response_factor(f['q'], f['tau'])
    j = 320  # predeclared calibration location t=.4, NOT the later target
    d_cal = clock_deficit(.2, float(f['truth_h'][j]))
    a = calibrate_theta0(float(h[j]), d_cal)
    d_prediction = clock_deficit(a, float(h[-1]))
    d_truth = clock_deficit(.2, float(f['truth_h'][-1]))
    errors = []
    for n in (51, 101, 201, 401, 801):
        g = fixture(n)
        hg = response_factor(g['q'], g['tau'])
        errors.append({'samples': n, 'max_relative_H_error': float(np.max(np.abs(hg/g['truth_h']-1)))})
    bad = fixture(memory_drift=.04)
    h_bad = response_factor(bad['q'], bad['tau'])
    a_bad = calibrate_theta0(float(h_bad[j]), d_cal)
    bad_deficit = clock_deficit(a_bad, float(h_bad[-1]))
    a_small, h_small = 1e-9, 1.2
    dq = np.array([2., 2.2, 2.4]); dtau = np.array([5., 5.04, 5.1])
    jac = log_h_jacobian(dq, dtau)
    sig = np.array([.002]*3+[.0002]*3)
    cov = np.diag(sig**2)
    cov[0,3] = cov[3,0] = .6*sig[0]*sig[3]
    return {
        'fixture_type': 'manufactured dimensionless trajectory; not an experiment',
        'calibration_t': float(f['t'][j]), 'evaluation_t': 1.0,
        'calibration_ratio_deficit': d_cal, 'estimated_theta0': a,
        'evaluation_deficit_prediction': d_prediction,
        'evaluation_deficit_constructed_truth': d_truth,
        'evaluation_relative_error': abs(d_prediction/d_truth-1),
        'quadrature_convergence': errors,
        'deliberately_unmodeled_memory_drift': .04,
        'wrong_model_evaluation_relative_error': abs(bad_deficit/d_truth-1),
        'small_signal': {'theta0': a_small, 'H': h_small,
            'stable_deficit': clock_deficit(a_small,h_small),
            'naive_float_deficit': 1-math.cos(h_small*a_small)/math.cos(a_small),
            'recovered_theta0': calibrate_theta0(h_small,clock_deficit(a_small,h_small))},
        'uncertainty_fixture': {'variance_log_H_with_covariance': float(jac@cov@jac),
            'variance_log_H_diagonal_only': float(jac@np.diag(np.diag(cov))@jac),
            'note': 'These are illustrative input uncertainties, not measured errors.'},
    }


class ResponseChecks(unittest.TestCase):
    def test_01_differential_recovery(self):
        t = sp.symbols('t', real=True)
        th, k = sp.Function('theta')(t), sp.Function('kappa')(t)
        self.assertEqual(sp.simplify(k*sp.diff(th,t)/(k*th)-sp.diff(th,t)/th),0)

    def test_02_scale_family_survives_differential_information(self):
        t = sp.symbols('t', real=True); a = sp.symbols('a', positive=True)
        th, k = sp.Function('theta')(t), sp.Function('kappa')(t)
        self.assertEqual(sp.simplify((k/a)*(a*th)-k*th),0)
        self.assertEqual(sp.simplify((k/a)*sp.diff(a*th,t)-k*sp.diff(th,t)),0)

    def test_03_tau_offset_remains_an_independent_state_input(self):
        f=fixture(); h=response_factor(f['q'],f['tau'])
        np.testing.assert_allclose(response_factor(f['q'],f['tau']+17),h,rtol=2e-14)

    def test_04_constructed_path_satisfies_constitutive_law(self):
        t=sp.symbols('t', real=True); q=2+t
        th=sp.exp(sp.Rational(15,100)*t+sp.Rational(2,100)*sp.sin(t))/5
        tau=5+sp.Rational(15,100)*(2*t+t*t/2)+sp.Rational(2,100)*((2+t)*sp.sin(t)+sp.cos(t)-1)
        self.assertEqual(sp.simplify(sp.diff(tau,t)-(q/th)*sp.diff(th,t)),0)

    def test_05_reconstruction_converges_at_second_order(self):
        errs=[]
        for n in (51,101,201,401):
            f=fixture(n); h=response_factor(f['q'],f['tau'])
            errs.append(float(np.max(np.abs(h/f['truth_h']-1))))
        self.assertTrue(all(3.8<errs[i]/errs[i+1]<4.2 for i in range(3)))

    def test_06_clock_ratio_identity(self):
        a,h=sp.symbols('a h',real=True)
        stable=2*sp.sin((h+1)*a/2)*sp.sin((h-1)*a/2)/sp.cos(a)
        self.assertEqual(sp.trigsimp(sp.expand_trig(stable-(1-sp.cos(h*a)/sp.cos(a)))),0)

    def test_07_clock_calibration_on_fixed_branch(self):
        for a in (1e-9,1e-4,.1,.4):
            for h in (1.01,1.2,2.):
                self.assertLess(abs(calibrate_theta0(h,clock_deficit(a,h))/a-1),2e-13)
                self.assertGreater(sensitivity(a,h)[0],0)

    def test_08_tiny_clock_deficit_does_not_round_to_zero(self):
        a,h=1e-9,1.2
        self.assertEqual(1-math.cos(h*a)/math.cos(a),0.)
        self.assertGreater(clock_deficit(a,h),0.)
        ah,hh=sp.Rational(1,10**9),sp.Rational(6,5)
        reference=float((1-sp.cos(hh*ah)/sp.cos(ah)).evalf(70))
        self.assertLess(abs(clock_deficit(a,h)/reference-1),1e-14)

    def test_09_clock_scale_is_not_identified_without_excitation(self):
        a=sp.symbols('a',real=True)
        self.assertEqual(sp.simplify(sp.cos(a)/sp.cos(a)),1)
        with self.assertRaises(ValueError): calibrate_theta0(1.,1e-4)

    def test_10_reject_invalid_data_and_undeclared_branches(self):
        cases=[(np.array([0.,1.]),np.array([1.,2.])),
               (np.array([1.,np.nan]),np.array([1.,2.])),
               (np.array([1.,2.]),np.array([1.])),
               (np.array([1.,-1.]),np.array([1.,2.]))]
        for q,tau in cases:
            with self.assertRaises(ValueError): response_factor(q,tau)
        for h,d in ((1.2,0.),(1.2,-.1),(1.2,1.),(.9,.01)):
            with self.assertRaises(ValueError): calibrate_theta0(h,d)

    def test_11_unknown_reference_drift_can_restore_ambiguity(self):
        a1,a2,h=.2,.3,1.2
        r1=1-clock_deficit(a1,h); r2=1-clock_deficit(a2,h)
        reference_drift=r2/r1
        self.assertAlmostEqual(r2/reference_drift,r1,places=14)
        self.assertNotAlmostEqual(reference_drift,1.,places=5)

    def test_12_calibration_then_distinct_cross_observable_evaluation(self):
        r=demonstrations()
        self.assertLess(r['calibration_t'],r['evaluation_t'])
        self.assertLess(r['evaluation_relative_error'],1e-6)

    def test_13_wrong_memory_model_is_not_rescued_by_one_calibration(self):
        r=demonstrations()
        self.assertGreater(r['wrong_model_evaluation_relative_error'],1e-4)

    def test_14_quadrature_jacobian_matches_numerical_derivatives(self):
        q=np.array([2.,2.2,2.4]); tau=np.array([5.,5.04,5.1]); z=np.r_[q,tau]
        analytic=log_h_jacobian(q,tau); numerical=[]
        for i in range(len(z)):
            zp,zm=z.copy(),z.copy(); zp[i]+=1e-5;zm[i]-=1e-5
            f=lambda y: np.log(response_factor(y[:3],y[3:])[-1])
            numerical.append((f(zp)-f(zm))/2e-5)
        np.testing.assert_allclose(analytic,numerical,rtol=2e-7,atol=2e-10)

    def test_15_covariance_changes_inferred_uncertainty(self):
        u=demonstrations()['uncertainty_fixture']
        self.assertGreater(u['variance_log_H_with_covariance'],0)
        self.assertGreater(abs(u['variance_log_H_with_covariance']/u['variance_log_H_diagonal_only']-1),.01)

    def test_16_clock_implicit_sensitivities(self):
        a,h=.2,1.2; d=clock_deficit(a,h); da,dh=sensitivity(a,h); step=1e-7
        numerical_d=(calibrate_theta0(h,d+step)-calibrate_theta0(h,d-step))/(2*step)
        numerical_h=(calibrate_theta0(h+step,d)-calibrate_theta0(h-step,d))/(2*step)
        self.assertAlmostEqual(numerical_d/(1/da),1.,places=7)
        self.assertAlmostEqual(numerical_h/(-dh/da),1.,places=7)

    def test_17_joint_field_equation_for_unknown_spatial_baseline(self):
        x,t,c=sp.symbols('x t c', nonzero=True)
        u=sp.Function('u')(x); h=sp.Function('H')(x,t);q=sp.Function('q')(x,t)
        tau=sp.Function('tau')(x,t); sd=sp.Function('Sdot')(x,t)
        lam=sp.Function('Lambda')(sp.exp(u)*h)
        th=sp.exp(u)*h;k=q/th
        original=sp.diff(k*sp.diff(th,x),x)-sp.diff(th,t,2)/c**2-(tau/k)*sd-lam
        transformed=sp.diff(q*sp.diff(u,x),x)+sp.diff(q*sp.diff(h,x)/h,x)-lam-sp.exp(u)*(sp.diff(h,t,2)/c**2+tau*h*sd/q)
        self.assertEqual(sp.simplify(original-transformed),0)

    def test_18_entropy_baseline_not_fixed_by_identity_scale_alone(self):
        x,t=sp.symbols('x t');s=sp.Function('S')(x,t);b=sp.Function('S0')(x)
        self.assertEqual(sp.diff(s+b,t)-sp.diff(s,t),0)

    def test_19_unmodeled_tau_evolution_biases_relative_theta(self):
        t=sp.symbols('t',positive=True);h0=sp.Rational(1,25);q=2+t
        bias=sp.integrate(h0/q,(t,0,1))
        self.assertTrue(bool(bias>0))
        f=fixture(1601,.04);h=response_factor(f['q'],f['tau'])
        measured=np.log(h[-1]/f['truth_h'][-1])
        self.assertAlmostEqual(measured,float(bias),places=7)

    def test_20_no_clock_target_enters_response_factor(self):
        f=fixture();before=response_factor(f['q'],f['tau'])
        f['truth_theta'][:]=123456.;f['truth_h'][:]=-99.
        np.testing.assert_array_equal(before,response_factor(f['q'],f['tau']))


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--json',type=Path)
    args=p.parse_args()
    result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ResponseChecks))
    report={'study':'IC-02-A','status':'conditional derivation / constructed-example verification',
        'source_branch_head':BASE,'executed_utc':datetime.now(timezone.utc).isoformat(),
        'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'tests_run':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
        'success':result.wasSuccessful(),
        'checks':[n for n in dir(ResponseChecks) if n.startswith('test_')],
        'demonstrations':demonstrations(),
        'limits':['No experimental dataset loaded or fitted.',
                  'A new joint hypothesis connects definitions from three historical versions; physical compatibility is unverified.',
                  'One designated clock shift calibrates theta0; a later clock shift is a separate constructed evaluation target.',
                  'Uses measured q and tau histories: cross-observable inference, not a forward initial-value ARK solver.',
                  'No empirical tau bridge, Lambda, or neutron lifetime is supplied.',
                  'Passing controls diagnose selected mathematical issues; they do not validate the mechanism.']}
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    return 0 if result.wasSuccessful() else 1


if __name__=='__main__':
    raise SystemExit(main())
