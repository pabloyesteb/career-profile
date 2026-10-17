---
id: "network-flow-cost-optimality"
title: "Residual networks, maximum flow and minimum-cost optimality"
domains:
  - "optimization"
  - "numerical-mathematics"
evidence_refs:
  - "ma4502:network-flows"
status: "reviewed"
---

# Residual networks, maximum flow and minimum-cost optimality

## Feasibility, residual improvement and certificates

A capacitated flow assigns edge quantities subject to capacity bounds and conservation at intermediate vertices. Its value is bounded by every source–sink cut capacity. A residual network represents permissible increases and reversals of current flow. Ford–Fulkerson augments until no improving path remains; the max-flow/min-cut theorem supplies a certificate, and integral capacities support integral solutions. Irrational-capacity examples qualify termination behavior; they must not inherit integer-capacity reasoning automatically.

Edmonds–Karp chooses shortest augmenting paths with bound \(O(m^2n)\). Dinic uses layered residual networks and blocking flows; the course develops an \(O(n^3)\) bound. Push–relabel instead permits preflows with excess and uses labels/admissible pushes to restore a feasible optimum; its presented implementation bound is \(O(n^2m)\). Invariants and phase/operation analyses differ even when all solve maximum flow.

## Supplies, circulations and minimum cost

A \(b\)-flow assigns supplies/demands at vertices. Feasibility reduces to maximum flow; costs then distinguish feasible flows. The difference between two feasible flows decomposes into residual circulations. Absence of a negative-cost residual cycle characterizes minimum-cost optimality in the represented setting, rather than absence of an arbitrary graph cycle.

Minimum mean cycle computation uses dynamic programming over fixed-length walks in \(O(nm)\). Minimum mean cycle-canceling selects residual improvements with polynomial progress bounds. Successive shortest paths maintain potentials and conservative reduced costs, augmenting along low-cost paths; the stated \(O(Bnm)\) bound depends on total supply \(B\). This dependence must be distinguished from polynomial encoded-input complexity. Unbounded negative-cycle examples and feasibility detection are separate issues.

## Applications and computational contracts

Edge-disjoint route feasibility, transportation/transshipment and capacitated allocation are concrete reductions. A planar non-crossing variant exposes where disjoint-path flow reasoning ceases to suffice. Python reference/scaffold material covers flow state, residual updates, push/relabel, minimum mean cycles with recovery and cycle-canceling. Graph generators and drivers are teaching resources, not independently measured personal experiments.

[MA4502 claims](../evidence/ma4502.yaml) map lectures and all exercise/code clusters. [Assignment/parity routing](matching-assignment-routing.md) supplies related reductions. Potentials resemble dual variables in [convex optimization](convex-conjugacy-sparse-optimization.md), while the residual negative-cycle certificate is a discrete-specific condition. Its relationship to numerical optimality is explanatory, not an assertion that continuous KKT conditions alone guarantee integrality.
