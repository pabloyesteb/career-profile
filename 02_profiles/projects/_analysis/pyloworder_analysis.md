# pyLowOrder — individual contribution analysis

Status: **contribution analysis complete; final professional profile not started**. Analysis date: 2026-10-14. Sources remained read-only; no project code, tests or training were executed and no dependencies were installed.

## 1. Repository and attribution context

Configured repository: `/home/pablo/UPM/pyLowOrder`, remote `https://github.com/ArnauMiro/pyLowOrder.git`, checked-out branch `140-GNN-implementation`, HEAD `f79ad1d67660eb9502c17398aa5c196cda90cc97`. Worktree clean; repository is not shallow, but only this local branch and its origin tracking branch are present. No fetch or remote-state verification performed. Local reachable history, not all possible upstream branches, bounds this analysis.

## 2. User-associated identities

`P. Yeste <p.yesteb@upm.es>` authors **242 distinct commits** reachable with `git log --all`, author dates 2025-01-30 through 2026-02-18. Name/email match the already established Pablo Yeste identity in the Career Profile sources. This is high-confidence association, not a cryptographic identity attestation. Author and committer use this same identity on these commits. No additional Pablo/Yeste identity was discovered among local author/committer pairs. Commit dates can differ from original author dates after integration; counts include a merge and are not a productivity measure.

`01_inventory/pyloworder_commits.csv` records every associated full hash, parent(s), author date, identity, subject and affected paths. `scripts/inspect_pyloworder_history.py` generated it by read-only Git inspection, with regenerable full patches and a repository snapshot under `.cache/pyloworder_analysis/`. Historical file paths in that inventory may no longer exist at HEAD.

The local tree includes the GNN development line and an earlier mesh-geometry branch merged into its ancestry. Exactly **241 associated non-merge commits and one merge** (`51a25a1`) are inventoried. HEAD itself is a merge by `fermingut`, not the user's commit. No coauthor trailers were found in the associated commit messages; their absence does not prove work was performed without discussion or assistance.

Academic linkage: the existing manifest records user-confirmed correspondence between pyLowOrder and **MA8102 Internship**. This establishes project association, not an employment relationship, a particular internship date range, or that every later commit belongs to the credited internship.

### Evidence convention

Paths below are relative to the external repository. Short commit hashes resolve uniquely in the inspected history; their full values and affected paths are in `01_inventory/pyloworder_commits.csv`. Historical paths are explicitly identified when replaced. **Direct** means a concrete authored diff; **collaborative** means identifiable integration with another developer's work; **infrastructure** means pre-existing software used/extended; **unverified outcome** means runnable-looking code or a stated intent without a checked execution/result. This is professional technical reconstruction, not a general software-quality audit.

## 3. Contribution inventory with evidence

