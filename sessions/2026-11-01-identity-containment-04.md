# Session handoff — IC-04 electromechanical observation of retained state

Date: 2026-11-01 America/Chicago. Curie. Parent head `050cefd7578209724f68da84ed7a01828bcba3a4`. Owner authorized continued research and repository notes; no archive, policy, source-repository or main-branch edits and no merge authorized.

## Durable result

[IC-04](../investigations/identity-containment-04/README.md) makes the IC-03 comparator electromechanically explicit. Declared homogeneous equal-biaxial incompressible geometry gives C=C0*exp(4s). A quadratic local memory energy plus Q^2/(2C) gives V=Q/C, mechanical generalized load L=Ke*s+m-2QV, and positive dissipation with m=Km(s-z), zdot=(s-z)/tr.

Electrical measurement alone at fixed shape cannot distinguish z. Independently calibrated joint channels give s=log(Q/(C0*V))/4, m=L+2QV-Ke*s and z=s-m/Km. These are conditional conventional inverse estimates, not independently measured universal ARK scalars. Geometry, charge, total source current, voltage, load, internal coordinate and stiffness must not be conflated.

Crucial refinement: m can relax to zero while z retains the adapted configuration. A subsequent unloading exposes it. Zero excess stress does not imply absent history, absent restoring stiffness or lost identity. Do not select tau=m solely because of the word memory. A drive is not the retained state, a relaxation time is not an identity lifetime, and positive balance is not frozen microscopic dynamics.

## Evidence and execution

[Primary-source register](../sources/identity-containment-04-primary-sources.md) records actual inspected source ranges and PDF screenshots. Conventional dielectric literature distinguishes internal mechanical history from electrical polarization and current leakage. A relevant experimental paper was inspected qualitatively, not fitted or digitized.

Seventeen grouped local symbolic/generated-data checks passed. Final script SHA256 and runtime versions are in test-results.json. A reconstructed initial memory propagates to a separate imposed ramp with RK4 cross-check; max load discrepancy at 128 steps is approximately 1.09e-11 J for arbitrary unit-consistent fixtures, not physical accuracy. Negative controls include unknown load offset, permittivity drift, zero-signal inversion, held-shape memory blindness and untransformed coordinate relabeling. Covariance retains shared electrical channels.

Prior research files/code were not changed or rerun. No independent second reviewer. GitHub archive CI is a separate preservation check. No new result establishes a charged-medium origin, physical clock effect, full ARK model, or neutron lifetime.

## Next gate

Require a declared tau contract and an independently justified mapping from measured boundary variables to the same theta/kappa used in XXII and XXV. A hypothetical theta=f(s) changes the conjugate load to L/f' and tangent to (K_s*f'-L*f'')/(f')^3; it is not a label replacement. f has not been supplied. XXII's magnetic-potential bridge is not the capacitor voltage used here. Avoid expanding into more analogies without resolving that constitutive bridge.

ASRP: risk of calling electrical sensitivity to geometry a measurement of all retained history; corrected by an explicit observation-rank test and a load-channel reconstruction. Risk of equating relaxation with identity loss; corrected by a stored-configuration/unloading control. Both constructive results and failures are preserved.
