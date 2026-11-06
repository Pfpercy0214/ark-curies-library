# IC-05 — Clock-defined geometry and the boundary-work bridge

Date: 2026-11-01. Parent research commit: `5bdfaff12f57c9af421e69a905fb5178f2138c0e`. Draft PR #2; no merge authorization. Status: source-contract audit, conventional static-gravity calibration, and conditional response transformation. No physical ARK scalar identification or new medium prediction.

## Result and scope

IC-04 left theta=f(shape) unspecified. This study supplies an explicit f for ONE declared radial mode in a fixed spherical gravitational background, using XXV's clock definition and the conventional metric as a calibration surface. It also derives a general static acceleration-to-clock integral, identifies its reference requirement, and shows exactly how a measured boundary-work response transforms. The remaining memory ambiguity is not removed by that coordinate transformation.

This is not another proposed material model and not a solution of the full ARK PDE. The radial mode below is NOT IC-04's equal-biaxial dielectric strain. Electrical capacitor voltage is NOT XXII's magnetic vector potential. We do not combine them by renaming variables.

Read with [IC-04](../identity-containment-04/README.md), [sources and access limits](../../sources/identity-containment-05-primary-sources.md), [test results](test-results.json), and [handoff](../../sessions/2026-11-01-identity-containment-05.md).

## 1. The source contracts selected for this investigation

[XXV Appendix A.1](../../raw/papers/paper-025-disciplined-containment-conv-01.md) explicitly defines theta=arccos(d proper_time/d coordinate_time), with an asymptotic time reference. It also gives a weak-field mass/radius expression and a distinct expression involving the gradient of a causal potential. The latter potential's units and connection to the clock lapse are not specified in the inspected passage. We do NOT silently identify it with the Newtonian potential.

[XXV A.2](../../raw/papers/paper-025-disciplined-containment-conv-01.md) gives proportional mechanical, electrical and thermal stiffness routes; these are not complete unit-normalized equalities. A.3 defines boundary adaptation through an integral of causal stress density and states that tau is history dependent. Its full stress contraction, mode weighting and unit map remain to be supplied.

[XVIII sections 2.2–2.3](../../raw/papers/paper-018-recursive-scalar-geometry-conv-01.md) gives an integrated stiffness-times-slope-change route for tension memory and describes stiffness through resistance/energy curvature. It also contains other historical normalized definitions. The present calculation selects the tangent relation conditionally, not all those definitions simultaneously.

Preserve the user's intended distinction: geometry, retained history and resistance are separate roles; tau is not automatically the applied drive; a relaxation time is not automatically identity lifetime. Prior assistant formulations are not automatically user-approved definitions.

## 2. A clock angle is not a local force gradient

Use a static spacetime with lapse N(x)>0 and spatial metric h_ij:

$$
ds^2=-N(x)^2c^2dt^2+h_{ij}dx^i dx^j.
$$

For an observer held at fixed spatial position, d proper_time/dt=N. On the source's principal real branch 0<N<=1,

$$
N=\cos\theta.
$$

The proper acceleration covector required to remain static follows from the metric connection:

$$
a_i=c^2\partial_i\ln N=-c^2\tan\theta\,\partial_i\theta.
$$

The acceleration is the SUPPORT acceleration of the static observer. An inward gravitational-acceleration convention has the opposite sign. Spatial gradients and proper lengths must use h_ij. This relation is not a formula for arbitrary moving observers, rotating frames, or time-dependent metrics.

Along a specified spatial path gamma,

$$
\ln\frac{N(x)}{N(x_0)}=\frac{1}{c^2}\int_\gamma a_i dx^i,
\qquad
\theta(x)=\arccos\!\left[N(x_0)\exp\!\left(\frac{1}{c^2}\int_\gamma a_i dx^i\right)\right].
$$

Thus the profile supplies relative clock rates; the declared reference supplies normalization. In this static setting a_i/c^2 is an exact gradient. Unexplained path dependence in measured integrals would require checking systematics or the static assumption, not assigning it to epsilon by default. A single local acceleration value does not specify the profile or boundary value without additional geometric/model information.

