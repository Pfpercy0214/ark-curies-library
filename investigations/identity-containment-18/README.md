# IC-18 — A responsive environment: baseline, feedback, and collective scale

Local research date: 2026-11-05 (America/Chicago). Execution timestamps are UTC, 2026-11-06. Parent and pinned source head: `5d02af080caf72d48784f16a7414d997c375704f`.

**Status:** source-linked structural extension with executed algebraic/generated checks. Not an identified ARK medium, a universal entropy equation, or an empirical result. Detector work stays paused. No archived source, prior investigation, policy, or manifest is rewritten; no merge authorized.

## Purpose and attribution

The owner proposed that a static background can help establish microscopic identities while its organized disturbances, rather than its undisturbed level, dominate some large-scale observations. This is a hypothesis, not a confirmed scale law. The preceding discussions also asked whether three independent identity anchors fix the environmental contribution, and whether different environments can support the same configuration. [The mechanistic note](../../history/mechanistic-notes/2026-11-05-environment-background-and-anchors.md) preserves those distinctions.

IC-16 specified candidate geometry/history kinetics. [IC-17](../identity-containment-17/README.md) showed that response functions and their reference conditions remain needed to turn that candidate into a physical model. This step resolves **one selected environmental response channel** and asks what happens if it is held fixed, allowed to relax, or eliminated from the displayed equations. It is not another device analogy.

Source statements: XXV A.4 makes omega a dependent internal–external balance; A.5 contains unresolved external modes; E13–E16 puts environmental drive into an effective identity functional. Those passages motivate explicit coupling, but do not uniquely prescribe the environmental energy, dynamics, or its translation from temperature/pressure. The charter's 4.3–4.4 and 5.1–6.8 require declared resolution, independent constraints, qualified partition invariance, and no residual-fitting epsilon. Our added environmental curvature, gradient cost and kinetic law remain **new candidate choices**. See [source record](../../sources/identity-containment-18-environment.md).

## 1. Subtracting a reference is not removing a physical background

Expand a smooth effective energy about a **jointly stationary reference** under specified controls and boundary conditions. Let x denote deviations of the chosen resolved identity coordinates (for example normalized geometry and retained state), and y deviations in selected environmental modes. Locally,

$$F=F_0+\tfrac12 x^T A x-x^T C y+\tfrac12y^T B y+O(\|(x,y)\|^3).$$

A and B are symmetric energy Hessians; C is a cross derivative. The reference state, energy normalization and permitted variations are inputs. Terms linear in freely varying coordinates vanish only at the stationary reference. A constrained reference or unbalanced support requires its constraint forces/linear terms; do not erase them by choosing a convenient origin.

At fixed domain and controls, F0 does not affect derivatives with respect to x or y. Nevertheless A, B, C, and the kinetic coefficients can depend on the physical background. Removing F0 leaves that dependence intact. If physical volume, metric, composition or the background itself is varied, their energy/work terms must be reconsidered. In particular, an arbitrary constant in a finite-system potential is not automatically a measured cosmological vacuum energy.

The code tests an explicit family with A(z0)=3+z0^2/5 and the same zero-deviation equilibrium at every z0. Its curvature changes even though subtracting F0 leaves all state forces unchanged. Constant external pressure can contribute through P0 V(q); that is a specified volume coupling, not merely an additive q-independent offset.

Thus the owner's possible scenario is mathematically intelligible: a background can be implicit in local response properties while a particular force measurement sees only differences. It has **not** been established that ARK's background affects only microscopic scales. That requires its actual response/coupling law.

## 2. Fixed surroundings and responsive surroundings are different contracts

Include independently prescribed generalized controls h and j:

$$F_2=\tfrac12x^TAx-x^TCy+\tfrac12y^TBy-h^Tx-j^Ty.$$

For positive-definite B, minimizing over the environmental coordinates gives

$$y_*(x)=B^{-1}(C^Tx+j),$$

