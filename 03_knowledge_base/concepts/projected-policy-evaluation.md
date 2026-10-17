---
id: "projected-policy-evaluation"
title: "Projected policy evaluation and norm mismatch"
domains:
  - "reinforcement-learning"
  - "mathematical-analysis"
  - "optimization"
  - "probability-statistics-uq"
evidence_refs:
  - "tum-approximate-dynamic-programming:projected-policy-evaluation"
  - "tum-approximate-dynamic-programming:norm-mismatch-example"
  - "mgt001299:deep-values"
status: "reviewed"
---

# Projected policy evaluation and norm mismatch

## Approximation problem

The supplementary profile distinguishes value tables from linear-feature/neural approximation, stationary-distribution weighting, mean squared Bellman error (MSBE) and mean squared projected Bellman error (MSPBE). Projection/weighting and approximation space affect the construction.

These are distinct objectives, not interchangeable labels for least squares. Exact projection matrices and objective formulas are absent from the profile; none is reconstructed here.

## Norm mismatch

Assignment 2 supplies a two-state Markov-chain counterexample to projected-evaluation convergence with a mismatched norm and alternative feature vectors. This records a substantive failure mode alongside convergence discussions. Actual matrices/features and the full derivation are not in the profile, so a worked numerical example would be unsupported.

## Cross-domain connection

[Hilbert projection](hilbert-projection.md) supplies an analytical approximation viewpoint; [Bellman evaluation](bellman-policy-evaluation.md) supplies a sequential-decision operator. The relationship is editorial concept organization, not a claim that the user historically implemented their combination.

Weighting and operator assumptions must accompany any future exact convergence statement. Broad claims about ergodicity/off-policy stability do not become universal guarantees. [Sample-based value learning](temporal-difference-learning.md) now captures the profile's GTD/LSTD/LSPE, stochastic-approximation and off-policy method map; exact equations/hypotheses unavailable upstream are not an unprocessed supplied derivation.

Deep RL separately supplies visitation-weighted value-error minimization and the semi-gradient target convention. They complement the projection discussion but are not automatically MSBE/MSPBE optimization. [Deep RL evidence](../evidence/mgt001299.yaml), `deep-values`, preserves that independent basis. [Invariant-measure dynamics](invariant-measures-chaos.md) provides a related long-run-distribution vocabulary, not a proof of off-policy convergence.

## Evidence and boundary

[Projected evaluation and norm-mismatch claims](../evidence/tum-approximate-dynamic-programming.yaml) → [ADPRL](../../02_profiles/supplementary/approximate_dynamic_programming.md), Function approximation and projected evaluation and Exercise, assignment and computational evidence. Presence of an assignment/code routine does not establish personal completion or implementation.