| Contribution | Representative user commits | Main evidence / historical evolution | Attribution |
|---|---|---|---|
| Core dataset correction | `7e039ce` | `pyLOM/dataset.py`: replace invalid `np.range` with `np.arange` for default point ordering | Direct small fix, not dataset authorship |
| Mesh incidence, adjacency and normals | `0434ffe`, `d71b179`, `5d546ce`, `c90e9f4`, `c93fa41`, `7f13e27`, `6ac4b42` | `pyLOM/vmmath/geometric.py`, `pyLOM/mesh.py`, `Examples/example_mesh.py`; Python algorithms and mesh integration | Direct additions/fixes; Cython integration collaborative |
| Original message-passing GNN/GNS | `437eeab`, `82eb033`, `24e87b8`, `2f4abf7`, `4543dd2`, `234144f`, `8ede77b`, `2653c30` | Historical `architectures/gnn.py` → `pyLOM/NN/architectures/gns.py`, `gns/layers.py` | Direct original implementation and iterative refactoring |
| Graph construction/filtering | `a160fc3`, `33a5245`, `de89763`, `51602f4`, `7c0ade0`, `f0b7dad` | Graph initially inside model, later `NN/utils/graph.py`, now `NN/gns/graph.py` | Direct geometry/graph adapter, filtering, fingerprint |
| Graph persistence and converter integration | `1f53a37`, `b7384ab`, `e61101d`, `8e295cb`, `eb74c64`, `078acf4`, `823dee7` | `pyLOM/inp_out/io_h5.py`, graph class, `Converters/DLR2h5.py` | Direct graph I/O and converter extensions; converter originally another developer's |
| Vectorized graph/input batching | `f1a253e`, `234144f`, `64c71d0`, `d17058c`, `9265590`, `8ede77b`, `f3974e8`, `828d382` | Historical batchers/GraphPreparer → `NN/gns/utils.py`, model/trainer | Direct implementation; several earlier loaders superseded |
| Typed configuration/API/Optuna | `7a8768a`, `d2742bf`, `8a0727c`, `121eaa2`, `fa93e3c`, `593b86c`, `9d3c143`, `1603450` | `NN/utils/config_schema.py`, resolvers, model API, Optuna helpers/configs | Direct GNS workflow and shared utility extensions |
| Reproducible experiments/artifacts | `60632bf`, `da420a6`, `3e9233e`, `6dfb017`, `0827701`, `a856048`, `3f94d5c` | RNG contracts, artifact schema, graph fingerprints, metadata, reproducibility tests | Direct infrastructure; not proof of achieved determinism |
| Scaling/dataset utilities | `572d7a9`, `fd07c77`, `5d50e4b`, `dbb2028`, `7093c55` | `NN/dataset.py`, `NN/utils/scalers.py` | Extend existing dataset/min-max scaler; add standard/robust scalers |
| Training/loss/checkpoint robustness | `bac8c6d`, `ac9ebda`, `0f3d8e0`, `5b2de93`, `d4b52d1`, `a65153f`, `d0489f0`, `4d84d88` | `NN/gns/trainer.py`, `NN/losses.py`, model/schema | Direct refactor, objectives, checkpoint metrics, guards and alignment fixes |
| Airfoil examples/documentation | `bdd6184`, `4cce1bd`, `3661f98`, `4ff3028`, `45c20b7` | `Examples/NN/example_GNS_DLR_airfoil.py`, dataset example, `docs/source/NN/GNS/` | Direct examples/docs; benchmark outcomes unverified |

The inventory covers all affected paths, including temporary configuration/batching modules and shared-interface edits. Counting 102 user commits touching `architectures/gns.py` or 64 touching its airfoil example describes iteration, not independent contributions or scientific output. Boilerplate moves, deleted debug utilities and minor import fixes are consolidated into the relevant clusters rather than inflated into separate achievements.

## 4. Detailed technical reconstruction

### 4.1 Geometry and mesh-to-graph prerequisites

**Requirement:** expose cell adjacency and consistent local geometric directions for a graph-based surface-field surrogate.

The original Python additions in `0434ffe` implement an undirected primal **edge→incident cells** map from cyclic polygon connectivity, a cell-neighbor graph across shared interior edges, breadth-first propagation to make neighboring surface-normal directions coherent, and outward **wall/edge normals** inside the polygon plane. `d71b179` exposes these operations through `Mesh`; later fixes adjust signatures/formats and compiled-interface compatibility. Current names include `edge_to_cells`, `cell_adjacency`, `fix_normals_coherence`, `wall_normals`, and mesh properties/methods in `pyLOM/mesh.py`.

For an edge vector \(t=v_{i+1}-v_i\) and surface normal \(n_s\), the wall-normal candidate is \(t\times n_s\), normalized and oriented using an interior-side test. Adjacency propagation flips a neighbor normal if its dot product with the current normal is negative. The algorithm assumes meaningful cyclic polygon connectivity; outward-wall logic assumes convex cells. The coherence routine begins from a boundary cell, so it should not be described as a validated universal closed/disconnected-surface orientation algorithm. [Commits `0434ffe`, `5d546ce`; current `geometric.py`.]

