# Technical knowledge base

**Source-profile extraction complete: 25/25 profiles reviewed**, updated 2026-10-17 under the approved [knowledge model](../docs/knowledge_model.md). This means all materially relevant content is represented at authoritative-profile depth or explicitly bounded by source limitations. It does not mean independent experiment reproduction, recovery of unavailable original detail, or completed global semantic consolidation.

## Navigate by question

| Question | Entry points |
|---|---|
| What supports solvability and approximation? | [Banach/duality/weak compactness](concepts/banach-duality-weak-compactness.md), [Hilbert projection](concepts/hilbert-projection.md), [Neumann inversion](concepts/neumann-series.md), [Fredholm/spectral theory](concepts/compact-operator-spectral-theory.md), [Sobolev foundations](concepts/sobolev-distributions.md) |
| How are continuous and discrete models optimized? | [Convex conjugacy](concepts/convex-conjugacy-sparse-optimization.md), [constrained NLP/Newton/barriers](concepts/constrained-nonlinear-optimization.md), [first-order/stochastic](concepts/first-order-stochastic-optimization.md), [proximal/block](concepts/proximal-block-optimization.md), [minimax](concepts/minimax-adversarial-learning.md), [manifold/nonconvex](concepts/nonconvex-geometric-optimization.md), [graphs/matroids](concepts/graph-greedy-matroid-optimization.md), [flows](concepts/network-flow-cost-optimality.md), [matching/routing](concepts/matching-assignment-routing.md) |
| How are predictions and latent models interpreted? | [Risk/selection](concepts/statistical-risk-model-selection.md), [regularized inference](concepts/regularized-linear-inference.md), [classification](concepts/generative-discriminative-classification.md), [ensembles/margins/kernels](concepts/ensemble-margin-kernel-methods.md), [mixtures/EM](concepts/mixtures-latent-inference.md), [PCA](concepts/matrix-low-rank-pca.md), [FA/ICA](concepts/latent-factors-independent-components.md), [causality](concepts/causal-graphical-models.md) |
| How do generative objectives and sampling differ? | [Variational inference/VAEs](concepts/variational-generative-inference.md), [invertible/continuous flows](concepts/invertible-generative-flows.md), [GAN/minimax](concepts/minimax-adversarial-learning.md), [diffusion/probability flows](concepts/diffusion-score-probability-flows.md) |
| How are uncertain simulations and surrogate predictions assessed? | [Random fields](concepts/random-fields-sampling.md), [stochastic PDEs](concepts/stochastic-pde-discretization.md), [multilevel estimators](concepts/multilevel-multifidelity-estimation.md), [sensitivity/rare events](concepts/sensitivity-rare-event-estimation.md), [concentration/JL](concepts/concentration-random-embeddings.md), [domain/split validation](concepts/surrogate-domain-split-validation.md), [residual diagnostics](concepts/residual-statistical-diagnostics.md), [calibration/intervals](concepts/prediction-interval-aggregation.md) |
| How do geometry, feedback and planning interact? | [Pose](concepts/rigid-body-pose-kinematics.md), [impedance](concepts/impedance-contact-dynamics.md), [NMPC](concepts/nonlinear-model-predictive-control.md), [recovery](concepts/progress-triggered-recovery.md), [feedback/observers](concepts/state-feedback-observers.md), [geometric planning](concepts/geometric-sampling-motion-planning.md), [transcription](concepts/optimal-control-transcription.md), [distance fields](concepts/signed-distance-neural-fields.md), [SLAM](concepts/probabilistic-slam-mapping.md) |
| How do sequential learning and adaptation differ? | [Search](concepts/heuristic-adversarial-search.md), [Bellman](concepts/bellman-policy-evaluation.md), [projected evaluation](concepts/projected-policy-evaluation.md), [TD](concepts/temporal-difference-learning.md), [DQN](concepts/deep-value-learning.md), [policy gradients/traces](concepts/policy-gradient-credit-assignment.md), [TRPO/PPO](concepts/policy-optimization-geometry.md), [biological models](concepts/biological-motor-action-models.md), [CMAC/SOM](concepts/local-adaptive-function-approximation.md), [distributional coding](concepts/distributional-value-coding.md), [dynamics](concepts/dynamical-flows-bifurcations.md), [invariant measures](concepts/invariant-measures-chaos.md) |
| How are language, meaning and structured outputs modeled? | [Text/n-grams](concepts/text-tokenization-language-statistics.md), [lexical representations](concepts/distributional-lexical-representations.md), [neural sequences/attention/alignment](concepts/neural-sequence-language-models.md), [hidden states/parsing](concepts/structured-sequence-parsing.md), [retrieval/dialogue](concepts/retrieval-grounded-dialogue.md), [logical/temporal extraction](concepts/semantic-knowledge-extraction.md), [entity/discourse coherence](concepts/entity-discourse-coherence.md) |
| What neural mechanisms and cognitive representations are covered? | [Spiking/plasticity](concepts/spiking-neuron-plasticity.md), [information/sensory inference](concepts/information-coding-sensory-inference.md), [bioelectronic/auditory interfaces](concepts/bioelectronic-neural-interfaces.md), [population/memory dynamics](concepts/population-dynamics-neural-memory.md), [cognitive architectures/binding](concepts/cognitive-architectures-binding.md) |
| Which computational contracts preserve scientific meaning? | [Training/scalers/metrics](concepts/neural-training-data-contracts.md), [geometric GNN](concepts/geometry-conditioned-message-passing.md), [graph batching](concepts/graph-neighborhood-batching.md), [sampling](concepts/reproducible-data-sampling.md), [experiments/persistence](concepts/reproducible-validation-workflows.md), [geometric metrics](concepts/geometric-field-validation.md), [robot interfaces](concepts/robot-perception-control-interfaces.md) |

