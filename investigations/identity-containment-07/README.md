# IC-07 — Conservation, exchange, and the stability of a closed configuration

Date: 2026-11-01. Parent: `7ababc8522edb4eeed3d00af558ea60668e08c07`. Status: conditional mathematical reconstruction and numerical verification; no experimental fit or independent second reviewer. Existing papers, policies, manifest and prior studies are unchanged. This is a candidate within the energy-functional family, not a new established ARK law or a physical superfluid construction.

## Question and result

[IC-06](../identity-containment-06/README.md) supplied a planar interface but showed that a closed spherical wall at a fixed reservoir pressure is not necessarily stable. Here the same quartic field energy supports a spherical profile that is a local minimum against **radial perturbations conserving the total field integral in a finite cell**. Allowing exchange with an ideal external reservoir opens a growing radial mode. Finite restoring response from that reservoir can stabilize the coupled radial problem without prohibiting exchange.

The interior phase is not sealed: it may exchange with its surrounding phase within the cell. The conserved quantity belongs to the **whole specified cell**, not automatically to the droplet alone. Nothing here identifies it as electric charge, atom number, mass, or the physical ARK identity.

The finite cell, chosen mean, double-well potential and mobility are declared assumptions. Coefficients and initial guesses were selected to explore a droplet branch with the target structure visible; this is not blind prediction or an empirical parameter estimate. No claim is made about all mean values, infinite space, all perturbations, or global stability.

## 1. Conservation is a physical condition, not a synonym for persistence

[Paper XXV](../../raw/papers/paper-025-disciplined-containment-conv-01.md), Appendix E1/E6, contains a local exchange equation. On a closed, equal-weight network with reciprocal couplings, a common relaxation coefficient and zero drive,

$$\dot q_i=\eta^{-1}\sum_j k_{ij}(q_j-q_i),\qquad k_{ij}=k_{ji},$$

summing over sites gives zero. With unequal cell volumes the appropriate weighted balance must be used. Asymmetric couplings, external source terms or boundary flow can destroy this invariant. The archive's condition that couplings are nonnegative does not by itself establish reciprocity.

The divergence part of E6 similarly conserves an integral under no-flux boundaries and no net source. Adding a local reaction term from a nonlinear potential does not automatically preserve it. Thus E6 and E13 cannot be combined into arbitrary dynamics without checking which quantities survive.

Keep IC-06's candidate energy,

$$F[q]=\int_{\mathcal V}\left[\frac K2|\nabla q|^2+\frac a4(q^2-v^2)^2\right]dV,$$

and propose the extra constraint

$$\mathcal C=\int_{\mathcal V}q\,dV.$$

For dimensionless q this integral has units of volume; it is not particle number by nomenclature. A measurement mapping and physical justification remain necessary. q is not declared to be the measured clock angle.

With fixed C the stationary equation is

$$\mu\equiv-K\nabla^2q+a q(q^2-v^2)=\lambda,$$

where the constant lambda is determined along with the profile by C and the boundary conditions. It is not assumed to be zero, an adjustable entropy correction, or ordinary pressure.

A conventional conserved kinetic completion is

$$\partial_tq=\nabla\cdot(M\nabla\mu),\qquad M>0.$$

This is a Cahn-Hilliard-type dissipative model, **not** a derivation of superfluid dynamics. It is an additional choice, not a consequence of static energy alone. For zero flux, C is conserved while

$$\dot F=-\int M|\nabla\mu|^2dV\le0.$$

For dimensional F in joules, mu has units J/m^3 and M has units m^5/(J s). The published computations use explicitly dimensionless K=a=v=M=1. Dissipative eigenvalues below are not oscillation frequencies, proper-time factors or ARK omega.

## 2. A computed closed profile in a finite environment

Domain: three-dimensional sphere of radius L=20, regular at its center, zero normal derivative of q at its outer surface. Fixed volume-weighted mean q=-0.75. A spherical positive interior phase joins a negative surrounding phase. Solve the radial stationary equation and the integral constraint simultaneously for q(r) and lambda.

The finite-volume energy uses exact spherical shell volumes and interface areas; its gradient defines the discrete chemical response. No fitted radius is supplied to the equilibrium equations. A tanh-shaped seed selects the investigated branch, not uniqueness of the nonlinear solve.

| Radial cells | Zero-crossing radius | F | Lowest unrestricted radial curvature | Lowest fixed-C radial curvature |
|---|---:|---:|---:|---:|
| 100 | 9.09394793 | 1080.35932 | -0.02433044 | +0.20879917 |
| 200 | 9.09351546 | 1080.85094 | -0.02438293 | +0.20906353 |
| 400 | 9.09331546 | 1080.97355 | -0.02439601 | +0.20912921 |
| 800 | 9.09326546 | 1081.00418 | -0.02439928 | +0.20914561 |

