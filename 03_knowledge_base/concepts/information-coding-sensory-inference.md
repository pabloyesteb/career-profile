---
id: "information-coding-sensory-inference"
title: "Information coding, population decoding and sensory inference"
domains:
  - "computational-neuroscience"
  - "probability-statistics-uq"
  - "language-vision-cognition"
evidence_refs:
  - "ei7646:coding-decoding"
  - "ei7646:probabilistic-perception"
  - "additional-cognitive-systems:plasticity-simulation"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "spiking-neuron-plasticity"
  -
    type: "related_to"
    target: "text-tokenization-language-statistics"
---

# Information coding, population decoding and sensory inference

## What information does a response preserve?

For stimulus \(S\) and neural response \(R\),
\[
H(R)=-\sum_r p(r)\log_2p(r),\qquad
I(S;R)=\sum_{s,r}p(s,r)\log_2\frac{p(s,r)}{p(s)p(r)}.
\]
Mutual information detects dependence that Pearson correlation can miss; it is not a causal effect. Response noise, repeated trials, rate versus precise spike timing, binary response words and temporal bins change the represented channel and information estimate. Information efficiency \(I(R;S)/H(R)\) distinguishes transmitted information from total response variability.

Efficient coding adapts representation to environmental statistics under noise/response constraints. Laughlin's input–output CDF example approximately equalizes response use. Blowfly H1 adaptation and natural-versus-artificial acoustic stimuli show environmental dependence. Sparse natural-image patch codes yield localized oriented receptive fields, but the profile does not specify a complete optimization implementation.

## Population decoding and ambiguous spatial codes

Grid-cell modules share scale/orientation and differ in phase. A single periodic module aliases position; combining scales improves range/resolution. The introductory tuning model is
\[
\Omega_j(x)=n_{\max}\exp\{k[\cos(2\pi(x-c_j)/\lambda_j)-1]\}.
\]
Population-vector/maximum-likelihood decoding combines responses across cells/modules. The recommendation for scale ratios below about 1.5 belongs to its specific model/plots, not a universal grid-cell theorem. Head-direction, place and grid codes carry different variables.

## Perception as an inverse problem

Multiple scenes can produce one sensory image. Generative/internal models map latent causes to observations; Bayesian perception combines likelihood and environmental priors. Natural-scene statistics, sound localization, uncertain visual/motor feedback and fly heading illustrate probabilistic hypotheses, not universal optimality of behavior.

Hierarchical/predictive-coding accounts combine generative feedback with evidence across larger receptive fields/features. Uncertainty-weighted sensory integration in Cognitive Systems complements this frame. An explicitly reserved blackboard derivation is absent, so no unprovided formula is reconstructed.

## Acting to acquire information

Infotaxis uses entropy reduction when searching an uncertain odor source in turbulent plumes. Moth/nematode behavior illustrates active sensing, not a convergence theorem or a personal robot implementation. This complements [belief-state mapping](probabilistic-slam-mapping.md) and [internal motor models](biological-motor-action-models.md): represent latent state, uncertainty and useful observations before choosing actions.

[Language information rates](text-tokenization-language-statistics.md) and [distributional vectors](distributional-lexical-representations.md) also depend on representation and environment statistics; token prediction and spike coding have different observations/objectives. [EI7646 claims](../evidence/ei7646.yaml) and [Cognitive Systems](../evidence/additional-cognitive-systems.yaml) retain theoretical provenance and missing derivations rather than asserting achieved decoding accuracy.