$$\boxed{F_{\mathrm{eff}}(x)=\tfrac12x^T(A-CB^{-1}C^T)x-(h+CB^{-1}j)^Tx-\tfrac12j^TB^{-1}j.}$$

Consequently the response with the environment clamped is A, while the fully relaxed response is

$$\boxed{A_{\mathrm{relaxed}}=A-CB^{-1}C^T.}$$

This is a conventional quadratic elimination, not newly discovered mathematics. Here it supplies a concrete consistency condition for the core reconstruction. The full block Hessian is positive definite exactly when B and its Schur complement are positive definite. A stable minimum with y clamped is not sufficient for stability against all joint variations.

For scalar A=3, B=2, g=0.8, the frozen response is 3 and the relaxed one is 2.68. For B=4, the latter is 2.84. Both can have the same zero-deviation mean. **Same equilibrium configuration does not imply identical environmental response.** This softening is relative to clamping the same reference state. It does not prove that changing external pressure or another background control can never stiffen a system: the reference A itself, preloads and admissible constraints can change.

This elimination computes a conditional stationary response, not a thermodynamic trace over every environmental microstate. At finite temperature, integrating fluctuating modes can supply further terms. No entropy or temperature has been assigned to this deterministic quadratic comparison.

## 3. Three anchors, response-equivalent environments, and residual freedom

A measured identity can constrain the environmental **combination that couples to it** without resolving all environmental components. In the stationary equations above, x responds to h+CB^-1 j. Directions in j that leave this combination unchanged are unidentifiable from x alone. Adding more measurements of x does not necessarily distinguish those directions.

The checks give a rank-three map from four controls to three outputs with an explicit nonzero null direction. This is not a theorem that three ARK anchors fail; it demonstrates why the chosen unknowns and their couplings must be counted. Other fixed relations can remove the freedom.

A scalar environmental summary E(z) is sufficient for a declared response family only if physically different z with the same E yield the same relevant response. A response Jacobian of rank greater than one cannot factor locally through one smooth scalar. Rank one is a necessary local condition, not by itself proof of global equivalence or adequacy for every observable. We test both a rank-two counterexample and a valid rank-one linear case.

Likewise S+epsilon bookkeeping is invariant only when that same sum enters all the specified couplings. Knowing the total does not separate its components. Spatial support, direction, spectrum and timing can require additional resolved channels; they must not be erased to preserve a preferred scalar count. No ordinary thermodynamic entropy is equated to S here.

These findings sharpen a useful hierarchy:

1. Same coarse identity/phase label.
2. Same resolved equilibrium state.
3. Same static response to the designated interventions.
4. Same finite-rate and spatial response.

Agreement at an earlier level does not establish later levels. The ice/pressure observation motivates this distinction, but no new ice phase simulation is performed.

## 4. Removing an environmental coordinate produces history, not its disappearance

For the scalar sector, take

$$F=\tfrac12Aq^2+\tfrac12Bu^2-gqu,$$

and explicitly choose relaxational kinetics

$$\dot q=-M(Aq-gu),\qquad \dot u=-L(Bu-gq),\qquad M,L>0.$$

Then

$$\dot F=-M(Aq-gu)^2-L(Bu-gq)^2\le0.$$

This is an effective relaxation law with a declared energy budget, not a microscopic energy-conserving theory or proof of a superfluid. Heat/noise in an omitted bath is not independently resolved here. Inertia, conserved currents, IC-16's more general tangent mobility and reversible couplings require their own specified extension. The diagonal mobility is one testable choice, not recovered source canon.

The environmental equation can be solved exactly:

$$u(t)=u(0)e^{-LBt}+Lg\int_0^t e^{-LB(t-s)}q(s)ds.$$

Substituting this into the q equation retains an initial-state contribution and a history integral. **An environment no longer displayed as a separate state can remain dynamically relevant through memory.** If the retained coordinate r already includes this same environmental relaxation, independently adding u would double-count it; a layer/variable assignment must decide where the mode resides.

