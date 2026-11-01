# IC-02 — Recovering identity through a controlled change

**Working candidate:** IC-02-A. **Date:** 2026-10-31, America/Chicago. **Author:** Curie. **Status:** conditional derivation and executable constructed-example checks; no experimental validation or independent review. Continuation of [IC-01](../identity-containment-01/README.md). Base research commit: `6ba49695728756d7359b8551f2118da8befa6896`.

## Result and its boundary

A measured product need not prevent reconstruction of its factors. Under an explicit common-regime hypothesis, a product history and a tension history determine the *relative* evolution of theta and kappa. One independently corrected clock-ratio change can then determine the remaining scale, on a specified branch. A different clock-ratio change remains available as a test with that scale frozen.

This is a constructive answer to the owner's proposal to use two core quantities plus another relation. It is NOT a proof that three isolated numbers describe any physical identity, or that the historical scalar definitions are already experimentally equivalent. Histories contain many samples. The joint interpretation below is a new candidate connecting three source versions, not a silently recovered universal ARK model.

No archived paper, manifest, policy, safeguard, or original-repository file is changed. The printed XXII inversion remains unfixed; only its direct product bridge is used.

## 1. Declared joint hypothesis, not an automatic equation merger

| Relation | Provenance | Additional requirement in this study |
| --- | --- | --- |
| q = kappa theta | XXII II, direct electromagnetic bridges | Fixed calibration, geometry and gauge convention; independently grounded q for the same resolved region. |
| d tau = kappa d theta | Differential form of the integral in XVIII 2.2 | Same kappa and theta as the bridge; no extra explicit memory-evolution term on this selected path. |
| Clock lapse = cos(theta) | XXV A.1 operational clock definition | Same theta as the other two relations; compatible reference convention and independently corrected clock comparisons. |

[Exact source locations and primary external records](../../sources/identity-containment-02-primary-sources.md) are part of this specification. The cross-version compatibility requirements are hypotheses to test, NOT findings established by the archive.

Work at one resolved location or consistently averaged region, with synchronized sampling along a smooth path that retains the relevant identity. Use the positive branch q>0, theta>0, kappa>0 without a zero crossing. Theta is dimensionless (angular label); the tangent relation requires tau, kappa and q to have compatible units. The exponent derived below is dimensionless only after this unit correspondence is supplied. A mechanical modulus, boundary force, normalized variable and lifetime are not interchangeable merely because all have been associated with kappa or tau in historical discussions.

The absolute tau reference is assumed independently characterized. Derivatives recover only changes in tau: an unknown additive tau offset survives and matters if a later equation uses tau itself. Unknown bridge scales or an unknown coefficient in d tau = C kappa d theta must be included as additional unknowns. The present uniqueness statement assumes those calibrations and the unit correspondence are fixed independently of the evaluation target.

For the ideal-solenoid example in XXII, A_comp/G=B. The two direct bridges then require Lambda_u=Lambda_A^2/mu_0 for a nonzero common q. They remain one state-information channel; deriving A from B does not supply a second independent scalar. This study does not use the inconsistent printed inverse formulas to manufacture either factor.

## 2. Recover the relative trajectory before choosing an absolute scale

Suppress the causal superscript in this working derivation only. From

$$
q(t)=\kappa(t)\theta(t),\qquad \dot\tau(t)=\kappa(t)\dot\theta(t),
$$

we obtain

$$
\frac{d}{dt}\log\theta=\frac{\dot\tau}{q}.
$$

Thus define the observable-path functional

$$
H(t)=\exp\!\left[\int_{t_0}^{t}\frac{d\tau(s)}{q(s)}\right],
\qquad H(t_0)=1.
$$

The admissible factors have the explicit form

$$
\boxed{\theta(t)=aH(t),\qquad \kappa(t)=\frac{q(t)}{aH(t)}}
$$

with one unknown positive reference value a=theta(t0) per resolved location. Scaling theta by a constant and kappa by its inverse preserves both the product AND the tangent equation. More samples of only these channels do not eliminate that exact freedom, although they can reduce measurement uncertainty and reveal model failures.

A separately established a fixes the whole trajectory on this branch. An absolute clock-to-asymptotic-reference measurement is one possible source of a, but it is not the only route: the next section shows how a *change in a relative clock ratio* can fix it jointly with H.

This is conditional cross-observable reconstruction using measured q(t) and tau(t). It is not a forward solution from initial state and environmental drive alone; the future q and tau histories are not predicted here.

## 3. A relative clock change can fix the scale jointly

A single clock comparison generally measures a ratio of lapses, not either absolute lapse. Let a test clock and a reference clock be compared at t0 and t1. After independently accounting for clock transition shifts, time transfer, reference drift and relevant motion/geometry, define

$$
\mathcal R_1=
\frac{(\nu_{\rm test}/\nu_{\rm reference})_{t_1}}
     {(\nu_{\rm test}/\nu_{\rm reference})_{t_0}}.
