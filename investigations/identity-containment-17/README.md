# IC-17 — Energy, boundary response, and the meaning of stiffness

Local research date: **2026-11-05, America/Chicago**. Execution timestamps are UTC (2026-11-06). Source/parent commit: `fd5663bf5cae6f8c99b63b63fdc349ca99ee07ae`.

**Status:** source-linked structural reconstruction and conditional mathematical checks. Not a canonical replacement, empirical validation, or uniquely identified ARK medium. IC-10–14 remains paused. No detector or experimental files were read.

## Purpose and source boundaries

[IC-16](../identity-containment-16/README.md) supplied a candidate coupled geometry/history model. Its missing physical connection was the relation between stored energy, boundary stress, and the several roles assigned to stiffness. This study addresses that connection instead of adding another device analogy.

The pinned source statements are deliberately not merged into an assumed universal law:

- **Paper I, section 5:** stored energy is written as `E=1/2 k^c(Delta theta^c)^2`, with stiffness allowed to differ by scale/system. The inspected numerical illustration prints `N rad^-2` for a quantity used to calculate joules; an energy-length conversion is not supplied in that passage. We do not silently repair it or endorse its experimental claims.
- **Paper XVIII, sections 2.2–2.3 and expanded recursion:** tension memory integrates `k^c d theta^c`; `k^c=1/theta^c` and a logarithmic memory expression are restricted normalized approximations. Independent physical anchors and context are explicitly requested by the source.
- **Paper XXV, A.2–A.4:** resistance, boundary adaptation, the schematic stress integral, and dependent internal–external balance. The tensor/scalar character, contraction and units of the causal-stress integral are not fully specified there.
- **Paper XXV, E13–E16:** an effective spatial-gradient functional and its fixed-parameter equilibrium variation. It does not independently identify the functional as a measured total energy with a complete material-deformation law.

These references are mapped by section, path, blob and inference role in [source-map.json](source-map.json). The source documents remain unchanged. Definitions below use neutral labels until a physical ARK identification is justified.

## 1. Derive a whole-identity response from a field energy

Consider the quadratic sector of the functional class, with fixed environment and retained state, constant spatial coefficient `G`, and local curvature `a`:

$$F[q]=\frac12\int_\Omega\left[G|\nabla q|^2+a q^2\right]dV.$$

The reference is chosen stationary, with its reference energy removed. Let a declared deformation shape be `h(x)` and its amplitude `A`, so `q(x)=A h(x)`. Direct substitution gives

$$\boxed{F=\frac12 K_h A^2,\qquad K_h=\int_\Omega\left[G|\nabla h|^2+a h^2\right]dV.}$$

This is a conditional bridge from the later field formulation to an earlier whole-configuration quadratic expression. **The effective stiffness includes the shape, size, normalization and constraints of the configuration. It need not equal the local gradient coefficient.** No separate fitted stiffness was introduced for each mode.

For unit cross-section, `h_n=sin(n pi x/L)`, `L=2`, `G=2`, `a=3`, the first three generated mode stiffnesses are 7.9348022, 22.7392088 and 47.4132198. Direct quadrature matches the analytical result. Two generated mode values recover the specified G/a and determine the third; this is an implementation demonstration, not a blind measurement test. Rescaling h also rescales its amplitude and coefficient; the stored energy remains invariant. Comparing bare coefficients without a shared mode normalization would be misleading.

This reduction is local/quadratic and holds the stated fields fixed. A nonlinear state-dependent coefficient, finite amplitude, adapting history, or a changing boundary requires the corresponding full variation. Nothing here identifies a sinusoidal mode amplitude as the clock-measured theta of an actual object. Boundary values alone also do not reconstruct an arbitrary interior: the implemented counterexample has identical endpoint values and different internal energies. A sufficiently specified field equation and boundary problem may remove that ambiguity.

## 2. Three legitimate stiffness descriptions must not be conflated

Let `U(q,r,E)` be recoverable energy in declared normalized coordinates, with retained state r and environment E held fixed during a partial derivative. Define a work-conjugate response and tangent stiffness:

$$T=U_q,\qquad K_t=U_{qq}.$$

These are proposed energetic observables, not automatic definitions of tau^c and kappa^c. With a fixed reference q0 and Delta=q-q0, define

$$K_s=\frac{T-T_0}{\Delta},\qquad K_E=\frac{2(U-U_0-T_0\Delta)}{\Delta^2}.$$

Ks is a secant response; KE is the coefficient that represents the accumulated energy as a quadratic expression at the current state. For a nonlinear law they generally differ from Kt. The constant-stiffness regime makes all three equal. This is standard elasticity bookkeeping, used to clarify source compatibility rather than replace ARK by a material model.

When a fixed-state tangent law is independently specified, there is a constructive energy family:

