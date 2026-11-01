#!/usr/bin/env python3
"""Exact algebra checks, not an empirical validation or a complete ARK solver.

Run: python test_closure.py --json test-results.json
Requires SymPy (tested with 1.14.0). No network access or source-file writes.
"""
from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path
import unittest

import sympy as sp


def is_zero(value: sp.Expr) -> bool:
    return sp.simplify(value) == 0


class ClosureChecks(unittest.TestCase):
    def setUp(self) -> None:
        self.th, self.k, self.tau = sp.symbols('theta kappa tau', positive=True)
        self.u, self.a, self.g = sp.symbols('Lambda_u Lambda_A G', positive=True)
        self.state = sp.Matrix([self.th, self.k, self.tau])
        self.q = self.th * self.k
        self.y = sp.Matrix([self.u * self.q**2 / 2, self.a * self.g * self.q])

    def test_01_product_symmetry(self) -> None:
        scale = sp.Symbol('scale', positive=True)
        transformed = self.y.subs(
            {self.th: scale * self.th, self.k: self.k / scale}, simultaneous=True
        )
        self.assertTrue(all(is_zero(v) for v in transformed - self.y))

    def test_02_two_product_bridges_rank_one(self) -> None:
        self.assertEqual(self.y.jacobian([self.th, self.k]).rank(), 1)

    def test_03_product_and_tau_rank_two(self) -> None:
        observations = self.y.col_join(sp.Matrix([self.tau]))
        self.assertEqual(observations.jacobian(self.state).rank(), 2)

    def test_04_independent_theta_and_tau_restore_rank_three(self) -> None:
        observations = self.y.col_join(sp.Matrix([self.th, self.tau]))
        self.assertEqual(observations.jacobian(self.state).rank(), 3)

    def test_05_two_anchors_plus_conditional_constitutive_law(self) -> None:
        th0, tau0 = sp.symbols('theta0 tau0', real=True)
        law = self.tau - tau0 - self.k * (self.th - th0)
        constraints = sp.Matrix([self.th, self.tau, law])
        jacobian = constraints.jacobian(self.state)
        self.assertTrue(is_zero(jacobian.det() - (self.th - th0)))
        self.assertEqual(jacobian.subs(self.th, th0).rank(), 2)
        recovered = (self.tau - tau0) / (self.th - th0)
        self.assertTrue(is_zero(law.subs(self.k, recovered)))

    def test_06_tangent_stiffness_requires_an_integration_anchor(self) -> None:
        th0, tau0, offset = sp.symbols('theta0 tau0 offset', real=True)
        field = self.th**2 + offset
        tangent = sp.diff(field, self.th)
        secant = field / self.th
        self.assertFalse(is_zero(tangent - secant))
        reconstructed = tau0 + sp.integrate(2 * self.th, (self.th, th0, self.th))
        self.assertTrue(is_zero(reconstructed - (tau0 + self.th**2 - th0**2)))
        self.assertTrue(is_zero(sp.diff(reconstructed, self.th) - tangent))

    def test_07_d1_rearrangement(self) -> None:
        operator, lam, rate = sp.symbols('operator Lambda Sdot', real=True)
        equation_residual = operator - (self.tau / self.k) * rate - lam
        inferred_rate = (self.k / self.tau) * (operator - lam)
        self.assertTrue(is_zero(equation_residual.subs(rate, inferred_rate)))

    def test_08_d1_has_spatially_variable_time_constant_nullspace(self) -> None:
        x, t = sp.symbols('x t', real=True)
        s = sp.Function('S')(x, t)
        c0 = sp.Function('C0')(x)
        self.assertTrue(is_zero(sp.diff(s + c0, t) - sp.diff(s, t)))

    def test_09_manufactured_d1_field_and_baseline(self) -> None:
        x, t = sp.symbols('x t', real=True)
        th = x**2 * t**2
        kappa, tau, speed = sp.Integer(2), sp.Integer(3), sp.Integer(4)
        lam = 5 * th
        operator = sp.diff(kappa * sp.diff(th, x), x) - sp.diff(th, t, 2) / speed**2
        rate = (kappa / tau) * (operator - lam)
        baseline = sp.Function('S0')(x)
        s = baseline + sp.integrate(rate, (t, 0, t))
        self.assertTrue(is_zero(operator - (tau / kappa) * sp.diff(s, t) - lam))
        self.assertTrue(is_zero(s.subs(t, 0) - baseline))
        self.assertTrue(is_zero(sp.diff(s + x**3, t) - sp.diff(s, t)))

    def test_10_resolved_unresolved_partition_is_not_identified_by_total(self) -> None:
        unresolved, epsilon, shift = sp.symbols('S epsilon shift', real=True)
        total = unresolved + epsilon
        shifted = total.subs(
            {unresolved: unresolved - shift, epsilon: epsilon + shift}, simultaneous=True
        )
        self.assertTrue(is_zero(shifted - total))
        self.assertEqual(sp.Matrix([total]).jacobian([unresolved, epsilon]).rank(), 1)
        constrained = sp.Matrix([total, epsilon])
        self.assertEqual(constrained.jacobian([unresolved, epsilon]).rank(), 2)

    def test_11_baseline_difference_does_not_suppress_environmental_drift(self) -> None:
        s0, s1, e0, e1 = sp.symbols('S0 S1 eps0 eps1', real=True)
        change = (s1 + e1) - (s0 + e0)
        self.assertTrue(is_zero(change - (s1 - s0) - (e1 - e0)))
        self.assertTrue(is_zero(change.subs(s1, s0) - (e1 - e0)))

    def test_12_printed_xxii_inversion_product(self) -> None:
        a_comp, b, mu = sp.symbols('A_comp B mu0', positive=True)
        th_printed = (self.a / self.u) * (b**2 / mu) / (a_comp * self.g)
        k_printed = (self.u / self.a**2) * (a_comp**2 * mu / b**2) / self.g**2
        product = sp.simplify(th_printed * k_printed)
        self.assertTrue(is_zero(product - a_comp / (self.a * self.g**3)))
        required_product = a_comp / (self.a * self.g)
        self.assertTrue(is_zero(product / required_product - 1 / self.g**2))
        self.assertFalse(is_zero(product - required_product))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path, help='Optional output report; does not change sources.')
    args = parser.parse_args()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(ClosureChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    record = {
        'study': 'IC-01',
        'kind': 'Exact symbolic and manufactured-example checks; not empirical validation',
        'source_commit': '2db757753005e6ac66c55797890b2960bffe9307',
        'python': platform.python_version(),
        'sympy': sp.__version__,
        'tests_run': result.testsRun,
        'failures': len(result.failures),
        'errors': len(result.errors),
        'skipped': len(result.skipped),
        'success': result.wasSuccessful(),
        'checks': [name for name in dir(ClosureChecks) if name.startswith('test_')],
        'interpretation': 'PASS means the stated algebraic conclusions were reproduced, including diagnosed non-identifiability and an incompatible printed inversion. It does not mean the source equations describe nature.',
    }
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8')
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    raise SystemExit(main())
