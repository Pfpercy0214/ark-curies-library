# IC-10 — Apparatus-aware inference: decay, transport, and detection

Date: 2026-11-01. Parent commit: `e533bd2e85e90fce33f8ebb441bf218ca86f19ca`. Draft research only; no archive changes or merge. Status: conditional derivations and executed synthetic verification, with primary-source constraints. **Not a neutron lifetime prediction, empirical fit, or physical identification of epsilon.** No independent reviewer.

## 1. Question and source contract

The [owner's clarification](../../history/mechanistic-notes/2026-11-01-apparatus-perturbations.md) is that preparation, containment and active measurement are physical interventions. IC-09 separately established, in a conventional comparator, that transport through a configuration need not destroy that configuration. The next question is which recorded signals distinguish an identity transition from departure from the observed region or altered product detection.

[Paper XXV](../../raw/papers/paper-025-disciplined-containment-conv-01.md), Appendix B.2–B.6, specifies `E = Delta S_t + epsilon_created`, a conditional survival rule `dQ_n/dt = -Gamma(Delta Pi) Q_n`, and a first-order response sensitivity. It also states that apparatus-to-perturbation and sensitivity mappings remain qualitative/parametric. Its beam/bottle ordering and infinite-lifetime limiting discussion are hypotheses, not inputs to this calculation. The historical text remains unchanged.

The [charter](../../raw/epistemics/ARK_Epistemic_Charter_v1.1.md), sections 4–6.9, permits measured-input reconstruction and calibrated transfer while requiring independent source, coupling, units and scope for epsilon. An unmeasured perturbation is neither zero nor an unrestricted explanation. This study adds an observation layer to B.3; it does **not** supply the microscopic rate functional or reconcile the ARK field variables with a measured neutron state.

All rates below use the same declared time coordinate, in inverse seconds. This is not a gravitational clock derivation. `Gamma_beta` means a beta-marked transition rate, not every conceivable disappearance channel. The comparison assumes the ordinary beta channel is the identity transition being investigated; any additional transition channel must be represented separately.

## 2. Forward observation, before inverse attribution

For a homogeneous stored population with no influx,

$$\dot N=-(\Gamma_\beta+\Gamma_\ell+\Gamma_u)N.$$

`ell` is non-beta removal from the population; `u` is an additional unobserved removal channel. Detector means may be

$$\mu_S=\eta_S N(T)+B_S,\qquad
\mu_\beta=\int_0^T\eta_\beta(t)\Gamma_\beta(t)N(t)dt+B_\beta.$$

A loss-mark channel has the analogous integral with `Gamma_ell`. Backgrounds, cross-talk, dead time, geometry/energy-dependent acceptance and changed phase-space distributions require their own calibrated response functions. If a physical boundary moves, removal flux is relative to that boundary, as in IC-09. A beam requires an exposure/decay-product model, not this storage equation reused by name.

Preparation and monitoring can affect rates as well as efficiencies. A proposed monitor is not presumed nonperturbing. The displayed equations describe a declared measurement configuration; additional back-action requires a coupled response model. The scalar reduction is justified only for its homogeneous, approximately constant-rate regime; otherwise resolve energy, trajectory, time or other relevant state dependence.

### Exact ambiguity in a survival-only record

With constant rates, survival identifies `lambda = Gamma_beta + Gamma_ell` (plus any extra channel), not its decomposition. For example `(0.001, 0.00008)` and `(0.00104, 0.00004)` per second give identical survival curves. These are deliberately synthetic, not measured neutron values.

Changing efficiency can mimic an additional rate. After correct background subtraction and matched initial normalization,

$$\widehat\lambda=-\frac{\ln[y(t_2)/y(t_1)]}{t_2-t_1}
=\lambda-\frac{\ln[\eta(t_2)/\eta(t_1)]}{t_2-t_1}.$$

A constant common efficiency cancels; a storage-time-dependent relative efficiency need not. As an **effect-size illustration only**, the historical round numbers 878 and 888 s differ in rate by `1.2826037883e-5 s^-1`. An unaccounted efficiency ratio of `0.9872558652` across 1000 s could produce that same added logarithmic slope. No evidence is supplied that an actual instrument has this error; published corrections must be respected.

## 3. Constructive recovery from separately characterized channels

Assume constant nonnegative beta/removal hazards over a common interval T; no influx; disjoint and exhaustive removal marks; calibrated effective efficiencies; and adequate background accounting. Let corrected *expected* counts be `s = mu_S/eta_S`, `b = mu_beta/eta_beta`, `l = mu_ell/eta_ell`. Then

$$s=N_0e^{-\lambda T},\qquad b=N_0\frac{\Gamma_\beta}{\lambda}(1-e^{-\lambda T}),\qquad
l=N_0\frac{\Gamma_\ell}{\lambda}(1-e^{-\lambda T}).$$

Therefore

$$\boxed{\lambda=\frac1T\ln\!\left(1+\frac{b+l}{s}\right),\quad
\Gamma_\beta=\lambda\frac b{b+l},\quad
\Gamma_\ell=\lambda\frac l{b+l}.}$$

An unknown common count/efficiency scale cancels; unknown relative efficiencies do not. The observation map has full local rank for initial population and the two rates in the tested positive regime. This is a conventional competing-risks inversion with explicit assumptions, not a newly discovered decay law. Nonlinear estimators from finite counts have sampling bias; the identities above apply to expectation values. At low counts, fit the joint likelihood rather than clipping negative background-corrected counts.

For synthetic `N0=200000`, `T=700 s`, rates `(0.001,0.00008) s^-1`, efficiencies `(0.9,0.65,0.7)`, observed means are `(84517.3510,63851.5657,5501.0580)`. The inversion recovers the supplied rates, so the beta timescale is 1000 s while uncorrected storage removal has timescale 925.9259 s. Returning known simulation inputs is implementation verification, not physical validation.

The channel requirement is a measurement-design target, **not an assertion that existing neutron instruments provide all three simultaneous channels**. Separate runs can be combined only with justified matching/normalization. Counting a removal mechanism may change it. Inventory completeness needs independent testing rather than being established by this inversion's own reconstruction of N0.

### Counterexamples that remain visible

With an additional unmonitored rate `0.00005 s^-1`, the same observed three means can be reproduced exactly by a wrong two-channel model with a different initial population. It gives approximately `(0.0010139107,0.0000811129) s^-1`. An independently anchored initial inventory exposes a deficit of about 4837.25 events for the chosen example. This deficit does not identify which missing mechanism caused it.

A population composed of different fixed-rate subpopulations also develops a changing aggregate hazard. For `S(t)=sum_i w_i exp(-lambda_i t)`,

$$\frac{d}{dt}[-\partial_t\ln S]=-\operatorname{Var}_{w(t)}(\lambda_i)\le0.$$

A changing fitted lifetime can therefore reflect population selection without any constituent rate changing. No conclusion about actual neutron data is drawn from that counterexample.

## 4. Uncertainty and calibration are part of the inference

Fixed-N0 survivor, beta, loss and missed counts were generated as multinomial outcomes, not falsely treated as independent Poisson counts. With 30000 replicas (seed 1001), the linearized count covariance agrees with the simulation: beta/removal standard deviations are approximately `3.7574e-6` and `1.0762e-6 s^-1`, with 95% interval coverage approximately 0.9498 and 0.9507. These are generated-data checks of one estimator and regime, not experimental confidence intervals.

A 0.3% independent relative uncertainty in the beta-channel efficiency contributes about `2.1713e-6 s^-1` additional beta-rate uncertainty in this example. A purely common multiplicative efficiency uncertainty cancels in the displayed inversion. Correlations must be propagated according to the actual calibration, not assumed away.

The forward endpoint solution was independently checked by ODE integration with tightened tolerances. No experimental calibration parameters were estimated. All synthetic model choices were visible during development; this is not a blind holdout.

## 5. A concrete apparatus mechanism after the decay

NIST's proton-counting beam method measures a yield proportional to beta rate, neutron exposure and proton collection efficiency [S1]. Interactions of already-created protons belong in the product-response model before being attributed to the neutron's evolution.

Consider a deliberately simplified model: protons are created at constant rate R over a trap cycle of duration T; they undergo charge exchange at independently supplied rate `r = n_gas <sigma v>`; each conversion leaves one trapped molecular ion; there are no secondary losses; final proton and molecular-ion detection efficiencies are `eta_p` and `eta_h`. Then

$$\dot P=R-rP,\qquad \dot M=rP,$$

$$\boxed{\eta_{\rm eff}(T)=\eta_h+(\eta_p-\eta_h)\frac{1-e^{-rT}}{rT}.}$$

The age average matters: newly created protons have not all spent the full cycle in the trap. Replacing the factor with `exp(-rT)` incorrectly treats their residence times as identical. We verified the expression with an independent two-species ODE and direct age integration. Equal efficiencies remove the total-yield effect even when conversions occur.

Illustrative values `r=20 s^-1`, `eta_p=0.9`, `eta_h=0.55` give effective efficiencies 0.89309, 0.86722 and 0.77124 for 2, 10 and 50 ms. Using a proton-only efficiency would overestimate the lifetime by factors about 1.00773, 1.03780 and 1.16695 although beta production was held constant. **These are not NIST parameter estimates or an explanation of the observed discrepancy.** Actual spectra, trajectory/energy distributions, other species, ion loss and detector response require the full apparatus model.

A useful control varies a genuinely downstream response after the decay while checking that upstream fields and neutron exposure are unchanged. An intervention on the neutron-containing region can then be tested separately. Causal separation must be independently demonstrated; physical proximity alone does not establish it.

## 6. What can be calibrated and tested without answer-forcing

XXV's first-order hypothesis motivates a local response form, but not its numerical coefficient:

$$\Gamma_\beta(x)=\Gamma_0+b x,$$

where x is an independently characterized apparatus control in a declared normalization. The code uses two synthetic reference controls to calibrate the two coefficients, freezes them, and predicts a third beta rate and product count while independently changing detection efficiency. It recovers the intended response only when that detection change is modeled. This checks a calibrated-transfer procedure, not the hypothesis's truth or the physical identity of x with epsilon.

If `epsilon=alpha*x` and `b=chi*alpha`, rates alone identify b, not alpha and susceptibility chi separately. Multiplying alpha by a common factor and dividing chi by it leaves the rates unchanged. The physical perturbation needs a separate operational definition; a measured pressure is not automatically the paper's causal imbalance.

Likewise a zero-pressure extrapolation of total removal is not automatically the ambient beta rate. With `Gamma_ell=ell0+c*p` and `Gamma_beta=Gamma0+b*p`, its intercept is `Gamma0+ell0` and slope `b+c`. A scan alone cannot assign the slope to identity response. Reducing deliberately created perturbations also does not establish vanishing ambient Delta S_t or infinite neutron lifetime.

For future work: characterize sources and detector responses from independent channels; record a conventional null with equivalent input access; calibrate declared sensitivities on designated references; freeze maps, units and rate-law choices; predict new controls and preferably more than one channel; propagate both calibration covariance and bounded unobserved losses. Unbounded missing influences remain unresolved, not a freely adjustable error bar. Multiple mechanisms can fit a residual; only independent discrimination can identify one.

## 7. Empirical constraints and source access

Accessed 2026-11-01. These records constrain the design; no event datasets were downloaded or fitted.

**S1 — NIST/BL2 charge exchange.** J. Caylor et al., Phys. Rev. C 112 (2025), DOI `10.1103/nr3b-3dtl`; [publication record](https://www.nist.gov/publications/detection-molecular-hydrogen-neutron-beam-lifetime-experiment), [arXiv v2 HTML](https://arxiv.org/html/2506.01682v2). Read abstract, sections I–III.2, IV.2 and VI–VII, including the exposure-efficiency relation and apparatus controls; did not inspect figures, full numerical simulation or underlying data. The study observes charge exchange under selected conditions, but concludes its impact on the earlier BL1 lifetime is unlikely to be significant (a worst-case estimate below 0.5 s). A demonstrated mechanism need not explain the anomaly. The simplified ODE above is our comparator, not a replacement for their analysis. Use the version identifier/publication date; the HTML also displays a later render-date string, not a new result.

**S2 — UCNtau systematic controls.** R. Musedinovic et al., Phys. Rev. C 111, 045501 (April 2025), DOI `10.1103/PhysRevC.111.045501`; [ORNL publication record](https://www.ornl.gov/publications/measurement-of-the-free-neutron-lifetime-in-a-magneto-gravitational-trap-with-in-situ-detection/). Read published abstract: residual-gas correction and four detector geometries are explicitly addressed. Do not claim apparatus effects were ignored. arXiv abstract `2409.05560` was also read; v1/v2 HTML retrieval failed. The published abstract's 877.83 s combined central value differs slightly from the earlier preprint abstract's 877.82 s; no averaging or numerical fitting used either value.

**S3 — J-PARC electron-counting beam.** Y. Fuwa et al., [arXiv:2412.19519v1](https://arxiv.org/html/2412.19519v1), posted 27 December 2024; [author's 2025 conference abstract](https://indico.ibs.re.kr/event/701/contributions/6588/). The read abstract reports `877.2 +/- 1.7(stat) +4.0/-3.6(sys) s`, compatible with bottle results, using electrons and a helium-capture normalization rather than trapped-proton counting. Therefore the archived two-band shorthand is not a universal classification of every beam instrument. This constrains a proposed apparatus-specific mechanism without selecting one. No figures, table-level subrun data or full systematic likelihood were analyzed.

Repository reads: current AGENTS, entry protocol and POLICIES; charter sections 4–6.9; XXV A.5–A.7 and B.1–B.8 plus an earlier retrieved gravity passage not used here; latest IC-09 handoff and exact previous code; investigation index. Charter blob `ae341b2a7e30fc1d25703a1f6dbc032595fec707`; XXV blob `3bbf2a40a7c4bdde67f4bbeb2a29147f10a036f5`. Personal-context retrieval informed the owner's intent but is not treated as a primary scientific source. No complete historical reread, source-PDF audit or full local archive verification is claimed.

## Verification record and next gate

Run `OPENBLAS_NUM_THREADS=1 python check_ic10.py --output test-results.json`. Fifteen groups passed on the first recorded run: partition invariance; survival ambiguity; efficiency drift; constructive inversion; rank/relative-efficiency limits; ODE refinement; multinomial covariance; hidden channel; selection; calibrated transfer; extrapolation; epsilon-scale ambiguity; product-trap response; causal-order control; invalid inputs. See [code](check_ic10.py) and [actual results](test-results.json). Tests were designed with the model visible, and include positive and negative controls. Passing is not empirical support for ARK.

Unchanged IC-09 code from the mounted packet was verified against Git blob `58f53c340082d0d4b7d53f880783694cfdb50302` and rerun: 12/12 groups passed. Its code and new report are in the download, not substituted for the old repository results. IC-01–08 were not rerun. Preservation CI and publication-byte checks are separate and reported after publishing.

ASRP checks: separate transition, transport and recording; preserve legitimate calibrated inference; do not infer epsilon from a target residual; do not treat a background or total-pressure proxy as a measured local perturbation; do not generalize two method labels over conflicting apparatus-level evidence; retain covariance and incomplete-channel alternatives.

**Next gate:** choose one accessible apparatus dataset with independently characterized pressure/fields, product response and exposure. Validate the conventional observation model first. Only then add an explicit ARK-derived coupling and compare additional predictions with the same uncertainty and input access. A remaining discrepancy is a question to investigate, not evidence that epsilon has been measured.
