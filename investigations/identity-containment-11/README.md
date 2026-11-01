# IC-11 — Published detector-response benchmark and the contrast test

Date: 2026-11-01. Parent commit: `9656f14ff1632cfae28252c4e259fad01d039798`. Draft research on the existing PR #2 branch; no merge, historical-archive change or new physical scalar identification.

**Status:** published simulation-response inputs plus executed conditional-inference tests. **The intended event-data validation remains incomplete:** the NIST event-data release was located, but its files could not be retrieved in this session. No measured event series, neutron lifetime, or ARK environmental coupling was fitted. Four small source-table consistency flags remain open. Passing computational checks does not remove those flags or validate the response simulation.

## 1. Evidence boundary

IC-10 supplied a two-species observation model and called for a real apparatus dataset. The NIST release `mds2-3859` contains BL1/BL2 events, simulations and residual-gas records. Its catalog and the authors' paper were accessible; the release's README and ZIP downloads were not. Direct container HTTP failed DNS resolution, download-tool requests failed, and web retrieval of the data links failed after redirecting to the NIST S3 cache. The PDF copies exceeded the web retrieval size limit. The paper's arXiv v2 HTML was read instead; no PDF/image transcription or graph digitization is claimed.

The useful fallback is not fabricated measurements. [published_response.csv](published_response.csv) transcribes the 30 matched settings in Tables 2 and 3 of J. Caylor et al., *Detection of Molecular Hydrogen in a Neutron Beam Lifetime Experiment*, arXiv:2506.01682v2 (12 December 2025), published in Phys. Rev. C **112**, 065501, DOI `10.1103/nr3b-3dtl`. Those tables contain **SRIM-plus-Monte-Carlo response estimates**, not 30 measured lifetimes or empirical efficiencies independently re-estimated here. [bl1_response.csv](bl1_response.csv) transcribes the 13 historical series and their source-specific response estimates from Table 4. The paper's observed timing/spectral trends provide context; we did not refit them or reproduce its apparatus simulation.

The two tabulations must not be pooled indiscriminately. Tables 2/3 use a 6.0 keV detection threshold. Table 4 uses actual BL1 settings with thresholds from 8.43 to 11.93 keV. Matching the molecular row requires doubling its listed half-proton energy to obtain the detector acceleration voltage. Zero gold areal density denotes the paper's PIPS case, not an ideal deadlayer-free detector.

Full URLs, access limitations, transcription decisions, source provenance, and unresolved flags are in the [source card](../../sources/identity-containment-11-published-response.md). Numerical tables and our calculations are included; the full article and inaccessible event archives are not republished.

## 2. Declared observation model and signed bias

Assume a constant beta rate `Gamma`, known neutron exposure `X` in neutron-seconds, one retained charged product per decay, trapped molecular-ion fraction `f`, and effective detector efficiencies `eta_p,d` and `eta_h,d`. Background, acceptance, dead time, return/backscatter treatment and multiple-ion events must either be included in those independently characterized response terms or explicitly modeled separately. Let `y_d` be the expected, background-corrected count divided by X:

$$y_d=\Gamma[(1-f)\eta_{p,d}+f\eta_{h,d}].$$

This is a mixture model for the recording channel, not a theory of the neutron's microscopic rate. Its use of the published table estimates is conditional; the table numbers do not prove that all real collection effects are captured. In particular, we do not reproduce BL1's backscatter extrapolation.

Define the calibrated detector contrast and proton-corrected yield:

$$k_d=\frac{\eta_{h,d}}{\eta_{p,d}}-1,\qquad z_d=\frac{y_d}{\eta_{p,d}}=\Gamma(1+fk_d).$$

A proton-only lifetime interpretation would give

$$\frac{\widehat\tau_d}{\tau}-1=\frac{1}{1+fk_d}-1.$$

The bias can have either sign: a replacement ion may be detected more or less efficiently than the proton it replaces. A physically present perturbation is not automatically a missed count or longer apparent lifetime.

### Benchmark with imposed f = 0.05

| Gold areal density, microgram/cm2 | Acceleration, kV | Published proton efficiency | Published molecular-ion efficiency | Calculated relative lifetime bias |
|---|---:|---:|---:|---:|
| 0 (PIPS) | 25 | 99.5% | 98.1% | +0.0704% |
| 20 | 25 | 99.2% | 99.9% | -0.0353% |
| 40 | 25 | 98.0% | 99.2% | -0.0612% |
| 60 | 25 | 96.3% | 96.3% | 0 at printed precision |
| 80 | 25 | 93.8% | 87.6% | +0.3316% |
| 100 | 25 | 90.5% | 68.0% | +1.2587% |
| 100 | 35 | 95.9% | 94.9% | +0.0522% |

