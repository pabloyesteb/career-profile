---
id: "matching-assignment-routing"
title: "Matching, assignment and parity-constrained routing"
domains:
  - "optimization"
  - "robotics-planning-geometry"
evidence_refs:
  - "ma4502:matching-routing"
status: "reviewed"
---

# Matching, assignment and parity-constrained routing

## Cardinality and augmenting structure

A matching uses no vertex twice; a perfect matching covers every vertex. Alternating paths exchange matched/unmatched edges, and symmetric difference describes how matchings differ. Augmenting paths increase cardinality. Hall's theorem characterizes bipartite saturation by neighborhood cardinality; König's theorem connects bipartite maximum matching with minimum vertex cover. These properties are not automatically general-graph statements.

Bipartite augmentation and Hopcroft–Karp organize searches into layers and simultaneous augmentation phases; the stated bound is \(O(\sqrt n\,m)\). Maximum order-preserving matching is an exercise in dynamic programming, not the same unconstrained bipartite optimization problem.

## Weighted assignment and parity corrections

Weighted bipartite perfect matching is the assignment problem. The Hungarian method maintains feasible dual potentials and an equality graph, updates dual feasibility when augmentation is blocked, and has the represented \(O(n^3)\) complexity. Reductions relate weighted matching to weighted perfect matching; they preserve a specified objective, not every variant of assignment.

The course develops general matching through minimum-weight \(T\)-joins, negative-cycle formulations and cycle-cone arguments. A \(T\)-join supplies a parity correction at prescribed vertices. Chinese postman/“Garbage Collecting” uses Eulerian augmentation for route inspection; adding a minimum-cost parity correction differs from finding a shortest single source–target path or a Hamiltonian tour. No unsupported blossom implementation is inferred from the general-matching topic.

## Transfer and evidence

School allocation, weighted assignment, order-preserving alignment and route inspection make the reduction-oriented reasoning concrete. They complement [network flows](network-flow-cost-optimality.md) and [matroid greedy structure](graph-greedy-matroid-optimization.md): recognizing the objective and feasibility class determines which certificate/algorithm applies.

[MA4502 matching-routing evidence](../evidence/ma4502.yaml) represents all late matching exercises and the course's algorithmic bounds. Python programs are supplied scaffolds/references, not evidence that the user personally implemented Hungarian/Hopcroft–Karp. Assignment-style analogies to engineering allocation are potential applications, not new professional deployments.