$$\boxed{U=U_0(r,E)+T_0(r,E)\Delta+\int_{q_0}^{q}(q-u)K_t(u,r,E)du.}$$

Thus

$$K_s=\int_0^1K_t(q_0+s\Delta)ds,\qquad K_E=2\int_0^1(1-s)K_t(q_0+s\Delta)ds.$$

The tangent, secant and energy coefficient sample the same curve differently. If instead KE is specified in `U=U0+T0 Delta+KE(q)Delta^2/2`, then

$$K_t=K_E+2\Delta\,\partial_qK_E+\frac{\Delta^2}{2}\partial_q^2K_E.$$

Substituting a state-dependent coefficient into the quadratic formula and then differentiating as though it were constant omits those terms. If the coefficient depends only on r/E and these are clamped, the corresponding q derivatives vanish; that is a legitimate distinct regime.

### A constructive branch, not a silent correction

Take XVIII's positive normalized tangent `Kt=1/q` and additionally hypothesize that its integrated tension is a work-conjugate response. At an explicit positive reference q0, zero reference response/energy gives

$$T=\ln(q/q_0),\qquad U=q\ln(q/q_0)-q+q_0.$$

This is convex on q>0 and has a minimum at q0. At q0=1, q=2, it yields `Kt=0.5`, `Ks=0.69314718`, `KE=0.77258872`. These are three descriptions of one generated law, not three disagreeing measurements.

By contrast, putting `k=1/q` pointwise into the literal flat-reference `U=kq^2/2` yields U=q/2 and zero second derivative. Both expressions cannot have that same k as their tangent stiffness on the same branch. **This is a conditional incompatibility of identifications**, not a whole-theory disproof: the quadratic k may be an energy coefficient, the tangent law may use a different normalization/regime, or the physical coupling may be different. The source's singular normalized branch cannot be integrated from q0=0 without a new prescription. We preserve the alternatives rather than select a convenient one.

## 3. Reference information remains physical information

The tangent law leaves U0 and T0 undetermined. When the retained state or surroundings vary, these are functions of those states, not merely two harmless constants.

Adding a function of r/E to U leaves its q-force and q-stiffness unchanged, while changing the retained-state force and environmental work. Adding `B(r,E)(q-q0)` preserves tangent stiffness but shifts the geometric response. The checks exhibit both cases.

Consequently, two independently grounded identity quantities plus a third relationship can be sufficient for a specified target, but the reference response, energy baseline and coupling must be accounted for. A missing reference is not an invitation to choose the target result. A common energy-density reference applied consistently to both sides of an interface can cancel in a stress difference; an unmatched offset must not be treated as a new physical pressure.

For proposed reversible forces in a complete smooth state space, the mixed derivatives must agree, for example `partial_r T=partial_q A_r`. The code checks an integrable pair and a counterexample with nonzero closed-loop work. A hysteretic *projected* response may have nonzero loop work because hidden state or dissipation is present; the exactness test does not prohibit such physics.

## 4. Retained state and measured response can be alternative coordinates

A significant constraint on the IC-16 interpretation is now explicit. Its independent retained state r must not automatically be equated to `U_q` while all other equations are left unchanged.

For a general local two-field energy, the map `(q,r)->(q,T(q,r))` is locally invertible when `T_r` is nonzero. It can represent the **same two-state mechanics**, not necessarily require a third state. But gradients and kinetics must transform as well. If `x_dot=-M grad_x U`, `y=Y(x)` and `J=partial Y/partial x`, then

$$\nabla_yU=J^{-T}\nabla_xU,\qquad M_y=J M J^T.$$

The example `U=(3q^2+0.8qr+2r^2)/2` has `T=3q+0.4r`. Rewriting the overdamped IC-16 sector in `(q,T)` preserves its trajectories, energy and dissipation to numerical precision. Renaming r as T without transforming the mobility gives different trajectories. This calculation uses a constant Jacobian; general inertial/state-dependent transformations require their additional terms.

An overly strong alternative assumption, `r=U_q` identically for two independent local coordinates, gives `U=qr+H(r)` and local Hessian determinant -1. It cannot be a strictly convex unconstrained stored energy in both coordinates under that assumption. Mixed force-control potentials, constrained state surfaces or a properly transformed chart are different cases, not refutations of the physical use of a response variable.

The full derivative of a measured T is also generally

$$\dot T=K_t\dot q+T_r\dot r+T_E\dot E.$$

The archived tangent relation is recovered only under the corresponding restrictions or with an explicit combined derivative. History can change the response while q is held constant. The candidate does not decide whether historical tau is the latent state or the response observable; it now provides a disciplined way to compare those readings.

## 5. Boundary stress needs a deformation rule, not just a surface

XXV A.3 writes a causal-stress boundary integral without fully fixing its tensor character, contraction or displacement coordinate. If sigma is interpreted as ordinary Cauchy stress, integrating traction yields a net vector force. The load conjugate to a specified boundary mode A is instead

