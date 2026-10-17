---
id: causal-graphical-models
title: Conditional independence, causal mechanisms and counterfactuals
domains: [probability-statistics-uq, machine-learning]
evidence_refs: ["ma4802:causal-models"]
status: reviewed
---

# Conditional independence, causal mechanisms and counterfactuals

## Factorization is not yet causal identification

Bayesian DAG models use parents/children, descendants, skeletons, colliders and v-structures to express conditional structure. d-separation examines active/blocked paths under conditioning, including collider descendants. Joint density factorizes into parent-conditioned node densities; a binary-chain example needs \(2p-1\) parameters rather than \(2^p-1\) for an unrestricted law.

The source states equivalence of local/global Markov and DAG factorization properties and characterizes Markov-equivalent DAGs by skeleton and v-structures. Faithfulness rules out cancellations creating extra independencies. Even ideal conditional-independence information without hidden confounders generally yields a Markov-equivalence class rather than a uniquely directed causal graph. No full discovery algorithm is supplied.

## Mechanisms, interventions and alternative worlds

Acyclic structural equations \(X_j=f_j(Pa_j,N_j)\), with jointly independent exogenous noises, induce a recursively sampled joint distribution. Mechanisms are invariant modules rather than arbitrary statistical conditional factors. Perfect intervention fixes a variable/replaces its equation, removing incoming causal influences. The represented Gaussian example distinguishes \(P(Y\mid do(X=a))\) from ordinary conditioning. No directed path rules out an effect; an existing path can still have zero total effect through cancellation.

Counterfactual inference proceeds by **abduction** (condition exogenous noise on observations), **action** (intervene), then **prediction**. Conditioned noises need not remain independent. Observational, interventional and counterfactual conclusions require progressively stronger identification information; a good predictive fit alone does not provide it.

## Connections and limitations

Graph-neural adjacency encodes physical neighborhood, Bayesian DAG edges conditional factorization, and causal arrows mechanisms. The common word “graph” does not establish an equivalence or causal interpretation of pyLowOrder. Likewise, a model experiment under changed settings is not automatically causal identification from observational data.

Evidence: `ma4802:causal-models` in [Statistical Learning claims](../evidence/ma4802.yaml), script §§7–8 as represented in the profile. Missing rendered independence glyphs and the unfinished final exercise are not reconstructed. This is theoretical coursework knowledge, not a personally deployed causal-discovery tool.
