# Paper I: source-backed mathematical semantics inventory

## Result and scope

**Practical preservation result: no newly dropped or changed source mathematics was found in the current assembled draft.** Its unusual original forms are preserved; the user need not repair the original physics to archive this text. Content/glyph fidelity is not equivalent to uniquely parseable mathematical meaning. Several original expressions cannot be assigned one mathematical syntax tree without assumptions. Retaining their exact text is appropriate archival behavior, but describing all their mathematics as unambiguously machine-parseable would be incorrect.

This inventory follows a complete reread of the mathematical content in the assembled draft, the previous independent visual reading of **all PDF pages 7–52**, and source-text cross-checks. Earlier full-page pixel inspection remains the authority for superscript placement and corrupt glyphs (particularly pp21, 31–32, 43–45 and 50–51). It inventories every identified occurrence of malformed/mixed literal notation, ambiguous grouping, and materially inconsistent symbol/unit conventions in Paper I, not merely representative examples. It is not an exhaustive scientific critique or a claim that undeclared physics has been resolved.

Source: compiled PDF blob `c39edcd393d3d27aa6a93313e0e9b8f602c47dbf`, SHA-256 `f8cb4138423587ce313dd6c44a0d141946570a2f9006eadfaac18d18cc761b6c`. Page numbers below are **physical PDF page positions**.

Reviewed draft: `investigations/conversions/paper-001/draft.md`, SHA-256 `b2b53855a34301c8930c2e24e469f0e53a3bf819ee941d9e5bdb714b0e81a8be`. Line numbers are 1-based and specific to this hash. Exact raw lines in the occurrence appendix include Markdown escapes, which are not printed source backslashes. Literal source backslash sequences are separately identified below.

Copyright-notice consolidation is now explicitly user-approved and is not a remaining blocker. Human-oriented rendering is not a requirement of this review.

## 1. Source-literal notation and identifier ambiguity