**Important attribution distinction:** `euclidean_d` appears as an addition at the top of `0434ffe`, but the same diff removes that function from the bottom: it is a **move**, not an original Euclidean/MPI-distance implementation. Likewise pre-existing cell-center/surface-normal primitives are inputs, not automatically user-authored. The compiled Cython implementation is principally attributable to **Arnau Miro** (`91bb392`, `1e0c94c`, `18d8e10`, etc.); the user's `80c4f37` changes its documentation, and the geometry merge integrates collaborative work. Claim Python geometry development and compiled-interface integration, not sole Cython/kernel authorship.

### 4.2 Graph representation and topology/geometry separation

**Requirement:** turn CFD surface meshes or imported airfoil graph data into validated PyTorch Geometric inputs without tying topology storage to one model.

`24e87b8` introduces an early Graph class; `a160fc3`/`33a5245` develop mesh construction, `de89763` filtering, and subsequent moves separate graph utilities from the architecture. Current `pyLOM/NN/gns/graph.py::Graph` extends PyG `Data`, holds named node/edge feature dictionaries, creates selected concatenated `x`/`edge_attr`, validates dimensions and edge indices, and moves tensors to the selected device. `Graph.filter` keeps nodes and edges whose endpoints remain, constructs an old→new index map, and relabels connectivity consistently.

For surface meshes, **graph nodes represent cells**, and two directed dual edges are emitted for each pair of cells sharing an interior primal edge. Node features include cell centers and surface normals. Edge features combine source-view wall normals with relative center displacement encoded as spherical distance/angles:

\[
d_{ij}=c_j-c_i,\quad r=\|d_{ij}\|,\quad
\theta=\arccos(d_z/r),\quad\phi=\operatorname{atan2}(d_y,d_x).
\]

The code handles zero-distance arithmetic, uses canonical global-node edge keys, separates incidence topology from per-cell geometry, and prepares contiguous `intc`/`float64` arrays for the existing compiled wall-normal helper. This addresses earlier local/global edge-index and dtype-contract ambiguities. [Current `Graph._compute_node_features_dict`, `_compute_edge_index_and_features_dict`; `7c0ade0`, `823dee7`.]

The imported NLR7301 graph uses a different supplied topology: 597 airfoil sample points, coordinates/normals, precomputed edges/wall normals, and planar edge displacement encoded as length and atan2 angle. Do not conflate that point graph with the cell-dual graph constructor. The feature recipe cites existing aircraft-pressure GNN research; implementation/adaptation is attributable, not invention of the published architecture.

### 4.3 HDF5 graph persistence and CFD data conversion

`1f53a37` adds graph load/save routines to the **existing** HDF5 module; `b7384ab` revises the contract; `078acf4` and `823dee7` implement/harmonize a strict flat schema. Current graph storage uses `/GRAPH`, schema `graph_flat_v2`, `numNodes`, `numEdges`, `edgeIndex`, and numeric `NODEFEATRS`/`EDGEFEATRS` groups with explicit `feature_names` ordering. The loader validates the schema and numeric shapes; graph-save append mode preserves unrelated root groups such as `/DATASET`. Graph class wrappers also support Torch serialization formats. [Current `Graph.save/load`; `pyLOM/inp_out/io_h5.py::h5_save_graph_serial`, `h5_load_graph_serial`.]

The contribution integrates with pyLOM's pre-existing dataset/mesh/partition/HDF5 machinery; it is not authorship of all parallel I/O. `Converters/DRL2h5.py` originated with **Arnau Miro** (`a733934`); the user develops its graph-aware adaptation, renames it to `DLR2h5.py` (`8e295cb`), refactors conversion (`e61101d`, `eb74c64`) and appends the harmonized graph schema to train/validation/test files.

