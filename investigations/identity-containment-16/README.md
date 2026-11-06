# IC-16 — A source-linked candidate for coupled geometry and retained history

Date: 2026-11-05 (UTC). Parent/source commit: `8f76c310c5beb5e36a3a974dad9e9ec451f0d4b1`.
Status: **candidate structural completion with executed consistency checks, not an established physical core**. The NIST/detector track remains paused. No historical paper, previous study, policy, manifest or source repository is changed; PR #2 is not merged.

This continues [IC-15](../identity-containment-15/README.md) by supplying a versioned state/normalization contract and an explicit candidate coupling. It does not try to make all archived equations simultaneously true. Source statements, mathematical deductions, and new choices are separated below and in [core-contract.json](core-contract.json).

## 1. Source map and the decision we actually need

Pinned sources:

- [XVI](../../raw/papers/paper-016-kernel-mechanism-conv-01.md), 2.1–2.6: integrated tension memory, stiffness and a pressure-driven collapse relationship. Its printed dimensional assignments need a bridge: the integral of kappa times theta-dot over time has the units of kappa for dimensionless theta. With the printed N/m for kappa and J s for tau, a direct equality is not dimensionally complete. A conversion would have dimensions length-squared times time. None is inferred here. This is a scoped equation/unit finding, not evidence that every later normalized formulation fails.
- [XVIII](../../raw/papers/paper-018-recursive-scalar-geometry-conv-01.md), 2.2–2.5 and expanded recursion in 3: tau integrates kappa*dtheta; kappa=1/theta is an isotropic/normalized approximation, and tau=log(theta) is restricted to normalized collapse models. The text explicitly cautions against deriving one scalar from another without the physical context and independent measurement anchors. These formulas are not promoted to universal laws here.
- [XXV](../../raw/papers/paper-025-disciplined-containment-conv-01.md), A.1–A.5: clock-ratio geometry, resistance proxies, boundary-adaptation memory, dependent pressure-balance omega and unresolved environment. A.4 says omega does not propagate independently. In contrast to older frequency/anchor terminology, pressure balance is not automatically inverse seconds.
- XXV E6/E12/E13–E16: spatial exchange, an inertial variant, and the effective functional. The source gives the functional class, not a unique U, kinetic coefficient or memory law. D.1 gives another schematic inertial/environmental equation; compatibility with it remains a condition, not an automatic consequence of using the same symbols.
- [Charter v1.1](../../raw/epistemics/ARK_Epistemic_Charter_v1.1.md), 4–6.9: distinguish versions, scale, measured input, latent state, output and calibrated mapping; report unresolved families rather than force uniqueness.

The owner's intended mechanism remains: organization can persist through exchange; geometry, resilience and history jointly affect the response; the environment participates; omega is not an independently acting stabilizer. These are hypotheses guiding reconstruction, not observations of the proposed medium.

**Working structural decision:** carry a geometry variable and a retained variable as resolved fields when history is not uniquely recoverable from current geometry. Treat kappa and omega as declared state functions only when actual constitutive maps are supplied. Alternatively retain them as independent variables with their own equations. Neither independence nor dependence follows from the number of symbols.

## 2. What the normalized historical branch does and does not remember

On the specific branch `d tau = kappa d theta`, `kappa=1/theta`, with positive dimensionless theta,

$$r-r_0=\ln(q/q_0).$$

The reference `r0-log(q0)` persists. However, a closed excursion in q has zero accumulated change in r. This branch does not encode additional path history once that reference is fixed. Calling the integral memory does not change this mathematical property.

That is not a rejection of the general integrated relationship. If its coefficient depends on another state or a changing environment, two paths can give different integrals. The code checks a simple closed q trajectory with a prescribed varying coefficient. A separate relaxation channel can also modify the reference. These alternatives must be specified, not silently combined with the path-independent approximation.

## 3. Normalization and state contract

Use dimensionless coordinates `xi=x/L0`, `s=t/T0`, geometry `q=theta^c/theta0`, and retained-state deviation `r=(tau^c-tau_ref)/tau0`. All scales/references require independent physical characterization for empirical application. Signed r denotes a deviation, not a claim of negative absolute persistence. No log of a dimensional quantity is used.

Let `E(xi,s)` denote a specified environmental input at the chosen resolution, not a measured thermodynamic entropy. A decomposition E=S+epsilon is allowed only when both terms truly enter the same normalized physical channel. If the complement changes dynamically, E needs a measured history or a coupled law; it cannot be selected from output residuals.

The following roles are distinct:

| Quantity | Candidate role | Missing physical connection |
|---|---|---|
| q | Independent geometry field | Which operational theta map and reference apply? |
| r | Independent retained field, or equivalent history functional | Which boundary observable fixes its scale and initial state? |
| k=K(q,r,E) | Proposed dependent resistance descriptor | Does current resolved state suffice, or is additional history needed? |
| Kg=Cg(k,...) | Spatial-gradient energy coefficient | Map and scale relating it to the archived kappa |
| b=Ct(k,...) | Coefficient in the normalized tangent relation dr=b dq | Its relation to Kg is not automatically equality |
| w=W(q,r,E) | Dependent balance descriptor entering stabilization | Pressure normalization and actual function; not a frequency |
| chi, zeta, L | Inertia, damping and independent memory relaxation | Kinetic functions/measurements not determined by equilibrium alone |
| E and boundary data | Prescribed input or explicitly resolved complement | Coupling, exchange and baseline; missing is not zero |

In three physical dimensions, if an effective energy is F=E0*A, its gradient coefficient in front of `|grad_x theta|^2/2` is `E0*Kg/(L0*theta0^2)`. The dimensional tangent coefficient is `tau0*b/theta0`. These generally have different dimensions. Normalizing them does not establish physical equality; a constitutive bridge is required. Source XVI's inconsistent direct unit assignment cannot be fixed merely by dropping units.

When inertia is retained, q-dot is an additional initial datum. Two field names do not mean two numbers describe an entire physical identity. Spatial profiles, boundary conditions and references remain part of the state specification. The compact definitions do not prove sufficiency for all domains.

## 4. One explicit candidate energy, with all dependencies varied

Use the source's functional structure, but declare a candidate two-field version:

$$\mathcal A[q,r;E]=\int_{\mathcal V}\left[\tfrac12K_g(q,r,E)|\nabla q|^2+\widetilde U(q,r,E)-P(E)q\right]d\xi,$$

where `U_tilde(q,r,E)=U(q,r,W(q,r,E))` when the source's dependent omega enters U. Kg is positive. The retained state is local in this first candidate; no unannounced gradient penalty for r has been added. Nonlocal or higher-dimensional history may ultimately be necessary.

Holding the specified environment fixed during this variation gives

$$g_q=-\nabla\cdot(K_g\nabla q)+\tfrac12 K_{g,q}|\nabla q|^2+\widetilde U_q-P,$$

$$g_r=\tfrac12 K_{g,r}|\nabla q|^2+\widetilde U_r.$$

The partials of U_tilde include `U_w W_q` and `U_w W_r`. At the boundary the q variation contributes `Kg*dq/dn*delta(q)`. Prescribed external E does not acquire an equilibrium equation by being written as an argument. If E is instead a resolved dynamical state, its own energy and evolution/exchange law must be included.

The coefficient and chain terms are required by the chosen dependencies; they are not arbitrary repairs. Conversely, the source's fixed-parameter variation remains correct for that different contract. An equation obtained holding r or kappa fixed cannot be promoted to a fully coupled variation by substitution alone.

## 5. Completing the tangent relation without losing feedback

The historical integrated relation motivates `r_dot=b*q_dot` in a restricted branch. It does not by itself specify a complete reciprocal evolution for the joint energy.

A useful counterexample: take energy gradients gq=1, gr=-3, b=1. Updating only geometry by `q_dot=-gq=-1` and then appending `r_dot=b*q_dot=-1` gives `A_dot=+2` with no declared work. Such a rule can be used for an externally driven process only if that input is accounted for; it is not automatically a passive relaxation of the proposed energy.

We propose, rather than recover from the papers, a positive quadratic rate potential:

$$\mathcal R=\int\left[\frac\zeta2\dot q^2+\frac{(\dot r-b\dot q)^2}{2L}\right]d\xi\quad(L>0,\zeta\ge0).$$

Minimizing `R+A_dot` at a fixed current state gives the overdamped equations. Adding a constant positive inertial coefficient gives the candidate parent system

$$\boxed{\chi\ddot q+\zeta\dot q=-g_q-b g_r,\qquad \dot r=b\dot q-Lg_r.}$$

For L=0 take the tangent constraint directly rather than divide by zero in R. chi=0 with zeta>0 supplies the overdamped limit. The symmetric quadratic choice is a conventional dissipative construction; it is not a uniquely inferred microscopic law. Reversible cross-couplings and additional transport structure are not excluded by this calculation.

For chi=0 define M=1/zeta. The mobility is

$$\begin{pmatrix}M&Mb\\Mb&Mb^2+L\end{pmatrix},\qquad \det=ML.$$