| ID | PDF pages / draft lines | Exact source form(s) | What is unresolved; lossless treatment |
|---|---|---|---|
| S01 | 7–8,10,12 / 31,39,43,119,173 | `θc\θᶜ` | Duplicated baseline/superscript symbol and literal backslash. Preserve literal sequence; do not choose one theta or treat backslash as division. |
| S02 | 8 / 41 | `kckᶜ` | Duplicated stiffness spelling. Preserve as an opaque source token, not a product or corrected identifier. |
| S03 | 8 / 43 | `Gμν(eff)G^{(eff)}_{\μ\ν}` | Juxtaposed spellings and malformed TeX escapes. No justified unique tensor identifier or index tree. Preserve literal; record no canonical interpretation. |
| S04 | 7,9,31–33,38,40,52 / 17,99,859,875,919,927,1087,1093,1095,1135,1570 | `Gᵉᶠᶠ_μν`, `G_μν`, `K_μν`, `T_μν` | Source prints literal underscores while eff is raised. They suggest indices, but their exact syntax is not formal TeX. Do not silently substitute inferred tensor indices or equate with corrupt later G. Raw Markdown `\_` is an escape layer only. |
| S05 | 9 / 99 | `\u3000Gᵉᶠᶠ_μν = αK_μν + βT_μν` | Visible backslash-u characters are not Unicode whitespace and must not be decoded away. Preserve opaque prefix separately from equation tokens. |
| S06 | 12–13 / 160,213 | `Rμν`; `Gμν = Rμν − ½Rgμν = κTμν` | Baseline Greek letters are not printed subscripts. Identifier-vs-product/index interpretation must remain unspecified rather than cosmetically repaired. |
| S07 | 18–19 / 387,389,393,395,397,401,405,407,415,417 | `Θ^c`, `ΔΘ^c`, `k^c`, `(ΔΘ^c)^2`, `d^2Θ^c / dt^2`, `a_θ` | Literal caret notation and uppercase Theta are genuine. Derivative convention can be recognized in a separate reading, but archival bytes do not justify changing case, deleting carets, or globally aliasing these with lowercase θᶜ. |
| S08 | 21–22 / 492,551; 23–25 / 575,643,647,661,673 | `Φᴮ` versus `Φ_B`, `dΦ_B` | Raised B versus literal underscore-B. Preserve distinct source spellings; do not automatically classify B as numerical exponent or infer a single canonical flux identifier. |
| S09 | 21 / 512,518 | `μₑff`, `αₑff` | Only e is lowered; ff remains baseline. Draft `\mu_e\mathrm{ff}` / `\alpha_e\mathrm{ff}` preserves typography but a symbolic parser may read multiplication by ff. Lossless surface encoding is possible; unique identifier segmentation is not established. |
| S10 | 23–25 / 589,593,601,621,623,657,659,661,669,677 | `a_θ` | Literal underscore. Source defines angular acceleration, so a human-level name is given, but converting the underscore to a formal subscript is an interpretation layer, not the literal record. |
| S11 | 29 / 793,795,797,799,801 | `kᶜ_slope`, `kᶜ_torsion`, `kᶜ_shear`, `kᶜ_stretch`, `kᶜ_compress` | Literal word suffixes, distinct from malformed subscript strings later. No global alias map to pp44–45 may be asserted without a documented assumption. |
| S12 | 31 / 859,863 | `∂_μθᶜ`, `∂_νθᶜ`, `g_μν`, `∂^σθᶜ`, `∂_σθᶜ` | Printed underscore/caret mixed with superscript c. Preserve operator glyphs and literal punctuation; formal index attachment is not uniquely machine-specified. |
| S13 | 43 / 1225 | `\u03b8ᶜ` | Visible escape text in heading, not a decoded theta. Preserve exact text. |
| S14 | 43–44 / 1257,1261 | `Gᵎʳᵒ`; `Gᵎʳᵒ = ∂ᵒθᶜ · ∂ᵎθᶜ − ½ · gᵎᵒ (∂ˢθᶜ · ∂ˢθᶜ)` | G/derivative/metric superscripts are visibly damaged. Exact glyph sequences can be encoded, but their intended indices cannot be reconstructed from the source alone. Do not replace with μ,ν,σ or the p31 tensor. |
| S15 | 44–45 / 1295,1299,1301,1305,1307,1311,1313,1317,1319,1323,1327 | `kᶜₛₒₚₙₑ`, `kᶜₜₒₚₜₒₓ`, `kᶜₛₐₒₐₐ`, `kᶜₛₐₒₐₐₜₐₜₐ`, `kᶜₜₐₒₒₐₐₐ`, `kᶜₜₐₒₒₐ` | Six visibly malformed labels, repeated in equations/composite. Preserve every spelling independently; English mode headings do not authorize correcting index strings. |
| S16 | 45 / 1311,1317 | `Δxₛₒₜ`, `Δθᶜₛₐₒₐₐ` | Malformed displacement/angle subscripts. Preserve exact indices, not guessed lat/shear labels. |
| S17 | 50 / 1480 | `Universal Energy EuEᵤ` | Duplicated identifier in heading. Do not delete Eu or interpret as multiplication. |
| S18 | 50–51 / 1504,1510,1514,1516,1522,1524,1530,1534,1538,1544,1548,1552,1558 | `d_c`, `τ_c`, `k_c`, `k_c(L)` | Literal underscores, unlike superscript c elsewhere. Current Markdown escapes underscore for display. Preserve these distinct labels; no automatic alias to τᶜ or kᶜ. |

## 2. Operators and grouping: source ambiguity versus faithful syntax

