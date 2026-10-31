# ARK / Curie's Library — agent collaboration contract

## Mission

Maintain a durable, searchable, interlinked Markdown research library grounded in historical sources, current measurements, and falsifiable investigation. The objective is **truthful classification of claims**, not confirmation of Aetherwave. Head Librarian: Curie (coordination designation only). No AI is granted automatic authority to act without an active session and permitted tools.

## Read order

1. `00_START_HERE.md`
2. `POLICIES.md`
3. `raw/epistemics/ARK_Epistemic_Charter_v1.1.md` (source of epistemic rules; read relevant sections, not a superficial summary)
4. `history/chronology.md`, `wiki/index.md` and newest session handoff
5. Task-relevant original paper(s), external evidence and equations

## Immutable raw collection — hard boundary

- **Never modify, delete, move, normalize, reformat, or automatically overwrite any file under `raw/`.** This includes fixed historical charters, paper Markdown, and the manifest.
- The human owner is the only party who imports source files or approves a new version as a distinct additional file. A corrected conversion receives a new versioned file and a documented supersession; the previous copy remains intact.
- No AI-generated annotations, YAML frontmatter, fixes, or summaries may be inserted into historical paper Markdown. Put them in `wiki/`, `claims/`, `history/` or `investigations/` and link back.
- A file's existence in `raw/` proves its provenance and integrity only insofar as the hash record and collection process are trustworthy; it does **not** establish scientific validity.

## Required empirical loop

1. **Frame:** state claim, version, physical regime, boundary/initial conditions, input-vs-target separation, measurement path, uncertainty and predicted distinguishing observation.
2. **Find:** consult external observations, recognized physical theory, primary literature, experimental data, and original sources. A second AI summary is not independent evidence. Record links, data versions, dates and what was actually read.
3. **Test:** check units, solution branches, conservation constraints, numerical sensitivity, calibration degrees of freedom, degeneracy, alternative mechanisms, and held-out predictions where possible. Never claim to have executed code that was not executed.
4. **Challenge:** actively search for counterexamples and established alternative explanations; preserve failed attempts and limits on data access.
5. **Record:** update source cards, claims, wiki backlinks, `sessions/` handoff, and decision/contradiction logs. A new session must not need to rediscover the same failure.

## Epistemic distinctions

- **Claim type** (definition, hypothesis, conditional derivation, interpretation, reconstruction, retrodiction, prospective prediction) is separate from **evaluation status** (untested, exploratory, calibrated, cross-validated, externally tested, inconclusive, contradicted, withdrawn) and **provenance** (observed, assumed, fitted, inferred, independent source, prior exposure).
- Fitting and calibration are not inherently invalid. Information leakage, target-conditioned choices and mislabeled evidence are the problem. Conversely, exact closure or numerical agreement alone does not prove a mechanism.
- A conventional model or experiment is not automatically evidence for ARK. Explicitly show what **novel** result ARK predicts and whether a rival model also predicts it.
- A repeated analogy across scales is a research lead, not a demonstration of the same causal mechanism.
- Epistemic charter v1.1 is the governing historical text; preserve its nuances rather than replacing it with slogans.
- Do not fabricate scientific references, DOIs, URLs, numerical results, dates, or source access. Mark unverified information as pending.

## ASRP loop

Detect difficulty → label the epistemic risk → anticipate the likely error → choose a corrective check → act → record consequence. Apply against both overclaiming and reflexive dismissal. This is an operational self-review technique, not evidence of changes to model weights or physics.

## Wiki maintenance

Each ingestion should update `wiki/index.md`, relevant concept pages, `claims/index.md`, `sources/index.md`, and a dated session note when warranted. Preserve traceable references to original path + heading/figure/equation identifiers. Do not silently rewrite a prior scientific verdict; record the old and new status with reasons.

## Authorized changes

Agents may edit `wiki/`, `claims/`, `sources/`, `history/`, `investigations/`, `sessions/`, `templates/` and propose changes to active instructions through review. No modification to `raw/` or original theory repository. No autonomous publication, credentials use, irreversible actions or claims of scheduled work without explicit user authority.
