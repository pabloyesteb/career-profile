# pyLowOrder — Graph-neural aerodynamic surrogates and scientific software

## Project identity, academic context and evidence

| Field | Value |
|---|---|
| Stable identifier | pyloworder / ma8102 |
| Project | pyLowOrder / pyLOM, collaborative scientific computing software |
| Contributor | Pablo Yeste Blesa |
| Associated academic module | MA8102 — Internship / Berufspraktikum (Master), TUM |
| ECTS | 6 |
| Grade | BE — passed |
| Identified Git identity | P. Yeste <p.yesteb@upm.es> |
| Evidenced contribution chronology | Author dates 2025-01-30 to 2026-02-18 |
| Inspected branch | 140-GNN-implementation |
| Inspected revision | f79ad1d67660eb9502c17398aa5c196cda90cc97 |
| Profile status | complete_validated |

Academic metadata comes from `01_inventory/courses.csv`, based on the configured transcript. The user confirms the pyLowOrder–MA8102 association. Contribution dates describe Git evidence, **not formal internship duration or employment dates**; not every commit is assigned to the credited internship.

Sources: the configured local repository `/home/pablo/pyLowOrder`; `02_profiles/projects/_analysis/pyloworder_analysis.md`; and `01_inventory/pyloworder_commits.csv`, which records full hashes, author metadata and affected paths for 242 associated commits (241 non-merge plus one merge). Repository-relative paths below resolve against that external checkout. Short hashes identify commits expanded in the inventory. **NN** abbreviates `pyLOM/NN/`; **G** abbreviates `pyLOM/NN/gns/`. Validation date: 2026-10-14. The inspected repository is clean; no project code, tests or training were executed for profiling.

## Scientific purpose and individual contribution

**Scientific reference [DLR]:** Derrick Hines and Philipp Bekemeyer, *Graph neural networks for the prediction of aircraft surface pressure distributions*, Aerospace Science and Technology **137** (2023), 108268, DOI: 10.1016/j.ast.2023.108268. Both authors are affiliated with DLR's Institute of Aerodynamics and Flow Technology. Full text: `00_sources/pyloworder/1-s2.0-S1270963823001657-main.pdf` (`pyloworder_dlr_reference`). Page references below are the PDF's 14 physical/article pages. This pre-existing research informs the implementation; it is distinct from the user's coauthored publication profiled separately.

pyLOM provides scientific tools for reduced-order modeling and data-driven surrogates. Pablo's identifiable work centers on a **graph neural solver (GNS) for aerodynamic surface-pressure prediction**, supported by mesh geometry, graph representations, scientific data conversion, training infrastructure and reproducible experiments. The evidenced example predicts **pressure coefficient CP from angle of attack and Mach number** on an NLR7301 airfoil graph. It is a steady field surrogate using CFD-derived data, not a newly implemented RANS solver or demonstrated time-integrating fluid simulator. [Repository `README.md`; `Examples/NN/example_GNS_DLR_airfoil.py`; `Converters/DLR2h5.py`; GNS documentation.]

The scientific motivation is to replace repeated expensive CFD evaluations with an operating-condition-to-surface-field surrogate. In the DLR formulation, a snapshot matrix contains pressure-coefficient fields at mesh locations, and the learned mapping approximates the RANS solution as \(\hat y(z)\approx f_{\mathrm{RANS}}(z)\). Moving shocks and flow separation challenge global linear POD representations; irregular aerodynamic meshes also do not naturally fit image-grid convolution. Geometry-conditioned graphs provide local spatial context without imposing a Cartesian image representation. Pressure fields are useful beyond pointwise regression because their surface integration determines aerodynamic loads and moments. [DLR §§1–3, pp. 1–4; §5.2.2, pp. 11–12.]

