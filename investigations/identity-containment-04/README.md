# IC-04 — Reading boundary memory through electromechanical measurements

Date: 2026-11-01 America/Chicago. Parent research commit: `050cefd7578209724f68da84ed7a01828bcba3a4`. Draft PR #2; not authorized for merge. Status: conditional measurement construction and comparator verification, not identification of physical ARK scalars.

## Result in one paragraph

A retained internal configuration, an excess restoring response, an applied drive, and a relaxation time are different quantities. In an ideal-dielectric comparator, the electrical readout at prescribed shape does not distinguish mechanical histories. A simultaneous mechanical-load observation supplies the missing information. We derive explicit joint-channel inversions, a dissipative evolution law, and a subsequent-response test. The comparator is now electromechanically coupled, rather than an isolated mechanical analogy, but it is NOT the magnetic-potential bridge of XXII or a clock measurement. It does not derive charge or validate a vacuum medium.

Read with [IC-03](../identity-containment-03/README.md), [source/access notes](../../sources/identity-containment-04-primary-sources.md), and the [session handoff](../../sessions/2026-11-01-identity-containment-04.md). The owner's boundary hypothesis remains [separately attributed](../../history/mechanistic-notes/2026-10-31-boundary-identity-charge.md).

## 1. Source contracts, not a silent definition change

[Paper XVIII](../../raw/papers/paper-018-recursive-scalar-geometry-conv-01.md), section 2.2, gives a tension-memory integral of stiffness times slope velocity. [XXV](../../raw/papers/paper-025-disciplined-containment-conv-01.md), Appendix A.3, gives a boundary causal-stress integral and calls tau history dependent. Neither passage supplies the complete contraction, units, material law and measurement conversion used below. XXV A.1's clock ratio and [XXII](../../raw/papers/paper-022-electromagnetism-conv-01.md) II's magnetic energy/vector-potential bridge remain separate source claims.

For this study we retain new comparator variables: s (observable logarithmic deformation), z (retained internal configuration), m (excess mechanical response), T (total material response), L (external mechanical generalized load), and t_r (relaxation time). None is silently renamed tau, theta, kappa, epsilon or omega. In particular, m is NOT the external drive, and s is NOT a proper-time ratio. The same-state and units bridge to ARK remains unresolved.

## 2. A declared, bounded physical regime

Consider a thin, homogeneous, incompressible dielectric layer with compliant electrodes and equal in-plane stretches lambda. Temperature and permittivity are held fixed. Fringing, leakage, inertia, damage and independent dielectric relaxation are neglected only for this comparator. Field equilibration is assumed fast relative to the mechanical memory evolution. These conditions are not asserted for all materials or actual experimental datasets.

The reference area and thickness are A0 and h0. Let s = ln(lambda). Incompressibility gives

$$
A=A_0e^{2s},\qquad h=h_0e^{-2s},\qquad C(s)=\varepsilon A/h=C_0e^{4s}.
$$

Here C0 = epsilon A0/h0. The factor four follows from the declared geometry; it is not tuned against a response. Q is STORED electrode charge, not XXII's product q and not total integrated source current in a leaky circuit. V=Q/C is the terminal voltage. Equal in-plane electrode displacement does not mean every real sample is homogeneous; source E2 specifically cautions against inferring uniform stress from some measured loads.

The mechanical free energy is a local, single-mode phenomenological choice:

$$
\Psi(s,z,Q)=\frac12K_e s^2+\frac12K_m(s-z)^2+\frac{Q^2}{2C(s)}.
$$

The quadratic log-strain energy is our illustrative constitutive law, not the finite-strain Gent model of E1 or a fit to E2. Its range must be limited before use with physical data. Ke and Km are positive energy-valued coefficients for this dimensionless mode; tr is in seconds; C0 is in farads; Q in coulombs; V in volts.

## 3. Boundary work separates applied load from retained response

Define m=Km(s-z), T=Ke s+m. At fixed z and Q,

$$
V=\partial_Q\Psi=Q/C,\qquad L=\partial_s\Psi=T-2QV.
$$

Thus the material response inferred from a complete quasistatic mechanical load measurement is T=L+2QV. The electric work-conjugate outward contribution is 2QV. L is not generally a load-cell force in newtons: for the equal-biaxial mode, L=P1*l1+P2*l2, because delta li=li delta s. Required supports and additional loads must be included. The retained material response is inferred through balance, not identified with the drive.

Adopt the dissipative law

$$
\dot z=(s-z)/t_r,\qquad\dot m=K_m\dot s-m/t_r.
$$

It gives the exact work balance

$$
L\dot s+V\dot Q=\dot\Psi+\frac{m^2}{K_m t_r}.
$$

Dissipated power is nonnegative. This is conventional isothermal free-energy bookkeeping, not an identification of thermodynamic heat with ARK's unresolved entropy term.

A useful frozen-state cross-response check follows without a new coefficient:

$$
\left.\partial_Q L\right|_{s,z}=\left.\partial_s V\right|_{Q,z}=-4V.
$$

It is an equality of mixed derivatives for this potential. A measurement allowing z to relax is a different derivative and is not required to satisfy the same frozen-state comparison.

## 4. What the electrical measurement can and cannot reveal

With nonzero same-sign Q and V and independently characterized C0,

$$
s_E=\frac14\ln\!\left(\frac{Q}{C_0V}\right).
$$

A direct geometric measurement gives s_M=ln(lambda). Comparing s_E and s_M tests the stated capacitance/geometry/permittivity mapping; it does not yet compare two determinations of causal theta.

