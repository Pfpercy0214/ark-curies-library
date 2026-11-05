# IC-15 — Structure-first checkpoint: reconnecting the governing equations

Date: 2026-11-04. Source/parent commit: `bd21644284ed40cd1f097d68aa296a7f23e9f950`.
Status: source-based structural reconstruction with limited symbolic checks, not a completed core theory, empirical validation, or a repair of the historical papers.

## 1. Owner direction and immediate scope decision

The owner asked us to avoid pursuing a small apparatus issue at the expense of reconstructing the framework as a whole. The detector-specific work had become the immediate work queue even though it did not yet test a defined ARK rate prediction. This checkpoint changes the priority: **reconstruct the coupled mechanics and their measurement interfaces first.**

IC-10–14, the NIST data, and their unresolved issues remain preserved. Their empirical branch is **paused by research priority**, not declared resolved, invalid, or refuted. The IC-14 timing discrepancy belongs to a conditional apparatus-template comparison; it is not an ARK prediction residual. A detector export convention cannot decide whether the proposed identity/medium dynamics are internally complete.

This does not mean waiting until every domain is proven before consulting evidence. Empirical constraints remain part of core development. A narrow subproblem receives priority only when its possible outcomes distinguish an explicit structural choice or directly test a declared model output. No further detector fitting, new external comparator, or empirical claim is made in this session.

## 2. Intended mechanics versus what is mathematically specified

The current conversation supplies the intended picture: an identity is a persistent coupled configuration whose boundary describes interaction, not necessarily an impermeable enclosure. Shape, resistance, and retained history contribute to how it responds. The environment can act throughout the configuration; balance does not imply absence of internal motion or throughflow. These are owner hypotheses and modeling aims, not established observations of the proposed substrat.

Earlier-context retrieval corroborates the owner's emphasis on reconstructing the coupled mechanics before detector details and on deriving omega rather than assigning it independent agency. Retrieved summaries are orientation, not verbatim archival proof. The original papers and charter remain the mathematical sources.

The governing charter explicitly permits coupled inverse reconstruction and independently calibrated inputs. It also requires source/version, units, scale, roles, and admissible states to be declared. A change in notation is not sufficient evidence of a contradiction. Conversely, a shared name does not establish an operational equivalence.

The next deliverable is a **minimal closed candidate specification**: enough independently given or derived relationships to determine the intended outputs under declared initial/boundary conditions, or to characterize the remaining admissible family. It need not assign an independent evolution equation to every symbol if an actual algebraic or constitutive relationship determines it. It must not turn missing relationships into unconstrained environmental residuals.

## 3. Working core map, with unresolved links visible

This is an organizational map, not a newly proposed master equation:

```text
Resolved identity at a declared scale: geometry / response / retained history
               <--> environment and neighboring identities
                          |
              constitutive and boundary exchange laws
                          |
         coupled evolution / balance / allowed transformations
                          |
           persistence, transitions, transport, recurrent modes
                          |
       domain-specific observable map --> apparatus / recorded data
```

Pressure balance or a resulting recurrence belongs inside the coupled description; it is not an unexplained agent that makes the rest stable. The environment of a smaller identity can be resolved structure in a larger one. Changing that partition must preserve the stated information and physical coupling.

Three scalar *fields* are not three scalar numbers. Initial profiles, boundary geometry, retained-state information, and derivatives can be required even when the vocabulary is small. Two measured anchors plus an independent relationship may suffice for a particular state or reduced model; sufficiency must be demonstrated for that task, not inferred by counting symbols.

### First-pass source map

| Item | Source examined at the pinned commit | Role in reconstruction | Not silently assumed |
|---|---|---|---|
| theta | XVIII sections 2–3.2; XXV A.1 | Geometry descriptor with stated measurement routes | Clock-ratio angle, spatial gradient, and compact phase are not interchangeable without a map |
| tau | XVIII 2.2; XXV A.3 | Integrated response / boundary adaptation and history | A force integral, relaxation time, and full internal memory are not equated by terminology |
| kappa | XVIII 2.3; XXV A.2 | Resistance with multiple proposed empirical routes | Ratios and dimensional moduli require declared normalization; different regimes are not automatically contradictions |
| omega | XVIII 2.5 versus XXV A.4 | Versioned anchor/balance descriptions; XXV makes it dependent on other scalars | No independently assigned frequency or stabilizing action is imported |
| environment | XXV A.5; charter 5.1–5.5 | Resolved versus unresolved influence, with specified coupling | An inferred residual is not an independently measured perturbation or a free repair term |
| spatial core | XXV D.1, E6/E7/E12/E16 | Repeated stiffness-weighted divergence operator | Shared spatial form does not itself equate relaxation, wave propagation and recursion |
| stabilization | XXV E13–E16 | Effective functional with U(theta; tau, omega) and drive Pi | Its functional form, units, allowed variations, and physical identification are not yet supplied by this checkpoint |
| measurement | XVIII's independently grounded inputs; XXV A and C | Conversion between physical observations and selected state variables | Reconstructing an input is not a separate prediction, but legitimate inverse closure is not dismissed |

