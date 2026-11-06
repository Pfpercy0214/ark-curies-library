# IC-02 — Sources, versions and access limits

Date accessed: 2026-10-31, America/Chicago. Exact historical snapshot: `6ba49695728756d7359b8551f2118da8befa6896` on the unmerged IC-01 research branch. Historical paper contents at this snapshot retain the archival merge versions.

## Historical sources (not empirical confirmation)

- **P18:** [Paper XVIII](https://github.com/Pfpercy0214/ark-curies-library/blob/6ba49695728756d7359b8551f2118da8befa6896/raw/papers/paper-018-recursive-scalar-geometry-conv-01.md), section 2.2, with sections 2-3 inspected for alternative definitions and update rules. Supplies the integrated kappa*dtheta relation. It does not establish compatibility with every later meaning of tau.
- **P22:** [Paper XXII](https://github.com/Pfpercy0214/ark-curies-library/blob/6ba49695728756d7359b8551f2118da8befa6896/raw/papers/paper-022-electromagnetism-conv-01.md), section II and nearby electromagnetic definitions. Git blob `4fa684d6c757d4e460c7c9944796cf90175e9f4b`. Supplies the direct product bridge and ideal-solenoid gauge/geometry convention. Its printed inverse is not used; IC-01's inconsistency remains documented.
- **P25:** [Paper XXV](https://github.com/Pfpercy0214/ark-curies-library/blob/6ba49695728756d7359b8551f2118da8befa6896/raw/papers/paper-025-disciplined-containment-conv-01.md), Appendix A.1-A.7 and D.1, with scope/falsifiability passages in section 12 inspected. Git blob `3bbf2a40a7c4bdde67f4bbeb2a29147f10a036f5`. A.1 defines theta through proper/coordinate time; A.3's boundary-stress definition is not silently equated to the XVIII memory variable. D.1 is used only for formal substitution, not numerical environmental inference.
- **C1:** [Epistemic charter v1.1](https://github.com/Pfpercy0214/ark-curies-library/blob/6ba49695728756d7359b8551f2118da8befa6896/raw/epistemics/ARK_Epistemic_Charter_v1.1.md), sections 5.2-8.4 re-read. Governs independent measured inputs, calibration, uncertainty, model flexibility and incomplete PDE closures; does not validate the physics.
- **I1:** [IC-01](../investigations/identity-containment-01/README.md) and its handoff/route map. Existing code matched Git blob `49c0868dc0731a99b574f1af1be7e00c09655a4b`; 12 tests rerun locally. This is a previous same-assistant calculation, not independent evidence.

## External primary sources

### E1 — Actual optical-clock comparisons

C. W. Chou, D. B. Hume, T. Rosenband, D. J. Wineland, **Optical Clocks and Relativity**, Science 329(5999), 1630-1633 (2010), DOI [10.1126/science.1192720](https://doi.org/10.1126/science.1192720).

Accessed the authors' abstract via [PubMed](https://pubmed.ncbi.nlm.nih.gov/20929843/) and the [NIST publication record](https://www.nist.gov/publications/relativity-and-optical-clocks). The abstract reports optical-clock comparisons revealing effects of relative speeds below 10 m/s and elevation differences below 1 m, with an optical-fiber comparison link. This establishes a real clock-ratio observable. It does not measure ARK tau or electromagnetic kappa, or demonstrate any of the proposed cross-domain equivalences.

Access limit: no full-paper equations, experimental series or raw data were analyzed in IC-02. No reported measurement was inserted into the numerical fixture. NIST's record has a different displayed title/journal metadata; Science citation and DOI were cross-checked against PubMed rather than copying the inconsistent journal label.

### U1 — Correlated measurement uncertainty

B. N. Taylor and C. E. Kuyatt, NIST Technical Note 1297, **Guidelines for Evaluating and Expressing the Uncertainty of NIST Measurement Results**, [Appendix A, law of propagation of uncertainty](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-appendix-law-propagation-uncertainty).

Read the official HTML treatment of equations A-1 through A-3 and its explanation of covariance and first-order Taylor approximation. Used to structure sensitivity/covariance propagation; this is not a numerical dataset or an ARK endorsement. Near degeneracy or strong nonlinearity, a first-order uncertainty expression is not automatically adequate.

### M1 — Dynamic observability/identifiability methodology

A. F. Villaverde, A. Barreiro, A. Papachristodoulou, **Structural Identifiability of Dynamic Systems Biology Models**, PLOS Computational Biology 12(10), e1005153 (2016), DOI [10.1371/journal.pcbi.1005153](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005153).

Read the primary article's abstract, introduction and observability/identifiability methodological passages. Provides context for analyzing the full dynamic observation map rather than counting measured labels. IC-02 does not claim to have run STRIKE-GOLDD, reproduced the paper's biological examples, or proved global identifiability of ARK. Its explicit scaling and monotonicity calculations are supplied independently in the present work.

## Evidence status

No physical scalar calibration, apparatus dataset, decay-rate measurement or experimental validation was performed. The numerical data in IC-02 are manufactured test fixtures. Third-party text is not copied into the repository beyond citations and original short source notes. No PDF was downloaded or source-page conversion audited in this pass.
