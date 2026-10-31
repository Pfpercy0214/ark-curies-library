# Paper V conversion audit

Status: **drafter checked; not independently verified**. No scientific assessment or correction. One complete paper, not a set of chapter files.

## Identity and provenance

- Printed title: Aetherwave Field Dynamics: Radiation, Curl, and EM Topology.
- Printed designation: `(Aetherwave Papers: V )`.
- Printed authors/date: Paul Frederick Percy Jr. & Curie GPTo, **2025**. No separate edition statement was inferred.
- Source: fixed compiled Volume 1, `Complete Aetherwave Unified Theory.pdf`, PDF pages **139–271 inclusive** (133 pages, one-based).
- Source repository commit: `110e554d944eeda6b0e14795f45a94b8a27a805e`; blob directory `c39edcd393d3d27aa6a93313e0e9b8f602c47dbf`.
- Conversion date: **2026-10-31**, distinct from original date.
- Both distinct visible copyright notices retained once at top, under owner's approved layout-only deduplication rule. No unique notice omitted.

## Method and boundaries

Native sorted PDF text supplied the starting transcription. **Every page 139–271 was rendered at 108 dpi and individually viewed**; every displayed equation, numerical expression, table row/cell and section boundary was inspected in those pixels. No scientific inference was used to fill or correct notation. There are no substantive figures on these pages; the PDF image-object inventory is also empty, but visual inspection—not that inventory alone—established figure absence. Horizontal rules are decorative separators, not omitted scientific figures. No figure assets are required.

All original prose, repetitions, recaps, placeholder discussions, references, and anomalous numbering remain in order. No generated paper summary, front matter, audit commentary or new page labels were inserted inside `draft.md`. Original wording and apparent scientific errors remain. References 1–11 are retained through p271. No newer standalone paper was substituted.

## Structural conversion

Headings become Markdown headings, bullet markers become list markers, page/line wraps become spaces, and fourteen lexical hyphen line-wrap splits are joined without removing their hyphen. Page boundaries may remain paragraph boundaries, but do not split the deliverable. Typography is conservatively simplified where it does not encode mathematical symbols. Distinct mathematical Unicode letters are retained where extraction distinguishes them. Clear short standalone equations use LaTeX; exact reversible mappings appear below. Slash divisions remain inline slash divisions, not regrouped fractions; fraction-slash glyphs are mapped to the slash operator where used in LaTeX. Literal malformed caret/underscore forms, ambiguous exponent combinations, prose-bearing formulas, and formulas with nontrivial glyph variants remain literal Unicode. Markdown escapes protect literal printed underscores from unintended emphasis.

The conversion contains **17 table segments, representing 14 logical tables**; three tables span pages 180–181, 187–188, and 232–233. Each segment retains its printed column header, including repeated continuation headers. This avoids any inference about deduplication of table content. All cells were inspected against pixels. Table-only text-layer ordering defects are corrected into their visible cells, not into new wording.

## Source-literal exceptions and preservation decisions

- pp141–142: printed `Θ^c`, `k^c`, `(ΔΘ^c)^2`, and `a_θ` include literal carets/underscores. These are retained as printed, not made conventional indices.
- pp143–146: the `sqrt(...)` notation is printed as a word; source values, scales and unit claims remain. The source's different 5000 J/500 J transformer examples are not reconciled.
- Throughout: source alternates θ/Θ, superscript-c/subscript identifiers, ASCII slash/fraction slash, lowercase/uppercase symbols, and text-literal underscores such as `Q_eff`, `J_causal`, `P_rad`, and `E_total`. No normalization of their intended meanings occurs.
- p162: prose references `(6.10.4)` within §6.9; p163 has equation label `(6.10.14)`. These are source labels and remain unchanged.
- p171: source-literal tensor `F_{μν}` remains literal; the table extraction initially displaced the underscore, and it was restored to its visually printed location. Corresponding displacement of printed underscores in pp177, 188 and 193 table cells was similarly corrected from pixels.
- p187: native sorted text interleaves the left cell's second-line word `flux` into the right cell's text. Visible table cells are “Induced voltage from changing flux” and “Induced voltage from transmitted angular acceleration”; Markdown restores that cell association. This is the sole remaining token-order difference in the reverse-format coverage comparison.
- p201: the printed transformer numerical sequence ending `≈ 1.118 × 10¹⁴ V` and its parenthetical caveat remain, without arithmetic or scientific correction.
- pp203, 259–260, 263, 265: malformed integral/summation forms with printed carets, braces and underscores are retained as literal text, including the source's `∫₀^{2π}` style and `∫_V`/`∑_i` forms; no inferred bounds or repairs.
- pp245–246: headings really read **Section 3.37** and **Section 3.38** amid the 6.x sequence. Not renumbered. §6.39 follows as printed.
- pp165 and 250: original descriptions of placeholder sections remain; no replacement text supplied.
- pp251–269: mixed superscript forms such as Sᶿ, malformed or ambiguous products/divisions, the source's alternating φ/ϕ forms, and parenthesis/grouping choices remain; ambiguous forms stay literal rather than receiving inferred LaTeX structure.
- Original cross-paper references and scientific/bibliographic statements are preserved without verification or correction. Source text that resembles a future-work instruction is documentary content, not an instruction executed by the converter.

## Coverage check

A complete reverse-format token comparison was run across all 133 pages, not a sample. It removed Markdown syntax and the approved repeated notices, reversed each exact LaTeX mapping, normalized whitespace and fraction-slash typography, and joined the fourteen source line-wrap hyphens. Both native text and reversed draft contain **27,779 tokens**. The sole diff is the p187 `flux` table-cell ordering correction described above. No other omitted, added or reordered text tokens were found. The footer notice is visually verified and added once because it is not emitted by the native extraction. Equal token coverage is not by itself visual or mathematical verification; it supplements the page inspection.

Exact remaining coverage diff:

```diff
--- 

+++ 

@@ -10974,12 +10974,12 @@

 voltage
 from
 changing
+flux
 Induced
 voltage
 from
 transmitted
 angular
-flux
 acceleration
 Mutual
 inductance
```

## Page-specific visual coverage

Every row below denotes an actual rendered-page inspection, covering all prose, inline/display math, numerical values, headers/footers and any table cells on that page. “Continuation” means the printed section continues across the page; it does not indicate omitted content. Equation labels are recorded literally as extracted, including source inconsistencies.

