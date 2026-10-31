# Paper I — AI math readability and semantic fidelity review

Date: 2026-10-31. Scope: the unchanged Paper I review draft, not archive intake or scientific validation.

## Conclusion

**For the clarified goal—preserve the original text and mathematical notation—the pilot remains source-faithful and AI-readable.** The fresh Markdown-only reader recovered the important operators, signs, grouping, units, table values and equation labels. The original’s odd forms are retained, not silently repaired. It does not make every source expression uniquely interpretable. Clear equations expose operators, parentheses, signs, exponents and units in text that an AI reader can recover. Source-malformed indices, mixed label conventions and under-grouped formulas still require interpretation. These source ambiguities are not conversion failures and do not require the owner to fix the physics or manually copy/paste the paper. No test can guarantee every AI will infer the same intended meaning. Successful LaTeX/MathML parsing alone cannot establish that promise.

The owner explicitly approved copyright notices once at the top of each paper and clarified that AI-readable math, not human visual rendering, is the objective. Both distinct notices already occur once at the top. That approval does not authorize interpreting malformed mathematics, archive intake, or merging. Browser visual QA is no longer an acceptance requirement for this pilot.

## Evidence and separation of tests

- Draft: [paper-only Markdown](../../investigations/conversions/paper-001/draft.md), 71,441 bytes; SHA-256 `b2b53855a34301c8930c2e24e469f0e53a3bf819ee941d9e5bdb714b0e81a8be`.
- [Prior source-image comparison](paper-001-independent-verification.md) checked all 46 pages, including numerical expressions and table cells. It establishes source-to-transcription comparison, not intended meaning or physical correctness.
- A [fresh AI reader](paper-001-blind-math-reading.md) read all 1,570 Markdown lines and all 50 LaTeX expressions, without PDF or prior audit. Its report tests what that reader could actually recover from the text, not what the transcriber intended.
- A [source-backed reviewer](paper-001-math-source-semantics.md) separately checked the high-risk reading and catalogued 18 notation families and 11 grouping/operator checks, with occurrence-level source pages and Markdown lines. No newly dropped or changed source mathematics was found. Source images, not extraction alone, determine whether a defect was introduced during conversion.
- Pandoc-to-MathML was rerun: 50 elements (47 display, three inline), zero `merror`, all XML-parseable. This is a syntax result only. Literal Unicode and code-span mathematics are not counted in those 50.
- The source contains ordinary prose, literal Unicode and literal code-span expressions as well as LaTeX. A consumer extracting only `$...$` blocks will omit mathematical content. Reading the complete UTF-8 Markdown is necessary.

## Concrete Markdown-only recoveries

- The alpha dimension was read correctly as metres to **−1/2** times amperes to **−1**—including the minus sign originally lost by native PDF extraction and restored during source checking.
- The inductive expression was read as a square root over the whole fraction, numerator `μ₀ × N² × A × I²`, denominator `l × kᶜ`.
- The plus/minus theta indices, absolute-value difference, all four additive PDE terms and both plus signs were recovered without a browser.
- The four table values were recovered separately, including `4 × 10⁸ N·rad⁻²`; the peak-voltage `∝` was not mistaken for equality.
- The reader also noticed the partial `e` subscript followed by baseline `ff`, malformed tensor/modal glyphs and ungrouped slash denominators. Source comparison—not the blind reader’s expectations—decides their provenance.

## Safe handling by downstream AI

Preserve case, Unicode code points, superscript/subscript positions, explicit grouping, relation symbols and units. Do not normalize all causal `c` labels into powers, all uppercase/lowercase theta into one symbol, all stiffness labels into one variable, or proportionality into equality. Do not decode a literal source `\u...` sequence as though it were an instruction to substitute a character. Keep the paper text separate from this audit.

Source-faithful text and unique mathematical semantics are different goals when the original notation is malformed. An optional normalized interpretation would have to be a separately labeled companion with mappings, explicit assumptions and unresolved alternatives. It must not silently replace the historical text. No such interpreted replacement is approved or produced here.

The fresh blind reader and source-backed reviewer agree on the observed high-risk forms. The source-backed review attributes them to the original notation, not new conversion damage. No draft correction was warranted; its checksum remains unchanged.

## Remaining decisions

The source ambiguities are retained as archival evidence and are not prerequisites to accepting this preservation pilot. No repair or interpretation companion is needed for the clarified task; it would be a separate future scope only if requested. Copyright repetition no longer needs a decision. Table-header consolidation and overall pilot approval remain separate; candidate XI is a catalog question unrelated to Paper I math. Import preparation and later paper conversions still require authorization.
