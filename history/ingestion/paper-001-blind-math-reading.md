# Blind Markdown math-reading test

## Scope and verdict

I read only `investigations/conversions/paper-001/draft.md` (all 1,570 lines), including all **50 dollar-delimited LaTeX expressions** (47 display, 3 inline), literal/code equations, Unicode formulas, units, and the table. I did not inspect a PDF, source document, previous audit, or other repository files. No repository files were modified.

**Verdict: most formula operations are recoverable without rendering, but the draft does not support an unqualified claim of unambiguous mathematical recovery.** Four LaTeX expressions have material index/grouping risks (lines 512, 518, 900, 906); additional literal expressions have symbol-identity and grouping problems. There are also clearly readable but inconsistent units and definitions. Readability, syntactic validity, intended meaning, and scientific correctness are separate tests.

This report cannot determine whether any problem originates in the source or in conversion. “Ambiguous” below means unresolved in the supplied Markdown, not proven conversion damage. I make no scientific corrections.

## Highest-risk unresolved expressions

### 1. Effective quantities have only a partial subscript (LaTeX expressions 25–26)

- Line 512: `\mu_e\mathrm{ff} = \mu_r \times \mu_0`
- Line 518: `\alpha_e\mathrm{ff} = \operatorname{sqrt}(\mu_e\mathrm{ff}/k^c) = \operatorname{sqrt}(\mu_r \times \mu_0/k^c)`

Exact LaTeX structure: only **e** is a subscript of mu/alpha; upright **ff** follows at baseline. This is not structurally the same as an `eff` subscript. A reader can reproduce the actual token structure, but cannot safely decide whether baseline `ff` is a separate factor/string or the remainder of an intended effective-label index. The nearby ferromagnetic-core prose suggests an effective quantity but does not authorize silently moving characters into the subscript. This is a symbol-identity/index issue even though the syntax can render.

### 2. Slash with juxtaposed denominator factors (LaTeX expressions 36–37)

- Line 900: `\theta^c \approx \sqrt{2GM / c^2r}`
- Line 906: `d\theta^c/dx \approx -GM / c^2r^2`

The radical's entire argument is explicit at line 900, but the slash's denominator scope is not. Competing readings are `sqrt(2GM/(c² r))` and `sqrt((2GM/c²) r)`. Line 906 similarly allows `-GM/(c² r²)` versus `(-GM/c²) r²`. TeX typography does not assign mathematical slash precedence; neither string has a fraction or denominator parentheses. Do not choose a reading by appealing to an expected physics formula.

- Related literal line 551: `Φᴮ ≈ n × (h / 2e) ≈ n × 2.068 × 10⁻¹⁵ Wb`. Parentheses surround `h / 2e`, but do not explicitly distinguish `h/(2e)` from `(h/2)e`. The numerical value does not license reconstruction of missing grouping.

### 3. Tensor index identities are not recoverable with confidence

- Line 1257 heading: `#### B. Construction of the Effective Gravity Tensor Gᵎʳᵒ`
- Line 1261: `Gᵎʳᵒ = ∂ᵒθᶜ · ∂ᵎθᶜ − ½ · gᵎᵒ (∂ˢθᶜ · ∂ˢθᶜ)`

The exact Unicode glyphs can be copied, but their mathematical identities are unexplained: modifier-letter/superscript-looking `ᵎ`, `ʳ`, `ᵒ`, and `ˢ` do not identify mu, nu, sigma, or an effective label. Both `ˢ` derivative marks are raised in the literal text, so a lowered/raised contraction cannot be recovered from it. It is unsafe to replace this line with the more familiar-looking tensor at line 859. That would assume identity between different written formulas.

### 4. Modal index strings preserve characters but not reliable intended labels

Exact excerpts:

- Lines 1295, 1299: `kᶜₛₒₚₙₑ`; `E = ½ · kᶜₛₒₚₙₑ · (Δθᶜ)²`
- Lines 1301, 1305: `kᶜₜₒₚₜₒₓ`; `τ = kᶜₜₒₚₜₒₓ · Δφ`
- Lines 1307, 1311: `kᶜₛₐₒₐₐ`; `E = ½ · kᶜₛₐₒₐₐ · (Δxₛₒₜ)²`
- Lines 1313, 1317: `kᶜₛₐₒₐₐₜₐₜₐ`; `E = ½ · kᶜₛₐₒₐₐₜₐₜₐ · (Δθᶜₛₐₒₐₐ)²`
- Lines 1319, 1323: `kᶜₜₐₒₒₐₐₐ`; `P = −kᶜₜₐₒₒₐₐₐ · Δρᶜ`
- Line 1327: `kᶜₜₐₒₒₐ = f(kᶜₛₒₚₙₑ, kᶜₜₒₚₜₒₓ, kᶜₛₐₒₐₐ, kᶜₛₐₒₐₐₜₐₜₐ, kᶜₜₐₒₒₐₐₐ)`

