# Ark: Curie's Library

**A persistent, source-grounded research atlas for Aetherwave / Aether Reality Kernel (ARK).**

> **First, read [`AGENTS.md`](AGENTS.md), [`00_START_HERE.md`](00_START_HERE.md), and the preserved [`ARK Epistemic Charter v1.1`](raw/epistemics/ARK_Epistemic_Charter_v1.1.md).**

The Head Librarian is **Curie**, a *coordination role*, not a claim of unattended service, persistent autonomy, or guaranteed access to any AI system. Researchers of any model family must follow the same source-integrity and evidence standards. Research proposals are not automatically endorsed by Curie or the owner.

## Purpose

This library is deliberately **separate** from the original [Aetherwave research repository](https://github.com/Pfpercy0214/aetherwave-unified-theory). That original project remains the source of historic research papers and current technical work. This library is an independent, AI-maintained knowledge map: it traces how the ideas developed, compares claims to established physics and experiments, records failures, and builds cross-domain links. It must not silently rewrite or validate the original theory.

The name shown here is the project title. GitHub's compatible repository identifier is `ark-curies-library`.

## Where to put things

| Path | Ownership | Function |
| --- | --- | --- |
| `raw/papers/` | Human / archive curator only | **Verbatim Markdown papers. Never edit, rewrite, or remove.** |
| `raw/epistemics/` | Human / archive curator only | Preserved copies of the ARK epistemic charter and historical methodology |
| `raw/MANIFEST.json` | Human / archive curator only | Immutable-asset checksums and provenance |
| `wiki/` | AI-editable, reviewed | Linked summaries, domain knowledge, identity and concept pages |
| `claims/` | AI-editable, reviewed | Claim provenance, status, assumptions, tests, and disagreements |
| `sources/` | AI-editable, reviewed | **Externally verified** bibliographic and empirical source notes |
| `history/` | AI-editable, reviewed | Chronology, decisions, conceptual evolution and corrections |
| `investigations/` | AI-editable, reviewed | Cross-domain investigations, falsifiers, negative results |
| `sessions/` | AI-editable, reviewed | Handoff records, AI activity and unresolved questions |
| `templates/` | AI-editable, reviewed | Structured recording forms |

**Read [`POLICIES.md`](POLICIES.md) for archive, evidence, and review safeguards.**

## Workflow (Karpathy-style LLM wiki, adapted for scientific research)

1. Human adds a checked, faithful Markdown document to `raw/papers/` and registers it with `python scripts/register_raw.py path/to/file.md`.
2. Agent reads sources and the methodological charter; it never edits `raw/`.
3. Agent compiles claims into connected `wiki/` pages, records `claims/` and `sources/` references, updates indexes and a durable session log.
4. Agent investigates contradictions using relevant real-world research (primary studies, measurements, standards, and reproducible calculations) rather than reasoning solely from other library notes.
5. An independent reviewer or separate verification pass audits substantive claims. Conflicts and failed tests stay recorded.
6. Human reviews significant promotions in claim status; agents can propose, not silently establish, a physical mechanism.

### Quick start

- Read [`00_START_HERE.md`](00_START_HERE.md).
- Run `python scripts/check_archive.py` and `python scripts/lint_library.py`.
- Add your first paper to `raw/papers/` **without altering its contents**, then `python scripts/register_raw.py raw/papers/paper-001.md`.
- Ask an agent: *"Ingest raw/papers/paper-001.md. Trace its claims to page and equation identifiers, link relevant external tests, record gaps, and preserve disagreements."*

> **Security / privacy:** Start with a **private** repository until you have reviewed original papers, personal notes, and source permissions. Git history is not a privacy boundary for previously published secrets. The supplied archive-check workflow is not full server-side protection; enable protected branches and required checks in GitHub after publication.
