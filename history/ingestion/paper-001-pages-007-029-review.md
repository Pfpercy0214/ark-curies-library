# Paper I draft audit — PDF pages 7–29

## Scope and evidence

- Authoritative file: `Complete Aetherwave Unified Theory.pdf`, compiled-volume blob `c39edcd393d3d27aa6a93313e0e9b8f602c47dbf`, source Git commit `110e554d944eeda6b0e14795f45a94b8a27a805e`.
- PDF SHA-256: `f8cb4138423587ce313dd6c44a0d141946570a2f9006eadfaac18d18cc761b6c`.
- Converted only PDF pages 7–29 inclusive, the first half of Paper I; no standalone-edition substitution. Page 29 ends with the composite-function/tensor paragraph; page 30 belongs to the other drafter.
- All 23 assigned page images were visually inspected at their rendered 1700-pixel page height, in addition to native text extraction. Equations, literal malformed notation, superscripts, units, numeric lists, paragraph continuity, headings, and notices were checked against pixels.
- No substantive figures, diagrams, or source tables occur in this half. Decorative horizontal rules are layout only. The nine-system list on p22 is a bulleted list, not a table, and remains a list.
- No provisional Markdown was used as source. No scientific claims, numerical calculations, or physics were corrected or validated.

## Layout transformations requiring owner review

1. Reflowed PDF line wrapping into prose paragraphs; retained visible hyphenated words, including compounds broken across a source line. Removed print pagination layout. Joined actual sentence continuations at 11→12, 12→13, 18→19, and 27→28. Lists continue across page boundaries without duplication.
2. Applied Markdown heading hierarchy and list syntax. Separated title, parenthetical paper designation, and authors. Promoted visibly distinct subheadings previously touching prose into separate headings. No invented headings or page markers in the paper.
3. **Proposed, pending owner approval:** retained each of the two recurring attribution/copyright notices once at the opening, in original wording. Omitted only duplicate repetitions of those notices. The two different notices were not conflated. No unique notice was omitted.
4. Encoded unambiguous display mathematics as LaTeX, preserving signs, values, operators, superscripts and source function names (`sqrt` stays `sqrt`). Unicode mathematical notation remains readable inline. Literal malformed/backslash/caret/underscore expressions are protected with Markdown code spans rather than silently repaired into canonical equations.
5. Original typographic weight/font changes and decorative horizontal separators are not reproduced. No content-bearing drawings were replaced or omitted.

## Page-to-section coverage

| PDF page | Content checked |
|---:|---|
| 7 | Title, authors, abstract, TOC 1–6 |
| 8 | TOC 7–14; §1 introduction, causal-slope definition |
| 9 | §1 variable list and effective tensor expression |
| 10 | §1 conclusion; §2 substrat and directional elasticity |
| 11 | §3 slope definition, black-hole discussion, GPS example begins |
| 12 | GPS continuation/calculation; directional geometry; §4 begins |
| 13 | §4 flow gradient, potential, comparison with GR |
| 14 | §4 flow visualization; §5 energy and variable list |
| 15 | §5 compression, transformer example, recovery list begins |
| 16 | §5 recovery/causality; §6 dipole definition |
| 17 | §6 transformer and cosmic examples; significance list begins |
| 18 | §6 list/conclusion; §§6.1, 6.1.1, 6.1.2 begin |
| 19 | §6.1.2 continuation; §§6.1.3–6.1.5 |
| 20 | §6.1 closing prose; §§6.2, 6.2.1, solenoid relation |
| 21 | §6.2.1 variables/core law; §6.2.2 flux/coupling |
| 22 | §§6.2.3–6.2.5, nine-system list, quantum conditions |
| 23 | §6.2.5 law/conclusion; §§6.3, 6.3.1 |
| 24 | §6.3.1 variable list continued; §§6.3.2–6.3.4 |
| 25 | §6.3.4 equations/conclusion; §6.3.5 |
| 26 | Section 6 continuation note; §7 temporal inversion/invisibility |
| 27 | §7 implication list continued, dipole collapse, engineering; §8 begins |
| 28 | §8 opening continuation, definition, ranges, implications |
| 29 | §8 quantum/gravitational bridge and composite stiffness |

## Equation, numeric, and visual checklist

