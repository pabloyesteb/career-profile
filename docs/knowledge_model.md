# Knowledge model for Career Profile

Status: **approved architecture; implemented knowledge base accepted as iteration zero on 2026-10-18**. The current representation is usable for downstream work; remaining optional editorial improvements are not prerequisites. The original design, examples and implementation plan below are retained as historical context, not pending approval or instructions to restart extraction. [AGENTS.md](../AGENTS.md) governs revisable interpretation, user-controlled positioning and progressive retrieval.

## 1. Goals, boundaries and inputs

Build a reusable technical reference that answers both “what does this method mean?” and “what evidence supports this person's experience with it?” Preserve equations, assumptions, algorithm variants, numerical contracts, engineering choices, results and limitations. Support technical retrieval/interview preparation and evidence selection for a later master profile, CV, cover letter or LinkedIn update.

Do not prewrite role-specific narratives, score proficiency, infer personal implementation from course resources, or turn every source mention into a competency. Do not add a database, embeddings, external service, source-ingestion framework or a second copy of the academic inventory. `02_profiles` remains the authoritative extraction layer; `03` consolidates it. Original sources and external repositories need not be reopened for the initial synthesis.

Reviewed the structure, technical-topic sequences, representative technical passages and evidence/limitation conventions of all **25 definitive/supplementary inputs** below. Internal `_analysis` reports and the course template are not additional synthesis inputs. The corpus comprises 16 course documents, four project documents and five supplementary maps. It represents **24 distinct technical experience/source groups**, because the Case Studies course and project documents describe the same academic work. Thesis/MA6018 and pyLowOrder/MA8102 must likewise retain their existing academic associations, not become duplicate achievements. Language metadata is outside this technical-profile corpus.

### Corpus coverage and model implications

All links in this table point to existing profiles, not proposed knowledge files.

