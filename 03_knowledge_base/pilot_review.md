# Knowledge-base pilot review

Date: 2026-10-15. Scope: **five source profiles only**, from the approved architecture. No original PDF, archive, source repository, internal reconstruction report or other course/project profile was reopened for technical extraction. No source code/notebook/training was executed.

## Deliverables and extraction scope

Created the pilot README, experience registry, controlled taxonomy, coverage records, 11 concept pages, five evidence files, three competency pages, this review and `scripts/validate_knowledge_base.py`. `themes/` exists and is intentionally empty. The 25-profile upstream corpus and all protected inventory/profile/downstream files remain unchanged.

| Group | Files / content |
|---|---|
| Mathematical concepts | `neumann-series.md`; `hilbert-projection.md` |
| Control/robotics concepts | `nonlinear-model-predictive-control.md`; `progress-triggered-recovery.md` |
| Scientific-ML concepts | `geometry-conditioned-message-passing.md`; `graph-neighborhood-batching.md` |
| Validation/data concepts | `reproducible-data-sampling.md`; `reproducible-validation-workflows.md`; `prediction-interval-aggregation.md` |
| Supplementary theory concepts | `bellman-policy-evaluation.md`; `projected-policy-evaluation.md` |
| Evidence files | `ma3001.yaml` (2 claims); `ma6018.yaml` (5); `ma8102.yaml` (4); `scientific_paper.yaml` (4); `tum-approximate-dynamic-programming.yaml` (3), all under `evidence/` |
| Competencies | `impedance-aware-control-design.md`; `scientific-ml-software.md`; `validation-data-workflows.md`, under `competencies/` |

**18 claims:** **6 knowledge, 7 implementation, 1 contribution, 1 decision, 2 results and 1 lesson**. The count represents scoped assertions, not independently verified experiments.

The analytical competency is grounded in the thesis's individually attributed OCP formulation and numerical/execution choices. The mathematical course concepts remain substantive even without an implementation competency. NGValidation's broader interval routine is explicitly not assigned individual authorship; its personal engineering competency relies instead on sampling/artifact changes.

## Coverage status

All five registered profiles have extraction `status: draft` and are **partially extracted**, not fully synthesized. Individual concept/competency `reviewed` status means checked pilot content, not empirical verification or whole-profile completion. All level-2/3 profile headings are accounted for in [coverage.yaml](coverage.yaml).

| Profile | Extracted selection | Deferred examples / insufficient detail |
|---|---|---|
| Functional Analysis | Neumann construction and projection setting | Most Banach-space, duality, weak-topology, Sobolev/Fredholm/spectral content intentionally deferred. Full Neumann proof/error bounds and exact projection characterization are not present at input-profile depth. |
| Thesis | Impedance-aware OCP, solver integration, multirate choice, recovery trigger/variants, qualified spiral result and interpretation | Full impedance/passivity theory, detailed pose/reference interpolation, contact-model extensions, other recovery comparisons and sensitivities deferred. Shared source/result/disclosure limits retained. |
| pyLowOrder | Message-passing equations, graph representation distinctions, double batching/seed alignment, external NLR MAE distinction | Detailed geometry algorithms, HDF5, scalers/losses, Optuna, provenance artifacts and reproducibility tests deferred. No personal benchmark results manufactured. |
| NGValidation | Seeded subsampling, run artifacts, interval aggregation paper/code contrast | Full ten-node scientific pipeline, hull validation, tail models, conditioning, feature importance, calibration results and other personal changes deferred. Paper/code versions remain distinct. |
| Supplementary ADPRL | Policy operator, projection/weighting distinctions and norm-mismatch assignment | Exact contraction/TD/projection guarantees and numerical counterexample data insufficient in the input. Multi-step operators, GTD/LSTD details, off-policy procedures and remaining exercises intentionally deferred. |

Coverage uses only the approved dispositions: `partial` for selected sections with remaining content, `gap` with `deferred:` reason for deliberately unselected material, and `context_only` for metadata, provenance, limitations and source registers. Reasons containing `insufficient_detail:` identify unsupported deeper statements separately from intentional deferral. No section is marked `mapped` merely because one claim cites it. Parent topic headings are also recorded; this is an accountability ledger, not a completeness percentage.

Machine-checked heading totals: **109 records: 27 partial, 61 intentionally deferred gaps, 21 context-only**. Per profile (partial/deferred/context): Functional Analysis 3/9/5; thesis 10/19/2; pyLowOrder 5/12/3; NGValidation 5/19/7; ADPRL 4/2/4. Insufficient-detail explanations occur within partially extracted sections and are not a claim that their remaining derivations were recovered.

## Retrieval acceptance tests

The following paths were followed against the saved files and checked against exact source-profile sections. The validator also executes structural/fixture assertions for all six; a PASS is not a new experiment result.

