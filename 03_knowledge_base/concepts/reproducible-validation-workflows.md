---
id: "reproducible-validation-workflows"
title: "Configuration and artifacts in scientific validation"
domains:
  - "scientific-software-data-engineering"
  - "machine-learning"
evidence_refs:
  - "scientific_paper:structured-artifacts"
  - "ma6018:experiment-workflow"
  - "cit413042:solver-architecture"
  - "cit413042:model-benchmark-integration"
  - "ma8102:graph-persistence"
  - "ma8102:typed-search"
  - "ma8102:reproducibility-contracts"
  - "ma8102:reproducibility-tests"
  - "scientific_paper:statistical-library"
  - "scientific_paper:split-robustness"
  - "scientific_paper:configuration-portability"
status: "reviewed"
---


# Configuration and artifacts in scientific validation

## Workflow unit and architecture

NGValidation organizes diagnostics around model × dataset × template. Its engine checks/merges settings, materializes notebooks/configuration, supports execution/resume and exports HTML; utilities load inputs, persist outputs, check requirements and export figures/tables.

The individually supported change organizes per-run files under model/dataset/template directories, saves run configurations, retains latest-result HTML and puts appendix exports in a media directory. This extends a collaborative engine rather than creating every statistical diagnostic.

## Engineering interpretation

Separating run identity from latest output helps preserve the association between inputs, configuration and artifacts. This is an architectural interpretation of documented organization, not a measured reproducibility improvement or immutable experiment ledger.

CSV/HDF5 fixtures and notebook/HTML reports make workflows inspectable, but do not prove the inspected 2023 checkout generated every figure in the 2025 paper. The library's tests package includes statistical procedures, not automatically a verified passing software-test suite.

## Simulation and geometry-benchmark workflows

The thesis supplies a second attributable implementation: YAML-configured controller/reference/recovery branches, fixed offset batteries, MuJoCo execution, HDF5 trajectories, JSON metadata and CSV/plot/video outputs. Logged true/perceived/reference states, wrench/contact data, KKT/solver timing and progress connect numerical behavior to the intended task. A stored success column is not self-validating: the known minimum-over-time classifier differs from final-error methodology. This is the same input–procedure–artifact principle as NGValidation, not the same validation statistic. `ma6018:experiment-workflow` in [thesis evidence](../evidence/ma6018.yaml).

Case Studies uses YAML/Pydantic scenarios and modular model/geometry/learning/initialization/solver/metric layers with CSV and GUI outputs. Personal model-selection/configuration/logging changes and integration commits are narrower than the collaborative runner. Untracked CSVs, stale-interface tests and CI scaffolds do not prove report lineage or a passing pipeline. [Case Studies claims](../evidence/cit413042.yaml). This connects experimental inspectability across three projects without asserting identical architectures or immutable run provenance.

## Limits and evidence

Python/configuration/Jupyter/HDF5 tools are evidenced; the profile does not establish that every integration was personally authored or every declared environment runs. No source code or notebooks were executed in this pilot.

[scientific_paper:structured-artifacts](../evidence/scientific_paper.yaml) → [NGValidation](../../02_profiles/projects/ngvalidation.md), Project identity and software architecture and Identifiable individual implementation contributions, commit 628aaf2d10996ec42f11839b5bff8f3d0efab45b. Related sampling remains a distinct technical contribution.

## Typed graph experiments and persistent scientific data

pyLowOrder adds a distinct implemented data contract. An adapted inherited converter reads NetCDF pressure/coordinates and Mach/AoA, imports NPZ graph geometry and emits compatible train/validation/test data. NN Dataset integration preserves spatial/sample filtering, output reshape and optional scaler retention; a small core ordering fix replaces invalid `np.range` with `np.arange`.

Graph-specific HDF5 uses strict `graph_flat_v2`: `/GRAPH` stores counts, `edgeIndex`, numeric `NODEFEATRS`/`EDGEFEATRS` and explicit feature-name ordering. Append mode replaces graph data without deleting unrelated `/DATASET`; loaders check schema/shape. Torch wrappers provide another persistence route. Graph additions extend inherited scientific/parallel I/O rather than replacing or individually authoring it all.

Pure dataclass intent and Dacite construction are separated from runtime device/activation/loss/optimizer resolvers. Optuna GNS search reuses loaded geometry, constructs trial configurations, reports intermediate values for pruning and cleans up failed/pruned GPU objects. TPE/MedianPruner and 100 configured trials are an example, not a record of successful runs. Search-space dimensions include layer depths/widths, activations/dropout, learning-rate scheduling and batch sizes. Final logged validation loss and best-checkpoint restoration have different semantics.

## Reproducibility has a defined scope

Separate seeded CPU generators control operating-sample and subgraph order; shuffle requires an explicit generator. Worker initialization and Optuna seeding extend existing project utilities. The graph SHA-256 uses contiguous int64 connectivity plus graph size/feature shapes: it is order-sensitive, excludes floating-feature values and is not an isomorphism invariant. Checkpoints retain typed config, graph provenance, learned state and history with load-time compatibility checks.

Effective YAML, canonical-JSON configuration hash, Git/Torch metadata, fitted scalers, metrics, optional plots and separate long seed selections (`input_nodes_full.json`) make an experiment inspectable. Optional caller metadata and cross-device determinism remain qualified. Authored tests compare model/optimizer/scheduler state, evaluation forwards, one-/multi-epoch loss and sampling behavior with exact comparisons; their presence is not a verified passing run.

The transferable connection to NGValidation, thesis simulation and Case Studies is maintaining input–procedure–output correspondence. A topology hash, a random seed, a held-out evaluation and a statistically valid uncertainty statement answer different questions. [pyLowOrder implementation evidence](../evidence/ma8102.yaml) supports these software activities without claiming end-to-end benchmark reproduction.

## Edge cases, portable configuration and statistical procedure

The final NGValidation extraction adds personally attributable numerical-only/dummy-category single-voxel handling, explicit training copies and split-template reporting/requirement corrections. User-provided `from_file` paths resolve relative to the run root with existence checks; example surrogate configurations are consolidated into the master config. GitPython synchronization-path adaptation extends an existing utility rather than establishing full utility authorship or production deployment.

The broader engine organizes `validationlib/engine`, model/transform wrappers, statistical `tests`, data/explainability `misc` and plots/tables. Its configurable CSV/HDF5/model artifacts and notebook execution/resume/HTML export expose model × dataset × diagnostic-template workflows. Expression residuals, sparse masks, joblib-supported feature permutations and binning belong to library context, not all personal code.

Code-backed Python/NumPy/pandas/SciPy/sklearn/statsmodels/h5py/joblib/Matplotlib/Seaborn and Jupyter/nbformat/nbclient/nbconvert/GitPython must be distinguished from the paper, which specifies no software stack. The declared Python 3.9.13 / TensorFlow 2.9.1 / Keras 2.9.0 / ONNX 1.12 / CUDA-cuDNN environment is not evidence every diagnostic ran on a GPU. Missing root requirement files and older layouts limit turnkey reuse.

These engineering details preserve inspectability but do not validate [statistical split adequacy](surrogate-domain-split-validation.md), [residual assumptions](residual-statistical-diagnostics.md) or [interval coverage](prediction-interval-aggregation.md) automatically. Those are scientific questions with separately scoped claims.
