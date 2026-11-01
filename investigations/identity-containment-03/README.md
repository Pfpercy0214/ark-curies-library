# IC-03 — Boundary work, restoring response, and retained state

Date: 2026-10-31 America/Chicago. Parent: `ac4ed97ee5f3ecfd9dc256fd182447df28ca0fc4` (draft PR #2). Status: conditional operational reconstruction and conventional-comparator verification, NOT experimental validation of ARK. No raw, policy, main-branch or source-repository changes.

## Question and result

Can the boundary interpretation of identity supply a measurable tension-memory channel for [IC-02](../identity-containment-02/README.md), without defining it from the clock result it is meant to test?

A constructive partial answer is to distinguish (1) a specified deformation coordinate, (2) the work-conjugate load/restoring response, and (3) a retained internal state with its own evolution. This yields explicit conventional benchmarks and a measurement plan. It does NOT yet identify any of them with a clock-defined ARK scalar or establish a common electromagnetic/clock/material state.

The owner's explanation is preserved separately in [H-B01](../../history/mechanistic-notes/2026-10-31-boundary-identity-charge.md). Source register and access limits: [primary-source notes](../../sources/identity-containment-03-primary-sources.md).

## 1. Preserve the source distinctions

Paper XVIII section 2.2 writes tension memory as an integral of stiffness times slope velocity. On the selected branch IC-02 used `d tau = kappa d theta`. Paper XXV Appendix A.3 instead presents `tau^c = integral_boundary sigma^c dot dA` and calls it history-dependent boundary adaptation. The contraction, physical units, and history law of that stress integral are not fully specified there.

If sigma is a conventional stress tensor and dA an oriented area vector, the unweighted integral is a force vector. If the normal stress magnitude is integrated over scalar area, it is a force-like scalar. Neither choice is automatically an angle-conjugate response or a memory timescale. This is an unresolved measurement definition, not a license to correct the historical paper.

We use NEW comparator notation below: s is a measurable deformation coordinate, T_s a restoring response, m a retained stress contribution, z an internal configuration, and t_r a relaxation time. None is silently renamed theta^c, tau^c, kappa^c, epsilon or omega. A driving load is not itself the retained state; actual transport also needs its own law.

## 2. A scalar that retains the deformation pattern

Let r(a,s) describe a material boundary, where a labels its surface and s specifies a deformation. For a physical traction t_b (force per area), the virtual work is

$$
\delta W_b=\int_{\partial\Omega}\mathbf t_b\cdot\delta\mathbf r\,dA
=\mathcal L_s\,\delta s,
\qquad
\mathcal L_s=\int_{\partial\Omega}\mathbf t_b\cdot\frac{\partial\mathbf r}{\partial s}\,dA.
$$

This is the ordinary virtual-work construction, used here as a CANDIDATE measurement bridge. It is a scalar for a declared deformation, not a complete encoding of an arbitrary boundary. Different deformation patterns generally require different generalized loads. We do not claim tensor/vector information has disappeared.

For dimensionless s, L_s has energy units. For a length coordinate it has force units; for an angular coordinate it has torque units. A normalization L_s/U_ref is dimensionless only after an independently stated energy reference. This is not the same object as an unweighted traction integral.

For a conservative material branch with free energy Psi(s,z), define the positive resisting response `T_s = partial_s Psi` at fixed internal state z. A measured external load equals T_s only when the relevant quasistatic balance includes all loads; inertia, supports, pressure, field momentum and other contributions cannot be ignored when present. The electric load alone is not automatically tau.

### Zero resultant does not imply zero deformation work

Use a prescribed spherical conducting boundary in vacuum, radius R, signed charge Q, no external field, electrostatic conditions:

$$
E_n=\frac{Q}{4\pi\epsilon_0 R^2},\quad
p=\frac{\epsilon_0 E_n^2}{2},\quad
U_Q=\frac{Q^2}{8\pi\epsilon_0R}.
$$

The resultant vector force is zero because `integral n dA = 0`. But the load for uniform radial dilation is

$$
F_R=4\pi R^2p=-\left.\frac{\partial U_Q}{\partial R}\right|_Q
=\frac{Q^2}{8\pi\epsilon_0R^2}.
$$

With `s=R/R0`, `L_s=R0 F_R`, which is nonzero for nonzero Q. Translation and dilation are different boundary motions; a translational resultant cannot characterize dilation. A supporting material or constraint is required to maintain the prescribed shape. This is not a free-droplet stability calculation.

Charge reversal changes E but not p or U. Therefore the mechanical load alone cannot recover charge sign. Signed electric flux retains that information. Q is an INPUT in this benchmark: no origin, quantization or new conservation law for charge is derived.

## 3. Environmental control changes the measured tangent

At fixed voltage V, an ideal source exchanges charge with the boundary. The relevant reduced electrical potential is `G_V = U - VQ = -C(R)V^2/2`, with `C(R)=4 pi epsilon0 R`. It gives the outward load `F_V=2 pi epsilon0 V^2`. Using `-partial_R(CV^2/2)` alone gives the wrong sign because it excludes source work.

At the same instantaneous R,Q,V with Q=CV, fixed-Q and fixed-V loads agree. Their radial tangents do not:

$$
\left.\partial_R F\right|_Q=-\frac{2F}{R},\qquad
\left.\partial_R F\right|_V=0.
$$

This is an explicit example of the surroundings participating in the observed response. It does not prove the material stiffness changed. A total response includes both material and electrical contributions, with the declared external constraint. Real source impedance and finite redistribution times need a dynamic circuit model outside this electrostatic limit.

A boundary coordinate must also be fixed. If `s=f(u)`, work conservation requires

$$
T_u=T_s f'(u),\qquad
K_u=K_s[f'(u)]^2+T_s f''(u),\quad K_s=\partial_s T_s.
$$

The preload term cannot generally be discarded. It vanishes when the particular transformed total response is zero; a material restoring load can remain nonzero in equilibrium with an external load. Apparent scalar agreement after arbitrary reparameterization is not independent physical agreement.

## 4. A retained-state comparator with an explicit energy balance

Use the standard-linear-solid idea, written as one generalized small-deformation mode:

$$
\Psi_m(s,z)=\tfrac12 K_e s^2+\tfrac12 K_m(s-z)^2,\qquad
\dot z=(s-z)/t_r,
$$

with `K_e,K_m,t_r > 0`, s and z dimensionless, K values in energy units, and t_r in seconds. These are declared material parameters of the conventional comparator, not newly asserted universal ARK constants.

Define

$$
m=K_m(s-z),\qquad T_s=K_e s+m.
$$

Then

$$
\dot m=K_m\dot s-\frac{m}{t_r},\qquad
\dot T_s=(K_e+K_m)\dot s-\frac{m}{t_r},
$$

and

$$
T_s\dot s=\dot\Psi_m+\frac{m^2}{K_m t_r}.
$$

The last term is nonnegative dissipation. This is mechanical/free-energy bookkeeping for an isothermal comparator, NOT a definition of ARK entropy. For a consistent isothermal thermal description the dissipated power becomes heat; no identification of that heat with Delta S_t is made.

At a held shape `s=s0` after a step from an initially relaxed state:

$$
T_s(t)=K_e s_0+K_m s_0e^{-t/t_r}.
$$

The boundary geometry can remain fixed while the retained contribution changes. Frozen-z tangent stiffness is `K_e+K_m`; fully relaxed stiffness is `K_e`. The same shape can have different responses after different histories. Neither response magnitude nor t_r is automatically an identity lifetime or a failure threshold.

Two tau interpretations are therefore distinct candidates: the full work-conjugate response T_s, which contains memory, or the retained component m. They have different response laws. z can be eliminated in favor of m; we are not claiming ARK must add a fourth independent identity scalar. What must remain explicit is the memory law and the material parameters it requires.

## 5. Consequence for IC-02, and a falsification control

IC-02 deliberately assumed `q=kappa theta` and `dot tau=kappa dot theta`, with no unaccounted extra contribution. More generally, on a branch with an independently specified extra evolution term r,

$$
\dot\tau=\kappa\dot\theta+r,
\qquad
\frac{d\ln\theta}{dt}=\frac{\dot\tau-r}{q}.
$$

This identity is NOT permission to fit r to the desired clock or geometry result. It must come from a separately justified response law, initial state and measurements. The same concerns apply to other controls and cross-couplings.

For the conventional comparator only, tentatively identifying tau with T_s and kappa with the frozen-z tangent makes `r=-m/t_r`. At held shape, the corrected numerator vanishes. Ignoring r makes IC-02's formula incorrectly infer a changing shape.

With manufactured `K_e=2`, `K_m=3` and one relaxation time of waiting, the uncorrected formula gives `H=0.684359...`, although actual relative geometry is exactly 1. This rejects extending that memory-free tangent inference to this relaxing comparator. It does NOT reject IC-02's explicitly narrower mathematical branch or ARK as a whole. These numbers are dimensioned comparator choices/normalized illustrations, not measured physical ARK values.

## 6. Constructive measurement and transfer plan

First choose a physically observable boundary deformation and the stress/force components that do work on it. Establish geometry, normalization, source condition, thermal state and initial history independently. A load cell plus displacement/shape measurement can define a mechanical response; the conversion into T_s requires the actual deformation map. A relaxation measurement tests whether a frozen-memory tangent is appropriate.

For an initially relaxed state with a calibrated zero-load reference in the stated single-mode comparator, a step response identifies K_e from its plateau, K_m from its excess initial response, and t_r from the transient ratio. An unknown load offset cannot be separated from K_e by one plateau at one amplitude; it needs an independent baseline or additional amplitudes. Freeze the identified quantities, then calculate a different ramp response:

$$
s(t)=v t,\qquad T_s(t)=K_e vt+K_m v t_r(1-e^{-t/t_r}).
$$

We tested this sequence on generated data and an independent RK4 integration of the z equation. It verifies implementation, not a blind experiment. No apparatus purchase, high-voltage operating procedure, or physical setup is prescribed.

One-mode identifiability is not general identity reconstruction. We also constructed two distinct relaxation spectra with the same initial value, final value and integrated relaxation, but different intermediate responses. Zero transient amplitude leaves t_r unidentified. Real measurement uncertainty, drift, extra modes and a wider relaxation spectrum need their own study before using physical data.

## 7. Executed checks and limits

Run `python test_boundary.py --output test-results.json` with NumPy and SymPy. The committed report binds the exact script SHA-256 and runtime versions. **36 named checks passed**, including expected failures of the wrong-sign voltage calculation, memory-free held-shape reconstruction and insufficient relaxation summaries. The manufactured ramp comparison converged under refinement; absolute error at 64 steps was about `3.79e-11` in comparator response units. No claim about experimental precision follows.

The unchanged IC-01 and IC-02 scripts were matched to their repository Git blobs and rerun: 12/12 and 20/20 passed. Rerun JSON records are included in the downloadable packet. Archive CI is separate and does not run these research tests. No independent reviewer or full-corpus/PDF-conversion audit was performed.

## 8. Next physical gate

We now have concrete candidate observations for geometry, restoring response and retained history. What is missing is an independently justified bridge from that resolved boundary state to the SAME theta/tau/kappa used by the EM and clock relations. Ordinary deformation s must not simply be renamed the clock angle. Force, integrated stress, energy-conjugate response, relaxation time and lifetime must not be silently interchanged.

A useful next derivation must select the meaning of tau, state its units and history law, and specify how causal geometry maps to an actual boundary deformation. It should predict a different response with frozen mappings. Positive scalar reduction results and counterexamples both remain in the record; no new equality is promoted to canonical physics here.