This is a scoped first pass, not a claim to have reread or certified all 25 papers. XVIII's alternative relations and XXV's schematic equations are preserved as stated. No universal kappa=tau/theta or automatic cross-domain equality is inserted.

## 4. A constructive connection already present in XXV

Let L_k(theta) abbreviate `div(kappa grad(theta))`. This is the source's spatial operator, not a replacement for the coupled theory.

XXV E6 states the transport form:

$$\partial_t\theta=D L_\kappa(\theta)+F.$$

Its stated stationary reduction E7 is

$$L_\kappa(\theta)=-F/D,$$

for nonzero D. XXV E13 defines

$$\mathcal F[\theta]=\int_V[\tfrac12\kappa(x)|\nabla\theta|^2+U(\theta;\tau,\omega)-\Pi(\Delta S_t)\theta]dV.$$

With kappa, tau, omega and the environmental drive held fixed during the variation, E15/E16 give

$$L_\kappa(\theta)=U_\theta-\Pi.$$

For these two source forms to describe **the same equilibrium**, using the same state, coefficients, coordinates and normalization, their source terms must satisfy

$$\boxed{F_* = D(\Pi-U_\theta)_*.}$$

This is an exact conditional compatibility relation, not a detector fit. The star denotes the shared equilibrium. It does not establish a global constitutive law for F away from that state, and it does not prove that all equilibria are stable.

One *optional extension*, explicitly additional to matching equilibria, is to use that source law at every state. Define

$$G=\delta\mathcal F/\delta\theta=-L_\kappa(\theta)+U_\theta-\Pi.$$

Then E6 becomes `theta_t = -D G`. For positive constant D, fixed coefficients and drive, and vanishing boundary work, its functional change is

$$\frac{d\mathcal F}{dt}=-D\int_VG^2\,dV\le0.$$

This is a possible coherent **relaxational sector**. It is not a derivation of all ARK dynamics, a physical total-energy conservation law, or a universal superfluid equation. Wave-supported behavior in E12/D.1 still needs its inertial/kinetic specification and a justified relationship to this sector. The source calls those formulations variants; this checkpoint does not silently identify them.

The source uses D=a^2/eta up to geometry factors and absorbs constant kappa into D in E8. Any comparison must preserve which convention is in force. Numerical rates cannot be inferred from the stationary operator alone.

## 5. The next structural choice is what varies together

XXV A.4 makes omega a dependent balance quantity. XVIII stresses coupling among the scalars. In contrast, the displayed E13–E16 derivative is the fixed-coefficient/fixed-parameter variation. Those descriptions can coexist, but the inference between them must be explicit.

For illustration of the distinction—not a new universal closure—suppose kappa=K(theta), tau=T(theta), omega=W(theta), with local algebraic dependencies and independently fixed drive. Varying the substituted functional gives

$$G_{\mathrm{coupled}}=-\nabla\cdot(K\nabla\theta)+\tfrac12K_\theta|\nabla\theta|^2+U_\theta+U_\tau T_\theta+U_\omega W_\theta-\Pi.$$

The partial U_theta here holds its other arguments fixed. Simply inserting responsive kappa/tau/omega into the already differentiated fixed-parameter equation can omit the additional terms. This is not a declaration that the archived fixed-parameter formula is wrong: it is correct for its declared variation. A constrained variation with multipliers, independent coupled field equations, or a history-dependent/nonlocal law can instead require a different treatment.

**The structural task is to decide which quantities are independent state variables, which are measured inputs, which are derived responses, and which are held fixed in each regime.** We cannot select an interpretation solely because it produces convenient equations.

No-flux boundary conditions also do not automatically preserve a field total once reaction/stabilization terms are present:

$$\partial_t\int_V\theta\,dV=D\oint_{\partial V}\kappa\nabla\theta\cdot n\,dA+D\int_V(\Pi-U_\theta)\,dV.$$

Whether theta is itself a conserved physical quantity must be established, not assumed. This is why earlier conserved-field and density/phase comparisons cannot silently become one model.

## 6. What we carry forward from the investigations

Prior study labels below summarize their stated scope in this conversation and the current repository handoff; their code/results were not rerun or independently reviewed here.

