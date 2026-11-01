# IC-14 — First timing transfer and the coordinate-convention gate

Date: 2026-11-01. Parent commit: `5df5dcf8e26fe02cfa046977763a7a897e7ce931`.

**Status: real event data analyzed, but only conditionally. The original timing-coordinate assumption failed. An explicitly inferred replacement enables comparison, not calibration certification. The selected apparatus model is not validated.** No neutron lifetime, environmental epsilon, species fraction or additional ARK effect is inferred.

## 1. What changed from intake

IC-13 verified bytes and numeric completeness. This study compares measured arrival-time histograms with the released ramp-control templates. Energy remains in arbitrary units and is not used for selection or conversion. The analysis therefore does not need to impute the 1,061 missing energies in Series 527: their finite times remain in the timing marginal. This does not establish missing-at-random behavior or validate a joint energy-time analysis.

The uploaded README says time is in microseconds. The article III.3.1 defines event timing relative to trap opening, so that was the original declared convention. Before building measured spectra, we wrote [the primary contract](analysis-contract.json). It specifies acquisition groups, windows, normalization, a common timing shift, sensitivity checks and limitations. It is preserved unchanged.

The calibration failed before evaluating the designated tail outcomes: interpreting the stored numbers directly gave negative template normalizations for both calibration runs. Original early-window counts were 133 and 53, versus late-window counts 985 and 422, respectively. We did not relabel that failed attempt as a successful preregistration. The original failed script, traceback and freeze record are retained in the downloadable packet.

## 2. An actual coordinate inconsistency in the release

A new audit of all fifteen event members found two formats beneath the same time-unit label:

- Series **537, 538, 954, 978 and 1030** contain only integer time values spanning **0–2047**.
- The other ten span **−53.6–151.1**, on a 0.1-step numerical grid, with negative and fractional values.

These are findings about unchanged file contents, not an accusation that the experiment lacked a timing calibration. See [the coordinate audit](time-coordinate-audit.json) and [reproducible audit code](audit_time_coordinates.py).

Caylor's dissertation section 4.2 describes 2048 waveform time bins indexed 0–2047. That supports the bin-index interpretation but does not establish the export conversion for these individual released files. Matching the two observed coordinate grids suggests

$$t_{\mathrm{candidate}}=0.1\,t_{\mathrm{stored}}-53.6.$$

We applied it only to the five explicitly listed integer-coordinate series, leaving the other files unchanged. The coefficients come from grid endpoints, not a fit to a target peak or tail. **This is still an unconfirmed mapping hypothesis.** Original bytes were not rewritten. The [candidate addendum](candidate-coordinate-contract.json) was frozen before candidate calibration and evaluation. The primary protocol remains failed at its coordinate gate.

Prior exposure is explicit: published trends were known, the prior intake scanned all rows, and the failed script computed histograms before stopping. Broad distributions in the two calibration runs were inspected to diagnose the failure. The later grid audit read all time columns. No claim of full blinding is made.

## 3. A narrow, reproducible comparison

The released simulation file has 110 bins, with centers −5.7 to 59.7 microseconds. We integrate its piecewise-constant bins when shifting, without curve smoothing or interpolation chosen from the target. Its fixed mixture is 3% molecular ions. Its ramps are 0, 6.2, 13.4, 27.8 and 44 V; measured headers state 0, 7.2, 14.4, 28.8 and 45 V. The article describes a voltage offset selected to improve agreement. These are previously adjusted source templates, not independently predicted controls.

The declared working model is

$$\mu_{rj}=A_r S_{rj}(\delta)+B_r.$$

For every run, counts in **[0,8.4)** and **[30,60)** microseconds supply two constraints for its scale and additive pedestal adjustment. The latter may be negative because the released template already has a baseline; every predicted total count remains positive. It is not interpreted as a negative physical background.

Only the early-bin shapes of **538 and 537** calibrate the common shift, bounded to ±1.2 microseconds. Runs **527 and 531** supply the transfer comparison in **[8.4,30)**. Their own early/late totals ARE inputs, so this is conditional tail transfer, not a prediction of their entire datasets. Series 539 is a declared zero-ramp diagnostic. All finite times are used; no energy threshold or row-order-as-time assumption is introduced.

The fitted shared shift is **0.3101803 microseconds**. It is an observation-model alignment parameter, not a measured gravitational clock-rate change. Early-bin Poisson deviance on the calibration runs decreases from 13607.21 to 2215.60, but remains large. Even the calibration shape is not adequately explained at count-only precision.

## 4. Actual conditional tail comparison

| Evaluation series | Nominal measured ramp | Measured tail triggers | Control-normalized template | Relative total discrepancy |
|---|---:|---:|---:|---:|
| 527 | 14.4 V | 3057 | 3083.40 | −0.856% |
| 531 | 28.8 V | 2099 | 2015.83 | +4.126% |

A close integrated count is not a close shape. The 36-bin tail quadratic discrepancies, using count and normalization covariance with the shift fixed, are 60.94 and 135.84. These are descriptive diagnostics, not calibrated chi-square probabilities or discovery significances. Series 531 shows structured discrepancies around the later feature even while its total is within a few percent. Plots and all 550 observed/predicted bins are in the packet.

