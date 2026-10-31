# Review Paper I — archival conversion pilot

**One paper, one Markdown file.** This pilot is only Paper I from compiled volume 1, PDF pp7–52, not a conversion of the entire volume into one file. The two volumes contain eleven identifiable publication segments; VI/XI numbering has explicit source qualifications. Later papers are not converted in this pilot.

1. Read the [draft](draft.md).
2. Compare it with the [46-page source excerpt](../../../sources/assets/paper-001/conv-01/source-pages-007-052.pdf).
3. Review the [audit and decisions](../../../history/ingestion/paper-001-conversion-audit.md) and [independent source check](../../../history/ingestion/paper-001-independent-verification.md).
4. Consult the [full source inventory](../../../history/ingestion/source-inventory.md) and [volume boundaries](../../../history/ingestion/volume-boundaries.md).

For a mathematical sample, inspect §6.2.2 against original PDF p21 (excerpt p15): the minus in the alpha dimensional exponent was recovered from pixels. The source mixes superscript B, literal `_B`, and a partial subscript in effective quantities; the draft deliberately preserves those differences. For the table method, inspect §14 Part II D against original pp45–46 (excerpt pp39–40): four rows, 12 data cells, one joined table. No substantive figure occurs in Paper I; no example figure was invented.

**Pending owner decisions:** approve or reject duplicate-notice consolidation and repeated-table-header consolidation; review source fidelity and the chosen Markdown renderer; then explicitly authorize import preparation if desired. Mathematical parsing passed, but browser visual rendering was blocked and is not claimed verified. Candidate XI numbering is a separate catalog decision.

No raw file, manifest record, policy or original source was changed. Do not run the intake registrar from this staging state. Source-faithful does not mean scientifically validated. No merge or automatic merge is authorized.

Run `python investigations/conversions/paper-001/verify_pilot.py` to check the fixed draft, evidence assets, raw baseline and page accounting. This check does not replace source review or owner approval.