Pablo's work translates this approach into reusable pyLOM software: geometry and CFD data become typed, persistable graphs; pressure regression is coupled to memory-aware batching, explicit tensor/index contracts, training safeguards and experiment artifacts. The demonstrated contribution is this integrated scientific-computing and ML-engineering workflow, rather than a new underlying flow solver.

The individual contributions form a connected workflow:

1. Prepare mesh or imported airfoil geometry and field/operating-condition data.
2. Construct and persist validated node/edge features and topology.
3. Encode operating conditions and geometry in a message-passing network.
4. Train and predict through operating-sample batches and local graph neighborhoods.
5. Select checkpoints, configure/search hyperparameters, and save reproducible artifacts.

**Directly authored:** original GNN/GNS implementation and its evolution; Python mesh adjacency/normal utilities and mesh integration; graph construction/filtering and graph-specific I/O; vectorized graph preparation and neighborhood batching; typed configuration and GNS hyperparameter workflows; loss/scaler additions, training correctness fixes, reproducibility utilities, examples and documentation. Attribution rests on concrete authored diffs, not the entire contents of modified files. [Contribution analysis §§3–4 and commit inventory.]

**Collaborative/inherited:** pyLOM's existing Mesh, Dataset, Pipeline, partition structures, base optimizer/evaluator and I/O are used or extended. The original converter and much compiled Cython geometry are Arnau Miro's work; Pablo adapted the converter and integrated the geometric interfaces. Third-party PyTorch/PyG/Optuna methods and published pressure-GNN concepts are building blocks, not personal mathematical inventions. POD, DMD, SPOD, VAE, KAN and PINN implementations elsewhere in pyLOM are **not** attributed to Pablo merely through project membership or shared-interface edits. [Analysis §§4.1, 4.3, 8; commits `91bb392`, `a733934`, and user integration diffs.]

## Technical contributions: mesh geometry and graph construction

The relationship between the reference method and the implementation is concrete:

| Scientific idea in [DLR] | Translation and additional engineering in pyLOM | Implementation evidence |
|---|---|---|
| Local geometry/topology conditions pressure prediction | Named geometric features, mesh-derived adjacency, normal coherence, graph validation/filtering and HDF5 persistence | `G/graph.py`; `pyLOM/vmmath/geometric.py`; graph I/O described below |
| Encode operating conditions and geometry; exchange learned edge-conditioned messages | Modular GNS encoder/layers/decoder and configurable dimensions/activations | `NN/architectures/gns.py`; `G/layers.py` |
| Batch conditions and target nodes with full message-passing neighborhoods | Vectorized disjoint-graph replication, CPU k-hop sampling, seed masks and corrected target alignment | `G/utils.py`; `G/trainer.py` |
| Train and select aerodynamic regression models | Typed configuration, losses/scalers, checkpoint selection, Optuna integration and reproducible artifacts | Training/configuration sections below |

The paper's CFD dual grid associates graph nodes with **primary mesh points and their dual control volumes**; pyLOM's general surface-mesh construction below instead uses **surface cells as nodes**. The imported NLR example supplies its own graph geometry. These are related locality-based representations, not identical mesh conventions. [DLR §2.2, Fig. 1, pp. 2–3; implementation sources below.]

### Connectivity, adjacency and normals

Python geometry additions map canonical undirected primal edges to their incident cells, derive cell adjacency across shared interior edges, and propagate normal orientation by **breadth-first search**. Neighbor normals are flipped when their dot product is negative. Mesh wrappers expose this geometry to downstream graph construction. [Commits `0434ffe`, `d71b179`, `5d546ce`; `pyLOM/vmmath/geometric.py`, `pyLOM/mesh.py`.]

For a cyclic polygon edge \(t=v_{i+1}-v_i\) and surface normal \(n_s\), an in-plane wall normal is obtained from

\[
n_w=\frac{t\times n_s}{\|t\times n_s\|},
\]

