# Session handoff — IC-11, 2026-11-01

Parent: 9656f14ff1632cfae28252c4e259fad01d039798. Owner authorized continuation, not merging. Research branch only; no historical archive, manifest, policies, safeguards or source-repository edits.

Study: [Published detector-response benchmark and contrast test](../investigations/identity-containment-11/README.md). [Source access](../sources/identity-containment-11-published-response.md). Code, two CSV transcriptions and actual output are in the study directory.

The intended empirical validation was attempted but not completed. Located NIST mds2-3859 public event/simulation release; README/ZIP downloads failed in web, specialized download and direct container routes. PDF retrieval exceeded tool size limits. Native arXiv v2 HTML was accessible. No experimental event file was read or fitted. This limitation must lead the handoff, not be concealed by describing simulation tables as measurements.

Useful completed work: source-specific response benchmark using 30 paired Table-2/3 settings and 13 Table-4 historical series; signed proton-only bias; incident/detected fraction distinction; two-response rate/composition inversion and third-setting consistency target; practical conditioning; synthetic covariance; table-rounding sensitivity; exact common-loss/back-action alternatives; and explicit threshold-specific transfer failure. No epsilon, physical rate-law or microscopic ARK mapping is established.

Four Table-3 cells do not close under nearest-rounding bounds using the printed loss terms. Retained both inputs, flagged discrepancies, and avoided those rows in the main endpoint/midpoint design. Needs PDF/source and unrounded simulation check. Also, Tables 2/3 use 6 keV threshold, unlike actual BL1 thresholds. Do not transfer response coefficients using only material/voltage or average individual biases into a published lifetime correction.

Final local suite: 14/14 named groups pass, including detection of the four unresolved input flags. An initial exploratory source-consistency assertion failed; discovery note is retained. First named 12-group suite passed, then two Table-4 tests were added and all 14 rerun. Unchanged IC-10 code matched Git blob e778bb09eca94b53f23ff52d493409234b8c52db and reran 15/15. Earlier IC studies not rerun. Actual initial/current outputs and previous-script rerun are in download. No independent reviewer, empirical fit or local whole-archive audit. GitHub preservation CI and content-hash verification must be checked separately after committing.

Next gate still open: retrieve source event files/README, resolve metadata and response precision, freeze calibration/control partitions, reproduce an observed response and only then test a specified additional physical coupling. More toy examples cannot substitute for that test. A changed response correlated with readout settings is not uniquely a changed neutron transition rate. No automatic job or Ada delegation was initiated.
