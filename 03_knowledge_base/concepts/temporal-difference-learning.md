---
id: "temporal-difference-learning"
title: "Sample-based value learning, bootstrapping and off-policy evaluation"
domains:
  - "reinforcement-learning"
  - "probability-statistics-uq"
  - "numerical-mathematics"
evidence_refs:
  - "mgt001299:sample-learning"
  - "ei7263:decision-models"
  - "ei7263:factored-models"
  - "tum-approximate-dynamic-programming:sample-linear-algebra"
  - "additional-cognitive-systems:rl-teaching"
status: "reviewed"
---


# Sample-based value learning, bootstrapping and off-policy evaluation

## What is known, sampled or bootstrapped?

Model-based learning estimates transition probabilities/rewards from observations, then solves the empirical MDP. Monte Carlo evaluation averages completed discounted returns for a fixed policy; DP uses expected model backups; TD uses sampled transitions and a bootstrapped value:
\[
\delta=r+\gamma V(s')-V(s),\qquad V(s)\leftarrow V(s)+\alpha\delta.
\]
SARSA's control target uses the behavior policy's actual successor action, \(r+\gamma Q(s',a')\); Q-learning uses \(r+\gamma\max_bQ(s',b)\). The latter learns a greedy target while behaving exploratorily. Learning only \(V\) cannot supply model-free action choice without a transition/reward model.

Exploration includes ε-greedy behavior, optimistic counts and the lecture bonus \(q+k/n\) for visited pairs; its zero-count convention is unspecified. Conditions \(\sum_n\alpha_n=\infty\), \(\sum_n\alpha_n^2<\infty\) distinguish schedules but are not alone a convergence theorem: visitation and model assumptions matter. Regret is introduced without a derived bound. Dyna is named background, not an implemented loop.

## Approximation and numerical evaluation

For \(\widehat V(s;w)\), semi-gradient TD uses \(\Delta w=\alpha\delta\nabla_w\widehat V(s;w)\), treating the bootstrapped target as fixed. Linear features make the derivative a feature vector; general tabular guarantees do not automatically survive approximation. ADPRL adds behavior/target-policy separation and importance sampling, gradient-TD/TD-corrected methods, LSPE/LSTD, Sherman–Morrison online inverse updates and Newton-type interpretations. Exact GTD/LSTD/Sherman–Morrison formulas and their sufficient sampling/feature conditions are absent from that profile and are not reconstructed here.

Supplied `script_09.py` implements named MSBE/MSPBE/API utilities; `script_12.py` supplies GTD/LSTD/value/policy helpers with MazeWorld examples. Random features can yield nonoptimal policies. [Projected evaluation](projected-policy-evaluation.md) retains objective/norm distinctions; no blanket off-policy stability conclusion follows.

## Learned factored models are a separate route

Humanoid RL-DT predicts **relative state changes**, one tree per component plus a reward tree, then plans by value iteration. Product-of-marginals transitions assume conditional independence given state/action. The reference method uses C4.5 information-gain splits; local scikit-learn classifier/regressor submissions are not C4.5 implementations. A heuristic exploitation threshold (40% of known maximum one-step reward in the robot paper) can stop exploration prematurely; visit-based optimism is discussed but absent from the inspected local implementation.

Soccer examples discretize leg/keeper/post measurements and use move-in/move-out/kick actions, camera/ArUco feedback and human kick rewards. The supplied adjusted four-feature implementation has an incomplete Bellman sweep due to assignment outside the inner post-bin loops, plus leg-state/readiness inconsistencies. Its presence demonstrates intended methods, not verified correct planning or personal code authorship. Deep RL's supplied tabular agent likewise has negative-Q greedy-selection and rounding caveats. These qualify software reuse without removing the taught theory.

Evidence: [Deep RL](../evidence/mgt001299.yaml), [humanoid learning](../evidence/ei7263.yaml) and [supplementary ADPRL](../evidence/tum-approximate-dynamic-programming.yaml). No supplied algorithm is promoted to personally implemented RL.

Cognitive Systems complements this with first-visit Monte Carlo/exploring starts/ε-greedy control, TD(0), SARSA versus Q-learning, cliff-walking exploration effects and n-step backup width/depth. Its sampling-versus-expectation distinctions align with this canonical explanation; the supplied DQN-style code is separately qualified rather than counted as personally trained control.
