# IC-01 — Versioned scalar routes and source map

**Scope:** first-pass inventory of selected passages, not a new read-through or audit of all 25 papers. All historical repository links below are pinned to `2db757753005e6ac66c55797890b2960bffe9307`. Source claims are not automatically established observations. Proper-time interval `Delta tau` is not silently identified with ARK `tau^c`.

## Candidate routes

| Quantity / version | Source route | Independent information required | Unresolved issue / permissible use |
| --- | --- | --- | --- |
| theta, P25 A.1 | `theta = arccos(Delta tau/Delta t)` | Clock ratio, reference convention, motion and potential corrections | Operational conditional assignment; no independent confirmation by inverting the same ratio. Domain and uncertainty matter near ratio 1. |
| theta, P25 A.1 | Static weak-field expression using G, M, r, c | Independently specified mass/geometry and declared regime | Model-based inference, not an independent clock channel when both inputs came from the same gravitational reconstruction. |
| theta, P25 A.1 | `abs(grad Phi^c)/c^2` | Definition/units of Phi^c and spatial scale | If Phi^c has ordinary gravitational-potential units, the expression has inverse-length units rather than an angle. A different potential or reference scale must be specified before equating it to the clock route. |
| kappa, P25 A.2 | Proportional to effective elastic modulus | Stress-strain characterization, geometry, material state, calibrated map | A proportionality is not a complete numerical conversion; anisotropy, response frequency and normalization cannot be omitted. |
| kappa, P25 A.2 | Proportional to resistivity/reference resistivity | Electrical measurements and independently specified reference | Dimensionless proxy with an unspecified proportionality. Equality to mechanical kappa is a testable source claim, not established here. |
| kappa, P25 A.2 | Proportional to inverse phonon mean free path | Transport characterization and a defensible phonon model | Different dimensions require a declared scale. Not automatically applicable to a free neutron. |
| tau, P25 A.3 | Boundary integral of causal stress | Boundary geometry, stress mapping, history and contraction convention | Scalar/vector meaning and causal-stress units need specification. If conventional traction units are intended, the integral is force-like, not a time. |
| tau, P25 A.3 | Persistence, yield/work-hardening or lifetime proxies | Independent response measurements and conversion law | A proxy is not equality. Using the lifetime under test to define tau prevents claiming an independent prediction of that same lifetime. |
| tau/kappa, P18 2.2 | `tau = integral kappa (dtheta/dt) dt` | Reference tau, state trajectory, kappa along it, other held-fixed variables | Conditional tangent stiffness; not universal secant `tau/theta`. Dependence on other state variables/history must be explicit. |
| kappa, P18 2.3 and section 3 loop | `k = 1/theta` in an isotropic/normalized implementation | Justified model regime and normalization | A constitutive/algorithmic assignment, not an additional measurement. Do not count it as a new experimental constraint. |
| theta/kappa, P22 II and V | Both bridges use `q=kappa theta` | Energy/field observations, fixed gauge/geometry/calibration | q can be identifiable while its factors are not. IC-01 checks the symmetry and printed inversion; other independent constraints may resolve the factors. |
| omega, P25 A.4 | `P_int - P_ext`; pressure balance | Maps from theta/kappa to internal pressure and environment to external pressure | Not automatically a frequency. P22's emergent-frequency language is a separate version pending a dimensional bridge. |
| epsilon, P25 B.2-B.4 | Resolved apparatus contribution in `E=S+epsilon` | Geometry, fields, walls, collisions, thermal/radiation conditions AND their coupling laws | Listing channels is not their numerical evaluation. Do not identify the complete residual with a particular channel. |
| S, P25 D.1 | Appears through its time derivative | Identity fields and derivatives, Lambda, coefficients, baseline or independent level constraint | With Lambda fixed, rate is recoverable conditionally; absolute level is not. A3/A4/B2 constraints must be tested jointly rather than silently blended. |

## A constructive search strategy

Start with an observable map `y=h(theta,kappa,tau; known controls)`. Include unknown calibrations, omega and boundary parameters in the unknown vector unless independently fixed. Test the complete constraint set, not only its equation count. Additional data should be selected to distinguish the actual remaining family of states.

An independent theta channel plus a valid product bridge and independently characterized tau is one possible three-anchor design. Two measured scalars plus a validated constitutive relation is another. Both require the same physical identity, compatible resolution, units, reference state and temporal sampling. A result showing only identifiable combinations is useful progress, not failed research.

Experimentally measured clock-rate differences provide an actual observable route worth investigating [E1], not evidence for ARK's cross-domain scalar equivalences. No laboratory dataset was loaded in this pass.

## Source register and inspected scope

- **C1:** [Epistemic Charter v1.1](https://github.com/Pfpercy0214/ark-curies-library/blob/2db757753005e6ac66c55797890b2960bffe9307/raw/epistemics/ARK_Epistemic_Charter_v1.1.md), relevant sections 1-8.5, especially 4.4, 5.2-5.5, 6.0 and 8.2. Governs interpretation, not physics validation.
- **P18:** [Paper XVIII](https://github.com/Pfpercy0214/ark-curies-library/blob/2db757753005e6ac66c55797890b2960bffe9307/raw/papers/paper-018-recursive-scalar-geometry-conv-01.md), sections 2-2.5 and section 3's expanded loop. Reviewed relevant opening range, not all appendices in this session.
- **P22:** [Paper XXII](https://github.com/Pfpercy0214/ark-curies-library/blob/2db757753005e6ac66c55797890b2960bffe9307/raw/papers/paper-022-electromagnetism-conv-01.md), sections II and V.1-V.3. Products and geometric factors were transcribed into the tests from these archived equations.
- **P25:** [Paper XXV](https://github.com/Pfpercy0214/ark-curies-library/blob/2db757753005e6ac66c55797890b2960bffe9307/raw/papers/paper-025-disciplined-containment-conv-01.md), inspected ranges 1000-1240, 1900-2170, 2260-2580, 2880-3210. Main dependencies: Appendix A.1-A.7, B.2-B.4 and D.1. Git blob `3bbf2a40a7c4bdde67f4bbeb2a29147f10a036f5`.
- **E1 / M1:** [Primary-source notes](../../sources/identity-containment-01-primary-sources.md): experimental clock-ratio record and structural-identifiability methodology, with explicit access limits.

The research recollection retrieved this session helped locate distinctions but is not used as independent physical evidence. This work records only the owner's current mechanistic direction; it does not publish unrelated private conversations. No PDF conversion was independently re-audited in this pass.

## Open decisions, not silently supplied defaults

1. Which layer/identity and state resolution will the first application use?
2. Which tau definition and units apply? Are response time, integrated stress and retained state connected by a specified law?
3. Which kappa is intended: tangent response, an operational proxy, or a normalized balance coordinate?
4. Which exact environmental field enters D.1, and how does the resolved epsilon partition enter its coupling?
5. Is Lambda explicitly specified, and does it introduce or remove environmental-level information through omega?
6. Which measurement constrains the baseline, and which distinct observable remains for an external test?

These are work items for reconstruction, not demands that the owner solve every missing equation before analysis can proceed.