$$\mathcal L_A=\int_{\partial\Omega}(\sigma\mathbf n)\cdot\frac{\partial\mathbf x}{\partial A}\,dA.$$

Here A in the derivative is the mode coordinate; dA denotes area. Body forces, inertia, field exchange and irreversible losses require their additional work terms. This expression alone is not a complete total-energy measurement protocol.

A sphere under a declared uniform outward traction has zero net translational force but nonzero radial-mode work. Surface quadrature and the volume-work derivative agree. For a dimensionless mode, the generalized load has energy units; for a length coordinate, it has force units. No claim is made that either is automatically the source's tension-memory unit.

Likewise, a field variation and a physical domain deformation are distinct. For an energy density `w=G|grad q|^2/2+V(q,r)` and an explicitly assumed material-scalar advection rule, an affine domain variation produces

$$\Sigma_{\rm shape}=wI-G\nabla q\otimes\nabla q.$$

The code verifies this shape derivative independently by perturbing the deformation matrix. It is the variational stress for that transport contract, not an automatic complete physical stress of the proposed medium. If an argument is instead conserved density `n=N/Volume`, an otherwise identical uniform current-volume energy `Volume*f(n)` gives `p=n f_n-f`; holding a scalar label fixed gives `p=-f`. These differences show why the transport rule cannot be inferred from the mere presence of a scalar energy.

This does not assert that a clock angle is a material density or an advected tracer. That is precisely a missing source-to-mechanics identification. Permeability and exchange remain explicit open inputs, not forbidden by a boundary-energy description.

## 6. Normalization must preserve the physical work

For a three-dimensional energy `F=E0 integral a d^3(x/L0)` and `q=theta/theta0`, the corresponding scales are:

| Role | Scale |
|---|---|
| Whole-mode energy stiffness | E0/theta0^2 |
| Spatial-gradient coefficient | E0/(L0 theta0^2) |
| Local energy-density curvature | E0/(L0^3 theta0^2) |
| Work-conjugate geometric response | E0/theta0 |

A stress-area integral supplies a force; multiplying by the appropriate displacement-per-mode factor supplies the generalized work load. An action-like J s quantity needs another independently specified conversion before being equated to an energy-like load. IC-16 documented that issue for XVI; we do not redefine it here.

Finally, scaling U by lambda and overdamped mobility by 1/lambda leaves the trajectories unchanged but changes the force/energy scale. A numerical evolution cannot determine its absolute energy calibration by itself. Independently measured energy, work, geometry and references are legitimate anchors, not prohibited fitting inputs.

## 7. What this resolves and the next structural gate

Completed: a conditional field-to-whole-identity energy map; distinctions among energy/secant/tangent coefficients; a general energy family reconstructed from a tangent law; constraints linking retained-state and response coordinates; and the mode/transport contract needed to turn boundary stress into an energetic scalar. This gives concrete compatibility tests instead of declaring different historical symbols either identical or irreconcilable.

Still not supplied: a unique constitutive potential, which source definition of tau is operational, the actual material/metric coupling of clock-defined theta, an absolute energy normalization, or a physical relation identifying spatial coefficient, integrated response and history. The standard continuum relationships do not establish ARK's underlying medium.

**Next gate:** assemble one versioned constitutive specification choosing the retained-state/observable chart, physical energy measure, geometry/transport coupling and reference conditions. Then test whether its energy-derived responses satisfy the archived governing relations simultaneously. Only introduce a new coupling where the source leaves it open, and label it. No return to detector fitting is needed for this gate.

## Verification record

Run `OPENBLAS_NUM_THREADS=1 python check_energy_map.py --output new-results.json`. All **13** symbolic/generated check groups passed on the first run; the repeat had identical substantive output apart from its UTC timestamp. Checks include independent quadratures, finite-difference refinement and exact matrix-exponential comparisons. The tests were designed with the formulas visible; no independent second reviewer or experimental data were involved.

The unchanged IC-16 script from the mounted packet was matched to Git blob `ad80d1b2b9e1f03fb0bdf68ef222bb4cad8ac2d9` and rerun: **11/11 pass**. The fresh rerun is in the downloadable packet, not substituted for its historical report. IC-01–15 were not rerun. No local complete-archive verification, source-PDF re-audit, empirical fit or author contact occurred. Remote preservation CI and publication hashes are separate checks.

Sources actually read and limitations appear in [the source record](../../sources/identity-containment-17-energy-stress.md). Personal-context retrieval helped preserve the owner's mechanistic priorities but was not used as scientific evidence or as a verbatim historical transcript. ASRP focus: preserve source roles; do not merge different stiffness definitions; do not convert a new integrable potential into recovered canon; do not equate net force to all boundary stress; and do not conceal physical scales inside normalization.
