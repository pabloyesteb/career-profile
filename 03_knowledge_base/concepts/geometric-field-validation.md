---
id: geometric-field-validation
title: Validate implicit geometry separately from trajectory performance
domains: [robotics-planning-geometry, machine-learning, scientific-software-data-engineering]
evidence_refs: ["cit413042:hausdorff-implementation", "cit413042:field-evaluation", "cit413042:sampling-result", "cit413042:solver-tradeoff-result", "cit413042:geometry-result", "cit413042:representation-tradeoff"]
status: reviewed
relations:
  - {type: related_to, target: reproducible-validation-workflows}
  - {type: related_to, target: signed-distance-neural-fields}
---

# Validate implicit geometry separately from trajectory performance

## Different metrics expose different failures

SDF-value MSE, occupancy IoU/Jaccard, surface error, Chamfer distance and Hausdorff distance do not measure the same property. IoU compares occupied sets by intersection over union. Chamfer averages nearest contour-point distances; symmetric Hausdorff takes the worst nearest-point separation:
\[
H(A,B)=\max\left\{
\sup_{a\in A}\inf_{b\in B}\|a-b\|,
\sup_{b\in B}\inf_{a\in A}\|a-b\|\right\}.
\]
Pablo's documented implementation adds this symmetric metric, shape checks and empty-surface handling. At the inspected HEAD a missing contour yields no metric, not perfect agreement. Pairwise distances operate on near-zero grid samples, so threshold/resolution affect the measured shape. A mean contour error can hide a localized maximum error; low MSE does not certify positive clearance.

The report evaluates reference distances on a predicted surface; code's surface loss evaluates predicted values on a reference surface. These one-sided operations must remain distinct. The source's physical length scale for reported contour distances is not established; do not relabel them millimeters or meters.

## Separate representation, optimizer and task outcomes

The team compares analytic/smoothed/neural fields, RRT/linear/default initialization, optional slack/control penalties, sampling distributions and decomposition granularity. Results include geometric quality, objective, runtime, trajectories and controls. Similar objective values can coexist with different field quality and derivative cost; increased geometric fidelity need not yield a better attained path objective.

Sampling results favor boundary-informed data in one ten-repetition study; this is not a universal dominance result. Corridor refinement uses 16/36/56/76 trapezoids, then compares a learned field. The final displayed network uses one million rather than 200,000 samples, and the later representation comparison disables earlier control regularization. These are not exchangeable ablations. The B1.1 IoU table/prose conflict and malformed Chamfer entry remain source limits, not silently repaired data.

## Software and experimental interpretation

SIREN model-selection/configuration/logging changes, NumPy/Torch metric annotations, CI scaffold and collaborative merges support specific personal engineering contributions. They do not establish authorship of every metric/runner/GUI or passing CI. YAML/Pydantic scenarios, CSV outputs, Matplotlib plots/animations and Tkinter demos make the team workflow inspectable; untracked result CSVs do not establish exact report-table provenance.

This complements [workflow reproducibility](reproducible-validation-workflows.md): associating a result with its run is different from choosing a metric that answers the intended question. It also parallels the thesis's distinction between controller behavior and task-success classification. Recorded Case Studies outcomes are team-reported/unreproduced, not personal performance improvements.

Evidence: [Case Studies evidence](../evidence/cit413042.yaml), especially personal Hausdorff commit `12544f1dc5819226a6a3a9b4b3b5535bcd38430d`, Evaluation quantities and the result/trade-off sections. Quantitative values and their conditions live in the result claims, rather than being copied into each synthesis.