with an interior-side test to orient it outward. This distinguishes the cell's surface normal from its edge/wall normals. The outward test assumes convex polygonal cells; boundary-seeded coherence is not a general guarantee for every closed/disconnected mesh. Later fixes reconcile geometry formats, global/local indices and compiled interfaces. [Functions `edge_to_cells`, `cell_adjacency`, `fix_normals_coherence`, `wall_normals`; commits `c93fa41`, `6ac4b42`, `7c0ade0`.]

The work includes integration with pre-existing Cython helpers using contiguous `intc` connectivity and `float64` coordinate arrays. It does not establish sole Cython/kernel authorship. An existing Euclidean-distance routine moved within an early diff is likewise not counted as an original implementation.

### Geometry-conditioned graph representation

`G/graph.py::Graph` extends PyTorch Geometric `Data`, separating named node/edge feature dictionaries from topology and model configuration. It validates node counts, feature shapes and edge indices; produces selected concatenated `x`/`edge_attr` tensors; and supports device transfer and filtering. `Graph.filter` keeps selected nodes, retains edges whose endpoints survive, and relabels connectivity through an old-to-new index map. [Commits `24e87b8`, `a160fc3`, `33a5245`, `de89763`, `51602f4`, `823dee7`.]

For surface meshes, **nodes represent cells**; two directed dual edges are constructed for cells sharing an interior primal edge. Node features include cell-center coordinates and surface normals. Edge features include source-cell wall normals and spherical relative-position descriptors:

\[
d_{ij}=c_j-c_i,\quad r=\|d_{ij}\|,\quad
\theta=\arccos(d_z/r),\quad\phi=\operatorname{atan2}(d_y,d_x).
\]

Topology incidence and geometric feature calculation are separate, with zero-distance arithmetic handling. [Graph `_compute_node_features_dict`, `_compute_edge_index_and_features_dict`; `7c0ade0`.]

The NLR7301 converter instead imports a **597-point airfoil graph** with supplied edges, coordinates, normals and wall normals, using planar edge length/atan2 angle. That point graph is distinct from the cell-dual mesh adapter. Both are supported representations; neither implies a personally developed CFD mesh generator.

## Scientific data processing and persistence

