# IC-19 — Pressure work: a bounded environment-to-identity coupling

Parent/source head: `61d2c129fb6d6e4032cf98748e54b45cd3f17c00`. Execution timestamps are preserved in UTC in [results.json](results.json).

**Status:** source-law compatibility analysis with constructed verification. This supplies a conditional mechanical pressure channel, not an absolute environmental entropy, a validated medium, or a selected universal core. Detector work remains paused. Historical sources and previous studies are unchanged; no merge is authorized.

## Purpose and provenance

[IC-18](../identity-containment-18/README.md) made the environment responsive but left its physical normalization and coupling open. The present bounded question is: **what must a measured pressure do in the candidate identity equations if the interaction obeys independently specified pressure-work accounting?**

The archived sources provide three separate statements:

1. Paper I, sections 4–5: an energy proportional to `k^c (Delta theta^c)^2/2`.
2. Paper XXV, A.4: internal causal pressure proportional to `theta^c^2 kappa^c`, balanced against an external entropy-pressure contribution.
3. XXV E13–E16: a source-like environmental term `-Pi(Delta S_t) theta^c` in an effective field functional.

They do not, in the inspected passages, supply a common dimensional normalization, an operative pressure-work volume, or a proof that the early energy and late pressure law are the same thermodynamic sector. Those are the conditions tested here, not facts silently imported from other models. Original proportionalities remain proportionalities; the scales introduced below are explicitly additional inputs.

The conventional benchmark is reversible mechanical work at specified temperature and composition: an imposed, spatially uniform pressure contributes `-p dV` to work on the system, or `+p V` to the total potential used at fixed external pressure. The corresponding Helmholtz pressure relation is `p=-partial F/partial V`. These are external thermodynamic/virtual-work constraints, not derivations of the proposed substrat. Sources and exact access limits: [source record](../../sources/identity-containment-19-pressure-work.md).

## 1. A measured pressure needs a deformation map

Let `x=(q,r)` denote declared, dimensionless geometry and retained-state coordinates. Let `V(x)` be the physical volume conjugate to the particular pressure-work channel, and `E_*` an energy normalization. This does **not** assume all matter excludes the proposed medium from its visible bulk volume. A permeating medium may require a different work coordinate or a full traction map, to be derived independently. For the present channel the relevant work is assumed to be `-p delta V`.

Uniform hydrostatic traction on an oriented surface is `t=-p n`. Its generalized load for a specified deformation is

$$Q_i=\int_{\partial\Omega}\mathbf t\cdot\frac{\partial\mathbf X}{\partial x_i}\,dA=-p\frac{\partial V}{\partial x_i}.$$

Hence the normalized mechanical drive is

$$\boxed{J_i^{(p)}=-\frac{p}{E_*}V_{,i}.}$$

For a controlled pressure change at the same configuration, the corresponding change is `delta J_i=-(delta p/E_*) V_,i`. A measured pressure and an independently characterized work-volume derivative can therefore fix a **particular resolved environmental contribution**. They do not determine an absolute `Delta S_t` or epsilon unless the additional map into those latent variables is specified.

The code independently integrates hydrostatic traction over an ellipsoid and checks the volume derivative. Net translational force vanishes while the generalized deformation loads do not. This is a check of work geometry, not a new empirical finding or a finite-deformation claim derived from linear elasticity alone.

At fixed p the environmental contribution to the normalized tangent matrix is `p V_,ij/E_*`. A static uniform pressure can therefore affect response whenever the work-volume map is nonlinear. It is not automatically an irrelevant constant.

### Connection to the source-like Pi term

For a specified mode `theta^c=theta_ref^c+theta_* q h(x)` in an energy-normalized field functional, the reduced source coefficient is `theta_* integral Pi_phys h dV / E_*`, when Pi is independent of the varied state. A pressure coupling must reproduce the generalized load above; `Pi_phys=p` is not a generally valid identification.

For the simple affine map `V=V_* (1-alpha q)`, the environmental energy is a constant minus `p V_* alpha q`, giving the mode drive `p V_* alpha/E_*`. That is one explicit regime in which the source's linear driving form can match pressure-work.

For a nonlinear V, the exact environmental potential is `p V(q,r)`, not a state-dependent coefficient multiplied by q without its derivative. For example, a force `J=pc/q` has potential `-pc log q`; replacing it with `-J(q)q` gives a constant and loses the force entirely. This does not show the source's independent-Pi variation is wrong. It prevents extending that variation into a responsive-Pi regime by substitution alone.

If V depends on r, pressure also acts in the r equation. The two components come from the same potential and obey matching cross derivatives. Deleting the r component while retaining q–r dependence can produce a non-integrable load. Such a load would need an explicit driven/nonconservative account, not a claim to the same passive stored energy.

## 2. A compatibility condition directly connects two archived claims

