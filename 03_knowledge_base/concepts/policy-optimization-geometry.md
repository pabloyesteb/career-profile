---
id: "policy-optimization-geometry"
title: "Trust-region policy optimization and continuous-action actor–critic"
domains:
  - "reinforcement-learning"
  - "optimization"
  - "machine-learning"
evidence_refs:
  - "mgt001299:policy-optimization"
  - "in2361:alignment"
status: "reviewed"
---


# Trust-region policy optimization and continuous-action actor–critic

## Distributional change is not parameter distance

TRPO optimizes an old-policy expectation of a likelihood-ratio/advantage surrogate while constraining old/new policy KL divergence. Importance sampling reuses old-policy observations; empirical state-averaged KL is a practical approximation, not the full theoretical bound. The expected outer product of policy scores defines Fisher information and the local KL quadratic geometry. An inverse-Fisher-scaled gradient follows from the local constrained approximation; neural-scale methods need approximate solves and a constraint-respecting step search. Complete sampled/approximate monotonic-improvement guarantees are not supplied.

PPO-Penalty adapts a KL coefficient. PPO-Clip instead maximizes
\[
\mathbb E\left[\min\{r_tA_t,
\operatorname{clip}(r_t,1-\varepsilon,1+\varepsilon)A_t\}\right],
\qquad r_t=\pi_{new}(a_t|s_t)/\pi_{old}(a_t|s_t).
\]
Positive/negative advantages cap incentives on opposite sides. Clipping is an objective modification, not a hard probability-ratio/KL constraint or inherited TRPO theorem. Repeated actor/critic epochs retain old log probabilities from a recent batch. Coding 3 uses categorical logits, stable log-softmax, tanh policy/value MLPs, weighted TD-error advantages, squared return regression and separate Adam optimizers. Its multiple actors are collected **sequentially in one environment**, unlike actual parallel A2C/A3C workers. A2C synchronizes and A3C asynchronously shares gradients from independent environments. Entropy regularization encourages stochasticity, not guaranteed coverage.

## Continuous actions and target updates

DDPG uses a deterministic actor \(\mu_\theta(s)\) to avoid exhaustive continuous-action maximization and a critic differentiable in action. Replay-state actor improvement differentiates the critic through that action. Target actor/critic networks bootstrap values; Polyak updates use
\[
w_{target}\leftarrow\tau w_{online}+(1-\tau)w_{target}.
\]
Added Gaussian action noise provides exploration in the lecture account; the original alternative noise process is only mentioned.

SAC is covered at overview depth: stochastic Gaussian mean/positive variance, tanh-like action squashing, replay, twin Q minima to reduce overestimation and an entropy-augmented objective with manual/learned target-entropy weighting. Older extra-value-network and newer twin-Q forms, plus a discrete variant, are distinguished. Complete SAC updates and DDPG/SAC source implementations are absent; TD3/ACER are outlook names only.

## Method choice and evidence

Discrete/continuous actions, on/off-policy data, collection cost, reuse and stability are meaningful comparison axes. None establishes that a student achieved a CartPole reward, trading return or autonomous-driving deployment. `mgt001299:policy-optimization` in [Deep RL evidence](../evidence/mgt001299.yaml) supports the mathematical/algorithmic account and supplied-code limits. [Credit assignment](policy-gradient-credit-assignment.md) provides the baseline/advantage assumptions independently of the optimizer.

## Preferences in language models: a related, different objective

NLP adds Bradley–Terry preference modeling and reference-policy KL-regularized RLHF, naming PPO as an optimization route. DPO uses a logistic preference loss on preferred/rejected reference-adjusted log-probability ratios, avoiding a separate online RL loop in its presented derivation. Full language/alignment details remain in [sequence-language models](neural-sequence-language-models.md). A malformed source reward/KL equation is not reconstructed; neither PPO clipping nor a learned preference objective establishes universal alignment or task safety.