| PDF page | Printed headings / boundary evidence | Equation labels / table coverage |
| --- | --- | --- |
| 139 | Introduction – Aetherwave Field Dynamics | Inline/display expressions and prose inspected |
| 140 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 141 | Section 6.1: Physical Interpretation of Magnetic Tension in the Substrat; 6.1.1 Magnetic Dipoles and Torsion in the Substrat; 6.1.2 Magnetic Induction as Stored Strain Energy | (6.1.1) |
| 142 | 6.1.3 Field Lines as Tension Vectors; 6.1.4 Collapse and Snapback; 6.1.5 Summary | (6.1.2), (6.1.3) |
| 143 | Section 6.2 and the voltage derivation in Section 6.3. Magnetic induction is no longer; RECAP: Section 6.2: Predictive Derivation of Causal Slope in Magnetic Systems; 6.2.1 Energy Equivalence and Scaling Law | Inline/display expressions and prose inspected |
| 144 | 6.2.2 Flux, Geometry, and Causal Coupling | Inline/display expressions and prose inspected |
| 145 | 6.2.3 Validation Across Systems; 6.2.4 Quantum Considerations | Inline/display expressions and prose inspected |
| 146 | 6.2.5 Summary and Implications; RECAP: Section 6.3: Derivation of Induced Voltage from Substrat Acceleration; 6.3.1 Angular Acceleration and Substrat Response | (6.3.1), (6.3.2), (6.3.3) |
| 147 | 6.3.2 Physical Interpretation; 6.3.3 Scaling Behavior | (6.3.4), (6.3.5), (6.3.6) |
| 148 | 6.3.4 Reconciliation with Classical Faraday Law; 6.3.5 Summary | (6.3.7), (6.3.8), (6.3.9), (6.3.10), (6.3.11) |
| 149 | Section 6.4: Displacement Current and Substrat Oscillation Dynamics; 6.4.1 Classical Displacement Current; 6.4.2 Substrat Interpretation of ∂E/∂t; 6.4.3 Substrat Wave Propagation | (6.4.1), (6.4.2), (6.4.3), (6.4.4) |
| 150 | 6.4.4 Deriving the Displacement Term; 6.4.5 Physical Interpretation; 6.4.6 Summary | (6.4.5), (6.4.6), (6.4.7), (6.4.8), (6.4.9) |
| 151 | Section 6.5: Substrat-Based Radiation Emission and the Origins of Electromagnetic Waves; 6.5.1 Overview and Motivation; 6.5.2 Oscillatory Torsion in the Substrat | Inline/display expressions and prose inspected |
| 152 | 6.5.3 Substrat Radiation Flux and Energy Transport; 6.5.4 Dipole Radiation and the Far Field Limit | Inline/display expressions and prose inspected |
| 153 | 6.5.5 Radiation Impedance and Wave Behavior; 6.5.6 Photon Emission as Quantized Substrat Oscillation; 6.5.7 Summary | Inline/display expressions and prose inspected |
| 154 | Section 6.6 — Substrat Mutual Inductance and Torsion Coupling | Inline/display expressions and prose inspected |
| 155 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 156 | Section 6.7 — Maxwell Curl Laws in Substrat Form | Inline/display expressions and prose inspected |
| 157 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 158 | Section 6.8: Substrat-Based Electromagnetic Radiation and Dipole Emission; 6.8.1 Classical Radiation Overview; 6.8.2 Substrat Oscillation and Radiative Emission | (6.8.1) |
| 159 | 6.8.3 Electric Dipole as Substrat Oscillator; 6.8.4 Radiated Power from Substrat Dynamics | (6.8.2), (6.8.3), (6.8.4), (6.8.5), (6.8.6) |
| 160 | 6.8.5 Directionality and Polarization; 6.8.6 Summary | (6.8.7), (6.8.8) |
| 161 | Section 6.9: Deriving Maxwell’s Equations from Substrat Dynamics; 6.9.1 Classical Overview of Maxwell’s Curl Equations; 6.9.2 Substrat Behavior: Angular Strain Fields | (6.9.1), (6.9.2), (6.9.3), (6.9.4) |
| 162 | 6.9.3 Reconstructing Faraday's Law; 6.9.4 Reconstructing Ampère’s Law with Displacement Current | (6.9.3), (6.10.4), (6.9.5), (6.9.6), (6.9.7), (6.9.8), (6.9.9), (6.9.10), (6.9.4), (6.9.11), (6.9.12) |
| 163 | 6.9.5 Summary of Field Correspondence; 6.9.6 Implications for Unified Theory | (6.9.13), (6.10.14), (6.9.15), (6.9.16), (6.9.17); table: 4 data rows × 2 columns, plus headers |
| 164 | Section 6.10 — Temporal Elasticity and the Delayed Response of Causal Fields; Section 6.11 — Coherence and Angular Mode Locking in EM Systems | Inline/display expressions and prose inspected |
| 165 | Section 6.12 — Angular Field Propagation in Synthetic Structures; Section 6.13: Displacement Current and Maxwell’s Completion via Substrat Strain; 6.13.1 Classical Background: Maxwell’s Fix to Ampère’s Law | (6.13.1), (6.13.2) |
| 166 | 6.13.2 Aetherwave Interpretation of Displacement Current; 6.13.3 Deriving Displacement Current from θᶜ Dynamics | (6.13.3), (6.13.4), (6.13.5) |
| 167 | 6.13.4 Physical Visualization: Capacitor Charging | (6.13.6), (6.13.7), (6.13.8), (6.13.9), (6.13.10) |
| 168 | 6.13.5 Connection to Electromagnetic Waves; 6.13.6 Summary; Section 6.14: Substrat Standing Waves and Photonic Quantization; 6.14.1 Motivation: From Classical Fields to Photons | (6.13.11); table: 4 data rows × 2 columns, plus headers |
| 169 | 6.14.2 Standing Waves in the Substrat | (6.14.1), (6.14.2), (6.14.3), (6.14.4), (6.14.5), (6.14.6), (6.14.7) |
| 170 | 6.14.3 Angular Momentum and Spin-1 Behavior; 6.14.4 Connection to Aharonov–Bohm Effect; 6.14.5 Emergence of the Electromagnetic Field Tensor | (6.14.8) |
| 171 | 6.14.6 Summary; Section 6.15: Mutual Inductance and Substrat Coupling; 6.15.1 Classical Background | (6.14.9), (6.14.10), (6.15.1); table: 6 data rows × 2 columns, plus headers |
| 172 | 6.15.2 Substrat Interpretation of Mutual Inductance; 6.15.3 Causal Coupling Equation | (6.15.2), (6.15.3) |
| 173 | 6.15.4 Deriving the Mutual Coupling Coefficient; 6.15.5 Energy Transfer Between Substrat Domains | (6.15.4), (6.15.5), (6.15.6), (6.15.7), (6.15.8), (6.15.9) |
| 174 | 6.15.6 Coherent Field Coupling and Substrat Continuity; 6.15.7 Summary; Section 6.16: Electromagnetic Radiation from θᶜ Oscillation; 6.16.1 Classical Context | Inline/display expressions and prose inspected; table: 5 data rows × 2 columns, plus headers |
| 175 | 6.16.2 Aetherwave Interpretation: Substrat Oscillations as Radiation Source; 6.16.3 Derivation of Radiated Power | (6.16.1), (6.16.2), (6.16.3) |
| 176 | 6.16.4 Radiation Pattern and Propagation | (6.16.4), (6.16.5), (6.16.6), (6.16.7), (6.16.8), (6.16.9) |
| 177 | 6.16.5 Implications for Antennas and Photons; 6.16.6 Relation to Maxwell and Quantum Formalism; 6.16.7 Summary | (6.16.10); table: 5 data rows × 2 columns, plus headers |
| 178 | Section 6.17: Maxwell’s Equations as Emergent Substrat Dynamics; 6.17.1 Objective; 6.17.2 The Substrat View: Tension, Curl, and Momentum Flow | (6.17.1), (6.17.2) |
| 179 | 6.17.3 Faraday’s Law from Substrat Curl; 6.17.4 Ampère-Maxwell Law from Angular Acceleration | (6.17.3), (6.17.1), (6.17.2), (6.17.4), (6.17.5), (6.17.6), (6.17.7) |
| 180 | 6.17.5 Gauss’s Law and Magnetic Monopoles; 6.17.6 Unification Recap | (6.17.6), (6.17.7), (6.17.1), (6.17.8), (6.17.9), (6.17.10); table: 2 data rows × 3 columns, plus headers |
| 181 | 6.17.7 Conclusion; Section 6.18: Substrat Model of Current and Charge Flow; 6.18.1 Objective; 6.18.2 Physical Model of Current | (6.18.1); table: 3 data rows × 3 columns, plus headers |
| 182 | 6.18.3 Charge Density from Substrat Divergence | (6.18.2), (6.18.3), (6.18.4) |
| 183 | 6.18.4 Interpretation: Aetherwave Charge as Angular Source; 6.18.5 Current-Driven Magnetic Fields | (6.18.5), (6.18.6), (6.18.7), (6.18.8), (6.18.9) |
| 184 | 6.18.6 Summary Table: Substrat Interpretations; 6.18.7 Closing Remarks; Section 6.19: Mutual Induction and Substrat Coherence in Transformers; 6.19.1 Overview | Inline/display expressions and prose inspected; table: 4 data rows × 3 columns, plus headers |
| 185 | 6.19.2 Causal Mechanism of Substrat Coupling | (6.19.1), (6.19.2), (6.19.3), (6.19.4) |
| 186 | 6.19.3 Geometry of Coherence; 6.19.4 Example Calculation | (6.19.5), (6.19.6), (6.19.7), (6.19.8) |
| 187 | 6.19.5 Mutual Angular Momentum Transfer; 6.19.6 Summary and Significance | (6.19.9), (6.19.10), (6.19.11), (6.19.12); table: 2 data rows × 2 columns, plus headers |
| 188 | Section 6.20: Radiative Emission from Oscillating Substrat Tension; 6.20.1 Overview; 6.20.2 Dipole Oscillation and Angular Emission | (6.20.1), (6.20.2); table: 2 data rows × 2 columns, plus headers |
| 189 | 6.20.3 Energy Density and Power Flow; 6.20.4 Far-Field Radiation and Angular Distribution | (6.20.3), (6.20.4), (6.20.5), (6.20.6), (6.20.7), (6.20.8) |
| 190 | 6.20.5 Relation to Photons and Quantization; 6.20.6 Summary; Section 6.21: Emergence of Maxwell’s Equations from Substrat Dynamics; 6.21.1 Overview | (6.20.9), (6.20.10) |
| 191 | 6.21.2 Substrat Flow and Causal Curl; 6.21.3 Ampère’s Law from θᶜ Acceleration | (6.21.1), (6.21.2), (6.21.3) |
| 192 | Continuation; all content inspected | (6.21.4), (6.21.5), (6.21.6), (6.21.7), (6.21.8), (6.21.9) |
| 193 | 6.21.4 Faraday’s Law from Substrat Snapback; 6.21.5 Summary of Correspondence; 6.21.6 Outlook: Recovering the Full Set | (6.21.10), (6.21.11), (6.21.12); table: 6 data rows × 2 columns, plus headers |
| 194 | Section 6.22: Field Quantization and Photon Emergence from θᶜ Nodes; 6.22.1 Overview; 6.22.2 Substrat Standing Waves and Photon Quantization | Inline/display expressions and prose inspected |
| 195 | 6.22.3 Field Line Quantization and Nodal Geometry | (6.22.1), (6.22.2), (6.22.3), (6.22.4), (6.22.5) |
| 196 | 6.22.4 Aharonov-Bohm Effects from Substrat Geometry; 6.22.5 Photons as Solitary Wave Modes | (6.22.6), (6.22.7), (6.22.8), (6.22.9) |
| 197 | 6.22.6 Summary and Quantum Correspondence; Section 6.23: Mutual Inductance and Causal Field Coupling Between Coils; 6.23.1 Overview | (6.22.10), (6.22.11); table: 6 data rows × 2 columns, plus headers |
| 198 | 6.23.2 Classical Mutual Inductance; 6.23.3 Causal Strain Transfer in the Substrat | (6.23.1), (6.23.2) |
| 199 | 6.23.4 Link to Classical Mutual Inductance | (6.23.3), (6.23.4), (6.23.5), (6.23.6), (6.23.7) |
| 200 | 6.23.5 Geometric and Material Effects; 6.23.6 Transformer Case Study | (6.23.8), (6.23.9), (6.23.10) |
| 201 | 6.23.7 Substrat Continuity and Energy Conservation | (6.23.11), (6.23.12), (6.23.13), (6.23.14), (6.23.15) |
| 202 | 6.23.8 Summary; Section 6.24: Electromagnetic Radiation from High-Frequency Substrat Oscillations; 6.24.1 Overview; 6.24.2 Oscillating Dipoles as Strain Sources | Inline/display expressions and prose inspected |
| 203 | 6.24.3 Deriving the Radiated Power | (6.24.1), (6.24.2), (6.24.3), (6.24.4), (6.24.5) |
| 204 | 6.24.4 Time-Averaged Energy Transfer; 6.24.5 Conditions for Radiation | (6.24.6), (6.24.7), (6.24.8), (6.24.9) |
| 205 | 6.24.6 Comparison with Classical Radiation; 6.24.7 Summary; Section 6.25: Derivation of ∇×𝐄 and ∇×𝐁 from Time-Varying Substrat Torsion; 6.25.1 Overview | Inline/display expressions and prose inspected; table: 5 data rows × 2 columns, plus headers |
| 206 | 6.25.2 Substrat Flow Geometry and Angular Torsion; 6.25.3 Deriving ∇×𝐄 = −∂𝐁/∂t | (6.25.1) |
| 207 | 6.25.4 Deriving ∇×𝐁 = μ₀𝐉 + μ₀ε₀ ∂𝐄/∂t | (6.25.2), (6.25.3), (6.25.4) |
| 208 | 6.25.5 Summary of Causal Curl Laws; Section 6.26: Quantized Substrat Oscillation and the Nature of Photons; 6.26.1 Overview | (6.25.5), (6.25.6), (6.25.7), (6.25.8); table: 3 data rows × 2 columns, plus headers |
| 209 | 6.26.2 Standing Wave Oscillation in θᶜ | (6.26.1), (6.26.2) |
| 210 | 6.26.3 Quantization from Substrat Energy Response; 6.26.4 Causal Mechanics Behind the Photon | (6.26.3), (6.26.4) |
| 211 | 6.26.5 The Aharonov-Bohm Effect and θᶜ Potentials; 6.26.6 Summary | (6.26.5), (6.26.6) |
| 212 | Section 6.27: Mutual Inductance and Substrat Coupling Between Coils; 6.27.1 Overview; 6.27.2 Classical Definition of Mutual Inductance | (6.27.1), (6.27.2) |
| 213 | 6.27.3 Substrat Interpretation of Mutual Inductance | (6.27.3), (6.27.4), (6.27.5), (6.27.6), (6.27.7), (6.27.8) |
| 214 | 6.27.4 Geometry of Substrat Coupling; 6.27.5 Transformer Behavior and Directionality | (6.27.9) |
| 215 | 6.27.6 Summary; Section 6.28: Radiation Emission from Substrat Oscillation; 6.28.1 Overview; 6.28.2 Classical Radiation from an Oscillating Dipole | (6.28.1) |
| 216 | 6.28.3 Substrat Oscillation as Radiation Source; 6.28.4 Energy Flux and Radiation Power | (6.28.2), (6.28.3), (6.28.4), (6.28.5), (6.28.6) |
| 217 | 6.28.5 Wave Equation from Substrat Mechanics | (6.28.7), (6.28.8), (6.28.9), (6.28.10), (6.28.11), (6.28.12) |
| 218 | 6.28.6 Polarization and Directionality; 6.28.7 Connection to Photons and Quantization | (6.28.13), (6.28.14) |
| 219 | 6.28.8 Summary; Section 6.29: Substrat Strain Fields Near Magnetized Objects and Field Lines; 6.29.1 Overview; 6.29.2 Magnetic Dipoles as Strain Sources | Inline/display expressions and prose inspected |
| 220 | 6.29.3 Mapping Substrat Curvature; 6.29.4 Substrat Curl and Field Lines | (6.29.1), (6.29.2), (6.29.3) |
| 221 | 6.29.5 Force on a Moving Charge; Section 5), yielding a Lorentz-like force:; 6.29.6 Energy Localization and Field Lines | (6.29.4), (6.29.5), (6.29.6), (6.29.7) |
| 222 | 6.29.7 Substrat Strain Topology; 6.29.8 Summary | Inline/display expressions and prose inspected |
| 223 | Section 6.30: Mutual Inductance and Field Coupling Through the Substrat; 6.30.1 Overview; 6.30.2 Classical Mutual Inductance; 6.30.3 Aetherwave Derivation | (6.30.1), (6.30.2) |
| 224 | 6.30.4 Propagation Through the Substrat | (6.30.3), (6.30.4), (6.30.5) |
| 225 | 6.30.5 Coupling Efficiency and Alignment; 6.30.6 Energy Transfer and Substrat Mediation; 6.30.7 Recasting Classical Mutual Inductance | (6.30.6), (6.30.7) |
| 226 | 6.30.8 Summary | (6.30.8), (6.30.9) |
| 227 | Section 6.31: Electromagnetic Radiation as Oscillation of Substrat Strain; 6.31.1 Overview; 6.31.2 Classical Background; 6.31.3 Substrat Origin of EM Radiation | (6.31.1), (6.31.2), (6.31.3) |
| 228 | 6.31.4 Energy and Power in Radiation; 6.31.5 Deriving Dipole Emission | (6.31.4), (6.31.5), (6.31.6), (6.31.7), (6.31.8), (6.31.9) |
| 229 | 6.31.6 Photons as Substrat Packets | (6.31.10), (6.31.11), (6.31.12), (6.31.13), (6.31.14) |
| 230 | 6.31.7 Comparison to Classical Theory; 6.31.8 Summary; Section 6.32: Connecting Maxwell’s Equations to Causal Slope Geometry | Inline/display expressions and prose inspected; table: 5 data rows × 2 columns, plus headers |
| 231 | 6.32.1 Overview; 6.32.2 Torsional Geometry of θᶜ Fields | (6.32.1), (6.32.2) |
| 232 | 6.32.3 Displacement Current and Ampère's Law; 6.32.4 Physical Interpretation | (6.32.3), (6.32.4), (6.32.1), (6.32.5), (6.32.6); table: 2 data rows × 2 columns, plus headers |
| 233 | 6.32.5 Unified Wave Equation; 6.32.6 Summary | (6.32.7), (6.32.8), (6.32.9); table: 2 data rows × 2 columns, plus headers |
| 234 | Section 6.33: Radiation Pressure, Polarization, and the Causal Poynting Vector; 6.33.1 Overview; 6.33.2 Causal Strain Waves and Propagation | (6.33.1), (6.33.2), (6.33.3) |
| 235 | 6.33.3 Direction of Energy Flow; 6.33.4 Radiation Pressure and Momentum | (6.33.4), (6.33.5), (6.33.6), (6.33.7), (6.33.8) |
| 236 | 6.33.5 Polarization as Directional Angular Strain; 6.33.6 Summary; Section 6.34: Quantized Substrat Modes and Photons; 6.34.1 Overview | (6.33.9) |
| 237 | 6.34.2 Standing Wave Quantization in θᶜ | (6.34.1), (6.34.2), (6.34.3), (6.34.4) |
| 238 | 6.34.3 Aharonov–Bohm and Causal Flow; 6.34.4 Quantized Field Lines and Photons | (6.34.5), (6.34.6), (6.34.7) |
| 239 | 6.34.5 Implications for Quantum Electrodynamics (QED); 6.34.6 Summary; Section 6.35: Mutual Induction and Causal Field Coupling; 6.35.1 Overview | (6.34.8), (6.35.1) |
| 240 | 6.35.2 Substrat Coupling Geometry; 6.35.3 Derivation of Mutual Voltage from θᶜ Coupling | (6.35.2), (6.35.3), (6.35.4) |
| 241 | 6.35.4 Transformer Geometry and Causal Efficiency; 6.35.5 Causal Continuity and Energy Transfer | (6.35.5), (6.35.6) |
| 242 | 6.35.6 Summary; Section 6.36: Radiation Emission and Oscillating Causal Slope; 6.36.1 Overview; 6.36.2 Oscillating Dipoles as θᶜ Sources | Inline/display expressions and prose inspected |
| 243 | 6.36.3 Substrat Wave Propagation; 6.36.4 Radiated Power and Energy Transport | (6.36.1), (6.36.2), (6.36.3) |
| 244 | 6.36.5 Directionality and Polarization; 6.36.6 Radiation from Accelerated Charges | (6.36.4), (6.36.5), (6.36.6) |
| 245 | 6.36.7 Coherence and Wave Quantization; 6.36.8 Summary; Section 3.37 — Tension Residuals in Large-Scale Structure Formation | Inline/display expressions and prose inspected |
| 246 | Section 3.38 — Shear and Torsion in Cosmic Filament Networks; Section 6.39: Radiation Emission from Oscillating Causal Slope; 6.39.1 Classical Electromagnetic Radiation; 6.39.2 Causal Oscillation and Radiation | (6.39.1), (6.39.2) |
| 247 | 6.39.3 Power of Radiated Substrat Waves; 6.39.4 Dipole Radiation from Causal Oscillation | (6.39.3), (6.39.4), (6.39.5) |
| 248 | 6.39.5 Poynting Vector and Energy Flux Analogy; 6.39.6 Quantum Implications: Photons and Quantization | (6.39.6), (6.39.7), (6.39.5), (6.39.8), (6.39.9), (6.39.10) |
| 249 | 6.39.7 Experimental Signatures; 6.39.8 Summary | Inline/display expressions and prose inspected |
| 250 | Section 6.40 — Energy Localization in Complex Substrat Networks; SECTION 6.41 — Substrat-Based Radiation Behavior | Inline/display expressions and prose inspected |
| 251 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 252 | SECTION 6.42 — Substrat-Based Antenna Emission and Classical Radiation Analogy | Inline/display expressions and prose inspected |
| 253 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 254 | SECTION 6.43 — Standing Waves, Resonance, and Angular Energy Confinement | Inline/display expressions and prose inspected |
| 255 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 256 | SECTION 6.44 — Substrat Tunneling and Phase-Coupled Cavities | Inline/display expressions and prose inspected |
| 257 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 258 | SECTION 6.45 — Angular Momentum Quantization from Substrat Waveforms | Inline/display expressions and prose inspected |
| 259 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 260 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 261 | SECTION 6.46 — Interference and Coherence of Confined Angular Modes | Inline/display expressions and prose inspected |
| 262 | SECTION 6.47 — Field Compression, Nodal Entrapment, and Emergent Mass Effects | Inline/display expressions and prose inspected |
| 263 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 264 | SECTION 6.48 — Dynamic Substrat Curvature and Energy-Momentum Conservation | Inline/display expressions and prose inspected |
| 265 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 266 | SECTION 6.49 — Cosmological Structure and Substrat Tension Networks | Inline/display expressions and prose inspected |
| 267 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 268 | SECTION 6.50 — Unified Scalar Framework of Matter, Motion, and Curvature | Inline/display expressions and prose inspected |
| 269 | Continuation; all content inspected | Inline/display expressions and prose inspected |
| 270 | References | Inline/display expressions and prose inspected |
| 271 | Continuation; all content inspected | Inline/display expressions and prose inspected |

