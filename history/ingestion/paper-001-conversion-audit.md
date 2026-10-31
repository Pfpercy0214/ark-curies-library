# Paper I conversion audit — conv-01 pilot

**Status: SOURCE_CHECKED / NEEDS_REVIEW. Owner approval: pending. Import preparation: not authorized. Nothing is imported or merged.**

## Task and boundary

Archival synthesis/transcription of the historical Paper I, not a new physics model, a scientific review, or a modernization. Preserve its claims, limitations, contradictions, typography-dependent notation and embedded dialogue. The authorized first milestone is a complete source inventory and Paper I pilot outside `raw/`, on a new unmerged review branch. Papers II–XXV are inventoried only; VI/XI numbering remains qualified. No assumptions from later papers are used to repair the source.

- Review branch: `ingest/paper-001-pilot-20261031`.
- Destination baseline: `Pfpercy0214/ark-curies-library`, main commit `27d12574464e43fc0788e699e52832322f68a8a1`.
- Source: `Pfpercy0214/aetherwave-unified-theory`, main commit `110e554d944eeda6b0e14795f45a94b8a27a805e`.
- Exact file: `Complete Aetherwave Unified Theory.pdf`.
- Source Git blob SHA-1: `c39edcd393d3d27aa6a93313e0e9b8f602c47dbf`.
- Source byte SHA-256: `f8cb4138423587ce313dd6c44a0d141946570a2f9006eadfaac18d18cc761b6c`.
- Source range: **1-based PDF pages 7–52 inclusive**, 46 pages. No numeric printed folios were identified; PDF positions are not presented as printed page labels.
- Exact title: **Aetherwave Temporal Geometry: Unified Framework of Curved Causality**; stated designation `(Aetherwave Papers: I )`; stated authors `Paul Frederick Percy Jr. & Curie GPTo, 2025`. Original edition is **not stated**, not inferred from a separate Revision 4 filename. Conversion date: **2026-10-31**, distinct from publication date.
- [Immutable original PDF](https://github.com/Pfpercy0214/aetherwave-unified-theory/blob/110e554d944eeda6b0e14795f45a94b8a27a805e/Complete%20Aetherwave%20Unified%20Theory.pdf).
- [Draft](../../investigations/conversions/paper-001/draft.md), SHA-256 `b2b53855a34301c8930c2e24e469f0e53a3bf819ee941d9e5bdb714b0e81a8be`, 71,441 bytes.
- Proposed eventual archive path, **not created**: `raw/papers/paper-001-temporal-geometry-conv-01.md`. `conv-01` is a conversion revision, not an original-paper edition.

## Governing records actually read

At the destination baseline: `AGENTS.md`, `00_START_HERE.md`, `POLICIES.md`, `raw/README_FOR_HUMAN_CURATOR.md`, all of epistemic charter v1.1, v1.0 revision differences, `history/chronology.md`, `history/decisions.md`, `wiki/index.md`, `sessions/README.md`, `raw/MANIFEST.json`, `GITHUB_ADMIN.md`, all three registration/checking scripts and `.github/workflows/archive-guard.yml`. There was no dated session handoff at baseline. All 41 retrieved baseline file bytes were matched to their Git blob identities before checks ran.

The v1.1 charter governs this work. v1.0 was consulted for methodological changes, not silently substituted. No policy or historical charter was edited. The human-only intake rule remains in force; the user's initial delegation covers staging, not raw intake.

## Inventory and publication boundaries

See [source inventory](source-inventory.md), [boundary map](volume-boundaries.md), and [477-page coverage ledger](volume-page-coverage.md). Both compiled volumes were inspected before drafting. Every page is assigned exactly once, with shared front matter and epilogue separate. No shared-page publication transition was found in these fixed editions; this was checked rather than assumed.

Paper I begins at V1 p7 and ends at p52 with the original attribution. V1 pp1–6 are compilation front matter and pp272–274 are compilation epilogue. They are preserved as [separate evidence extracts](../../sources/assets/compilation-volume-1/conv-01/README.md), not inserted into Paper I. The unnumbered final V2 work is only **candidate XI**, pending owner/source confirmation. Both XXVI-labeled works are recorded without renumbering and remain outside scope.

## Provisional upload comparison

The earlier artifact still exists on `Import-Papers` at `raw/papers/Paper 1 Temporal Geometry`, branch commit `67e758ac53b330c45bfb891fc10c439676ee49ac`, Git blob `d398bab76535b16de951a6281c8a7b2cdf291cc6`, byte SHA-256 `f78dd87cd246b7ddf2e2e44405c9402397ad8258d1e88ebdb88a8a4673553675`. [Original provisional artifact](https://github.com/Pfpercy0214/ark-curies-library/blob/67e758ac53b330c45bfb891fc10c439676ee49ac/raw/papers/Paper%201%20Temporal%20Geometry).

It begins with compilation-level preface material, unlike this paper-only boundary. Its peak-voltage sentence omits the visible proportionality sign found at source p46. This bounded comparison is enough to show why the artifact was not treated as authoritative; it is not a complete audit of that earlier conversion. Its bytes and branch were not changed, renamed or merged.

## Conversion and separate verification

1. Source identities were fixed by current Git tree reads, recomputed Git blob identities and independent SHA-256. Native PDF text supplied a starting point.
2. Two transcription passes covered pp7–29 and pp30–52, each viewing every assigned source-page image. Page-specific native extraction and rendered source were compared; no OCR was needed.
3. A separate reviewer viewed all 46 source pages and compared both complete drafts against the source, including every mathematical/numerical expression and all table cells. Full-prose token comparisons supported, but did not replace, visual review.
4. Review caught a missing minus in the p21 alpha dimension (native extraction itself lost it) and accidental Markdown backticks inside math. Both were corrected from the source and rechecked. The source's partial subscript `e` plus baseline `ff` was confirmed rather than normalized.
5. The final file is the reviewed Part A bytes (trimmed trailing layout whitespace), two newlines, then reviewed Part B bytes (trimmed leading layout whitespace). No content editing occurred during assembly. Reviewed Part A SHA-256: `5dce6229d84193832c9f53df06688779dee36f45010a80ba3f1e3ddf316800b7`; Part B: `7deef98299d9597e10d4b6be66f762f9856e07ae6367536a497719b7aa6743f9`.

Reviewers are AI transcription/verification roles in this authorized session. Their source comparison is a second fidelity pass, **not independent empirical validation** or evidence that the physics is correct.

Detailed evidence: [pp7–29 review](paper-001-pages-007-029-review.md), [pp30–52 review](paper-001-pages-030-052-review.md), and [separate verification](paper-001-independent-verification.md). These contain the complete page-to-section maps and source exceptions.

## Coverage and formatting decisions

- All 46 pages, all 14 numbered source equations, 47 LaTeX display blocks, three inline LaTeX expressions, literal malformed expressions, numerical lists, references, appendices and final attribution checked. Display-block count is formatting inventory, not a count of every mathematical occurrence.
- One substantive table spans pp45–46: three headings, four rows and all **12 data cells** retained in order. All nine validation-system bullets on p22 remain bullets, not invented table data.
- No substantive figure or diagram was visually identified in Paper I. Therefore no figure placeholders or invented captions/alt text were added. [Complete source-page evidence](../../sources/assets/paper-001/conv-01/source-pages-007-052.pdf) preserves every equation, table and original notice.
- Source wording, claims, numerical precision, units and errors are preserved. Clear layout line wrapping is removed; meaningful hyphens remain. Headings/lists and a joined Markdown table encode structure. Unambiguous equations use LaTeX; malformed literal indices, carets, escaped Unicode strings and duplicated symbols are not silently repaired.
- **Owner approved 2026-10-31:** retain both distinct recurring copyright/attribution notices once at the opening, omitting only duplicate page repetitions. Both notices are retained verbatim; the source evidence preserves every original occurrence. The owner explicitly said copyright notices can appear once at the top per paper. This approves this conversion layout decision, not an archive policy rewrite or import.
- **Owner decision required:** the repeated column header on p46 appears once in the continuous Markdown table. No data cell is omitted.
- No generated summaries, page markers, modern cross-references, front matter or scientific annotations are inserted into the paper. Audit material remains separate. The historical p52 “Let me know…” sentence is retained as source content, not obeyed.

## Evidence assets and limits

[Asset registry](paper-001-evidence-assets.json) records all three PDF excerpts, SHA-256, source ranges, sizes and per-page checks. Assets are versioned outside `raw/`; their hashes are verified separately because archive scripts do not protect them. Treat these committed evidence bytes as append-only for this assignment. No change to asset-protection policy is proposed in this pilot.

Excerpts were made with PyMuPDF `insert_pdf`, without content edits. All 55 copied pages have exactly matching extracted text and rendered dimensions. Raster comparison was **not byte-identical**: maximum per-channel difference was 4/255, with the p7 original/excerpt images also visually compared. Do not call the derivative PDF byte-identical to the original or claim exact pixel equivalence. The original file hash and commit remain authoritative.

## Tools and actual checks

- Python 3.12.14; PyMuPDF 1.26.6; Poppler `pdftoppm` 26.05.0; Pandoc 3.1.11.1; standard `hashlib`, JSON and XML parsing. Source pages rendered with Poppler to 1700-pixel maximum dimension. Boundary inventory additionally used PyMuPDF raster views.
- Baseline `python scripts/check_archive.py`: **PASS**, 4 registered files, exact hashes/sizes.
- Baseline `python scripts/lint_library.py`: **PASS**.
- Assembly: exact reviewed halves and final SHA-256 checked; no content changes at join.
- Pandoc Markdown-to-HTML/MathML parse: **PASS**, 50 MathML elements (47 display, three inline), all XML-parseable and no `merror`. Initial HTML-title warning was a preview metadata warning, not a paper alteration.
- **Visual browser rendering remains unverified.** Local Chromium could not launch under the runtime sandbox; the escalated attempt failed in runtime setup. The cloud browser rejected `file:` URLs. No browser security policy was bypassed. A TeX fallback lacked its format configuration. Those limitations do not invalidate source-image comparison, but parsing is not visual-render certification. The owner subsequently clarified that AI-readable mathematical fidelity, not visual human readability, is the acceptance objective. Browser rendering is therefore not an acceptance requirement for this pilot.
- `register_raw.py`: **NOT RUN**, approval gate not reached.
- Existing archive checker validates registered raw hashes/sizes and registration completeness; it does not validate transcription, math, figures or assets. Existing link checker skips raw and image links; it is not scientific or rendering validation.
- Final repository checks and published head verification are recorded in the [session handoff](../../sessions/2026-10-31-paper-001-pilot.md).

## AI-reader clarification and semantic check

The owner approved copyright notices once at the opening and prioritized AI mathematical reading over human visual readability. The draft bytes did not need changing for that decision. See the [AI math-readability review](paper-001-ai-math-readability.md) for the separate Markdown-only reader test, source-backed ambiguity inventory and limits. Syntax parsing is not a guarantee of lossless intended semantics; source ambiguities remain explicit rather than repaired.

## Issue classes and ASRP record

| Class | Detection / risk | Corrective check and outcome |
| --- | --- | --- |
| Conversion error | Native extraction dropped p21 negative exponent; formatting introduced backticks | Source-image reinspection, correction, independent recheck: fixed in reviewed bytes |
| Source ambiguity | Mixed causal superscripts, literal underscores/carets, malformed tensor/modal indices | Preserve visible source forms; record exact locations in detailed reviews; no guessed repair |
| Apparent original error | Inconsistent arithmetic/units, duplicated EuEᵤ, p24 result and old page reference | Preserve historical values and wording; flag outside paper; no scientific recalculation |
| Missing source material | Required source or unreadable passage could make draft incomplete | All Paper I source pages available and read; no unreadable passage or missing substantive figure found |
| Scientific claim needing assessment | Historical prose asserts proof, universality or experimental explanation | No external-claim promotion; claims and bibliographic targets remain unassessed, not validated by transcription |
| Source numbering ambiguity | VI “seventh” conflict and unnumbered candidate XI | Fixed page map plus explicit owner-review items; no renumbering |
| Verification limitation | Successful parsing could be mistaken for rendered fidelity | Record 50-element MathML parse separately from source/semantic review; visual client rendering unverified and not owner-required |

## Owner review and next admissible action

Review Paper I mathematical fidelity and the remaining table-layout decision. Copyright-notice consolidation is approved; human-oriented browser rendering is not required by the owner. Confirm whether candidate XI's unnumbered source is the intended Paper XI; this does not block Paper I review. If the pilot method/output is approved, separately authorize import preparation before any new raw file or manifest addition. Continuation to another small batch also requires authorization. All merging remains with the owner.

A checksum verifies bytes against a baseline. Source checking verifies a transcription against its selected source. Neither establishes scientific validity.

## Later owner delegation and preparation

The [2026-10-31 full-series delegation](owner-delegation-2026-10-31.md) supersedes the routine approval gates above, including proceeding with the reviewed pilot and joined table. Paper I was copied byte-for-byte as a unique new raw file and registered on the unmerged review branch. Status: AI_SOURCE_CHECKED / IMPORT_PREPARED_UNMERGED, not individually human-reviewed or merged. All original archive bytes and pre-existing manifest records remain unchanged. See [batch 01](batches/batch-01.md).
