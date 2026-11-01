# IC-13 — Verified NIST receipt and a missing-channel audit

Date: 2026-11-01. Parent: `ed7252ee5efe00c37f9967f5c455b3bb08996260`.
Status: acquisition resolved; numeric-schema exception recorded; analysis calibration still incomplete. This is an actual-file intake checkpoint, not a new physics result.

## What arrived and what was independently checked

The owner supplied the five NIST mds2-3859 distributions, an acquisition manifest, and acquisition notes. All five distribution sizes and SHA-256 hashes were recomputed and match the supplied acquisition manifest. Every one of the 33 ZIP-member hashes, sizes, row counts and interpreted headers also matches. All three ZIP CRC checks pass. No ZIP contents were extracted or executed; source bytes were not edited. These are receipt/integrity comparisons against another acquisition record, not a publisher-certified checksum or proof of scientific validity.

The package contains 15 BL2 series with 2,157,334 listed event records; 14 BL2 simulation files; four BL1 data/simulation files; and 1,600 RGA rows. The BL2 total has **2,156,273 complete finite energy-time pairs**. The difference is a newly identified missing-energy issue described below. The acquisition manifest's structural row count was correct; it did not assert complete numeric contents in every field.

See [validation summary](validation-summary.json), [run catalog](run-catalog.csv), [audit code](audit_received.py), [parser tests](test_audit.py), and [updated analysis contract](analysis-contract.json). The full 48,770-byte audit, original acquisition sidecars, source README, and execution log are in the downloadable IC-13 packet. The full audit hash is recorded in the summary and it can be regenerated from the unchanged uploads. Large experimental ZIPs and the RGA numerical series are not copied into Git.

## Actual data-quality finding: Series 527

`BL2data.zip/Series_527.txt` has 22,717 records. The first 21,656 contain both numeric columns. The final **1,061 records have an empty energy field but a finite time field**. These are source-file lines **21,664–22,724 inclusive** (1-based, including headers).

The first affected literal record is `,5.3`; the last is `,-1.1`. There is no basis in the uploaded documentation for deciding whether this reflects an acquisition condition, export choice, or another cause. The ZIP and member hashes match, so this is not a mismatch introduced by the handoff. Physical row order is not demonstrated to be acquisition chronology.

No energy was replaced with zero, interpolated, inferred from time, or silently discarded. The default complete-pair gate refuses this series for a joint energy-time model. The known times may be useful for an all-trigger timing analysis, but energy-selected timing requires an explicit missingness/selection policy. Missing at random is not assumed. A model could eventually marginalize the missing channel under justified assumptions; that is not implemented here. Other series are not blocked by this particular exception, but calibration remains necessary.

## Further distinctions established from the actual files

- BL2 measured energy is in **arbitrary units**. SRIM simulation energy is in **keV**. No undocumented scale conversion is applied.
- Series 911 begins with a UTF-8 byte-order mark. The parser recognizes it for header interpretation; the original bytes and hash remain intact. Its displayed header in the acquisition manifest omits that marker.
- BL1 series 125 is an energy-time event list with energy labeled keV. BL1 series 134 is a time-histogram file. Its 1,024 values in the counts column are fractional, and 454 are negative. The documentation available here does not provide the processing covariance; these cannot be treated as raw nonnegative integer Poisson counts or rounded into them. This is not an accusation of invalid measurements or evidence that a particular processing step occurred.
- The RGA file contains signed ion-current readings: 14 negative January entries and 626 negative March entries. They are preserved, not converted to zero, pressure, or ARK epsilon. There is no newly established run-specific trap-local gas mapping.
- Measured ramp voltages in the five-run comparison are 0, 7.2, 14.4, 28.8, and 45 V. The simulation comparison labels 0, 6.2, 13.4, 27.8, and 44 V and specifies 3% H2+ contamination. Pairing nearby settings is not proof of independent voltage calibration; the simulation mixture is not an inferred observed fraction.
- Headers identify trap durations, not live time, number of cycles or neutron exposure. The README calls the package a representative sample for its charge-exchange publication, not a complete lifetime measurement.
- The README's working title and its BL1 simulation filename typo remain unchanged. The actual member is `BL1_Series134_simulation.txt`.

## Metadata-defined comparison map, not yet a frozen fit

The five ramp-control series are 539, 538, 527, 531 and 537 (ordered by stated ramp voltage). All state SB detector, 25 kV acceleration and 10 ms trap duration. This matching of header fields does not establish identical gas conditions, gain, effective threshold, exposure or other upstream controls. Series 527 requires the missing-channel decision above.

Series 963, 911/923/954/974, 970, 978/1030 and 1058 describe 3, 20, 30, 50 and 100 ms trap durations at the stated 45 V ramp and 25 kV acceleration. Series 537 provides the nominal 10 ms setting. Equal nominal settings across different series are not automatically replicates under identical conditions. Series 1137 uses PIPS at 30 kV rather than SB at 25 kV.

This information supports a prospective metadata review and retrospective transfer design. It does not support reading row-count ratios as decay-rate ratios or survival probabilities. Numerical schema validation read every row; no spectrum, event-cut optimization, peak alignment, model fit, or held-out physics outcome was calculated in this session. Previously read article trends are already known, so future evaluation is not wholly blind.

## Verification history

An initial exploratory numpy.loadtxt call failed on the blank energy in Series 527. A second strict decoded-header comparison stopped at the Series 911 byte-order mark. These failures led to explicit missing-channel reporting and BOM-aware interpretation, not alteration of data. The final standard-library audit covers all files and records both issues.

Thirteen parser/safety unit tests pass: documented units, missing values, actual zeros, BOM/hash preservation, fractional histograms, signed RGA values, nonfinite/nonnumeric rejection, wrong widths, blank-line handling, unsafe paths, symlinks, line ranges and absent schema. They test software behavior, not an experimental mechanism. The full actual-file audit separately matches five distributions and 33 members. The tests do not prove absence of experimental systematics. No earlier IC test suite was rerun, no local whole-archive verifier ran, and no independent reviewer assessed this checkpoint. GitHub preservation CI and remote publication hashes are checked separately.

## Source and decision boundary

The primary source actually read in this session is the supplied NIST README, generated 2025-05-30, DOI `10.18434/mds2-3859`, plus the uploaded original bytes, headers and acquisition records. Acquisition records report official NIST URLs and final NIST cache endpoints, but this session did not independently repeat those remote downloads. No additional scientific publication or external website was consulted for this intake. Repo reads: current PR, IC-12 contract and handoff, entry protocol, AGENTS, POLICIES and charter v1.1 sections 4–6.7. Prior source/PDF reviews are not claimed as rerun.

ASRP: missing is not zero; a hash match is not numeric completeness; a time column is not necessarily a decay time; simulation output is not measured response; a histogram label does not establish raw-count likelihood; trap timing is not exposure; calibration is allowed but must not be hidden in outcome matching.

**Next task:** use the publication's methods and available calibration evidence to define the first apparatus-response comparison. Complete the energy/time mappings, threshold and background treatment, missing-channel policy and full-run calibration/evaluation assignments before fitting. Begin with a documented response-shape test; absolute lifetime and additional ARK coupling remain separate, currently underdetermined targets. No new request to reacquire these five files is necessary.