| Input profile | Technical breadth / modeling implication |
|---|---|
| [Functional Analysis](../02_profiles/courses/ma3001-functional-analysis.md) | Banach/Hilbert spaces, duality, weak compactness, distributions/Sobolev spaces, Fredholm/spectral theory; preserve theorem assumptions and infinite-dimensional setting. |
| [Foundations of Data Analysis](../02_profiles/courses/ma4800-foundations-of-data-analysis.md) | Projections, SVD/PCA, concentration, Johnson–Lindenstrauss, conjugacy; distinguish finite-dimensional algorithms from operator theory. |
| [Numerical UQ](../02_profiles/courses/ma5348-numerical-methods-uncertainty-quantification.md) | Random fields, uncertain elliptic PDEs, FEM, Monte Carlo/MLMC, stochastic Galerkin; retain discretization and statistical errors separately. |
| [Nonlinear Optimization](../02_profiles/courses/ma3503-nonlinear-optimization.md) | Constraint qualifications, KKT, second-order conditions, penalties, augmented Lagrangians and SQP; exercise-grounded rather than full-lecture extraction. |
| [Combinatorial Optimization](../02_profiles/courses/ma4502-combinatorial-optimization.md) | Matroids/MST, flows, matching, complexity; retain discrete algorithm guarantees. |
| [Case Studies course](../02_profiles/courses/cit413042-case-studies-optimization.md) | Direct transcription, robot models, learned SDFs, constrained NLP; link to the same experience's project view. |
| [Statistical Learning](../02_profiles/courses/ma4802-statistical-learning.md) | Inference, regularization, validation, trees/boosting, kernels, mixtures/EM, representations and causal models; distinguish taught examples from personal coding. |
| [Deep Generative Models](../02_profiles/courses/cit4230003-advanced-machine-learning-deep-generative-models.md) | Flows, variational inference/VAE, GAN, diffusion, conditional flow matching; do not flatten distinct objectives. |
| [NLP](../02_profiles/courses/in2361-natural-language-processing.md) | Language/sequence models, transformers, alignment, retrieval, parsing and semantics; preserve historical/current and unavailable-practical qualifications. |
| [Robot Motion Planning](../02_profiles/courses/in2138-robot-motion-planning.md) | Configuration spaces, roadmaps/PRM/RRT, filtering and SLAM; syllabus-only evidence, Summer Semester 2024 edition qualification. |
| [Humanoid learning](../02_profiles/courses/ei7263-biologically-inspired-learning-humanoid-robots.md) | CMAC, internal models, biological action selection, RL-DT, SOM, distributional-value presentation; presentation attribution differs from supplied code. |
| [Computational Neuroscience](../02_profiles/courses/ei7646-computational-neuroscience.md) | Neural coding/plasticity, probabilistic perception, bioelectronics, neuroprostheses, auditory and attractor models; retain non-ML scientific breadth. |
| [Deep RL](../02_profiles/courses/mgt001299-introduction-to-deep-reinforcement-learning.md) | Search, MDP/TD, DQN variants, policy gradients, PPO, DDPG/SAC; supplied code and source defects are not successful personal experiments. |
| [MLMC seminar](../02_profiles/courses/ma6015-advanced-seminar-course.md) | Multilevel/multifidelity estimators, BLUE, sensitivity and rare events; participant presentations and missing advertised topics remain qualified. |
| [FOML](../02_profiles/courses/additional-foml-fundamentals-of-optimization-for-machine-learning.md) | Convex/nonconvex, proximal/minimax, Wasserstein/Riemannian optimization and training; supplied coverage exceeds established TUM-delivery provenance. |
| [Technical Cognitive Systems](../02_profiles/courses/additional-cognitive-systems-technical-cognitive-systems.md) | Spiking computation, cognition, ACT-R, neurorobotics, RL and language/quantization/RAG; separate conceptual exposure, supplied notebooks and implementations. |
| [Thesis](../02_profiles/projects/thesis.md) | Impedance-aware NMPC, quaternion geometry, multirate simulation, progress/recovery and sensitivity studies; preserve reported-result and classifier-bug qualifications. |
| [pyLowOrder](../02_profiles/projects/pyloworder.md) | Attributable mesh/graph/GNS, batching, scaling, typed experiments and reproducibility engineering; DLR reference results are third-party, not user benchmarks. |
| [NGValidation](../02_profiles/projects/ngvalidation.md) | Surrogate assurance, split geometry, residual/tail analysis, uncertainty and configurable reporting; distinguish 2025 paper from 2023 code and specific authored changes. |
| [Case Studies project](../02_profiles/projects/case_studies_optimization.md) | SDF/optimal-control integration, SIREN/Hausdorff contributions, team experiments; shared experience, different claim-level attribution. |
| [Supplementary control](../02_profiles/supplementary/advanced_control.md) | State feedback/LQR, observers, decoupling, disturbances, zero dynamics; content, not accredited completion. |
| [Supplementary ADPRL](../02_profiles/supplementary/approximate_dynamic_programming.md) | Bellman operators, projected evaluation, TD/GTD/LSTD and off-policy learning; exact assumptions may need deeper extraction. |
| [Supplementary dynamics](../02_profiles/supplementary/dynamical_systems.md) | Manifolds, normal forms/bifurcations, chaos, invariant measures, mixing and entropy; preserve mathematical topics outside target job sectors. |
| [Supplementary ML](../02_profiles/supplementary/machine_learning.md) | EI71058 regression/kernels, learning theory, optimization, CNNs and data curation; distinct from FOML. |
| [Supplementary robotics](../02_profiles/supplementary/mobile_robotics.md) | IN2404 geometry, estimation, SLAM, mapping, MPC and planning/RL; distinct from IN2138. |

Recurring information: definitions and model assumptions; theorem/convergence/complexity statements; formulations and algorithms; code/data structures and numerical interfaces; tools; engineering decisions; test protocols; quantitative/negative findings; source discrepancies and future work. Recurring relationships include shared mathematical foundations, method variants, competing representations, common software patterns, and the same method used in different physical applications.

## 2. Architecture comparison and recommendation

| Criterion | A. Markdown-first, metadata and links | B. Markdown + explicit YAML evidence |
|---|---|---|
| Technical depth | Excellent for derivations and explanation | Equally strong: mathematical narrative remains Markdown |
| Maintenance | Lowest initial overhead; prose citations easy | Small structured layer to maintain; IDs/fields need checking |
| Retrieval | Text search/headings/tags; attribution filtering largely manual | Text search plus exact filtering by concept, provenance, actor and claim type |
| Traceability | Usually paragraph citations; easy to lose qualifiers when reusing text | Reusable bounded claims with source locators and inseparable limits |
| Duplication | Theme pages tend to repeat concepts/experience prose | Canonical concepts, shared experience registry and referenced evidence |
| Decisions/results | Flexible prose, weak uniformity | Typed payloads preserve comparisons, units, experimental context and attribution |
| Complexity | Few conventions, more interpretation downstream | Four entity types, simple YAML; no database or graph engine |

**Recommend B:** Markdown-first technical reading with a minimal YAML evidence spine. The corpus's third-party DLR results, thesis-reported outcomes, paper/code discrepancies, course/project overlap and supplementary provenance justify explicit relationships. A pure Markdown approach is viable but would require readers to reconstruct those boundaries repeatedly when preparing applications. A third storage architecture offers no demonstrated advantage at this scale.

