---
id: distributional-value-coding
title: Distributional return representations and asymmetric prediction errors
domains: [reinforcement-learning, computational-neuroscience, probability-statistics-uq]
evidence_refs: ["ei7263:distributional-knowledge", "ei7263:distributional-presentation"]
status: reviewed
---

# Distributional return representations and asymmetric prediction errors

## More than a scalar expectation

The named presentation on Dabney et al.'s *A Distributional Code for Value in Dopamine-Based Reinforcement Learning* (Nature, 2020) contrasts expected return with a population representing a return/value distribution. Positive and negative prediction errors have different scales \(\alpha_+,\alpha_-\); optimistic/pessimistic channels are indexed by
\[
\tau=\frac{\alpha_+}{\alpha_++\alpha_-}.
\]
With approximately linear responses on each side, predictions relate to **expectiles**. Expectiles generalize the mean; quantiles generalize the median. They are not interchangeable distributional labels. The profile supplies no full expectile-loss derivation or distributional Bellman equation, so neither is reconstructed.

Reversal points mark rewards at which response changes sign. A set of reversal points and asymmetries supports approximate decoding of outcome distributions. Variable reward-magnitude/probability tasks examine diverse VTA dopaminergic/GABAergic responses; repeated-trial consistency and asymmetry/reversal associations distinguish the scientific hypothesis from merely averaging neural noise.

## Scientific interpretation and personal activity

Pablo Yeste Blesa's supplied presentation documents analysis/explanation of this research. It is not authorship of the original article, a personal neural-recording experiment or a distributional-RL implementation. The source reports no local quantitative replication. Deep RL's Rainbow overview provides a separate algorithmic connection to return distributions, not proof that the biological model and a DQN were personally combined.

This broadens the vocabulary of uncertainty: a distribution of future rewards differs from a prediction interval around a surrogate response or sampling uncertainty in an estimated expectation. Representing distributional structure does not by itself establish a risk-sensitive control objective. Evidence: the knowledge and personal-presentation claims in [humanoid evidence](../evidence/ei7263.yaml), exact named presentation section and supporting-paper locators retained there.
