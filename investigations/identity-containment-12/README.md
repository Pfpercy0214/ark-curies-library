# IC-12 — Event-data intake and a bounded validation protocol

Date: 2026-11-01. Parent: `cf0879c783192bd9e8f1f040e95a394d1fb3e080`. Research PR #2 only. **Status: BLOCKED_AWAITING_SOURCE_FILES. This is tested analysis infrastructure and a proposed protocol, not an event-data result or another physical mechanism study.** No changes to `raw/`, policies, source repository, or earlier investigations. No merge authorized.

## What changed

IC-11 left the empirical step incomplete. This session retried the official README and event distributions, NIST's documented metadata routes and the observed public S3 cache. The catalog and article HTML remained accessible; no README, raw events, RGA record, unrounded simulation or authoritative file checksum was retrieved. Native Python reports DNS failure; the web retrieval reports unavailable redirects or timeout. The specialized downloader also failed. A connector search did not identify a relevant NIST downloader; unrelated storage apps were not suggested. These are session access failures, not evidence that the public data do not exist.

Rather than fit another generated curve, this addition supplies a small, reproducible intake tool; a null-filled analysis contract; a specific likelihood specification; and an acquisition handoff. No event adapter is invented before reading the release documentation.

## Source access and provenance

Primary public catalog (read 2026-11-01):
https://catalog.data.gov/dataset/data-used-in-writing-detection-of-molecular-hydrogen-in-a-neutron-beam-lifetime-experiment

Dataset: NIST `mds2-3859`. It describes event energies/times, related simulations, earlier experiment material, and residual-gas data. Listed official distributions:

- https://data.nist.gov/od/ds/mds2-3859/README.txt
- https://data.nist.gov/od/ds/mds2-3859/BL2data.zip
- https://data.nist.gov/od/ds/mds2-3859/BL2Simulations.zip
- https://data.nist.gov/od/ds/mds2-3859/BL1simanddata.zip
- https://data.nist.gov/od/ds/mds2-3859/RGA_data.txt

Primary author paper: J. Caylor et al., *Detection of Molecular Hydrogen in a Neutron Beam Lifetime Experiment*, https://arxiv.org/html/2506.01682v2 . Read native HTML apparatus, acquisition, timing/pressure/trap-time and simulation discussion, including equations 1–3 and captions 5–14. No image pixels, source PDF, event bytes or plots were analyzed this session. The paper's displayed later render date is not a newly inferred publication date. Dataset filenames alone do not establish their internal schema.

Official NIST programmatic-access documentation read:
https://www.nist.gov/metis/developer-tools . It documents metadata via `?format=nerdm`, component download URLs, sizes and checksums. Attempts at `https://data.nist.gov/od/id/mds2-3859?format=nerdm`, `?format=text`, the RMM record routes, canonical `ark:/88434/` routes, and the known S3 README failed. No NERDm record or publisher checksum was obtained. The downloader therefore records a **local** SHA-256 if it retrieves bytes and leaves publisher_checksum null. It does not pretend a locally generated checksum authenticates the source's scientific content.

[access-attempt.json](access-attempt.json) is the actual stdout of the new downloader's README/BL2 retry, both DNS failures. Other web/specialized-download failures are documented here rather than invented as HTTP status logs. `BL1simanddata.zip` timed out through web; `RGA_data.txt` and `BL2data.zip` redirected to the unavailable public cache. The other listed simulation ZIP was not separately fetched this session.

Repository records actually read: PR #2, AGENTS, entry protocol, POLICIES, charter v1.1 sections 4–6.9, latest IC-11 handoff, and the current IC-11 script header/blob. The prior packet's code was hash-matched and executed. No full-corpus reread, fresh paper audit or local full-archive verification is claimed.

## The first empirical target is detector composition, not absolute neutron lifetime

Use documented BL2 energy/arrival-time events and their apparatus metadata to test whether a response model transfers across independently specified readout conditions. The candidate is a ramp-voltage series with adequately matched upstream conditions; availability and run IDs remain unknown. Do not assume that every detector scan held gas density, flux, temperature or trap preparation fixed.

Before opening evaluation outcomes, record:

1. File hashes, documentation provenance, actual columns and units, time origin, channel calibration, acquisition/run grouping and event multiplicity handling.
2. Detector specification, trigger/energy threshold, timing window, trap length/time, nominal and actual voltages, neutron monitor exposure, and applicable gas/temperature conditions. Missing means unknown, not zero or a universal default.
3. Background model and its control observations; explicit treatment of inflight events, pileup, return/backscatter and losses. Do not subtract counts and then pretend the result is Poisson without modeling subtraction uncertainty.
4. Source and normalization of each proton/ion response template, whether it represents incident or detected fractions, and its parameter covariance. A visual shape from a differently normalized figure is not an absolute event count.
5. Complete acquisition groups assigned to calibration and evaluation. Randomly holding out events from the same acquisition does not test transfer to a different control regime. Actual assignments remain null until the release is inspected.
6. Allowed calibrations, excluded adjustments, uncertainty calculation, residual statistic and evaluation criterion. Fit only designated calibration responses, freeze the model, then evaluate a different group. If validation fails, record it before proposing a revision.