One source of truth per fact: concept explanations in concept Markdown; capability statements in competency Markdown; provenance/profile mappings in the experience registry; experience-specific assertions/results/decisions in evidence YAML. Theme pages are navigational synthesis, not another store of detailed claims.

## 3. Minimal data model

Four entity types; no separate theorem, algorithm, tool, decision, result, lesson, job-sector or document entities initially.

| Entity | Purpose | Required fields | Optional fields/content |
|---|---|---|---|
| **Concept** | Explain a reusable theory, model, method or coherent method family | `id`, `title`, `domains`, `evidence_refs`, `status`; Markdown technical explanation | `aliases`, typed `relations`; assumptions, equations, algorithm/pseudocode, guarantees, variants, implementation considerations and applications |
| **Experience/source group** | Identify where evidence comes from, without repeating profiles | `id`, `title`, `profiles`, `facets`, `academic_credit`, `learning_relationship`, `limitations` | Existing academic/source/project IDs, associated module, original revision/hash references already recorded in profiles, disclosure restrictions |
| **Evidence claim** | A scoped, verifiable assertion about content, action, decision, result or observation | `id`, `experience`, `kind`, `concepts`, `statement`, `basis`, `actor`, `verification`, `references`, `limitations` | `tools`, implementation details, decision/result/lesson payload; optional `related_claims` |
| **Competency** | State a bounded professional capability supported by personal work | `id`, `title`, `concepts`, `evidence_refs`, `status`; Markdown scope/engineering explanation | Tools, operating context and exclusions; no self-assigned skill score |

`status` is the **knowledge-extraction** lifecycle `draft` or `reviewed`, not a new academic processing state and not empirical verification. The source profiles' `complete_validated` status is not renamed or inherited as proof that tests passed.

### Identifiers and references

- Concepts and competencies: lowercase descriptive IDs such as `neumann-series`, `nonlinear-model-predictive-control`, `geometry-conditioned-message-passing`, `scientific-ml-software`. IDs survive title/path changes; filename normally matches ID.
- Experiences retain existing IDs: `ma3001`, `ma6018`, `ma8102`, `cit413042`, `scientific_paper`; supplementary groups retain `tum-*` source IDs. NGValidation's displayed name does not replace its stable `scientific_paper` ID. `thesis`, `pyloworder` and `case_studies_optimization` are aliases/associated project IDs, not new experiences.
- Evidence claims: `<experience-id>:<descriptive-claim-id>`, e.g. `ma8102:seed-target-alignment`. Namespace entity types separately; use explicit fields rather than guessing entity type from an ID.
- Every reference contains repository-root-relative `profile` and exact `section` text. Optional `locator` carries a table row, equation, named function, original page or commit **as already cited in that profile**. No original source is reanalyzed to fill a design/example gap. Markdown links help humans; IDs/locators support checking.
- `profiles` entries contain `path`, provenance `category`, and the content `sha256` captured during future extraction. This detects stale syntheses; no illustrative hash is fabricated here. Evidence references must point to a profile registered under their experience.

### Provenance and evidence semantics

An experience can have multiple facets: Case Studies is both accredited coursework and documented project work. **Each profile reference** has one of `accredited_coursework`, `documented_project_work`, `supplementary_academic_material`. A claim references the facet that supports it. This avoids assigning one exclusive category to a mixed experience.

The following dimensions are independent, not a ranking:

| Field | Values / meaning |
|---|---|
| `kind` | `knowledge`, `implementation`, `contribution`, `decision`, `result`, `lesson`; `contribution` covers explicitly attributed non-code work such as mathematical formulation, experimental design, visualization or technical presentation |
| `basis` | `course_material`, `project_code`, `project_report`, `external_reference`, `supplementary_material`; split a claim when bases support materially different assertions |
| `actor` | `user`, `team`, `third_party`, `unspecified`, `not_applicable`; attribution is claim-specific, not inferred from membership |
| `verification` | `not_applicable`, `statically_documented`, `reported_not_reproduced`, `independently_reproduced`; last value only if an input profile explicitly establishes it |

Accredited coursework establishes taught knowledge, not independently authored code. Supplementary material enriches technical content with `academic_credit: not_established`, `learning_relationship: unspecified`; supplied algorithms/exercises do not become personal implementations. A third-party result embedded in a user's project profile remains third-party. Tool integration is not tool authorship. A proposed extension remains background/future work in the concept text, not an implementation claim. Registry `academic_credit` uses `established`, `not_established` or `not_applicable` (e.g. a non-academic publication); an established project/module association does not imply that every later contribution belongs to its credited period.