## Output integrity

- `draft.md` bytes: 200545
- `draft.md` SHA-256: `19265b1dad7763a0c46427887f397fb630d6c667b14062aa973fcb5680da2f24`
- Source PDF SHA-256: `f8cb4138423587ce313dd6c44a0d141946570a2f9006eadfaac18d18cc761b6c`
- Figure/crop manifest: empty (no substantive figures).
- Independent verification: pending separate reviewer.

## Reversible math-encoding record

Keys are exact LaTeX strings; values are their source strings. This is conversion evidence outside the paper, not an alternate scientific formulation.

```json
{
  "E = \\frac{1}{2}k^{c}(\\Delta \\theta ^{c})^{2}": "E = ½kᶜ(Δθᶜ)²",
  "E = \\frac{1}{2} \\times  (4 \\times  10^{8}) \\times  (0.005)^{2} E \\approx  5000 J": "E = ½ × (4 × 10⁸) × (0.005)² E ≈ 5000 J",
  "E = \\frac{1}{2} \\times  (7.3 \\times  10^{69}) \\times  (\\pi /2)^{2} E \\approx  9 \\times  10^{69} J": "E = ½ × (7.3 × 10⁶⁹) × (π⁄2)² E ≈ 9 × 10⁶⁹ J",
  "E = (1/2) \\times  L \\times  I^{2}": "E = (1/2) × L × I²",
  "E = (1/2) \\times  k^{c} \\times  (\\Delta \\theta ^{c})^{2}": "E = (1/2) × kᶜ × (Δθᶜ)²",
  "L \\approx  (\\mu _{0} \\times  N^{2} \\times  A) / l": "L ≈ (μ₀ × N² × A) / l",
  "\\Delta \\theta ^{c} = \\alpha  \\times  N \\times  I \\times  f_{s}": "Δθᶜ = α × N × I × fₛ",
  "\\Delta \\theta ^{c} = n \\times  \\theta _{0}": "Δθᶜ = n × θ₀",
  "E = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c})^{2}": "E = (1/2) · kᶜ · (Δθᶜ)²",
  "\\nabla  \\times  B = \\mu _{0} \\cdot  J + \\mu _{0} \\cdot  \\varepsilon _{0} \\cdot  \\partial E/\\partial t (6.4.1)": "∇ × B = μ₀ · J + μ₀ · ε₀ · ∂E/∂t (6.4.1)",
  "E \\propto  \\nabla \\theta ^{c} (6.4.2)": "E ∝ ∇θᶜ (6.4.2)",
  "\\partial E/\\partial t \\propto  \\partial \\nabla \\theta ^{c}/\\partial t = \\nabla (\\partial \\theta ^{c}/\\partial t) (6.4.3)": "∂E/∂t ∝ ∂∇θᶜ/∂t = ∇(∂θᶜ/∂t) (6.4.3)",
  "\\partial ^{2}\\theta ^{c}/\\partial t^{2} = c^{2} \\cdot  \\nabla ^{2}\\theta ^{c} (6.4.4)": "∂²θᶜ/∂t² = c² · ∇²θᶜ (6.4.4)",
  "\\theta ^{c}(x, t) = A \\cdot  \\sin(kx - \\omega t) (6.4.5)": "θᶜ(x, t) = A · sin(kx − ωt) (6.4.5)",
  "\\partial \\theta ^{c}/\\partial t = -A \\cdot  \\omega  \\cdot  \\cos(kx - \\omega t) (6.4.6)": "∂θᶜ/∂t = −A · ω · cos(kx − ωt) (6.4.6)",
  "\\theta ^{c}(t) = \\theta _{0} \\cdot  \\cos(\\omega t)": "θᶜ(t) = θ₀ · cos(ωt)",
  "\\theta ^{c}(t, r) = (\\theta _{0}/r) \\cdot  \\cos(\\omega t - kr)": "θᶜ(t, r) = (θ₀⁄r) · cos(ωt − kr)",
  "E = \\hbar  \\cdot  \\omega  = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c})^{2}": "E = ℏ · ω = (1⁄2) · kᶜ · (Δθᶜ)²",
  "P = (\\mu _{0} \\cdot  q^{2} \\cdot  a^{2}) / (6\\pi  \\cdot  c)": "P = (μ₀ · q² · a²) / (6π · c)",
  "\\nabla ^{2}\\theta ^{c} - (1/c^{2}) \\cdot  \\partial ^{2}\\theta ^{c}/\\partial t^{2} = 0": "∇²θᶜ − (1/c²) · ∂²θᶜ/∂t² = 0",
  "U = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c})^{2}": "U = (1⁄2) · kᶜ · (Δθᶜ)²",
  "P \\propto  q^{2} \\cdot  a^{2} / (c \\cdot  \\mu _{0})": "P ∝ q² · a² ⁄ (c · μ₀)",
  "\\nabla  \\times  E \\propto  \\nabla  \\times  (\\partial \\theta ^{c}/\\partial t)": "∇ × E ∝ ∇ × (∂θᶜ⁄∂t)",
  "\\nabla  \\times  E \\propto  \\partial (\\nabla  \\times  \\theta ^{c})/\\partial t": "∇ × E ∝ ∂(∇ × θᶜ)⁄∂t",
  "\\nabla  \\times  \\theta ^{c} \\propto  B": "∇ × θᶜ ∝ B",
  "\\nabla  \\times  E \\propto  \\partial B/\\partial t": "∇ × E ∝ ∂B⁄∂t",
  "\\nabla  \\times  E = -\\partial B/\\partial t": "∇ × E = −∂B⁄∂t",
  "\\nabla  \\times  B = \\mu _{0}\\varepsilon _{0} \\partial E/\\partial t + \\mu _{0} J": "∇ × B = μ₀ε₀ ∂E⁄∂t + μ₀ J",
  "\\nabla  \\times  B \\propto  \\nabla  \\times  (\\nabla  \\times  \\theta ^{c})": "∇ × B ∝ ∇ × (∇ × θᶜ)",
  "\\nabla  \\times  (\\nabla  \\times  \\theta ^{c}) = \\nabla (\\nabla  \\cdot  \\theta ^{c}) - \\nabla ^{2}\\theta ^{c}": "∇ × (∇ × θᶜ) = ∇(∇ · θᶜ) − ∇²θᶜ",
  "\\nabla  \\times  B \\propto  -\\nabla ^{2}\\theta ^{c}": "∇ × B ∝ −∇²θᶜ",
  "\\nabla ^{2}\\theta ^{c} \\propto  \\partial ^{2}\\theta ^{c}/\\partial t^{2}": "∇²θᶜ ∝ ∂²θᶜ⁄∂t²",
  "\\nabla  \\times  B \\propto  \\partial E/\\partial t": "∇ × B ∝ ∂E⁄∂t",
  "\\nabla  \\times  B = \\mu _{0} \\cdot  J": "∇ × B = μ₀ · J",
  "\\nabla  \\times  B = \\mu _{0} \\cdot  (J + \\varepsilon _{0} \\cdot  \\partial E/\\partial t)": "∇ × B = μ₀ · (J + ε₀ · ∂E/∂t)",
  "\\theta ^{c} = \\arccos(\\Delta \\tau  / \\Delta t)": "θᶜ = arccos(Δτ / Δt)",
  "\\omega ^{c} = \\partial \\theta ^{c} / \\partial t": "ωᶜ = ∂θᶜ / ∂t",
  "\\nabla  \\times  B \\propto  \\omega ^{c}": "∇ × B ∝ ωᶜ",
  "\\partial ^{2}\\theta ^{c} / \\partial t^{2} - v^{2} \\cdot  \\nabla ^{2}\\theta ^{c} = 0": "∂²θᶜ / ∂t² − v² · ∇²θᶜ = 0",
  "\\theta ^{c}(x, t) = \\theta _{0} \\cdot  \\sin(kx - \\omega t)": "θᶜ(x, t) = θ₀ · sin(kx − ωt)",
  "\\theta ^{c}(x, t) = A \\cdot  \\sin(kx) \\cdot  \\sin(\\omega t)": "θᶜ(x, t) = A · sin(kx) · sin(ωt)",
  "L^{c} = I^{c} \\cdot  \\omega ^{c} = \\hbar ": "Lᶜ = Iᶜ · ωᶜ = ℏ",
  "V_{2} = -M \\cdot  (dI_{1} / dt)": "V₂ = −M · (dI₁ / dt)",
  "\\Delta \\theta ^{c}_{2} = K_{12} \\cdot  \\Delta \\theta ^{c}_{1}": "Δθᶜ₂ = K₁₂ · Δθᶜ₁",
  "V_{2} = \\xi  \\cdot  Q \\cdot  K_{12} \\cdot  d^{2}\\theta ^{c}_{1} / dt^{2}": "V₂ = ξ · Q · K₁₂ · d²θᶜ₁ / dt²",
  "E_{1} = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c}_{1})^{2}": "E₁ = (1/2) · kᶜ · (Δθᶜ₁)²",
  "E_{2} = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c}_{2})^{2} = (1/2) \\cdot  k^{c} \\cdot  (K_{12} \\cdot  \\Delta \\theta ^{c}_{1})^{2} = (1/2) \\cdot  k^{c} \\cdot  K_{12}^{2} \\cdot  (\\Delta \\theta ^{c}_{1})^{2}": "E₂ = (1/2) · kᶜ · (Δθᶜ₂)² = (1/2) · kᶜ · (K₁₂ · Δθᶜ₁)² = (1/2) · kᶜ · K₁₂² · (Δθᶜ₁)²",
  "\\eta  = E_{2} / E_{1} = K_{12}^{2}": "η = E₂ / E₁ = K₁₂²",
  "P \\propto  (\\mu _{0} \\cdot  I_{0}^{2} \\cdot  \\omega ^{4} \\cdot  L^{2}) / (6\\pi  \\cdot  c^{3})": "P ∝ (μ₀ · I₀² · ω⁴ · L²) / (6π · c³)",
  "\\theta ^{c}(t) = \\theta _{0} \\cdot  \\sin(\\omega t)": "θᶜ(t) = θ₀ · sin(ωt)",
  "E \\equiv  -\\xi _{1} \\cdot  \\partial \\theta ^{c} / \\partial t (6.17.2) B \\equiv  \\xi _{2} \\cdot  (\\nabla  \\times  \\theta ^{c})": "E ≡ −ξ₁ · ∂θᶜ / ∂t (6.17.2) B ≡ ξ₂ · (∇ × θᶜ)",
  "\\nabla  \\times  E = -\\partial B / \\partial t": "∇ × E = −∂B / ∂t",
  "\\nabla  \\times  E = -\\xi _{1} \\nabla  \\times  (\\partial \\theta ^{c} / \\partial t) = -\\xi _{1} \\partial (\\nabla  \\times  \\theta ^{c}) / \\partial t = -\\partial B / \\partial t": "∇ × E = −ξ₁ ∇ × (∂θᶜ / ∂t) = −ξ₁ ∂(∇ × θᶜ) / ∂t = −∂B / ∂t",
  "\\nabla  \\times  B = \\mu _{0}J + \\mu _{0}\\varepsilon _{0} \\partial E / \\partial t": "∇ × B = μ₀J + μ₀ε₀ ∂E / ∂t",
  "\\nabla  \\times  B = \\xi _{2} \\nabla  \\times  (\\nabla  \\times  \\theta ^{c})": "∇ × B = ξ₂ ∇ × (∇ × θᶜ)",
  "\\nabla  \\times  B = -\\xi _{2} \\nabla ^{2}\\theta ^{c}": "∇ × B = −ξ₂ ∇²θᶜ",
  "\\partial ^{2}\\theta ^{c} / \\partial t^{2} = -(k^{c} / \\rho _{s}) \\nabla ^{2}\\theta ^{c}": "∂²θᶜ / ∂t² = −(kᶜ / ρₛ) ∇²θᶜ",
  "\\nabla  \\times  B = (\\xi _{2} \\cdot  \\rho _{s} / k^{c}) \\cdot  \\partial ^{2}\\theta ^{c} / \\partial t^{2}": "∇ × B = (ξ₂ · ρₛ / kᶜ) · ∂²θᶜ / ∂t²",
  "\\nabla  \\times  B = (\\xi _{2} \\cdot  \\rho _{s} / (k^{c} \\cdot  \\xi _{1})) \\cdot  \\partial E / \\partial t": "∇ × B = (ξ₂ · ρₛ / (kᶜ · ξ₁)) · ∂E / ∂t",
  "\\mu _{0}\\varepsilon _{0} = \\xi _{2} \\cdot  \\rho _{s} / (k^{c} \\cdot  \\xi _{1})": "μ₀ε₀ = ξ₂ · ρₛ / (kᶜ · ξ₁)",
  "\\nabla  \\cdot  B = \\nabla  \\cdot  (\\nabla  \\times  \\theta ^{c}) = 0": "∇ · B = ∇ · (∇ × θᶜ) = 0",
  "J = \\rho  \\cdot  v": "J = ρ · v",
  "J \\equiv  \\kappa  \\cdot  (\\theta ^{c} \\times  \\nabla \\theta ^{c})": "J ≡ κ · (θᶜ × ∇θᶜ)",
  "\\nabla  \\cdot  E = \\rho  / \\varepsilon _{0}": "∇ · E = ρ / ε₀",
  "E = -\\xi _{1} \\cdot  \\partial \\theta ^{c} / \\partial t": "E = −ξ₁ · ∂θᶜ / ∂t",
  "\\nabla  \\cdot  E = -\\xi _{1} \\cdot  \\nabla  \\cdot  (\\partial \\theta ^{c} / \\partial t)": "∇ · E = −ξ₁ · ∇ · (∂θᶜ / ∂t)",
  "\\rho  = -\\varepsilon _{0} \\xi _{1} \\cdot  \\nabla  \\cdot  (\\partial \\theta ^{c} / \\partial t)": "ρ = −ε₀ ξ₁ · ∇ · (∂θᶜ / ∂t)",
  "B = \\xi _{2} (\\nabla  \\times  \\theta ^{c})": "B = ξ₂ (∇ × θᶜ)",
  "\\nabla  \\times  B = \\xi _{2} (\\nabla  \\times  (\\nabla  \\times  \\theta ^{c}))": "∇ × B = ξ₂ (∇ × (∇ × θᶜ))",
  "\\theta _{2}^{c}(t) \\approx  \\chi  \\cdot  \\theta _{1}^{c}(t - \\Delta t)": "θ₂ᶜ(t) ≈ χ · θ₁ᶜ(t − Δt)",
  "V_{2} \\propto  I_{1} \\cdot  (dI_{1} / dt)": "V₂ ∝ I₁ · (dI₁ / dt)",
  "\\theta ^{c}(x, t) = \\theta _{0} \\cdot  \\sin(\\omega t - kr)": "θᶜ(x, t) = θ₀ · sin(ωt − kr)",
  "E = \\frac{1}{2} \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c})^{2}": "E = ½ · kᶜ · (Δθᶜ)²",
  "u(r, t) = \\frac{1}{2} \\cdot  k^{c} \\cdot  (\\theta _{0} \\cdot  \\sin(\\omega t - kr))^{2}": "u(r, t) = ½ · kᶜ · (θ₀ · sin(ωt − kr))²",
  "\\langle u\\rangle  = \\frac{1}{4} \\cdot  k^{c} \\cdot  \\theta _{0}^{2}": "⟨u⟩ = ¼ · kᶜ · θ₀²",
  "E = \\frac{1}{2} \\cdot  k^{c} \\cdot  (\\partial \\theta ^{c} / \\partial t)^{2} \\cdot  V": "E = ½ · kᶜ · (∂θᶜ / ∂t)² · V",
  "\\theta ^{c}(x, t) = \\theta _{0} \\cdot  \\sin(kx) \\cdot  \\cos(\\omega t)": "θᶜ(x, t) = θ₀ · sin(kx) · cos(ωt)",
  "E = \\frac{1}{2} \\cdot  k^{c} \\cdot  \\theta _{0}^{2} \\cdot  V": "E = ½ · kᶜ · θ₀² · V",
  "E = h \\cdot  f": "E = h · f",
  "\\theta ^{c}(x, t) = 0": "θᶜ(x, t) = 0",
  "\\theta ^{c}_{n}(x, t) = \\theta _{0} \\cdot  \\sin(n\\pi x / L) \\cdot  \\cos(\\omega t)": "θᶜₙ(x, t) = θ₀ · sin(nπx / L) · cos(ωt)",
  "E_{n} = n \\cdot  h \\cdot  f": "Eₙ = n · h · f",
  "M = \\mu _{0} \\cdot  N_{1} \\cdot  N_{2} \\cdot  A / l": "M = μ₀ · N₁ · N₂ · A / l",
  "\\Delta \\theta ^{c}_{2}(t) \\approx  \\alpha  \\cdot  \\Delta \\theta ^{c}_{1}(t - d / c)": "Δθᶜ₂(t) ≈ α · Δθᶜ₁(t − d / c)",
  "\\theta ^{c}(t, r) \\approx  \\theta _{0} \\cdot  \\sin(\\omega t - kr) \\cdot  \\cos(\\varphi )": "θᶜ(t, r) ≈ θ₀ · sin(ωt − kr) · cos(φ)",
  "\\varepsilon  = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c})^{2}": "ε = (1/2) · kᶜ · (Δθᶜ)²",
  "S = \\varepsilon  \\cdot  c = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c})^{2} \\cdot  c": "S = ε · c = (1/2) · kᶜ · (Δθᶜ)² · c",
  "\\theta ^{c}(t) = \\theta _{0} \\cdot  \\sin(\\omega t) \\Rightarrow  \\omega ^{c}(t) = \\theta _{0} \\cdot  \\omega  \\cdot  \\cos(\\omega t)": "θᶜ(t) = θ₀ · sin(ωt) ⇒ ωᶜ(t) = θ₀ · ω · cos(ωt)",
  "\\nabla  \\times  (\\partial \\theta ^{c} / \\partial t) = \\partial  / \\partial t (\\nabla  \\times  \\theta ^{c})": "∇ × (∂θᶜ / ∂t) = ∂ / ∂t (∇ × θᶜ)",
  "\\varepsilon _{0} \\propto  1 / (k^{c} \\cdot  c^{2})": "ε₀ ∝ 1 / (kᶜ · c²)",
  "\\theta ^{c}(x, t) = A \\cdot  \\sin(kx - \\omega t)": "θᶜ(x, t) = A · sin(kx − ωt)",
  "\\partial ^{2}\\theta ^{c} / \\partial x^{2} = (1 / v^{2}) \\cdot  \\partial ^{2}\\theta ^{c} / \\partial t^{2}": "∂²θᶜ / ∂x² = (1 / v²) · ∂²θᶜ / ∂t²",
  "\\Delta \\phi  = (e / \\hbar ) \\oint  A \\cdot  dl": "Δϕ = (e / ℏ) ∮ A · dl",
  "A \\propto  \\nabla \\theta ^{c}": "A ∝ ∇θᶜ",
  "V_{2} \\propto  -Q_{2} \\cdot  C_{12} \\cdot  I_{1} \\cdot  (dI_{1} / dt)": "V₂ ∝ −Q₂ · C₁₂ · I₁ · (dI₁ / dt)",
  "d(t) = d_{0} \\cdot  \\sin(\\omega t)": "d(t) = d₀ · sin(ωt)",
  "P \\propto  (q \\cdot  d_{0} \\cdot  \\omega ^{2})^{2} / c^{3}": "P ∝ (q · d₀ · ω²)² / c³",
  "|E| \\propto  \\sin(\\theta ) / r, |B| \\propto  |E| / c": "|E| ∝ sin(θ) / r, |B| ∝ |E| / c",
  "\\theta ^{c}(t, r) = \\theta _{0} \\cdot  \\sin(\\omega t - kr)": "θᶜ(t, r) = θ₀ · sin(ωt − kr)",
  "S = E \\cdot  v = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c})^{2} \\cdot  c": "S = E · v = (1/2) · kᶜ · (Δθᶜ)² · c",
  "\\langle S\\rangle  = (1/4) \\cdot  k^{c} \\cdot  \\theta _{0}^{2} \\cdot  c": "⟨S⟩ = (1/4) · kᶜ · θ₀² · c",
  "P = 4\\pi r^{2} \\cdot  \\langle S\\rangle  = \\pi  \\cdot  r^{2} \\cdot  k^{c} \\cdot  \\theta _{0}^{2} \\cdot  c": "P = 4πr² · ⟨S⟩ = π · r² · kᶜ · θ₀² · c",
  "\\partial ^{2}\\theta ^{c} / \\partial t^{2} = v^{2} \\cdot  \\nabla ^{2}\\theta ^{c}": "∂²θᶜ / ∂t² = v² · ∇²θᶜ",
  "\\partial ^{2}E / \\partial t^{2} = c^{2} \\cdot  \\nabla ^{2}E": "∂²E / ∂t² = c² · ∇²E",
  "E = \\hbar  \\cdot  \\omega ": "E = ℏ · ω",
  "\\theta ^{c}(r) = \\theta _{0} \\cdot  \\cos(\\theta ) / r^{3}": "θᶜ(r) = θ₀ · cos(θ) / r³",
  "T^{c}(r) = \\nabla \\theta ^{c}(r)": "Tᶜ(r) = ∇θᶜ(r)",
  "\\nabla  \\times  T^{c} = \\nabla  \\times  (\\nabla \\theta ^{c}) = 0": "∇ × Tᶜ = ∇ × (∇θᶜ) = 0",
  "F = q \\cdot  (v \\times  B^{c}) = q \\cdot  (v \\times  \\nabla  \\times  A^{c})": "F = q · (v × Bᶜ) = q · (v × ∇ × Aᶜ)",
  "F = q(E + v \\times  B)": "F = q(E + v × B)",
  "E^{c}(r) = (1/2) \\cdot  k^{c} \\cdot  (\\theta ^{c}(r))^{2}": "Eᶜ(r) = (1/2) · kᶜ · (θᶜ(r))²",
  "\\Delta \\theta ^{c}_{2}(t) \\approx  G(r_{12}) \\cdot  \\Delta \\theta ^{c}_{1}(t - \\tau )": "Δθᶜ₂(t) ≈ G(r₁₂) · Δθᶜ₁(t − τ)",
  "E_{2} = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c}_{2})^{2}": "E₂ = (1/2) · kᶜ · (Δθᶜ₂)²",
  "\\langle E\\rangle  = (1/4) \\cdot  k^{c} \\cdot  \\theta _{0}^{2}": "⟨E⟩ = (1/4) · kᶜ · θ₀²",
  "P \\propto  q^{2} \\cdot  a^{2}": "P ∝ q² · a²",
  "\\theta ^{c}(r, t) = (\\theta _{0} / r) \\cdot  \\sin(\\omega t - kr)": "θᶜ(r, t) = (θ₀ / r) · sin(ωt − kr)",
  "S^{c} = (1/\\mu ^{c}) \\cdot  (\\partial \\theta ^{c}/\\partial t)^{2}": "Sᶜ = (1/μᶜ) · (∂θᶜ/∂t)²",
  "\\theta ^{c}_{n}(x, t) = A_{n} \\cdot  \\sin(k_{n}x) \\cdot  \\sin(\\omega _{n}t)": "θᶜₙ(x, t) = Aₙ · sin(kₙx) · sin(ωₙt)",
  "\\nabla  \\times  (\\nabla  \\times  \\theta ^{c}) = \\mu _{0}\\varepsilon _{0} \\cdot  \\partial ^{2}\\theta ^{c}/\\partial t^{2}": "∇ × (∇ × θᶜ) = μ₀ε₀ · ∂²θᶜ/∂t²",
  "\\theta ^{c}(x, t) = \\theta _{0} \\cdot  \\sin(n \\cdot  \\pi x / L) \\cdot  \\cos(\\omega _{n}t)": "θᶜ(x, t) = θ₀ · sin(n · πx / L) · cos(ωₙt)",
  "E = \\frac{1}{2} \\cdot  k^{c} \\cdot  (\\theta _{0})^{2}": "E = ½ · kᶜ · (θ₀)²",
  "E_{n} \\propto  \\omega _{n} \\Rightarrow  E_{n} = \\hbar  \\cdot  \\omega _{n}": "Eₙ ∝ ωₙ ⇒ Eₙ = ℏ · ωₙ",
  "E = h \\cdot  f = \\hbar  \\cdot  \\omega ": "E = h · f = ℏ · ω",
  "\\Delta \\varphi  = \\oint  A \\cdot  dl = \\oint  \\theta ^{c} \\cdot  dl": "Δφ = ∮ A · dl = ∮ θᶜ · dl",
  "\\Delta \\theta ^{c} = \\theta _{0} \\cdot  \\sin(\\pi x / L)": "Δθᶜ = θ₀ · sin(πx / L)",
  "\\theta ^{c}(x, t) = \\theta ^{c}_{1}(x, t) + \\theta ^{c}_{2}(x, t)": "θᶜ(x, t) = θᶜ₁(x, t) + θᶜ₂(x, t)",
  "V_{2} \\propto  -dI_{1}/dt": "V₂ ∝ −dI₁/dt",
  "\\theta ^{c}(t) = \\theta _{0} \\cdot  \\sin(2\\pi ft)": "θᶜ(t) = θ₀ · sin(2πft)",
  "u = (1/2) \\cdot  k^{c} \\cdot  (\\Delta \\theta ^{c})^{2}": "u = (1/2) · kᶜ · (Δθᶜ)²",
  "\\theta ^{c}(t) \\propto  \\int  (v \\times  a) \\cdot  dt": "θᶜ(t) ∝ ∫ (v × a) · dt",
  "S = (1 / \\mu _{0}) \\cdot  (E \\times  B)": "S = (1 / μ₀) · (E × B)",
  "S^{c} = (1 / k^{c}) \\cdot  (\\partial \\theta ^{c} / \\partial t \\times  \\partial \\theta ^{c} / \\partial x)": "Sᶜ = (1 / kᶜ) · (∂θᶜ / ∂t × ∂θᶜ / ∂x)",
  "\\partial ^{2}\\theta ^{c}/\\partial t^{2} = v_{s}^{2} \\nabla ^{2}\\theta ^{c}": "∂²θᶜ/∂t² = vₛ² ∇²θᶜ",
  "\\theta ^{c}(x, t) = \\theta _{0} \\cdot  \\cos(kx - \\omega t)": "θᶜ(x, t) = θ₀ · cos(kx − ωt)",
  "\\theta ^{c}(z, t) = \\theta _{0} \\cdot  \\sin(kz) \\cdot  \\cos(\\omega t)": "θᶜ(z, t) = θ₀ · sin(kz) · cos(ωt)",
  "\\partial \\theta ^{c}/\\partial t = -\\theta _{0}\\omega  \\cdot  \\sin(kz) \\cdot  \\sin(\\omega t)": "∂θᶜ⁄∂t = −θ₀ω · sin(kz) · sin(ωt)",
  "\\nabla \\theta ^{c} = \\theta _{0}k \\cdot  \\cos(kz) \\cdot  \\cos(\\omega t)": "∇θᶜ = θ₀k · cos(kz) · cos(ωt)",
  "\\partial ^{2}\\theta ^{c}/\\partial t^{2} = -\\theta _{0}\\omega ^{2} \\cdot  \\sin(kz) \\cdot  \\cos(\\omega t)": "∂²θᶜ⁄∂t² = −θ₀ω² · sin(kz) · cos(ωt)",
  "= -(1/\\mu _{0}) \\cdot  \\theta _{0}^{2}\\omega k \\cdot  \\sin(kz) \\cdot  \\cos(kz) \\cdot  \\sin(\\omega t) \\cdot  \\cos(\\omega t)": "= −(1⁄μ₀) · θ₀²ωk · sin(kz) · cos(kz) · sin(ωt) · cos(ωt)",
  "\\sin(2x) = 2 \\cdot  \\sin(x) \\cdot  \\cos(x)": "sin(2x) = 2 · sin(x) · cos(x)",
  "P \\propto  \\theta _{0}^{2}\\omega ^{2}k^{2}L^{2}/\\mu _{0}c": "P ∝ θ₀²ω²k²L²⁄μ₀c",
  "\\theta ^{c}(x, t) = \\theta _{0} \\cdot  \\sin(n\\pi x/L) \\cdot  \\cos(\\omega _{n}t)": "θᶜ(x, t) = θ₀ · sin(nπx⁄L) · cos(ωₙt)",
  "\\partial ^{2}\\theta ^{c}/\\partial t^{2} = v_{s}^{2} \\cdot  \\partial ^{2}\\theta ^{c}/\\partial x^{2}": "∂²θᶜ⁄∂t² = vₛ² · ∂²θᶜ⁄∂x²",
  "\\Delta f = v_{s}/(2L)": "Δf = vₛ⁄(2L)",
  "J^{c} = -\\kappa  \\cdot  \\partial \\theta ^{c}/\\partial t \\cdot  \\Delta \\theta ^{c}": "Jᶜ = −κ · ∂θᶜ/∂t · Δθᶜ",
  "\\theta ^{c}(\\varphi , t) = \\theta _{0} \\cdot  \\sin(m\\varphi ) \\cdot  \\cos(\\omega _{m}t)": "θᶜ(φ, t) = θ₀ · sin(mφ) · cos(ωₘt)",
  "\\theta ^{c}(\\varphi  + 2\\pi , t) = \\theta ^{c}(\\varphi , t)": "θᶜ(φ + 2π, t) = θᶜ(φ, t)",
  "\\partial \\theta ^{c}/\\partial t = -\\theta _{0}\\omega _{m} \\cdot  \\sin(m\\varphi ) \\cdot  \\sin(\\omega _{m}t)": "∂θᶜ/∂t = −θ₀ωₘ · sin(mφ) · sin(ωₘt)",
  "\\theta ^{c}_{1}(\\varphi , t) = \\theta _{0} \\cdot  \\sin(m\\varphi ) \\cdot  \\cos(\\omega _{1}t) \\theta ^{c}_{2}(\\varphi , t) = \\theta _{0} \\cdot  \\sin(m\\varphi  + \\delta ) \\cdot  \\cos(\\omega _{2}t + \\varphi )": "θᶜ₁(φ, t) = θ₀ · sin(mφ) · cos(ω₁t) θᶜ₂(φ, t) = θ₀ · sin(mφ + δ) · cos(ω₂t + φ)",
  "\\partial \\Delta \\theta ^{c}/\\partial t = 0": "∂Δθᶜ⁄∂t = 0",
  "\\theta ^{c}(r, t) = \\theta _{0} \\cdot  \\sin(n\\pi r / R) \\cdot  \\cos(\\omega _{n}t), 0 \\le  r \\le  R": "θᶜ(r, t) = θ₀ · sin(nπr ⁄ R) · cos(ωₙt), 0 ≤ r ≤ R",
  "\\varepsilon ^{c}(r) = (1/2) \\cdot  k^{c} \\cdot  [ (\\partial \\theta ^{c}/\\partial t)^{2} + v_{s}^{2} \\cdot  (\\nabla \\theta ^{c})^{2} ]": "εᶜ(r) = (1⁄2) · kᶜ · [ (∂θᶜ⁄∂t)² + vₛ² · (∇θᶜ)² ]",
  "\\partial \\varepsilon ^{c}/\\partial t + \\nabla  \\cdot  S^{c} = 0": "∂εᶜ⁄∂t + ∇ · Sᶜ = 0",
  "J^{c} = -k^{c} \\nabla (\\partial \\theta ^{c}/\\partial t)": "Jᶜ = −kᶜ ∇(∂θᶜ⁄∂t)"
}
```

## Independent-review corrections (2026-10-31)

Restored independent equation boundaries identified by the independent reviewer: p140 transformer and cosmic-stretch calculations each now have separate equality and approximation displays; p178 labeled E definition (6.17.2) and subsequent B definition separated; p261 independent θᶜ₁ and θᶜ₂ mode equations separated. No symbols, numerical values, or prose changed. Earlier reverse-map entries represent normalized whitespace and therefore remain usable after collapsing display boundaries.

Current corrected draft: 200573 bytes; SHA256 `699ebc5af2ebf6a23229d47b5cfdb52b46d78f10237a0f2e12eb4dacac4792e9`. Prior hash above superseded. Reviewer recheck pending.

Reviewer label placement follow-up: (6.17.2) moved from E expression to standalone label preceding B, matching source; (6.17.1) remains before E. Current draft 200575 bytes; SHA256 `784397f49f6105a9b850de3440a16e0cd7db80d069df8b76c53c13dd55198066`.