For a sinusoidally prescribed q, the force T=Aq-gu has complex response

$$\boxed{K(\Omega)=A-\frac{g^2}{B+i\Omega/L}.}$$

The low-rate value is A-g^2/B, the rapid-response limit is A, and the environmental relaxation time is t_e=1/(LB). A,B,g fixed with different L gives identical mean and static stiffness but different dynamics. The tests compare an independently integrated ODE with the explicit convolution and the frequency expression. Omega is a probe frequency, not the archived balance omega or a universal clock rate.

The conventional existence of memory in reduced transport descriptions is documented in Zwanzig's 1961 work. Its 1972 correction addresses neglected fluctuations in the nonlinear derivation. We read both abstracts and do not present the earlier general nonlinear formulation as unqualified. Our elementary linear calculation is derived explicitly and does not depend on that contested step.

## 5. Spatial response gives a scale without imposing an on/off mass threshold

To the scalar sector add specified positive gradient costs:

$$F=\int\left[\tfrac12Aq^2+\tfrac12G_q|\nabla q|^2+\tfrac12Bu^2+\tfrac12G_u|\nabla u|^2-gqu\right]dV.$$

At fixed q the relaxed environmental field obeys

$$(B-G_u\nabla^2)u=gq.$$

The boundary conditions are part of the inverse operator. On the infinite-space or periodic linear branch the response to wave number k is

$$u_k=\frac{gq_k}{B+G_uk^2},\qquad
K_{\mathrm{eff}}(k)=A+G_qk^2-\frac{g^2}{B+G_uk^2}.$$

A spatial response length follows:

$$\ell=\sqrt{G_u/B}.$$

In this specified model, environmental feedback is weaker for rapid spatial variation and stronger for broadly organized perturbations. This is conditional on the positive-gradient linear model, not a demonstrated cross-scale law of matter. The local background's influence on A or kinetic coefficients is separate from this additional spatial response. A Gaussian finite-range response operator is a conventional field-theory construction; the library claim is its explicit role and limits here, not novelty.

### A bounded collective-source calculation

Prescribe a uniform small perturbation q0 inside radius R and zero outside, with u tending to zero far away. q0 is a declared configuration-source amplitude, **not a derived matter density, mass, or impermeable exclusion volume**. This is a forced-response calculation, not a self-bound object. The source step is a spatial-control idealization; no q-interface energy or particle stability is inferred from it.

Solving the same environmental equation gives

$$\boxed{\frac{u(0)}{gq_0/B}=1-(1+R/\ell)e^{-R/\ell}.}$$

| R/ell | Center response as fraction of the broad-source limit |
|---:|---:|
| 0.1 | 0.00467884 |
| 0.5 | 0.09020401 |
| 1 | 0.26424112 |
| 3 | 0.80085173 |
| 5 | 0.95957232 |

At small R the fraction is R^2/(2ell^2)+higher terms; it approaches unity for large R. The response is nonzero at every positive size. There is no hand-inserted threshold at which the medium begins to interact. This compares **fixed source amplitude with growing size**, so the total prescribed source grows too. Fixed-total and changing-shape comparisons are different experiments.

Inside and outside, the field and its normal derivative match. No impermeable wall is inserted. These static conditions alone do not define the transport of material through the configuration.

The analytic center value is checked against the three-dimensional Green-function volume integral. The entire radial profile satisfies the differential equation and matching conditions symbolically. An independent finite-difference boundary-value solve converges at second order. Its distant boundary value is supplied from the analytic exterior, so this is an implementation check, not a new empirical boundary prediction.

The exterior is proportional to exp(-r/ell)/r. **This is a screened response, not a derivation of gravity.** Sending B to zero at fixed finite A and nonzero g violates AB>g^2 for unrestricted uniform joint variations. Conservation restrictions, nonlinear stabilization, different cross-couplings or a different physical energy may change that conclusion, but must be derived. The candidate cannot acquire a gravitational interpretation by silently deleting the stabilizing term.

