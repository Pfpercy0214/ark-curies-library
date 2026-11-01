# IC-09 — Throughflow without loss of configuration

Date: 2026-11-01. Parent: `1b9428a9f3a8effe116e893acadca50cb7cbb469`. Status: conditional conventional-model derivation and executed numerical checks. No experimental fit, physical ARK scalar identification, independent second reviewer or merge.

## Motivation and boundary of the claim

The owner clarified that a knot-created boundary need not be impermeable. Preserve that distinction as a modeling requirement, not an empirical finding. [The clarification](../../history/mechanistic-notes/2026-11-01-permeable-identity-boundaries.md) is recorded separately from the calculations.

[Paper VIII](../../raw/papers/paper-008-thermodynamic-flow-conv-01.md), section 5, already permits an internally stationary configuration under open boundary forcing. That supports examining open identity descriptions; its diffusive/relaxing equations are not silently replaced by the conservative phase dynamics below. The terminology and entropy interpretation differ. In particular, a nonzero conservative flux is not automatically thermodynamic entropy production or the ARK environmental term.

[IC-08](../identity-containment-08/README.md) introduced a conventional Gross-Pitaevskii (GP) density/phase comparator, while leaving its mapping to ARK unresolved. It used a prescribed ring-density profile and an inverse-manufactured potential for one numerical check. Here, in the **same conventional model family**, a known gray-soliton solution has a self-consistent localized density dip with throughflow and **no localized external potential or material wall**. This is not a new solution of physics, a topological knot, a closed particle, or a derivation of GP from ARK. The field requires a nonzero background and prescribed preparation/asymptotic conditions.

The result establishes a limited but concrete possibility: persistent organization and nonzero transport across its moving boundary are compatible. It does not identify a universal permeability coefficient, an impermeable material surface, an atomic constituent, electric charge, or a gravitational clock rate.

## 1. Model and units

Use the repulsive one-component, one-dimensional, lossless mean-field equation

$$i\hbar\partial_t\psi=-\frac{\hbar^2}{2m}\partial_x^2\psi+g|\psi|^2\psi.$$

Here g>0 is a one-dimensional coupling (energy times length), n=|psi|^2 is number per length, m is the supplied particle mass, and hbar is the supplied action scale. No trap potential, sink, or dissipative coefficient is included in this declared ideal regime. Zero external potential is an explicit comparison-model assumption, not an inference from missing environmental measurements.

Let the independently characterized far-field density be n0, the sound speed c=sqrt(g n0/m), the length unit xi=hbar/(m c), and the time unit xi/c. The code uses n0=m=g=hbar=1, so c=xi=1. Its times are dimensionless, not seconds, proper time, or an identified ARK tau. Its phase is not theta^c.

Define the dimensionless soliton speed relative to the background b, |b|<1, and a=sqrt(1-b^2). With background velocity u, a standard branch is

$$\psi(x,t)=e^{i[u x-(1+u^2/2)t]}\{a\tanh[a(x-(u+b)t)]+ib\}.$$

Direct substitution verifies this equation without solving for a supporting potential. The soliton center speed is V=u+b. The stationary-profile frame uses u=-b. No claim of uniqueness follows from far density and current: the uniform solution also exists. A localized branch, phase imprint, or initial preparation must be declared rather than selected after observing the target.

## 2. The boundary moves differently from the transported density

Writing z=x-Vt,

$$n=1-a^2\operatorname{sech}^2(az),\qquad j=\operatorname{Im}(\psi^*\partial_x\psi)=Vn-b.$$

Therefore

$$j_{\rm relative}=j-Vn=-b.$$

For b nonzero, density passes through the profile in its own frame. The minimum density is b^2, not zero. For b=0 the black-soliton limit has a node and no relative current. The velocity j_relative/n is not well-defined at that exact node; the code treats the limit separately.

For an interval whose ends A(t),B(t) move with the pattern,

$$\frac{d}{dt}\int_{A(t)}^{B(t)}n\,dx=[j-\dot A n]_A-[j-\dot B n]_B.$$

Thus stationary integrated content does not require vanishing inflow/outflow. An asymmetric moving interval was deliberately used to test the motion correction: ignoring it falsely suggests accumulation. A separate fixed-window calculation recovers its predicted nonzero accumulation while the pattern travels through it.

In a symmetric window |z|<=L, the density inventory and hydrodynamic crossing time are

$$N_L=2L-2a\tanh(aL),\qquad T_{\rm cross}=N_L/|b|.$$

