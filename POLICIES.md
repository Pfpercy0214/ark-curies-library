# Library stewardship and evidence policy

## 1. Two different repositories, two different purposes

- Original Aetherwave repository: papers, current theory research, and historic source material.
- Ark: Curie's Library: derived, cross-linked, externally checked research knowledge and critical audits.
- The Atlas must not be treated as a substitute for the original text. Always cite the exact source version.

## 2. Source immutability

`raw/` is human-curated. Agent edits are prohibited. Files in `raw/` are byte-preserved; SHA-256 hashes are stored in `raw/MANIFEST.json`. A verified archive file must be cited by path and version. Corrections become **new files** with an explicit supersedes relationship, not destructive edits.

The provided GitHub Action blocks pull requests that change or delete existing raw files. It checks stored hashes. **Neither this Action nor CODEOWNERS is absolute protection** if bypassed, disabled, or if a privileged user edits the manifest and files together. Configure protected branches, required status checks, human approvals and appropriate permissions to enforce the policy, and retain external backups.

## 3. History and attribution

The development history is first-class source material. Separate documents written at the time from later reconstructions. Do not backdate. Preserve superseded assumptions and failed paths. Record quotations accurately and briefly. Date events at the precision actually supported by the evidence.

## 4. Verification with the outside world

An AI cannot promote a mechanism claim merely because it appears coherent with library documents. Each material physics claim needs relevant external evidence or an explicit statement that empirical confirmation is absent. Favor papers, experimental datasets, official data and reproduced calculations. Keep source notes, DOI/URL, access date, version, relevant methods, uncertainty, and whether the original text was actually consulted. Cite a secondary summary as secondary.

## 5. Epistemic status

Maintain independent fields: claim type, evaluation status, evidence/provenance, and validity domain. Never collapse agreement, fit, derivation, interpretation, and prediction into one confidence grade. Disagreement between reviewers is stored, not averaged away. Established physics is an external benchmark, not automatically part of ARK.

## 6. Independent review

Any high-impact conclusion should have a substantive challenge pass checking assumptions, units, information flow, alternate explanations and falsifiers. Another model repeating the original conclusion without independent source checks does not constitute external validation.

## 7. Transparency

No invented execution, browsing, calculations, citations, source access, human approvals, autonomous jobs or unfinished background activity. Tasks that require real-world evidence but lack it remain tagged `NEEDS_EXTERNAL_CHECK`.

## 8. Privacy and external publishing

Treat unreviewed drafts and internal research as private. The person publishing the repository is responsible for ensuring sensitive correspondence, personal details, access tokens and unpublished work are not included. Follow legal access and copyright limits when documenting external articles; save original annotations and limited excerpts, not entire copyrighted articles without permission.
