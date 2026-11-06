# IC-06 — Field energy, boundaries, and the missing rate law

Date: 2026-11-01. Mode: source audit and conditional construction. Status: DERIVED-CONDITIONALLY / synthetic verification; empirical identification and independent second review pending. Parent research head: `885abb9622933ebe7ea0db089dd392f84cfa409d`. Historical papers and policies are unchanged.

## Question and source contract

Can one specified medium model determine a boundary's organization, its restoring response, and disturbance rates without assigning these independently after seeing observations?

The immediate source is [Paper XXV, Appendix E](../../raw/papers/paper-025-disciplined-containment-conv-01.md), especially E6, E12, and E13–E16. Its E13 is an effective functional with a gradient penalty, a local potential U(theta; tau, omega), and an environmental drive Pi(Delta S). E15 is the partial variation at fixed coefficient/other fields. E6 specifies first-order relaxation; E12 separately introduces an inertial wave extension. These are not automatically the same dynamics. [IC-05](../identity-containment-05/README.md) identified the need for a dimensioned field energy and a retained-state law. External sources and access limits are [recorded separately](../../sources/identity-containment-06-primary-sources.md).

The owner's recent bubble/wake analogy is an exploratory mechanism lead: configurations displace or restructure a surrounding medium, changing support and propagation. It is not a measurement of an ARK medium, and ordinary gas is not identified with that medium. This study returns to the actual archived functional rather than adding another device analogy.

## 1. What is recovered, assumed, and derived

| Layer | Content | Status |
| --- | --- | --- |
| Archived structure | Gradient energy + local U + source; relaxation and wave alternatives | Recovered from XXV E6/E12/E13–16 |
| Physical normalization | Interpret F as joules and define a dimensional gradient coefficient K | New declared completion, not an established ARK scalar map |
| Potential | Symmetric quartic double well for a particular construction | Additional candidate, not selected by evidence |
| Dynamics | Constant positive inertia chi, optional nonnegative damping | Additional kinetic law, not derivable from static F alone |
| Retained state | Optional internal variable z with dissipative evolution | Explicit new extension; not identified as tau^c |
| Results | Boundary profile, energy per area, spectrum, energy budgets, counterexamples | Conditional consequences checked below |

Let q = theta - theta_star for a constant reference theta_star, without claiming that this field is a measured clock angle. The offset permits two field values without automatically placing theta outside a chosen clock-angle branch. For example theta_star=pi/4 and v=0.4 keep the constructed wall between 0 and pi/2. This is a compatibility convention, not a derivation of a gravitational clock mapping.

Use

$$F[q]=\int_V\left[\frac K2|\nabla q|^2+U(q)-Jq\right]dV.$$

For dimensionless q and F in joules: K has units J/m; U and J have units J/m^3; chi below has units J s^2/m^3; gamma has units J s/m^3. The energy-like archive does not by itself establish this SI normalization. If archived kappa is normalized, its conversion to K must be independently specified. K here is not automatically a bulk modulus, an integrated material stiffness, or XXII's kappa. Equal units do not identify J with thermodynamic pressure or measured entropy.

## 2. The boundary response follows from variation

With K prescribed independently of q, and other state fields frozen,

$$\delta F=\int_V\big[-\nabla\cdot(K\nabla q)+U_q-J\big]\delta q\,dV
+\int_{\partial V}K\partial_nq\,\delta q\,dA.$$

This recovers the E15 structure and identifies the surface response conjugate to changing q: b_q=K partial_n q. Its units are J/m^2 per unit dimensionless q. It is **not** pressure (J/m^3), net force, or automatically tau^c. To obtain ordinary mechanical stress requires specifying how spatial displacement changes q, domain volume, other fields and boundary conditions; IC-03/05's mode work remains relevant.

If K=K(q), the variational equation additionally contains (1/2)K_q |grad q|^2. E15 must not be copied unchanged into that case. If tau, omega or another field depends on q under the variation, its chain terms must also be included or varied independently. A frozen partial derivative is not a complete coupled equation.

## 3. Static energy does not choose a time evolution

For constant chi>0 and gamma>=0, one possible kinetic completion is

$$\chi q_{tt}+\gamma q_t=\nabla\cdot(K\nabla q)-U_q+J.$$

This follows from kinetic density chi q_t^2/2 plus the declared potential and a dissipative term. It is not supplied by the static functional alone. With J=0, fixed material parameters and no boundary power, the total field energy decreases by integral gamma q_t^2. Inertial and overdamped dynamics can share equilibrium fields but have different trajectories.

