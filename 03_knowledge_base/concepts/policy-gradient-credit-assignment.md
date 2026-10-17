---
id: policy-gradient-credit-assignment
title: Policy gradients, compatible critics and temporal credit assignment
domains: [reinforcement-learning, optimization, probability-statistics-uq]
evidence_refs: ["mgt001299:policy-gradients", "mgt001299:multistep-credit", "tum-approximate-dynamic-programming:sample-linear-algebra"]
status: reviewed
relations:
  - {type: related_to, target: policy-optimization-geometry}
  - {type: related_to, target: temporal-difference-learning}
---

# Policy gradients, compatible critics and temporal credit assignment

## Scores, returns and baselines

Direct policy parameterization handles stochastic decisions and continuous actions. Episodic initial-value and continuing state-weighted objectives require their corresponding visitation measures; the source does not supply a universal normalization/proof. The score identity produces policy gradients weighted by \(Q^\pi(s,a)\). For fixed-variance Gaussian mean \(f(s)^T\theta\), the score is \((a-\mu)f(s)/\sigma^2\); feature-softmax scores are \(f(s,a)-\mathbb E_{b\sim\pi}f(s,b)\).

REINFORCE weights scores by completed-episode reward-to-go: no bootstrapped value-target bias, but high trajectory variance and no direct license for arbitrary stale replay. Action-independent baselines have zero expected score contribution; \(A^\pi=Q^\pi-V^\pi\). With exact \(V^\pi\), the one-step TD error is conditionally unbiased for advantage; an approximate value generally introduces bias. Q actor–critic samples the successor action under the current policy rather than taking Q-learning's maximum.

Compatible critic approximation requires \(\nabla_w\widehat Q=\nabla_\theta\log\pi\) and minimization of the corresponding policy-weighted squared Q-error. The MSE first-order condition supports exact expected-gradient preservation under those conditions, not for arbitrary neural critics. Exercises construct centered-softmax linear features. Stochastic policies add randomness but do not guarantee visitation coverage; finite-difference policy gradients are a separate noisy/costly numerical approach.

## Forward targets and backward traces

n-step returns interpolate between one-step bootstrapping and completed Monte Carlo returns. TD(λ) weights them by \((1-\lambda)\lambda^{n-1}\), with remaining finite-episode mass on the full return. Backward accumulating state traces satisfy
\[
E_t(s)=\gamma\lambda E_{t-1}(s)+1(S_t=s),\qquad
\Delta V(s)=\alpha\delta_tE_t(s).
\]
Function approximation replaces the indicator by \(\nabla_w\widehat V(S_t;w)\); policy-score traces similarly propagate actor credit. Fixed-weight/end-of-episode updates support the forward/backward equivalence proof. Online changing weights can break exact equivalence; λ=0 gives TD(0), and small steps only make the illustrated difference small.

The fixed-weight episodic identity
\[
G_t^\lambda-\widehat V(S_t)
=\sum_{k\ge t}(\gamma\lambda)^{k-t}\delta_k
\]
requires the represented terminal/limiting treatment. GAE names this weighted-TD-error advantage structure. The supplied PPO code uses `signal.lfilter` discounted sums, while fitting the value network to reward-to-go, not to policy advantages. It is not a verified generic rollout implementation: reward-positive masking and termination-only handling restrict reuse.

Evidence: [Deep RL claims](../evidence/mgt001299.yaml), policy-gradient/E6 and multistep/E7/Coding 3 sections; [ADPRL](../evidence/tum-approximate-dynamic-programming.yaml) adds named traces/importance-sampling context without complete derivations. No personal actor–critic training is established.
