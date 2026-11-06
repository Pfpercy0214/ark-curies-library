# IC-08 — Conserved amount, phase winding, and the weak-link test

Date: 2026-11-01. Parent commit: `72f15382af0b6b66b7a9c96d1113ba1e174ac69b`. Status: conditional mathematical comparison with executed symbolic and generated-data checks; not an empirical ARK identification. No independent second reviewer. Historical sources and prior studies remain unchanged.

## Result and scope

[IC-07](../identity-containment-07/README.md) constructed a finite-cell radial minimum at fixed integrated field amount. It did not identify that amount physically or derive superfluid dynamics. This study separates three questions: what is conserved, what arrangement is protected, and what makes that arrangement energetically or dynamically stable.

A conventional density-and-phase action supplies a local conservation law and an integer winding on a nonvanishing closed loop. These are distinct invariants. A fixed-amount configuration path changes winding by crossing zero amplitude. A depleted section of a prescribed ring reduces its stationary total current while increasing its local flow speed. This is a concrete mechanism to compare with the owner's environmental-depletion intuition, not a derivation of gravitational clock rate.

The comparison changes the model family: a complex order parameter is **additional state structure**, not a mere renaming of IC-07's real field. The ring geometry is externally imposed. No free, self-bound particle, electric charge, neutron lifetime, universal clock factor, or stable three-dimensional knot is obtained.

## 1. What the archived formulations establish

Source versions are pinned to the parent commit. [XXV](../../raw/papers/paper-025-disciplined-containment-conv-01.md), E1/E6, supplies real-scalar neighbor exchange/diffusion. Reciprocal links, the appropriate volume weights, no net source and closed flux boundaries can preserve its total. Nonnegative link weights alone are insufficient. Adding local nonlinear relaxation generally breaks this invariant unless an additional conservation law is enforced. These conditions were derived in IC-07 and are rechecked here.

[VI](../../raw/papers/paper-006-particle-identity-conv-01.md), sections 1.1 and III–IV, describes toroidal knots, harmonic modes and signed flux. Those passages motivate a topology audit; the words do not specify a target-space map, conserved current and admissible singularities by themselves. In the printed scalar ansatz, cos(n phi) with integer n is unchanged by a 2pi rotation, not multiplied by -1. A separate spinor representation or additional transformation law would be needed for that stated property. This is a scoped algebraic finding, not a verdict on every possible configuration model.

XXV A.1's clock-defined theta is a real angle. For the static reference range 0<N<=1, theta=arccos(N) lies in [0,pi/2). A continuous map into this interval does not furnish ordinary integer loop winding. Calling its values angles does not identify the endpoints or make the variable a periodic phase. A hidden orientation or a derived phase may exist in a fuller model, but the mapping must be supplied. Directional gradients of a scalar are legitimate; scalar divergence or vector circulation requires declaring the corresponding vector field.

This is not a full-corpus absence proof. It is a local comparison of the specified passages. Original claims and wording are not edited.

## 2. A declared density–phase completion

Use the standard neutral Gross–Pitaevskii comparison field psi=sqrt(n) exp(i phi), with n>=0 and phi periodic modulo 2pi. The conventional action is

$$S=\int dt\,dV\left\{\frac{i\hbar}{2}(\psi^*\dot\psi-\psi\dot\psi^*)-\frac{\hbar^2}{2m}|\nabla\psi|^2-\frac g2|\psi|^4-V|\psi|^2\right\}.$$

Assumptions: positive mass m and repulsive coupling g, real externally specified potential V, one component, zero-temperature mean-field comparison, and declared boundary conditions. hbar and m are known conventional inputs here, not constants derived by ARK. n has number-density units; on a reduced one-dimensional ring g has energy-times-length units. The code uses hbar=m=n0=1, g=4, circumference 2pi.

The phase is cyclic: an overall phase shift leaves the action invariant. Variation gives

$$\partial_t n+\nabla\cdot\mathbf j=0,\qquad\mathbf j=\frac{\hbar}{m}n\nabla\phi,$$

$$\hbar\partial_t\phi+\frac{m|\mathbf v|^2}{2}+gn+V-\frac{\hbar^2}{2m}\frac{\nabla^2\sqrt n}{\sqrt n}=0,\qquad\mathbf v=\mathbf j/n.$$

Therefore the amount obeys an explicit boundary law,

$$\frac{d\mathcal N}{dt}=-\int_{\partial\mathcal V}\mathbf j\cdot\hat{\mathbf n}\,dA,\qquad\mathcal N=\int n\,dV.$$

