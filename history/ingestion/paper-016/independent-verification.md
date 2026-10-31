# Paper XVI — independent preservation verification

## Result

All 36 pages independently rendered with Poppler at 1800-pixel page height and viewed in full. Complete draft compared against original wording, mathematical/numerical expressions, tables, references, appendices and one figure. No dropped substantive text or numeric/table value found. One mathematical expression-boundary defect and two structural formatting corrections were reported to the lead; all corrected by the drafter and independently rechecked. No unresolved conversion defect remains. This is source-to-output preservation review, not scientific validation.

Initial reviewed draft: SHA256 `d3f2ba94639e6468c945236011b8eb9f0431c34162f6d12e0d98e5b8504e0cca`, 57,129 bytes.

Source: `XVI The Mechanism of the Aether Reality Kernel- Scalar Recursion, Causal Pressure, and Temporal Bifurcation.pdf`; Git blob `833534cfee6d82967e559868689a2c1fee6f0060`; SHA256 `13898b831c644ebd37189e4f1922904463d02458d859e309c55ac062e1db0abd`; physical pages 1–36, stated date 7/21/2025, no edition stated.

## Conversion corrections requested

1. **p33, Appendix B.1:** source has one expression `τᶜ = E × t_decay`. Draft incorrectly wraps only `τᶜ = E × t` in display LaTeX and leaves `_decay` in a separate paragraph. Preserve the whole literal source expression together, e.g. `τᶜ = E × t\_decay`. Do not silently reinterpret its original baseline underscore as a repaired subscript.
2. **p13, §4.6:** three distinct conditional lines beginning `If ω ≫`, `If ω ≈`, `If ω ≪` are concatenated into one paragraph. Restore separate lines/paragraphs to keep the conditional statements distinct.
3. **p29, references 1–3:** title continuations are split into unindented separate paragraphs. Join each reference into one complete item. No words should change.

Reviewer did not edit the draft. All three corrections were applied by the drafter and independently rechecked against the source. Final verified SHA256 `5cd665e776968737871da2de038fd8a64f4f72d793d4b6107ae43ff724b370cc`, 57,114 bytes. Full 45,129-character comparison, 80-cell count and all seven asset hash checks rerun successfully. Other reflow, normalized emphasis and approved copyright notice once at top do not change substantive content.

## Checks executed

- Independently extracted all source pages directly, then reversed Markdown/table markup and the LaTeX mappings after individually checking every mapping against source pixels. Full ordered nonwhitespace content comparison: **45,129 source characters = 45,129 reverse-mapped draft characters**, exact equality. Bullets/pipes are layout-normalized. This check cannot detect expression boundaries; defect 1 was found through visual comparison, not concealed by equality.
- All **80 table cells including headers** independently compared visually: p23 18 cells, p26 36 cells, p32 12 cells, pp35–36 14 cells (including repeated header). Every symbol, numeric precision, range, unit and cell association matches.
- Source figure p8 and `assets/figure-01.png` both viewed. Complete outer/inner circles, diamond, cross, eight θᶜ labels, four τᶜ labels and four kᶜ labels retained. Geometry/caption/source placement unchanged; not redrawn. SHA256 `9489104c42e0c0fef2295261ba22d8bcde792fb248322243fb61df3c35298189`. All seven manifest asset SHA256 values independently recomputed and match. Final staged relative link resolution remains lead's packaging responsibility.
- All displayed and inline mathematical expressions checked, including original slash scopes, literal underscores/carets, inequalities, superscripts/subscripts, ∆ versus Δ usage and multiplication symbols. No scientific repair performed.

## Page-specific coverage

| Page | Independent source/output comparison |
|---|---|
| 1 | Full title/authors/date, author Unicode note, introduction and 0.00000% claim, copyright. |
| 2 | Intro ending; scalar definitions; mixed derivative `dτdt\frac{d\tau}{dt}` and boxed U+2061 in arc⁡tan retained; tan⁻¹ equation and limits. |
| 3 | τᶜ integral with original ∫₀^T; kᶜ derivative/ratio; all units and implications. |
| 4 | ω period/derivative, Hertz unit, ∆S_cl/k_B literal forms, pressure derivative and collapse rate. |
| 5 | Entropy implications, non-reductionist scalar lists, observation claims. |
| 6 | Recursion/π emergence prose and full constraints list. |
| 7 | r=τᶜ/kᶜ, C=θᶜ·τᶜ/ω, π=C/(2·r), all surrounding text. |
| 8 | Complete substantive figure, internal labels, caption, all five mappings; crop separately inspected. |
| 9 | Figure continuation, triadic lists, ω embedding and interpretation. |
| 10 | Three ω roles, entropic deformation, nested-system examples. |
| 11 | Summary and entropy discussion, causal pressure definition. |
| 12 | Pᶜ, ∆Sₜ derivative, collapse inequality, ω lock; literal trailing ** and stability qualifier. |
| 13 | Both propagation directions and all three ω/∆Sₜ conditions; boundary correction requested. |
| 14 | Time recursion prose/scalar list; f∝1/τᶜ and implications. |
| 15 | cos dilation equation, limits, perceived-time integral, exhaustion conditions. |
| 16 | Literal ω_actual condition, flicker/overfrequency lists, summary. |
| 17 | Summary statements and all dual-arrow experimental statements. |
| 18 | θᶜ⁻/θᶜ⁺, all definitions, Dₛ sign expression including ω⁻¹ and three sign conditions. |
| 19 | Interpretation, knot statements and thermodynamics implications. |
| 20 | Summary, simulation introduction, numbered equations1–2 and descriptions. |
| 21 | Equations3–4; neutron/hydrogen numerical values, units and collapse inputs. |
| 22 | Inputs/results including 9.5×10¹³,1.7×10¹⁴,6.2ps; bidirectional case. |
| 23 | All 18 parameter-table cells, experimental platforms, summary/discussion transition. |
| 24 | Identity/entropy discussion and all lists. |
| 25 | Intelligence and AGI prose/lists unchanged. |
| 26 | All 36 cross-scale table cells; symmetry statements. |
| 27 | Poetic statements, historical conversational transition, conclusion lists/prose. |
| 28 | Persistence principle, prospective XVII/XVIII titles, final words. |
| 29 | Final statement and references1–3, exact URLs; reference continuity correction requested. |
| 30 | References4–8 and URLs, Appendix A scalar derivations, tan⁻¹√ grouping. |
| 31 | All tension/stiffness/anchor derivations, × versus ·, differential orders and units. |
| 32 | Entropy equations; all 12 metrics-table cells; Appendix B exponential/integral derivation. |
| 33 | t_decay boundary defect; B.2–B.4 full equations/conditions and literal τ_min/T_c. |
| 34 | B.4 ending, B.5 sign and inequality; Appendix D opening (no C in source). |
| 35 | Crystal scalar sections; all 8 first table-segment cells. |
| 36 | Repeated header plus 4 continuation body cells; entire closing paragraph. |

## Original-source ambiguities/oddities retained

The source visibly mixes typed LaTeX with Unicode, including the p2 duplicated derivative and boxed function-application glyph. Its native U+2061 is retained in text and the complete p2 source image preserves the visible box; no guessed arctangent repair. Literal ∫₀^T, e^(−t/τ), t_decay, τ_min, T_c and ω_actual should remain literal forms. The p32 table's Tₐ differs from later T_c. Appendix sequence A/B/D, prospective later-paper titles and historical conversational text are original. Simulated precision, unit inconsistencies and scientific/cognitive claims are preserved without endorsement or correction.
