# Paper XVII conversion audit

<!-- current-intake-binding -->
**Current intake binding (2026-10-31):** AI-source-checked and independently verified; IMPORT_PREPARED_UNMERGED under owner delegation. Final registered SHA-256 `b5c5008edf922c500a24ecb8955397ffa626ead620cdb2e91af120f71de38bf4`, 21029 bytes. Earlier draft-status/fingerprint notes below are historical; the separate final verification and prepared ledger control current status. No individual human review or scientific validation claimed.
<!-- /current-intake-binding -->

Status: SOURCE_CHECKED; drafter check and separate independent source-preservation verification complete. Not imported.

Source `17 Predictive Causal Pressure Model and the Voyager Anomaly.pdf`, commit `110e554d944eeda6b0e14795f45a94b8a27a805e`, Git blob `24ca22d003a6986e78d0fdfa543664a3ce253cb6`, SHA-256 `5127cd56739e3e8f257274190cfaecc2756437d1f426785f34a2c4ecf7c38990`. Complete PDF pages1–15, no printed folios. Title “Predictive Causal Pressure Model and the Voyager Anomaly: A Substrat-Based Analysis”; authors Paul Frederick Percy Jr. & Curie GPTo; Jul 22, 2025 preserved. Paper number is filename/inventory assignment, not visibly stated in title; not added to original draft. Edition not stated.

## Method and checks

PyMuPDF blocks; all15source pages rendered at1.5scale and actually viewed. Every equation, numerical input/date/prediction and plot checked against pixels. Layout wraps removed, meaningful hyphens preserved; headings/lists added, pervasive bold styling not reproduced. Single distinct rights notice once at top with owner permission. Clear display math LaTeX, inline scalar/numerical Unicode. Literal underscore label A_eff retained as escaped underscore, not silently made subscript. Source literal Weibull expression with P_failure, T_eff and caret ^β preserved in code.

Nine figure occurrences (five distinct numbered figures) retained in original order with source captions and page-specific exact image-bound crops. Figure1 occurs pp3/4/6, Figure2 pp5/8, Figure4 p7, Figure5 pp9/11, Figure3 p10. A Figure2 caption on p13 has no actual figure underneath in the PDF; preserved caption only, no invented image. All chart axes, tick labels, legends, colored curves/thresholds retained; images not redrawn or curve data inferred. No tables.

| PDF page | Checked coverage |
|---|---|
| 1 | Title/authors/date, abstract, introduction and entropy start |
| 2 | Entropy continuation, scalar definitions, PSI equation and first variable |
| 3 | Pressure equations, all definitions, Figure1 first occurrence |
| 4 | Definitions, repeated Figure1, zones start |
| 5 | Zones II/III, thermal assertions, Figure2 first occurrence |
| 6 | Methods, numerical inputs, Figure1 third occurrence, exponential equation |
| 7 | Definitions, Figure4, material inputs/thermal equation and 50°C claim |
| 8 | Figure2 second occurrence, lifespan inputs/equations/2025 probability |
| 9 | Figure5, repeated thermal paragraphs and --- prefix, telemetry list |
| 10 | Continuation, Figure3 dual axes, subsystem claims |
| 11 | Figure5 repeat, repeated text and forecast start |
| 12 | Repeated change-of-state paragraphs, all 2025/2035/2042 forecasts |
| 13 | 2026/2045 tests, repeated thermal text, Figure2 caption without image, conclusion |
| 14 | Conclusion close and ten references |
| 15 | Eleventh/final reference and URL |

Full native-text character comparison after reversing explicit math and markup and ignoring whitespace: PASS. Plot labels are raster-only, so their coverage depends on pixel inspection and exact crops, not this native check. Source contradictions (50°C narrative versus sub-degree plotted range; baseline statement versus curve), repeated paragraphs/figures, --- prefixes, forecast dates and all scientific assertions retained without correction or external verification.

Asset provenance/crop points/SHA-256 in `assets/manifest.json`. Figure links target `../../sources/assets/paper-017/conv-01/`. Conversion date2026-10-31. Draft bytes 21029; SHA-256 `b5c5008edf922c500a24ecb8955397ffa626ead620cdb2e91af120f71de38bf4`.

Independent-review correction,2026-10-31: source p14 References heading separated from preceding conclusion. No wording change. Independent recheck pending.

Independent verification closed (2026-10-31): all requested corrections rechecked; no unresolved conversion defect. See `independent-verification.md`, SHA-256 `364924dddcd1930dced4dbd42608dc3412a16f44a11ac3a82589d22499869f07`. Earlier pending statements record the contemporaneous review state and are superseded by this closure. Final draft hash above remains unchanged.