Do not silently enrich a syllabus-only or supplementary outline with a detailed theorem from general knowledge. A deeper claim needs another sufficiently detailed profile reference, or an explicit extraction gap. More sources do not upgrade the provenance of an existing claim.

### Relations: explicit, small and stored once

| Relationship | Representation / semantics |
|---|---|
| Experience represented by profiles | Registry `profiles`; paired course/project documents share one ID |
| Claim supported by evidence | Claim `references`; reference to a precise profile passage, never just a theme |
| Claim concerns concepts | Claim `concepts`; many-to-many |
| Competency supported by claims | Competency `evidence_refs`; never a chain of unsupported competency assertions |
| Concept related to concept | `relations: [{type, target}]`; types `requires`, `specializes`, `contrasts_with`, `related_to` |
| Claim qualified/compared by another | Optional `related_claims: [{type, target}]`; `contrasts_with` or `qualifies` |
| Entity indexed by domains | Multi-valued `domains` on concepts; competencies/themes may derive domains from concepts |

Directional edges live on the origin concept; store a symmetric edge once in a deterministic ID order. Backlinks are derived, not manually duplicated. Proposed cross-domain interpretations must be labeled editorial and must not imply historical use of a method in a project that never used it. A concept prerequisite is not proof the user implemented it.

### Technical content, decisions, results and limitations

**Mathematics:** use LaTeX in Markdown, define symbols/dimensions, state hypotheses next to guarantees, and cite the supporting claim. Preserve finite/infinite-dimensional distinctions, minimization/reward sign conventions, local/global results, continuous/discrete formulations and algorithm variants. Keep a source's material formula conflict visible; separate a supported implementation formula instead of silently correcting the source. No full lecture reproduction is needed.

**Implementation:** store workflow, shapes/indexing, geometry conventions, numerical scheme, integration responsibilities and tools in the applicable claim; concept text explains reusable implications. For pyLowOrder, retain cell-dual versus imported point graphs, seed supervision and sample/node axes—not merely “GNN experience.” Distinguish designed tests from verified passing tests.

**Decision payload:** `choice`, `context`, `rationale`, optional `alternatives` and `tradeoffs`. Say whether the rationale is explicitly documented or an editorial interpretation in the statement/limitations. Do not invent a comparison experiment because alternatives were mentioned.

**Result payload:** `metric`, `values` (labeled methods/conditions), `unit`, `evaluation_context`, and optional baseline/sample count/uncertainty. `actor`, `verification` and `limitations` remain mandatory. Preserve denominators, units, hardware/timing context, dataset scope, negative findings and whether test sets changed. Do not treat model settings as achieved performance, or substitute a source-qualified result with a stronger headline percentage.

**Lesson payload:** `observation`, `implication`, `scope`. Label it as a profile-supported finding or an explicitly editorial synthesis; do not invent a personal learning story. A useful example is that more detailed prediction did not improve the thesis baseline while recovery did, within its reported experiment.

**Limits:** every claim has `limitations: []` or a concise explicit list. Store common source limits in the experience and material local restrictions on the claim; retrieval must render both. Unknown is not false, and `not_established` is not “no credit ever existed.” Record disclosure restrictions for public downstream use. No confidence/proficiency score is necessary.

### Deduplication and granularity

Start with aliases and existing titles; merge only when definition, assumptions and objective agree. One concept per useful retrieval/explanation unit, not per keyword or every equation. Keep coherent variants within one page initially; split if assumptions/algorithms need independent retrieval. Never merge PCA with all low-rank approximation, continuous/discrete stability, or collision SDFs with TSDF mapping just because vocabulary overlaps.

Canonical technical explanations combine source-backed material, with distinct applications linked through claims. One event/result is recorded once, even if two profiles cite it. A Case Studies report result cited by both course and project profiles gets one `cit413042:*` claim with two references if useful, not two independent corroborating experiments. Distinct paper/code versions remain separate claims and can contrast without either being erased.

## 4. Preliminary taxonomy

Use a controlled, non-exclusive domain list in `taxonomy.yaml`. Subtopics below are indexing suggestions, not mandatory child entities. Add a domain only when the corpus supports it; do not organize the initial model around target employers.