Choose a restricted branch with q positive, retained state fixed, a positive constant k, and common calibrated scales `E_*` and `P_*`. For this conditional comparison identify the early stored-energy expression with the reversible fixed-temperature potential, up to state-independent terms:

$$F_{\rm id}=\frac{E_* k}{2}q^2,\qquad p_{\rm int}=P_*kq^2.$$

This additionally aligns the early zero of `Delta theta` with the q=0 reference used in the late pressure expression. It is not automatically valid at an arbitrary energy reference or for state-dependent k.

If that pressure is mechanically conjugate to V along this mode, then

$$p_{\rm int}=-\frac{F_{{\rm id},q}}{V_{,q}}.$$

Consequently the two laws require

$$\boxed{V(q)=V_{\rm ref}-\frac{E_*}{P_*}\log(q/q_{\rm ref}).}$$

The ratio `E_*/P_*` has volume units. This is a **conditional necessity**, not a measured volume law, a new definition of theta, or a globally valid geometry. The chart requires q>0, V>0, and the independently declared range of the causal-angle map. It is singular at q=0 and cannot be silently extended to the full vacuum/reference limit.

At imposed external p, stationarity of `F_id+pV` yields `q^2=p/(P_* k)`, and the one-coordinate loaded curvature is `2 E_* k>0`. That proves a local minimum only in this restricted mode. It says nothing by itself about history relaxation, other shapes or full field stability.

For a nonzero energy reference `q_e`, keeping `F_id=E_*k(q-q_e)^2/2` instead requires

$$V(q)-V(q_{\rm ref})=-\frac{E_*}{P_*}\left[\log(q/q_{\rm ref})+q_e\left(\frac1q-\frac1{q_{\rm ref}}\right)\right].$$

At q=q_e the volume derivative vanishes, making the pressure-as-ratio coordinate description singular there. The reference is physical bookkeeping that cannot be discarded. If k changes with q, its derivative also enters; the constant-k logarithmic result no longer follows unchanged.

## 3. A second consistent completion has the same pressure balance

Suppose instead that an independently justified deformation map is affine:

$$V=V_{\rm ref}-\Lambda(q-q_{\rm ref}),\qquad \Lambda>0.$$

Keeping the same squared-slope pressure law requires

$$\boxed{F_{\rm id}=\frac{\Lambda P_*k}{3}q^3+\text{reference},}$$

on the positive-q branch. The environmental term is now genuinely linear in q. The pressure equilibrium is again `q^2=p/(P_*k)`, but the energy and deformation law are different. A cubic energy here is an explicitly derived alternative completion, not a rewrite of the archived quadratic law or a globally bounded potential for negative q.

This is not a contradiction that must be repaired by adding entropy. It is a constitutive choice the current proportionalities do not settle. If all three claims are to hold simultaneously in the same sector, the work-volume map cannot be left unspecified.

### Matching one state does not choose the whole constitutive law

The generated comparison deliberately matches the two candidates at `q_ref=0.5`, with `E_*=P_*=1`, `k=2`, `V_ref=3`, and `Lambda=2`. References are aligned so both have the same energy, volume, generalized identity response and loaded stiffness at the reference pressure p=0.5.

| Quantity | Both at reference | Quadratic/log-volume at p=2 | Cubic/affine-volume at p=2 |
|---|---:|---:|---:|
| q | 0.5 | 1.0 | 1.0 |
| V | 3.0 | 2.3068528 | 2.0 |
| identity response F_id,q | 1.0 | 2.0 | 4.0 |
| loaded q-stiffness | 4.0 | 4.0 | 8.0 |

These are dimensionless constructed examples, not observations. The higher-pressure state was not used to align the reference. Separate numerical minimizations recover both analytical equilibrium branches, and pressure-work quadrature recovers their different stored-energy changes.

This does not establish that three independent anchors fail for an already specified finite-dimensional model. It distinguishes **reconstructing a state under fixed laws** from **selecting a constitutive law using one state**. Additional calibrated deformation/work response could choose between these candidates; merely checking their shared pressure balance cannot.

## 4. The environment's extra restoring response can have physical units

IC-18 represented environmental curvature abstractly. For a declared finite, isothermal reservoir sharing a constrained total work-volume, write

$$V_e=V_{\rm total}-V(x),\qquad F_{\rm total}=F_{\rm id}(x)+F_e(T,V_e),$$

with `p_e=-partial F_e/partial V_e` and bulk modulus `K_e=-V_e partial p_e/partial V_e` under the specified thermal/composition conditions. The environment's contribution to the coordinate Hessian is

$$\boxed{H_e=p_e H_V+\frac{K_e}{V_e}\,\nabla V\nabla V^T.}$$

The second term is positive semidefinite when `K_e>0`. It supplies a physically dimensioned extra restoring contribution relative to an ideal pressure reservoir at the same state. In a normalized environmental-volume coordinate `u=delta V_e/V_s`, the corresponding energy curvature is `B=(K_e/V_e)V_s^2/E_*`, subject to the same constraints.

