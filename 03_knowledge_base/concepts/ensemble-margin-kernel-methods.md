---
id: "ensemble-margin-kernel-methods"
title: "Trees, ensembles, margins and kernel representations"
domains:
  - "machine-learning"
  - "probability-statistics-uq"
  - "optimization"
evidence_refs:
  - "ma4802:ensembles-margins"
  - "tum-machine-learning-optimization:regression-kernels"
  - "additional-cognitive-systems:statistical-examples"
status: "reviewed"
---


# Trees, ensembles, margins and kernel representations

## Partitions, bootstrap aggregation and sequential weighting

CART recursively selects axis-aligned splits using squared regression error or classification impurity (misclassification, entropy, Gini). Leaves estimate means or class frequencies; depth/pruning/CV control complexity. XOR exposes immediate-improvement stopping limitations. Bagging aggregates bootstrap-trained learners; forests additionally subsample candidate split features to reduce correlation. Out-of-bag predictions exclude trees trained on that observation, giving an internal comparison mechanism rather than an independent external validation set.

AdaBoost adds weak learners using weighted classification error:
\[
\alpha_t=\tfrac12\log\frac{1-\varepsilon_t}{\varepsilon_t},
\qquad w_i\leftarrow w_i\exp(-\alpha_ty_ih_t(x_i)),
\]
then renormalizes. Exponential-loss minimization gives that coefficient and a population optimum of half log-odds. Early stopping limits the additive sequence. Unlike bagging, sequential reweighting couples successive fits.

The supported training-error bound is \(\prod_t2\sqrt{\varepsilon_t(1-\varepsilon_t)}\), with edge form \(\exp(-2\sum_t\gamma_t^2)\), \(\gamma_t=1/2-\varepsilon_t\). A uniform positive edge yields \(\exp(-2T\gamma^2)\). This is not a generalization bound; the lecture's alternative missing-factor-2 display is explicitly not adopted.

## Separation and functional representation

Hard-margin SVM minimizes \(\|\beta\|^2/2\) subject to \(y_i(\beta^Tx_i+\beta_0)\ge1\); soft margins use hinge penalties for nonseparable data. Support vectors and signed distances connect geometry to optimization. Perceptron updates misclassified examples; the finite separable-data convergence proof uses normalized augmented observations and distance to a scaled separator. Nonseparability removes that conclusion; initial conditions affect which separator is found.

MA4802 introduces nonlinear feature/kernel geometry only. Supplementary EI71058 independently adds dual SVM, Gaussian kernels and a representer theorem, but its exact theorem assumptions and detailed dual equations are unavailable at profile depth. This does not retrospectively turn MA4802 into an RKHS course. Lagrangian duality and feature representation are distinct levels of explanation.

Applications include interpretable decision rules, genetic-population classification and Viola–Jones cascades. RL-DT's factored trees predict transitions rather than directly classify a target population; tree syntax does not make the tasks equivalent. Evidence: [Statistical Learning](../evidence/ma4802.yaml) and [supplementary ML](../evidence/tum-machine-learning-optimization.yaml), not personal implemented classification systems.

Cognitive Systems adds introductory perceptron/XOR, SVM geometric margins and illustrative boosted-tree regression. Its short treatment does not supply the full soft-margin/kernel-dual theory available from other sources. Keeping these source scopes separate prevents a new corroborating course reference from implying a deeper theorem or personal ensemble implementation.
