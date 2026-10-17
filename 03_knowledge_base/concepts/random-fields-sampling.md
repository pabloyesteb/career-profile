---
id: random-fields-sampling
title: Random fields, covariance representations and sampling
domains: [probability-statistics-uq, numerical-mathematics, mathematical-analysis]
evidence_refs: ["ma5348:probability-fields", "ma5348:field-sampling", "ma5348:teaching-code", "ma6015:lognormal-fem-analysis", "ma6015:rare-events"]
status: reviewed
relations:
  - {type: related_to, target: stochastic-pde-discretization}
---

# Random fields, covariance representations and sampling

## Probabilistic objects and regularity

A random field is described by realizations and finite-dimensional distributions, with mean and covariance functions in the second-order setting. A covariance kernel must induce positive-semidefinite matrices. Gaussian, lognormal, weakly stationary and strictly stationary fields are distinct classes; covariance stationarity alone does not describe every distributional property.

Banach-valued random variables require measurability, not merely formal pointwise samples. Numerical UQ covers Borel laws, strong/weak measurability, Pettis measurability, Bochner integration and \(L^p(\Omega;W)\), together with almost-sure/mean convergence, Chebyshev and Borel–Cantelli. Hilbert-valued Gaussian examples and covariance operators extend finite Gaussian-vector descriptions. Kolmogorov continuity addresses existence of sufficiently regular versions; a version and an arbitrary realization cannot be interchanged without the relevant regularity/moment assumptions. Complete constants/hypotheses are not stated in the input profile, so no sharper continuity theorem is asserted here.

## Three sampling representations

1. **Grid covariance factorization.** Assemble covariance at grid locations and use Cholesky or spectral factors to sample a Gaussian vector. Positive-definiteness/semidefiniteness determines whether the chosen factorization works.
2. **Circulant embedding.** For suitable Toeplitz covariance structures, extend to a circulant matrix and use Fourier diagonalization/FFT sampling. The embedding must be positive semidefinite; a nominal minimal extension need not suffice. Sampling cost is part of a multilevel model's work, not free preprocessing.
3. **Karhunen–Loève expansion.** Covariance integral-operator eigenpairs supply orthogonal modes; retaining leading modes gives the profile's optimal finite-rank mean-square representation, with truncation error from discarded eigenvalues. Mean-square and uniform convergence are separate results with different assumptions. Collocation/quadrature approximates eigenpairs; Brownian bridge and Gaussian covariance examples test normalization and truncation.

KLE connects [operator spectra](compact-operator-spectral-theory.md) to stochastic representation; [matrix SVD/PCA](matrix-low-rank-pca.md) gives a related finite-dimensional reduction, not the same error criterion. No unsupported field formula, eigenvalue-decay rate or guaranteed FFT complexity constant is supplied beyond profile depth.

## Numerical use and limits

Lognormal diffusion coefficients \(a=\exp(g)\) ensure samplewise positivity but not uniform bounds across all Gaussian realizations. Fernique-type integrability and coefficient extrema enter PDE analysis; positivity alone is insufficient for a uniform energy estimate. The rare-event seminar's MLE-var changes KL dimension by level, adding Gaussian coordinates when refining and discarding unnecessary components after transitions. That reduces coarse over-parameterization but complicates conditional-sampling bookkeeping.

The Numerical UQ archive supplies MATLAB covariance assembly and spectral sampling (`sample1D.m`), Brownian-bridge/Gaussian KLE eigenpair experiments (`kle_bbridge.m`, `kle_gauss.m`, `kle_gauss_plots.m`), and random-coefficient FEM examples. These are documented teaching resources, not evidence of personally authored sampling software.

Evidence: [Numerical UQ](../evidence/ma5348.yaml) probability/fields and discretization/sampling claims; [seminar](../evidence/ma6015.yaml) lognormal analysis and rare-event claims. See [stochastic PDE discretization](stochastic-pde-discretization.md) for the downstream model/error contract.
