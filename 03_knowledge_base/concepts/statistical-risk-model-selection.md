---
id: "statistical-risk-model-selection"
title: "Statistical decision risk, generalization and model selection"
domains:
  - "probability-statistics-uq"
  - "machine-learning"
evidence_refs:
  - "ma4802:risk-selection"
  - "tum-machine-learning-optimization:risk-data"
  - "in2361:classification-evaluation"
  - "additional-cognitive-systems:statistical-examples"
  - "scientific_paper:diagnostic-refinement"
status: "reviewed"
---


# Statistical decision risk, generalization and model selection

## The prediction question determines the target

Under a joint law of \((X,Y)\), minimizing expected loss pointwise gives the conditional mean for squared loss, median for absolute loss and \(\arg\max_cP(Y=c|X=x)\) for zero–one classification loss. These are different optimal predictions, not interchangeable notions of accuracy. Training samples are i.i.d. in the represented statistical framework; the empirical objective and population risk are different quantities.

Global parametric regression and neighborhood-based kNN encode different regularity/locality assumptions. kNN consistency is stated for \(N,k\to\infty\), \(k/N\to0\), with further mild regularity not fully developed in the profile. Weighted-response calculations in exercises distinguish conditional/unconditional bias and variance. Prediction error includes irreducible response noise, not just error estimating a noiseless regression function. High-dimensional fixed-mass neighborhoods and near-orthogonal random vectors explain why local methods can demand more data.

No-free-lunch precludes a universally best predictor without domain assumptions. Double-descent plots distinguish model-size and training-epoch effects, interpolation thresholds and nonmonotone test risk in particular polynomial/MNIST/CIFAR examples. They are not a theorem that overparameterization always improves performance.

## Selection and statistical comparison

Hold-out, repeated splits, K-fold and leave-one-out procedures estimate different practical comparison schemes. Hyperparameter selection uses validation, not the final test set; selected models are refitted on training data. Scaling is fitted only on training observations. Accuracy, prediction/MSE, ROC/AUC and out-of-bag estimates answer different evaluation questions.

AIC/BIC compare likelihood with model complexity under asymptotic/model assumptions. Ridge effective degrees of freedom are \(\operatorname{tr}(H_\lambda)\); active coefficients supply a Lasso complexity proxy. Exact penalty normalizations are not independently reconstructed from the source. Nested logistic likelihood-ratio tests use an asymptotic chi-square reference with added-parameter degrees of freedom; heart-risk exercises contrast p-value forward selection with ℓ₁ selection. This is statistical comparison, not clinical validation.

## Generalization and data quality

Supplementary ML adds uniform convergence, Hoeffding/union bounds, algorithmic stability and early stopping as algorithmic regularization. Exact bounds and stability conditions are unavailable at its map depth, so none is invented. Optimization error is not generalization error.

Its data-curation deck also distinguishes distribution shift, pretraining/fine-tuning, feature-selection leakage, heuristic filtering, deduplication and learned quality filters. DCLM/FineWeb/C4 examples are source-era illustrations with controlled model/compute/token comparisons, not current dataset rankings. Reproducible sampling does not guarantee representativeness or causal validity.

Evidence: [Statistical Learning](../evidence/ma4802.yaml) decision/selection sections and [supplementary ML](../evidence/tum-machine-learning-optimization.yaml). Supplied notebook experiments are taught resources, not personally achieved metrics. See [linear inference](regularized-linear-inference.md), [classification](generative-discriminative-classification.md) and [causal models](causal-graphical-models.md) for distinct inferential targets.

## Structured-output metrics and matched comparisons

NLP broadens evaluation beyond scalar accuracy: micro/macro F1, retrieval rank, translation n-grams, attachment, span/cluster agreement and human adequacy assess different targets. Paired bootstrap system comparison resamples common examples rather than treating correlated predictions as independent; the ambiguous slide p-value wording remains unavailable, not a generic test formula.

Cognitive Systems' capacity/Occam/regularization and polynomial-Ridge examples reinforce the distinction between model capacity, fit and held-out behavior. NGValidation adds a further practical contrast: fixed-test learning curves for acquisition differ from error-versus-epoch stopping and from pyLowOrder's external changing-test-set data comparisons. Diagnostic refinements are hypotheses for testing, not guaranteed improvements or additional achieved personal metrics.
