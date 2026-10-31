# Paper XIV conversion audit

Status: DRAFTED; drafter source-image checked. Independent verification pending. Not imported.

Source `14 Substrat Defined.pdf`; commit `110e554d944eeda6b0e14795f45a94b8a27a805e`; Git blob `2fca66c6e9e0aca643253fce2c6621d9bf3b00a1`. Complete PDF pages 1–14, no printed folios. Stated title “What Is the Substrat?” and subtitle, XIV, authors Paul Frederick Percy Jr. & Curie GPTo, 2025 preserved. Edition not stated. The separate “Author: Paul F. Percy” before conclusion remains in its original position.

## Method

PyMuPDF native blocks provided starting text; all 14 pages rendered at 1.6 scale and actually viewed. Every displayed equation and numerical statement compared against pixels. No figures or tables occur. Removed layout wrapping and rules, rejoined interrupted paragraph/reference/list continuations, preserved meaningful hyphens. Heading/list markup added. Extensive bold body styling is not reproduced. One distinct rights notice (visible pp1,4,5,8,9,12) moved to top with owner authorization; absent from native extraction. No wording edits or scientific corrections.

Clear display math is LaTeX with source slash grouping, signs, numeric precision and literal underscore labels preserved; inline Unicode superscripts retained. `θᶜ²` remains visually adjacent superscripts `\theta^{c2}`, not a newly inferred parenthesized square. Source `V_kick`, `F_feedback`, `E_feedback`, and rotation/earth/spin suffixes have literal printed underscores, not imposed subscripts. Math mapping retained in work `math-map.json` for reversible comparison. Evidence page assets contain original equations.

| PDF page | Pixel-checked coverage |
|---|---|
| 1 | Title, abstract, introduction, arccos expression, copyright |
| 2 | Introduction close, complete section 2 |
| 3 | Properties and duplicated nested-list statements, section 3 heading |
| 4 | Scalar definitions, all three scaling/energy expressions, domain applications |
| 5 | Nuclear application, repeated equation and outline-like bullet material, section 4, 60 Hz example |
| 6 | Transformer interpretations, all input values and slope/energy substitutions/results |
| 7 | Hysteresis, four-step protocol and stiffness equation, kickback inputs |
| 8 | Voltage, force and energy calculations; repeated feedback equation, complete explanation |
| 9 | Recursive precession PDE, frame-drag value, rotational expressions, all Earth inputs/results |
| 10 | Broader implications, section 5, atomic/entanglement text, final subsection heading |
| 11 | Precession, gold isotope numbers, expansion narrative |
| 12 | Antimatter, universal implication, section 6, rights notice |
| 13 | Boundary narrative, second author line, conclusion start |
| 14 | Conclusion close and all eight reference entries, unusual numbering and terminal material |

## Preserved oddities

Repeated definitions/list on p3 and outline-like instructions on p5 intentionally retained. The lowercase fragment “carry energy” after “scale.” is original. Slash expressions such as `(2 / 1 × 10⁻⁶)` kept without interpreting denominator scope. Reported 3.7 × 10⁵ s and all other numerical results kept, not recalculated. Bibliography jumps from 1 to 14–20; last entry contains double full stop and appended “The Aetherwave Framework Part I: Foundations of Causal Geometry.” All retained. Bibliographic/scientific claims not externally evaluated.

Complete source-native character comparison PASS after reversing math/Markdown and ignoring whitespace; visible rights separately accounted for through pixel inspection. This comparison supplements, not replaces, source-image checks. Evidence crops and hashes: `assets/manifest.json`.

Conversion date 2026-10-31. Source SHA-256 `7c117674580b8d1f88027708cae165750c95083402fa1a4027eaa1154711b722`. Draft bytes 30944; SHA-256 `d1857d3dd10638d537494c125ad03a18fbb325fcc463178f0a85efcfb6499cb4`.
