# Human curator: archive intake only

This read-only shelf contains verbatim inputs, not AI reformulations. Keep machine-generated frontmatter, comments and summaries **outside** it. When converting a paper from PDF or spreadsheet to Markdown:

1. Preserve title, version, equations, units, footnotes, references, figures, table values and source ordering. Save source page references or figure captions in a separate conversion audit outside `raw/`.
2. Mark any conversion ambiguities in `investigations/` or `history/`, **not** in the immutable paper text. Do not present guesses about a missing symbol as a verified transcription.
3. Add a uniquely versioned file under `raw/papers/` (e.g., `paper-021-v2.md`); do not replace an earlier version.
4. Run `python scripts/register_raw.py raw/papers/paper-021-v2.md` after human review; it rejects a mismatch against any previously registered checksum.
5. Run `python scripts/check_archive.py` and commit both the file and appended manifest record. Save primary source provenance and conversion QA in `history/`.

**Archive integrity is not scientific validity.**