All values are in the declared test normalization, not physical lengths, energies or rates. The curvature eigenvalues are mass-weighted second variations, not direct temporal growth rates. The constant reference field q=-0.75 has F=1603.52125. The chosen droplet has lower energy than this one comparator; this is **not** a proof that it is the global minimizer.

An independent continuous boundary-value collocation solve gives lambda=0.1025941287569 and F=1081.0143896981. Finite-volume energy differences improve approximately fourfold on each grid doubling. These are alternative numerical implementations within this session, not a second investigator.

The unconstrained negative direction changes C. After projecting it out using the actual volume weights, the lowest radial curvature is positive. The conserved radial dynamics also have negative growth exponents. A small zero-integral perturbation relaxes in a separate nonlinear BDF integration while conserving C to approximately 4e-12 in the test units.

**Scope of stability:** local radial stability in a finite environment. Angular sector l=2 is positive in the tested discretizations, but the translation-like l=1 eigenvalue falls from 6.50e-5 to 1.01e-6 as the grid is refined. Do not call this numerical near-zero value physical pinning. Continuum translation/boundary effects, migration toward the cell wall, general nonradial instabilities, multiple droplets, nucleation and global minima have not been resolved. No atom or universally stable particle has been constructed.

## 3. Pressure balance does not alone determine restoring response

A separate thin-interface check makes the radial mechanism transparent. With constant surface tension sigma, interior amount N, density n=N/V and an appropriate bulk energy/free-energy density f(n), write

$$E(R,N)=4\pi\sigma R^2+V f(N/V)+p_{\rm out}V,\qquad V=4\pi R^3/3.$$

Choose the thermodynamic constraint consistently (for example isothermal free energy). Then p=n f'(n)-f(n) and bulk modulus B=n^2 f''(n). At fixed N, stationary radius satisfies

$$p_{\rm in}-p_{\rm out}=2\sigma/R.$$

The radial second derivative at that balance is

$$E_{RR}=4\pi R\left(3B-2\sigma/R\right).$$

Thus a local radial minimum requires 3B>2sigma/R. Surface tension plus a fixed pressure difference has B=0 and gives the IC-06 instability. A sufficiently strong pressure response to compression can reverse it. This coarse check is conventional capillary thermodynamics, not a claim that ordinary-fluid volume equals atomic substrat displacement; it is not substituted for the numerical field model.

## 4. Weak exchange opens a slow instability

Now allow flux only across the **outer cell boundary**. Match an ideal reservoir's reference chemical response to the previously computed lambda so that the same profile is a stationary reference. This comparison of control conditions does not mean that the reservoir value was independently measured.

Let the integrated outward flow be

$$\dot{\mathcal C}=-g(\mu_{\rm boundary}-\mu_{\rm ext}),\qquad g\ge0.$$

The q boundary derivative remains zero. The chemical-response boundary has the corresponding Robin flux; the finite-volume implementation adds one nonnegative boundary conductance. For constant mu_ext the grand energy G=F-mu_ext C obeys

$$\dot G=-\int M|\nabla\mu|^2dV-g(\mu_{\rm boundary}-\mu_{\rm ext})^2\le0.$$

An open system can decrease this grand energy while departing from the old droplet, because that reference is a saddle when C may change. There is no conservation violation: the change in C is exactly the computed boundary flux.

Along the nearby equilibrium branch define C_lambda=dC/dlambda. It can be calculated from the Hessian or from two separately solved neighboring constrained states. Both methods give approximately -170113.423 on the 200-cell grid. This negative branch susceptibility is not an assumed universal material property.

In the weak-exchange limit the slow radial growth exponent is

$$s_+\simeq-\frac{g}{C_\lambda}>0.$$

Computed growth exponents are 5.62086e-5, 5.85156e-6 and 5.87585e-7 for conductances 10, 1 and 0.1. The limiting ratio s_+/g is 5.87843e-6. Smaller exchange can therefore make departure arbitrarily slow in this idealized linear limit without making the equilibrium stable.

A nonlinear integration initialized along the growing mode gives amplification 1.349891 after a time for which the linear prediction is exp(0.3)=1.349859. This checks a local response from the specified equations; it is not an experimental lifetime prediction. A time to visible departure also depends on perturbation amplitude and detection threshold; stochastic escape, noise and particle decay are not modeled.

## 5. The complement can stabilize exchange without perfect isolation

A finite external environment need not maintain a constant chemical response. Expand its energy around the reference total partition. After eliminating its amount using total conservation, its quadratic contribution gives

$$G_{\rm tot}=F-\lambda_*\mathcal C+\frac{\beta}{2}(\mathcal C-\mathcal C_*)^2,\qquad\beta>0.$$

