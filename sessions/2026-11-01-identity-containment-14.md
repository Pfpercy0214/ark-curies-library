# Session handoff — IC-14, 2026-11-01

Parent: 5df5dcf8e26fe02cfa046977763a7a897e7ce931. Continued owner-authorized research, no merge. All new work is outside raw/; previous studies and source bytes are unchanged.

[IC-14](../investigations/identity-containment-14/README.md) records the first actual-event timing comparison and a newly detected coordinate inconsistency.

Original protocol frozen before measured timing histograms: early [0,8.4), target [8.4,30), late [30,60), shared shift calibrated on 538/537, transfer on 527/531, fixed released templates, no energy cuts. Literal microsecond interpretation failed with negative scales before target scoring. Five files (537,538,954,978,1030) have integer 0–2047 coordinates; ten span -53.6–151.1. Thesis supports waveform-bin interpretation but no file-specific export map was established.

Explicit conditional extension uses 0.1*stored_time-53.6 for those five files. Frozen before candidate calibration/evaluation; not independently verified timing calibration. Released simulation already has source-adjusted ramps and a 3% ion mixture. Evaluation early/late sums are normalization inputs. Not blind prediction.

Fitted common shift 0.3101803 us. Evaluation-tail totals: 527 measured 3057 vs predicted 3083.40 (-0.856%); 531 measured 2099 vs predicted 2015.83 (+4.126%). Structured shape discrepancy remains, including calibration shape. Alternative late baseline changes 527's sign. Count-only quadratic diagnostics and bootstrap omit important systematic uncertainties. No validated apparatus model, lifetime, epsilon or ARK physical inference.

Ten software checks pass, full candidate rerun identical apart from timestamp. Unchanged IC-13 intake audit hash matched and rerun, parser 13/13 pass. IC-01–12 not rerun; no whole-repository local audit or independent review. Initial modeling failure and plotting-permission failure recorded. Full outputs/failures/plots are in the downloadable packet; committed compact summary fingerprints them. Remote CI and published hashes must be checked separately.

Next: confirm timing export from independent documentation/author response (no contact initiated), recover source selection and baseline controls, then revisit joint energy-time mapping. Do not promote a residual to a new mechanism. Preserve all missing-energy records. Archive and earlier investigations remain untouched.