The predeclared sensitivity branches produce:

| Branch | Series 527 total discrepancy | Series 531 total discrepancy |
|---|---:|---:|
| No fitted shift | +5.555% | +12.915% |
| Late control window [40,60) | +0.594% | +4.091% |
| Coarsened 1.2-microsecond bins | −0.580% | +4.498% |

The sign for 527 depends on the baseline convention. Coarsening changes the fitted shift to approximately 0.29613 microseconds. We did not pick the best-looking variant as a new primary result.

A 200-repetition Poisson plug-in bootstrap, seed 1401, refits the common shift and control normalizations. The tail-residual standard deviations are about 62.14 and 50.54 counts. This estimates counting variation conditional on the observation model; it is not a null-model goodness-of-fit simulation. It omits template uncertainty, timing/energy calibration, selection effects, cycle correlations, and environmental drift. No total uncertainty interval or formal rejection probability is claimed.

Of Series 527's 1,061 time-present/missing-energy records, 897 fall in the plotted −6 to 60 range: 704 early, 147 in the evaluated tail, 40 late and six before zero. They remain included, with a separate timing table. No missing energy is interpreted as zero or used to select an event.

## 5. Interpretation boundary

The comparison has advanced beyond simulated examples: the observed counts are actual uploaded experimental records. It does not validate the selected response model. Unconfirmed timing conversion, all-trigger versus source selection differences, imperfect pedestal treatment, unknown template uncertainty and nonidentical upstream conditions remain possible explanations. A mismatch here is not evidence that the authors' full apparatus model fails, and certainly not a new physical neutron effect.

No absolute neutron exposure is supplied. These are arrival times of recorded products after trap opening, not individual neutron decay times. The common count normalization and normalized shape cannot establish a neutron lifetime. The ARK hypothesis has not supplied or been assigned an additional coupling in this calculation.

## 6. Reproduction and verification

With the original uploads and acquisition manifest in DATA:

```sh
python audit_time_coordinates.py --data-dir DATA --output coordinate-audit-new.json
OPENBLAS_NUM_THREADS=1 python analyze_timing_candidate.py --data-dir DATA --output-dir run-new --bootstrap 200
```

The scripts refuse to overwrite existing outputs. The candidate analyzer verifies original ZIP and selected member hashes and checks the template grid. Ten named software checks pass: shift identity, constant extension, affine recovery, exclusion of target tails from normalization, synthetic shift recovery, exclusion of evaluation groups from shift calibration, zero-count likelihood, coarse-bin integration, singular-design rejection and covariance derivatives. These tests check implementation, not empirical adequacy.

The full candidate analysis was rerun and produced identical substantive results excluding its timestamp. The standalone coordinate audit also reproduced the first audit. The unchanged IC-13 audit was matched to Git blob `b86e8eb00c75087221c73a8ff6a276da6ed232cd`, rerun on all inputs, and its 13 parser/safety tests passed. IC-01–12 were not rerun. No local complete-archive verification or independent second review was performed. Publication/CI checks are separate.

[The compact result record](validation-summary.json) preserves numerical summaries and SHA-256 fingerprints of the complete outputs. The download includes full results, comparison CSV, failed native-coordinate script/traceback, frozen contracts, source-check logs, previous-intake rerun, and two figures. An initial plotting attempt failed on a container-directory permission; after changing permissions the same plots rendered successfully. No scientific result was changed for that plotting fix.

## 7. Sources actually consulted and next decision

- Uploaded NIST README and acquisition records, DOI `10.18434/mds2-3859`; original event and template bytes. Receipt identity is against supplied hashes, not publisher authentication.
- Caylor et al., arXiv v2, https://arxiv.org/html/2506.01682v2 , sections III.3.1, IV.1 and IV.3. Read native methods text; no plot digitization. The mixture and voltage adjustments already use source observations.
- Caylor, 2022 dissertation, https://trace.tennessee.edu/utk_graddiss/7195 . Read searchable text of sections 4.2–4.4 through the official repository's PDF response. The requested screenshot failed at the retrieval-size limit (approximately 19.9 MB), and a direct download failed DNS resolution. No page-image, diagram or PDF-table verification is claimed. The description of indexed waveform bins does not independently certify the candidate export mapping.
- Repository: pinned entry protocol, AGENTS, POLICIES, charter v1.1 sections 4–6.3, IC-13 contract/handoff and source audit code. No new whole-corpus or historical-PDF review.

ASRP consequences: preserve the initial coordinate failure; do not optimize a conversion against the evaluated tail; retain missing-channel times without inventing energy; distinguish approximate integral agreement from shape validation; keep source-fitted templates distinct from a new independent prediction.

**Next gate:** establish the file-specific time export/calibration, then reproduce the source's documented selection and background treatment. A joint energy-time comparison requires an independent energy mapping and a declared missingness treatment. Do not repair these unresolved observation-model issues by adding epsilon. No email, automated job or Ada task was initiated, and no merge is authorized.
