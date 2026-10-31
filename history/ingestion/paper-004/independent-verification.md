# Paper IV — independent source verification

**PASS** — source-faithfulness review, not scientific validation.

Reviewed artifact: `draft.md`, 51,801 bytes, SHA-256 `3f9bd13c268c2c7b0ab7d7baae519f3a4323f4ef0713d7b8d26ac01558406f43`.
Reviewer: `transcribe_pilot_second_half`, separate from the drafter.
Review date: 2026-10-31. Original paper date: 2025; these dates are distinct.
Source: fixed compiled Volume I, PDF pages 102–138 inclusive (37 pages), Git blob `c39edcd393d3d27aa6a93313e0e9b8f602c47dbf`, source SHA-256 `f8cb4138423587ce313dd6c44a0d141946570a2f9006eadfaac18d18cc761b6c`.

## Coverage and checks

Every page listed below was viewed as a rendered image and compared with the corresponding continuous Markdown, including prose, headings, list ordering, every mathematical/numerical expression, references and notices. Native text was supplementary, not a substitute for pixels.

- PDF p102: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p103: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p104: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p105: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p106: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p107: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p108: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p109: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p110: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p111: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p112: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p113: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p114: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p115: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p116: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p117: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p118: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p119: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p120: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p121: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p122: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p123: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p124: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p125: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p126: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p127: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p128: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p129: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p130: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p131: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p132: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p133: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p134: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p135: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p136: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p137: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.
- PDF p138: prose, order, headings and all visible mathematical/numerical material checked; no unresolved conversion defect.

## Specific checks

- All 18 cells of the 6-row, 3-column table on p120 match the source, including powers, units, approximate estimates and the source's scalar notation. No calculated values were corrected.
- All 18 LaTeX displays checked visually, including the image-only tensor on p135 and the position operator. Literal underscores/carets and malformed mixed notation remain literal; pp132–135 baseline `θc`, `kc`, `Es`, `τc`, `Eu`, `dc`, `∂i`, `∂j`, `∂u`, `∂v` and `∂s` were not silently made into indices.
- Source crops `shield-p122.png` and `einstein-tensor-p135.png` viewed directly and compared to full source pages. Both match; byte counts and SHA-256 values match `assets/manifest.json`. Tensor superscript/subscript placement, contraction and parentheses agree with the added LaTeX transcription.
- Three distinct copyright/header/footer notices retained once at opening; repeated page furniture omitted as authorized. The unique final p138 notice is present at opening.
- Preserved source anomalies include p117 `nise` subscript, p118–119 inconsistent numerical estimates, duplicated 15.4 numbering, literal/mixed notation, and reference [2] “Maping the interior od a Black Hole”. All 11 references checked on pp136–138.
- Independent reverse-format comparison (`work/independent-check.py`) reverses logged equation formatting, removes Markdown layout/authorized notices and the image-only tensor addition, and compares against native paragraph extraction: **6,887 / 6,887 tokens, zero differences**. The table cells were separately checked from pixels; extraction alone cannot establish their associations.

No draft edits were made by this reviewer. Asset links are the intended publication paths and need the publisher's placement check; this report verifies the working assets and source fidelity, not remote publication.