The converter reads NetCDF snapshots containing coordinates and `cp`, parses **Mach and angle of attack** from case filenames, constructs pyLOM field/operating-variable arrays, and imports graph geometry from NPZ files. It includes pressure/normal visualization with Matplotlib. This is data preparation for a CFD surrogate, not a new RANS flow solver. The dataset path `/home/p.yeste/CETACEO_DATA/nlr7301/` is additional corroborating identity/context evidence, not an accessible result collection analyzed here.

### 4.4 Graph neural solver: encoder–message passing–decoder

**Requirement:** predict aerodynamic surface pressure coefficient from operating conditions and fixed geometry.

`437eeab` creates `architectures/gnn.py` with message/update MLPs but also incomplete placeholders; `82eb033` and subsequent training/graph commits turn that scaffold into a developed model. `4543dd2` renames the architecture to GNS; `8ede77b` extracts reusable layers/helpers; `2653c30` applies normalization at every message-passing stage. Current code lives in `NN/architectures/gns.py` and `NN/gns/layers.py`.

For node geometry \(g_i\) and global operating condition \(z\), the encoder forms \(h_i^0=E([z,g_i])\). A message layer computes

\[
m_{ij}^{\ell}=\phi_\ell([h_i^\ell,h_j^\ell,e_{ij}]),\qquad
\bar m_i^\ell=\operatorname{mean}_{j\in\mathcal N(i)}m_{ij}^\ell,
\quad h_i^{\ell+1}=\gamma_\ell([h_i^\ell,\bar m_i^\ell]).
\]

`MessagePassingLayer` implements PyG mean aggregation, learned message and update MLPs. The current model adds activation and GroupNorm after each graph layer, then decodes nodal predictions. `GNSMLP` supports configurable depth, hidden width, activation and dropout. Geometry/edge dimensions are derived from the graph, while operating-input and output dimensions are configuration fields. [Current `GNS.forward`, `_build_encoder`, `_build_message_passing_layers`, `_build_decoder`; layers file; original authored diffs.]

The evidenced example maps **[AoA, Mach] → pressure coefficient CP** on NLR7301. Its illustrative configuration uses latent width 16, hidden width 256, one message-passing layer, six encoder hidden layers, ELU, zero dropout and CUDA. These are configurable example settings, not measured optimum hyperparameters. Despite the name “Graph Neural Simulator” in some docs, this evidenced task is a **steady field surrogate**, not demonstrated temporal fluid integration. No PDE residual or conservation law is explicitly enforced in this architecture.

### 4.5 Two-axis batching and seed-node alignment

Large graphs and multiple operating conditions are handled through two separate batching dimensions: batches of operating samples and batches of graph seed nodes with their k-hop context. Historical `batchers.py`, `GraphPreparer` and `gns_batchers.py` implement graph preparation; later refactors consolidate this into `NN/gns/utils.py::InputsInjector`, `_GNSHelpers`, and `ManualNeighborLoader`. Earlier loaders are historical contributions, not additional independent subsystems still active at HEAD. [Commits `f1a253e`, `64c71d0`, `9265590`, `8ede77b`, `f3974e8`, `828d382`.]

`InputsInjector.replicate_inject` vectorizes a batch of \(B\) conditions over a subgraph of \(N\) nodes: repeat static features, concatenate each condition to its nodes, repeat edge attributes, and offset each copy's connectivity by \(bN\). The result is a disjoint graph with \(BN\) nodes and \(BE\) edges. This eliminates Python per-condition graph construction; no numerical speedup is inferred. `234144f` and `d17058c` provide attributable vectorization/refactoring evidence.

`ManualNeighborLoader` samples CPU k-hop subgraphs with `k_hop_subgraph`, relabels local nodes, retains global `subset` indices and local `seed_mask`, then transfers to the target device. The hop radius follows message-passing depth. Supervision applies to seed nodes; surrounding nodes provide context. It also offers a path not requiring PyG's extension-backed NeighborLoader in some cluster deployments. This is GPU-aware tensor/software integration, not personally authored GPU kernels or demonstrated distributed training.

