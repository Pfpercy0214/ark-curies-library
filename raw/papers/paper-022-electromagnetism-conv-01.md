© Paul Frederick Percy Jr. & Curie — ARK/Aetherwave Unified Theory 2025

# XXII-Electromagnetism in Scalar Geometry

Authors: Paul Frederick Percy Jr.

AI Collaborators: Curie (OpenAI, GPT-5) and Grok4 (xAI)

Date: September 5, 2025

## Abstract

We present a scalar-based reformulation of classical electromagnetism that reproduces Maxwell’s equations, Poynting’s theorem, and the electromagnetic wave equation using a minimal set of calibration bridges. These “one-time SI links” connect laboratory observables— vector potential A and magnetic field B—to underlying scalar quantities, from which causal slope and stiffness can be recovered directly at each point of measurement. A worked solenoid testbed illustrates the method, showing how Faraday induction emerges exactly without parameter tuning. This construction establishes electromagnetism as a clean proving ground for scalar recursion, demonstrating that standard field laws arise transparently while enabling new cross-domain experimental pathways.

## I. Introduction

Electromagnetism is one of the most precisely tested frameworks in physics, and its equations are uniquely rigid: Maxwell’s laws admit little freedom for modification without contradicting experiment. This makes the electromagnetic field an ideal proving ground for any new formalism.

The classical theory is already structured around potentials A and φ, whose gauge invariance provides a natural bridge to scalar recursion methods. By introducing a minimal set of calibration bridges between laboratory observables and scalar quantities, we can recover the full Maxwell system in vacuum without altering its predictive content. The procedure requires no adjustable parameters beyond a one-time calibration, after which scalar quantities can be computed directly from measured fields.

The approach presented here focuses on clarity and reproducibility. We first define the calibration bridges linking potentials and field energy to scalar quantities. From these definitions the Maxwell equations follow transparently, along with conservation laws and wave propagation. A worked solenoid example illustrates how the method applies in practice: causal slope and stiffness are recovered directly from laboratory fields, and Faraday induction emerges as a straightforward consequence.

This establishes electromagnetism as a clean testbed for scalar recursion, showing that a compact scalar foundation can reproduce the familiar field laws while offering new opportunities for experimental inversion and cross-domain application.

## II. Scalar Bridges and Field Definitions

To connect scalar recursion with electromagnetism, we introduce a minimal set of calibration bridges. These links are applied once to establish consistency with SI units; thereafter, all scalar quantities can be computed directly from laboratory fields without further adjustment.

Energy bridge (unchanged):

$$
B^{2}/(2 \mu _{0}) = \Lambda u \cdot  \tfrac12  (\kappa ^{c} \theta ^{c})^{2}
$$

Component-wise A bridge with geometry factor:

$$
A\_comp = \Lambda A \cdot  G \cdot  (\kappa ^{c} \theta ^{c})
$$