| Domain ID | Corpus-grounded scope |
|---|---|
| `mathematical-analysis` | Functional/Hilbert/Banach analysis, operator/spectral theory, weak topologies, Sobolev/variational foundations |
| `optimization` | Convex/nonconvex, constrained/NLP/KKT, proximal and stochastic methods, minimax, Riemannian methods, combinatorial optimization |
| `numerical-mathematics` | Linear algebra/SVD, numerical ODE/PDE schemes, FEM/Galerkin, solver discretization and approximation |
| `probability-statistics-uq` | Random fields, inference, concentration, Monte Carlo/MLMC, rare events, residual/tail modeling and prediction intervals |
| `dynamical-systems` | Stability, manifolds, bifurcations, chaos, ergodicity and mixing |
| `control-estimation` | Impedance, optimal/nonlinear control, MPC/LQR, observers, filtering and sensor fusion |
| `robotics-planning-geometry` | Kinematics/quaternions, configuration spaces, RRT/roadmaps, contact, SDFs, SLAM/maps |
| `machine-learning` | Supervised learning, regularization/generalization, deep/generative/graph models and representation learning |
| `reinforcement-learning` | MDP/Bellman, DP/TD, policy optimization, actor–critic and function approximation |
| `language-vision-cognition` | NLP/transformers/retrieval/semantics, image features/CNNs, cognitive architectures and embodied cognition |
| `computational-neuroscience` | Neural coding/plasticity, cellular models, neuroprostheses, sensory inference and bioelectronics |
| `aerospace-engineering` | Aerodynamic surface-pressure surrogates, structural reserve factors/loads and navigation/control connections |
| `scientific-software-data-engineering` | Numerical-array interfaces, graph/data persistence, solver/ML integration, configuration, diagnostics and reproducibility |

Cross-cutting methods are **concepts with several domains**, not a second taxonomy: autodiff, projection, uncertainty, geometric features, sampling, sparse/low-rank representations, validation and reproducibility. For example, projection in Hilbert spaces and projected Bellman evaluation are related but not interchangeable; the latter has weighted-norm/sampling assumptions. Graph topology appears in combinatorial algorithms, planning and GNNs with different semantics. Insurance/actuarial work is a future application direction: the corpus supports risk-relevant statistics, not an invented actuarial-experience domain.

## 5. Proposed file structure

Nothing in this tree is created by this design task:

```text
03_knowledge_base/
  README.md                 # Retrieval guide, evidence semantics, topic index
  experiences.yaml          # 24 groups -> 25 profile paths; existing IDs/provenance
  taxonomy.yaml             # Controlled domain IDs and labels
  coverage.yaml             # Profile-section coverage and unresolved extraction gaps
  concepts/
    <concept-id>.md         # Canonical technical explanation + YAML front matter
  evidence/
    <experience-id>.yaml    # Scoped claims; avoid one huge global claims file
  competencies/
    <competency-id>.md      # Bounded technical capability, linked to personal evidence
  themes/
    <domain-or-theme>.md    # Short cross-source synthesis and links, produced last
```

Four directories each serve a different retrieval purpose. No sector folders, original-document copies, standalone result database or manually maintained reverse-link files. `coverage.yaml` is knowledge-synthesis tracking, not a replacement for `01_inventory/processing_manifest.csv`. Theme IDs can combine domains where useful; not every taxonomy label needs a mostly empty theme page.

### Registry and front-matter examples

Illustrative records below are **proposed data**, not new extracted experiences or claims of exhaustive pilot coverage. Paths are repository-root-relative. Production `profiles` entries additionally require their actual `sha256`.

```yaml
# experiences.yaml: abbreviated record
experiences:
  - id: cit413042
    title: Case Studies Optimization
    facets: [accredited_coursework, documented_project_work]
    academic_credit: established
    learning_relationship: completed_academic_project
    profiles:
      - path: 02_profiles/courses/cit413042-case-studies-optimization.md
        category: accredited_coursework
      - path: 02_profiles/projects/case_studies_optimization.md
        category: documented_project_work
    limitations:
      - Team-level methods/results and personally authored changes are distinct.
```

```markdown
---
id: neumann-series
title: Neumann-series inversion
domains: [mathematical-analysis, numerical-mathematics]
aliases: [Neumann expansion]
evidence_refs: ["ma3001:neumann-inversion"]
status: draft
---
# Neumann-series inversion

For a bounded operator T on a Banach space with ||T|| < 1,
\((I-T)^{-1}=\sum_{k=0}^{\infty}T^k\).
The course profile documents series-based inversion and a linear integral-equation
application. Completeness and the norm condition are part of the explanation.

Evidence: ma3001:neumann-inversion; see its profile locator below.
```

The example formula expresses the series-based construction already documented in the profile; further rates/proofs must not be added without adequate profile support. Front matter supplies discoverability, not a substitute for mathematical prose.

## 6. Representative evidence and competency examples