It is positive semidefinite for M>0, L>=0. This explicitly connects the tangent response to the force on geometry: **the retained variable affects the geometric update rather than being only a diagnostic updated afterward.**

The total candidate energy `H=A+integral(chi*q_dot^2/2)` obeys

$$\boxed{\dot H=-\int(\zeta\dot q^2+L g_r^2)d\xi+\int f_E\dot E\,d\xi+\oint K_g\partial_nq\,\dot q\,dA.}$$

This assumes fixed coordinates/domain and constant chi; moving physical boundaries, variable inertia and other work channels need their corresponding terms. Fixed drive and vanishing boundary work make H nonincreasing. When zeta=L=0, the candidate conserves H. Neither a decreasing effective functional nor its conservative limit proves physical total-energy identification or superfluidity.

No-flux conditions are not silently prescribed for all identities. The periodic verification domain only removes boundary work for that test. Neither q nor r is identified as a conserved material density. Permeable identities and conserved particle/charge currents still require a proper observable/flux map.

## 6. Equilibria and reductions must retain their constraints

With chi=0, M>0 and L>0, stationary states satisfy gq=gr=0. With L=0, only `gq+b*gr=0` is required along the accessible tangent direction. A state can therefore be stationary on a constrained branch while not minimizing energy over all independently varied states. It is not a contradiction and not proof of unrestricted stability.

For b=1/q and L=0, the candidate preserves `r-log(q)`. With L>0,

$$\frac d{ds}(r-\log q)=-Lg_r.$$

Thus the source's normalized integral can be a genuine restricted reduction, without asserting that every history-dependent state must lie on it.

Two reductions must not be confused:

- **Prescribed constitutive relation r=T(q):** the reduced force is `gq+T'(q)*gr`, and its curvature includes the additional `T''(q)*gr` term. Our L=0 tangent-compatible branch uses this constrained derivative when such a local relation exists.
- **Relaxed internal variable:** solve `gr=0` for r=r*(q), where a regular stable branch exists. The reduced force is gq by the envelope relation. The reduced curvature is the Schur complement `Aqq-Aqr*Arr^-1*Arq`, not the frozen-r curvature. In a spatial problem this may be a nonlocal operator; the simple example below is local.

Clamping r is a third intervention. In the chosen rate potential, r_dot=0 leads to an effective damping `zeta+b^2/L` for L>0. Simply deleting the r equation after solving the coupled system does not implement that clamp. In a properly declared fixed-parameter sector, the resulting positive effective mobility D recovers IC-15's source compatibility `F=D(Pi-Uq)`. Agreement of equilibrium alone still does not select the kinetic coefficient.

For XXV D.1, with matched normalization and chi corresponding to its inertial coefficient, compatibility would require its combined right-hand side `(tau/kappa)*S_dot+Lambda` to match `gq+b*gr+div(Kg grad q)+zeta*q_dot`. This is a required identity to derive from physical couplings, **not a definition of S_dot from a residual**. The candidate does not claim to have established it.

## 7. A closed realization tests the structure without using a detector target

For a local quadratic linearization choose

$$A=\tfrac12a q^2+cqr+\tfrac12d r^2,\qquad a=3,\ c=0.4,\ d=2,\ b=0.6.$$

These numbers are declared dimensionless inputs to a consistency example, not measured ARK constants. The same energy produces three different stiffness responses:

| Response condition | Coefficient |
|---|---:|
| Retained variable held fixed | 3.00 |
| Retained variable fully relaxed | 2.92 |
| Rapid tangent-constrained response | 4.20 |

For finite relaxation L and a sinusoidally imposed geometry, the internal contribution to the force has modulus

$$K_{\rm int}(\Omega)=a+2bc+b^2d-\frac{(c+bd)^2/d}{1+i\Omega/(Ld)}.$$

The full required drive additionally includes inertia and direct damping when present. The calculation matches a separately integrated sinusoidal response and an explicit causal memory integral. This shows how a local two-state formulation and an appropriate history-dependent one-state description can represent the same chosen dynamics. Merely replacing r by its equilibrium value does not preserve finite-rate behavior.

The angular rate Omega here is an excitation/spectral variable, not XXV's pressure-balance omega. With chi=0.7, zeta=0.4, L=0.3, the unforced linearized system has roots approximately `-0.415144` and `-0.378142 +/- 2.426087 i`. These rates follow from the declared equations; none was assigned as an independently acting anchor. Their physical time scale remains uncalibrated.

A second, nonlinear 24-site periodic realization uses

`Kg=1+0.2q^2+0.1r^2`, `b=0.7Kg`, `w=q^2 Kg-E`,

