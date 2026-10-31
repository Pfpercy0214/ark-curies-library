# Independent source verification — Paper XXV

**PASS — source-fidelity review.** No conversion defects or unresolved source-reading blockers found. This is an archival comparison, not endorsement or correction of the scientific claims.

Reviewer: transcribe_pilot_first_half (not the drafter). Review date: 2026-10-31.

- Source: `XXV-Disciplined Containment in a Scalar Medium.pdf`, complete standalone pages 1–79, Git blob `35d8f091ff634e56a176c7dc84d16406ece885e9`, source commit `110e554d944eeda6b0e14795f45a94b8a27a805e`.
- Source SHA256: `e5fea0ae671e4595598482302faf902b2bfff2d374a7a0f642b2d9019d8a22a2`.
- Reviewed draft: `draft.md`, **111693 bytes**, SHA256 **`1df23477e459905b539ae491573bf584f901e623550452961470425dcfc547f7`**. Hash rechecked after review.

## Method and coverage

Viewed and read every source page image, including every equation, scalar, numerical expression, list, citation, table cell, footer and page transition. Existing source-render cache was used for pixels; native source text was freshly extracted independently with PyMuPDF. Reversing documented LaTeX mappings and Markdown layout, normalizing whitespace/list markers, and excluding the separately checked repeated running copyright yielded **14831 source tokens and 14831 draft tokens, zero differences**. Pixel verification supplements this test and checks the meaning of the mappings rather than assuming reversibility proves correctness.

| Source pages actually viewed | Coverage and result |
| --- | --- |
| 1–4 | Title, date, author/AI variants, acknowledgments, abstract, introduction and scalar definitions; all text and notation checked. PASS. |
| 5–8 | Methodological arguments, scalar quantities and context/measurement discussion; prose and lists complete. PASS. |
| 9–12 | Neutron lifetimes, decay/context discussion and section hierarchy, including 4.4/4.6; 878 and 888 seconds unchanged. PASS. |
| 13–16 | Causal completeness, breakdowns and measurement consequences; all prose/scalar notation checked. PASS. |
| 17–20 | Section 6 and phase-boundary/identity conditions, including source Appendix A referral; all text, inequality-style conditions and lists checked. PASS. |
| 21–24 | Phase transitions and continuum opening; source 10⁻³⁶–10⁻³⁵ m and partial ℓₐ,eff typography checked. PASS. |
| 25–28 | Continuum/quantization conditions and literal underscore notation, derivative signs, κᶜ,min and ω maximum condition; all complete. PASS. |
| 29–32 | Discreteness and stability selection; full prose and lists checked. PASS. |
| 33–36 | Cosmological phase-space definitions, 5/27/68 percent and literal Ω labels; all retained. PASS. |
| 37–40 | Galaxy dynamics, acceleration/rotation and variable coupling expressions; source signs, superscript grouping, roots and literal underscore labels preserved. PASS. |
| 41–44 | SPARC procedure, predicted acceleration/velocity, asymptotic expressions and phase-regime prose; all checked. PASS. |
| 45–48 | Reinterpretation, limitations, predictions and p46 table; every table cell checked separately. PASS. |
| 49–52 | Predictions/conclusion, all 12 references, appendix overview; complete and uncorrected. PASS. |
| 53–56 | Appendix A operational scalar definitions, root/derivative expressions, stiffness proxies, tension integral, pressure and entropy definitions; exact signs, symbols and literal baseline underscores checked. PASS. |
| 57–60 | Appendix A close and B neutron model; 878/888 seconds, identity/environment definitions, decay ODE, exponential, effective lifetime and perturbation decomposition all checked. PASS. |
| 61–64 | Lifetime inequalities, first-order Γ expansion, perturbation/lifetime relations and Appendix C assumptions; overbar, subscripts, signs and literal labels checked. PASS. |
| 65–68 | Galaxy solver, stiffness constraints, boundary conditions, rotation extraction, residuals and lensing integral; all equations, conditions and prose checked. PASS. |
| 69–72 | Appendix D kernel, Newtonian/GR/quantum limits and perturbation expression; derivative orders, minus signs, groupings and source claims unchanged. PASS. |
| 73–76 | Linearized modes and Appendix E discrete-to-continuum derivation E1–E7; all indices and literal source caret/braces/underscores checked. PASS. |
| 77–79 | E8–E16, scaling arguments, variational functional, equilibrium signs and final three-part summary; full content through final sentence checked. PASS. |

## Specific preservation checks

- One distinct copyright notice is present once at opening in original wording: © Paul Frederick Percy Jr. & ‘Curie’ — ARK/Aetherwave Unified Theory 2025. Repeated source copies only are omitted. Source 2025 footer and January 28, 2026 date are not reconciled.
- Source collaborator variants GPT-5.2/GPT-5 and Grok 4/Grok remain distinct.
- One table, p46 Section 11.7: 3 columns × 6 rows including header = **18 cells**. Checked every cell against pixels, including κᶜ and θᶜ cells, exact wording and order. PASS.
- No substantive figures were visible; no missing figure assets found. Inspection cache is not a deliverable asset set.
- All 34 clear equation mappings checked against source pixels. Slash grouping and same-level c2 superscript retained. Literal square-root glyph plus parentheses is represented by `\surd` rather than guessed fraction regrouping.
- ε_created, ∫_∂Ω, κᶜ,min, Ω_eq/under/over, g_obs/g_θ/v_pred/κ_ref, τ_n, τᶜ_b, Σ_b and other baseline-label oddities remain literal, not repaired into inferred indices.
- p74 literal `e^(i ωₙ t)` is preserved; the source eigenmode factor `−(c² / κᶜ₀)` is not scientifically changed. p75–76 Σ/κ braces and nonuniform ∇d/∇_d notation remain original. p77 t_relax/c_eff/∫_V remain literal.
- Native-text equality supports absence of omitted/added wording across all 79 pages. Title, 13 main sections, 12 references, repeated appendix overview and complete Appendices A–E are present. Historical referral/overview mismatches remain source text.

No draft edits were made by this independent reviewer. No external citations were followed or rewritten; no source instruction executed. PASS applies only to the exact draft hash above.