$$

If the reference lapse is unchanged or independently corrected, its *unknown constant baseline cancels*. Under the candidate's clock mapping,

$$
\boxed{\mathcal R_1=\frac{\cos(aH_1)}{\cos a}},\qquad H_1=H(t_1).
$$

We do not set the reference clock's theta to zero. The relation is about the test region's theta at two states relative to one consistent coordinate convention. Time intervals labeled proper time are not ARK tension tau.

### A sufficient uniqueness result

For H1>1, restrict

$$
0<a<\frac{\pi}{2H_1},\qquad 0<\mathcal R_1<1.
$$

Then

$$
\frac{d}{da}\log\!\left[\frac{\cos(aH_1)}{\cos a}\right]
=\tan a-H_1\tan(aH_1)<0.
$$

The ratio decreases continuously from 1 to 0 on this interval, giving exactly one a for a permitted measurement. This is a proved branch-specific result, not a global uniqueness claim across arbitrary oscillatory cosine branches. H1=1 supplies no clock-change scale information. Inconsistent signs, zero q and inaccessible branches are flagged rather than clipped or chosen to match the answer. The numerical implementation deliberately supports this H>1 branch only.

### Calibration is not the evaluation target

Using the first clock shift to find a is calibration. For a later independently measured q/tau path with H2 and the same declared identity/reference/calibrations, predict

$$
\mathcal R_{2,\rm pred}=\frac{\cos(aH_2)}{\cos a}
$$

before opening that clock-comparison result. No new a is selected at t2. This is a potential cross-observable consistency/transfer test, not automatically a discriminator of substrat ontology. A conventional model with equivalent information must also be evaluated.

The software example uses an explicitly manufactured smooth path. It proves that this calculation is implementable and checks numerical error; it is not an unseen experiment, independent scientific confirmation, or an inferred neutron lifetime.

## 4. What must actually be measured before this is an experiment

The current practical candidate is a fixed, resolved electromagnetic test region: calibrated field measurements supply q under XXII's selected gauge/geometry, a properly colocated clock supplies corrected ratio changes, and a separately calibrated boundary/response measurement would have to supply the particular tension tau used in the tangent relation. **The last mapping is not established by this study.** The identification of the clock's region, field region and boundary response as one compatible state is also a requirement, not an assumption concealed by collocation.

Do not substitute a decay lifetime, relaxation time, ordinary net force, or flux for tau without a derived dimensional and operational bridge. Do not set an unknown tau offset to a convenient value. Do not infer tau from the clock shift being evaluated. Mechanical/electrical/clock transfer constants must be fixed or independently constrained before a uniqueness claim is applied.

Clock-comparison observations are real: the Chou et al. experimental abstract reports optical-clock time dilation from relative speeds below 10 m/s and elevation changes below one meter [E1]. This establishes an observable comparison channel, not its proposed relation to electromagnetic q or ARK tension. No real dataset containing synchronized q, a validated tau, and corrected clock shifts for the same state was loaded in this pass.

A field perturbation can change an atomic transition frequency through ordinary apparatus-dependent shifts without changing proper-time lapse. Those shifts, reference drift, and motion cannot be relabeled as ARK time deformation by default. An independently characterized clock measurement model and a conventional comparator are necessary before interpreting a residual.

No laboratory build, new equipment purchase or claimed practical sensitivity is recommended by this mathematical pilot. The immediate readiness gate is identifying the physical tau bridge and the common-state/units mapping in source-backed terms; then determine whether existing data can test them.

## 5. Baselines and uncertainty remain physical inputs

There are at least four different reference questions:

1. **Identity scale a:** can be fixed by the joint clock/trajectory constraint above.
2. **Absolute tau offset:** absent from the tangent equation; needs an independent reference if absolute tau is required.
3. **Reference-clock drift:** can imitate a clock change; must be independently controlled, corrected or bounded.
4. **Entropy level S0(x):** not fixed merely by identifying a; D.1 includes an entropy derivative.

If the reference clock changes by a lapse ratio b, the measured normalized clock ratio is R_meas=cos(aH)/(b cos a). With arbitrary unknown b, multiple a values reproduce the same reading. Correcting or bounding b is part of the input specification, not an optional caveat.

The stable signal expression is

$$
d\equiv1-\mathcal R
=\frac{2\sin[(H+1)a/2]\sin[(H-1)a/2]}{\cos a}.
$$

For small a, d is approximately (H^2-1)a^2/2. Consequently,

$$
\frac{\delta a}{a}\simeq\frac{\delta d}{2d}
-\frac{H\,\delta H}{H^2-1}.
$$

An algebraically identifiable scale may still be poorly measured when the excitation or clock shift is tiny. The code tests a numerical trap: a=1e-9, H=1.2 gives d=2.2e-19, while subtracting two rounded binary64 clock rates produces zero. Keeping the measured fractional deficit directly avoids this arithmetic loss; it does not create experimental precision that the instruments do not have.