`U_tilde=0.5(q-0.6)^2+0.3(q-0.6)r+r^2+0.1w^2`, `P=0.05E`,

with prescribed E(s)=0.4+0.05 sin(0.7s). This is a completely specified finite-dimensional demonstration of the candidate, not a derivation of these functions from the archive. Its exact discrete energy gradient includes both Kg derivatives and the w chain rule. The cumulative energy balance, including environmental work, closes to about 1.1e-11 over the tested interval. That is a numerical consistency result, not a claim of physical accuracy, continuum convergence, or global well-posedness.

## 8. What is completed and what is still open

Completed: source/version distinctions, an explicit normalization contract, an energy-consistent tangent/history candidate, its constrained and relaxed reductions, and reproducible mathematical checks. This is more than another example of a familiar object, but less than a uniquely specified physical ARK core.

Still required for a physical model:

1. Operational maps and scales for q/r and the different resistance roles; adequacy of a single retained field.
2. A physically grounded joint stabilization functional and constitutive maps Kg, b, W, P. These must be fixed independently of the target.
3. Inertial, relaxation and boundary-exchange laws, including the relation to XXV D.1 and any genuinely conserved quantity. The kinetic parameters cannot be inferred from equilibrium alone.
4. A specified environmental state or complement evolution, with permeability and input work accounted for. E is not chosen to force the desired outcome.
5. An observable map and distinct test. No universal clock law, stable particle, charge quantization, or cross-domain success follows from the current consistency checks.

The next core task should address the missing **energy/stress and scalar-normalization map** using the archived definitions. It should not return to NIST fitting or add another physical analogy unless it resolves one of these declared structural choices. Treat this candidate alongside alternatives; do not promote it to source canon because it has code.

## 9. Verification and source access

Run `OPENBLAS_NUM_THREADS=1 python check_core.py --output new-results.json`. Eleven check groups passed on the first execution; the full run was repeated with identical substantive results excluding its timestamp. They cover the historical normalized path, dimensional bridge, responsive variation, environment partition, reciprocal kinetics, energy balance, constraint reductions, linear evolution and timestep refinement, frequency-dependent history, and a nonlinear finite-lattice realization. Tests were developed with the formulas visible, not blind or independently reviewed.

The unchanged IC-15 script was matched to Git blob `44d3fb8dd40ee35f86f4e0450c0f2ebdae5b39bb` and rerun: six checks passed. Its fresh report is included in the packet, not substituted for the old result. IC-01–14 were not rerun. No source-PDF audit, local whole-archive verification, empirical fit or NIST analysis occurred. GitHub archive-preservation CI is a separate check after publication.

Repository reads: pinned PR metadata; AGENTS, entry protocol, POLICIES, chronology, decisions, wiki index, IC-15 README/handoff; charter sections 4–6.9; XVI opening/2.1–2.6; XVIII opening/2–3.2 and shorter 2.3–3 excerpt; XXV 9/10 opening, A.1–A.5 and C.4–D/E with E6–E16 read explicitly. Some long tool ranges were truncated; no unseen portion is claimed as read. Source blobs: XVI `12c1405afed8785a9e14f235ebefffc26d77e09e`, XVIII `3dc7c4b0e1ea9634af2496efbf43baedef4ad7e5`, XXV `3bbf2a40a7c4bdde67f4bbeb2a29147f10a036f5`, charter `ae341b2a7e30fc1d25703a1f6dbc032595fec707`.

External baseline, consulted 2026-11-05:

- Onsager, *Reciprocal Relations in Irreversible Processes II*, Phys. Rev. 38, 2265 (1931), DOI 10.1103/PhysRev.38.2265; publisher abstract read at https://journals.aps.org/pr/abstract/10.1103/PhysRev.38.2265 . Supports the conventional role of quadratic dissipation and coupled rates under specified assumptions. We did not establish microscopic reversibility for ARK, read the full PDF, or claim Onsager uniquely implies our rate potential.
- Idaho National Laboratory, MOOSE, *Basic Phase Field Equations*, https://mooseframework.inl.gov/moose/modules/phase_field/Phase_Field_Equations.html . Official documentation read for the distinction between free energy, kinetics, and conserved/nonconserved field evolution. It does not supply a physical ARK mapping. No software-library API is used from that page.

ASRP: distinguish source from completion; a normalized log branch from general memory; spatial-energy stiffness from a tangent coefficient; prescribed environment from an equilibrated variable; pressure-balance omega from an oscillation rate; and passive energy accounting from physical validation. A coherent candidate is useful precisely because its remaining constitutive and observational commitments are visible.
