# Session handoff — IC-16 coupled-core candidate, 2026-11-05

Parent/source head: 8f76c310c5beb5e36a3a974dad9e9ec451f0d4b1. Owner authorized continuation of structure-first reconstruction, not merging. NIST track remains paused and no measurement files were read.

[IC-16 study](../investigations/identity-containment-16/README.md); [machine-readable state contract](../investigations/identity-containment-16/core-contract.json). Code and actual local results are in the study directory.

Source findings: XVI's tension integral and printed dimensional assignments need an explicit bridge; XVIII's normalized kappa=1/theta branch integrates to log(theta/theta_ref) and carries a reference but not additional closed-path history. General variable stiffness can retain path information. XXV makes omega dependent on pressure balance and supplies a functional class, not unique coupled kinetics. Preserve these distinctions rather than declaring a canonical definition.

New candidate, explicitly not recovered canon: independent normalized geometry q and retained state r, constitutive gradient coefficient Kg and tangent coefficient b (not silently equal), and derived balance W. Full energy variation retains coefficient and W chain terms. A quadratic rate potential supplies reciprocal feedback: chi*q_ddot+zeta*q_dot=-gq-b*gr; r_dot=b*q_dot-L*gr. Energy accounting includes damping, memory relaxation, external input and boundary work. Frozen, tangent-constrained and equilibrated states have different derivatives. A consistent finite-dimensional example is implemented, but physical functions/scales and correspondence to XXV D.1 remain unspecified.

11/11 new check groups passed on first run; exact substantive repeat output matched. Linear solution cross-checked by matrix exponential, IVP and RK4 refinement; nonlinear finite-lattice power balance included; no PDE convergence or global physical-stability claim. Unchanged IC-15 script matched Git blob 44d3fb8dd40ee35f86f4e0450c0f2ebdae5b39bb and reran 6/6. IC-01–14 not rerun. No independent reviewer, empirical fit, local whole-archive verifier or source-PDF audit. External references were the Onsager II publisher abstract and INL's official phase-field documentation, used only as conventional method baselines. No new physical evidence for ARK is claimed.

Next: source-grounded energy/stress and normalization mapping for the candidate or a competing closure. Need constitutive functions and rate inputs determined independently of target observables. Do not add epsilon to enforce D.1 agreement, do not call W an oscillation frequency, and do not let another isolated device comparison displace the core reconstruction.

Only new research files and navigation are proposed; raw/, manifests, policies, earlier studies and original repository remain unchanged. Publication hashes, PR state and preservation CI must be confirmed separately. No Ada task or background process has been initiated.