For exact first-order propagation of the implicit calibration,

$$
\delta a=\frac{\delta d-d_H\,\delta H}{d_a},\qquad
u_a^2=\frac{u_d^2+d_H^2u_H^2-2d_H\,\mathrm{Cov}(d,H)}{d_a^2}.
$$

Here the symbol u_a denotes standard uncertainty, not a new state. Covariances with q and tau, common calibration errors and cross-time correlations must also be carried through H and kappa; a third printed quantity is not statistically independent merely because it has a different label. The executable endpoint-log-H Jacobian provides a starting point for joint covariance propagation. For nonlinear, near-boundary or non-Gaussian uncertainty, the first-order formula alone is insufficient. [U1]

## 6. Challenge the selected constitutive branch

If the actual behavior is

$$
\dot\tau=\kappa\dot\theta+h(t),
$$

then the inferred log trajectory includes the bias integral h(t)/q(t). Here h is a diagnostic placeholder for a violated branch assumption, not a fitted rescue term or an identified environmental cause. One clock calibration can absorb part of the error, so a different withheld comparison is necessary.

The executable negative control adds a declared 0.04*t to the manufactured tau while leaving its constructed theta/clock truth unchanged. One calibration still gives a plausible scale, but the later clock-deficit prediction has a nonzero relative error of about 2.91e-4, versus 1.77e-9 quadrature/calibration error in the correctly specified synthetic case. This is a demonstrated difference in test fixtures, not a claim of detectability against actual laboratory noise. The threshold was a software test criterion, not an experimental discovery threshold.

Other necessary failures/controls: an unexcited path; unknown reference drift; wrong calibration/units; a zero crossing; an unmodeled state transition; and reuse of the clock target to assign q or tau. A failed comparison can locate an inadequate mapping or missing physics. It does not by itself identify epsilon or falsify every ARK version.

## 7. Connect back to the complete field equation without assuming its closure

At different spatial locations the integration factor is a(x), not necessarily one constant. Write theta=e^{u(x)}H(x,t), kappa=q/(e^u H). If the same candidate variables are also compatible with XXV D.1, exact substitution gives

$$
\nabla\cdot(q\nabla u)+\nabla\cdot(q\nabla\log H)
-\Lambda(e^uH,\omega)
=e^u\left[c^{-2}\partial_t^2H+\frac{\tau H}{q}\,\partial_tS\right].
$$

This specifies where additional spatial, environmental and boundary information could constrain the remaining identity-baseline field. It is a formal operator identity, independently checked in one spatial dimension. It is not a solved well-posed boundary problem or proof of global uniqueness. In particular, we have not set Lambda=0, prescribed omega as an independent frequency, assumed spatial uniformity, supplied missing normalization scales, or identified S with S+epsilon.

After identity reconstruction, D.1 can conditionally give an environmental rate only when its other terms are known. The entropy integration baseline, the S/epsilon partition, and environmental microstructure remain separate questions. A different coupled pressure-balance equation might add that information; it must be inspected rather than assumed absent or present.

## 8. Executed work and next evidence gate

Run:

```bash
python investigations/identity-containment-02/test_response.py --json investigations/identity-containment-02/test-results.json
```

Twenty new symbolic/numerical checks pass with Python 3.13.5, NumPy 2.3.5 and SymPy 1.14.0. [Results](test-results.json) bind the script SHA-256, versions, constructed inputs, convergence, covariance fixture, negative controls and numerical limits. The prior IC-01 script was also rerun unchanged: 12/12 passed, and its Git blob was matched to the repository. These are local executions; archive CI is a separate safeguard.

The calibrated manufactured example recovers a=0.2000000001414404 from a true fixture value 0.2 and predicts a distinct clock deficit with relative numerical error 1.77e-9. Doubling the time-path sampling reduces the smooth-quadrature error by approximately four. These numbers are software diagnostics, not physical accuracy claims.

**The substantive result is a candidate operational route, not merely another declaration of underdetermination.** It shows exactly how a perturbation path and an independent comparison can close the product ambiguity, and which additional assumptions make that possible.

Next evidence gate: establish a dimensionally compatible, target-independent tau measurement for the same region and prove or test the common meaning of theta across the EM and clock bridges. Only then select a real dataset, freeze a calibration/evaluation split, and compare with conventional physics. Do not substitute the well-measured neutron lifetime for an absent tension measurement.

## ASRP / research provenance

Risks detected: silently merging historical variable meanings; inferring an absolute scalar from one relative clock comparison; declaring a symmetry fatal before testing joint constraints; and disguising a reconstructed trajectory as forward prediction. Checks: explicit compatibility ledger, monotonic branch proof, scale/ref-drift negative controls, integration tests, covariance propagation and source-pinned field substitution. Outcome: a conditional constructive route, with physical compatibility and empirical evaluation still open. No separate independent reviewer was used.