A constant rescaling N -> A*N leaves acceleration and clock ratios unchanged but changes arccos(N). This is an unfixed time-normalization freedom, not a new physical adjustable parameter. XXV's asymptotic reference fixes it when that reference exists and is applicable. In a laboratory, two clock readings alone measure a ratio, not the asymptotically normalized N. A valid ratio can exceed one even when each N is below one; taking arccos of the raw ratio is then the wrong operation.

For an ordinary potential Psi=c^2 ln N, |grad Psi|/c^2 is an inverse length, not an angle. In a weak field Psi approximately equals the Newtonian potential and theta^2 approximately equals -2*Psi/c^2 in the chosen normalization. Therefore the literal gradient route in XXV A.1 needs an explicit integral/length mapping OR a different definition and units for Phi^c. This is a specific unresolved source bridge, not proof that no consistent bridge is possible. The clock route itself is well defined in its declared domain.

## 3. Explicit independent mapping for one boundary mode

Choose a static nonrotating spherical background of independently specified mass M. Let r_s=2GM/c^2. Outside the source, for R>r_s and asymptotically normalized time, the conventional Schwarzschild lapse is

$$
N(R)=\sqrt{1-r_s/R},\qquad
\theta(R)=\arcsin\sqrt{r_s/R}.
$$

This uses standard general relativity as a calibration surface; it does not derive that metric from ARK. The model inherits G, c, the background, static-observer choice and reference convention. The test boundary's backreaction is neglected explicitly. Matter deformation, charge, environmental fields or changing M cannot be added while silently retaining the same map.

Let the radial mode coordinate be s=ln(R/R0). Here s is a NEW radial coordinate, not the planar stretch in IC-04. Then

$$
\theta(s)=\arcsin\!\left(\sqrt{r_s/R_0}e^{-s/2}\right),
\quad f'=-\frac12\tan\theta,
\quad f''=\frac14\tan\theta\sec^2\theta.
$$

This is the missing f for that bounded case. It is not a universal map from material deformation to causal geometry. The same shape at a different gravitational background has a different clock angle. Likewise, different retained material states at the same R can have the same clock angle. The map knows where the boundary is in a declared gravitational field; it does not encode all of the boundary's internal history.

An independently characterized M/R profile predicts a clock ratio at another radius. Comparing that prediction to corrected clock data is a meaningful cross-observable test, but obtaining M from the same clock ratio and returning it is not independent confirmation. Motion, reference drift and clock-transition shifts must be independently treated. No such experimental dataset is analyzed here.

## 4. What boundary response is conjugate to this angle?

Let U(s,z) be a reversible stored-energy function for a specified boundary mode and retained state z, with a fixed energy reference and other controls stated. Define T=(partial U/partial s)_z and K_s=(partial T/partial s)_z. These can in principle come from calibrated mode-specific work measurements. They are not automatically universal ARK quantities.

Changing coordinates while preserving work gives the candidate response and tangent

