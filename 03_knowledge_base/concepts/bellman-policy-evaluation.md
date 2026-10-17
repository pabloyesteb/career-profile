---
id: "bellman-policy-evaluation"
title: "Stationary-policy Bellman evaluation"
domains:
  - "reinforcement-learning"
  - "optimization"
  - "probability-statistics-uq"
evidence_refs:
  - "tum-approximate-dynamic-programming:bellman-policy-operator"
  - "mgt001299:markov-planning"
  - "ei7263:decision-models"
  - "tum-mobile-robotics:planning-learning"
  - "additional-cognitive-systems:rl-teaching"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "projected-policy-evaluation"
---


# Stationary-policy Bellman evaluation

## Supported formulation

The supplementary profile records the stationary-policy operator
\[
T_\pi J=G_\pi+\gamma P_\pi J.
\]
\(J\) denotes state costs, \(G_\pi\) policy immediate costs, \(P_\pi\) the induced transition matrix and \(\gamma\) discounting in the finite-state/action, infinite-horizon discussion. This is a cost convention; replacing it with reward maximization must not silently change action selection.

The map distinguishes policy evaluation from the optimal Bellman operator, state from state-action costs, and finite-horizon recursion from stationary fixed points.

## Reward maximization and horizon assumptions

Accredited Deep RL provides an independently supported reward convention:
\[
Q^*(s,a)=\sum_{s'}P(s'|s,a)[R(s,a,s')+\gamma V^*(s')],\qquad
V^*(s)=\max_aQ^*(s,a).
\]
MDPs separate state-dependent actions, transitions, reward, policy and initial/terminal conditions. The Markov property makes future evolution conditionally independent of earlier history given the current state; an observation need not be that state under partial observability. Finite-horizon policies can depend on remaining time; a backward optimal-stopping example is undiscounted but finite. Continuing discounted returns use bounded rewards and \(0\le\gamma<1\); a tail bound is proportional to the reward bound times \(\gamma^{H+1}/(1-\gamma)\). An absorbing terminal mechanism is another setting, not a guarantee for arbitrary undiscounted continuing tasks.

Value iteration uses optimal backups and greedy lookahead. Policy iteration alternates exact policy evaluation with improvement; finite-policy termination needs exact evaluation and tie handling. Dense iterative evaluation costs \(O(|S|^2)\) per pass in the course's account. These results are not arbitrary neural actor–critic guarantees. Humanoid and Mobile Robotics supply separate teaching examples of the same planning/learning distinction, with their own provenance.

## Algorithmic structure

ADPRL adds optimistic policy iteration with incomplete evaluation, multi-step/geometrically averaged and λ-policy operators, asynchronous/Gauss–Seidel schedules, distributed VI, state-action cost representations and linear-programming formulations. Assignment 1 considers finite-horizon truncation and state/control/disturbance-dependent discounting. Exact advanced-operator formulas/conditions are absent from that map; they are not filled in from general knowledge or inferred from the separately supported scalar-discount theorem.

[Projected evaluation](projected-policy-evaluation.md) changes the representation from full tables to approximations. Exact operator reasoning cannot be transferred unqualified to a mismatched projection norm.

## Detail gap and provenance

The original supplementary map names monotonicity/contraction without complete hypotheses/rates. The new discounted-reward/tail statements above are separately supported by Deep RL, not retroactively attributed to ADPRL. Full advanced-operator proofs/inverse formulas remain unavailable. See [Deep RL evidence](../evidence/mgt001299.yaml), `markov-planning`, alongside the original supplementary claim.

[Supplementary Bellman claim](../evidence/tum-approximate-dynamic-programming.yaml) → [ADPRL](../../02_profiles/supplementary/approximate_dynamic_programming.md), Sequential decisions and exact dynamic programming and Policy iteration and computational variants. Academic credit is not established; learning relationship is unspecified.

Cognitive Systems supplies independent accredited coverage of Markov processes/MDPs, expected discounted state/action values, Bellman evaluation/optimality, GPI, policy/value iteration and gridworld backups. These strengthen the theoretical source base without adding personal implementations. The accompanying CartPole example has a narrower bootstrap architecture described in [deep value learning](deep-value-learning.md), not a new Bellman theorem.