This is not in conflict with IC-18's Schur-complement softening. There we compared freeing an independently relaxable coordinate with holding it clamped. Here total volume constrains the environment to respond to the identity's displacement; it is compared with an ideal fixed-pressure bath. The permitted variations are different.

A generated reservoir with `F_e=-C log V_e` (positive reference units understood), C=2.5 and reference V_e=5 has p=0.5. In the logarithmic branch above it increases the loaded q-curvature from 4.0 to 4.4 without changing the reference equilibrium. A controlled reduction of total volume from 8 to 7.8 moves the equilibrium to q=0.50933038. Root finding and separate minimization agree. Second derivatives converge under refinement. This is a specified illustrative reservoir equation of state, not a measurement of ARK entropy or a claimed model of the universal medium.

Particle amounts are fixed in this pressure-work calculation. That is a stated thermodynamic constraint, not a claim that every identity boundary is impermeable. Actual particle exchange, heat transport, shear, electromagnetic traction or steady throughflow requires its additional work/flux terms. Nor is the work-volume automatically the macroscopic excluded volume of an atom or object.

## 5. A direct environment-to-identity prediction is now available conditionally

For a fixed-temperature potential `G(x,p)=F_id(x)+p V(x)` at a smooth stable equilibrium with Hessian H, differentiating its equilibrium condition gives

$$\boxed{\frac{dx_*}{dp}=-H^{-1}\nabla V.}$$

If H, the geometry map and their scales are independently characterized, this predicts the first-order response to a pressure change. Along that unconstrained stable branch,

$$\frac{dV}{dp}=-\nabla V^T H^{-1}\nabla V\le0.$$

Clamped retained variables, zero modes, phase transitions and other constraints require the appropriate reduced problem; the inverse cannot be used across a singular branch. The code checks this against finite differences and a separate pressure-step equilibrium in a two-coordinate example. This is a conventional conditional response relation that can serve as an observable-mapping test, not a new empirical ARK law.

The volume sensitivity needed here cannot be obtained from the same pressure-step response and then used to claim that response was independently predicted. A calibration on one range followed by a frozen comparison on another is legitimate, with shared uncertainty disclosed.

Temperature is not substituted for pressure. For a physically defined Helmholtz sector, the ordinary entropy is `S_th=-partial F_id/partial T`, giving `partial_T partial_i G=-partial_i S_th` while `partial_p partial_i G=partial_i V`. These generally act in different directions in the state space. A short symbolic counterexample records this fact; no separate thermal model or conversion to ARK Delta S_t is claimed.

## 6. Baselines and the environmental entropy remain distinct

A consistent bookkeeping reassignment `p->p+c`, `F_id->F_id-cV` leaves the total potential unchanged. Changing p alone while retaining the same independently fixed F_id is a different physical loading and generally changes the state. Thus a reference convention is not a license to erase physical background pressure from every observable.

A resolved pressure contribution can now be computed in work units under a declared mapping. For example, prescribed p=200,000 Pa, V_q=-3e-12 m3 and E_*=2e-6 J give normalized drive 0.3. These are illustrative independent inputs, not an experiment. Converting that drive to a latent environmental variable still requires a fixed map Pi(Delta S_t,epsilon,...). Different unknown map scales assign different entropy-like numbers to the same drive. Neither the absolute background nor its S/epsilon partition has been recovered.

The constructive gain is therefore limited and explicit: **we can replace one unspecified environmental contribution by an independently interpretable work channel, and derive what the archived internal-pressure claims would require of its geometry.** The remaining couplings are not concealed inside a fitted residual.

## Verification and next core decision

Run `OPENBLAS_NUM_THREADS=1 python check_pressure_work.py --output new-results.json`. All **13** groups passed on the first run; repetition gave identical substantive output excluding the UTC timestamp. Checks include independent surface integration, exact derivatives, both source-law completions, numerical minimization, pressure-work quadrature, finite-reservoir Hessians/refinement, coupled equilibrium sensitivity, consistent reference changes and failure controls. Code is an explicit finite-mode test, not a continuum stability theorem or physical validation. No independent second reviewer or experimental data were used.

The unchanged IC-18 script was matched to Git blob `a8f2c9564ef3bb48c4b4e3fe72fe610dd4177fd3` and rerun: **13/13 passed**. Its rerun report is in the download, not substituted for the previous repository result. IC-01–17 were not rerun. No source-PDF re-audit or local whole-archive verification was performed; remote archive-preservation CI is separate.

**Next decision:** identify an independently supported deformation/work-volume mapping for a declared physical regime, or show that causal pressure is not ordinary mechanical pressure and specify the different coupling. Use that information to select or reject these completions before further scalar reduction. The two alternatives are not new canon. No additional device, detector or cosmology fitting is required to state this structural question.