These are **hypothetical fixed-composition comparisons using published simulation estimates**. The paper reports admixtures up to about 5% in some BL2 diagnostic conditions, but no observation establishes the same f for every row. The 100-microgram cases are not among the 13 BL1 settings; the +1.26% example cannot be claimed as a correction to BL1 or an explanation of the lifetime discrepancy. No lifetime target was used to choose f or tune coefficients.

If a one-percent upward-bias effect is imposed merely as a design question, the thick detector requires f about 4% at 25 kV but about 95% at 35 kV. This large response contrast is a possible diagnostic, not evidence those fractions occur. Effects below the table's precision cannot be inferred accurately from its rounded values.

## 3. Trapped fraction and observed fraction are different

The fraction among detected events is

$$f_{\rm det}=\frac{f\eta_h}{(1-f)\eta_p+f\eta_h},\qquad
f=\frac{f_{\rm det}\eta_p}{\eta_h(1-f_{\rm det})+f_{\rm det}\eta_p}.$$

At 100 microgram/cm2 and 25 kV, an imposed trapped fraction of 5% becomes about 3.8042% among detected events. A published spectral-mixture parameter must be audited for its normalization before assigning it to either quantity; we have not assumed that the authors' fitted fractions are uncorrected detected fractions.

A missing or faint visual ion feature is not itself a zero-concentration measurement. The paper discusses exactly this issue for PIPS versus surface-barrier spectra. We do not infer a numerical composition from pictures.

## 4. Conditional separation of rate and composition

With fixed upstream conditions across two independently calibrated detector settings,

$$z_d=a+b k_d,\qquad a=\Gamma,\quad b=\Gamma f.$$

Therefore

$$\Gamma=\frac{k_2z_1-k_1z_2}{k_2-k_1},\qquad
f=\frac{z_2-z_1}{(k_2-k_1)\Gamma}.$$

The determinant is `k2-k1`. Two settings can separate the two unknowns only if the response ratios differ. Two readings for two unknowns have no residual degree of freedom: reconstruction alone is not validation. A third setting supplies a consistency test of the frozen line, while a separately characterized beta channel or neutron inventory can test additional assumptions.

Absolute exposure remains necessary for an absolute Gamma. An unknown common normalization rescales Gamma but leaves f unchanged. Unknown relative gains can change both. Altering acceleration voltage is not automatically a nonperturbing downstream intervention: field penetration, acceptance, ion transport and upstream state changes must be checked. Exchanging whole detectors across reactor cycles certainly does not guarantee unchanged gas composition. The hypothetical reversible same-detector scan is a design proposal, not a claim that the published runs meet these invariances.

### Executed design example, not measured data

Using the 100-microgram detector's 25 and 35 kV coefficients, injected values `Gamma=0.001 s^-1`, `f=0.04` are reconstructed exactly. Their frozen result predicts the independently evaluated **generated** yield at 30 kV. A deliberately introduced one-percent midpoint recording change produces a one-percent mismatch. No real holdout or blind result is claimed.

For the endpoint pair the contrasts differ by about 0.23819, and the dimensionless linear design has condition number 8.54. The 20-microgram pair has contrast separation only 0.0030404 and condition number 657.83. In the declared synthetic noise model, two independent 0.1% relative yield errors give a fraction standard deviation about 0.00588 for the first pair but 0.46535 for the second. Full algebraic rank does not ensure a useful measurement.

With 40000 Gaussian replicas (seed 1101), the first pair's simulated and delta-method standard deviations agree within 0.6%; nominal 95% coverages are approximately 0.9495 and 0.9511. These errors are invented design assumptions, not the experiment's uncertainties. The difference in fractional sensitivity between designs is approximately 79-fold. Common gain preserves f; opposite 0.1% gain errors shift the reconstructed f from 0.04 to about 0.03168. No clipping hides noisy unphysical estimates.

## 5. Actual acquisition thresholds prevent naive transfer

The standard 6-keV table gives, at 60 microgram/cm2 and 27.5 kV, efficiencies of 97.0% and 97.8%. BL1 series 149, with threshold 10.66 keV, has source-specific values of 96.7% and 85.3%. For the same **imposed** one-percent trapped fraction, the proton-only bias changes from about -0.00825% to +0.11803%.

This is a source-table transfer failure if one uses only detector material and voltage to select a response. It is not a controlled experimental isolation of threshold's causal contribution; additional series-specific detector characterization can contribute. We did not rerun SRIM to separate those changes.

All 13 Table-4 entries and their reported difference column are preserved. Individual-series hypothetical biases are not averaged into a lifetime correction. The event weights, covariance, collection corrections and original extrapolation are not available in the downloaded working files. The authors' analysis found no evidence for molecular ions in BL1 above its approximate one-percent detection limitation and reported a worst-case correction around -0.3 s, below 0.5 s. We have not independently reproduced that result; our diagnostic benchmarks do not override it.

