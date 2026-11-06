# Session handoff — IC-05 clock-defined geometry and boundary work

Date: 2026-11-01. Curie. Parent head 5bdfaff12f57c9af421e69a905fb5178f2138c0e. Owner requested continued research and recording on the existing draft branch. No merge, main-branch, source-repository, raw/archive or policy changes authorized.

## Result

[IC-05](../investigations/identity-containment-05/README.md) returns to the source contracts instead of extending generic device analogies. XXV A.1's theta=arccos(N), static metric and GR calibration give a_support=c^2 grad(log N)=-c^2 tan(theta) grad(theta). An independently characterized acceleration profile determines clock ratios; the stated reference fixes the level. A raw relative clock ratio is not an asymptotically normalized lapse. If the causal potential has ordinary potential units, its local gradient/c^2 is inverse length, not theta; the paper's alternative potential definition/length map remains unspecified.

A fixed spherical background and a radial test-boundary mode s=ln(R/R0) supply an explicit f: theta=asin(sqrt(rs/R0)*exp(-s/2)). This s is not IC-04's in-plane dielectric strain. Static clocks, independent background calibration, negligible boundary backreaction and common energy reference are essential conditions. It is a conventional calibration example, not a new ARK derivation of GR.

For independently measured generalized work response T and frozen-state tangent Ks, the coordinate map requires tau_W=-2T cot(theta), kappa_W=4Ks cot(theta)^2+2T csc(theta)^2. These W-labeled candidates are not canonical ARK scalars. Mode weighting, orientation, normalization and force-versus-work units are explicit. At evolving retained state z, dot(tau_W)=kappa_W dot(theta)+partial_z(tau_W)*dot(z). Stiffness also leaves a history-dependent response offset undetermined. Thus a full boundary response and XVIII's path accumulator need a specified regime or extra evolution law before being equated.

## Execution and evidence

Fourteen named grouped symbolic/generated-data checks passed. Script SHA-256: 4ddd37773eb95b17ffc4a34c8219eb85440ea8d2a9b9b9d3b168965d6aa1ee1a. Python 3.13.5, SymPy 1.14.0; exact runtime and results in test-results.json. Independent numerical implementations check the profile integral and energy derivatives with refinement; this is not independent human/AI review or a blinded physical test. Prior IC code was not rerun. No experimental data fitted or digitized. No full-corpus/PDF re-audit. Archive CI is a separate preservation check.

Source access is recorded [here](../sources/identity-containment-05-primary-sources.md): archived XVIII/XXV; Tong's metric/static normalization; Chou et al. author abstract. Bothwell et al. was inspected only at metadata level; full Nature page access failed. No physical tau, kappa, medium, charge origin, particle lifetime or new clock effect established.

## Next task

Inspect ARK's archived field-energy/variational formulations for a dimensioned energy, causal-stress definition and retained-state dynamics. Determine whether they supply the mode-specific work density and memory reference required here. Do not choose tau=stress, tau=z or tau=relaxation time by analogy. Do not call a coordinate transformation a new observable. Preserve the distinction between the user's intended mechanical picture and conditional mathematical realizations. Additional laws are new development, not recovered source content.

ASRP: detected risk of equating local gradient with clock level and force-valued stress with energy-valued conjugate response; corrected by explicit normalization, spatial integration, mode work and unit accounting. Detected risk of erasing memory with a coordinate change; corrected by the full state derivative and history-offset control. Both constructive mapping and its non-identifications are retained.
