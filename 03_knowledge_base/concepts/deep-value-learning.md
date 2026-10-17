---
id: "deep-value-learning"
title: "Deep Q-learning, replay and value-network variants"
domains:
  - "reinforcement-learning"
  - "machine-learning"
evidence_refs:
  - "mgt001299:deep-values"
  - "additional-cognitive-systems:rl-teaching"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "distributional-value-coding"
  -
    type: "related_to"
    target: "temporal-difference-learning"
---


# Deep Q-learning, replay and value-network variants

## DQN's data and target contracts

A value approximator can take a state and emit values for discrete actions, or take a state/action pair and emit a scalar. Correlated transitions and moving bootstrapped targets motivate replay and target networks. DQN stores \((s,a,r,s',done)\), samples minibatches and fits
\[
y=r+\gamma(1-done)\max_b\widehat Q(s',b;w_{target})
\]
against the online network's selected-action output. Collection, exploration, replay, optimization and target synchronization are distinct loop stages. Semi-gradients do not differentiate through the target. Architecture, learning/exploration schedules, capacity, minibatch size and copy frequency affect behavior.

The CartPole solution uses four observations/two actions, two 64-unit tanh layers, linear Q outputs, Adam, bounded `deque` replay, random minibatches, indexed Q selection and weight save/load/evaluation loops. It is supplied teaching code, not an achieved personal score. Updated code ignores Gymnasium truncation and uses only termination; time-limit semantics therefore require review. Older Gym/TensorFlow versus Gymnasium/Keras versions are not interchangeable environments.

## Distinct improvements

Double DQN decouples successor-action selection (online network) from evaluation (target network), addressing maximization overestimation. Prioritized replay samples
\[
P(i)=p_i^a/\sum_kp_k^a,\qquad
w_i\propto(1/(NP(i)))^b,
\]
with normalized importance weights. The priority exponent \(a\) and bias-correction exponent \(b\) have different roles. Proportional absolute-TD-error priorities add a positive offset; rank-based priorities reduce sensitivity to magnitude outliers. Correcting sampling bias and preserving diversity are separate issues.

Dueling networks separate a shared representation into value/advantage streams and combine
\[
\widehat Q(s,a)=\widehat V(s)+\widehat A(s,a)
-\operatorname{mean}_b\widehat A(s,b).
\]
Rainbow combines these mechanisms with multistep learning, distributional returns and noisy exploration. Those latter additions are overview content here, not fully derived coding implementations. The [distributional dopamine presentation](distributional-value-coding.md) supplies separate conceptual evidence; it does not establish a personally trained distributional DQN.

## Interpretation and source limits

Atari replay/target ablations are published teaching examples, not local experiments. Hand-worked linear-feature minibatches explain update mechanics without being deep-network training. Replay decorrelation, target stabilization and a terminal mask are algorithmic design choices, not unconditional neural convergence guarantees. Evidence: `mgt001299:deep-values` in [Deep RL evidence](../evidence/mgt001299.yaml), value approximation/DQN and variant sections.

## A supplied variant without a target network

Cognitive Systems' CartPole program uses two **32-unit ReLU** hidden layers, linear action values, replay/minibatches, ε-greedy behavior, terminal reward shaping and MSE/Nadam fitting. Unlike the Deep RL example above, it bootstraps using the **same online network** and has no separate target network. Replay alone therefore does not make it the full stabilized canonical DQN algorithm. Its older Gym four-result `step`/single-result `reset` and Keras optimizer API remain untested compatibility limits. No personal training reward or successful run is inferred.