- IC-01–05: measurement identifiability, reference/baseline requirements, boundary work and retained-state distinctions. Conditional bridges to audit, not an already closed scalar theory.
- IC-06–09: constructive comparison models showing interfaces, conditional stability, winding and throughflow. Their potentials, kinetic coefficients, density/phase variables and constraints are not automatically native ARK state variables.
- IC-10–14: observation models, NIST receipt and conditional detector comparisons. Preserve as a future validation track; do not use their residuals to choose core laws.

The original source README describes the NIST package as representative charge-exchange material, not all data from a lifetime experiment. That narrow evidentiary purpose remains distinct from this project's governing-mechanics task.

No successful test of a conventional comparator establishes the proposed medium. No mismatch in a provisional detector conversion establishes failure of the core theory. Each result retains its actual scope.

## 7. Core completion gates and bounded work queue

**First: state and normalization contract.** Build a versioned map of theta, tau, kappa, omega and the environment at one specified scale. Record units, references, available independent measurement paths, geometric content and which relations are asserted versus demonstrated. Do not erase alternative source definitions or infer inconsistency before testing the mappings.

**Second: coupled closure.** Recover the relationships for kappa's response, tau's retained history, the environmental coupling Pi/Lambda/F, and the selected kinetic law. Allow derived variables and simultaneous solutions. Trace the information path and characterize any undetermined family. A name or proportionality alone is not a completed operational map.

**Third: structural compatibility.** Test source-to-source reductions, allowed variations, dimensional normalizations, boundary-work/exchange accounting, admissible initial/boundary data and the meaning of stability. Identify what is shared across domains and what legitimately depends on the physical state. Do not delete PDE terms simply to remove a disagreement.

**Fourth: a discriminating observable.** Specify a distinct observable from independent inputs or a frozen calibration. Choose an external measurement that directly constrains a core linkage. Small targeted tests are welcome before global completion; open-ended apparatus reconstruction is not the main track.

A narrow task is resumed only when we can state: the structural uncertainty it addresses; which alternative outcomes distinguish models; what independent inputs are available; and a concrete stopping/parking condition. The NIST track reopens when a declared ARK coupling and output make those records informative, or when a bounded calibration question is directly required for an agreed test. Pending export-convention questions remain unresolved, not assumed away.

This is a priority correction, not an instruction to insulate the theory from evidence or certify its correctness before testing. Structural coherence first, empirical constraints throughout, detailed apparatus work when it has a defined role.

## 8. Verification, provenance and limits

Primary repository texts: [Paper XVIII](../../raw/papers/paper-018-recursive-scalar-geometry-conv-01.md), [Paper XXV](../../raw/papers/paper-025-disciplined-containment-conv-01.md), and [Epistemic Charter v1.1](../../raw/epistemics/ARK_Epistemic_Charter_v1.1.md). Exact source versions are fixed by the parent commit above. [Executed checks](check_structure.py) and [actual results](results.json) are separate from the interpretation.

Source reads in this session: entry protocol, AGENTS, POLICIES, chronology, decision register, wiki index, charter v1.1 sections 4–6.9, current PR metadata and IC-14 handoff; XVIII sections 2–3.2; XXV portions of sections 9/12, Appendices A, C/D, and E. Relevant equations were read directly from Markdown. No whole-corpus reread, PDF re-extraction, or external literature search was performed. The NIST README was supplied in context. No scientific claim has been promoted to empirical confirmation.

Pinned source blobs: charter `ae341b2a7e30fc1d25703a1f6dbc032595fec707`; XXV `3bbf2a40a7c4bdde67f4bbeb2a29147f10a036f5`. XVIII and all equations are located by original path/heading at the parent commit, not by inferred publication chronology.

Run `python check_structure.py --output new-results.json` with SymPy. Six exact algebra/example checks passed and the final run repeated identically. The first attempt stopped because SymPy did not canonicalize two equivalent unevaluated multivariate derivative-substitution forms. We replaced that software assertion with a general K(theta) variation check and a separately labeled symbolic-polynomial chain-rule check; the initial script and failure record are in the packet. No source equation was altered to make a test pass. The final test's scope is narrower than a generic computer proof of arbitrary history-dependent closures.

No empirical fit, new numerical PDE experiment, independent second review, prior IC suite rerun, or local full-archive verification occurred. GitHub preservation checks are separate and must be reported from actual status after publication. Files under raw/, existing investigations, and the original repository are unchanged.

ASRP: scope drift detected; identified the unsupported jump from a detector diagnostic to a core validation priority; preserved that work and returned to source-native relationships. Separate equilibrium matching from global dynamics, and fixed-parameter variation from evolving coupled state. Do not trade one narrow rabbit hole for a long catalog with no closed candidate.

**Next concrete deliverable:** a versioned state/normalization specification and the closure relationships required to connect XXV's spatial, variational and kinetic sectors, traced back to the foundational kernel papers. No additional NIST fitting is the default next step.
