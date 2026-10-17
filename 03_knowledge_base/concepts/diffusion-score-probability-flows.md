---
id: diffusion-score-probability-flows
title: Denoising scores, Langevin sampling and probability-space gradient flow
domains: [machine-learning, probability-statistics-uq, dynamical-systems, optimization]
evidence_refs: ["cit4230003:diffusion", "additional-foml:probability-geometry"]
status: reviewed
relations:
  - {type: related_to, target: invertible-generative-flows}
---

# Denoising scores, Langevin sampling and probability-space gradient flow

## Gaussian corruption and learned reversal

The discrete diffusion model fixes a Gaussian noising chain and learns a Gaussian reverse chain. Its arbitrary-time marginal is
\[
z_n=\sqrt{\bar\alpha_n}x_0+\sqrt{1-\bar\alpha_n}\epsilon,
\]
avoiding all earlier transitions when constructing a training sample. The reverse-model ELBO separates reconstruction, transition KL and terminal-prior KL terms. Conditioning the forward posterior on clean data makes it Gaussian in closed form; the exercise proves the marginal by induction and derives score/noise equivalence \(score=-\epsilon/\sigma_n\) in that conditional setting. It is not a general marginal score identity for an observed noise realization without conditioning.

Learned reverse means/variances can be parameterized through noise prediction. Noise-conditioned denoising score matching covers low-density regions; explicit score matching removes the unavailable data score using learned-score divergence/trace terms. Full coefficient formulas absent from the profile are not invented.

## Sampling and a different optimization geometry

Scores are log-density gradients. Langevin sampling is presented through Euler discretization of an SDE; target stationarity belongs to the limiting small-step/infinite-time setting, not arbitrary finite sampling. Annealed sampling traverses noise levels from near-Gaussian to data; a simplified scheme uses one reverse Langevin-style step per level.

FOML separately interprets density evolution through Fokker–Planck and 2-Wasserstein gradient flow of relative entropy to a target π. Push-forwards/transport, geodesic convexity/HWI, log-Sobolev gradient dominance and Talagrand-type distance control provide distinct links between energy, gradient and distance. Strong log-concavity supports the represented exponential **continuous-time** convergence; unadjusted Langevin introduces discretization error in iteration guarantees. Exact constants/inequalities are not stated in the profile and are not reconstructed.

This connects optimization over samples with optimization over distributions, not a claim that every learned diffusion is strongly log-concave or every discrete sampler inherits a continuous bound.

## Applications and limitations

DALL-E 2/Imagen illustrate encoders, diffusion representation priors, conditional decoding and classifier-free guidance; they are source-era examples, not locally trained systems or current product recommendations. Sampling cost, limited interpretable latents and no cheap exact likelihood distinguish diffusion from [invertible flow models](invertible-generative-flows.md). FOML's MIT-branded material has unresolved exact TUM-delivery provenance; generative-course programming tasks are absent. Evidence: [CIT4230003](../evidence/cit4230003.yaml) and [FOML](../evidence/additional-foml.yaml).