Each example is grounded only in an existing profile. The complete five-source pilot should instantiate the same fields uniformly; abbreviated YAML below illustrates the core records. No original PDF/code was reopened for this design.

### A. Mathematics: Functional Analysis

```yaml
# evidence/ma3001.yaml
experience: ma3001
claims:
  - id: ma3001:neumann-inversion
    experience: ma3001
    kind: knowledge
    concepts: [neumann-series]
    statement: >-
      Course coverage includes Neumann-series inversion for I-T with norm(T)<1
      and its application to a linear integral equation.
    basis: course_material
    actor: not_applicable
    verification: not_applicable
    references:
      - profile: 02_profiles/courses/ma3001-functional-analysis.md
        section: Normed, Banach, and operator spaces
        locator: Series and operator equations; Algorithms and numerical methods
    limitations: [No software implementation is evidenced by this course profile.]
```

This supports an analytical explanation/technical interview topic. It does not create an “implemented operator solver” capability. Link Hilbert projections/SVD to FDA and numerical UQ as related knowledge, without claiming that a theorem was consciously used in a specific project.

### B. Thesis: implementation, decision, reported result and lesson

Use `ma6018`, profile `02_profiles/projects/thesis.md`, domains control/robotics/numerical mathematics. Create separate claims rather than one broad “robust MPC” assertion:

| Claim | Evidence locator and faithful payload |
|---|---|
| `ma6018:impedance-in-prediction` (`implementation`, `project_code`, `user`, `statically_documented`) | **Optimal control formulation**: finite-horizon tracking with \(x_{k+1}=\Phi_h(x_k,u_k)\), feedforward acceleration bounds and impedance response inside prediction; CasADi/acados, multiple shooting, SQP/Gauss–Newton and HPIPM. Do not claim bounds on total wrench/joint torque. |
| `ma6018:multirate-feedback` (`decision`, `project_code`, `user`, `statically_documented`) | **Computational architecture**: hold first feedforward action over the control interval but recompute impedance feedback each physics substep. Choice/context is explicit; comparative numerical wrench findings require a separate reported-result claim. |
| `ma6018:spiral-grid-result` (`result`, `project_report`, `user`, `reported_not_reproduced`) | **Search versus estimated-direction recovery**: baseline 47/121; discrete spiral 78/121 over fixed planar offsets. Intended success is final true-position error <2.5 mm. Keep the profile's known classifier discrepancy, lack of independent corrected reproduction and simulation-only scope attached. |
| `ma6018:recovery-versus-prediction` (`lesson`, `project_report`, `user`, `reported_not_reproduced`) | **Controller, reference and recovery comparison**: prediction/contact augmentation alone did not enlarge the reported baseline set; reference recovery did. Scope: this setup, not a universal rejection of MPC/contact modeling. |

A competency such as **integrate constrained prediction, feedback and experiment logging for contact-rich simulation** links the implementation/decision claims. The result may contextualize the project only with its qualifiers; neither oracle counts nor sampled-region expansion is a guaranteed deployable success rate. The concepts contain full supported formulations, not just the table summary.

### C. pyLowOrder: cross-domain implementation versus external results

`ma8102:seed-target-alignment` is an `implementation` claim (`project_code`, `user`, `statically_documented`) referencing **Two-axis batching and neighborhood sampling** in `02_profiles/projects/pyloworder.md`: view predictions as `[B,N,F]`, map global targets through `subset`, then select identical local seeds. The adjacent vectorization claim preserves \(BN\) nodes, \(BE\) edges and per-copy connectivity offsets \(bN\). The capability is correctness-conscious graph/scientific-ML integration—not a measured speedup.

```yaml
# competencies/scientific-ml-software.md: front matter
id: scientific-ml-software
title: Implement geometry-conditioned scientific ML workflows
concepts: [geometry-conditioned-message-passing, graph-neighborhood-batching]
evidence_refs: ["ma8102:seed-target-alignment", "ma8102:disjoint-graph-injection"]
status: draft
```

The Markdown body should explain mesh/graph/data contracts and what the cited changes establish. The concept's mathematical explanation can retain encoder–message–mean-aggregate–update–decoder equations from **Encoder–message passing–decoder**. Domains are ML, aerospace, geometry and scientific software.

Record the DLR NLR pressure MAE 0.0061 separately as `ma8102:dlr-nlr-mae` (`result`, `external_reference`, `third_party`, `reported_not_reproduced`), citing **Scientific-reference experiments and interpretation**. This result must not support personal achieved-accuracy claims; the profile explicitly lacks verified pyLOM GNS benchmark outcomes. Likewise, implemented reproducibility tests do not imply independently verified passing runs.