At fixed s and Q, voltage is independent of z. Distinct retained configurations can therefore have identical geometry and electrical readings, but different mechanical loads. The observation map (s,z) -> (s,V) has rank one. Adding the load, the determinant of the map (s,z) -> (V,L) is 4*Km*V, nonzero when Km and V are nonzero.

The resulting explicit conditional reconstruction is

$$
\boxed{m=L+2QV-K_e s_E,\qquad z=s_E-m/K_m.}
$$

This is a JOINT electrical/mechanical inference, not an independent electrical determination of universal tau. Ke, Km and C0 must be separately calibrated; they are not recovered as three independent identity scalars by this inversion. It is a two-state comparator with specified controls and material parameters. Unknown calibration factors enlarge its unknown state.

Constructed example: Ke=2 J, Km=3 J, C0=1 F, s=0.1, Q=0.2 C. With z=0 or z=0.1, both states have C=1.4918247 F and V=0.1340640 V, while m is 0.3 or 0 J and L is 0.4463744 or 0.1463744 J. These are unit-consistent software fixtures, not an apparatus specification or measured material values. The extra load observation recovers the two distinct states.

## 5. Adaptation is not necessarily disappearance of history

At a long held shape, z approaches s and m approaches zero. Yet z need not approach zero, Ke remains positive, and the identity need not fail. A rapid subsequent unloading to s=0 at initially fixed z gives m=-Km*z. The retained configuration becomes visible through that new response even though the prior excess stress had vanished.

Consequently, total response T, excess response m, and internal configuration z must not all be called the same memory variable without a specified conversion. The comparator does not select tau=m merely because m has been called a retained stress. XXV's persistence interpretation may require a baseline or a broader state mapping. A decline in excess stress alone is not a derivation of identity decay or of a particle lifetime.

## 6. Environmental controls determine the tangent

For prescribed voltage, include source work through

$$
\mathcal G(s,z,V)=\Psi_m(s,z)-C(s)V^2/2.
$$

At matched Q=CV the required mechanical loads agree, but the frozen-z total tangents differ:

$$
K_Q=K_e+K_m+8QV,\qquad K_V=K_e+K_m-8QV.
$$

The material tangent itself is Ke+Km. Ke is its relaxed value. K_V can lose positivity within this reduced voltage-controlled model; that is not a complete multidimensional stability or breakdown calculation. Charge reversal preserves these mechanical expressions while reversing V. The signed charge input is retained, not derived from pressure.

## 7. A clock-coordinate mapping must transform the response too

Suppose a FUTURE independently justified mapping supplies theta=f(s), with nonzero f', with other internal states held fixed. Work conjugacy then requires

$$
\tau_\theta=\frac{L}{f'},\qquad
\kappa_\theta=\frac{K_s f'-L f''}{(f')^3}.
$$

The preload term matters. The corresponding product theta*kappa_theta is not generally s*K_s. This is a coordinate calculation, not a determination of f or a physical assertion that tau is the total load. A material-only response T has its own analogous transformation. If f depends also on z, Q or other variables, additional coupling terms are required. A unit normalization also needs a stated reference scale.

No clock data or physical f was supplied or fitted here. XXII's bridge involves magnetic energy and a gauge-specified vector potential, not this capacitor's voltage. Applying it to this device without a new mapping would be an unearned substitution.

## 8. Error controls and a prospective use of data

A changed permittivity or capacitance reference is degenerate with inferred geometry: if true C=C0*g*exp(4s) but g is omitted, s_E-s=ln(g)/4. A 1% unmodeled change generates a log-strain bias 0.00248758 in the constructed check. A constant unknown load offset is indistinguishable from an offset in inferred m. Stored charge must be distinguished from leakage charge. Nonuniform shape, temperature drift, multiple relaxation modes and electrode contributions need independent characterization, not a fitted residual called epsilon.

For measured channels y=(L,Q,V,C0,Ke), first-order covariance is J*Sigma*J^T for outputs (s,m). The two Jacobian rows are

```text
s: [0, 1/(4Q), -1/(4V), -1/(4C0), 0]
m: [1, 2V-Ke/(4Q), 2Q+Ke/(4V), Ke/(4C0), -s]
```

Shared Q,V,C0 uncertainties therefore cannot be counted as independent confirmations. The linear approximation must be checked near zero signal and for large uncertainty.

A physical test would independently characterize geometry, controls, equilibrium response and history law; freeze them; reconstruct an initial state; and predict a later load or deformation not used in that reconstruction. The present code does only the generated-data version. It reconstructs m0 once, propagates it through a different programmed ramp, and compares predicted load with an independently coded RK4 integration of z. No later load target enters the predictor.

## 9. Execution record and next gate

Run `python test_measurement.py --output test-results.json` with NumPy and SymPy. Seventeen grouped checks pass, covering derivatives, dissipation, observation rank/inversion, history blindness, unloading, controls, covariance, mapping and omission failures. The independently integrated constructed ramp converges with refinement: maximum load discrepancy at 128 steps is about 1.09e-11 J for the software fixture, not empirical accuracy. The report binds the exact script SHA-256 and runtime versions.

No experimental data were digitized, fitted or predicted. No physical ARK scalar, clock effect, charge origin, neutron lifetime or superfluid property was established. No independent second reviewer. Prior IC-01/02/03 code was not changed or rerun in this pass. Archive CI is separate from these local research tests.

The next gate is not another generic comparator: specify which sourced tau definition is the proposed measured quantity, its normalization, and the same-state mapping to theta/kappa. The joint-channel construction is a candidate instrument model; it does not supply that constitutive bridge automatically. A mapped ARK prediction should then be compared with the conventional comparator using equal information access.
