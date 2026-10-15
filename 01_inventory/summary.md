# Academic material inventory summary

Latest status — supplementary integration (2026-10-15): **16 definitive course + four definitive project + five supplementary material profiles = 25 corpus profiles**. The 20 definitive profiles, 21 transcript entries, 123 degree ECTS and 14 additional ECTS are unchanged. All five previously unmatched archives are identified and processed as user-authorized supplementary academic materials; no transcript matches were fabricated. `academic_credit: not_established` and `learning_relationship: unspecified` apply to all five. Their source IDs remain unchanged; `supplementary_processing_manifest.csv` tracks selective topic-map completion separately from the transcript-only manifest. Older requests for inclusion decisions below are superseded, not a reason to discard these sources. The expanded corpus is ready for source-qualified thematic synthesis; each supplementary profile identifies valuable documents for optional deeper extraction.

Latest status — IN2138 update (2026-10-15): **20 definitive profiles: 16 courses and four projects**. All 18 non-language transcript entries are `complete_validated`; three language entries remain `metadata_only`. IN2138 is now documented by `in2138_official_syllabus`, with explicit Summer Semester 2024 and syllabus-only limitations; no ZIP match is claimed. This supersedes older missing-source/count statements below. Five unmatched archives remain potentially relevant and need scope decisions, not automatic dismissal. Exact filenames/absolute paths and existing content evidence are in `profiles_completion_review.md` §5. No confirmed-scope profiling blocker remains.

Scientific-reference update (2026-10-15): `pyloworder_dlr_reference` is registered in `config/sources.yaml` and `files_manifest.csv`; its complete 14-page DLR paper informs the existing validated pyLowOrder profile. It is neither the user's coauthored article nor an additional project/profile. Totals remain 15 course and four project profiles. The available-source profiling phase can close for synthesis with IN2138's documented source gap and unmatched archives outside confirmed scope; see the current completion review.

Current reconciled processing status (2026-10-14): **19 definitive profile documents** exist: 15 courses and four projects (scientific paper; thesis; pyLowOrder; Case Studies Optimization). All 21 transcript entries are accounted for: 17 `complete_validated`; one `blocked_missing_source` (IN2138); three `metadata_only` language entries. CIT413042 now links its preserved course profile and definitive project profile, describing the same academic work once; the original final report is registered alongside its identical local copy. MA8102 remains covered by pyLowOrder. Five unmatched archives remain outside the transcript-confirmed scope. The extra project document adds no academic record or credits. See `profiles_completion_review.md` and `processing_manifest.csv`; earlier stage reports remain historical. Internal reports under `02_profiles/projects/_analysis/` do not count as definitive profiles. The findings below describe the original inventory stage.

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

- Master's thesis: accessible 98-page final PDF, 70-page final-presentation PDF with notes, final-presentation LaTeX source, and accessible Git repository at revision `57efc6aa6119cd5ae969ed83fc67efcb40c71672`; repository is dirty with 105 status entries.
- Scientific article: accessible 17-page PDF.
- pyLowOrder: accessible, clean Git repository at revision `f79ad1d67660eb9502c17398aa5c196cda90cc97`.
- Previous CV: accessible one-page PDF.
- Case Studies Optimization: accessible original 60-page final PDF at `/home/pablo/TUM/SoSe 25/Case Studies/Trajectories-4.pdf`, byte-identical to preserved local copy; existing repository at `934956c78c03d5581505a50652b2ab4302e6baa5` with untracked material. Both course and project profiles now exist for the same CIT413042 work.

Repository paths, branches, revisions, dirty-state counts, and origins are in `repositories.md`. Configured file hashes, PDF page counts, and the presentation-source record are in `files_manifest.csv`.

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

## Historical readiness for profiling

Inventory is complete and internally validated. Profiling can begin for the 12 exact archive matches, the two user-confirmed matches, and the separately sourced thesis and case-studies module. Preserve the internally evidenced MIT/MLSS/PKU provenance and the unresolved TUM-delivery question when using the Fundamentals profile. Obtain IN2138 material if possible. The formerly stale source paths and malformed Case Studies entry in `config/sources.yaml` have been corrected.

The paragraph above records original inventory readiness; those available-material profiles are now completed. Current readiness for thematic synthesis and the distinction between missing-source closure and optional improvements are assessed in `profiles_completion_review.md`.