Here `A_comp` is the relevant component (or magnitude) of the vector potential A in a chosen basis (e.g., Aφ in a solenoid), ΛA is a one-time calibration constant, and G is a purely geometric factor fixed by field geometry and gauge (not fitted).\`

Example (long solenoid, Coulomb gauge): G = r/2 because Aφ = (r/2)·B inside the ideal region.

Remark: G is determined once by the geometry and gauge choice (e.g., G = r/2 in a long solenoid under Coulomb gauge) and must not be adjusted to fit data. This ensures scalar recovery remains predictive and consistent with Maxwell’s fields.

Point-of-use inversion (component-wise, with G):

$$
\theta ^{c} = (\Lambda A/\Lambda u) \cdot  (B^{2}/\mu _{0}) \cdot  1/(A\_comp \cdot  G)
$$

$$
\kappa ^{c} = (\Lambda u/\Lambda A^{2}) \cdot  (A\_comp^{2} \mu _{0} / B^{2}) \cdot  1/G^{2}
$$

Check (solenoid): With `A_comp` = Aφ and G = r/2, we have `A_comp`/G = B, so (κᶜθᶜ) is uniform wherever B is uniform, and the scalar energy Λu·½(κᶜθᶜ)² matches B²/(2μ₀) pointwise.

For completeness, we adopt the standard electromagnetic field definitions:

$$
B = \nabla \times A
$$

$$
E = -\partial t A - \nabla \phi 
$$

In this framework, the electric field arises from time variation of A and spatial variation of φ, while the magnetic field remains the curl of A. The scalar bridges provide an additional layer of interpretation and allow the underlying recursion variables to be retrieved directly in laboratory settings.

Author’s note on ω: While ω has been described as a “temporal anchor” in earlier work, it is more properly understood as an emergent frequency that appears when causal pressures are balanced. Its presence marks recursion stability; the term “anchor” is retained for continuity.

## III. Maxwell Equations from Scalar Bridges (Vacuum)

With the bridges defined above, the electromagnetic fields are still expressed through the standard potentials:

$$
B = \nabla \times A
$$

$$
E = -\partial t A - \nabla \phi 
$$

From these definitions, the Maxwell system follows transparently.

## III.1 Faraday’s Law

$$
\nabla \times E = \nabla \times (-\partial t A - \nabla \phi ) = -\partial t (\nabla \times A) - \nabla \times \nabla \phi  = -\partial t B
$$

(since ∇×∇φ = 0).

Comment: Faraday induction remains unchanged. The role of the scalar bridge is not to alter the identity but to guarantee that when A is interpreted as ΛA κᶜθᶜ, the same induction law emerges automatically.

## III.2 Gauss’s Law for Magnetism

$$
\nabla \cdot B = \nabla \cdot (\nabla \times A) = 0.
$$

Comment: This expresses the absence of magnetic monopoles. In scalar terms, κᶜθᶜ always derives from a curl structure, so closed flux is guaranteed.

## III.3 Gauss’s Law for Electricity (Vacuum)

For source-free regions (ρ = 0):

$$
\nabla \cdot E = \nabla \cdot (-\partial t A - \nabla \phi ) = -\partial t (\nabla \cdot A) - \nabla ^{2}\phi .
$$

In Coulomb gauge (∇·A = 0), this reduces to

$$
\nabla \cdot E = -\nabla ^{2}\phi  = 0.
$$

With sources present, the usual relation ∇·E = ρ/ε₀ defines charge density via φ and A.

Comment: Scalar bridges don’t interfere with charge definition; they only re-express A in terms of slope and stiffness, which can still be recovered point-by-point.

## III.4 Ampère–Maxwell Law (Vacuum or with Sources)

Define D = ε₀E and H = B/μ₀ in vacuum. Then:

$$
\nabla \times H = J + \partial t D
$$

$$
\nabla \cdot D = \rho 
$$

with the continuity equation ∂tρ + ∇·J = 0.

Comment: The scalar bridges supply physical content for A, but the Ampère–Maxwell structure remains intact. Because `A_comp` = ΛA · G · (κᶜθᶜ), and G is fixed by geometry/gauge (not fitted), the inversion formulas for θᶜ and κᶜ remain stable. Energy flow and charge conservation follow unchanged, ensuring that standard laboratory observables (E, B, J, ρ) map consistently to scalar recursion variables.

## III.5 Wave Equation in Vacuum

Take curl of Faraday’s law and substitute Ampère–Maxwell (J = 0):

$$
\nabla \times (\nabla \times E) = -\partial t (\nabla \times B) = -\mu _{0}\varepsilon _{0} \partial t^{2}E.
$$

Using the vector identity ∇×(∇×E) = ∇(∇·E) − ∇²E and ∇·E = 0 (vacuum), we obtain:

$$
\nabla ^{2}E - \mu _{0}\varepsilon _{0} \partial t^{2}E = 0,
$$

and similarly for B.

Comment: The wave equation emerges in its standard form, with light speed c = 1/√(μ₀ε₀). The scalar bridges therefore reproduce classical wave propagation exactly, confirming that re-expressing A in terms of κᶜθᶜ does not distort propagation.

## IV. Energy Conservation and Momentum (Poynting Theorem)

The energy stored in the electromagnetic field and its flow through space are described by the energy density u and the Poynting vector S. In vacuum these take the familiar form:

$$
u = \tfrac12  \varepsilon _{0} E^{2} + B^{2}/(2 \mu _{0})
$$

$$
S = (1/\mu _{0}) E \times  B
$$

To see how conservation arises, we combine Maxwell’s equations.

Take Ampère–Maxwell’s law:

$$
\nabla \times H = J + \partial t D.
$$

Dot this equation with E:

$$
E\cdot (\nabla \times H) = E\cdot J + E\cdot \partial t D.
$$

Now take Faraday’s law:

$$
\nabla \times E = -\partial t B.
$$

Dot this equation with H:

$$
H\cdot (\nabla \times E) = -H\cdot \partial t B.
$$

Subtract the two relations and use the vector identity:

$$
\nabla \cdot (E\times H) = H\cdot (\nabla \times E) - E\cdot (\nabla \times H).
$$

This yields:

$$
\partial t (\tfrac12  \varepsilon _{0} E^{2} + \tfrac12  \mu _{0}^{-1} B^{2}) + \nabla \cdot (E\times H) = -E\cdot J.
$$

Identifying energy density and Poynting vector, we obtain the conservation law:

$$
\partial t u + \nabla \cdot S = -E\cdot J.
$$

Comment: This expression states that the time rate of change of electromagnetic energy in a volume plus the net flux of energy out of the volume equals the work done on charges inside.

## Scalar Bridge Interpretation

The magnetic energy term, B²/(2 μ₀), connects directly to the scalar recursion energy via the bridge:

$$
B^{2}/(2 \mu _{0}) = \Lambda u \cdot  \tfrac12  (\kappa ^{c} \theta ^{c})^{2}.
$$

This means that the same energy density which drives electromagnetic dynamics is also interpretable as the scalar recursion energy of slope and stiffness. No new parameters are introduced—Λu is a one-time calibration constant.

Thus Poynting’s theorem simultaneously conserves electromagnetic energy and scalar recursion energy. The bridge confirms that standard electromagnetic experiments already provide direct access to underlying scalar balances.

## V. Testbed: long solenoid (formal derivation and point-of-use inversion)

## V.1 Geometry and fields (long-solenoid limit)

Consider a cylindrical solenoid of radius R with turns-per-length n carrying current I(t). In the long-solenoid approximation (length ≫ R), edge effects are negligible inside r<R, and the standard textbook fields are:

$$
B(t) = \mu _{0} n I(t)
$$

(axial, uniform inside)

$$
A\phi (r,t) = \tfrac12  r B(t)
$$

(azimuthal potential inside)

$$
E\phi (r,t) = -\tfrac12  r dB/dt
$$

(from E = −∂tA and symmetry ⇒ ∇φ = 0)

These relations fix A and B directly from the lab setup and determine the induced azimuthal electric field during transients.

## V.2 One-time calibration of bridges (ΛA, Λu)

Choose a single reference configuration (Iref, Bref, Aref at some rref>0). The calibration bridges

$$
A = \Lambda A \cdot  (\kappa ^{c} \theta ^{c})
$$

$$
B^{2}/(2 \mu _{0}) = \Lambda u \cdot  \tfrac12  (\kappa ^{c} \theta ^{c})^{2}
$$

are fixed once by matching the measured Aref and Bref (any consistent choice suffices; thereafter ΛA and Λu remain constant for the platform). No further tuning is performed in subsequent experiments.

Note on measurability: Inside a long solenoid, Aφ is inferred from B via Aφ = ½ r B by symmetry; outside the ideal region, A can be reconstructed numerically from B using ∇×A = B and a chosen gauge. For the long-solenoid testbed in Coulomb gauge, the geometric factor is G = r/2. ΛA and Λu are calibrated once; G is fixed by geometry/gauge and is not a fit parameter.

## V.3 Point-of-use inversion for scalar recovery

Given measured fields (`A_comp`, B) at any (r,t) with `A_comp` ≠ 0 and B ≠ 0, recover the scalars directly:

$$
\theta ^{c} = (\Lambda A/\Lambda u) \cdot  (B^{2}/\mu _{0}) \cdot  1 / (A\_comp \cdot  G)
$$

$$
\kappa ^{c} = (\Lambda u/\Lambda A^{2}) \cdot  (A\_comp^{2} \mu _{0} / B^{2}) \cdot  1 / G^{2}
$$

Here `A_comp` is the chosen component or magnitude of the vector potential (e.g., Aφ in the solenoid), and G is a geometry factor fixed by gauge and symmetry (e.g., G = r/2 in a long solenoid under Coulomb gauge).

For the long-solenoid case:

$$
A\phi  = \tfrac12  r B
$$

$$
G = r/2
$$

Then A_comp / G = B, making (κᶜθᶜ) uniform wherever B is uniform. As a result, Λu · ½ (κᶜθᶜ)² matches B²/(2μ₀) point-wise.

Thus causal slope θᶜ and stiffness κᶜ are computed directly from the same laboratory fields that define the solenoid test. No assumptions about their values are required.

Uncertainty propagation (first-order, relative): If A and B have fractional uncertainties δA/A and δB/B, and G is known with uncertainty δG/G:

$$
\delta \theta ^{c}/\theta ^{c} \approx  \sqrt{[ (2 \delta B/B)^{2} + (\delta A/A)^{2} + (\delta G/G)^{2} ]}
$$

$$
\delta \kappa ^{c}/\kappa ^{c} \approx  \sqrt{[ (2 \delta A/A)^{2} + (2 \delta B/B)^{2} + (2 \delta G/G)^{2} ]}
$$

(If G is exact from geometry, drop δG/G.) These relations guide instrumentation specs—for example, prioritize B precision when recovering θᶜ.

## V.4 Re-deriving Faraday induction from scalar update

Think of the current as the paddle and the field as the displaced water: A varies with proximity (∝ r) while B settles uniformly; the factor G normalizes this geometric proximity so that scalar energy tracks the uniform B²/(2μ₀).

Use the electric-field definition:

$$
E = -\partial t A - \nabla \phi .
$$

In this symmetry ∇φ = 0, so:

$$
E\phi  = -\partial t (\Lambda A G \kappa ^{c} \theta ^{c}) = -\partial t A\phi .
$$

From Aφ = ½ r B(t), we immediately obtain:

$$
E\phi  = -\tfrac12  r dB/dt,
$$

which is Faraday’s law for the long-solenoid geometry.

Here κᶜ and θᶜ were not assumed; they were recovered from Aφ and B, while G normalized the geometry, and the scalar update reproduced the classical induced field identically.

## V.5 Practical notes and edge cases

- Gauge and geometry: Aφ is gauge-dependent but fixed by symmetry in the long-solenoid case. In Coulomb gauge (∇·A = 0), the geometric factor is G = r/2, which normalizes the r-scaling of Aφ. When reconstructing A numerically from B in other geometries, enforce a consistent gauge so that G is well defined and not treated as a tunable parameter.

- Axis behavior: At r = 0, Aφ = 0, making inversion formulas ill-defined. Avoid the axis when computing θᶜ and κᶜ.

- Finite length: For solenoids of finite length, B(r,z) is not perfectly uniform; use measured B and reconstructed A in the inversion formulas rather than relying on the long-solenoid idealization.

- Outside region (r > R): Fields differ from the ideal interior relations. The scalar bridges still apply using the actual measured A and B.

- Instrumentation: Measure B with a calibrated Hall probe or fluxgate. Infer Aφ via symmetry (inside) or reconstruct numerically from B using ∇×A = B in a fixed gauge.

- Consistency checks:

  - For constant B, Eφ → 0.

  - Dimensional analysis: [A] = Wb·m⁻¹, [B²/μ₀] = J·m⁻³, so θᶜ and κᶜ are dimensionless under the bridges.

  - Reversing I flips B and A but leaves κᶜ θᶜ invariant under the energy bridge.

  - Verify that Λu · ½(κᶜ θᶜ)² = B²/(2 μ₀) across different radii when G is enforced, confirming gauge/geometry consistency.

## V.6 Minimal experimental protocol (step-by-step)

1. Calibrate ΛA, Λu once using a known current and geometry. For a solenoid, select a reference point `r_ref` and use the analytic relation Aφ = (r/2)B to set G = r/2.

2. Sweep I(t) to generate dB/dt while logging B(r,t) and inferring Aφ(r,t). Always record the geometry factor G used in the inversion.

3. Compute θᶜ, κᶜ at each (r,t) using the inversion formulas with `A_comp` and G included.

4. Predict Eφ from −∂t(ΛA κᶜ θᶜ) and compare to probe measurements (or to −½ r dB/dt).

5. Assess decoherence effects: if noise elevates Σₜ, expect increased scatter in θᶜ recovery during rapid transients.

Summary: The long-solenoid protocol demonstrates how laboratory measurements of A and B, together with the geometry factor G, allow direct recovery of scalar variables and validation of Faraday induction without parameter tuning.

## VI. Media, constitutive response, and gauge

## VI.1 Linear isotropic media

In homogeneous isotropic media the macroscopic relations D = εE and B = μH hold, with ε and μ possibly frequency-dependent. The scalar bridges defined earlier remain unchanged, since they attach at the level of vector potential A and magnetic energy density. Medium response is introduced through ε and μ in the usual way: charges and currents contribute via polarization P and magnetization M, defined by D = ε₀E + P and B = μ₀(H + M). Thus the scalar recursion formalism coexists with standard constitutive models; no additional bridges are required.

## VI.2 Boundary conditions

At material interfaces, the Maxwell boundary conditions apply:

- The tangential components of E are continuous unless surface current density is present.

- The tangential components of H jump according to surface current K: n×(H₂−H₁)=K.

- The normal component of B is continuous: n·(B₂−B₁)=0.

- The normal component of D jumps according to surface charge density σ: n·(D₂−D₁)=σ.

Because the bridges tie directly to A and energy density, the recovery of θᶜ and κᶜ is performed on each side of the interface using the measured A and B there. In this way scalar values inherit the same discontinuities or continuities as the macroscopic fields.

## VI.3 Gauge considerations

Gauge transformations A → A + ∇χ, φ → φ − ∂tχ leave E and B invariant. The inversion formulas for θᶜ and κᶜ assume a gauge-fixed A; any gauge that reproduces the measured fields suffices.

In practice, Coulomb gauge (∇·A = 0) is convenient for inversion, but not mandatory. When reconstructing A numerically from B, consistency in gauge choice ensures θᶜ and κᶜ are stable.

Geometry factor note: For symmetric testbeds (e.g., solenoids), the geometry factor G must be defined in a fixed gauge. In Coulomb gauge, Aφ = (r/2)B implies G = r/2. Using inconsistent gauges would alter `A_comp` and therefore corrupt the inversion. Thus, always enforce a gauge where G is well defined and document G alongside field measurements.

## VI.4 Plane-wave propagation and impedance

In a homogeneous isotropic medium, seek plane-wave solutions of the form

$$
E(r,t) = E_{0} \exp[i(k\cdot r - \omega t)], B(r,t) = B_{0} \exp[i(k\cdot r - \omega t)].
$$

Maxwell’s equations impose:

$$
k\cdot E_{0} = 0
$$

(E transverse to propagation).

$$
k\cdot B_{0} = 0
$$

(B transverse as well).

$$
B_{0} = (1/\omega ) k\times E_{0}.
$$

Dispersion:

$$
|k|^{2} = \varepsilon \mu  \omega ^{2}.
$$

The intrinsic impedance of the medium is η = √(μ/ε), relating field magnitudes: |E₀|/|H₀| = η. In terms of scalar bridges, κᶜθᶜ extracted from A and B travels consistently with these relations; the calibration ensures that recovered scalars preserve wave impedance without additional tuning.

Here ω coincides with the field’s angular frequency — the emergent marker of sustained recursion in oscillatory EM solutions.

Comment: This shows that scalar recursion supports classical transverse plane-wave propagation identically. Phase velocity v = 1/√(με) emerges unaltered, confirming that scalar recovery is transparent to wave transport.

## VI.5 Energy transport in plane waves

For the plane-wave solutions above, the time-averaged energy density is

$$
\langle u\rangle  = \tfrac14  (\varepsilon  |E_{0}|^{2} + \mu ^{-1} |B_{0}|^{2}).
$$

Using B₀ = (1/ω) k×E₀ and |k|² = εμ ω², one finds |B₀| = √(εμ) |E₀|, so the electric and magnetic contributions to energy are equal. The time-averaged Poynting vector is

`⟨S⟩ = ½ Re(E×H*) = (|E₀|²/2η) ˆk,`

pointing along the propagation direction with magnitude consistent with ⟨u⟩ v, where v = 1/√(με).

Scalar bridge note: Because B²/(2 μ₀) = Λu · ½ (κᶜ θᶜ)², the magnetic contribution to ⟨u⟩ is simultaneously a measure of scalar recursion energy density. Thus energy conservation and transport in plane waves carry through identically in both electromagnetic and scalar descriptions.

## VII. Discussion and outlook

The scalar–electromagnetic bridges developed here demonstrate three central points:

1. Maxwell’s equations are reproduced identically once the standard field definitions are adopted.

2. Energy density in electromagnetic fields maps directly to scalar recursion energy through a single calibration constant Λu.

3. Point-of-use inversion formulas allow θᶜ and κᶜ to be extracted directly from laboratory fields A and B, enabling experiments that connect classical measurements to scalar dynamics.

The solenoid testbed illustrates this clearly: measured A and B determine θᶜ and κᶜ without assumptions, and updating the scalars yields Faraday induction exactly. This confirms that electromagnetic systems provide a clean, controlled environment to validate scalar recursion without altering predictive content. Electromagnetism, with its precision and experimental accessibility, is therefore an ideal proving ground.

Looking forward, several natural extensions emerge:

- Radiation reaction: scalar recursion may offer new insight into self-interaction energy flow, reframing issues such as the Abraham–Lorentz force.

- Complex media: frequency-dependent ε and μ allow tests in dispersive and anisotropic materials, providing further checks on the bridges.

- Covariant formulation: embedding the bridges into the four-potential Aμ and field tensor Fμν would connect scalar recursion directly with relativistic field theory.

- Quantum links: because Λu · ½(κᶜθᶜ)² is simultaneously magnetic energy density and recursion energy, engineered EM environments may serve as platforms to probe τᶜ persistence and Σₜ-driven decoherence.

Context within the larger framework. While this paper has presented electromagnetism in isolation, the scalar recursion formalism belongs to a broader program: the Aether Reality Kernel (ARK). Earlier work established how the same scalars θᶜ, τᶜ, κᶜ, dSₜ, and ω unify gravitational, thermodynamic, and quantum phenomena. Here, we have shown that classical electromagnetism also falls cleanly within this structure. The continuity across domains suggests that what appear as separate field laws are different projections of a common scalar geometry.

Conclusion. Electromagnetism stands as a precise and transparent domain in which scalar recursion reproduces every classical law without tuning, while also providing measurable pathways into the deeper substrat dynamics developed across the broader ARK series. This dual role—familiar and yet revelatory—marks it as a cornerstone in the continuing effort to unify physical law under scalar geometry.

## References

1. J. C. Maxwell, A Dynamical Theory of the Electromagnetic Field, Philosophical Transactions of the Royal Society of London, 155 (1865), 459–512.

2. O. Heaviside, Electromagnetic Theory, Vols. 1–3, London: The Electrician Printing and Publishing Company, 1893–1912.

3. R. P. Feynman, R. B. Leighton, M. Sands, The Feynman Lectures on Physics, Vol. II, Addison-Wesley, 1964.

4. J. D. Jackson, Classical Electrodynamics, 3rd Edition, Wiley, 1998.

5. D. J. Griffiths, Introduction to Electrodynamics, 4th Edition, Cambridge University Press, 2017.

6. C. Kittel, H. Kroemer, Thermal Physics, 2nd Edition, W. H. Freeman, 1980.

7. P. F. Percy Jr. and Curie, Aetherwave Unified Theory, Papers I–XXI, Zenodo (2023–2025).

## Appendix EM-A: Vector identities (Unicode)

The following vector calculus identities are used repeatedly in the derivations above:

$$
\nabla \times \nabla \phi  = 0
$$

$$
\nabla \cdot (\nabla \times A) = 0
$$

$$
\nabla \times (\nabla \times F) = \nabla (\nabla \cdot F) - \nabla ^{2}F
$$

$$
\nabla \cdot (E\times H) = H\cdot (\nabla \times E) - E\cdot (\nabla \times H)
$$

These relations ensure that the field definitions B = ∇×A and E = −∂tA − ∇φ generate a closed and internally consistent Maxwell system. They also guarantee that conservation laws (Poynting theorem) and wave equations follow directly from the scalar–electromagnetic bridges without additional assumptions.

## Appendix EM-B: Poynting theorem (derivation sketch)

Starting from Ampère–Maxwell and Faraday:

$$
\nabla \times H = J + \partial tD
$$

$$
\nabla \times E = -\partial tB
$$

Dot E into Ampère–Maxwell:

$$
E\cdot (\nabla \times H) = E\cdot J + E\cdot \partial tD.
$$

Dot H into Faraday:

$$
H\cdot (\nabla \times E) = -H\cdot \partial tB.
$$

Subtracting and using ∇·(E×H) = H·(∇×E) − E·(∇×H) yields:

$$
\partial t (\tfrac12  \varepsilon _{0}E^{2} + \tfrac12  \mu _{0}^{-1}B^{2}) + \nabla \cdot (E\times H) = -E\cdot J.
$$

Identifying u = ½ ε₀E² + B²/(2μ₀) and S = (1/μ₀)E×B gives the conservation law:

$$
\partial t u + \nabla \cdot S = -E\cdot J.
$$

## Appendix EM-C: Units and calibration bridges

ΛA and Λu are fixed once per experimental platform by matching a single reference configuration (for example, a known solenoid with calibrated current and geometry). Once chosen, these constants remain fixed; scalar quantities θᶜ and κᶜ are then computed directly from laboratory fields using the inversion formulas:

$$
\theta ^{c} = (\Lambda A/\Lambda u) \cdot  (B^{2}/\mu _{0}) / A
$$

$$
\kappa ^{c} = (\Lambda u/\Lambda A^{2}) \cdot  (A^{2} \mu _{0} / B^{2})
$$

This one-time calibration ensures consistency with SI units and prevents parameter tuning. Thereafter, scalar recovery is fully predictive at each measurement point.

## Appendix EM-D: Experimental notes and pitfalls

When applying the scalar–electromagnetic bridges in laboratory settings, several considerations ensure accurate scalar recovery:

1. Gauge choice and geometry factor

- A is gauge-dependent, but inversion formulas for θᶜ and κᶜ assume a consistent gauge.

- Coulomb gauge (∇·A = 0) is convenient and ensures geometry factors like G are well defined.

- In symmetric testbeds (e.g., long solenoid), record the geometry factor explicitly (G = r/2 in Coulomb gauge). Treat G as fixed by geometry/gauge, not as a fit parameter.

2. Zero crossings

- At r = 0 in cylindrical geometries, Aφ = 0, making inversion ill-defined.

- Avoid regions where A → 0 or B → 0 when computing θᶜ and κᶜ directly.

3. Finite-size effects

- In non-ideal solenoids, B is not perfectly uniform.

- Use actual measured B and reconstructed A, rather than relying solely on analytic forms.

4. Noise sensitivity

- θᶜ scales with B²/A, making it sensitive to small uncertainties in B.

- κᶜ scales with A²/B², so errors grow when B is small.

- Propagate uncertainties explicitly to determine instrument requirements.

5. Consistency checks

- Energy balance: verify B²/(2 μ₀) matches Λu · ½ (κᶜ θᶜ)².

- Symmetry: reversing current I should flip B and A but leave κᶜ θᶜ invariant under the energy bridge.

- Gauge stability: confirm that the chosen gauge keeps G fixed and that θᶜ, κᶜ remain consistent across different measurement radii.

Summary: These practical checks ensure scalar recovery is stable, reproducible, and directly comparable with electromagnetic measurements, allowing scalar recursion to be tested in the same controlled settings where Maxwell’s laws are already validated.