### D. NGValidation: scientific methodology and specific engineering capability

Experience ID remains `scientific_paper`, displayed title NGValidation. Profile: `02_profiles/projects/ngvalidation.md`.

```yaml
# evidence/scientific_paper.yaml: selected claim
experience: scientific_paper
claims:
  - id: scientific_paper:seeded-data-sampling
    experience: scientific_paper
    kind: implementation
    concepts: [reproducible-data-sampling]
    statement: Added a CLI for indexed CSV loading and optionally seeded random row sampling.
    basis: project_code
    actor: user
    verification: statically_documented
    tools: [Python, pandas, argparse]
    references:
      - profile: 02_profiles/projects/ngvalidation.md
        section: Identifiable individual implementation contributions
        locator: sampling_datasets.py; commit 3d92c269134eec3aa3ff990bcd4d43ce57775bfe
    limitations:
      - Implementation evidence is not proof of a completed experiment or sampling-quality improvement.
```

A validation-workflow competency can additionally cite the profile's authored per-run artifact/configuration changes. Broader library methods belong to separately attributed claims: convex-hull membership via nonnegative barycentric weights and SciPy/HiGHS linear feasibility; residual distributions; binned uncertainty and coverage checks. Do not assign all those algorithms personally to the user merely to strengthen a competency.

Represent paper intersection aggregation and code widest-interval selection as **distinct scoped knowledge/implementation claims**, linked by `contrasts_with`; preserve the 2023-code/2025-paper limitation. The paper's R²=0.999 and approximately nominal coverage findings are team-reported results with their own scopes. No certification or universal calibration guarantee follows. This case tests preservation of source disagreements rather than canonicalizing them away.

### E. Supplementary ADPRL: valuable knowledge with limited provenance

Use experience `tum-approximate-dynamic-programming` and the exact provenance fields in `02_profiles/supplementary/approximate_dynamic_programming.md`: `source_category: supplementary_academic_material`, `academic_credit: not_established`, `learning_relationship: unspecified`.

`tum-approximate-dynamic-programming:projected-policy-evaluation` is `knowledge`, `supplementary_material`, `not_applicable`, `not_applicable`, referencing **Function approximation and projected evaluation** and **Exercise, assignment and computational evidence**. Retain \(T_\pi J=G_\pi+\gamma P_\pi J\), linear approximation, stationary-distribution weighting, MSBE/MSPBE distinctions and the norm-mismatch counterexample assignment. Link to projection and Bellman concepts across mathematical analysis, RL, statistics and optimization.

The profile lists supplied GTD/LSTD Python routines and assumptions needing deeper extraction. That establishes represented computational material, not a personal GTD implementation, completed assignment or a new convergence proof. Its profile-level detail suffices for the initial map; if exact projection/convergence hypotheses are absent, mark that subclaim pending rather than reconstructing them. Other detailed profiles may support independent, separately attributed explanations.

## 7. Retrieval and downstream use

Start with README/theme links, aliases and ordinary `rg` search. Concept pages answer mathematical/algorithmic questions; their evidence links recover applications. Evidence files answer “where, by whom, with what result and limitations?” Competency pages identify supported actions, not generic job-description keywords.

Examples of useful retrieval paths:

- **Explain SQP versus an interior-point method:** concept comparison → course theory and thesis/Case Studies applications → assumptions and solver-use evidence.
- **Find personally implemented GNN work:** competency → user implementation claims → pyLowOrder profile sections/commit locators; exclude DLR result claims from achieved metrics.
- **Prepare an uncertainty interview:** theme → numerical UQ/MLMC concepts and NGValidation diagnostics → distinguish theoretical assumptions, reported calibration and software implementation.
- **Prepare an application:** choose competencies/experience claims → carry attribution/results/limits into `04_master_profile` → write role-specific material downstream. Technical concept presence alone is never evidence of personally delivering that capability.

The knowledge base can include technically specific capability descriptions, but polished career stories, seniority, job fit and sector-specific wording belong in `04`/`05`. Public outputs must respect disclosure restrictions inherited from profiles. No automated CV generator or external retrieval service is needed for the first implementation.

## 8. Implementation and validation plan

