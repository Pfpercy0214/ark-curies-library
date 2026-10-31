# Paper XII conversion audit

Status: DRAFTED; drafter source-image checked. Independent verification completed; see `independent-verification.md`. Not imported.

Source: `12 Aetherwave Predictions Aligned with CERN’s Lead-to-Gold Experiment.pdf` at source commit `110e554d944eeda6b0e14795f45a94b8a27a805e`; Git blob `7f560def8a465b422ea8806478d0985407f85ce0`; SHA-256 `113b355f0b6f26f56541292edf7d5e34bbd32e7f3ff4516c8b9dc9981c1fe590`. Complete PDF pages 1–7; no printed folios. Stated title, number XII, authors Paul Frederick Percy Jr. & Curie GPTo, and year 2025 preserved. Edition not stated. Conversion date 2026-10-31.

## Method and coverage

PyMuPDF 1.26.6 native blocks for initial extraction; rendered every page at scale 1.6 and viewed all seven actual page images. Removed layout line wraps, retained meaningful hyphens, added Markdown heading/list structure, joined the two page-spanning paragraphs and split list continuations. No substantive wording corrections. Source visible copyright notice (not native-extracted) preserved once at top per owner instruction. Original repeated footer placement omitted. No substantive figures or tables found. All numeric expressions and equations checked against pages, particularly pages 2, 3 and 5. Causal superscript c retained. Display math converted to LaTeX; inline Unicode notation retained without flattening.

| PDF page | Checked contents |
|---|---|
| 1 | Title/authorship, abstract, introduction, rights notice |
| 2 | Introduction continuation; section 2 isotope/count/ratio statements; section 3 heading |
| 3 | Sections 3.1–3.4, all bullets, arccos and energy equations |
| 4 | Rights notice; section 3 close; 4.1–4.2; 5 heading |
| 5 | Rights notice; illustrative-input limitation, all times/powers/units/equations, numerical results, 6 heading |
| 6 | Discussion, numbered list, conclusion start |
| 7 | Conclusion continuation, both references and URL |

## Preserved source oddities and limits

- Page 2 isotope notation begins with superscript minus (⁻²⁰⁸Pb, ⁻²⁰³Au, ⁻¹⁹⁷Au); retained, not repaired.
- Page 5 `≙` encoded as an equals sign with wedge above, not replaced by equality or approximation. Other signs and precision preserved.
- Scientific interpretations and cited experiments were not assessed. The source's illustrative input caveat remains intact.
- All source-native characters match draft after reversing explicit math/Markdown transformations and ignoring whitespace: PASS. This check alone does not prove fidelity; the visible footer addition required image review.

Evidence assets and source crops/hashes: `assets/manifest.json`. No evidence-image links inserted into paper because all substantive content is text and unambiguous equations.

Draft byte count: 14249. Draft SHA-256: `57c6bf7c187df55d34450908ab4ff29ce1858cb5de3df7ac7572f5bc558b22af`.

## Independent-review resolution — 2026-10-31

Reviewer confirmed draft source fidelity; audit-only correction removes erroneous p7 rights-notice claim and records visible notices on pp1,4,5. Draft unchanged. Independent report SHA-256: `7e18cdf4bc8f6eb2e9172060849df164bcb6a7284e4b6e4f6488176f3780cd38`.
