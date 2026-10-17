---
id: variational-generative-inference
title: Variational inference, amortized latent models and autoencoders
domains: [machine-learning, probability-statistics-uq, optimization]
evidence_refs: ["ma4802:generative-representations", "cit4230003:variational-inference", "cit4230003:vae"]
status: reviewed
---

# Variational inference, amortized latent models and autoencoders

## Posterior approximation and a bounded objective

For \(p_\theta(x,z)=p_\theta(x|z)p_\theta(z)\), marginalizing latent variables can be intractable. With trial density \(q\),
\[
\log p_\theta(x)=\mathcal L(\theta,q)
+KL(q(z)\|p_\theta(z|x)),\qquad
\mathcal L=\mathbb E_q[\log p_\theta(x,z)-\log q(z)].
\]
KL is nonnegative and directional; the bound is tight exactly at the posterior (almost everywhere). The Statistical Learning script's reversed inequality is resolved by its explicit supplement, not copied. Variational-family/support mismatch may prevent tightness or make KL infinite.

EM coordinates model and inference updates; restricting a mean-field family makes inference/mini-batching easier but excludes posterior correlations. Monte Carlo estimates objective/parameter gradients when integration is unavailable. Pathwise gradients use parameter-free noise, e.g. \(z=R\epsilon+\mu\) with covariance \(RR^T\), permitting differentiation through sampling. Exercises add exponential scaling/inverse-CDF reparameterization and factorized KL; discrete latents require different treatment, not an assumed Gaussian trick.

## VAE versus ordinary representation learning

An ordinary autoencoder reconstructs through an encoder/decoder bottleneck or copying restriction. Linear autoencoders recover the principal subspace; sparse variants penalize activations and denoising variants reconstruct clean observations from corruption. Historical RBM pretraining followed by backpropagation is a training strategy, not the definition of all autoencoders. Manifold/disentanglement/self-supervised motivations do not guarantee identifiable latent factors.

A VAE amortizes per-instance inference with shared \(q_\phi(z|x)\), a prior and neural likelihood decoder. Its objective is expected reconstruction log-likelihood minus \(KL(q_\phi\|p)\). Gaussian reparameterization is
\[
z=\mu_\phi(x)+\sigma_\phi(x)\odot\epsilon,\quad\epsilon\sim N(0,I).
\]
Positive scales/covariances are enforced (exponentiation in the exercise); mini-batches often use one reconstruction sample. The profile names a closed-form Gaussian KL without a detailed formula, so none is reconstructed here. β-VAE increases KL weight (β>1 in the lecture) to encourage disentanglement, not universal latent interpretability. Unconditional generation uses prior samples and the decoder, not the encoder.

## Interpretation and evidence

Reconstruction, exact likelihood, variational lower bound, posterior approximation and generation are distinct criteria. Image/single-cell denoising, imputation and latent traversal are teaching examples, not personal trained models. [Statistical Learning](../evidence/ma4802.yaml) and [generative-course claims](../evidence/cit4230003.yaml) support the concepts; advertised programming tasks are absent. [Mixture inference](mixtures-latent-inference.md), [invertible flows](invertible-generative-flows.md) and [diffusion](diffusion-score-probability-flows.md) preserve their different objectives.
