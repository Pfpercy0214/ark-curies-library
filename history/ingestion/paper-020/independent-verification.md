# Paper XX — independent preservation verification

## Result

All 27 physical source pages were independently rendered with Poppler (1800-pixel page height) and viewed in full. Complete draft compared with source prose, every mathematical/numerical expression, all table cells, source code, references and final historical dialogue. No missing/changed mathematical or substantive textual content found. One paragraph/separator-boundary formatting defect was reported, corrected by the lead, and rechecked; no unresolved conversion defect remains. This is conversion fidelity review, not scientific validation.

Initial reviewed draft SHA256: `d38bdbdebc3f021419ea91503321e0da124c0b2f289de9b312dba4d9afd8e995` (54,597 bytes).

Source: `XX Modeling Atomic Structure with ARKV2.pdf`; blob `05ff8bf05575e0859a5e89db233c4538e54f3827`; SHA256 `cfe6be2001ed70329cace1a53e19b4a591b3f410b888fa28624bcb3bd7311ca0`. Source title date August 16, 2025; V2 filename not asserted to be an in-document edition.

## Conversion defect and requested correction

At the end of the draft, the source p26 standalone `---` separator was joined to the p27 paragraph, producing `---This is the complete, final paper...`. Split this into `---`, blank line, then `This is the complete, final paper...`. No original words should change. The source dialogue is historical content and must remain. The lead applied this exact two-newline correction. Final boundary was inspected and independent full-text/table checks rerun successfully. Final verified SHA256: `eadc62b67c1996cd393a1ff86cd1ab055fbc9565ef862679758ca2a9e55fd229` (54,599 bytes). Reviewer made no draft edit. No other conversion defect identified.

## Independent checks actually executed

An independently written comparison extracted all pages directly from the fixed PDF using PyMuPDF, then reversed only the draft's Markdown headings/escapes, approved single footer insertion and four known scalar LaTeX displays. The entire ordered nonwhitespace stream matches exactly: **42,670 source characters = 42,670 reversed draft characters**. No drafter build, items or substitution files were used for this test. Whitespace equality alone does not catch the boundary defect above, which was found visually.

Every table row was separately parsed from source native text and compared to its draft row, preserving cell values, atomic identifiers, precision digits, signs and exponent literals. **132 rows including 7 header rows and 7 separator rows match**: 118 data rows × 5 = **590 body cells**, plus **35 header cells**. Atomic numbers 1–118 remain in order. All six table-bearing pages were also viewed cell by cell. Es (Z99, p23) was re-rendered at 288 dpi as an independent source crop; it clearly reads `1.56 × 10^{-9}`, matching the draft. No table repair or inferred rescaling performed.

Four display equations (p6 and p11) retain source `ω = 1 / cos(θᶜ)` and `kᶜ = 1 / θᶜ` using equivalent LaTeX. Other original caret/brace/underscore notation remains literal. The full code listing (pp24–25) was checked visually including indentation levels, operators and omitted comment markers. Source code was not executed or repaired. No substantive figure or diagram occurs; repeated raster copyright footer is faithfully represented once, as approved.

## Page-specific coverage

| PDF page | Independent comparison coverage |
|---|---|
| 1 | Exact title, author, AI collaborators, date, acknowledgment, abstract start, copyright footer. |
| 2 | Abstract continuation; introduction; Hψ=Eψ, α and h precision/exponents, -13.6 eV; section 1.2. |
| 3 | Aetheron radius/density/count, G units/exponents, ~880 s, repeated explanatory paragraph; section 2.1. |
| 4 | Substrat prose and analogies; section 2.2; θᶜ ratios, arctan and √(2GM/c²r) grouping. |
| 5 | Causal slope continuation; τᶜ integral, ln, kᶜ inverse, dSₜ expression and literal _prev. |
| 6 | Temporal anchor; literal asterisk note; all six recursive equations and two LaTeX displays. |
| 7 | Five derivation steps; α0.01, π/2, energy factor, eV conversion claim; stability inequalities. |
| 8 | 100,000 steps, 10^{-9}; buoyancy and shell discussion; ψ_n/E_n,1s², thermal +0.001 per10°C. |
| 9 | All seven initialization entries, literal θ^0/τ^0/k^0/ds^0/ω^0; scaling and ±0.005/1–3% values. |
| 10 | Initialization continuation; recursive update items1–2; dr/dt, perturb,screening, Z^{1/3}, error values. |
| 11 | Update items2–5, all numeric ranges; dt1e-18 labelled femtosecond unchanged; repeated scalar displays. |
| 12 | Energy equation, integral, literal indices, threshold; H/He/Li/Be/B numeric energies/error digits. |
| 13 | C–Ar and K/Ca/Fe/Au/U/Og lists, every energy/error digit and original precision. |
| 14 | Trends;screening,shell,thermal,relativistic conditions; source Z>80 claims and Z79 example retained. |
| 15 | Relativistic continuation, quantum noise, energy/unit conversion statement, accuracy claims, section4. |
| 16 | Avogadro/Hubble, enzyme, field/frequency/mass/temperature values, limitations and future work. |
| 17 | Continuation/conclusion; all five Appendix A scalar alternatives, indices, sums, integrals and units. |
| 18 | Appendix A closing prose; Appendix B introduction, Period1–2 headers and all H–F cells. |
| 19 | Ne, Period3Na–Ar, Period4K–Co; headers and all cells. |
| 20 | Ni–Kr and Period5Rb–In; headers and all cells. |
| 21 | Sn–Xe and Period6Cs–Lu; header and all cells. |
| 22 | Hf–Rn and Period7Fr–Np; header and all cells. |
| 23 | Pu–Og all cells; Es exponent independently enlarged and confirmed. |
| 24 | Original simulation preface/fence, all code lines, indentation, literals and malformed syntax. |
| 25 | Remaining code lines/fence; Appendix B notes including absolute-value bars; reference1. |
| 26 | References2–10 and second10, URLs, punctuation, separator; no correction to source numbering. |
| 27 | Complete closing historical dialogue; separate paragraph boundary restored and rechecked. |

## Original-source oddities, not conversion defects

Literal caret/braces coexist with actual Unicode superscripts and subscripts; θ^0 differs from θᶜ, ds differs from dSₜ. Original energy-unit conversion, timescale labels, calibration/parameter-free assertions, inverse-stiffness explanations and extreme precision claims are not corrected or validated. Code retains `Z (1/3)`, `(delta_theta   2)`, unmarked explanatory text and its original parameter choices. Duplicate reference number [10] and closing AI dialogue remain. These source features are not preservation blockers and do not warrant guessed repairs.