| Question | Retrieval path | Answer and qualification | Result |
|---|---|---|---|
| 1. Mathematical concept with hypotheses/formulation? | [Neumann page](concepts/neumann-series.md) → `ma3001:neumann-inversion` in [course evidence](evidence/ma3001.yaml) → Normed, Banach, and operator spaces / Algorithms and numerical methods | Bounded operator on a Banach space, norm below one, inverse represented by its Neumann series. Full proof and truncation bounds remain gaps rather than reconstructed content. | PASS |
| 2. What was personally implemented? | [Batching page](concepts/graph-neighborhood-batching.md) → `ma8102:seed-target-alignment` in [pyLowOrder evidence](evidence/ma8102.yaml) → Two-axis batching and neighborhood sampling | Predictions `[B,N,F]`, targets restricted through global subset and matched local seed indices; concrete function/commit locators retained. No passing-run or speedup inference. | PASS |
| 3. Which quantitative result, conditions and limits? | [Recovery page](concepts/progress-triggered-recovery.md) → `ma6018:spiral-grid-result` in [thesis evidence](evidence/ma6018.yaml) → evaluation/results/classifier profile sections | Baseline 47/121 versus discrete spiral 78/121 fixed planar-offset simulations, intended final true-position error below 2.5 mm. Saved 12 mm minimum-over-time classification discrepancy and unreproduced status remain attached. | PASS |
| 4. Which analytical competency has personal support? | [Control-design competency](competencies/impedance-aware-control-design.md) → formulation/contribution, implementation and multirate decision claims → thesis contribution boundary / OCP / numerical / architecture sections | Formulating impedance-aware prediction and integrating numerical/execution choices is documented personal methodological work. Neither inherited planner authorship nor a stability proof is inferred. | PASS |
| 5. What is supplementary knowledge without personal implementation? | [Projected evaluation](concepts/projected-policy-evaluation.md) → ADPRL knowledge claims in [supplementary evidence](evidence/tum-approximate-dynamic-programming.yaml) → approximation/assignment sections plus registry | Weighted projection, MSBE/MSPBE distinction and norm-mismatch failure mode are represented. Credit is not established, relationship unspecified; exact derivation absent and personal GTD/assignment completion not inferred. | PASS |
| 6. How do domains connect without conflation? | [Hilbert projection](concepts/hilbert-projection.md) → typed related_to edge → projected evaluation → Bellman page and separate claims | Shared approximation/projection viewpoint links analysis and RL; ADPRL weighting/operator assumptions remain distinct. The connection is editorial, not a claim of historical implementation. | PASS |

Two additional boundary spot checks: the DLR MAE claim is third-party and supports no personal achieved-accuracy competency; the NGValidation paper intersection and code widest-selection claims retain distinct basis/actor/verification and an explicit contrast link.

## Validation

Command: `python3 scripts/validate_knowledge_base.py`. Uses already available PyYAML and Python standard library; no dependencies installed. Validation covers:

- YAML/front matter parsing, duplicate YAML keys and duplicate entity IDs.
- Existing stable experience IDs, module associations, exact pilot-profile allowlist and actual hashes.
- Concept/claim/experience links, domain IDs/enums and exact profile-heading locators.
- Personal-activity competency support, supplemental provenance and external-result boundaries.
- Result metric, labeled values, units, sample/denominator context, verification and nonempty limitations; decision/lesson payload structure.
- Complete heading accounting, coverage/evidence/concept consistency and refusal to label partial profiles fully reviewed.
- Local Markdown links, empty themes directory and all six retrieval fixtures.

Six in-memory negative tests reject: external result reattributed to the user; result missing units; supplementary knowledge promoted to personal implementation; nonexistent profile section; competency supported only by an external result; and duplicate YAML keys. No invalid fixtures are written into the corpus.

Final results: **PASS** for the pilot validator (5 experiences, 11 concepts, 18 claims, 3 competencies), **6/6 retrieval checks**, and **6/6 in-memory invalid-input checks**. Both existing inventory/profile validators and `git diff --check` also pass. Before/after SHA-256 comparisons found no changes or additions under `01_inventory`, `02_profiles`, `04_master_profile` or `05_cv`; no original source was modified. The themes directory contains no files.

The structural validator cannot prove mathematical truth, evaluate attribution beyond the authoritative profiles, or independently reproduce experiments. Manual review compared formulas, boundaries and result context directly with the five profiles. Partial-sum/argmin/interval-width notation explicates the already represented construction/definition; no new rates, proofs or guarantees were introduced.

## Duplication and model weaknesses

1. General theory lives in concept Markdown; contextual assertions/metrics live in evidence. Readable explanations still need limited overlap with claim statements. This is intentional, not an excuse to duplicate full profiles.
2. Thesis OCP formulation and its implementation share a context but answer different questions: personal mathematical formulation versus solver/execution integration. Keep them separate; do not count them as independent projects or experiments.
3. Claim IDs link to a YAML file, not directly to a navigable YAML record. ID search plus exact profile heading works at pilot scale; derived backlinks/ID indexes may help later, but no new infrastructure was introduced.
4. `reason` text distinguishes deferred from insufficient detail without changing approved coverage enums. This works but is less machine-queryable than a structured gap subtype. Consider an optional subtype only after review; not silently added here.
5. A competency's matching user-attributed claim is necessary, not sufficient to establish the semantic appropriateness of its wording. Automated checks cannot replace this review or determine proficiency.
6. Mathematical detail can stop at profile depth. The projection/Bellman pages explicitly expose those limits rather than treating theorem names as complete derivations. Richer profiles can later support stronger separately attributed statements; reopening sources requires separate authorization.
7. Source limitation inheritance is operationally important: retrieve experience limits together with claim limits. A downstream consumer extracting only numeric fields could still misrepresent the thesis or DLR study.

## Recommendations before scaling

The four entity types and directory architecture worked; **no structural redesign was applied or is currently necessary**. Review concept granularity, qualifier rendering and the treatment of insufficient-detail gaps before expanding. Optional proposals needing approval are a structured coverage-gap subtype and a lightweight derived ID/backlink index if manual retrieval becomes cumbersome.

Continue with incremental extraction from the approved corpus, mapping major sections and preserving the existing shared-experience relationships. The full corpus's 24 experience groups and 25 documents are not all registered by this pilot. Thematic synthesis should wait until the relevant concept/evidence coverage is sufficiently developed and separately authorized. No CV, professional narrative, thematic synthesis or downstream master-profile content was created.
