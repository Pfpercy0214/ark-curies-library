# Independent verification — Paper XXII

Status: **PASS**, including final display-delimiter correction recheck. Review date: 2026-10-31. Reviewer is not the drafter; reviewer did not edit draft.

Reviewed draft: 27417 bytes; SHA-256 `ed962a7dbdc64b1126b73ba08a1101237eea3549e7466655313a9cfc7d92b35c`.
Source: fixed standalone `XXII-Electromagnetism in Scalar Geometry.pdf`, 15 pages, Git blob `1595391c60c2063f55e78cd49bc6882649a0b775`, independently rehashed SHA-256 `13a1142acc75dc2bfe7ff645bad25bf77e68e55a53b17876b873fe03dbb0bda8`.

Read the complete draft and actually viewed each source page `work/p1.png`–`work/p15.png`, comparing all prose, mathematics/numerical expressions and structural order. Title, author, collaborators and September 5, 2025 date agree. All seven numbered references and all four appendices retained. No substantive figures or tables exist in these pages. Single distinct rights notice verified from pixels and retained once as authorized.

## Page coverage

- pp1–3: front matter, introduction, calibration bridges/inversions, literal terminal backtick, field definitions, author note, Faraday and magnetic Gauss law.
- pp4–5: electric Gauss, Ampère–Maxwell, wave equation, all energy/Poynting steps.
- pp6–8: scalar bridge, solenoid field geometry/calibration, point-of-use recovery, both uncertainty expressions and induction, edge-case list.
- pp9–10: remaining consistency bullets, five-step protocol, media, all boundary conditions, gauge and plane-wave relations.
- pp11–12: VI.5 heading, energy transport expressions, complete discussion/conclusion and reference heading.
- pp13–15: all seven references, complete EM-A–D, final practical summary.

All 59 recorded mathematical transformations checked against pixels: 58 LaTeX displays and one literal detached-circumflex expression. Source baseline ∂t, Aφ/Eφ, ΛA/Λu and related letters remain baseline; literal A_comp/r_ref retain underscores. Radical grouping, exponents, signs and factors agree. Detached `ˆk` is preserved, not silently changed to an over-hat. Inconsistent source bridge algebra, physical assertions and body-versus-appendix inversions were not corrected. No content defect or unresolved symbol ambiguity found.

## Supplementary check

Fresh native extraction and exact reversal of recorded math transformations, Markdown wrappers/escaping and authorized bullet-marker layout compared the entire non-whitespace character sequence. No substantive differences; only four source dash sub-bullets require the explicitly documented list-marker normalization. `independent_check.py` and `independent-text-check.json` retain the reproducible result. Raster footer checked independently of extraction.

## Minor formatting correction requested

Place closing display delimiters on their own lines where explanatory prose follows `$$` on the same line. Keep explanatory wording outside math, unchanged. This is Markdown portability rather than missing content; final bytes must be rechecked after the drafter makes it.

Final recheck: drafter placed closing delimiters on standalone lines. All explanation wording remains outside math and unchanged. Fresh inverse comparison is exact for all 20,094 normalized non-whitespace source characters; no differences. Final fingerprint above supersedes original.