Equivalently mu_ext=lambda_*-beta(C-C_*). beta is the environment's inverse susceptibility in this local expansion, to be derived or independently characterized; it is not fitted here to an empirical target and is not identified with epsilon, kappa or a cosmological pressure.

For the single-negative-mode radial branch the restoring threshold is

$$\beta_{\rm crit}=-1/C_\lambda.$$

The augmented Hessian adds beta times the outer product of the integral's gradient. In the 200-cell calculation beta_crit=5.878430889e-6. At 0.9 times this value the lowest radial curvature is -0.00223334; at 1.1 times it the curvature is +0.00219180. At the threshold it is zero to numerical precision. This result is local to the branch and reservoir Taylor approximation, not all possible environments.

The new stabilizing response is not created by notation: it must physically reside in the environment or another independently specified constraint. It illustrates the owner's complement intuition without assuming the entire physical hypothesis is already proved.

## 6. External benchmark, not validation

Conserved versus nonconserved phase-field kinetics are standard; INL's MOOSE documentation explicitly distinguishes them. Petrov's 2015 theory gives a separate microscopic stabilization route for a Bose mixture through competing mean-field attraction and quantum-fluctuation repulsion. Schmitt et al. report self-bound magnetic quantum droplets in a trap-free levitation field and a critical atom number below which they evaporate. These are established research examples of constraints and constitutive physics mattering to finite configurations; they do not identify our q, C or mobilities with atoms or a gravitational medium.

No experimental values from those papers entered the calculation. Our symmetric quartic finite-cell model is **not** a reproduction of the quantum-droplet experiments, does not derive their critical atom number, and is not a self-bound vacuum solution.

## Verification, provenance and handoff

Run `OPENBLAS_NUM_THREADS=1 python check_ic07.py --output test-results.json`. Ten substantive check groups pass: reciprocal conservation, stationary/grid/stability analysis, energy variations, independent continuous BVP, flux/energy budgets, closed dynamics, weak-exchange susceptibility, finite-environment response, nonlinear evolution, and the capillary criterion. The exact code hash, versions and numeric values are in [test-results.json](test-results.json). Tests were designed with the calculations visible; no claim of independent or blind assessment.

IC-06's unchanged script was matched against Git blob `3608cae59d1a572e666a3fa14cd7c3220599219b` and rerun: 20/20 passed. That separate report is in the downloadable packet. IC-01–05 were not rerun. The current study did not re-audit source PDFs or run a local complete-archive verifier. GitHub preservation CI is reported separately after publication.

Source access: current AGENTS, POLICIES, entry protocol and investigation index; locally retained charter v1.1 methodology/ASRP sections; the prior IC-06 packet and code; the source Markdown of XXV lines 3000–end at the parent commit (blob `3bbf2a40a7c4bdde67f4bbeb2a29147f10a036f5`). No full-corpus reread. Exact claims from earlier source documents remain subject to their original audits.

External sources accessed 2026-11-01:
- INL MOOSE, Basic Phase Field Equations: https://mooseframework.inl.gov/moose/modules/phase_field/Phase_Field_Equations.html . Official HTML read, including conserved/nonconserved distinction. Some rendered equations are absent from parsed text; calculations here were derived and implemented explicitly.
- D. S. Petrov, Quantum Mechanical Stabilization of a Collapsing Bose-Bose Mixture, PRL 115, 155302 (2015), DOI 10.1103/PhysRevLett.115.155302; https://arxiv.org/abs/1506.08419 . Abstract and supplied article-text introduction/equations consulted; no figures, numeric dataset or full reproduction. The supplied text contains an inconsistent parenthetical date; the publication year is taken from the journal record, not that line.
- M. Schmitt et al., Self-bound droplets of a dilute magnetic quantum liquid, Nature 539, 259–262 (2016), DOI 10.1038/nature20126; https://arxiv.org/abs/1607.07355 . Abstract and supplied prose on experiment/levitation and critical atom number consulted. Figures and experimental data were not inspected or used.

ASRP checks: do not assume nonlinear stabilization conserves the source's integral; derive the conservation condition. Do not call a finite-cell radial minimum an isolated stable particle; inspect unrestricted and angular modes. Do not mistake slow growth for stability; compute the open-boundary spectrum and nonlinear response. Do not elevate a generic substrate analogy into an experimental identification. Retain the remaining reference, scaling and measurement questions.

**Next gate:** determine whether ARK actually supplies a conserved amount, phase circulation, topological sector, or other stabilizing constraint with a measurable meaning. Establish its boundary flux and environmental susceptibility from the same constitutive specification. Then test cell-size dependence, nonradial behavior and held-out responses. Preserve the local mathematical result even if this particular conserved-q candidate is rejected. No new omega is introduced as an autonomous stabilizer; rates follow only after kinetics and control conditions are specified.
