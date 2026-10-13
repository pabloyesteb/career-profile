# Inventory issues requiring review

Inventory date: 2026-10-13.

## User input or additional material needed

1. Locate material for **IN2138 Robot Motion Planning**, if available. The archive **Mobile Robotik (IN2404)** is a different module by both title and code.

The earlier Fundamentals of Optimization for Machine Learning ambiguity is resolved: the user confirmed that `Machine Learnin 950839125 (W25_26)_20261012_1602.zip` is not that course and supplied `fund_opt_ML_CIT413031.zip` as the corresponding material.

The earlier Cognitive Systems ambiguity is also resolved: the user confirmed that `CogSys SS2025_20261012_1559.zip`, internally **Cognitive Systems: Neural Networks and Applied AI (IN2222)**, corresponds to additional-credit **Technical Cognitive Systems / Kognitive Systeme**.

## Configuration and layout observations

- The stale PDF paths, malformed `case_studies` indentation, and missing case-studies PDF entry in `config/sources.yaml` were corrected on 2026-10-13. Configured PDF paths now resolve to the inventoried files.
- Empty source directories `00_sources/pyloworder/` and `00_sources/tum/extracted/` exist. pyLowOrder is correctly available through the configured external repository; no extracted TUM files were relied upon.

## Missing or unmatched material

- No matched TUM ZIP exists for MA8102 Internship, SZ0339 German B2.1, SZ0341 German C1.1, or the additional-credit German B1.2 course. This may be expected for non-lecture or language modules.
- Five valid archives have no transcript match: Advanced Control (MW1420), Approximate Dynamic Programming and Reinforcement Learning, Dynamical Systems (MA3081), Machine Learning and Optimization, and Mobile Robotik (IN2404).
- The confirmed Fundamentals of Optimization for Machine Learning archive contains 23 PDFs: 20 grouped under `MIT_course/` and 3 at archive root. The user described it as combining TUM-course slides with similar MIT material, but slide-level inspection found that the complete 21-lecture sequence is internally branded MIT 6.881 and the remaining two decks are branded MPI-IS Tübingen MLSS and PKU Summer School. No file is internally TUM-branded. The archive-to-course match remains user-confirmed, but which subset was delivered at TUM is unresolved; see `slide_processing_report.md`.
- The thesis and case-studies module use standalone PDFs/repositories rather than TUM course ZIPs; this is recorded as separate source coverage, not missing material.

## Duplicates and packaging observations

- `duplicate_files.csv` contains seven duplicate-content groups detected by identical uncompressed size and ZIP CRC-32. Six groups have two copies and one group has four copies. All occur within a single archive; no cross-archive duplicate group was detected.
- The duplicate list includes a Mobile Robotik pair named as an exercise and a solution but with identical bytes. This could be intentional packaging or a mislabeled file and should be treated cautiously during profiling.
- Several ZIPs contain nested ZIP/IMSCC or other packaged content. The outer members are inventoried; nested packages were not executed or recursively extracted.
- Material-type labels in `archive_files.csv` and `archive_summary.csv` are filename/path heuristics for triage, not claims about course content. Extension counts and member paths remain available for audit.

## Reproducibility cautions

- The Master's thesis repository has 105 Git status entries and the case-studies repository has 6. Their recorded commit hashes alone do not capture uncommitted state; later analysis should record or snapshot the precise dirty-state evidence used.
- pyLowOrder is clean at the recorded revision.