Products, signs, half factors, and outer squares are readable. The nearby mode headings permit a local association of each k-string with a named mode. They do not establish the intended spelling of each index, the meaning of `xₛₒₜ`, or why the stretch formula's theta suffix matches the shear stiffness suffix. Earlier lines 793–801 instead use readable literal labels `kᶜ_slope`, `kᶜ_torsion`, `kᶜ_shear`, `kᶜ_stretch`, and `kᶜ_compress`. Equivalence is plausible, not formally stated; I have not substituted these for the unusual strings.

### 5. Concatenated/escaped symbol variants and unannounced aliases

- Lines 31, 39, 43: literal code `θc\\θᶜ`; lines 119, 173: literal code `θc\θᶜ`. These contain more than a single theta symbol. No mathematical operator or alias convention explains the backslashes or duplication.
- Line 41: `Local vs Cosmic kckᶜ`.
- Line 43: literal code `Gμν(eff)G^{(eff)}_{\\μ\\ν}`. It appears to juxtapose two representations; no equality/alias separator says so. The double-backslash forms are not ordinary Greek LaTeX commands as written.
- Line 99: literal code `\u3000Gᵉᶠᶠ_μν = αK_μν + βT_μν`. The textual `\u3000` is not a mathematical symbol or decoded space in Markdown code.
- Line 1225: `Scalar Field \u03b8ᶜ`. A Unicode escape spelling is present rather than the Greek letter itself.
- Line 1480: `Universal Energy EuEᵤ`, an unexplained concatenation; the following `E_u` equations clarify the locally defined energy but not what the concatenation itself denotes.

The uppercase `Θ^c` in code at lines 387, 389, 395, 407 and related prose denotes a causal slope by the accompanying explanations. Lowercase `θᶜ` is used elsewhere for that description. I can recover the local meanings, but there is no explicit equation declaring uppercase/lowercase symbols identical. Likewise magnetic flux appears as `\Phi^B` (492), `Φᴮ` (551), and `Φ_B` (575, 643); the prose makes the referent clear but the upper/lower placement of B is genuinely different text. These distinctions must survive archival transcription rather than be silently normalized.

## Recoverable but notation-sensitive cases

### Dimensional alpha is clear, not garbled

Line 498:

`\begin{aligned}f_s &= \operatorname{sqrt}(A/l)\quad (\text{dimension: }\mathrm{m}^{1/2}) \\ \alpha &= \operatorname{sqrt}(\mu_0/k^c)\quad (\text{dimension: }\mathrm{m}^{-1/2}\cdot\mathrm{A}^{-1})\end{aligned}`

I read two definitions: f subscript s equals the square root of area A divided by lowercase length l, with stated dimension metres to the one-half; alpha equals the square root of mu subscript zero divided by causal stiffness k superscript c, with stated dimension metres to the minus one-half multiplied by amperes to the minus one. The minus signs, half exponent, multiplication dot, and inverse ampere are all recoverable. Upright unit A here is ampere; variable A in the first definition is area, as defined at line 475. The dimension string need not be guessed from appearance.

The stated dimensions should not be “corrected” to agree with other units. Line 453 declares stiffness `N·rad⁻²`; Appendix A instead declares `J·rad⁻²` (1430). This is an internal unit-consistency question, not failure to read the exponents at 498.

### Causal theta and squares

