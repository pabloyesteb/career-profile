---
id: "regularized-linear-inference"
title: "Linear inference, shrinkage and sparse regression"
domains:
  - "probability-statistics-uq"
  - "machine-learning"
  - "optimization"
  - "numerical-mathematics"
evidence_refs:
  - "ma4802:linear-inference"
  - "tum-machine-learning-optimization:regression-kernels"
  - "additional-cognitive-systems:statistical-examples"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "statistical-risk-model-selection"
---


# Linear inference, shrinkage and sparse regression

## Linear estimation and uncertainty

For Gaussian \(y=X\beta+\epsilon\), full-column-rank least squares gives normal equations, coefficient covariance \(\sigma^2(X^TX)^{-1}\), residual variance with degrees-of-freedom correction and Student-t tests. Gauss–Markov concerns minimum covariance among **linear unbiased** estimators; a biased estimator can have smaller MSE. Collinearity and rank deficiency matter before interpreting either coefficients or an inverse.

With centered predictors/intercept handled separately,
\[
\widehat\beta_\lambda=(X^TX+\lambda I)^{-1}X^Ty,
\quad H_\lambda=X(X^TX+\lambda I)^{-1}X^T.
\]
Positive ridge regularization stabilizes the normal system while introducing bias. Along SVD directions the response shrinkage is \(d_j^2/(d_j^2+\lambda)\), and \(\operatorname{tr}(H_\lambda)=\sum_jd_j^2/(d_j^2+\lambda)\). Tikhonov replaces the penalty with \(\lambda\beta^TQ\beta\), subject to invertibility of the resulting normal matrix. Gaussian-prior scaling in the source yields ridge posterior mean and covariance \(\sigma^2(X^TX+\lambda I)^{-1}\); prior/posterior uncertainty is not frequentist test error. Laplace/Student noise are briefly discussed robust-likelihood alternatives.

## Sparsity and normalization conventions

Lasso uses an ℓ₁ constraint/penalty, subgradient optimality and residual-updating coordinate soft thresholding. The script's **unscaled** squared loss gives threshold \(\lambda/2\); library objectives need not use that normalization. Geometric corners/faces explain thresholding rather than ridge's proportional shrinkage. Laplace priors support a posterior-mode interpretation; rank deficiency can make coefficient solutions nonunique.

Elastic net combines ℓ₁/ℓ₂ penalties and groups correlated predictors; an augmented-design exercise converts it to Lasso. The source's α weights ℓ₂, unlike library `l1_ratio`. Additional represented methods include LARS paths, compressed sensing, Dantzig residual-correlation ℓ∞ constraints and group-size-weighted group-Lasso penalties. These supplements are not all supplied implementations.

## Connections and limits

[SVD](matrix-low-rank-pca.md) explains direction-dependent conditioning; [convex/proximal optimization](proximal-block-optimization.md) explains how the nonsmooth problem is solved. Supplementary ML adds least-squares early stopping as algorithmic regularization, but its exact spectral derivation is absent. [Model selection](statistical-risk-model-selection.md) separates statistical tuning from convergence of a fixed objective.

The source's manual augmented-design coordinate loop omits columns and its nominal penalty-mixture study varies the wrong parameter; `.score()` is mislabeled error. These establish intended teaching methods, not verified numerical outcomes. Evidence: [MA4802](../evidence/ma4802.yaml), linear inference/exercises, and [supplementary ML](../evidence/tum-machine-learning-optimization.yaml).

Cognitive Systems independently supplies normal-equation/projection and Gaussian-noise likelihood viewpoints plus a scikit-learn `PolynomialFeatures + Ridge` exercise. The explicit Gram inverse requires nonsingularity; changing degree and regularization changes capacity as well as conditioning. This is an additional accredited teaching example, not a separately attributed regression implementation.