`d0489f0` and `4d84d88` specifically correct **output/target seed alignment**. `_GNSTrainingLoop._extract_seeded_output_targets` reshapes predictions to `[B,N,F]`, selects identical seed indices for prediction/target, maps full targets through global `subset`, and uses explicit `index_select` instead of inconsistent flattened masks. Shape and empty-seed guards make the contract explicit. This is a substantive correctness fix for double batching, not just formatting. Final inference reassembles arrays shaped `[samples, graph_nodes, output_features]`; full-order invariance across arbitrary sampler settings was not tested in this analysis.

### 4.6 Training objectives, numerical guards and checkpoint selection

`ac9ebda` extracts training from GNS into `_GNSTrainingLoop`, while preserving the model's `fit/predict` interface. Training uses PyTorch autograd, configurable optimizer/scheduler, validation and retained model/optimizer/scheduler state. `bac8c6d` replaces last-epoch retention with best-validation checkpoint restoration.

`0f3d8e0` introduces **FocalMSELoss** in the newly added `NN/losses.py`:

\[
L=\operatorname{mean}\big[(|\hat y-y|+\epsilon)^\gamma(\hat y-y)^2\big],
\]

with mean/sum reduction. It emphasizes hard regression residuals, motivated by CP targets concentrated near zero; it is not focal classification/cross-entropy. The training helper also has optional target-magnitude weighting \(\operatorname{mean}[(1+\alpha|y|)(\hat y-y)^2]\). These are implemented objectives, not established accuracy improvements. [Current `_compute_loss`; `NN/losses.py`.]

`5b2de93` makes configured loss and MAE selection explicit. `a65153f` supports MAE checkpoint selection after an inverse output transformation into physical/output units; the inverse function must be supplied. This should not be described as automatically computing every metric/objective in physical space: current `run_epoch` applies the inverse-space hook to the MAE metric branch, and the optimization loss remains separately computed. Per-batch means are averaged over batches rather than being demonstrated as a globally sample-weighted metric.

`d4b52d1` adds optional gradient-norm clipping and finite-value guards for outputs, targets, loss and gradients. Later alignment work adds structured JSONL tensor diagnostics and optional epoch-zero loss evaluation. These aid numerical diagnosis and prevent silent NaN propagation; they do not prove convergence or eliminate all unstable runs. [Current trainer `train`, `_train_one_batch`, `_to_metric_space`, `_compute_loss`; associated diffs.]

### 4.7 Scaling and dataset integration

The existing NN Dataset and MinMaxScaler are extended, not originally created wholesale by this contribution. `572d7a9` supports loading the main pyLOM Dataset format; `fd07c77` adds **block min–max scaling**, sharing extrema across grouped vector components. `dbb2028` adds dataset filtering with spatial/sample-shape handling and options to retain/drop fitted scalers; `5d50e4b` adjusts dataset/scaler contracts.

`7093c55` directly adds **StandardScaler** and **RobustScaler**, supporting NumPy/Torch data, inverse transforms and serialized parameters:

\[
x_{std}=(x-\mu)/\sigma,\qquad
x_{robust}=(x-\operatorname{median})/(Q_{75}-Q_{25}).
\]

Near-zero scale values fall back to one. Parameters are fitted per supplied block: list inputs allow separate variable blocks, whereas a single matrix is treated as one block by these new classes. Do not assume the usual independent-per-column behavior of an unrelated library. The robust quantiles use NumPy percentiles, transferring tensor data to CPU during fitting. [Current `NN/utils/scalers.py`; commit diff.]

### 4.8 Configurable experiments, Optuna and persistence

