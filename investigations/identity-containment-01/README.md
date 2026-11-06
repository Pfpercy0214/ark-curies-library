# IC-01 — Identity closure and the environmental baseline

**Date:** 2026-10-31 (America/Chicago). **Author:** Curie. **Mode:** source reconstruction and conditional mathematical derivation. **Status:** exploratory; symbolic checks executed; no empirical validation or independent reviewer yet.

Source snapshot: `Pfpercy0214/ark-curies-library@2db757753005e6ac66c55797890b2960bffe9307`. This working study does not change the historical papers, archive manifest, policies, or the original theory repository.

## Question and owner direction

The owner proposed that independently deriving the identity scalars could constrain the balancing environmental contribution without identifying the environment's configuration. A known environmental baseline might help resolve epsilon. The owner also proposed two independently grounded scalars plus another independently justified relationship as an alternative to three direct scalar determinations. This is a paraphrase of this session's research direction, not a claim that sufficiency is established.

We test the strongest limited version: **under a declared model and resolution, which combinations of identity and environmental variables are determined by the available information?** Three named scalars are not automatically three independent constraints, nor does a scalar field reduce to one number. Conversely, indirect derivation through fixed physical relationships is legitimate; statistical independence is not required. Shared uncertainties must be propagated. [C1]

Read the [versioned scalar-route map](scalar-route-map.md) for source locations, candidate measurements, and unresolved mappings. External literature and its access limits are in the [primary-source notes](../../sources/identity-containment-01-primary-sources.md).

## 1. A rate constraint is different from an absolute environmental level

Paper XXV Appendix D.1 gives the schematic equation [P25]:

$$
\nabla\cdot(\kappa^c\nabla\theta^c)-c^{-2}\partial_t^2\theta^c
=\frac{\tau^c}{\kappa^c}\partial_t(\Delta S_t)+\Lambda(\theta^c,\omega).
$$

For this calculation only, abbreviate the field `Delta S_t` by `S(x,t)`; its subscript is not another time derivative. Define

$$
R=\nabla\cdot(\kappa^c\nabla\theta^c)-c^{-2}\partial_t^2\theta^c-\Lambda(\theta^c,\omega).
$$

If the fields, derivatives, reference scales, and Lambda are known and tau and kappa are nonzero,

$$
\partial_t S=\frac{\kappa^c}{\tau^c}R,\qquad
S(x,t)=S_0(x)+\int_{t_0}^{t}\frac{\kappa^c(x,s)}{\tau^c(x,s)}R(x,s)\,ds.
$$

**Conditional finding IC-01-R1:** this isolated equation fixes a rate, not the integration baseline `S_0(x)`. With Lambda held fixed, adding any time-independent `C(x)` to S leaves D.1 unchanged. The baseline can be spatially structured, not merely one constant. This is not a claim about the complete coupled system: another independent algebraic or boundary relation can constrain it. If omega or Lambda changes with S, that dependence must be included in the joint problem before asserting a nullspace.

This makes the owner's baseline proposal mathematically concrete. A measured S at a reference time fixes this integration freedom, conditional on the model. An equilibrium constraint may also fix a level, but it must actually contain S with known coupling. Steady identity does not automatically imply all internal rates or fluxes vanish. At tau = 0 the rearrangement fails to identify Sdot; at kappa = 0 the quoted source equation is singular.

Three scalar values at one point do not supply spatial gradients, accelerations, Lambda, boundary data, or reference scales. Those may be independently known, derived, or additional unknowns; list them rather than assuming them away.

## 2. Total forcing does not identify its resolved and unresolved components

XXV Appendix B.2 uses `E = Delta S_t + epsilon_created`, while B.4 lists apparatus contributions. D.1 explicitly contains the derivative of `Delta S_t`, not the derivative of this E. A mapping between these representations is required; **this study does not silently replace one with the other.** [P25]

For any candidate law depending only on the sum E, the bookkeeping transformation

$$
S'=S-d,\qquad \epsilon'=\epsilon+d
$$

preserves E. Knowing E therefore does not separately identify both contributions. An independent determination of epsilon permits `S = E - epsilon` in this additive representation. It does not identify every physical mode contributing to S. The partition invariance applies to the same physical influence relabeled, not to differently coupled disturbances with equal numerical totals. [C1, section 5.4]

A baseline difference obeys

$$
E_1-E_0=(S_1-S_0)+(\epsilon_1-\epsilon_0).
$$

It measures the change in epsilon alone only if unresolved environmental drift is independently negligible, bounded, or separately measured. A baseline is not automatically an absolute zero of epsilon. Measurement error, numerical error, model error, and physical forcing remain separate records.

