# Stage 2 course-profiling pilot report

Historical reference retained during inventory simplification. Links and source locations have been updated; dated processing statuses and workflow instructions below describe the retired extraction phase. The active registry is `01_inventory/sources.yaml`; document fingerprints remain in the relevant project profiles.

Pilot completed: 2026-10-13. Scope was limited to three courses; no thematic knowledge-base files were created.

## Pilot selection

1. **MA3001 Functional Analysis** — selected as the mathematically intensive case. Its 94-page core script covers a theorem-heavy progression from Banach and Hilbert spaces through weak convergence, Sobolev spaces, Fredholm theory, spectral theory, and compact-operator decomposition. Fourteen sheet/solution pairs make it possible to validate the abstract syllabus against proof problems.
2. **MA4502 Combinatorial Optimization** — selected as the extensive exercise/solution case. It has a consolidated script, fourteen dated note sets, eleven official sheet/solution pairs, and student exercise material. The problems cover algorithms, correctness arguments, complexity, reductions, and applications across the complete lecture sequence.
3. **MA5348 Numerical Methods for Uncertainty Quantification** — selected as the computational-assignment case. It combines long-form notes and slides with five substantial problem/solution sets, nine loose MATLAB files, and two MATLAB packages implementing random-field, finite-element, Monte Carlo, multilevel, and stochastic Galerkin workflows.

All three are exact archive-to-transcript matches with sufficient local evidence. No official web module descriptions were needed.

## Material reviewed

| Course | PDFs and approximate volume | Exercises/solutions | Computational material | Backbone used |
|---|---:|---|---|---|
| MA3001 Functional Analysis | 33 PDFs, ~189 pages | 14 sheets + 14 solutions; mock exam + solution | None evidenced | 94-page script + 10-page current supplement |
| MA4502 Combinatorial Optimization | 52 PDFs, ~523 pages | 11 official sheets + solutions; 15 student submissions structurally inspected | 27 Python files across six exercise sets | 96-page consolidated script; dated notes as cross-check |
| MA5348 Numerical Methods for UQ | 33 PDFs, ~573 pages | 5 sheets + 5 solutions; oral-exam topic list | 9 loose MATLAB files; 2 packages with 16 MATLAB members, partly duplicated | 109-page notes + 37-page MLBLUE supplement + ordered lecture decks |

The review inspected every major lecture chapter/block, every official exercise sheet at problem-heading level or deeper, solutions where method identification was needed, and all code statically. Untrusted course code was not executed.

## Outputs

- Reusable template: `02_profiles/courses/_template.md`
- Extraction and validation method: `docs/legacy_inventory/course_profile_methodology.md`
- Functional Analysis: `02_profiles/courses/ma3001-functional-analysis.md`
- Combinatorial Optimization: `02_profiles/courses/ma4502-combinatorial-optimization.md`
- Numerical Methods for Uncertainty Quantification: `02_profiles/courses/ma5348-numerical-methods-uncertainty-quantification.md`

The three `processing_manifest.csv` rows are now marked `complete_validated`.

## Validation results

- Transcript title, code, credits, and grade were checked against `courses.csv` for all three profiles.
- Coverage tables map every backbone chapter to a profile section.
- The Functional Analysis exercise/mock-exam audit confirmed the thirteen core chapters and added the current distribution-theory supplement, integral-equation use of Neumann series, and concrete spectral/Fredholm examples.
- The Combinatorial Optimization audit confirmed all four lecture chapters and added Python implementations, reductions, dynamic programming, disjoint-path, assignment, and route-inspection applications.
- The NUMUQ oral-exam list independently confirmed Chapters 1–10. Exercises/code added practical covariance sampling, KLE collocation, finite-element Monte Carlo, MLMC rate estimation, confidence intervals, matrix-free stochastic Galerkin products, and preconditioned CG. Dedicated slides added MLBLUE, which is outside the consolidated notes' main chapter list.
- Each major technical section now has a document, chapter/page, sheet, or code-path reference.

## Difficulties and decisions

- The Functional Analysis backbone is an older TUM script (WS 2017/18) inside the WS 2024/25 archive. Current sheets, the WS 2024/25 supplement, and mock exam closely track it, so it was retained with the date discrepancy stated explicitly.
- The Combinatorial archive includes substantial dated class notes and student submissions. The consolidated script and official exercises were preferred to avoid duplicate coverage and unverified student-authored claims.
- Several NUMUQ PDFs lack a `.pdf` extension, and its nested ZIPs duplicate some loose MATLAB files. File signatures and archive structure, rather than filename extensions alone, were used for volume counts.
- Mathematical PDF extraction occasionally degrades symbols. Claims were checked against surrounding definitions, section headings, exercises, and source code rather than copied from isolated OCR fragments.
- Supplied code sometimes carries attribution to external academic software. Profiles describe the code as course material and do not claim student authorship.

## Method improvements proposed

- Preserve the two-pass method: backbone syllabus mapping followed by an exercise/code delta audit.
- Require a source-to-topic coverage table in every profile; it exposed MLBLUE as otherwise easy to miss.
- Extend the new lightweight pilot validator beyond its current metadata, status, required-section, profile-link, and primary archive-member checks when scaling to all courses.
- Record analyzed source members and page counts in a machine-readable per-course evidence manifest if later batches become large.
- For slide-only or image-heavy courses, add page rendering/OCR selectively and record OCR confidence rather than assuming text extraction is complete.

## Unresolved issues

- No content-level blocker remains for these three pilot profiles.
- The Functional Analysis backbone-date discrepancy should remain visible in future use.
- The profiles record course coverage, not proficiency or individual authorship of supplied code.