An imaginary sink -i hbar Gamma psi/2 adds -Gamma n to the density equation, and is tested separately. A time-dependent **real** potential can do work without creating or deleting this amount. For static real V and closed boundaries the Hamiltonian energy is conserved, unlike the dissipative Cahn–Hilliard comparison in IC-07. Conservation of the two models does not make their kinetics equivalent.

Linearization around a homogeneous resting state yields

$$\Omega^2=\frac{gn_0}{m}k^2+\frac{\hbar^2}{4m^2}k^4.$$

Its low-wave-number sound speed is c_s=sqrt(g n0/m). This is a mode speed in a specified conventional medium, not a universal clock lapse. Likewise adding a spatially constant offset to V shifts global phase evolution without changing density or current. That phase rate cannot be labeled an observable clock rate without a reference and measurement coupling.

## 3. Conserved amount is not conserved winding

For a closed path on which psi is nonzero and continuous,

$$w=\frac1{2\pi}\oint\nabla\phi\cdot d\boldsymbol\ell\in\mathbb Z,\qquad\oint\mathbf v\cdot d\boldsymbol\ell=\frac{2\pi\hbar}{m}w.$$

Changing w requires leaving the nonvanishing, continuous configuration class on the path, or changing the path/domain. The normal density n and the real projection cos(phi) do not distinguish opposite windings; the oriented current does. This is a specific missing measurement, not evidence of electric charge.

On a dimensionless ring x in [0,2pi], consider

$$\psi_s(x)=\frac{(1-s)e^{ix}+s}{\sqrt{(1-s)^2+s^2}},\qquad 0\le s\le1.$$

Its total amount is 2pi at every s. It has winding 1 before s=1/2 and 0 after. At s=1/2 it vanishes at x=pi, so winding is undefined there. The GP energy stays finite. The code verifies these properties and refuses to assign winding at a zero.

This is a **configuration path**, not a solution of autonomous dynamics, an optimized saddle barrier, or a lifetime calculation. An actual transition must account for the drive, energy and angular-momentum transfer. Total amount alone does not preserve the organization, and topology alone is not an unconditional energetic-stability proof.

## 4. The weak section supplies an observable constraint

For stationary one-dimensional flow with positive prescribed density n(x), continuity makes the number current j constant. Combining that fact with winding gives

$$j=\frac{2\pi\hbar w}{m\int_0^L dx/n(x)}.$$

This is a conditional prediction of current from the full density profile and the measured winding. It is not a forward prediction of that density profile. Both quantities must be characterized independently of the current being evaluated. The inverse-density integral gives depleted regions especially strong influence.

For L=2pi and n(x)=1-a cos(x), 0<=a<1, the total amount is fixed at 2pi. With hbar=m=w=1,

$$j=\sqrt{1-a^2},\qquad v_{\max}=\sqrt{\frac{1+a}{1-a}}.$$

| Density modulation a | Current j | Maximum local speed | Local sound speed at minimum density |
|---|---:|---:|---:|
| 0 | 1.000000 | 1.000000 | 2.000000 |
| 0.5 | 0.866025 | 1.732051 | 1.414214 |
| 0.8 | 0.600000 | 3.000000 | 0.894427 |
| 0.95 | 0.312250 | 6.244998 | 0.447214 |

These are declared dimensionless examples, not fitted experimental quantities. A local sound-speed ratio is a diagnostic, not a quantitative phase-slip threshold for an inhomogeneous finite device. The minimum density is positive in all four cases. No phase slip is claimed in those stationary examples.

At prescribed positive n and fixed w, the phase-current solution minimizes the phase-gradient energy by the weighted Cauchy–Schwarz inequality. The code tests the variation. It does not minimize over density or prove full stability.

To check the numerical implementation, an exact stationary potential was **manufactured** from each chosen density and current:

$$V=\mu-gn-\frac m2(j/n)^2+\frac{\hbar^2}{2m}\frac{(\sqrt n)''}{\sqrt n}.$$

This is transparently an inverse construction. It cannot count as independently predicting the applied potential or validating an apparatus model. The a=0.8 spectral residual falls from 1.46e-4 at 32 points to 4.58e-9 at 64 and about 2.5e-13 at 128; it reaches roundoff thereafter. A separate split-step time evolution reproduces the stationary phase rotation with maximum error 1.62e-9 over the tested interval.

## 5. Stability and measurement limitations