The user develops a typed, configuration-driven GNS API from early YAML loaders (`d2742bf`, `8a0727c`) through dataclass DTOs (`121eaa2`) and runtime resolvers (`fa93e3c`, `593b86c`, `9d3c143`). Current `config_schema.py` separates model, training, dataloader, subgraph and graph-provenance fields. Dacite enforces typed dictionary construction; resolvers instantiate device, activation, loss, optimizer/scheduler and specified external classes. Historical loader/factory files were moved/replaced; they should not be treated as missing promised contributions.

`GNS.create_optimized_model` adapts existing Optuna infrastructure: sample model/training search spaces, reuse one loaded graph across trials, build typed configs, train/evaluate trials, report intermediate values for pruning, clean up failed/pruned GPU models, and return the selected configuration/model for downstream fitting. The example specifies a TPE sampler, MedianPruner, 100 trials and searched architecture/training parameters. These are **configured workflows**, not proof 100 successful trials ran. Current objective uses the final logged validation loss; best-checkpoint restoration and hyperparameter scoring are distinct operations. [Commits `7a8768a`, `5153829`, `1603450`, `60632bf`; current architecture, optimizer helpers and example config.]

`60632bf`, `da420a6` and associated changes establish explicit RNG streams for input ordering/subgraphs, seeded samplers and worker initialization. Helpers reject shuffled loading without an explicit generator. This integrates existing seed facilities rather than establishing authorship of every project RNG utility.

`f0b7dad` adds a topology fingerprint: SHA-256 of contiguous int64 edge-index bytes, plus graph size/feature shapes. It does not hash all floating features, is sensitive to stored edge order, and is not a graph-isomorphism identifier. Model checkpoints store pure configuration, graph provenance/fingerprint, learned state and optimizer/scheduler history; load checks graph compatibility. `3e9233e` adds Git provenance; `c946edb` improves commit resolution.

`6dfb017` extracts reusable experiment reporting/saving from the example. `a856048` adds full-run-config persistence; `3f94d5c` unifies seed-selector and reproducible artifact contracts. `save_experiment_artifacts` writes effective config YAML, canonical-JSON configuration hash, metadata including Git/Torch version, model checkpoint, scalers, metrics and optional plot generators. Long explicit node lists can be stored separately in `input_nodes_full.json`. This is a substantial reproducibility/data-contract contribution, not proof all callers supplied all optional provenance fields. [Current `NN/utils/experiment.py`, `_build_repro_config`; authored diffs.]

### 4.9 Examples, documentation and integration

The airfoil example (`bdd6184`, `4cce1bd`, later iterations) wires dataset/graph loading, scaling, training or hyperparameter search, evaluation, checkpoint/export and plots. `3661f98` adds an explicit DLR-style comparison configuration; its commit message does not establish comparable measured performance. `4ff3028` supplies an NN Dataset example. `45c20b7` adds GNS API, architecture, configuration and usage documentation under `docs/source/NN/GNS/`.

The surrounding `Pipeline`, base optimizer/evaluator, mesh/dataset and plotting infrastructure predates or includes other authors. The user adapts/extends interfaces, not all the project's MLP/KAN/PINN/autoencoder/POD/DMD/SPOD implementations. For example, shared-interface changes touching other architectures in refactors do not establish original authorship of those models.

## 5. Mathematical and numerical methods represented

The attributable work substantially evidences:

- Primal edge incidence, cell-dual graphs, adjacency, BFS, normalized cross-product wall normals and orientation coherence.
- Euclidean relative geometry, Cartesian-to-polar/spherical encoding and geometry-conditioned graph features; **not** original MPI Euclidean-distance implementation.
- Learned message/update functions, neighborhood mean aggregation, encoder–processor–decoder GNNs, MLPs, activation/dropout and GroupNorm.
- k-hop receptive fields, seed/context distinction, induced/relabelled subgraphs and vectorized disjoint graph batching.
- Gradient-based regression, Adam/learning-rate scheduling, MSE/MAE, residual-focused and target-weighted losses, gradient clipping and finite-value safeguards.
- Min–max/vector-block scaling, standardization, median/IQR scaling and inverse-space evaluation.
- Hyperparameter search/pruning integration, explicit RNG contracts, best-validation checkpoints and reproducible experiment schemas.

