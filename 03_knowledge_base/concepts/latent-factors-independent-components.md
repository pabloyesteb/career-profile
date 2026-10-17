---
id: latent-factors-independent-components
title: Latent factors, probabilistic PCA and independent components
domains: [machine-learning, probability-statistics-uq, numerical-mathematics]
evidence_refs: ["ma4802:latent-factors"]
status: reviewed
relations:
  - {type: related_to, target: matrix-low-rank-pca}
---

# Latent factors, probabilistic PCA and independent components

## Gaussian factors and reconstruction

Factor analysis maps Gaussian latent variables through a linear loading matrix with diagonal observation noise, giving mean \(W\mu_0+\mu\) and covariance \(W\Sigma_0W^T+\Psi\). Rotational/scale/mean ambiguities require normalization or structural restrictions. Gaussian conditioning supplies latent scores; EM is discussed for fitting/missing data.

PPCA restricts noise to be isotropic. The profile supports leading-covariance-eigenpair loading solutions with orthogonal rotational ambiguity and noise estimated from discarded eigenvalues, but not a reliably printed full likelihood formula. The zero-noise limit connects to ordinary PCA. Improving reconstruction with more components and selecting component count by held-out likelihood are different objectives.

Ordinary PCA's orthonormal reconstruction theorem equates least squared reconstruction error with maximal projected variance; centered-data SVD supplies directions/scores without forming feature covariance. Linear autoencoders recover the principal subspace without necessarily an orthonormal learned basis. See [SVD/PCA](matrix-low-rank-pca.md) for that canonical matrix geometry rather than a second duplicate derivation.

## Independence is stronger than whitening

ICA assumes invertible instantaneous mixing \(X=AS\) of independent sources. Scaling, signs and order are indeterminate; PCA whitening removes correlation but not general statistical dependence. The represented separability theorem assumes independent finite-covariance sources and at most one Gaussian/deterministic component in its setting, giving identification up to scaling/permutation. A positive twice-differentiable density proof in two dimensions uses mixed log-density derivatives; full generalization beyond those source conditions is not asserted.

For unmixing \(B\), likelihood uses \(\log|\det B|+\sum_i\log p_i(b_i^Tx)\). Unknown source densities make the estimation semiparametric; ambiguous score-sign terminology prevents adopting the source's consistency inequality as a standalone verified theorem. FastICA is a supplied library method, not an extracted full fixed-point derivation.

Noisy mixed sine/square/sawtooth signals, Olivetti face loadings/reconstructions/noise and wine PCA-versus-LDA illustrate distinct assumptions, not personal signal-recovery or medical results. Evidence: `ma4802:latent-factors` in [Statistical Learning claims](../evidence/ma4802.yaml).