Pablo extended the existing converter to read NetCDF snapshots containing coordinates and `cp`, associate cases with **Mach/AoA**, construct pyLOM field/operating-variable arrays, and import graph geometry from NPZ. Train/validation/test files carry compatible graph data; Matplotlib plots pressure distributions and normals. [Commits `e61101d`, `8e295cb`, `eb74c64`; `Converters/DLR2h5.py`, originally another developer's converter.]

Graph-specific HDF5 functionality was added and iteratively harmonized in `pyLOM/inp_out/io_h5.py` and Graph save/load wrappers. The strict `graph_flat_v2` schema stores `/GRAPH` with node/edge counts, `edgeIndex`, and numeric `NODEFEATRS`/`EDGEFEATRS` groups, including explicit feature-name ordering. Append mode replaces graph content while preserving unrelated root groups such as `/DATASET`. Loaders check schema and shape contracts. [Commits `1f53a37`, `b7384ab`, `078acf4`, `823dee7`; `h5_save_graph_serial`, `h5_load_graph_serial`, `Graph.save/load`.]

This is graph persistence integrated with inherited scientific I/O, not authorship of all pyLOM parallel HDF5. Graph wrappers also expose Torch serialization. NN Dataset integration includes loading the main pyLOM dataset format and spatial/sample filtering with consistent output reshaping and optional scaler retention. A separate small core Dataset fix corrects default ordering from `np.range` to `np.arange`. [Commits `572d7a9`, `dbb2028`, `7e039ce`; `NN/dataset.py`, `pyLOM/dataset.py`.]

## Graph neural network architecture

### Encoder–message passing–decoder

Pablo introduced the original GNN module, developed its graph/training functionality and refactored it into `NN/architectures/gns.py` plus reusable layers/helpers. The early addition was a scaffold; the developed functionality is evidenced by the subsequent implementation sequence, not the first commit alone. [Commits `437eeab`, `82eb033`, `2f4abf7`, `4543dd2`, `8ede77b`.]

Each operating condition \(z\), such as [AoA, Mach], is concatenated with node geometry \(g_i\) and encoded into latent features:

\[
h_i^0=E([z,g_i]),\quad
m_{ij}^{\ell}=\phi_\ell([h_i^\ell,h_j^\ell,e_{ij}]),\quad
\bar m_i^\ell=\operatorname{mean}_{j\in\mathcal N(i)}m_{ij}^\ell,
\quad\tilde h_i^{\ell+1}=\gamma_\ell([h_i^\ell,\bar m_i^\ell]).
\]

Message and update functions are learned MLPs. The implementation applies activation and GroupNorm after each graph layer, followed by a decoder yielding per-node field predictions. `GNSMLP` supports hidden width/depth, configurable activation and dropout; graph dimensions determine the geometry/edge feature sizes. [G/layers.py, `GNSMLP`, `MessagePassingLayer`; `GNS.forward`, `_build_encoder`, `_build_message_passing_layers`, `_build_decoder`; normalization commit `2653c30`.]

The example config uses latent width 16, hidden width 256, one message-passing stage, six encoder hidden layers, ELU, zero dropout and CUDA. These are **example parameters**, not proven optimal settings. The architecture does not explicitly enforce a PDE residual or conservation law. Published aerodynamic GNN approaches inform the design; original software implementation does not imply invention of message passing itself. [Graph source references; `Examples/NN/configs/gns_config.yaml`.]

The architecture follows the scientific pattern in DLR Eqs. (15)–(24): node inputs combine operating conditions, coordinates and surface normals, \(x_i=z\oplus c_i\oplus\nu_i\); directed edge inputs combine relative displacement and the dual-interface normal, \(e_{ji}=(c_j-c_i)\oplus f_{ji}\). Normals distinguish differently oriented surfaces, while displacements/interface orientation give messages geometric meaning rather than just abstract adjacency. The paper uses normalized normals and polar/spherical coordinate representations for geometric vectors. Its learned messages, mean aggregation, concatenated updates and two-group GroupNorm explain the implementation's design; the NLR example's latent width 16, hidden width 256, one graph layer and six encoder hidden layers also correspond to the paper's NLR configuration. These are design connections, not an assertion of benchmark reproduction. [DLR §§3.3–3.4, p. 4; §4, pp. 5–6; Appendix Table 14, p. 13; `Examples/NN/configs/gns_config.yaml`; `G/layers.py`.]

### Two-axis batching and neighborhood sampling

Training batches both operating conditions and seed nodes, with surrounding k-hop nodes providing message-passing context. `G/utils.py::ManualNeighborLoader` samples CPU subgraphs with `k_hop_subgraph`, relabels nodes, retains global `subset` indices and a local `seed_mask`, then transfers data to the target device. Hop count follows message-passing depth; only seeds are supervised. This also provides an alternative where extension-backed NeighborLoader is unavailable. [Commits `f1a253e`, `64c71d0`, `9265590`, `8ede77b`, `f3974e8`, `828d382`; current loader/helpers.]

`InputsInjector.replicate_inject` vectorizes replication of a subgraph over \(B\) operating samples. For \(N\) nodes and \(E\) edges, it repeats geometry/edge attributes, injects condition features and offsets each graph's connectivity by \(bN\), producing a disjoint batched graph with \(BN\) nodes and \(BE\) edges. This replaces per-condition graph assembly; no numerical speedup is inferred. [Commits `234144f`, `d17058c`; G/utils.py.]

Seed-target alignment received explicit correctness fixes: predictions are viewed as `[B,N,F]`, global targets are restricted through `subset`, and both are selected with the same seed indices using `index_select`. Guards reject invalid shapes and empty seed sets. This preserves supervision correspondence across operating-condition and graph batching. [Commits `d0489f0`, `4d84d88`; G/trainer.py, `_extract_seeded_output_targets`.]

This batching strategy implements the reference's memory-management rationale: an \(\ell\)-layer network needs \(\ell\)-hop context, but only seed-node outputs need supervision. DLR Algorithm 1 combines operating-condition batches with neighborhood subgraphs, replicating topology for each condition and computing MSE only on the selected targets. pyLOM adds reusable graph injection, device handling and explicit seed/global/local indexing safeguards around this procedure. Context nodes must not accidentally become loss targets or change prediction–target correspondence. [DLR §3.4.2 and Algorithm 1, p. 4; implementation evidence above.]

## Training, losses and numerical techniques

`_GNSTrainingLoop` separates epoch/batch execution from model construction while retaining `fit/predict` integration with the existing Pipeline. It uses PyTorch autograd, configurable optimizers and schedulers, validation, and state retention. Best-validation checkpoint restoration includes model, optimizer and scheduler state rather than simply keeping the last epoch. [Commits `ac9ebda`, `bac8c6d`; G/trainer.py, `train`, `run_epoch`; architecture `fit`.]

### Regression objectives and checkpoint metrics

Alongside configured regression losses, Pablo added **FocalMSELoss**:

\[
L_{focal}=\operatorname{mean}\left[(|\hat y-y|+\epsilon)^\gamma(\hat y-y)^2\right],
\]

with mean/sum reduction. It emphasizes difficult regression residuals, motivated by CP targets concentrated near zero; it is not focal classification loss. An optional target-weighted MSE uses \(\operatorname{mean}[(1+\alpha|y|)(\hat y-y)^2]\). Neither objective is claimed to have a verified accuracy benefit. [Commit `0f3d8e0`; NN/losses.py; trainer `_compute_loss`.]

Configurable checkpoint selection includes loss or MAE, with optional inverse-transformed **physical/output-space MAE** when an inverse output function is supplied. This separates the training objective from the validation selection metric; the physical-space option is not applied automatically to every objective. Epoch aggregation averages batch metrics rather than establishing a global sample-weighted estimator. [Commits `5b2de93`, `a65153f`; trainer `_to_metric_space`, `run_epoch`.]

Finite-value guards check predictions, targets, loss and gradients; optional gradient-norm clipping bounds the norm before optimizer updates. Structured JSONL tensor diagnostics and epoch-zero loss evaluation support numerical investigation. These are implemented training safeguards, not convergence guarantees. [Commits `d4b52d1`, `d0489f0`; trainer `_train_one_batch`, `_debug_log`.]

### Scaling and inverse transformations

Pablo extended the inherited MinMaxScaler with **block scaling**, sharing extrema across grouped vector components, and added StandardScaler and RobustScaler:

\[
x_{mm}=a+\frac{x-x_{min}}{x_{max}-x_{min}}(b-a),\qquad
x_{std}=\frac{x-\mu}{\sigma},\qquad
x_{robust}=\frac{x-\operatorname{median}}{Q_{75}-Q_{25}}.
\]

The classes support NumPy/Torch data, inverse transformation and parameter serialization. Standard/robust parameters are fitted per supplied block; a list supplies separate variable blocks, while a single matrix is treated as one block by those classes. Near-zero standard deviation/IQR falls back to one. Robust fitting uses NumPy percentiles on CPU. These implementation contracts matter when scaling vector fields and restoring meaningful output units. [Commits `fd07c77`, `5d50e4b`, `7093c55`; NN/utils/scalers.py.]

## Hyperparameter optimization, configuration and reproducibility

### Typed experiments and Optuna integration

The GNS API evolved toward pure dataclass configurations for model, training, input/subgraph loading and graph provenance. Dacite performs typed dictionary construction; runtime resolvers construct device, activation, loss, optimizer/scheduler and specified classes from configuration. This separates serializable experiment intent from runtime objects. Earlier configuration factories/loaders were superseded during refactoring, not separate final subsystems. [Commits `d2742bf`, `8a0727c`, `121eaa2`, `fa93e3c`, `593b86c`, `9d3c143`; NN/utils/config_schema.py; pyLOM/utils/config_resolvers.py.]

`GNS.create_optimized_model` extends existing Optuna support: sample architecture/training search spaces, reuse a loaded graph across trials, construct typed configurations, train/evaluate, report intermediate values for pruning, and clean up failed/pruned GPU models. The example config selects a TPE sampler, MedianPruner and 100 trials, searching network depths/widths, activations, dropout, learning rate/scheduling and batch sizes. This is implemented/configured optimization—not evidence of 100 successful runs. The trial objective uses final logged validation loss, distinct from best-checkpoint restoration. [Commits `7a8768a`, `1603450`, `60632bf`; model `create_optimized_model`; NN/utils/optuna_utils.py; example config.]

### Explicit randomness and traceable artifacts

Separate seeded CPU generators govern operating-sample and subgraph ordering; worker initialization and seeded Optuna sampling support controlled experiments. Helpers require an explicit generator when shuffling is enabled. This integrates existing project seeding utilities without claiming their complete authorship or universal cross-device determinism. [Commits `60632bf`, `da420a6`; G/utils.py and model initialization.]

Graph provenance includes SHA-256 of contiguous int64 connectivity bytes plus graph size/feature shapes. It detects topology mismatches; it is order-sensitive and does not hash all floating features or establish graph-isomorphism equivalence. Model checkpoints preserve typed configuration, graph provenance, learned state and training history, with load-time compatibility checks. [Commit `f0b7dad`; Graph `fingerprint`; GNS `save/load`.]

Experiment utilities save effective configuration YAML, a canonical-JSON configuration hash, Git/Torch metadata, checkpoint, fitted scalers, metrics and optional generated plots. Long explicit seed selections can be stored separately in `input_nodes_full.json`; full run configuration and seed-selector contracts were added to strengthen reproducibility. This records available provenance, not proof every caller supplies every optional field. [Commits `6dfb017`, `3e9233e`, `a856048`, `3f94d5c`; NN/utils/experiment.py, `save_experiment_artifacts`, `_build_repro_config`.]

## Software engineering, tools and integration

The work demonstrates **Python scientific software development**, modular model/layer/graph/trainer separation, typed APIs, shape/index/device/dtype contracts, serialized schemas, backwards-interface adaptation and collaborative Git integration. Original additions, refactoring and corrective changes are distinct contributions; modifying a shared file is not authorship of all its code.

Explicit tools include **NumPy, PyTorch/autograd/CUDA tensor APIs, PyTorch Geometric, Optuna, Dacite, dataclasses/typing, YAML/JSON, h5py/HDF5, NetCDF4/NPZ, Matplotlib, pytest and Git**. Cython routines are integrated through numerical-array contracts. Pinned/multiworker loading and CPU/GPU paths are supported, but this evidence does not establish personally written GPU kernels, distributed GNS training or measured HPC scaling.

Pablo supplied the GNS airfoil example, an NN Dataset example and GNS architecture/API/configuration/usage documentation. These explain the integrated workflow and expose it to other users. [Commits `bdd6184`, `4ff3028`, `45c20b7`; `Examples/NN/`; `docs/source/NN/GNS/`.]

## Scientific-reference experiments and interpretation

The following are **Hines and Bekemeyer's published experiments**, not measurements of Pablo's pyLOM implementation. They explain the aerodynamic purpose and empirical motivation of the implemented method.

- **CFD and data:** DLR TAU solves RANS with the Spalart–Allmaras turbulence model. For the NLR7301 airfoil at Reynolds number \(1.7\times10^6\), the mesh has 29,441 points including 597 surface points; 98 converged operating cases from 100 Halton samples are split into 39 training, 20 validation and 39 test cases. Inputs are Mach number and angle of attack; the output is the surface \(C_p\) field. The CRM transport-aircraft mesh has approximately 43 million volume-grid points and 454,404 surface points; 149 retained cases split 75/30/44. Its six parameters additionally include inboard/outboard aileron, elevator and horizontal-tailplane deflections. The CRM geometry is fixed to a 1-g flight shape, without a vertical tailplane. [DLR §4, pp. 4–6.]
- **Comparisons and training:** POD interpolation (PODI) reconstructs \(\hat y=\Phi\hat z(z)\) from interpolated reduced coefficients. Coordinate-conditioned MLP and coordinate-plus-normal MLPN baselines isolate the benefit of orientation features and graph context. Neural models use MSE, Adam, exponential learning-rate decay, up to 1,000 epochs and validation-MAE checkpoint selection. Optuna/TPE searches MLP/MLPN settings; PODI uses grid search, whereas costly CRM GNS variants are explored without the same full automated search. The paper uses TensorFlow for MLP/MLPN and PyTorch Geometric for GNS; this does not add TensorFlow to the user's evidenced implementation tools. [DLR §§3–5, pp. 3–8; Appendix Tables 10–14, p. 13.]
- **Pressure accuracy:** NLR test MAE is 0.0061 for GNS versus 0.0126 for PODI, 0.0068 for MLP and 0.0066 for MLPN (Table 5). CRM MAE is 0.0091 versus PODI 0.0198, MLP 0.0117 and MLPN 0.0092 (Table 6). Thus graph prediction approximately halves MAE relative to PODI in these experiments, but the margin over normal-aware MLPN is small and GNS is not best on every metric. Pressure cuts/error maps show the relevance of local orientation and spatial context around complex surfaces and shock regions. Extrapolation examples still misplace shocks; more plausible step-like behavior is not correct shock-location prediction. [DLR §§5.1–5.2, pp. 7–11, Figs. 4–9.]
- **Data and integrated loads:** CRM GNS MAE changes from 0.0153 to 0.0091 to 0.0081 with 37, 75 and 104 training samples. The corresponding test sets also change (75, 44 and 15 cases), so this is not a fixed-test learning curve. For the 44-case test, lift-coefficient MAE is 0.0046 for GNS versus PODI 0.0091, but MLPN is 0.0044; pitching-moment MAE is 0.0058 for both GNS and PODI. On a separate eight-case Mach-0.82 angle-of-attack polar, GNS lift/moment MAEs are 0.0082/0.0063 versus PODI 0.0193/0.0118. Local pressure accuracy therefore matters for engineering loads, but does not guarantee uniformly superior integrated quantities. [DLR §§5.2.1–5.2.2, Tables 7–8, pp. 10–11; Fig. 10, p. 12.]
- **Computational trade-off:** Table 9 reports about 19 hours per CFD case on 64 CPU cores; CRM GNS training takes 36 hours and evaluation \(5\times10^{-4}\) hours (about 1.8 seconds), with neural timing on an NVIDIA RTX 2080. MLP/MLPN training takes 8/6 hours and evaluation \(5\times10^{-5}\) hours; PODI is much cheaper still. These are different-hardware reference timings: they motivate amortized surrogate evaluation, not pyLOM speedups or a universal real-time guarantee. [DLR §5.3, p. 12.]

The published limitations and directions include expensive training/hyperparameter selection, imperfect extrapolation, geometry-specific models, more efficient training/parallel evaluation, extension to changing geometries and high-lift configurations, and training objectives that better preserve integrated loads. The authors cannot share their data. The relationship to pyLOM is consequently strongest at the level of scientific formulation and implemented engineering: irregular-mesh aerodynamic learning, local geometric feature construction, memory-aware message passing, and reusable/reproducible training infrastructure. The user's added losses, typed APIs, persistence and correctness safeguards address implementation needs; the paper does not demonstrate their individual empirical benefit. [DLR §6, p. 12; data-availability statement, p. 13; implementation sections above.]

## Tests, evaluation and supported outcomes

The authored reproducibility suite includes checks for deterministic-algorithm enforcement, evaluation-forward consistency, one-epoch state consistency, multi-epoch loss sequences, subgraph sampling and rejection of unseeded shuffle. It hashes/compares model/optimizer/scheduler state and uses exact/zero-tolerance comparisons. Mesh examples visualize/check normals; airfoil examples include regression evaluation, loss curves and true-versus-predicted plots. [Commit `0827701`; G/test_gns_repro.py; commits `7f13e27`, `3661f98`; relevant examples.]

**Supported outcome:** implemented graph-based surrogate functionality and its geometry, data, training and reproducibility infrastructure, with identifiable seed-alignment and numerical-safety fixes. Tests and example comparisons are implemented validation procedures, not verified passing runs. The inspected evidence does not provide GNS-specific saved accuracy metrics, trained benchmark checkpoints, speedup measurements or successful-trial totals; no quantitative performance claim is made. External NLR7301 data/results and historical example/API mismatches limit independent end-to-end reproduction. Upstream release inclusion is not established by this local development-branch evidence.

These qualifications do not block a source-grounded technical profile. Exact internship timing, additional branches/results and any further collaborative attribution can refine later applications without changing the demonstrated implementation scope.

## Technical knowledge and thematic categories

The substantial implemented knowledge spans:

- **Geometric and graph algorithms:** incidence/adjacency, BFS orientation, cross-product normals, dual graphs, polar/spherical edge descriptors, subgraph filtering/relabeling and k-hop context.
- **Scientific machine learning:** geometry-conditioned message passing, encoder–processor–decoder networks, mean aggregation, MLPs, GroupNorm/dropout, autograd regression and neighborhood supervision.
- **Numerical training/evaluation:** objectives and MAE selection, output-unit restoration, vector-block/standard/robust scaling, gradient clipping, finite-value diagnostics and validation checkpoints.
- **Scientific data/software engineering:** NetCDF/NPZ conversion, typed HDF5 schemas, CPU/GPU shape/index contracts, vectorized double batching, modular APIs, configuration-driven search and reproducible artifacts/tests.
- **Aerospace application:** Mach/AoA-conditioned pressure-coefficient surrogates on CFD-derived airfoil geometry, rather than a claim of developing the underlying flow solver.

Thematic categories: **machine learning; scientific computing and data engineering; numerical geometry and graph algorithms; aerospace engineering and aerodynamic surrogate modeling; software engineering and reproducible research**. The profile is not restricted to one application sector and does not infer unrelated reduced-order algorithms from the host library.

## Profile validation

Scientific-context update: **2026-10-15**. The complete 14-page DLR article, including experiments, conclusions and appendix settings, was read from cached layout-preserving extraction; pages 4 and 12 were also rendered and inspected for architecture/Algorithm 1 and aerodynamic/cost interpretation. Targeted existing implementation evidence was used without repeating contribution attribution. Published metrics/timings remain explicitly separate from implementation outcomes. The profile remains `complete_validated`; the reference adds neither an academic record nor another definitive profile.

Validation used the completed contribution analysis and commit inventory, with targeted code checks rather than a repeated Git-history investigation. Coverage includes every substantive contribution cluster: geometry, graph/data persistence, original GNS/layers, batching/alignment, dataset/scaling, losses/training, configuration/Optuna, reproducibility and examples/docs. Representative commits are traceable to full hashes in the inventory; current and explicitly historical paths are distinguished.

Academic metadata and MA8102 association were checked against the existing inventory. Authored work, collaborative geometry/converter integration, inherited infrastructure and external methods remain separate. Equations and tensor contracts match identified implementations; example parameters are not represented as measured outcomes. No unsupported performance, employment, release or universal reproducibility claim is introduced. Original sources and completed course, paper and thesis profiles remain unchanged.
