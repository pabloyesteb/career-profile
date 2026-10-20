# Course profile extraction methodology

Historical reference retained during inventory simplification. Links and source locations have been updated; dated processing statuses and workflow instructions below describe the retired extraction phase. The active registry is `01_inventory/sources.yaml`; document fingerprints remain in the relevant project profiles.

## Purpose and scope

This methodology converts heterogeneous course archives into concise, technically specific, source-grounded course profiles. It records material taught in a completed course; it does not assess personal proficiency. A profile must cover the course actually evidenced by local material and must not be expanded with plausible but unsupported subject matter.

## Evidence hierarchy

Use sources in this order, while allowing lower-ranked sources to add material absent above them:

1. The grade transcript for official module code, title, ECTS, and grade.
2. Comprehensive local lecture notes or a complete ordered slide series for the principal syllabus.
3. Course-specific examination topic lists or syllabus/organization documents for intended coverage.
4. Exercise sheets and solutions for techniques, proof patterns, examples, and applications.
5. Assignments, projects, notebooks, and source code for implementation details and computational tools.
6. Mock or past examinations as a coverage cross-check, not as the sole basis for a topic.
7. Official TUM module descriptions only if local evidence is incomplete or ambiguous.

Do not treat student submissions as authoritative without corroboration. Distinguish materials from another institution or course when an archive contains mixed provenance.

## Workflow

### 1. Establish identity and freeze the evidence set

- Copy transcript metadata into the profile without inferring missing values.
- Record the archive filename and the archive-to-module matching basis.
- Record the archive structure: counts and approximate pages by material type, plus code/data files and nested packages.
- Never execute code from an archive. Inspect it statically.

### 2. Select representative documents

Identify one or more backbone sources that span the course, normally comprehensive notes or the complete slide sequence. Add targeted evidence from:

- examination topic lists, to check intended scope;
- every exercise sheet at least at heading/problem level;
- solutions where needed to identify the actual method used;
- every project/assignment at task level;
- code by filenames, interfaces, dependencies, and algorithmic structure.

Record why each selected source is informative. Page count alone does not determine importance.

### 3. Build a source-to-topic coverage map

Before drafting prose, map every major lecture chapter or slide block to a profile section. This prevents late-course topics from being missed. Mark supplemental topics that appear only in exercises, projects, examinations, or code.

### 4. Extract at technical-concept level

For each topic, capture only supported items:

- mathematical objects, assumptions, formulations, and convergence notions;
- named theorems and what they establish in the course context;
- algorithms, inputs/outputs, invariants, stopping conditions, and complexity where stated;
- discretizations, estimators, approximation spaces, error decompositions, and solvers;
- programming languages, libraries, data structures, and supplied implementations;
- scientific or engineering model problems and use cases.

Prefer names such as “Banach–Steinhaus theorem,” “minimum mean cycle-canceling,” or “Karhunen–Loève truncation” over labels such as “advanced analysis,” “graph methods,” or “simulation.”

### 5. Synthesize hierarchically

Group related content by mathematical or computational relationship rather than copying the lecture calendar. Preserve meaningful distinctions—for example, basic Monte Carlo, multilevel Monte Carlo, and multifidelity Monte Carlo—without repeating common definitions.

Omit template sections that genuinely do not apply. Explicitly state when no programming language or computational assignment is evidenced.

### 6. Cite for verification

- Cite archive members using `archive.zip :: path/inside/archive`.
- Add page or section references for long documents.
- Cite exercise/sheet numbers for content that is absent from the backbone notes.
- Cite code paths for implementation claims.
- Keep transcript metadata citations separate from technical-content citations.

## Validation checklist

A profile is `complete_validated` only after all checks pass:

1. **Identity:** title, code, ECTS, and grade agree with `courses.csv`.
2. **Lecture coverage:** every major chapter or ordered slide block maps to a profile section or an explicit justified exclusion.
3. **Technical depth:** named results, algorithms, mathematical frameworks, and numerical methods are captured where present.
4. **Exercise delta:** every exercise sheet has been checked for topics or applications not apparent in the backbone source.
5. **Computational delta:** assignments and code have been checked statically for languages, implementations, solvers, and numerical experiments.
6. **Assessment cross-check:** exam topic lists or mock exams do not reveal a missing major area.
7. **Traceability:** each major profile section has at least one real source reference.
8. **Restraint:** the profile contains no unsupported proficiency claims, inferred projects, or generic padding.

## Pilot findings about the method

- A comprehensive script plus an exercise audit is efficient for theorem-based courses.
- For algorithm courses, code skeletons and exercise sheets materially improve the profile by revealing implemented algorithms and applications.
- For numerical courses, a current exam-topic list is a strong independent check on long lecture notes, while static code inspection reveals discretization and solver details that prose alone may not expose.
- Archive-level material labels are useful for triage but cannot replace document inspection; filenames and extensions can be misleading.