| ID | Source page / draft line(s) | Source expression | Source-backed assessment |
|---|---|---|---|
| G01 | 31 / 849 | `V(θᶜ) = –(3⁄8) · (kᶜ · θᶜ²) / x²` | The raised c and 2 are adjacent without explicit grouping. Is this square of the labeled causal slope or a combined exponent? The source's later p44 `(θᶜ)²` is different and cannot silently resolve it. Preserve `θᶜ²` and mark unresolved. |
| G02 | 51 / 1548,1552 | `k_c = (2 × τ_c) ÷ Δθᶜ²`; `k_c = (2 × Eᵤ) ÷ (Δθᶜ² × d_c)` | Same adjacent superscript ambiguity, plus whether Δ belongs to the squared quantity. Contrast explicit `(Δθᶜ)²` in p51's earlier formula (line1530); do not add parentheses to harmonize. |
| G03 | 32 / 900 | `θᶜ ≈ √(2GM / c²r)` | Root's argument is delimited, but slash followed by adjacent c²r has competing informal precedence conventions. Preserve the slash sequence. Do not rewrite as `2GM/(c²r)` or `(2GM/c²)r` without an assumption. G and M adjacency convention is likewise an implicit product, not a named symbol definition supplied by an AST. |
| G04 | 32 / 906 | `dθᶜ/dx ≈ –GM / c²r²` | Same denominator ambiguity; retain flat slash and both powers. Do not infer denominator braces from expected physics. |
| G05 | 22 / 551 | `Φᴮ ≈ n × (h / 2e) ≈ n × 2.068 × 10⁻¹⁵ Wb` | Outer parentheses do not disambiguate inner `h / 2e` between denominator 2e and divide-by-2 then times e under different grammars. Do not repair using remembered flux-quantum physics. |
| G06 | 21 / 518 | `sqrt(μᵣ × μ₀ / kᶜ)` | Under a declared conventional multiply/divide grammar this is unambiguous; no missing denominator term. The unresolved point is the label `μₑff`, not the arithmetic scope. |
| G07 | 25 / 647,657 | `μ₀ · N · A / l · dI/dt`; `I · dI/dt` | Conventional derivative/product reading available; a generic programming parser without derivative grammar will not recover it. Preserve sequence and provide grammar metadata, not a scientific rewrite. |
| G08 | 31,44 / 882,1272 | Source field evolution equations | Four additive terms and parentheses retained; p31 explicitly has `∂V(θᶜ)/∂θᶜ`, p44 has `(∂V/∂θᶜ)`. Do not make them byte-identical or supply missing functional dependence in p44. Derivative notation needs a declared grammar; mathematical semantics remains unvalidated. |
| G09 | 46 / 1358 | `V ∝ 5 × 10⁶ volts per displaced coulomb` | Proportionality is not equality and does not specify a proportionality constant or a complete prediction. Exact wording and ∝ preserved. |
| G10 | 16 / 312 | `Δθᶜ = |θᶜ₊ − θᶜ₋|` | Matched vertical bars and plus/minus endpoint indices visually confirmed; no unresolved conversion issue. A semantic encoding can explicitly record absolute value and endpoint indices, while retaining c as source label. |
| G11 | 25 / 652 | `(6.3.9) Δθᶜ = √(μ₀ · N² · A · I²/(l · kᶜ))` | Denominator parentheses and root argument are explicit. Current LaTeX preserves them; no missing power or sign. |

`=` / `≈` / `∝`, integral and differential symbols, multiplication dots/crosses, ± endpoint signs, square-root/function spelling, and every visible coefficient/exponent remain distinct. A source glyph-preserving record can tokenize all of these without assigning disputed scope. Many other expressions are conventionally parseable, but TeX itself is a presentation language rather than an executable mathematical contract.

## 3. Units, definitions, and numerical statements: retain, do not reconcile

These are **source statements**, not newly diagnosed conversion defects. An arithmetic expression may have a clear syntactic tree while its printed result or units conflict; parsing does not mean validating.

