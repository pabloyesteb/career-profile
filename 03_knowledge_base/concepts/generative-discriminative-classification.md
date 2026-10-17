---
id: "generative-discriminative-classification"
title: "Generative and discriminative classifiers and likelihood fitting"
domains:
  - "probability-statistics-uq"
  - "machine-learning"
  - "optimization"
evidence_refs:
  - "ma4802:classification"
  - "in2361:classification-evaluation"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "neural-training-data-contracts"
---


# Generative and discriminative classifiers and likelihood fitting

## What distribution is modeled?

Generative classification estimates priors and class-conditional densities; discriminative classification estimates \(P(Y|X)\). Indicator-response least squares can mask intermediate classes in multiclass problems, so regression-to-labels is not automatically a suitable probabilistic classifier.

Gaussian QDA uses class-specific covariances/quadratic boundaries; LDA pools covariance for linear boundaries. Whitening yields nearest-class-mean geometry adjusted for priors. Small samples motivate diagonal/naive-Bayes assumptions, diagonal LDA, class/pooled and isotropic shrinkage, covariance priors and projection. Inverse-Wishart regularization is introduced, not fully rederived here. Mixture and KDE class densities provide nonlinear extensions without establishing general RKHS theory in MA4802.

## Logistic curvature and numerical fitting

Binary logistic **negative log-likelihood** has gradient and Hessian
\[
\nabla\ell=X^T(\mu-y),\qquad \nabla^2\ell=X^TSX,
\quad S=\operatorname{diag}(\mu_i(1-\mu_i)).
\]
The Hessian is semidefinite, and positive definite at finite parameters under full column rank. Complete separation can still preclude a finite unregularized MLE. Convexity alone does not establish existence; ℓ₁/ℓ₂/elastic penalties change that estimation problem. Multinomial softmax uses a reference class for identifiability; one-versus-rest is another classification construction.

IRLS derives from Newton fitting using working response
\[
z_k=X\beta_k+S_k^{-1}(y-\mu_k).
\]
Changing weights distinguish it from a single ordinary least-squares solve. Gradient/metric-steepest descent, exact/backtracking sufficient-decrease search, Newton quadratic models, trust-region/Hessian regularization and quasi-Newton extensions offer different curvature costs. Newton's local quadratic and steepest descent's linear behavior require their regular settings; no unrestricted rate theorem is supplied. A descent direction admits sufficiently small backtracking steps in the represented argument.

## Evidence and applications

Simulated Gaussian and wine comparisons distinguish LDA/QDA/logistic behavior, while likelihood-ratio selection uses coronary-risk data. The covariance exercise's transposed symmetric matrix is not a distinct law; its notebook applies \(A\) versus \(A^T\) as generating transforms. [Statistical Learning evidence](../evidence/ma4802.yaml) preserves these source limits. No personal clinical or predictive outcome follows from the notebook resource. [Risk/model selection](statistical-risk-model-selection.md) and [first-order methods](first-order-stochastic-optimization.md) supply complementary context.

## Text likelihoods and feature assumptions

NLP supplies multinomial Naive Bayes: class priors and conditionally independent bag-of-word likelihoods are estimated from smoothed counts and evaluated in log space. Negation/unseen vocabulary and lexical context affect the feature contract. Logistic/softmax discriminative fitting instead optimizes conditional cross-entropy with L1/L2 regularization; model comparisons need matched data/metrics. The [text-statistics page](text-tokenization-language-statistics.md) preserves tokenization and language-estimation context without treating a generative classifier as a complete language generator.