Bounded capabilities: [control formulation/integration](competencies/impedance-aware-control-design.md), [uncertainty/error analysis](competencies/uncertainty-error-analysis.md), [scientific-ML software](competencies/scientific-ml-software.md), [validation/data workflows](competencies/validation-data-workflows.md), [computational-learning analysis](competencies/analyze-computational-learning-models.md).

Cross-experience syntheses: [modeling/optimization](themes/mathematical-modeling-and-optimization.md), [scientific computing/ML](themes/scientific-computing-and-machine-learning.md), [sequential learning/adaptation](themes/sequential-learning-and-adaptive-behavior.md), [statistical inference/generative modeling](themes/statistical-inference-and-generative-modeling.md). These remain evolving syntheses, not a fixed classification or completed global consolidation.

## Inventory, provenance and retrieval

- [experiences.yaml](experiences.yaml): **24 groups / 25 profile documents**: **16 accredited course + four project + five supplementary documents**. Case Studies' course/project pair is one experience; thesis/MA6018 and pyLowOrder/MA8102 retain academic associations.
- **73 concepts, 185 claims in 24 evidence files, five competencies, four themes.**
- Claim kinds: **128 knowledge, 32 implementation, five contribution, 17 result, two lesson, one decision**. Implementation records include library-level work with unspecified authorship; the total is not a count of personal achievements.
- [coverage.yaml](coverage.yaml): **25 reviewed**, **274 mapped / 148 context-only level-2/3 headings; zero partial/gap entries**.
- [taxonomy.yaml](taxonomy.yaml): thirteen non-exclusive domains. [pilot_review.md](pilot_review.md) is a historical checkpoint, not current coverage/counts.

YAML paths are repository-root-relative; Markdown links are file-relative; evidence locators match exact profile headings. Search IDs, e.g. `rg 'scientific_paper:split-robustness' 03_knowledge_base`. Retrieve each claim with the experience's common limitations.

Claim kind, basis, actor and verification remain independent. Accredited coursework establishes taught knowledge, not authored software. Supplementary credit remains `not_established` and learning relationship `unspecified`. Personal analytical exposition can support a capability without software. Third-party DLR results, collective publication results, unspecified library routines and personal code contributions are not interchangeable.

## Completed extraction batches

| Batch | Profiles completed |
|---|---|
| Foundations/optimization/UQ | Functional Analysis, FDA, Nonlinear Optimization, Numerical UQ, MLMC seminar |
| Control/planning/geometry | Thesis, both Case Studies documents, IN2138, supplementary Advanced Control |
| Learning/dynamics/adaptation | Deep RL, humanoid learning, supplementary ADPRL, Dynamical Systems, Mobile Robotics |
| Statistical/generative ML | Statistical Learning, Deep Generative Models, FOML, supplementary ML, remaining pyLowOrder coverage |
| Final discrete/language/neural/validation | Combinatorial Optimization, NLP, Computational Neuroscience, Technical Cognitive Systems, remaining NGValidation coverage |

### Final batch

Added **17 concepts**: three discrete-optimization families, seven language/structured-inference families, five neural/cognitive/biophysical families and two surrogate-validation concepts. Grouping is by distinct technical questions, not individual algorithms or every profile heading.

Added **49 claims**: 40 knowledge, five implementations and four published results. Two implementations are specifically personal NGValidation changes; three retain unspecified library authorship. Existing claim IDs and the paper/code interval contrast are preserved.

