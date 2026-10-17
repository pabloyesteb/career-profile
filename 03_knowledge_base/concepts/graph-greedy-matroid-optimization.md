---
id: "graph-greedy-matroid-optimization"
title: "Graph algorithms, greedy optimality and matroid structure"
domains:
  - "optimization"
  - "numerical-mathematics"
evidence_refs:
  - "ma4502:graph-greedy"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "matching-assignment-routing"
  -
    type: "related_to"
    target: "network-flow-cost-optimality"
  -
    type: "related_to"
    target: "structured-sequence-parsing"
---

# Graph algorithms, greedy optimality and matroid structure

## Graph representation, encoding and algorithm choice

Directed/undirected graphs distinguish walks, paths, cycles, connectivity and acyclic digraphs. Running time uses \(n\) vertices and \(m\) edges, but polynomial complexity refers to encoded input length: dependence on a numeric supply is not automatically polynomial in its binary representation. Linear/integer formulations, integer hulls and polynomial LP solvability via ellipsoids provide context, not a supplied general-purpose integer solver.

DAG shortest paths exploit topological order in \(O(n+m)\). Dijkstra requires nonnegative edge weights; with Fibonacci heaps the stated bound is \(O(m+n\log n)\). Bellman–Ford handles negative weights and detects negative cycles in \(O(mn)\). These are different admissibility/complexity contracts; a shortest-path algorithm is not a universal solver for arbitrary path constraints. Maze/custom adjacency-matrix examples illustrate representation choices.

## When greedy decisions have a structural guarantee

A minimum spanning tree connects all vertices without cycles at minimum edge-weight sum. Cut/cycle properties justify Prim and Kruskal, rather than a heuristic belief that a locally cheap edge always helps. Prim's basic bound is \(O(n^2)\), improving to \(O(m+n\log n)\) with an advanced structure. The notes' presented Kruskal implementation is \(O(mn)\); union–find refinement is discussed, not substituted for that actual implementation.

An independence system is downward closed. Matroids additionally satisfy exchange: for independent \(A,B\) with \(|A|<|B|\), some element of \(B\setminus A\) augments \(A\) independently. Bases, circuits and graphic-matroid examples explain why weight-ordered greedy succeeds for every weight function in the represented theorem. Knapsack, matching and traveling-salesman independence systems provide counterexamples; their failure to have this property matters more than sharing a “select edges/items” vocabulary.

## Implementation context and connections

Python scaffolds/completed references cover shortest paths and Kruskal with custom graph/maze objects, not a dependency on NetworkX or an individually authored project. Static code inspection does not establish personal completion or measured runtimes. [MA4502 evidence](../evidence/ma4502.yaml) preserves this boundary.

[Flows](network-flow-cost-optimality.md) and [matching](matching-assignment-routing.md) require stronger global invariants than greedy edge selection. [Dependency parsing](structured-sequence-parsing.md) also selects graph structure, but its maximum **directed** spanning-tree cycle contraction is not Prim/Kruskal on an undirected MST. Graph topology in [message passing](geometry-conditioned-message-passing.md) is a computational representation, not an optimization objective. These are reusable distinctions, not claims that these algorithms were combined in pyLowOrder.
