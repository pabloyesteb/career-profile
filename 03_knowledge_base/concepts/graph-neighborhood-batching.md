---
id: "graph-neighborhood-batching"
title: "Graph-neighborhood batching and supervision contracts"
domains:
  - "machine-learning"
  - "scientific-software-data-engineering"
  - "numerical-mathematics"
evidence_refs:
  - "ma8102:seed-target-alignment"
  - "ma8102:disjoint-graph-injection"
status: "reviewed"
---

# Graph-neighborhood batching and supervision contracts

## Two axes and contextual nodes

Training batches operating conditions and seed nodes. An \(\ell\)-layer message-passing model needs \(\ell\)-hop context while supervising only selected seeds. ManualNeighborLoader extracts/relabels CPU subgraphs, retains global subset indices and a local seed mask, then transfers them to the target device.

Context nodes influence messages; being present in a subgraph does not make them loss targets. Correct tensor shape alone does not prove correct supervision identity.

## Disjoint graph replication

A subgraph of \(N\) nodes and \(E\) edges replicated over \(B\) operating samples creates \(BN\) nodes and \(BE\) edges. Geometry/edge features repeat, operating features are injected and graph-copy \(b\)'s connectivity is offset by \(bN\). Replicas remain disjoint. This replaces per-condition assembly without an established numerical speedup.

## Seed/target alignment

Predictions are viewed as \([B,N,F]\), with \(F\) output-feature width. Global targets are restricted through subset, then predictions and targets use the same local seed indices through index_select. Guards reject invalid shapes and empty seed sets.

These are topology, indexing and numerical-data contracts, not convergence guarantees or proof of passing experiments. They support an attributable scientific-ML engineering capability.

## Evidence

[ma8102 alignment and injection claims](../evidence/ma8102.yaml) → [pyLowOrder](../../02_profiles/projects/pyloworder.md), Two-axis batching and neighborhood sampling, with function/commit locators. Application is aerodynamic regression; no historical use in unrelated projects is inferred.
