# Session handoff — IC-13, 2026-11-01

Parent: ed7252ee5efe00c37f9967f5c455b3bb08996260. Owner provided five original NIST distributions, acquisition manifest and notes after the IC-12 access blocker. Existing authorization covers research-branch documentation, not merge. No raw archive, policies, prior investigations or source-repository edits.

[IC-13 entry](../investigations/identity-containment-13/README.md).

Receipt verified: 5/5 distribution hashes/sizes, 33/33 member hashes/sizes/row counts/interpreted headers, 3/3 ZIP CRC checks. No publisher checksum verified. 15 BL2 series, 2,157,334 listed records, 2,156,273 complete energy-time pairs. No source bytes altered or large experimental archives copied into Git. Full member audit and original provenance sidecars remain in the downloadable packet; compact fingerprints, parser, tests, contract and catalog are committed.

New source-level issue: Series_527 has 1,061 missing energies with times present, at original lines 21,664–22,724 inclusive. Default joint energy-time use of that file is blocked pending a declared missingness rule. Do not call these zero-energy events or silently delete them. No cause inferred. Series_911's UTF-8 BOM is interpreted without changing its bytes. BL1 series 134 has fractional counts and 454 negative entries; not raw Poisson count inputs. RGA signs are retained.

Thirteen parser/safety tests pass; actual-data audit executed. Initial numpy parser failed on missing energy; next strict header comparison encountered BOM. Both recorded, not hidden. No experimental fitting, spectral outcome inspection, ARK coupling, lifetime inference, independent review, earlier-suite rerun or local complete-archive audit. Remote CI is a separate publication check.

Next: source-backed calibration and response protocol. Measured/simulated ramp settings differ; nominal header equality does not establish upstream invariance. BL2 energy is arbitrary units and trap duration is not exposure. Read publication methods to complete maps/cuts/background/likelihood, then freeze acquisition-group split. Raw acquisition is no longer blocked; quantitative inference is not automatically cleared.
