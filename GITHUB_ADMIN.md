# GitHub administration — Ark: Curie's Library

**Repository:** https://github.com/Pfpercy0214/ark-curies-library  
**Private by default.** This library is separate from the original Aetherwave research repository.

## Essential server-side protections

The `raw/` archive is governed by add-only rules and hash verification. The supplied CI checks and CODEOWNERS are important safeguards, but **do not alone make files immutable**. A user with sufficient repository access can bypass them, edit CI, or rewrite Git history.

In **Settings → Rules → Rulesets**, create a ruleset for `main` (availability depends on plan/repository). Require pull requests, require the `archive-guard` status check once it appears, disallow force pushes and branch deletions, and apply to administrators where your GitHub plan permits. Limit who can change the ruleset and `.github/workflows/`.

For stronger archive guarantees, restrict write access to `raw/`, require owner approval for additions, maintain offsite read-only backups, and record release/tag hashes. **No GitHub ruleset can prevent a privileged owner from changing their own content**; the purpose is to prevent silent or accidental changes and preserve an auditable history.

## Paper ingestion

1. Create a faithful, manually verified Markdown conversion of an original paper.
2. Add it as a **new file** under `raw/papers/`. Never edit an existing raw file. Keep document version and origin in its filename or manifest.
3. Run `python scripts/register_raw.py raw/papers/PAPER_NAME.md --origin 'source and conversion notes'`.
4. Run `python scripts/check_archive.py` and `python scripts/lint_library.py`.
5. Submit the import for owner approval; include provenance, conversion checks, and any ambiguity logs.
6. AI agents may then create annotations only in the editable catalog directories.

## Initial validation

```bash
python scripts/check_archive.py
python scripts/lint_library.py
```

The archived epistemic charters are copies of historical methodological sources, not empirical verification of the physics claims they discuss.