## 3. Which third constraint actually adds information?

XXII sections II and V use the bridge pair [P22]

$$
u_B=\frac{\Lambda_u}{2}(\kappa^c\theta^c)^2,\qquad
A_{\mathrm{comp}}=\Lambda_A G\kappa^c\theta^c.
$$

With fixed nonzero calibration and geometry factors, both depend only on `q = kappa theta`. The exact continuous transformation `theta -> a theta`, `kappa -> kappa/a` preserves the pair. On the nonzero domain their measurement Jacobian has rank one, not two. This is an exact symmetry of these bridges, not a conclusion from a singular-point rank test.

**Conditional finding IC-01-R2:** adding an independently grounded tau gives two independent state combinations. Adding an independent theta measurement for the same resolved state raises the rank to three and gives `kappa = q/theta`, provided the bridges and cross-measurement correspondence are valid. This is a concrete possible route, not a claim that all three measurements currently exist for a neutron or any particular apparatus. A computed A from the same B under a fixed gauge does not add an independent physical constraint merely because A has a new name.

The owner's two-scalars-plus-a-relation alternative is also sound in principle. For example, the **illustrative, additional constitutive assumption**

$$
\tau-\tau_0=\kappa(\theta-\theta_0)
$$

with independently established constant kappa behavior and reference values gives `kappa = (tau-tau0)/(theta-theta0)` from theta and tau. Its local constraint determinant is `theta-theta0`; the reference point is degenerate. This law is NOT declared to be universal ARK mechanics. Its provenance and tests matter as much as a third instrument's provenance.

XVIII section 2.2 instead gives a path integral `tau = integral kappa (dtheta/dt) dt`. For the exact branch with no additional memory evolution, `d tau = kappa d theta` is a tangent relation. It does not generally imply `tau = kappa theta`: integration needs a reference and the path-dependent kappa. For `tau = theta^2 + C`, tangent stiffness is `2 theta`, while the secant ratio is `theta + C/theta`. Reversible integration alone does not establish hysteretic memory. [P18]

Full column rank supplies a regular local uniqueness test for a declared finite-dimensional map, not a global guarantee or adequate precision in noise. A rank deficiency at an isolated singular point is not alone proof of nonuniqueness. These tests supplement, rather than replace, the physical specification. [M1]

## 4. A separate printed-inversion issue

As archived, XXII's point-of-use formulas are

$$
\theta_p=\frac{\Lambda_A}{\Lambda_u}\frac{B^2/\mu_0}{A_{\mathrm{comp}}G},\qquad
\kappa_p=\frac{\Lambda_u}{\Lambda_A^2}\frac{A_{\mathrm{comp}}^2\mu_0}{B^2G^2}.
$$

Their product is `A_comp/(Lambda_A G^3)`, whereas the stated A bridge requires `A_comp/(Lambda_A G)`. Thus these expressions do not generally invert that bridge. The formal ratio is `1/G^2`; normalization and units require their own audit. Choosing a special G does not resolve the product degeneracy or establish a general inversion.

**Finding IC-01-R3:** a local algebraic inconsistency in the archived formulas. No archival text was changed; no corrected inversion was invented. This session did not repeat PDF fidelity review. Determine which bridge/version was intended before proposing a new formulation. A problem in this pair is not a verdict on every other derivation route.

## 5. Executed checks and next construction

Run from the repository root, in an environment with SymPy (tested with 1.14.0):

```bash
python investigations/identity-containment-01/test_closure.py --json investigations/identity-containment-01/test-results.json
```

[Recorded result](test-results.json): 12 exact symbolic/manufactured-example checks passed. They cover bridge symmetry and rank, a constructive extra-anchor route, a conditional constitutive route, tangent versus secant stiffness, D.1 rearrangement and baseline freedom, partition degeneracy, baseline drift, and the printed-inversion discrepancy. Synthetic constants and fields are test fixtures, not fitted physical results. PASS verifies these narrow mathematical statements, including diagnosed defects; it does not validate ARK's mechanism or reproduce any experiment.

Next construction: select one identity and resolution; declare its units and state; choose one theta route and one independent resistance/persistence route; specify all constitutive and environmental couplings; evaluate the joint constraints; then predict an observable not used in that reconstruction. The neutron apparatus mapping remains a later target, not an accomplished calculation.

**Working conclusion:** identity closure, environmental-level recovery, resolved/unresolved partition, and environmental microstructure reconstruction are distinct achievements. A valid result at one level can be useful without claiming all four.

Sources: [P18, P22, P25, C1](scalar-route-map.md); [M1 and E1](../../sources/identity-containment-01-primary-sources.md).