At a homogeneous minimum q0, let B=U_qq(q0)>0. With zero damping, a small plane wave obeys

$$\Omega^2(k)=\frac{Kk^2+B}{\chi},\qquad u=\sqrt{K/\chi},\qquad\Omega_0=\sqrt{B/\chi}.$$

u is the characteristic/front speed of this linear hyperbolic model; it is not the phase or group speed of every mode and is not identified with light speed. Omega_0 is the zero-wavenumber small-oscillation angular rate, not an atomic clock frequency or the archive's omega. With damping, a mode exponent satisfies chi s^2+gamma s+(Kk^2+B)=0. The small-inertia slow branch tends to s=-(Kk^2+B)/gamma; with U flat this yields diffusion coefficient K/gamma. The continuum diffusion approximation has nonzero tails and is not itself proof of a finite propagation front. The local discrete source network, continuum approximation, and inertial model require their own regime assumptions.

Multiplying chi by four leaves every static field and its energy unchanged while halving u and Omega_0. This is an explicit non-identifiability example: a static boundary profile cannot fix an absolute dynamical rate without kinetic information. That information may be independently measured or derived from additional mechanics; it need not be an illegitimate fitting knob.

## 4. A constructive boundary, not just a missing-information argument

Choose a>0, v>0, constant K, zero drive, and

$$U(q)=\frac a4(q^2-v^2)^2.$$

For a planar interface with q(-infinity)=-v and q(+infinity)=v,

$$q(x)=v\tanh(x/\ell),\qquad\ell=\sqrt{\frac{2K}{av^2}}.$$

ell is the tanh-profile width parameter, not a universal choice of measured interface thickness. The gradient and local-potential contributions are equal along this solution. Subtracting the equal zero bulk energies, the excess energy per unit area is

$$\sigma=\frac{2\sqrt{2Ka}}3v^3.$$

This is an interface-tension candidate from virtual change of area. It is not a derivation of electromagnetism or a physical ARK pressure tensor. The planar second-variation operator is proportional to A-dagger A, with A=d/dy+2 tanh y. It is nonnegative for admissible perturbations, with a translation zero mode. This establishes linear planar stability in the stated boundary sector, not stability of an unconstrained compact object.

The same chosen potential supplies B=2av^2, hence the consistency relation

$$\boxed{\Omega_0\ell=2u}.$$

It is specific to this potential, homogeneous frozen parameters and lossless small-amplitude dynamics. It connects independently distinguishable static and dynamic observables without requiring a new fitted value for each. Calibration of two inputs and comparison to a third can test the relation only if they were not all calculated from the same input measurements. This is a familiar quartic-field construction applied as an explicit candidate inside the source's functional family, not a novel law or established ARK prediction.

Illustrative coefficients K=2, a=3, v=0.4, chi=5 give ell=2.88675134595, sigma=0.147801668913, u=0.632455532034 and Omega_0=0.438178046004 in the declared test units. These are constructed inputs, not measured substrate properties.

## 5. Environmental drive changes the allowed states

For constant J, stationary homogeneous fields solve a q(q^2-v^2)=J. The symmetric quartic has two local minima separated by a maximum only for

$$|J|<\frac{2av^3}{3\sqrt3}.$$

Except at J=0, the two minima generally have unequal energies; one may be metastable. At the threshold a minimum and maximum merge. The numeric branch check verifies two minima below and one above this threshold. A stationary unforced flat wall approaching two asymptotic constants also requires equal effective bulk energies. A tilt generally drives interface motion unless another constraint or spatially varying environment supplies balance.

This is a conditional realization of environmental selection, not an independent mapping from atmosphere, vacuum, gravitating matter or epsilon to J. Specifying that map is still required.

## 6. Two source claims need narrower conditions

**Nonlinearity alone does not imply multiple phases.** U(q)=q^2/2+q^4/4 is nonlinear and strictly convex: U_qq=1+3q^2>0, with one minimum. Thus Appendix E.3/E.4's broad implication from nonlinear stabilization to multiple minima is too strong without further constitutive conditions. The positive quartic double-well example shows a constructive sufficient case; the archive is not edited.

**A stable planar interface does not establish a stable closed identity.** In the thin-wall, fixed surface tension, fixed reservoir-pressure model,

$$E(R)=4\pi\sigma R^2-\frac{4\pi}{3}\Delta p R^3.$$