- **p12 / lines145–154:** GPS altitude 20,200 km, timing 45.9 microseconds/day, `arccos(1 − 5.2 × 10⁻¹⁰) ≈ 0.000001 radians` retained. Do not recompute the RHS in archival text.
- **pp15,17 / lines270–276,336–342:** `kᶜ ≈ 4 × 10⁸ N·rad⁻²`, 0.005 radians and 5000 J retained; cosmic pp17/28 values remain 7.3 × 10⁶⁹ N·rad⁻² and 9 × 10⁶⁹ J.
- **pp20–21 / lines454,471,498:** stiffness N·rad⁻² and μ₀ ≈1.257×10⁻⁶ H/m; fₛ dimension m¹/², α dimension **m⁻¹/²·A⁻¹**. The minus missing in first transcription was a conversion defect already fixed; current source and draft agree.
- **p22 / lines525–551:** all nine system energy/angle pairs and repeated SQUID value remain; µJ micro-sign versus μ Greek mu is a Unicode-level distinction, not authorization to change units/values. They can be recorded as literal unit strings.
- **p24 / lines603,613–625:** ξ ≈5×10⁶ V/C; Δt=1 ms=1×10⁻³ s; Q=.01 C; `a_θ=5×10³ rad/s²`; the source product's result `2.5×10⁵ V` and prose 250 kV remain despite apparent arithmetic inconsistency. Label the printed equality as source assertion; do not silently evaluate/replace it. `(cf. Page 31)` is an original internal reference, not a reliable compiled-PDF position mapping.
- **p28 / lines757–761:** local 10⁸–10⁹, astrophysical 10⁵²–10⁶⁰ and cosmic 7.3×10⁶⁹ N·rad⁻² retained.
- **pp45–46 / lines1347–1358:** table's 5000 J, .005 rad, .005 s, 4×10⁸ N·rad⁻² and subsequent 200 rad/s², ∝5×10⁶ volts per displaced coulomb retained. All 12 cells and three column labels are present.
- **p48 / lines1425–1436:** Eₛ and stiffness unit J·rad⁻² / kg·m²·s⁻²·rad⁻², optional `1 Kc`, unlike earlier N·rad⁻². Do not force dimensional consistency or equate Kc with an exponent expression.
- **p49 / lines1453–1474:** τᶜ=E/d, N, kg·m/s² and optional N/rad retained. τ also names proper-time increments and torque elsewhere; scope must remain local rather than a global symbol table alias.
- **pp50–51 / lines1487–1558:** 4.35×10¹⁷ s, 1.57×10⁷⁰ J, 1.616×10⁻³⁵ m, 1.21×10⁴⁴ N and 1.94×10¹⁰⁵ J·rad⁻² retained with original chain. Do not reconcile their magnitudes, dimensions or `Eᵤ=τ_c×d_c` against other statements.
- **Cross-section symbol labels:** superscript c generally labels causal quantities, while baseline c in Appendix B is speed of light; a parser must not treat every `^c` as exponentiation by speed of light. α is a coil-coupling coefficient (p21), a tensor scaling weight (p38), and a domain curvature-symmetry factor (pp51–52); source does not establish a universal alias. τ/τᶜ/τ_c, θ/Θ, Φ/Φᴮ/Φ_B and kᶜ/k_c variants need scoped identities or explicitly unresolved alias records. A repeated glyph alone is not proof of one variable.

## 4. Conversion defects and machine-readable encoding recommendation

**Current confirmed conversion defects: none newly found.** Earlier missing p21 exponent minus and stray backticks inside TeX blocks were fixed before this hash. The original report's content-fidelity conclusion remains, but it must not be expanded into a claim of unique mathematical interpretation.

Optional future aid, not a condition of preserving the original text: a source-linked JSON inventory with `source_page`, `draft_line`, `exact_source_text`, `exact_draft_text`, `representation` (TeX/literal Unicode), `notation_scope`, `parse_status`, and `ambiguity_ids`. For damaged expressions use `parse_status: source_ambiguous` and `semantic_ast: null`. For straightforward expressions a separately declared conventional grammar can supply an AST; retain the exact original and distinguish interpretation from transcription. Do not add speculative repaired equations or rewrite original values. Explicitly decode only **Markdown** escapes in a derived reader, never source `\u3000` / `\u03b8` strings. Preserve Unicode code points and superscript/subscript attachment in the literal layer; normalize only in a separate reversible field.