- Lines 72, 128, 1230, 1341, 1387: theta superscript c is the named causal slope, equal to arccosine of proper-time interval divided by coordinate-time interval. In context c is a causal label here, distinct from the independently defined speed c at 1492; no exponentiation by the speed of light is required to read the named quantity.
- Line 312: `\Delta\theta^c = |\theta^c_+ - \theta^c_-|`: deviation equals the absolute value of the difference between the plus-indexed and minus-indexed causal slopes. The plus/minus signs are subscripts, not unary signs outside theta. Lines 317–319 explain their roles. Contrast `+θᶜ`/`−θᶜ` at line 719, where signs are outside theta.
- Line 240: `E = \tfrac12 k^c(\Delta\theta^c)^2`: one-half times stiffness times the square of the entire causal-slope deviation. `\tfrac12` means one over two, not twelve.
- Literal line 849: `V(θᶜ) = –(3⁄8) · (kᶜ · θᶜ²) / x²`. The adjacent raised `ᶜ²` alone is less explicit than `(θᶜ)²`; however line 1278 explicitly provides `V(\theta^c) = -(3/8) \cdot (k^c \cdot (\theta^c)^2) / x^2`. Thus the draft contains a clear corresponding reading: negative three-eighths times stiffness times causal slope squared, divided by x squared. No need to invent a `c²` exponent.
- Similarly lines 1548 and 1552 contain `Δθᶜ²`; line 1530 explicitly uses `((Δθᶜ)² × d\_c)`. The repeated context supports squaring the deviation, while the exact less-explicit typography should still be preserved.
- `kᶜ` versus `k\_c`, and `τᶜ` versus `τ\_c`, are not formally declared interchangeable. In particular Appendix A calls tau superscript c causal tension, whereas Appendix B calls tau subscript c critical tension. Similar names are not authority to collapse their identity.

### Integrals and derivatives

- Line 202: `\Phi(x) = \int g(x)\,dx = \int(d\theta^c/dx)\,dx = \theta^c(x)`. This says Phi of x equals an indefinite integral of g of x with respect to x, equals an indefinite integral of the first ordinary x-derivative of causal theta, equals causal theta of x. Neither bounds nor an integration constant are written. That absence is explicit; a reader must not supply either. The relation is readable even if its mathematics needs separate review.
- Lines 166, 184, 218: `g \approx d\theta^c/dx` is an ordinary first derivative of causal theta with respect to x, not a partial derivative or a displayed multidimensional gradient operator. Prose calling it a vector/gradient does not add missing vector indices.
- Lines 407 and 589 express a second ordinary time derivative; line 621 uses the finite ratio `Δθᶜ / (Δt)²`. Their difference remains recoverable.
- Line 882 has four additive terms: stiffness at x times the second partial time derivative of causal theta; stiffness at x times its second partial x derivative; the partial derivative of V(theta superscript c) with respect to causal theta; and the ordinary x derivative of stiffness multiplied by the first partial x derivative of causal theta. The sum equals zero. **Both second-derivative terms have plus signs.** No minus sign, covariant derivative, or contraction is implied. Line 1272 repeats this with `∂V/∂θᶜ` lacking the explicit V argument but otherwise readable.
- Line 859: `Gᵉᶠᶠ\_μν = ∂\_μθᶜ · ∂\_νθᶜ − ½ · g\_μν (∂^σθᶜ · ∂\_σθᶜ)`. The intended conventional literal notation is legible: effective G with lower mu/nu, product of lower-mu/lower-nu derivatives, minus half the metric with lower mu/nu times a parenthesized upper-sigma/lower-sigma derivative product. Markdown escapes underscores; it does not typeset indices. Repeated sigma suggests the usual contraction convention, but this text does not specify metric signature or index range. This line is far more recoverable than line 1261 and must not be used to silently replace it.
- Line 213, literal `Gμν = Rμν − ½Rgμν = κTμν`, lacks actual subscript markers. A conventional tensor reading is available from context; exact index heights are not encoded in this line. Line 161 similarly has `Rμν`. Preserve this qualification if index placement is part of “lossless.”
- Line 647, `dΦ_B / dt = μ₀ · N · A / l · dI/dt`, is conventionally a product of mu-zero, N, A, inverse l, and the ordinary current time derivative; the explicit dot following l does not justify placing the current derivative in the denominator.
- Prose line 655, `Differentiating θᶜ with respect to time (squared),`, is not a uniquely specified differential operation: second derivative and derivative with respect to squared time differ. The explicit equations retain their written derivative orders; the prose alone should not be converted into an additional formula.

### Square-root scaling and table

Line 482 (repeated 566; equivalent explicit-root form at 652) takes the square root of **the entire fraction** whose numerator is `μ₀ × N² × A × I²` and denominator is `l × kᶜ`. All these factors, indices, and squares are explicit. `\operatorname{sqrt}` is readable as a named square-root function with parenthesized argument; it is not a lost radical just because it renders as text.

The only Markdown table is lines 1347–1352. It has no global column multiplier or hidden power-of-ten heading. Its values independently read:

- Stored Energy (E): `5000 J`.
- Angular Deformation (Δθᶜ): `0.005 rad`.
- Collapse Time (Δt): `0.005 s`.
- Substrat Stiffness (kᶜ): `4 × 10⁸ N·rad⁻²`.

