---
id: "geometry-conditioned-message-passing"
title: "Geometry-conditioned message passing for aerodynamic fields"
domains:
  - "machine-learning"
  - "robotics-planning-geometry"
  - "aerospace-engineering"
  - "scientific-software-data-engineering"
evidence_refs:
  - "ma8102:gns-architecture"
  - "ma8102:dlr-nlr-mae"
  - "ma8102:mesh-geometry"
  - "ma8102:graph-persistence"
  - "ma8102:dlr-crm-pressure"
  - "ma8102:dlr-loads"
  - "ma8102:dlr-data-scaling"
  - "ma8102:dlr-cost"
status: "reviewed"
relations:
  - {type: related_to, target: signed-distance-neural-fields}
  -
    type: "related_to"
    target: "graph-neighborhood-batching"
---

# Geometry-conditioned message passing for aerodynamic fields

## Representation and formulation

The pyLOM example predicts steady surface pressure coefficient from operating conditions such as Mach/AoA; it is not a personally developed RANS solver or a time-integrating fluid simulator.

For operating conditions \(z\), node geometry \(g_i\) and edge geometry \(e_{ij}\), the profile documents
\[
h_i^0=E([z,g_i]),\quad
m_{ij}^{\ell}=\phi_\ell([h_i^\ell,h_j^\ell,e_{ij}]),\quad
\bar m_i^\ell=\operatorname{mean}_{j\in\mathcal N(i)}m_{ij}^{\ell},\quad
\tilde h_i^{\ell+1}=\gamma_\ell([h_i^\ell,\bar m_i^\ell]).
\]
Learned MLP messages and updates combine node/neighborhood/edge information. Activation and GroupNorm follow graph layers; a decoder produces per-node outputs.

## Geometry and topology contracts

The general mesh adapter uses cells as nodes and shared interior primal edges to construct directed dual edges. Features include centers, surface normals, wall normals and relative-position descriptors. The imported NLR airfoil instead supplies a point graph with planar features. Related locality does not make cell centers and CFD primary nodes interchangeable.

The DLR approach motivates scientific locality/pressure learning; Pablo translates pre-existing methods into reusable pyLOM components, not invention of message passing.

## Depth, outcomes and evidence

Depth determines the neighborhood context needed by [batching](graph-neighborhood-batching.md). Configured widths/activation are example parameters, not measured optima; the architecture does not enforce a PDE residual/conservation law.

[ma8102:gns-architecture](../evidence/ma8102.yaml) supports individual implementation. The separate DLR MAE result has actor third_party and cannot support personally achieved accuracy. No verified personal speedup is supplied.

[pyLowOrder](../../02_profiles/projects/pyloworder.md), Encoder–message passing–decoder, Geometry-conditioned graph representation and Scientific-reference experiments and interpretation, via the referenced claims.

## Constructing geometry before learning

The Python mesh contribution maps canonical undirected primal edges to incident cells, derives adjacency and propagates normal coherence by BFS, flipping a neighboring normal when the dot product is negative. For cyclic polygon edge \(t=v_{i+1}-v_i\) and surface normal \(n_s\), the wall normal uses
\[
n_w=(t\times n_s)/\|t\times n_s\|.
\]
An interior-side test orients it outward for convex polygonal cells. Boundary-seeded coherence is not a general closed/disconnected-mesh guarantee; inherited Cython helpers are integrated through contiguous integer-connectivity/float64-coordinate contracts.

Cell centers \(c_i\) yield \(d_{ij}=c_j-c_i\), \(r=\|d_{ij}\|\), \(\theta=\arccos(d_z/r)\), \(\phi=\operatorname{atan2}(d_y,d_x)\), with zero-distance handling. The graph adapter separates incidence from feature computation. Its named dictionaries validate shapes/indices, select/concatenate model tensors and transfer devices; filtering retains surviving endpoint edges and relabels through an old-to-new map. These operations preserve physical identity, not merely tensor rank. Graph HDF5/data-conversion detail is consolidated in [workflow contracts](reproducible-validation-workflows.md).

## Engineering objective and what the reference experiments show

Moving shocks and separation challenge a global linear POD basis; irregular surface meshes challenge image-grid convolutions. Local edge geometry and orientation expose useful physical context, without enforcing RANS or conservation. Surface pressure is also integrated into loads and moments, so pointwise loss is not the whole engineering objective.

The external DLR study uses TAU RANS/Spalart–Allmaras data. NLR7301 has Reynolds number \(1.7\times10^6\), 597 surface points and a 39/20/39 split of 98 converged cases. CRM has 454404 surface points, six operating/control parameters and 75/30/44 cases on a fixed 1-g shape without a vertical tailplane. CRM pressure MAE is 0.0091 for GNS versus 0.0198 PODI and 0.0092 normal-aware MLPN: orientation is important and the graph advantage over the latter is small. In the 44-case integrated-load comparison GNS lift MAE is 0.0046 versus MLPN 0.0044; GNS and PODI pitching-moment MAE are both 0.0058. On a separate eight-case Mach-0.82 polar, GNS lift/moment MAEs are 0.0082/0.0063 versus PODI 0.0193/0.0118. This different evaluation is not pooled with the 44-case test.

The CRM 37/75/104-training-sample errors (0.0153/0.0091/0.0081) use 75/44/15 test cases respectively, so they are not a fixed-test learning curve. Table 9's 36-hour GNS training and 0.0005-hour evaluation on RTX 2080 contrast with 19-hour CFD cases on 64 CPU cores; different hardware and upfront training/data costs prohibit a universal speedup. Cheaper PODI and MLP baselines remain relevant. High training/search cost, unequal tuning budgets, geometry-specific models, imperfect extrapolated shock locations and unavailable reference data limit conclusions.

These are published reference outcomes, not measurements of the pyLOM branch. They motivate memory-aware graph learning and integration of pressure/load metrics, efficient training and future geometry generalization; none establishes an empirical benefit of the user's added losses or tooling. The original scientific source is already summarized in the [definitive profile](../../02_profiles/projects/pyloworder.md); [result claims](../evidence/ma8102.yaml) retain evaluation contexts and units.