The paper reports a timing comparison that used a ramp offset to improve agreement. That offset cannot silently become an independently measured input to our reproduction. Either recover an independent voltage calibration or label an offset as an estimated nuisance, calibrate it on specified runs, and propagate it unchanged to evaluation runs. Prior exposure to published trends prevents calling the whole exercise blind.

## Why normalized spectra cannot generally determine an absolute rate

Let unnormalized expected counts in joint energy/time bin j be

$$\mu_j=\Gamma X\{(1-f)\eta_p p_j+f\eta_h h_j\}+b_j,$$

where X is independently characterized neutron exposure, f is the incident/trapped species fraction under the selected model, eta are efficiencies, p and h are normalized **detected** response shapes conditional on their species, and b is background. Definitions and selection windows must be consistent. An unknown overall neutron calibration multiplies Gamma; shared calibration uncertainty is not independent information.

For the zero-background case, define `w_j=(1-f) eta_p p_j+f eta_h h_j`, W=sum(w_j), and N=sum(n_j). The independent-Poisson likelihood factors exactly:

$$\prod_j {e^{-\Gamma Xw_j}(\Gamma Xw_j)^{n_j}\over n_j!}
=\operatorname{Pois}(N;\Gamma XW)\operatorname{Mult}\left(\{n_j\};N,\{w_j/W\}\right).$$

The conditional shape part contains no Gamma. It can constrain f when the species responses are independently informative, but cannot supply the lost absolute count/exposure normalization. In the actual study, some plotted spectra were deliberately given different visual normalizations; digitizing them would not restore that missing normalization.

**Qualification:** a background whose absolute amplitude is independently known can introduce an external scale into the conditional shape through the signal-to-background ratio. Our tests explicitly show this exception. An unconstrained background does not provide that anchor. We therefore do not claim that every conceivable normalized-spectrum analysis is scale-blind.

Absolute-rate analysis requires the count term plus independently justified absolute exposure, effective efficiencies, channel completeness and upstream invariance. Those requirements are additional to spectral-shape validation. A successful detector composition fit alone is not a measurement of epsilon or an environmental change in beta decay. No operational ARK coupling is supplied by this protocol.

## Intake tool and commands

`nist_intake.py` uses Python 3.10+ standard library only. It accepts only the five cataloged filenames and declared HTTPS NIST/cache hosts, never sends credentials, refuses overwrites, bounds download and uncompressed sizes, validates text/ZIP formats, inventories and hashes ZIP members without extraction, rejects traversal/links/encryption/duplicates, and reads member CRCs. Resource limits or a new redirect host may need explicit review for a real release. It is not a complete security sandbox or scientific authenticity validator.

From this directory in an environment with working public internet access:

```bash
python nist_intake.py fetch /path/to/nist-data --files README.txt BL2data.zip > acquisition.json
python nist_intake.py inspect /path/to/nist-data/BL2data.zip > inventory.json
python nist_intake.py validate analysis-contract.json --root /path/to/nist-data
```

If files are acquired separately, `inspect` works offline. Large event archives remain outside Git; only compact provenance and reviewed derived outputs belong in the research PR. Never execute source-provided scripts during intake. The final validation command intentionally exits 2 with the current contract. It cannot pass until the evidence and run partition are supplied. Its best status is `READY_FOR_REVIEW`, not scientific approval. Filling strings is not proof; source-backed review is required.

The proposed contract is **not** a finalized preregistration. Its schema, cuts, runs and calibrations are deliberately unresolved. Freeze and hash the completed specification after metadata review and before evaluation events; log any later change with its effect on prior exposure. Do not use the absence of a response mismatch as evidence of negligible perturbation.

## Actual verification

`python check_ic12.py` executed **18/18 offline unit tests**, covering source restrictions, mocked transfer, hashing, archive inventories and CRC, bad paths/links/duplicates, resource limits, real missing-data blocking, overlapping groups, changed input hashes, additional absolute-rate requirements, likelihood factorization, common-scale cancellation, and the fixed-background exception. These fixtures are explicitly not NIST events. No initial test failed; there was no empirical execution to succeed or fail.

The real contract remains `BLOCKED` with 12 unresolved items. Both live downloader attempts failed. Successful mocked transfer proves code behavior under a controlled fixture, not live source availability.

The unchanged IC-11 script matched Git blob `d1663f57387d396ac3a71f117b3e284b49ccc537` and reran 14/14. Its four source-table consistency flags remain unresolved. That fresh report is in the download; the original IC-11 report is untouched. IC-01–10 were not rerun. No independent second reviewer. Publication hashes and GitHub preservation CI are reported separately after writing.

ASRP: source-access failure is an input blocker, not permission to manufacture data; normalization can erase the target scale; an offset selected using a response is calibration, not an independent apparatus measurement; an event-level split is not a new apparatus regime; local checksums and test success cannot certify source truth. We deliberately stopped adding new physical toy models while this empirical step is blocked.

## Immediate next input

Acquire the release README and BL2 event archive through an environment that can access NIST; simulations and ancillary records follow as the README requires. An acquisition-only handoff is in [ADA_HANDOFF.md](ADA_HANDOFF.md). No message or job has been sent to Ada automatically. With those bytes, inspect schema, select a bounded response reproduction and complete the protocol. Until then no event fit, lifetime correction, empirical epsilon or additional ARK-rate conclusion is justified.
