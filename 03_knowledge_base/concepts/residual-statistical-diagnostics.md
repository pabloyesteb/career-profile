---
id: "residual-statistical-diagnostics"
title: "Signed residuals, conditional diagnostics and model reliance"
domains:
  - "probability-statistics-uq"
  - "machine-learning"
  - "aerospace-engineering"
evidence_refs:
  - "scientific_paper:residual-methods"
  - "scientific_paper:diagnostic-refinement"
  - "scientific_paper:statistical-library"
  - "scientific_paper:aggregate-fit"
  - "scientific_paper:conditional-diagnostics"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "statistical-risk-model-selection"
  -
    type: "related_to"
    target: "surrogate-domain-split-validation"
---

# Signed residuals, conditional diagnostics and model reliance

## Sign, tail and conditioning are engineering choices

For NGValidation \(e=y-\hat y\): positive residual means a too-low reserve factor (conservative concern), negative means a too-high factor (understated failure concern). Mean signed error can cancel; zero mean implies neither zero magnitude nor balanced counts. MAE/MSE/R² and truth-versus-prediction plots expose different properties.

The paper reports R²=0.999 for **one** failure-mode output over approximately \(10^6\) plotted test points. This does not establish all-six-output accuracy, absence of dangerous tails or certified reliability. Exact dataset/model/run settings are unavailable.

## Global distributions and uncertainty in a quantile

Gaussian, Laplace and Cauchy fits all fail full-range tests at reported \(p<0.001\). Laplace fits the center visually but misses tails, Gaussian/Laplace understate extreme errors, and Cauchy overstates them. A four-parameter Johnson SU fit passes an illustrated KS comparison without exact parameters/p-value. KS and tail-sensitive Anderson–Darling are different diagnostics; fitted-distribution p-value calibration is incompletely specified.

Tail expected-count reasoning compares \(N\,P(e\ge e_x)\) with one. Transformation followed by generalized ESD is proposed. The printed Johnson normalization lacks a parameter and uses an inconsistent transform; the code separately implements
\[
z=\gamma+\delta\,\operatorname{arcsinh}((e-\xi)/\lambda).
\]
This is code evidence, not a retroactive correction or proof of the exact published run.

A nonparametric bootstrap resamples \(N\) observations with replacement and recomputes a statistic. A confidence interval for a residual percentile is **not** the resulting prediction interval. The reported 5th/95th estimates −0.0432/0.0448 have reordered bootstrap endpoints [−0.0548,−0.0353] / [0.0379,0.0586]. Rounded midpoint offsets −0.045/+0.048 give a separate nominal-90% prediction interval. Neither unconditional Gaussian bootstrap convergence nor improved midpoint accuracy is established. [Calibration](prediction-interval-aggregation.md) retains the later nominal-95% results separately.

## Conditional diagnostics find what aggregates hide

Categorical residual boxplots, ANOVA for mean differences and Levene for variance differences show stringer heterogeneity, both \(p<0.005\). Pearson linear and Spearman monotonic trends differ; binning plus ANOVA/Levene exposes nonmonotonic/local structure. The illustrated load has linear-trend \(p=0.59\) yet binned-mean ANOVA \(p=0.01\). Joint frame/stringer heatmaps identify comparatively difficult locations without tabulated exact losses.

Output conditioning uses ten bins and KS comparisons at 0.05: Gaussian compatibility is described only for a limited region \(y<2.25\), and Johnson SU also fails at largest outputs. Text alternates true/predicted conditioning; a deployable output-conditioned interval needs predicted output. Heteroscedasticity is not resolved by one global fitted distribution.

## Model reliance and diagnostic feedback

PFI retains baseline held-out MSE, shuffles one feature and computes \(\Delta MSE_\ell=MSE_{[\ell]}-MSE_{\rm baseline}\). Shuffling preserves that feature's marginal distribution, not joint dependence; reliance is not causal influence and ΔMSE need not always be positive. The 22-feature illustration has three dominant inputs without disclosed identities/exact scores. SHAP/LIME mentions are not additional analyzed experiments; the repository separately imports SHAP and implements joblib-supported permutation diagnostics.

Capacity/regularization/epoch changes and fixed-test training-size learning curves are diagnostic heuristics, not guaranteed improvements. “Boosting” means iterative refinement here, not an AdaBoost implementation. Proposed low-reserve-factor relative loss leaves zero denominators unresolved. The correlation penalty
\[
\gamma\|C(Y)-C(\hat Y)\|_F
\]
targets inter-output Pearson dependence, not a PDE residual or automatic marginal accuracy. Example correlations 0.79 (crippling/buckling) and 0.81 (buckling/compression) describe ground truth, not measured improvements. Negligible PFI, PCA and sparse outgoing weights suggest feature selection; VAE/GAN augmentation, PINNs and drift monitoring are undeveloped alternatives.

[NGValidation evidence](../evidence/scientific_paper.yaml) distinguishes published collective findings from library procedures and personal workflow changes. [Statistical risk](statistical-risk-model-selection.md), [causal assumptions](causal-graphical-models.md) and [rare-event reasoning](sensitivity-rare-event-estimation.md) provide conceptual connections without claiming an actuarial or causal-identification experiment.
