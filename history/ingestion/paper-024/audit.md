# Paper XXIV conversion audit

<!-- current-intake-binding -->
**Current intake binding (2026-10-31):** AI-source-checked and independently verified; IMPORT_PREPARED_UNMERGED under owner delegation. Final registered SHA-256 `09911c0471e765e64e549bad14bd60d255434b5a6cc9e4eccf412e5b8822f8c8`, 81734 bytes. Earlier draft-status/fingerprint notes below are historical; the separate final verification and prepared ledger control current status. No individual human review or scientific validation claimed.
<!-- /current-intake-binding -->

Status: drafter checked all 46 source pages; independent review pending. This is source preservation, not endorsement of the paper’s claims or a check of its scientific validity.

## Identity and provenance

- Source: `XXIV The Scalar Origin of Quantum Gravity.pdf`, all PDF pages 1–46.
- Printed heading: “XXIV: The Scalar Origin of Quantum Gravity”. Date October 16, 2025.
- Printed author and AI-collaborator distinctions retained verbatim.
- Read-only source repository `Pfpercy0214/aetherwave-unified-theory`, pinned commit `110e554d944eeda6b0e14795f45a94b8a27a805e`.
- Git source blob `deb36484fb328754f26c49d057f0592ae61ecd15`.
- Source SHA-256 `fab1c065b272a4e5beeb51f39ddbf3082bc2d5c87dc4679911d6007f9d36c4c0`.
- Draft SHA-256 `09911c0471e765e64e549bad14bd60d255434b5a6cc9e4eccf412e5b8822f8c8`; 81734 bytes UTF-8.

## Coverage and formatting

All 46 PDF pages rendered and inspected individually, including every equation, numerical expression, reference, table cell, and all appendices A–H. No substantive figures. A single distinct copyright notice, visible e.g. p1 but absent from native extraction, restored once near the top under owner-approved consolidation. No source prose omitted; emphasis formatting is not treated as new semantic prose. Physical prose continuations rejoined; lexical hyphens retained. Source list markers represented by Markdown list markers. Reference boundaries retained, including the series reference with its full I–XXIII listing. Historical claims of AI coauthorship and empirical validation are source text, not this conversion’s certification.

Nine borderless logical tables, 178 body cells and 30 header cells, retained in reading order. Automatic table detector found none; column/row rectangles were determined and checked against rendered pages. Joined continuations preserve all cells without synthesizing headers or labels:

| Source pages | Table | Body cells |
| --- | --- | ---: |
| 8 | Observable correspondence | 15 |
| 10 | Observational equivalence | 8 |
| 19 | Cross-domain summary | 25 |
| 33–34 | Appendix A definitions | 25 |
| 34–35 | Appendix B equations, including split first description cell | 21 |
| 36 | Appendix C constants | 15 |
| 37 | Appendix E tests | 12 |
| 38–39 | Appendix F symbols/units | 39 |
| 41–42 | G.8 historical correspondence | 18 |

## Math fidelity and original odd forms

34 unambiguous standalone display occurrences encoded as LaTeX with reversible source-string mappings; 13 further displays retained in fenced literal Unicode text. Inline and table Unicode notation remains machine-readable source text. Standalone mathematical boundaries are kept, with explicit textual “and” separators when the source uses them. Slash fractions remain slash fractions; missing bounds, factors, and unusual definitions are not repaired. Full mappings and literal-expression inventory accompany the working audit; these checks do not promise every AI will interpret every source ambiguity identically.

- Source `ρₑff` has only e in subscript; encoded `\rho_{e}ff`, not silently normalized to a full eff subscript. Source baseline `∫Ωᶜ` on p9 and `∫Ω` on p46 retained rather than invented integration-bound notation.
- Source `G_{μν}`, `T_{μν}` literal underscore/braces stay literal, including p13’s display. Neither the repeated θᶜ factors nor absent tensor indices repaired.
- Compound superscript forms `θᶜ²` and `kᶜ⁻¹` retained literally rather than deciding whether c is a label or an exponent to be multiplied/raised. Corresponding whole displays are literal, preserving their exact grouping uncertainty.
- Mixed literal exponential forms `e^(−i ωₙ t)` / `e^{i(k·x − Ωt)}` and explicit textual clauses retain original characters. The p25 paired standing-wave equations retain source “with”; no implied multiplication between equations introduced.
- Appendix H keeps its original source approximations, convention note, duplicated explanatory forms and scientific inconsistencies. Its displayed/inline root, dot accent on T, subscripts, units, relations, and literal braces checked visually. No intended-physics reconstruction performed.
- Source Σ is preserved as printed Σ, not changed into a sum operator with invented bounds.