| Stage | Work and exit condition |
|---|---|
| 1. Approval | Approve four entities, provenance semantics, directory layout and pilot; no content migration before approval. |
| 2. Small pilot | Use the five representative sources above: Functional Analysis, thesis, pyLowOrder, NGValidation and supplementary ADPRL. Create roughly 8–12 concept pages, 2–3 bounded competencies and 12–20 claims including a decision, negative/result qualification, third-party result and paper/code contrast. Test retrieval; do not claim full coverage of these profiles yet. |
| 3. Refinement | Review whether fields/links answer real questions without repeated prose. Adjust granularity/enums once, retain stable IDs and document changes before expanding. |
| 4. Full extraction | Register all 25 profile paths under 24 groups, capture profile hashes, map every major technical section, deduplicate concepts and incrementally review claims. Keep coursework, project and supplementary provenance distinct. |
| 5. Thematic synthesis | Write short cross-experience themes only after reviewed concepts/evidence exist. Highlight common foundations, contrasting assumptions, applications and capability evidence; link rather than copy full profiles. |
| 6. Coverage review | Validate counts/links/types/qualifiers, review mathematical fidelity and test representative retrieval paths. Publish unresolved technical gaps explicitly; distinguish optional deeper extraction from missing coverage. |

`coverage.yaml` should have one entry per input profile: `profile`, `sha256`, extraction `status`, and section records containing `section`, `concepts`, `evidence_refs`, `disposition` (`mapped`, `partial`, `context_only`, `gap`) and a reason for nonmapped content. Major technical sections must be accounted for; bibliography/admin repetition can be context-only. Incomplete source detail is not permission to mark a detailed theorem extracted. Coverage is not a file-count or keyword-count score.

### Lightweight checks to implement after approval

1. **Structure:** parse YAML/front matter; unique IDs; controlled enums; every referenced concept/claim/experience/profile exists. Resolve profile sections by exact heading, not unstable line numbers. Check Markdown links. Reject invented academic IDs/credits.
2. **Coverage/counts:** 25 input profiles, 24 experience groups, 16 course/four project/five supplementary document categories; exclude `_analysis` and `_template`. Verify paired Case Studies mapping and preserved MA6018/MA8102 associations. Record every major profile section or a reasoned gap.
3. **Evidence safety:** competencies require at least one user-attributed implementation, contribution or decision claim, appropriate to the stated capability. Mathematical analysis, presentation and experiment-design capabilities need not involve code, but their personal activity must be documented. Team-only work can contextualize participation, but not stand alone as proof of individually implementing a subsystem. Supplementary/course-material/third-party-only claims cannot establish personal implementation capability.
4. **Results:** require metric/unit/context/attribution/verification/limits; flag percentages without denominators, comparisons with differing conditions, or “implemented tests” promoted to verified outcomes. Review the thesis discrepancy and DLR/publication boundaries explicitly.
5. **Fidelity:** manually check a sample of equations, assumptions, named guarantees, code contracts and evidence locators against profiles—not original sources. Automated schema checks cannot establish mathematical truth or contribution attribution.
6. **Freshness:** compare stored profile hashes; mark affected claims/pages for review on changes instead of silently carrying stale results. Do not reread original repositories by default. Re-run existing inventory/profile validators only as upstream consistency checks.
7. **Preservation:** source profiles/inventories remain unchanged during extraction. A later source gap requiring new analysis is a separately scoped task; the knowledge model itself must record the gap.

Pilot acceptance questions: can a reader retrieve an exact mathematical statement with hypotheses, an attributable implementation and its tensor contract, a reported but unreproduced result, a contradictory paper/code formulation, and supplementary-only knowledge without confusing any pair? Can a person trace each competency to a profile passage within two link hops? If not, refine before full extraction.

## 9. Trade-offs and decisions requiring approval

**Trade-offs:** explicit evidence adds metadata work but avoids repeated downstream interpretation. Canonical concepts reduce duplication, but application-specific formulations must remain distinct. YAML is excellent for small bounded records, not long derivations; keep technical prose/equations in Markdown. The registry is a mapping to existing experiences, not an academic database. No universal “expertise level” is needed. Strict provenance sometimes means a rich theory concept has no demonstrated implementation competency; that is accurate, not a defect.

Approval requested for:

1. Hybrid Markdown/YAML with the four entity types and separate claim attribution/verification dimensions.
2. The proposed layout, existing experience IDs, and 24-group/25-document mapping.
3. Capability semantics: documented personal activity required for demonstrated competencies, with implementation claims specifically needed when claiming implementation; taught/supplementary knowledge remains fully retrievable without proficiency grading.
4. The five-source, deliberately small pilot and the initial taxonomy; revise taxonomy/granularity after pilot rather than creating empty domain files in advance.

No source inconsistency identified by the profiles blocks this design. The known thesis/publication/reproducibility/disclosure limits must travel with affected claims. Optional richer supplementary extraction can be deferred; no new qualification assessment, source audit or professional narrative is necessary to begin the approved pilot.
