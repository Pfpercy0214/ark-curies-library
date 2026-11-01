# IC-11 primary-source and access record

Access date: 2026-11-01. These are bibliographic/provenance records and numerical transcriptions, not claimed local copies of inaccessible data.

## S1: publication and version

J. Caylor et al., *Detection of molecular hydrogen in a neutron beam lifetime experiment*, Phys. Rev. C 112, 065501 (12 December 2025), DOI 10.1103/nr3b-3dtl.

- NIST publication record: https://www.nist.gov/publications/detection-molecular-hydrogen-neutron-beam-lifetime-experiment
- Primary author HTML, version actually used: https://arxiv.org/html/2506.01682v2
- The arXiv identifier explicitly dates v2 to 12 December 2025. Its HTML also displays a later render date; this was not treated as a new publication/version.
- Read apparatus and inference sections I–VII, including Equations 1–5 and Tables 1–4, figure captions and the authors' interpretation. No figure pixels were digitized and no event spectra were refitted.
- Original v1 HTML was consulted while locating the paper but all tabulated inputs in this study use v2. No v1 numbers were mixed into the CSV.
- NIST PDF https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=959779 and arXiv PDF https://arxiv.org/pdf/2506.01682v2 exceeded the web tool's retrieval size limit (approximately 11.9 MB). No PDF pages or screenshots could be accessed; claims are based on native HTML, not PDF inspection.

## S2: experimental data release located, not downloaded

NIST dataset ID mds2-3859, public data associated with the paper:

- Landing page: https://data.nist.gov/od/id/mds2-3859
- Government catalog: https://catalog.data.gov/dataset/data-used-in-writing-detection-of-molecular-hydrogen-in-a-neutron-beam-lifetime-experiment
- README: https://data.nist.gov/od/ds/mds2-3859/README.txt
- BL2 events: https://data.nist.gov/od/ds/mds2-3859/BL2data.zip
- BL2 simulations: https://data.nist.gov/od/ds/mds2-3859/BL2Simulations.zip
- BL1 records and simulations: https://data.nist.gov/od/ds/mds2-3859/BL1simanddata.zip
- RGA record: https://data.nist.gov/od/ds/mds2-3859/RGA_data.txt

The government catalog was read and identifies energies/times, earlier experiment records, simulations and RGA data. The NIST landing page rendered only its loading shell in the web tool. README and BL2 ZIP requests failed after redirecting to `nist-oar-cache.s3.amazonaws.com/prd/fst4/mds2-3859/`; direct cache attempts also failed. Generic container HTTP failed DNS resolution. The download tool failed for the NIST release, cache and article HTML. We did not obtain event bytes, a README content description, original raw-file hashes, calibrated channel definitions, or event-level uncertainties. The remaining distribution URLs above are cataloged, not all separately retried. Do not claim their individual availability was tested.

The catalog states first publication 10 July 2025 and file metadata last modified 30 May 2025; these are metadata, not dates of observations. The paper dates the pertinent observations to 2018–2020. No current-status conclusion about the entire dataset repository follows from this session's access failures.

## Numerical transcription contract

- [Standard response CSV](../investigations/identity-containment-11/published_response.csv): Table 2's 30 proton rows paired with Table 3's 30 molecular rows; one combined row per detector/acceleration setting. Input energies for half-proton simulations are doubled to identify equal full acceleration settings. Loss fractions and printed efficiencies remain separate columns. Percent units are divided by 100 in calculation, not confused with fractions.
- [BL1 response CSV](../investigations/identity-containment-11/bl1_response.csv): 13 Table-4 series, including threshold, efficiencies and printed difference. Repeated detector settings across different series are preserved, not counted as new independent measurements.
- Source table caption text is not reproduced wholesale. CSV column names are our normalization. Values were manually transcribed from the tool's native HTML table and checked against that table during construction; this is not an independent second-person transcription or a PDF check.
- The Table-2 20 microgram/cm2, 35 keV stopped-fraction cell prints `0000`; it is represented as numeric zero, with this formatting decision recorded. `30 .0` is represented as 30.0. No nonzero value was inferred or repaired.
- Table 4 explicitly associates zero gold areal density with PIPS. This is not a zero silicon-oxide deadlayer.
- Four Table-3 efficiencies do not overlap the displayed component-sum intervals under a nearest-rounding assumption; these remain unresolved and are listed in the study and executable results. Calculations preserve printed and component-derived variants. This is not a determination of error in the original experimental analysis.
- Hashes in our test report identify these CSV transcriptions, not original NIST files or article bytes. No fabricated external checksum is supplied.

## Publication context not overridden by this benchmark

S1 identifies hydrogen composition rather than total pressure alone as relevant. It warns that trap-local density/thermal conditions are not measured directly by the remote vacuum diagnostics. Table response estimates depend on detector, acceleration and threshold. Its BL1 analysis reports no observed molecular signal above an approximate one-percent sensitivity and a worst-case shift below 0.5 s (around -0.3 s in its specific calculation). We did not reproduce that weighting or correction; deliberately chosen large-response settings are not the BL1 setting list.

## Attribution and reuse

Numerical facts are attributed to the authors and NIST. This package contains only the transcribed response numbers, our code and commentary, not the complete article or figures. The dataset catalog points to https://www.nist.gov/open/license ; that NIST use/attribution statement was read. We make no representation that NIST endorses ARK, our derived calculations, or these transcriptions.

## Repository context actually read

Pinned head: 9656f14ff1632cfae28252c4e259fad01d039798. Read AGENTS, entry protocol, POLICIES, charter v1.1 sections 4–6.9, IC-10 README, current investigation index and PR #2 status. IC-10 code from the mounted packet was hash-matched and executed. No complete paper-corpus reread, fresh source-PDF review or new validation of the archived neutron equation. Charter blob: ae341b2a7e30fc1d25703a1f6dbc032595fec707. All new work stays outside raw/.
