# Paper XVI conversion audit

Status: DRAFTED; drafter source-image checked. Independent verification pending. Not imported.

Source `XVI The Mechanism of the Aether Reality Kernel- Scalar Recursion, Causal Pressure, and Temporal Bifurcation.pdf` at commit `110e554d944eeda6b0e14795f45a94b8a27a805e`; Git blob `833534cfee6d82967e559868689a2c1fee6f0060`; SHA-256 `13898b831c644ebd37189e4f1922904463d02458d859e309c55ac062e1db0abd`. Complete PDF pages 1–36; no printed folios. Stated Paper XVI, full title, Paul Frederick Percy Jr. & Curie GPTo, 7/21/2025 retained. Edition not stated. Conversion date 2026-10-31.

## Method

PyMuPDF native blocks; all 36 pages rendered at scale1.5 and actually viewed. All equations, numeric values/units, and all table cells compared against pixels. Text reflowed without substantive changes. Repeated single copyright notice placed once at top per owner authorization; no running page markers in draft. Heading/list/table markup added; pervasive bold emphasis not fully reproduced. One substantive figure cropped at its exact PDF image bounds and inserted in source order; original labels and geometry retained, not redrawn. Figure caption and all surrounding interpretation text retained.

Clear selected display equations represented in LaTeX with exact reversible mapping in local `math-map.json`; inline Unicode math retained. Source author explicitly states return to Unicode for AI, and that note is preserved. Literal caret/underscore forms such as ∫₀^T, e^(−t / τ), t_decay, τ_min and T_c retained instead of silently repairing notation. Mixed derivative fragment `dτdt\frac{d\tau}{dt}` preserved in code; source arctan contains U+2061 FUNCTION APPLICATION, visibly rendered as a boxed glyph, retained together with page-image evidence. Source trailing ** retained as escaped literal asterisks. The appendix table's Tₐ differs from later T_c and remains unchanged. Appendix sequence A, B, D is original; no missing C invented.

## All-page coverage

| PDF page | Checked contents |
|---|---|
| 1 | Title/authors/date and author Unicode note; introduction |
| 2 | Introduction close, scalar definitions; malformed mixed derivative and arctan glyph |
| 3 | Tension integral, stiffness definition and units |
| 4 | Anchor and entropy definitions, expressions and units |
| 5 | Non-reductionist discussion and scalar lists |
| 6 | Recursive curvature, π emergence and constraints |
| 7 | π ratios and implications; section 3 heading |
| 8 | Entire Figure 1 (including internal labels), caption and five mappings |
| 9 | Triadic structure, embedding omega |
| 10 | Entropic deformation and nested systems |
| 11 | Section 3 summary, entropy section and pressure definition |
| 12 | Pressure equations, collapse inequality, omega lock and literal ** |
| 13 | Both propagation directions and balance inequalities |
| 14 | Temporal recursion and inverse-frequency equation |
| 15 | Dilation equation, perceived-time integral and exhaustion |
| 16 | Overfrequency, flicker, summary |
| 17 | Summary close and time experiments |
| 18 | Bidirectional pressure, direction sign equation, conditions |
| 19 | Interpretation, knot model and implications |
| 20 | Summary, simulation intro, core equations (1)/(2) |
| 21 | Core equations (3)/(4), neutron/hydrogen values, collapse inputs |
| 22 | Remaining inputs, simulated results, bidirectional case |
| 23 | Parameter table all18cells; summary and discussion start |
| 24 | Discussion continuation, identity and entropy |
| 25 | Intelligence and AGI lists |
| 26 | Cross-scale table all36cells, symmetry section |
| 27 | Poetic statements and transition sentence, conclusion |
| 28 | Scalar principle, prospective paper titles, final words |
| 29 | Final statement and references1–3 |
| 30 | References4–8; Appendix A first derivations |
| 31 | Memory/stiffness/anchor derivations, all equations |
| 32 | Entropy derivations; metrics table all12cells; Appendix B energy integral |
| 33 | B.1 end, B.2–B.4 equations and text |
| 34 | B.4 end/B.5; Appendix D start (no C present) |
| 35 | Crystal scalar sections and first table segment all8cells |
| 36 | Crystal table continuation all6cells and closing paragraph |

Four tables (last split across pp35–36 with repeated header preserved) have 80 cells including headers; every cell checked. Source historical prospective titles for XVII/XVIII differ from later published papers; neither corrected. Historical conversational transition “Proceeding now to the final section:” retained. Scientific/medical/cognition claims, simulated results and reference validity not evaluated or endorsed; no new calculations or simulation performed.

Complete native-text character comparison after reversing explicit math and Markdown and ignoring whitespace: PASS with zero differences (`native-comparison.json`). Native text does not contain figure labels or visible copyright; those verified separately from pixels and retained via crop/notice. Comparison is not a substitute for pixel verification.

Assets and exact crop/source-page/SHA-256 metadata: `assets/manifest.json`. Draft figure link uses parent destination `../../sources/assets/paper-016/conv-01/figure-01.png`; parent owns staging. Draft bytes 57114, SHA-256 `5cd665e776968737871da2de038fd8a64f4f72d793d4b6107ae43ff724b370cc`.

Independent-review correction, 2026-10-31: p33/B.1 literal `τᶜ = E × t_decay` restored as one expression (escaped underscore, not inferred subscript); p13 three If ω cases separated; p29 reference continuations1–3 joined to their respective entries. Zero native comparison differences after these formatting corrections. Independent recheck pending.