The stationary radius R_c=2sigma/Delta p for positive Delta p has E''(R_c)=-8pi sigma<0. It is an unstable critical bubble, not a stable atom. At zero pressure difference surface energy decreases on shrinking. Fixed particle content, compressibility, conserved charge, topology, rotation, constraints or another constitutive term can change this result, but whichever mechanism is proposed must be specified and tested rather than inferred from the word "bubble." This counterexample applies only to the model stated, not all possible medium identities.

## 7. Retained history is an additional resolved state, not a name for a coefficient

An explicit extension is

$$U(q,z)=\frac a4(q^2-v^2)^2+\frac h2(z-bq)^2,\qquad
z_t=-M U_z,$$

with h>0, M>0, dimensionless z,b. This is new conditional model development, not a recovered law for tau^c or an omega-stabilizer. The material relaxation time is t_r=1/(Mh), not tau^c.

At equilibrium z=bq, so the same static wall survives. Near either uniform well the frozen curvature is B_fr=2av^2+hb^2, whereas the equilibrated curvature is the Schur complement B_rel=U_qq-U_qz^2/U_zz=2av^2. For exp(-i Omega t), the additional complex curvature is

$$\Delta B(\Omega)=hb^2\left[1-\frac1{1-i\Omega t_r}\right].$$

Thus the static profile can remain unchanged while finite-frequency response depends on retained-state kinetics. The lossless width-rate identity cannot be applied blindly to a frozen-history resonance. A fast-memory, weak-loss limit must actually hold to recover its relaxed-mode interpretation.

With constant K and chi, the full energy excluding external source potential obeys

$$\frac{dE_0}{dt}=\int_{\partial V}K q_t\partial_nq\,dA+
\int_V\left[Jq_t-\gamma q_t^2-MU_z^2\right]dV.$$

This accounts explicitly for boundary power, external drive, and nonnegative dissipation. If material parameters themselves vary, their work terms must be included. If -Jq is included in the energy, replace Jq_t with -q J_t. No unknown term is set to zero merely to obtain agreement.

## 8. What this does and does not say about clocks or superfluidity

A rate emerging from one field model is not a universal gravitational clock law. Different excitations can have different stiffness, inertia, local curvature and retained-state couplings. A common multiplier for all clock species requires an additional shared coupling structure. The two-mode test distinguishes common inertia rescaling from species-dependent curvature changes; the latter does not preserve a common rate factor.

The source functional does not by itself specify conserved medium density, a phase/current law, vortices, an equation of state, or the dynamical spacetime coupling. This study therefore has not constructed a physical superfluid, shown that ordinary air changes the proposed medium, recovered signed electric charge, derived gravity, or predicted a new clock shift. Analogue-acoustic geometry is an external mathematical precedent with restricted conditions, not proof of the ARK ontology.

## Verification and development record

Run `python check_ic06.py --output test-results.json` with NumPy, SciPy and SymPy. The exact final runtime, versions, script SHA-256 and all 20 named outcomes are in [test-results.json](test-results.json). All 20 pass. Symbolic calculations are cross-checked by energy quadrature, direct energy differences, second-order spatial refinement and separate ODE integration. The method is not an independent second review, blind evaluation or an empirical fit. Historical IC scripts were not rerun; no full-corpus/PDF fidelity audit or local full-archive check was performed. GitHub archive CI is a separate check, reported in the PR after publication.

Initial development run: 19/20 passed. The centered-difference refinement test used a symmetric base profile and antisymmetric variation whose cubic truncation coefficient canceled, leaving roundoff rather than the expected convergence. The fixture was changed to a non-canceling variation, not the field equation or physical assumptions. Final errors fall by four on each halving of the variation: 1.46859e-4, 3.67148e-5, 9.17870e-6. The failed first run is retained in the downloadable packet; its script hash is recorded in that run's JSON. No failed empirical result was discarded.

## Next research gate

The productive next step is to constrain the **same** K, U, kinetic coefficient and retained-state evolution from a concrete archive/microphysical specification, instead of fitting separate laws for pressure, propagation and clock rate. Determine what conserves or anchors a closed identity and what calibrates its inertial response. The conditional width/rate relation is one possible test surface, not a reason to adopt the quartic potential universally. Recover or propose these missing laws explicitly, then compare against independently characterized responses. Keep measured-input reconstruction, numerical verification and physical mechanism evidence distinct.