These are implementation-specific capabilities, not a claim of original mathematical invention, CFD-solver development or capability in every low-order method offered by the library.

## 6. Software engineering and computational tools

**Directly evidenced:** Python; NumPy; PyTorch/autograd/CUDA tensor paths; PyTorch Geometric `Data`, `MessagePassing`, `k_hop_subgraph`; dataclasses/typing/protocols; Dacite; Optuna; YAML/JSON; h5py/HDF5 integration; NetCDF4 and NPZ conversion; Matplotlib; pytest; Git history/provenance; SHA-256 fingerprints; modular API/refactoring and explicit shape/device/dtype contracts.

**Integration rather than exclusive implementation:** pyLOM Mesh/Dataset/PartitionTable/Pipeline, existing I/O and metrics, external Cython geometric routines, third-party optimizers and graph-learning primitives. Existing profiling decorators are used; use of a decorator does not establish implementation of the profiling/HPC backend. CPU/GPU code paths and pinned/multiworker loading are implemented/configured, but no measured GPU speedup, cluster scaling or MPI-distributed GNS training is established.

## 7. Tests, validation and outcomes

### Implemented test/experiment evidence

`0827701` adds `pyLOM/NN/gns/test_gns_repro.py`, with six named tests at HEAD:

1. deterministic-algorithm enforcement;
2. evaluation-forward determinism;
3. one-epoch model/optimizer/scheduler/loss-state determinism;
4. multi-epoch loss-sequence determinism under shuffle;
5. subgraph sampler sequence checks;
6. negative test requiring an RNG generator for shuffled loading.

The tests hash/compare state dictionaries and use exact equality/zero-tolerance comparisons. They depend on example configuration, external NLR7301 graph/datasets and an appropriate installed environment. Their existence demonstrates authored validation procedures, **not a verified passing run or universal cross-device reproducibility**. The sampler check compares seed masks, not a complete canonicalized global-node sequence, so do not overstate what it proves.

`Examples/example_mesh.py` provides visualization/checking of mesh normals and includes authored testing changes (`7f13e27`, `61caef3`). Airfoil examples call regression evaluators, true-versus-predicted plots, loss curves and save/load checks. Older temporary `Examples/NN/test_configs.py` (`121eaa2`) supplies configuration checks; historical tests need historical APIs, not an assumption they remain at HEAD.

### Supported outcomes and limits

Supported outcomes are **implemented functionality and integration**: an attributable GNS subsystem with geometry/graph adapters, data persistence, batching, training and experiment-management workflows, plus explicit correctness fixes. The revision includes clearly later modifications/replacements rather than a single pristine original implementation.

No GNS-specific saved metrics, trained checkpoint or completed benchmark report was identified in the inspected tracked paths. Generic `Testsuite/DATA/*.h5` files exist, but are not the referenced converted NLR7301 train/validation/test result set and were not repurposed as evidence. Data/results paths in the GNS example refer outside the checkout (`CETACEO_DATA`, `CETACEO_RESULTS`); those collections were not analyzed. No accuracy, speedup, convergence rate, successful trial count or passing CI result is inferred from configuration/commit subjects.

Current docs/examples contain historical-interface mismatches: the example calls tensor methods on `predict`, while current inference returns NumPy; its reload demonstration constructs a fresh model rather than clearly restoring learned checkpoint weights; parts of the test/docs refer to older API/import locations. These limit claims of demonstrated end-to-end deployment, without negating the individually identifiable implementation contributions. No repairs or execution were attempted. This is the extent of quality commentary needed for the contribution assessment, not a general code audit.

## 8. Collaborative boundaries and uncertainties