The latter is also obtained by integrating a fluid characteristic dz/dt=-b/n(z). It is not tracking distinguishable atoms or measuring a quantum constituent residence-time distribution. It is not the lifetime of the pattern.

Example: b=0.6, a=0.8, L=3/a=3.75. Then N_L=5.9079123941, |j_relative|=0.6, T_cross=9.8465206568. Thirty time units carry 3.04676 window inventories through the profile. The numerical field evolution over that interval retains its density to a maximum absolute error 1.77e-5 relative to the analytical solution. This is unperturbed consistency over several advective crossing times, not a general stability theorem.

## 3. Pressure alone is not the balance law

For this normalized GP equation, momentum balance has the flux

$$\Pi=n v_f^2+\frac{n^2}{2}+\frac{n_x^2}{4n}-\frac{n_{xx}}4,\qquad v_f=j/n.$$

In the stationary-profile frame,

$$\Pi=b^2+\frac12.$$

At b=0.6, the center has an advective contribution 1, interaction-pressure contribution 0.0648, and gradient contribution -0.2048. Their sum is 0.86, the same as the far-field value. Omitting gradient stress leaves an imbalance. The term arises from the spatial-gradient energy in the declared model; it is not a fitted epsilon or an additional force inserted to support the chosen profile.

The stationary wave has the same chemical frequency mu=1+b^2/2 at either end. Its energy current is J_E=mu*j, nonzero and constant. The conservative model needs no chemical-potential drop to sustain its prepared current. A resistive law j=L*Delta(mu) is therefore not an adequate replacement for this phase-dependent dynamics. We did not derive a finite-temperature entropy balance or identify this model's energy flow with Delta S_t.

Adding an explicit imaginary loss term -i Gamma(x) psi/2 changes the continuity law by -Gamma n. That separate control is tested. Crossing a boundary and actual removal of the conserved density are not interchangeable operations.

## 4. Shape, phase and flow can constrain one another

For the selected positive-b branch, with the uniform background phase gradient removed,

$$\Delta\phi=-2\arccos b,\qquad \ell=1/\sqrt{1-b^2},\qquad D=\int(1-n)dx=2\sqrt{1-b^2}.$$

The background-rest-frame excitation energy, with the uniform chemical reference subtracted, is E_s=4(1-b^2)^(3/2)/3. It is not the bare energy of the infinite uniform background, nor the lab-frame energy with arbitrary added flow. Quadrature verifies D and E_s; phase comparison verifies the phase drop.

| b | Minimum density / far density | Width parameter ell | Relative current | Phase drop |
|---|---:|---:|---:|---:|
| 0.2 | 0.04 | 1.020621 | -0.2 | -2.738877 |
| 0.6 | 0.36 | 1.250000 | -0.6 | -1.854590 |
| 0.9 | 0.81 | 2.294157 | -0.9 | -0.902054 |

These are generated dimensionless examples, not a physical data fit. In physical units, ell is multiplied by xi and current by n0*c. An independently measured minimum-density fraction would determine |b| within this model; an oriented current/phase measurement supplies the missing sign. Independent n0,c and mass/action calibration supply the dimensional scale. Width and phase are then available for comparison rather than refitting. No such experimental comparison was performed.

Opposite signs of b give the same density and opposite currents. Density alone therefore does not specify the entire state. Also, as |b| approaches 1, the dip and phase difference vanish continuously. This gray profile has no discrete knot invariant established here. It cannot stand in for a stable three-dimensional particle.

Changing the width by 20 percent while holding the other branch parameters fixed produces a nonzero equation residual about 0.1023. The balance does not support every arbitrarily chosen shape. Nevertheless, the existence of a uniform alternative prevents us from claiming that asymptotic data alone select the soliton.

## 5. What the numerical work tests

[Code](check_ic09.py) and [actual results](test-results.json) record twelve executed check groups. They include symbolic substitution, exact currents, fixed/moving control-volume balances, momentum and energy flux, independent quadrature and fluid-characteristic integration, opposite orientations and limiting cases, an incorrect-width control, an explicit sink, and nonlinear field evolution.

The nonlinear check uses a method of lines with fourth-order centered spatial derivatives and adaptive DOP853 time integration. The outer ghost values are supplied by the declared infinite-line solution. For the stationary test they are constant in the background envelope; the density inside is evolved, not reset. Boundary conditions are therefore **not an independent measurement or a test against arbitrary environmental disturbances**. The simulation is not a scattering experiment or independent second review.

