---
id: heuristic-adversarial-search
title: Heuristic, adversarial and stochastic search
domains: [optimization, reinforcement-learning]
evidence_refs: ["mgt001299:search-utility", "mgt001299:planning-learning"]
status: reviewed
---

# Heuristic, adversarial and stochastic search

## Problem representation and frontier logic

A search model specifies start state, actions/successors, transition costs, goal test and a returned plan. A state graph has one node per state; an unfolded search tree may repeat states along different paths. This distinction is separate from a graph-search algorithm's marked/closed list. Frontier discipline, goal-test timing, parent links and reconstruction affect completeness and optimality.

DFS uses a stack/recursion, BFS a queue, UCS a priority on accumulated cost \(g\), greedy search a priority on remaining estimate \(h\), and A* \(f=g+h\). BFS minimizes action count under unit costs; DFS need not find a shortest path. The supplied UCS checks goals when removed from the queue and replaces more expensive frontier paths. Admissibility means no overestimate of nearest-goal cost. The source's A* proof is for **tree search**: an optimal-path ancestor has \(f(N)\le f(G_{opt})<f(G_{subopt})\). It does not establish a separate consistent-heuristic/closed-list theorem. Route-distance heuristics and gridworld code provide concrete examples, not personal implementations.

## Utilities change the backup operator

Rational-agent utilities encode preferences under orderability, transitivity, continuity, substitutability and monotonicity axioms. In zero-sum minimax, alternating max/min assumes rational adversarial play; depth limits and evaluation functions lose exact exhaustive-play guarantees. Multiplayer examples propagate utility vectors. Expectimax uses probability-weighted chance nodes rather than worst-case minima, as in uncertain racing costs.

Full minimax has exponential tree cost in the teaching account; depth-limited evaluation trades exact play for tractability. Order-preserving utility transforms preserve minimax ordering but nonlinear transforms can change lottery/expectimax rankings: expected magnitudes matter. This is not an arbitrary monotone-invariance theorem under uncertainty.

## Search with learned evaluation

MCTS cycles through selection, expansion, rollout and backup. AlphaGo combines expert-guided policy learning, self-play/value evaluation and tree search; AlphaGo Zero uses self-play and a joint residual policy/value network. Priors/visit-dependent exploration guide search, while terminal outcomes train value. These are teaching case studies, not locally authored or reproduced systems.

Hierarchical options are temporally extended subpolicies in a semi-MDP; feudal control assigns subgoals/local rewards. Inverse RL infers rewards with nonidentifiability/expert assumptions. Transfer/multitask learning faces action-space changes, exploration failures, gradient/reward-scale conflicts and unequal resources; actor-mimic/distillation are overview names. Multi-agent settings introduce nonstationarity, partial observation and shared-reward credit assignment; centralized training/decentralized execution, shared parameters, communication, factorized values and centralized critics are discussed approaches.

Geometric RRT warm starts, game-tree search and Bellman optimization have related sequential structure but different spaces/objectives. Evidence: [Deep RL claims](../evidence/mgt001299.yaml), search and applied-topic sections. Portfolio trading, autonomous driving, delivery/pricing and neural-combinatorial control are application examples, not personal financial outcomes or deployed autonomy.
