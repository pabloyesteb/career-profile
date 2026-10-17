---
id: invariant-measures-chaos
title: Global dynamics, invariant measures and ergodic structure
domains: [dynamical-systems, mathematical-analysis, probability-statistics-uq]
evidence_refs: ["tum-dynamical-systems:global-statistical"]
status: reviewed
relations:
  - {type: related_to, target: projected-policy-evaluation}
---

# Global dynamics, invariant measures and ergodic structure

## Geometry of global recurrence and chaos

The supplementary map follows homoclinic/heteroclinic orbits and global bifurcations through Andronov–Leontovich, Smale horseshoes/symbolic coding and Smale–Birkhoff homoclinic results. Melnikov splitting functions/integrals diagnose transverse intersections in the represented forced-Duffing example; simple zeros are connected there to horseshoe dynamics. The source profile does not supply the integral or its perturbative/nondegeneracy assumptions, so no numerical threshold or complete theorem is reconstructed.

Sensitive dependence, one-dimensional maps, renormalization, trapping regions and attractors broaden the geometric sequence; Conley's theorem adds a global organization viewpoint. Logistic/doubling maps, van der Pol, Duffing and Lorenz are named examples, not personally simulated systems.

## Statistical structure is a separate mathematical statement

Invariant measures, Poincaré recurrence, ergodicity, Birkhoff's ergodic theorem and weak/strong mixing concern long-run/statistical behavior, not simply an irregular-looking trajectory. Entropy uses finite partitions and iterated refinements, beginning with
\[
H(\mathcal A)=-\sum_j\mu(A_j)\ln\mu(A_j).
\]
Sheet 13 adds invariant-function tests, Fourier analysis of a hyperbolic toral automorphism and the implication chain **strong mixing ⇒ weak mixing ⇒ ergodicity**. These are substantive late-course topics; exact measure-preservation/integrability hypotheses and entropy-rate constructions beyond the profile are unavailable here.

## Relationship to learning and inference

ADPRL weights value approximation by a policy's stationary distribution. That motivates a precise conceptual question about what long-run sampling distribution a learning objective uses. It does **not** transfer a dynamical ergodic theorem into a universal guarantee for off-policy TD, dependent Monte Carlo or a robot exploration policy. Likewise, state-distribution shifts are not synonymous with deterministic chaos.

This contributes mathematical breadth beyond optimization/software: orbit structure, reduction, recurrence, information and statistical dynamics. Evidence: `tum-dynamical-systems:global-statistical` in [dynamics claims](../evidence/tum-dynamical-systems.yaml). No personal computation or proof reconstruction is implied by this supplementary source.