## 6. A constructive environmental recovery, with its remaining freedom

For this declared scalar response, independently characterized A and g, plus measurements of slow stiffness Ks, spatial response length ell and relaxation time te would give

$$B=\frac{g^2}{A-K_s},\qquad G_u=B\ell^2,\qquad L=\frac{1}{Bt_e}.$$

That is a concrete example of independent channels constraining the surroundings. It requires A>Ks, a specified mode, an energy/coordinate calibration and a common state/regime. It is not a universal three-point theorem: A and g are additional known inputs, not forgotten unknowns. A generated example recovers B=2, Gu=8, L=0.3, then computes a separate spatial-mode response. All generating values were visible during development; no blind validation is claimed.

Without independent normalization of u and its coupling, the transformation

$$u'=\alpha u,\quad B'=B/\alpha^2,\quad G_u'=G_u/\alpha^2,
\quad g'=g/\alpha,\quad L'=\alpha^2L$$

leaves the identity's static, spatial and dynamic response invariant. Thus those observables need not determine an absolute environmental amount. A measured environment-side observable or another independently grounded scale is required. Calling the unidentified variable entropy does not resolve the ambiguity.

If source distributions superpose linearly, eliminating u also produces cross terms between sources in the effective energy. The interaction is determined by the response kernel and their arrangement; it is not automatically additive in geometric volume or proportional to inertial mass. The code checks one finite-dimensional example of this cross term. No equivalence-principle or universal coupling result is claimed.

## 7. Environmental specification to carry into the core

[environment-contract.json](environment-contract.json) records what must be explicit:

- Identity/complement resolution, permitted variations, physical reference state and whether a mode is prescribed or dynamically resolved.
- Independent physical controls and their coupling map; pressure/temperature/fields are not directly added without compatible units and justified couplings.
- Reference forces, local susceptibility/curvature, spatial response, relaxation/inertial response, boundary input and exchange.
- Which combinations are observable, which environmental partitions remain unresolved, and which additional observations distinguish alternatives.
- Different validity regimes for mean equilibrium, local stability, finite-rate response and collective behavior.

The next core task is to fill one **source-grounded coupling map** into this contract, or reject this extension in favor of a better one. It should determine whether the archive's pressure-like drive changes only the source term or also the stabilization/kinetics. This is not permission to fit each coefficient to every target. The response functions must be derived or calibrated independently and then used to predict a different observable. No new detector, ice, or galaxy-modeling branch is needed for that gate.

## Verification and limitations

Run `OPENBLAS_NUM_THREADS=1 python check_environment.py --output new-results.json`. The first 12-group suite passed. A constructive environment-recovery check was then added, and the final **13/13** groups passed, with a repeat producing identical substantive output except the UTC timestamp. Initial code results and logs remain in the packet. No failed execution is hidden; no failures occurred in these runs.

Tests include symbolic variation, joint versus reduced minimization, matrix-exponential/ODE comparison, convolution/forced response, scalar-summary counterexamples, normalization degeneracy, Fourier/dense agreement, exact interface matching, quadrature and radial refinement. Their passing establishes only the stated implementation and mathematical consequences. No experiment, fitted ARK parameter, universal clock law, unrestricted nonlinear stability proof or independent reviewer.

The unchanged IC-17 script was matched to remote Git blob `d66e6a800dfca751980b15da7a63eb72c931a9c6` and rerun: **13/13 pass**. Its fresh report/code are in the packet, not substituted for its prior repository record. IC-01–16 were not rerun. No NIST data, source PDFs or complete local archive audit were used. Preservation CI and published file hashes are checked separately after committing.

ASRP interventions: distinguish zero-of-energy from physical background; maintain reference constraints; do not double-count environmental history in r and u; do not interpret a scalar-response fit as absolute entropy; keep fixed-amplitude versus fixed-total scaling separate; do not promote a screened forced response to gravity or a stable particle. Standard mathematics and the owner's organizing idea are both useful without being evidence of an identified universal medium.