## Actual automated checks

All 64,374 non-whitespace native source characters preserved in the assembled pre-math representation (character multiset equality; not a sequence proof because table column ordering and joins change extraction order). Reversible mapping strings preserved for all 34 LaTeX occurrences. Tables extracted by source-checked rectangles and all 208 cells read against pixels. Pandoc MathML conversion: 34 math nodes, zero merror, no stderr. Syntax success is separate from visual source fidelity; this is not a browser-rendering acceptance test. Independent verifier must check the exact final hash before registration.

## Page coverage

| PDF page | Visual source check | LaTeX displays | Literal displays |
| --- | --- | ---: | ---: |
| 1 | Complete | 1 | 0 |
| 2 | Complete | 0 | 0 |
| 3 | Complete | 0 | 0 |
| 4 | Complete | 0 | 0 |
| 5 | Complete | 2 | 0 |
| 6 | Complete | 2 | 1 |
| 7 | Complete | 1 | 1 |
| 8 | Complete | 0 | 0 |
| 9 | Complete | 2 | 1 |
| 10 | Complete | 0 | 1 |
| 11 | Complete | 0 | 0 |
| 12 | Complete | 3 | 0 |
| 13 | Complete | 3 | 1 |
| 14 | Complete | 0 | 0 |
| 15 | Complete | 1 | 0 |
| 16 | Complete | 1 | 0 |
| 17 | Complete | 3 | 0 |
| 18 | Complete | 1 | 0 |
| 19 | Complete | 0 | 0 |
| 20 | Complete | 2 | 1 |
| 21 | Complete | 1 | 1 |
| 22 | Complete | 1 | 0 |
| 23 | Complete | 1 | 0 |
| 24 | Complete | 1 | 0 |
| 25 | Complete | 2 | 2 |
| 26 | Complete | 2 | 0 |
| 27 | Complete | 1 | 0 |
| 28 | Complete | 0 | 0 |
| 29 | Complete | 0 | 0 |
| 30 | Complete | 0 | 0 |
| 31 | Complete | 0 | 0 |
| 32 | Complete | 0 | 0 |
| 33 | Complete | 0 | 0 |
| 34 | Complete | 0 | 0 |
| 35 | Complete | 0 | 0 |
| 36 | Complete | 0 | 0 |
| 37 | Complete | 0 | 0 |
| 38 | Complete | 0 | 0 |
| 39 | Complete | 0 | 0 |
| 40 | Complete | 0 | 0 |
| 41 | Complete | 0 | 0 |
| 42 | Complete | 0 | 0 |
| 43 | Complete | 1 | 1 |
| 44 | Complete | 1 | 0 |
| 45 | Complete | 1 | 1 |
| 46 | Complete | 0 | 2 |

## Literal display inventory

- p6: `u = ½ kᶜ θᶜ²`
- p7: `d/dt (θᶜ τᶜ kᶜ) = 0 for a closed system`
- p9: `dSₜ dt = kᶜ⁻¹ ∂θᶜ/∂t`
- p10: `ω = ∂θᶜ/∂τᶜ, and sign(dSₜ) defines the arrow of time.`
- p13: `T_{μν} ∝ τᶜ kᶜ θᶜ θᶜ`
- p20: `U ∝ kᶜ θᶜ² Z²`
- p21: `q ∝ Z · ω θᶜ, m ∝ Z · kᶜ θᶜ²`
- p25: `ρₑff = ½ kᶜ θᶜ² + τᶜ (∂θᶜ/∂t)².`
- p25: `θᶜₙ(r,t) = Aₙ sin(n π r / L) e^(−i ωₙ t) with ωₙ² = (kᶜ / τᶜ)(n π / L)².`
- p43: `∇²Φ = 4π G ρ with kᶜ₀ ↔ 1/(2G) to leading order.`
- p45: `Δω/ω = ½ Δ(kᶜ/τᶜ) / (kᶜ/τᶜ) ≈ − Δ(kᶜ/τᶜ) (up to convention; paper uses linearized sign)`
- p46: `C[δθ] − (1/c²) ∂²δθ/∂t² = (τ₀/k₀) ∂(δdSₜ)/∂t + higher order.`
- p46: `d/dt ∫Ω [½ kᶜ θᶜ² + τᶜ (∂θᶜ/∂t)²] dV = − ∫Ω θᶜ ω (∂θᶜ/∂t) dV`
