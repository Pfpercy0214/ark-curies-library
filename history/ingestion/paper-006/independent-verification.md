# Paper 006 — independent source verification

**PASS after correction** — source-faithfulness review, not scientific validation.

Reviewed `draft.md`: 35,733 bytes; SHA-256 `420662ef0f17dfc496881bcaf01f97c88a4151b2ef0a21c8da5b42fd8a99a328`.
Reviewer: `transcribe_pilot_second_half`, separate from drafter. Review date 2026-10-31; original year 2025, no edition statement.
Source: fixed compiled Volume II, physical PDF pages 1–19, Git blob `c511e7baa47ca1c37e31e4445839e5aadfe6d12a`, SHA-256 `e4568a9894782114023d74befea0e689f3d0d8b07d4514ea40c9b40f47492ec8`.

## Page coverage

Every page was viewed as rendered pixels and compared with the corresponding full draft text, including prose/order/headings, every math/numerical expression, notices and references. Native extraction was supplementary.

- PDF p1: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p2: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p3: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p4: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p5: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p6: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p7: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p8: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p9: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p10: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p11: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p12: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p13: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p14: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p15: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p16: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p17: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p18: full visual/text/math/numerical review completed; no unresolved defect.
- PDF p19: full visual/text/math/numerical review completed; no unresolved defect.

## Findings and recheck

- p2 §1.3: draft originally encoded `E_{m}ᵢ_{n}`, incorrectly separating the contiguous subscript. Publisher corrected to `E_{min}`; final expression rechecked against pixels.
- p11 §7.4: suspended-hyphen spacing in `pre- and post-interaction` was collapsed. Publisher restored the space; rechecked.
- Original draft hash `2b5fadd0f47073f331f1314ccc71464614b42edecba9f3db60e339b4dc43d398` is superseded by the hash above. Drafter math-map retains the pre-correction string; independent-check.py accounts for the corrected version.
- All 20 cells of p16's 4-row, 5-column planet table checked, including 5.2/9.6/19.2 AU, 3.6×10⁴/8.9×10⁴/2.7×10⁵, 4.8×10³⁸/3.1×10³⁸/2.6×10³⁸, and all result labels.
- All 9 LaTeX equation mappings checked. Source's baseline Ω, mixed literal underscores/carets, t₁/₂, odd numerical estimates and “seventh formal entry” wording preserved. No numbering repaired.
- Both distinct notices restored once at opening; all 10 references including original GitHub URL and internal AI peer-review entry checked. No substantive figures.
- Independent sequential reverse-format comparison against native text: remaining differences are exactly the two source notices (absent in native.txt) and two layout-only split-word joins (`charge- based`, `high- curvature`). No substantive omission or addition.

Reviewer made no draft edits. This report binds the exact working draft hash above, not remote publication.