- **High-confidence direct attribution:** concrete changes in the 241 non-merge authored commits. The original GNN addition, graph/batching evolution, Python geometric additions, new losses/scalers and later trainer fixes have explicit diff evidence.
- **Identifiable collaborative integration:** mesh geometry includes Arnau Miro's compiled versions; the original converter is his. Shared experiment plotting includes later `fermingut` changes (`7841cab`, `7a209c9`), and current HEAD is his merge. A merge or a user-touched shared file does not transfer authorship of another developer's changes.
- **Inherited infrastructure:** numerical low-order decompositions, base CFD data structures, general neural architectures, external libraries and project build/GPU/MPI backends are not treated as personally developed.
- **History limitation:** non-shallow does not mean every upstream branch is locally present. Reachable attribution is complete for this checkout's refs; contributions on absent branches, other identities or uncommitted/unpublished work remain outside evidence. No fetch was requested or performed.
- **Identity/assistance limitation:** metadata and corroborating example author/path strongly associate the identity with Pablo; Git does not independently establish who typed each line or exclude collaborative assistance. No vague-name identity was silently included.
- **Temporal limitation:** January 2025–February 2026 author dates establish contribution chronology, not continuous employment or internship duration; rebased author/committer dates can differ.

## 9. Technical knowledge represented by the contributions

**Implemented experience:** geometric graph preprocessing for CFD; graph-network surface-field surrogates; topology/feature schemas; CPU/GPU tensor shape/index management; autograd training and validation checkpoints; scalable-by-batching inference/training design; regression objectives/scaling; typed experiment configuration; hyperparameter-search integration; deterministic RNG contracts and reproducibility tests; scientific data conversion/persistence; integration/refactoring in collaborative research software.

**Application knowledge:** aerodynamic pressure-coefficient fields, Mach/AoA conditioning, RANS-derived mesh data and NLR7301 airfoil regression. This is supported surrogate/data-handling context, not proof of authoring RANS physics solvers or independent aircraft design/validation.

**Thematic relevance for later profiling:** machine learning; scientific computing/data engineering; numerical geometry and graph algorithms; aerospace/aerodynamic surrogate modeling; software engineering and reproducible research. Do not equate membership in a reduced-order-modeling repository with personally implementing POD, DMD, SPOD, VAE, KAN or PINN methods. No thematic synthesis files are generated here.

## 10. Questions, completion and next step

Questions that would improve a later final profile, without blocking this analysis:

1. Are there additional Git identities, branches or separate repositories containing your pyLowOrder work that are absent from this checkout?
2. Which contribution dates/components belong specifically to the MA8102 internship, and which are later voluntary/research development?
3. Are NLR7301 metrics, Optuna studies, trained checkpoints, reproducibility-test logs or mesh validation outputs available for any attributable revision? What outcomes may be quoted?
4. Were these GNS/geometry contributions merged into an upstream release/main branch, or should a final profile describe them as development-branch work? Local history alone does not establish release inclusion.
5. Are there collaborative roles or externally adapted implementations not documented in commit metadata that should qualify personal attribution? The Hines/Bekemeyer architectural inspiration and inherited converter/compiled geometry are already distinguished.

### Coverage and completion checkpoint

All 242 associated commits are cataloged; the full affected-path set was reviewed to identify contribution clusters. Substantive initial additions, representative functional diffs, later refactors/corrections and relevant surrounding code/docs/tests were inspected. Not every import/debug-only patch was separately narrated, and no unrelated subsystem was exhaustively analyzed. Source revision/worktree checks and CSV/hash/path validation support resumability; they are not software execution tests.

This analysis replaces the initial attribution checkpoint and is complete for available local evidence. `ma8102` remains deferred to a **final project profile**, with analysis completion recorded in the existing processing manifest. Next logical step: user review of the attribution/result questions, then separately requested final pyLowOrder profiling. Existing course, paper and thesis profiles remain unchanged.