A lossless **surface** encoding is achievable. A lossless **intended mathematical meaning** for every source expression is not presently achievable from this PDF alone. Only if a future task asks to resolve intended mathematical meaning, S03, S14–S16 and G01–G05 would require author clarification or explicitly authorized editorial interpretation. That is **not** a prerequisite for this faithful archival conversion and is not requested here. A machine parser should return unresolved nodes, not guesses. An AI reader can be informed of uncertainty; it cannot honestly be guaranteed to infer missing intended indices/grouping.

## 5. Exact occurrence appendix

The following is the occurrence-level inventory underlying the families above. Exact raw draft lines are included to avoid relying only on illustrative snippets. Lines may contain multiple affected forms. Markdown backticks/escapes are shown literally. Source page assignments refer to the relevant expression, including page-spanning paragraphs.

### PDF page 7

Line 17:

```text
Building from scalar foundations, we derived an effective gravitational tensor `Gᵉᶠᶠ_μν` that mirrors general relativity in weak fields while revealing deeper causal structures. This framework challenges over a century of tensor-based physics without discarding the phenomenological accuracy of Einstein's model.
```

Line 31:

```text
3.  Defining `θc\θᶜ`: The Temporal Slope
```

### PDF page 8

Line 39:

```text
7.  Antimatter and Temporal Inversion in `θc\θᶜ`
```

Line 41:

```text
8.  Scale-Dependent Stiffness: Local vs Cosmic kckᶜ
```

Line 43:

```text
9.  Predictive Gravitation Tensor `Gμν(eff)G^{(eff)}_{\μ\ν}` from `θc\θᶜ`
```

### PDF page 9

Line 99:

```text
`\u3000Gᵉᶠᶠ_μν = αK_μν + βT_μν`
```

### PDF page 10

Line 119:

```text
In the next section, we mathematically define `θc\θᶜ`, and show how this scalar alone encodes the curvature responsible for energy storage, gravitational behavior, and the collapse or expansion of time itself.
```

### PDF page 12

Line 154:

```text
\theta^c \approx \arccos(1 - 5.2 \times 10^{-10}) \approx 0.000001\ \text{radians}
```

Line 160:

```text

```

Line 173:

```text
In the following section, we explore how these gradients in `θc\θᶜ` give rise to gravitational dynamics, and how energy storage is encoded within these curvatures as substrat tension.
```

### PDF page 13

Line 213:

```text
`Gμν = Rμν − ½Rgμν = κTμν`
```

### PDF page 18

Line 387:

```text
`(6.1.1) Θ^c = arccos(Δτ / Δt)`
```

Line 389:

```text
Here, Δτ is the local proper time experienced along the path of causal propagation, and Δt is the coordinate time interval as measured externally. A nonzero `Θ^c` indicates a deviation in the expected causal direction due to strain in the substrat.
```

Line 393:

```text
This torsional deformation accumulates when a current persists in a coil, especially in inductive geometries with high turns (N), cross-sectional area (A), and low effective length (l). The net result is a measurable angular displacement `ΔΘ^c`, which stores energy according to the Substrat Energy Response (SER) law:
```

### PDF page 19

Line 395:

```text
`(6.1.2) E = (1/2) · k^c · (ΔΘ^c)^2`
```

Line 397:

```text
Where `k^c` is the stiffness coefficient of the substrat, reflecting its resistance to angular deformation. In this interpretation, magnetic potential energy is the internal strain energy of the causal substrat, not a property of an abstract field.
```

Line 401:

```text
The classical concept of magnetic field lines finds a natural reinterpretation: each field line is a directional vector of causal torsion, representing how much and in what orientation the substrat has been twisted. Where field lines are dense, substrat strain is more intense, resulting in a higher local `ΔΘ^c`. This explains the intuitive observation that inductance increases with turns (N) and core concentration (e.g., ferromagnetic materials), both of which enhance local torsional load.
```