## 6. Source precision is part of the result

An exploratory audit initially failed when requiring every tabulated efficiency to equal one minus its listed losses within ordinary nearest-rounding intervals. Four molecular-response entries remain inconsistent under that audit:

| Gold, microgram/cm2 | Acceleration, kV | Recomputed from printed losses | Printed efficiency |
|---|---:|---:|---:|
| 0 | 30.0 | 99.844% | 99.9% |
| 0 | 32.5 | 99.947% | 100.0% |
| 100 | 27.5 | 81.446% | 81.5% |
| 100 | 32.5 | 92.547% | 92.6% |

Loss terms are printed to 0.001 percentage points and efficiencies to 0.1 percentage points. The diagnostic allows +/-0.0005 for each loss and +/-0.05 for efficiency, clipped at physical bounds. The four intervals do not overlap. This finding is scoped to the accessible HTML and the declared rounding assumption. It is not adjudicated as an error in the original experiment; PDF/source verification and unrounded simulation output are still needed. Possible formatting or nonstandard rounding must not be silently excluded.

We preserve every number and keep two calculation branches: printed efficiencies are primary; component-derived efficiencies are a sensitivity analysis, not an authoritative repair. The main 25/35 kV endpoint and 30-kV comparison at 100 microgram/cm2 avoid those flagged rows. The flag status is explicit in `test-results.json` even when computational checks pass.

For the main synthetic endpoint data, perturbing the four printed efficiencies by their rounding halfwidths at all 16 vertices gives reconstructed f ranging about 0.03551–0.04449. This is only a rounding-vertex sensitivity, not a total systematic uncertainty or a proven global bound. Using component-derived endpoint efficiencies yields f about 0.04040. No uncertainty covariance for the underlying response simulation is supplied by this extraction. High-precision inference is not justified by the table's extra apparent digits or by our code's arithmetic precision.

## 7. Remaining alternatives and the connection to ARK

The observation line can distinguish a composition-dependent recording effect from a common physical-rate factor **only within its input contract**. A common missed fraction rescales the intercept and is indistinguishable from a changed rate using these channels alone. Unconstrained detector-setting-dependent changes in the upstream rate can exactly reproduce a different inferred composition, even with many settings. Neither a good line fit nor a residual uniquely identifies epsilon.

IC-10's uniform-production reaction model supplies the optional link

$$f(T)=1-\frac{1-e^{-rT}}{rT}.$$

The implementation checks this against an independent two-species ODE and inverts it for synthetic r=8 per second. Recovering r from f is inverse inference, not an independently measured gas density or ARK perturbation. Real proton energy and residence-time distributions, spatial gas variation, and secondary species need their own characterized model.

The framework's proposed decomposition `Delta S_t + epsilon_created` remains a claim about independently specified physical influence. This detector study supplies no constitutive mapping from pressure or gas composition to that quantity. It provides a way to avoid confusing observed-event selection with an identity-transition response while building such a mapping. The conceptual basis is the source-qualified neutron/charter treatment already audited in [IC-10](../identity-containment-10/README.md), not a new derivation from the archived neutron equation.

## Verification and next gate

Run `OPENBLAS_NUM_THREADS=1 python check_ic11.py --output test-results.json`. **14/14 final check groups pass**, including explicit detection of the four unresolved input flags. The earlier exploratory all-rows consistency assertion failed as described above; no source number was changed to make it pass. The first named suite had 12 groups and passed; two additional Table-4 checks were then added and the full suite rerun. Initial outputs and the discovery note are retained in the downloadable packet. No independent second reviewer.

The unchanged IC-10 script from the mounted packet was matched to Git blob `e778bb09eca94b53f23ff52d493409234b8c52db` and rerun: 15/15 checks pass. Its fresh report is included in the download, not substituted for the old result. IC-01–09 were not rerun. No local full-archive validation or PDF audit is claimed; repository preservation CI and publication hashes are reported separately.

ASRP: distinguish inaccessible data from nonexistent data; simulation estimates from observations; incident from detected mixtures; half-energy from full acceleration; ordinary rounding from source uncertainty; mathematical rank from precision; response transfer from blind validation; downstream control from assumed absence of upstream back-action. No automated job, experiment or independent Ada review was initiated.

**Next gate remains unmet:** obtain and hash the event archives and README, verify series/threshold/exposure normalization, and reproduce one source response using the unrounded apparatus simulation and independent control records. Freeze a calibration subset and test a different control setting. Only after that add a physically specified ARK rate coupling and compare a distinct observation. The result here is a bounded apparatus-specific benchmark and a discrimination design, not completion of the real-data validation.
