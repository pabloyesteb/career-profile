# Academic material inventory summary

Inventory date: 2026-10-13. Scope is limited to source discovery and structural inventory; no course content or profile analysis was performed.

## Transcript

The authoritative source is the six-page TUM grade report dated 7 October 2026, available at `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf` (SHA-256 recorded in `files_manifest.csv`). It lists:

- 18 completed degree modules/achievements totaling **123 ECTS**: one thesis (30), twelve graded subject modules (68), one graded case-studies module (10), one pass/fail seminar (3), one pass/fail internship (6), and two graded language modules (6).
- 3 completed additional-credit courses totaling **14 ECTS**. These are kept distinct because the report states that they do not count toward the degree result.
- Official module-level names, codes where supplied, credits, grades, transcript section, and archive status are transcribed in `courses.csv`. `BE` is preserved as the transcript's pass mark rather than converted to a numeric grade.

The 123-ECTS degree total and 14-ECTS additional-credit total recompute exactly from the inventory.

## TUM course archives

There are **19 ZIP archives**, totaling 4,059,476,364 bytes (about 3.8 GiB), with **997 regular file members** and 4,317,450,356 uncompressed bytes. Every ZIP passed a full integrity read. No encrypted members, symlinks, or unsafe paths were found.

The archive collection includes lecture notes/slides, exercise sheets, solutions, exams, projects/assignments, code/notebooks, datasets, media, course administration pages, and nested packages. Exact member paths, sizes, CRCs, extensions, and heuristic material labels are in `archive_files.csv`; per-archive counts and top-level organization are in `archive_summary.csv`.

Matching results:

- **12 exact matches** to transcript modules, based on common module code and/or a distinctive exact title.
- **2 user-confirmed matches**: `fund_opt_ML_CIT413031.zip` for additional-credit Fundamentals of Optimization for Machine Learning, and Cognitive Systems: Neural Networks and Applied AI (IN2222) for additional-credit Technical Cognitive Systems. The Fundamentals archive has 23 PDFs—20 under `MIT_course/` and 3 at archive root. Later slide-level inspection found internal branding for MIT 6.881, MPI-IS Tübingen MLSS, and PKU Summer School, but no internally TUM-branded deck; the archive match is confirmed while TUM-specific delivery provenance remains unresolved.
- **5 unmatched archives**: Advanced Control (MW1420), Approximate Dynamic Programming and Reinforcement Learning, Dynamical Systems (MA3081), Machine Learning and Optimization, and Mobile Robotik (IN2404). The user explicitly confirmed that Machine Learning and Optimization is not the Fundamentals course.

The full evidence and rationale for every archive is in `archive_matches.csv`.

## Non-archive sources

- Master's thesis: accessible 98-page PDF and accessible Git repository at revision `57efc6aa6119cd5ae969ed83fc67efcb40c71672`; repository is dirty.
- Scientific article: accessible 17-page PDF.
- pyLowOrder: accessible, clean Git repository at revision `f79ad1d67660eb9502c17398aa5c196cda90cc97`.
- Previous CV: accessible one-page PDF.
- Case Studies Optimization: accessible 60-page PDF and accessible Git repository at revision `934956c78c03d5581505a50652b2ab4302e6baa5`; repository is dirty.

Repository paths, branches, revisions, dirty-state counts, and origins are in `repositories.md`. PDF hashes and page counts are in `files_manifest.csv`.

## Inventory artifacts

| File | Purpose |
|---|---|
| `courses.csv` | Authoritative transcript module catalog |
| `archive_matches.csv` | Archive-to-module matching decisions and evidence |
| `archive_summary.csv` | Per-archive structure, material categories, size, and safety/integrity results |
| `archive_files.csv` | Complete member-level ZIP inventory |
| `duplicate_files.csv` | Probable exact duplicate groups within the ZIP collection |
| `files_manifest.csv` | Source PDF/ZIP locations, sizes, hashes, and configuration status |
| `repositories.md` | External repository access and revisions |
| `processing_manifest.csv` | Per-course inventory/profile state and next action |
| `review_issues.md` | Missing sources, ambiguities, inconsistencies, and questions |

## Readiness for profiling

Inventory is complete and internally validated. Profiling can begin for the 12 exact archive matches, the two user-confirmed matches, and the separately sourced thesis and case-studies module. Preserve the internally evidenced MIT/MLSS/PKU provenance and the unresolved TUM-delivery question when using the Fundamentals profile. Obtain IN2138 material if possible. The formerly stale source paths and malformed Case Studies entry in `config/sources.yaml` have been corrected.