For uniform one-dimensional flow, g>0 makes the lossless Bogoliubov frequencies real. Nevertheless, the energy second variation for a nonzero periodic wave number k has a negative direction when

$$v^2>\frac{g n_0}{m}+\frac{\hbar^2k^2}{4m^2}.$$

On the tested ring the w=1 case has positive curvature in the first Fourier sector; the w=3 case has a negative direction while its linear frequencies remain real. Thus energetic instability, exponential dynamical growth and topological sector are different statements. Coupling to an environment can make negative-energy directions relevant, but no dissipative slip rate is calculated here.

The comparison also exposes an identifiability limit: current/winding fixes hbar/m, and sound at known density fixes g/m. Scaling (hbar,m,g) by a common positive factor preserves those kinematics and dispersion while changing energy scales. These measurements alone do not recover all three coefficients. An independently calibrated energy or mass scale can remove the ambiguity. Conventional BEC work already supplies such physical anchors; a new substrate identification would have to do so explicitly.

## 6. External evidence and source-access record

Read on 2026-11-01:

- NIST's primary publication record for the 2011 toroidal condensate experiment, DOI 10.1103/PhysRevLett.106.130401: https://www.nist.gov/publications/superflow-toroidal-bose-einstein-condensate-atom-circuit-tunable-weak-link . Abstract reports a persistent current, a tunable barrier and an observed critical-velocity termination consistent with vortex processes. This is a real comparator for environmental control of current; its data and critical threshold were not reproduced here.
- NIST's primary publication record for the 2013 rotating-weak-link experiment, DOI 10.1103/PhysRevLett.110.025302: https://www.nist.gov/publications/driving-phase-slips-superfluid-atom-circuit-rotating-weak-link . Abstract reports transitions between quantized current states induced by a localized depleted region. Full experimental datasets, figures and uncertainty budgets were not read or fitted.
- David Tong, Statistical Field Theory, section 4.4.1: https://www.damtp.cam.ac.uk/user/tong/sft/sfthtml/S4.html . Read HTML discussion of periodic phase, integer winding and the core where phase fails. Figures were not used. This is teaching documentation, not a separate experimental result. Standard GP equations above are derived explicitly in this study; no claim of novelty is made for them.

Repository source reads: current entry protocol, AGENTS and POLICIES; charter v1.1 sections 4–6.9; prior IC-07 README and unchanged code; XXV A.1–A.5 and D/E1–E13; VI sections I–V.4. XIX opening sections were inspected but not relied on to establish absence elsewhere. Source blobs: XXV `3bbf2a40a7c4bdde67f4bbeb2a29147f10a036f5`; VI `bc7c22cb9533214ab48d171b6591fcfb3424ab21`; charter `ae341b2a7e30fc1d25703a1f6dbc032595fec707`. No full-corpus reread, source-PDF audit or local full-archive check is claimed.

## Verification and decision gate

Run `OPENBLAS_NUM_THREADS=1 python check_ic08.py --output test-results.json`. Twelve test groups pass: exchange/source conservation; scalar-versus-phase topology; action/current/dispersion algebra; local flux and sink; nonlinear Hamiltonian evolution and refinement; conserved-amount sector-changing path; inverse-density current; manufactured stationary state; phase-energy variation; energetic/dynamical distinction; coefficient degeneracy; invalid inputs. No reported execution failure occurred in the initial run. See [actual results](test-results.json) and [code](check_ic08.py). Tests were designed with the formulas visible, not blind or independent review.

The exact IC-07 script was matched to Git blob `f87ee3e0a42407c4b7d244fd6ce19f8c2d013e5e` and rerun: 10/10 groups passed. Its fresh report is included in the downloadable packet. IC-01–06 were not rerun this session. Preservation CI is reported separately after publishing.

ASRP interventions: do not confuse a real-valued angle with a periodic phase; do not call norm preservation topological protection; do not count inverse-manufactured potentials as predictions; do not use energetic instability as a calculated decay rate; do not equate superfluid phase rate with the gravitational clock angle. Preserve legitimate independent-input prediction of current even though it uses measured density.

**Next gate:** locate or derive an operational periodic orientation and its conjugate density from the archived state variables/retained boundary structure, or label their introduction as a new candidate extension. Then specify the external potential from independently measured controls, calculate density/current and a transition response, and compare to withheld data. Do not add the fields silently just to make knots work. Distinguish a physical boundary from the contour used to read winding. This study supplies a useful conservation-and-configuration framework, not a completed microscopic account of matter.