$$
\tau_W=\left.\frac{\partial U}{\partial\theta}\right|_z=\frac{T}{f'},
\qquad
\kappa_W=\left.\frac{\partial\tau_W}{\partial\theta}\right|_z=
\frac{K_s}{(f')^2}-\frac{T f''}{(f')^3}.
$$

For the radial clock map this becomes

$$
\boxed{\tau_W=-2T\cot\theta,\qquad
\kappa_W=4K_s\cot^2\theta+2T\csc^2\theta.}
$$

The preload term is required. The label W means work-conjugate candidate, not an assertion that either quantity equals the physical tau^c/kappa^c throughout ARK. With dimensionless angles and log deformation, T, tau_W and kappa_W are energy-valued (or have the corresponding explicitly stated angular units). A density-based version requires its volume and measure to be fixed separately.

A conventional traction integral without mode weighting is force-valued. To infer a generalized response, its contraction with the actual boundary displacement must be supplied. For a radial mode in this fixed metric, local radial displacement is dR/N and local work redshifts by N; using energy referred to infinity gives T=R*F_radial. That factor R is not an optional cosmetic unit conversion. For general modes use the full traction/displacement work integral, not a scalar net force. The net vector resultant of a spherical pressure can vanish while radial-mode work is nonzero.

If XXV's sigma^c is NOT ordinary mechanical traction, its units and measurement relationship must instead be derived. We do not declare its printed integral erroneous by assuming missing units. The needed specification is now concrete: stress meaning, orientation, contraction, deformation mode, reference energy and any normalization.

Hessians also depend on coordinate and preload. Only at a stationary TOTAL controlled potential does the tangent sign transform simply by 1/(f')^2. A negative partial mapped tangent under an unaccounted preload is not by itself proof of physical instability.

## 5. Which tau contract survives a changing retained state?

At fixed z, the candidate pair satisfies d tau_W = kappa_W d theta by construction. Along a real changing history,

$$
\dot\tau_W=\kappa_W\dot\theta+
\left.\frac{\partial\tau_W}{\partial z}\right|_\theta\dot z,
$$

with additional terms for additional controls. Neither geometry nor coordinate transformation makes that second term disappear.

To test this fact, reuse the mathematical memory energy from IC-04 ONLY as a software fixture:

$$
U=\tfrac12K_e s^2+\tfrac12K_m(s-z)^2,
\qquad\dot z=(s-z)/t_r.
$$

This is not an asserted constitutive law for a gravitating shell. It gives

$$
\dot\tau_W-\kappa_W\dot\theta=2K_m\cot\theta\,\dot z.
$$

At held radius and fixed background, theta is constant while retained adaptation can change the response. XVIII's path accumulator integral(kappa*dtheta) and the complete work-conjugate response therefore cannot be identified over arbitrary histories without a specified restriction or extra evolution term. This limits THAT identification, not all ARK versions or every possible definition of tau.

There is a related reference ambiguity. Adding B(z)*theta to U changes tau_W by B(z) without changing kappa_W at fixed z. Consequently recovering stiffness and geometry does not automatically recover the complete tension-memory value. A separately specified response reference, boundary balance or state equation may provide it. That is consistent with the user's idea of closure by additional physical information; it is not a demand that every scalar be directly measured.

The field angle, the energy-conjugate response, a path accumulator, an internal retained coordinate, and a relaxation time must remain distinct until their bridge is shown. No one of them is selected as canonical by this study.

## 6. A focused physical test rather than a renamed analogy

1. Declare the identity region, background, static observer/reference, deformation mode, environmental controls and state variables. Fix the candidate tau interpretation and units BEFORE looking at the comparison output.
2. Independently characterize the geometric/gravitational route; predict corrected clock ratios. Preserve their covariance and prior calibration exposure. Physical clock-shift evidence is a benchmark, not evidence of a superfluid.
3. Measure mode-specific work and its frozen-history tangent. Account for support/electrical source work and reference energy. Transform with the independently specified f, including preload.
4. Vary retained history at fixed geometry/background. A changed boundary response with unchanged theta distinguishes response/history from geometry. If the proposed tau is a strict path accumulator, test its separate evolution rather than calling the observed stress that accumulator.
5. Freeze any required constitutive bridge and predict another load or clock comparison not used to fit it. A new residual does not identify its own cause; do not force it into entropy.

A practical laboratory design is NOT specified here. The spherical reference is an analytically controlled calibration problem. NIST/JILA clock experiments establish that gravitational clock differences are measured, but the inspected sources do not provide the complete boundary-work/history dataset needed for this bridge.

## 7. Verification and limitations

Run `python test_bridge.py --output test-results.json` with SymPy. Fourteen named grouped checks pass. They include exact lapse/acceleration identities, independently coded spatial quadrature with refinement, reference ambiguity, raw-ratio domain rejection, the explicit radial f, invariant work, direct-energy cross-checks, omitted-preload failure, held-shape memory evolution, history-dependent response offsets, information-rank preservation, force/work units, changed-background and clock-systematic negative controls, and cancellation-safe weak-signal evaluation.

Results bind the script SHA-256 and runtime. These are algebraic and constructed-data implementation checks, not fourteen experimental confirmations. The tests were written after formulating these derivations and are not a blinded evaluation. No external data were fitted or digitized; no independent second reviewer; prior IC tests were not rerun. No archived formula or policy was changed. No full-corpus or PDF-fidelity audit was performed. GitHub archive CI, when available, is separate from local research verification.

## Next gate

The clock-to-boundary coordinate gap is closed only for this declared static radial mode. The general ARK bridge still requires a sourced field energy/stress constitutive law and a retained-state evolution law with a common normalization. The next productive task is to inspect the archived field-energy/variational formulations for those ingredients, rather than append more unconnected device analogies. Any added law must be labeled new development and tested on an observable it did not supply as an input.