At t=2 with 128,256,512 interior points, maximum complex-field errors are approximately 5.44e-5,3.59e-6,2.29e-7, consistent with fourth-order spatial refinement. Tightening the time tolerance changes the result by about 3.0e-9. A comparable-resolution wider box gives about 3.58e-6. A moving branch is also propagated. At t=30, the stationary 256-point profile's maximum density error is 1.77e-5. Neither small numerical errors nor an exact solution prove unrestricted nonlinear, transverse or three-dimensional stability.

The first formal run passed all twelve groups. The exploratory prototype also supplied the resolution settings; these are developed consistency tests, not preregistered or blind tests. The first report is retained in the downloadable packet and copied without modification as the repository result. The unmodified IC-08 code was byte-matched to Git blob `451f0cb37cce2ce767c2c6bff8969a95e2a0ebaf` and rerun: 12/12 passed. Its fresh report and reproduction code are in the downloadable packet, not substituted into the prior study. IC-01–07 were not rerun.

## 6. External evidence: what was actually read

Read on 2026-11-01; primary publication HTML abstracts/metadata only, not full PDFs, figures, datasets or uncertainty budgets:

- Burger et al., *Dark Solitons in Bose-Einstein Condensates*, PRL 83, 5198 (1999), DOI 10.1103/PhysRevLett.83.5198. Reports phase-imprinted solitons and coherent/dissipative dynamics in elongated rubidium condensates. https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.83.5198
- Denschlag et al., *Generating Solitons by Phase Engineering of a Bose-Einstein Condensate*, Science 287, 97 (2000), DOI 10.1126/science.287.5450.97. NIST's record describes phase preparation and interferometric phase readout. This establishes a relevant experimental class, not verification of our numerical example. https://www.nist.gov/publications/generating-solitons-phase-engineering-bose-einstein-condensate
- Walczak and Anglin, *Exact Bogoliubov-de Gennes solutions for gray-soliton backgrounds*, PRA 84, 013611 (2011), DOI 10.1103/PhysRevA.84.013611. The abstract identifies exact small-excitation solutions and a reflectionless-potential construction. This study independently checks the nonlinear background solution; it does not reproduce those full scattering solutions. https://journals.aps.org/pra/abstract/10.1103/PhysRevA.84.013611
- Walczak and Anglin, *Back-reaction of perturbation wave packets on gray solitons*, PRA 86, 013611 (2012), DOI 10.1103/PhysRevA.86.013611. Reports wave-packet passage with a shift and a soliton response required by momentum accounting. Transmission therefore need not mean absence of interaction. No scattering or back-reaction magnitude is calculated here. https://journals.aps.org/pra/abstract/10.1103/PhysRevA.86.013611

The arXiv HTML version of 1104.0886 was unavailable; a PubMed page for an additional transverse-instability study returned no usable article text and was not used as evidence. No PDF was inspected or full-paper access claimed. No figures or full third-party articles were copied into the repository.

Repository reads this session: current PR head/status; AGENTS, entry protocol and POLICIES; charter v1.1 sections 4–6.4; IC-08 handoff and locally attached package; VIII sections 1–2 and 4–7 excerpt; current investigation index. VIII blob: `3e3f3df88c16b6bc135b73bf042ada0370e453ca`; charter blob: `ae341b2a7e30fc1d25703a1f6dbc032595fec707`. No full-corpus reread, complete local archive validation, or new source-PDF conversion audit is claimed. GitHub preservation CI is checked separately after publication.

## 7. Consequence for the ARK reconstruction

The calculation supplies a structural constraint to carry forward: stationarity must be defined for the configuration, while permeability/flux must specify what crosses and in which frame. A transport timescale must not be renamed identity lifetime. Geometry alone omits orientation, and a pressure-only picture can omit the field-gradient stress that makes a configuration possible.

It does **not** resolve the IC-08 gate: how (or whether) the periodic phase and its conjugate density derive from ARK's scalar definitions. The owner's permeable-boundary clarification motivated this additional comparison before that gate was resolved; the distinction is explicit to avoid silently substituting a conventional condensate for ARK.

Next useful task: return to the versioned ARK field-energy/current relations and write the missing observation-to-state mapping or label its introduction as a new candidate extension. Then perturb a prepared configuration with independently specified controls and predict its changed profile/phase/current, rather than choosing controls from the desired response. A closed three-dimensional identity, its permeability channels, and a universal clock factor require additional derivation.

ASRP checks: no impermeability inferred from geometry; moving boundary flux explicit; no irreversible entropy inferred from current alone; no stationary solution equated with generic stability; no uniform background equation mistaken for proof of state selection; no implicit mapping of phase to theta^c, transit time to tau^c, or GP coefficients to kappa^c. Independent review and physical validation remain pending.