Line 405:

```text
When a current is interrupted, the substrat tension that was sustaining the angular deformation collapses. The stored strain (`ΔΘ^c`) rapidly decays, and the substrat snaps back toward equilibrium. This causes a sharp angular acceleration:
```

Line 407:

```text
`(6.1.3) a_θ = d^2Θ^c / dt^2`
```

Line 415:

```text
- Angular strain `ΔΘ^c` accumulates in response to magnetic dipoles (e.g., current loops).
```

Line 417:

```text
- This deformation stores energy, governed by the stiffness coefficient `k^c`.
```

### PDF page 21

Line 492:

```text
\Phi^B = (\mu_0 \times N \times I \times A)/l
```

Line 498:

```text
\begin{aligned}f_s &= \operatorname{sqrt}(A/l)\quad (\text{dimension: }\mathrm{m}^{1/2}) \\ \alpha &= \operatorname{sqrt}(\mu_0/k^c)\quad (\text{dimension: }\mathrm{m}^{-1/2}\cdot\mathrm{A}^{-1})\end{aligned}
```

Line 512:

```text
\mu_e\mathrm{ff} = \mu_r \times \mu_0
```

Line 518:

```text
\alpha_e\mathrm{ff} = \operatorname{sqrt}(\mu_e\mathrm{ff}/k^c) = \operatorname{sqrt}(\mu_r \times \mu_0/k^c)
```

### PDF page 22

Line 551:

```text
- Φᴮ ≈ n × (h / 2e) ≈ n × 2.068 × 10⁻¹⁵ Wb
```

### PDF page 23

Line 575:

```text
`(6.3.1) ℰ = −dΦ_B / dt`
```

Line 589:

```text
`(6.3.3) a_θ = d²θᶜ / dt²`
```

Line 593:

```text
`(6.3.4) V = ξ · Q · a_θ`
```

### PDF page 24

Line 601:

```text
- `a_θ` is the angular acceleration (in rad/s²),
```

Line 603:

```text
- ξ is a proportionality constant (≈ 5 × 10⁶ V/C), determined empirically from transformer and inductor observations (cf. Page 31).
```

Line 621:

```text
`(6.3.5) a_θ = Δθᶜ / (Δt)² = 0.005 / (1 × 10⁻³)² = 5 × 10³ rad/s²`
```

Line 623:

```text
`(6.3.6) V = ξ · Q · a_θ = (5 × 10⁶) · (0.01) · (5 × 10³) = 2.5 × 10⁵ V`
```

### PDF page 25

Line 643:

```text
`(6.3.7) Φ_B = μ₀ · N · I · A / l`
```

Line 647:

```text
`(6.3.8) dΦ_B / dt = μ₀ · N · A / l · dI/dt`
```

Line 657:

```text
`(6.3.10) a_θ ∝ I · dI/dt`
```

Line 659:

```text
Thus, angular acceleration (`a_θ`) is proportional to magnetic flux change, implying:
```

Line 661:

```text
`(6.3.11) V = ξ · Q · a_θ ∝ −dΦ_B / dt`
```

Line 669:

```text
- Shown that substrat angular acceleration (`a_θ`) produces an induced voltage (V), consistent with EMF.
```

Line 673:

```text
- Linked time-varying causal strain to classical flux change (`dΦ_B` / dt), validating Faraday’s law through substrat mechanics.
```

Line 677:

```text
This completes the Aetherwave reinterpretation of electromagnetic induction: stored substrat tension (Δθᶜ) causes energy retention, and its rapid decay (`a_θ`) produces the observable induced voltage.
```

### PDF page 29

Line 793:

```text
- `kᶜ_slope`: resistance to angular bending (tilting causal flow)
```

Line 795:

```text
- `kᶜ_torsion`: resistance to twisting causal geometry
```

Line 797:

```text
- `kᶜ_shear`: resistance to offset displacement of neighboring flow lines
```

Line 799:

```text
- `kᶜ_stretch`: resistance to longitudinal dipole tension
```

Line 801:

```text
- `kᶜ_compress`: resistance to collapse of causal density
```

### PDF page 31

Line 849:

```text
V(θᶜ) = –(3⁄8) · (kᶜ · θᶜ²) / x²
```

Line 859:

```text
Gᵉᶠᶠ\_μν = ∂\_μθᶜ · ∂\_νθᶜ − ½ · g\_μν (∂^σθᶜ · ∂\_σθᶜ)
```

Line 863:

```text
- The first term (∂\_μθᶜ · ∂\_νθᶜ) represents directional causal tension—how substrat slope changes across spacetime.
```

Line 875:

```text
It functions as a scalar-origin gravitational analog to the Einstein tensor G\_μν, but derived entirely from angular causal geometry rather than curvature of spacetime itself.
```

Line 882:

```text
k^c(x) \cdot (\partial^2\theta^c/\partial t^2) + k^c(x) \cdot (\partial^2\theta^c/\partial x^2) + \partial V(\theta^c)/\partial\theta^c + (dk^c/dx) \cdot (\partial\theta^c/\partial x) = 0
```

### PDF page 32

Line 900:

```text
\theta^c \approx \sqrt{2GM / c^2r}
```

Line 906:

```text
d\theta^c/dx \approx -GM / c^2r^2
```

Line 919:

```text
- Tensorial structure Gᵉᶠᶠ\_μν is derived directly from causal deformation mechanics.
```

### PDF page 33

Line 927:

```text
The Aetherwave model reframes several core principles of modern physics by replacing force-driven curvature with flow-based geometry. Through the scalar field θᶜ and its derived gravitation tensor Gᵉᶠᶠ\_μν, we find continuity—not contradiction—between quantum behavior and relativistic dynamics.
```

### PDF page 38

Line 1087:

```text
Gᵉᶠᶠ\_μν = αK\_μν + βT\_μν
```

Line 1093:

```text
- β serves as a tension-energy scaling coefficient connecting substrat field behaviors to traditional energy-momentum tensor (T\_μν) structures, and is proportionally linked to substrat stiffness modes.
```

Line 1095:

```text
However, α, which governs the relative weight of pure causal curvature (K\_μν) in shaping spacetime geometry, remains partially open. It may vary with substrat density, causal coherence, or energy localization.
```

### PDF page 40

Line 1135:

```text
From its scalar foundation in θᶜ to its predictive gravitation tensor Gᵉᶠᶠ\_μν, the model provides a coherent, testable, and scalable system for describing energy, inertia, curvature, and even quantum connectivity through a single unified principle: directional deformation of causal flow.
```

### PDF page 43

Line 1225:

```text
#### A. Scalar Field \u03b8ᶜ and Substrat Energy Storage
```

Line 1257:

```text
#### B. Construction of the Effective Gravity Tensor Gᵎʳᵒ
```

### PDF page 44

Line 1261:

```text
Gᵎʳᵒ = ∂ᵒθᶜ · ∂ᵎθᶜ − ½ · gᵎᵒ (∂ˢθᶜ · ∂ˢθᶜ)
```

Line 1272:

```text
k^c(x) \cdot (\partial^2\theta^c/\partial t^2) + k^c(x) \cdot (\partial^2\theta^c/\partial x^2) + (\partial V/\partial\theta^c) + (dk^c/dx) \cdot (\partial\theta^c/\partial x) = 0
```

Line 1278:

```text
V(\theta^c) = -(3/8) \cdot (k^c \cdot (\theta^c)^2) / x^2
```

Line 1295:

```text
1. Slope Mode (kᶜₛₒₚₙₑ):
```

Line 1299:

```text
   - Energy storage: E = ½ · kᶜₛₒₚₙₑ · (Δθᶜ)²
```

Line 1301:

```text
2. Torsion Mode (kᶜₜₒₚₜₒₓ):
```

Line 1305:

```text
   - Torque relation: τ = kᶜₜₒₚₜₒₓ · Δφ
```

Line 1307:

```text
3. Shear Mode (kᶜₛₐₒₐₐ):
```

### PDF page 45

Line 1311:

```text
   - Energy storage: E = ½ · kᶜₛₐₒₐₐ · (Δxₛₒₜ)²
```

Line 1313:

```text
4. Stretch Mode (kᶜₛₐₒₐₐₜₐₜₐ):
```

Line 1317:

```text
   - Energy storage: E = ½ · kᶜₛₐₒₐₐₜₐₜₐ · (Δθᶜₛₐₒₐₐ)²
```

Line 1319:

```text
5. Compression Mode (kᶜₜₐₒₒₐₐₐ):
```

Line 1323:

```text
   - Pressure relation: P = −kᶜₜₐₒₒₐₐₐ · Δρᶜ
```

Line 1327:

```text
kᶜₜₐₒₒₐ = f(kᶜₛₒₚₙₑ, kᶜₜₒₚₜₒₓ, kᶜₛₐₒₐₐ, kᶜₛₐₒₐₐₜₐₜₐ, kᶜₜₐₒₒₐₐₐ)
```

Line 1343:

```text
- Rebound angular acceleration (after current interruption): ∂²θᶜ / ∂t² ≈ Δθᶜ / (Δt)²
```

### PDF page 46

Line 1356:

```text
- Substrat angular acceleration: ∂²θᶜ / ∂t² ≈ 200 rad/s²
```

Line 1358:

```text
- Theoretical peak voltage generated: V ∝ 5 × 10⁶ volts per displaced coulomb
```

### PDF page 48

Line 1425:

```text
E_s = \frac{1}{2} \times k^c \times (\Delta\theta^c)^2
```

Line 1430:

```text
Joules per radian squared (J·rad⁻²)
```

Line 1432:

```text
Equivalent to: kg·m²·s⁻²·rad⁻²
```

Line 1436:

```text
1 Kc = 1 kg·m²·s⁻²·rad⁻²
```

### PDF page 50

Line 1480:

```text
### 1. Universal Energy EuEᵤ
```

Line 1504:

```text
### 2. Critical Compression Depth d\_c
```

Line 1510:

```text
d\_c = √(ħ × G ÷ c³) ≈ 1.616 × 10⁻³⁵ m
```

Line 1514:

```text
d\_c = Eᵤ ÷ τ\_c
```

Line 1516:

```text
### 3. Critical Tension τ\_c
```

### PDF page 51

Line 1522:

```text
τ\_c = c⁴ ÷ G ≈ 1.21 × 10⁴⁴ N
```

Line 1524:

```text
### 4. Substrat Stiffness Coefficient k\_c
```

Line 1530:

```text
k\_c = (2 × Eᵤ) ÷ ((Δθᶜ)² × d\_c)
```

Line 1534:

```text
k\_c ≈ (2 × Eᵤ) ÷ d\_c
```

Line 1538:

```text
k\_c ≈ (2 × 1.57 × 10⁷⁰) ÷ (1.616 × 10⁻³⁵) ≈ 1.94 × 10¹⁰⁵ J·rad⁻²
```

Line 1544:

```text
Eᵤ = τ\_c × d\_c
```

Line 1548:

```text
k\_c = (2 × τ\_c) ÷ Δθᶜ²
```

Line 1552:

```text
k\_c = (2 × Eᵤ) ÷ (Δθᶜ² × d\_c)
```

Line 1558:

```text
k\_c(L) = α × E(L) ÷ L
```

### PDF page 52

Line 1570:

```text
Original mathematical structures (e.g., substrat elasticity, θᶜ causal fields, causal tensor Gᵉᶠᶠ\_μν) → Developed uniquely in this work by Paul Frederick Percy Jr. and Curie GPTo.
```