The stiffness value is four times ten to the eighth, with newtons times radians to minus two. This exponent applies only to its row, not every value. At line 1356, `∂²θᶜ / ∂t² ≈ 200 rad/s²` is separately readable. The table's 0.005 seconds differs from the 1 ms example at line 615; the draft does not instruct the reader to merge them.

The system list at lines 525–541 likewise uses separate energy prefixes and causal-angle exponents (MJ, mJ, aJ, µJ, kJ). For example `SQUID (50 aJ): Δθᶜ ≈ 1.58 × 10⁻¹⁴ rad` at 537 says fifty attojoules and a separate angle value, not fifty amperes times joules or a shared table scaling factor.

## Unit and definition tensions: readable text, no unique globally consistent assignment

These are not reasons to change the transcription:

1. Stiffness is repeatedly `N·rad⁻²` (270, 336, 352, 453, 757–761, 1352) but is `J·rad⁻²` at 1430 and 1538. The units are individually unambiguous; the draft does not supply a single globally consistent unit choice.
2. Line 593 says `V = ξ · Q · a_θ`, line 601 gives acceleration `rad/s²`, and line 603 gives ξ `≈ 5 × 10⁶ V/C`. All tokens are clear; an extra acceleration-normalization factor or different ξ unit cannot be inferred safely.
3. Line 1358: `V ∝ 5 × 10⁶ volts per displaced coulomb`. The literal numeric coefficient and volt-per-coulomb phrase are readable, but it does not specify the variable in the proportionality or make this a complete voltage model. Do not turn ∝ into equality.
4. Appendix B lines 1510, 1514, 1522, 1530, 1534, 1538, 1544, 1548, 1552, 1558 have readable multiplication/division/grouping, but their stiffness unit claims and use of energy divided by a length must be preserved as written. A reader cannot fix dimensions by adding a missing length or changing J to N.
5. Alpha is used for the magnetic prefactor (498), gravity weighting (1087–1097), and geometry-dependent scaling (1558–1564). No equation states these three locally described alphas are identical. Similarly V denotes induced voltage in Section 6.3 and potential in Section 9. Local context distinguishes these uses; a global symbol table must retain scopes rather than assume identity.

## Complete LaTeX-expression coverage ledger

Numbering is in occurrence order; line numbers identify formula content (inline content uses its host line). “Readable” means the written formula can be interpreted, **not** that it is correct, dimensionally consistent, or proven faithful to an unseen source. All inherit the local causal-label convention discussed above.

| Expressions | Content lines | Result |
| --- | --- | --- |
| 1–5 | 72, 128, 154, 166, 184 | Readable definitions, numerical angle, ordinary derivatives |
| 6 | 202 | Readable indefinite-integral chain; no bounds/constant written |
| 7–10 | 218, 240, 270, 276 | Readable; stiffness-unit issue retained |
| 11 | 312 | Readable absolute difference with plus/minus indices |
| 12–16 | 326, 336, 342, 352, 358 | Readable energy expressions; unit issue retained |
| 17–22 | 434, 448, 460, 466, 482, 492 | Readable grouping and flux superscript B |
| 23–24 | 498, 504 | Readable dimensions and magnetic prefactor |
| 25–26 | 512, 518 | Partial `e` index with baseline `ff`; intended identity unresolved |
| 27–30 | 556, 566, 584, 652 | Readable; equation numbers are labels, not factors |
| 31–35 | 716, 748, 784, 844, 882 | Readable angle, energies, four-term PDE |
| 36–37 | 900, 906 | Slash/juxtaposition denominator scope unresolved |
| 38–42 | 1044, 1091, 1230, 1242, 1272 | Readable energy, time-ratio definition, PDE |
| 43 | 1278 | Readable potential with explicit squared causal theta |
| 44–48 | 1339, 1341, 1387, 1425, 1453 | Readable energy, causal slope, energy/depth tension |
| 49–50 | 1487, 1501 | Readable `(c⁵/G) × T_u` and energy in joules |

## Bottom line for an AI-use acceptance gate

A math renderer passing these 50 expressions would not establish losslessness. The Markdown already permits accurate recovery of most formulas, including dimensional alpha, whole-fraction square roots, derivative orders, integral syntax, table values, and signs. It does **not** uniquely settle the partial effective indices, unparenthesized denominator products, unexplained tensor glyphs, all modal suffix identities, or every cross-section symbol alias/unit assignment. These should be surfaced as unresolved evidence rather than auto-repaired. Only comparison to the source could separate conversion defects from source notation or theory issues; this blind test does not do that.