- [x] 33 LaTeX display blocks plus 14 literal-notation display blocks: 47 blocks total. Four blocks contain two stacked rows, for 51 displayed rows. Inline math and mathematical list entries are additional and not included in that count.
- [x] All 14 explicitly numbered expressions in this half: (6.1.1)–(6.1.3) and (6.3.1)–(6.3.11).
- [x] Original equation numbering preserved; no renumbering or generated equation labels.
- [x] Zero source tables: table-cell verification not applicable.
- [x] All nine p22 system bullets checked: Transformer 500 J/0.00158 rad; Switching Inductor 0.05 J/1.58 × 10⁻⁵ rad; MRI Magnet 1.25 MJ/0.079 rad; Ignition Coil 0.16 J/2.83 × 10⁻⁵ rad; Relay Coil 12.5 mJ/7.91 × 10⁻⁶ rad; Tokamak Coil 12 MJ/0.245 rad; SQUID 50 aJ/1.58 × 10⁻¹⁴ rad; RF Coil 0.5 µJ/1.58 × 10⁻⁶ rad; Superconducting Coil 50 kJ/0.005 rad.
- [x] p28 local/astrophysical/cosmic stiffness ranges retained, including all `N·rad⁻²` units.
- [x] No substantive figures/drawings found; no asset placeholders needed for this half.
- [x] All unique source words retained. No AI narrative, scientific appraisal, summary, or front matter added to paper draft.

## Exact source anomalies retained, not repaired

| Location | Source-specific preservation |
|---|---|
| pp7–8 TOC | `θc\θᶜ`, `kckᶜ`, and `Gμν(eff)G^{(eff)}_{\μ\ν}` remain literal. TOC spacing/hyphenation differs from main §1 and is not editorially unified. |
| p9 | Literal `\u3000Gᵉᶠᶠ_μν = αK_μν + βT_μν`, including the visible `\u3000` characters and underscores. |
| pp10,12 | Transition prose retains duplicated `θc\θᶜ`. |
| p12 | `θᶜ ≈ arccos(1 − 5.2 × 10⁻¹⁰) ≈ 0.000001 radians` retained, without recalculation or numerical correction. |
| p13 | `Gμν = Rμν − ½Rgμν = κTμν` preserved as baseline μν, not silently converted into tensor subscripts. |
| pp15,17 | Repeated transformer energy result `E ≈ 5000 J`, with 0.005 radians and 4 × 10⁸ N·rad⁻², preserved. |
| pp18–19 | Uppercase Θ and visibly literal caret strings in `Θ^c`, `k^c`, `(ΔΘ^c)^2`, and `a_θ = d^2Θ^c / dt^2` preserved, not normalized to lowercase θ or superscript formatting. |
| p21 | Flux `Φᴮ` has superscript B; not silently converted to the later p23+ literal `Φ_B`. Both dimensional statements (`m¹ᐟ²`, `m⁻¹ᐟ²·A⁻¹`) retained. `μₑff`, `αₑff` retain only the e as a subscript rather than converting all of eff. |
| pp23–25 | Literal `_B` and `_θ` remain underscores, unlike the superscript B on p21. |
| p24 | Original reference `(cf. Page 31)` retained as written; not retargeted to compiled-volume pagination. Equation (6.3.6) retains `2.5 × 10⁵ V`, and following prose retains `250 kV`. |
| p25 | “Differentiating θᶜ with respect to time (squared),” and (6.3.10) `a_θ ∝ I · dI/dt` retained without mathematical repair. |
| p29 | Literal suffixes `kᶜ_slope`, `kᶜ_torsion`, `kᶜ_shear`, `kᶜ_stretch`, `kᶜ_compress` preserved, not converted to inferred tensor indexes. |

## Remaining review

No unresolved unreadable glyph was found within these assigned pages. Source inconsistencies above are not conversion fixes. Independent verifier and parent assembly review remain required, particularly mixed literal notation and the proposed duplicate-notice policy. This draft is archival transcription, not scientific validation or approval for import.

## Independent-review corrections applied

- Removed accidental Markdown backticks inside LaTeX blocks (formatting pass had matched `k^c`).
- Rechecked p21 against pixels: α dimension has negative one-half exponent, despite missing minus in native extraction; transcribed as `m^{-1/2}·A^{-1}`.
- Encoded p21 baseline ff explicitly upright after subscript e, preserving the source’s unusual mixed baseline rather than treating ff as variables.

## Mechanical checks run

- All 33 LaTeX blocks have balanced braces and contain no Markdown backticks.
- All 14 numbered source expressions appear exactly once.
- Each non-LaTeX body block matches its source-extracted token content after removing only Markdown wrappers, bullet syntax, and whitespace differences; page-continuation joins included. This token check supplements, not replaces, visual review, and cannot detect native-extraction omissions such as the p21 minus corrected above.