Enriched **14 existing concepts**, the **validation-workflow and computational-learning-analysis competencies**, and **all four existing themes**. No new competency/theme was needed. Academic theory remains substantive even without a new personal implementation claim. Biomedical sensing/stimulation retains its own technical scope rather than being forced into an ML narrative.

Final-batch coverage: **71 mapped / 30 context-only headings**. Every major technical block is represented. Parent headings, administration, repeated summaries, source registers and validation context are not counted as independent technical achievements.

## Unresolved source limitations—not extraction deferrals

- **NGValidation:** restricted industrial data, undisclosed exact splits/bootstrap settings/architecture, 26-versus-22 feature ambiguity and 2023-code/2025-paper lineage. Johnson transform, relative-loss zero handling, interval aggregation/sign and p-value/coverage wording remain qualified. Published R²/coverage figures are collective reported outcomes, not independently reproduced certification or personal benchmarks.
- **Language/Cognitive Systems:** unavailable programming tasks or referenced LIF/Oja/NRP files, mixed historical versions, malformed reward/KL/CRF displays and incomplete requested LLM notebook functionality. Supplied generated-code execution is unsafe to treat as sandboxed; it was not run. IN2222 is source metadata, not an invented official transcript code.
- **Neuroscience:** missing blackboard derivation, untranscribed demonstration videos, a plasticity-bound typo and model-specific empirical statements. No personal fabrication/clinical/recording experiments are inferred.
- **Earlier sources:** IN2138 remains syllabus-only with edition qualification; supplementary provenance stays explicit; FOML's imported-slide/TUM-delivery scope remains limited; absent theorem hypotheses are not reconstructed. Thesis classifier/simulation/disclosure limits, Case Studies collaborative scope and pyLowOrder's lack of verified personal benchmarks remain attached to claims/experiences.

These documented limits do not leave a major profile section unprocessed. None requires an immediate user decision to close source-profile extraction. Original-source reanalysis or public-disclosure permission, if later needed, is a separately scoped action.

## Validation and final-batch retrieval

Run `python3 scripts/validate_knowledge_base.py` and `python3 scripts/validate_profile_state.py`. The existing KB validator's source allowlist/module checks were extended for the four final courses; no new validator, dependency, schema or infrastructure was introduced.

Checks cover YAML/front matter, unique IDs, source hashes/exact sections, links, controlled provenance/enums, competency support, result context and coverage. Original six retrieval fixtures and six invalid-input checks remain. Final-batch retrieval additionally checks:

| Question | Retrieval path and preserved distinction |
|---|---|
| When does a greedy graph algorithm certify optimality? | Graph/matroid → `ma4502:graph-greedy`; exchange/cut structure and actual implementation bounds |
| How do language inference algorithms differ? | Structured parsing → `in2361:structured-inference`; sum/max paths, compatible spans and directed trees |
| What connects statistical and biological PCA? | Matrix approximation ↔ spiking/plasticity → Oja claim; reconstruction versus normalized covariance dynamics, no invented missing notebook |
| What was personally added to NGValidation? | Workflow competency → `split-robustness` / `configuration-portability` → exact commit locators; wider statistics remain collective/unspecified |
| What does approximately nominal coverage establish? | Interval calibration → `coverage-intervals`; CI endpoints/undisclosed counts, constituent versus full-intersection and marginal versus conditional scope |
| Does the language notebook establish completed RAG/code evaluation? | Retrieval/sequence concepts → Cognitive Systems claims; supplied 32→6 retrieval and five single-sample tasks versus missing requested features |

Structural checks and source-grounded retrieval checks pass; they do not independently prove theorems or reproduce outcomes. Protected inventories/profiles/architecture and original scientific sources remain unchanged.

## Potential next-phase consolidation—not performed

1. Review shared projection/low-rank/regularization language across operator theory, PCA, Oja, latent language vectors and LoRA; retain distinct objectives.
2. Review boundaries among statistical-risk, residual-diagnostic and validation-workflow explanations; keep selection, coverage, applicability and certification distinct.
3. Improve cross-navigation for graph/DP structures across flow/matching, parsing, planning and GNN topology without merging unlike algorithms.
4. Review information/uncertainty/memory/credit terminology across neural coding, cognitive architectures, language and RL; distinguish mutual information, inference, replay and traces.
5. Review long multi-source concept/theme pages for repetition and navigation only after a global semantic review; no entity merge or capability inflation is implied.

Source extraction stops here. Global consolidation and downstream `04_master_profile`/`05_cv` work have not begun.
