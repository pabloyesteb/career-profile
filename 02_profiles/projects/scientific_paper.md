# Scientific paper — Statistical validation of industrial supervised-learning surrogates

## Publication identity and evidence

| Field | Value |
|---|---|
| Stable profile identifier | scientific_paper |
| Title | Towards certification: A complete statistical validation pipeline for supervised learning in industry |
| Authors, in published order | Lucas Lacasa; Abel Pardo; Pablo Arbelo; Miguel Sánchez-Domínguez; Noelia Bascones; Pablo Yeste; Alejandro Martínez-Cava; Gonzalo Rubio; Ignacio Gómez; Eusebio Valero; Javier de Vicente |
| Journal | Expert Systems With Applications |
| Publication | Volume 277 (2025), article 127169 |
| DOI | 10.1016/j.eswa.2025.127169 |
| Publisher identifier | S0957417425007912 |
| Publication dates | Received 6 November 2024; revised 29 January 2025; accepted 4 March 2025; available online 13 March 2025 |
| Local authoritative source | `00_sources/article/1-s2.0-S0957417425007912-main.pdf` |
| Source extent | 17 PDF pages; 17 numbered figures; equations (1)–(10); no numbered tables or appendices |
| Source SHA-256 | `32ac496f492cadee89d9675beaad3ab0997aca3ae83ef52aeac8fff8efd9ac58` |
| Profile status | complete_validated |

Bibliographic information is supported by PDF p. 1 and its metadata. The local PDF was resolved from `sources.article_pdf` in `config/sources.yaml`, relative to that configuration's directory, and verified against `01_inventory/files_manifest.csv`. It is the sole technical source for this profile. The [publication DOI](https://doi.org/10.1016/j.eswa.2025.127169) and [publisher page](https://www.sciencedirect.com/science/article/pii/S0957417425007912) identify the work; no external literature or repository was analyzed to expand its content.

References below use **[Paper, section, equation/figure, PDF page]**. Physical PDF page numbers agree with printed article pages. Analysis completed 2026-10-14. No repository revision applies because this task analyzes the published PDF only.

## Attribution and knowledge-use boundary

**Explicit user attribution:** the CRediT statement assigns **Pablo Yeste: Software, Visualization, Investigation**. He is a coauthor affiliated with the Department of Applied Mathematics, ETSI Aeronáutica y del Espacio, Universidad Politécnica de Madrid; the published contact is `p.yesteb@upm.es`. [Paper, p. 1; CRediT statement, p. 16.]

The same three CRediT categories are assigned to Pablo Arbelo, Miguel Sánchez-Domínguez and Noelia Bascones. Conceptualization/methodology/formal analysis and writing roles are assigned separately in the statement. It does **not** allocate particular algorithms, figures, experiments or code modules among the four Software/Visualization/Investigation contributors. Consequently this profile does not claim that Pablo individually devised the complete pipeline, implemented every method, performed all experiments or wrote every section.

The user explicitly confirms that the paper's complete technical content corresponds to their knowledge. Accordingly the technical material below is available for later knowledge-base use, independently of whether individual implementation ownership can be established. The distinction is between **knowledge represented by the work**, **explicit contribution categories**, and **unresolved task-level authorship**; the latter does not block this profile.

The collaboration is situated in an Airbus–UPM working group on surrogate verification/validation for loads and stress analysis. The acknowledgments identify ONEiRE (P220021406), funded by CDTI, and other supporting projects. This is context for the coauthored work, not evidence that the user personally managed grants or held an Airbus employment role. [Paper, §1, p. 2; acknowledgments, p. 16.]

## Research problem, motivation, and contribution

Industrial surrogates can replace or complement expensive engineering computations, but a small average prediction error does not establish dependable behavior throughout an operating domain. Aerospace use particularly requires distinguishing unsafe errors, identifying poorly sampled regions, understanding model reliance on inputs and qualifying prediction uncertainty. The paper addresses the absence of an explicit, practical statistical validation procedure at the required level of engineering scrutiny. [Paper, §§1, 4, pp. 1–3.]

Its principal contribution is an integrated **ten-node directed validation workflow**, combining data preparation, split auditing, model training, multiscale residual analysis, explainability, iterative refinement and calibrated prediction intervals. Feedback edges make validation iterative rather than a final scalar score. The workflow combines established ML/statistical methods with a proposed **voxel tessellation and proximity method (VTPM)** for split assessment and an assembled multiscale uncertainty approach. [Paper, Fig. 1, p. 4; §§4.1–4.10.]

The aim is to contribute evidence toward industrial certification, **not to demonstrate that a model or the pipeline has received regulatory certification**. References to EASA/design assurance explain the motivation; the paper is not a legal compliance determination or a complete airworthiness approval process. Its worked application is supervised aerostructural regression, not reinforcement learning or operational aircraft control. [Paper, §§1, 3, 5.]

## Engineering application and experimental evidence

### Aerostructural surrogate task

The application concerns semi-monocoque fuselage skin/stringer panels subjected to axial, hoop and shear loading, pressure and temperature. Location is described through frames and stringers. The surrogate predicts six reserve-factor outputs for:

1. Forced Crippling.
2. Column Buckling.
3. In Plane.
4. Net Tension.
5. Pure Compression.
6. Shear Panel Failure.

The stated input dimension is **26**, representing loads and maneuver specifications; the six outputs are stated to lie in **[0,5]**, described as a logarithmic risk-related scale, with lower reserve factors indicating greater failure concern. These are continuous engineering outputs, not six class probabilities. The paper does not supply a conversion from reserve factor to calibrated failure probability, complete structural governing equations or a numerical stress-analysis solver. Forced crippling is motivated through buckled skin forcing attached stiffener flanges out of plane. [Paper, §3, pp. 3–4; Fig. 2.]

The illustrated test scatter has approximately **10⁶ points** for one failure-mode reserve factor. Voxel split auditing involves approximately **800 voxels**. Exact total/train/calibration/validation counts, full feature names, precise dataset-generation provenance and a reproducible sample-selection specification are not given. Figure 14 separately illustrates PFI with **22 features**; the paper does not explain whether these are a reduced subset of the original 26 or a distinct illustrative configuration. No reduction from 26 to 22 is inferred. [Paper, Figs. 4, 6, 14, pp. 7–8, 13.]

The data-availability statement explicitly says the authors lack permission to share the data. The PDF is sufficient to profile the published methods and reported findings, but not to reproduce the numerical study independently. [Paper, p. 16.]

### Nature of comparisons and reported experiments

This is primarily a methodological pipeline illustrated through one industrial problem, **not a controlled benchmark of many trained architectures**. Gaussian, Cauchy, Laplace and Johnson SU fits are residual-model comparisons. Train/test errors and shuffled-feature errors are diagnostics/baselines within the pipeline; global versus conditional uncertainty intervals compare uncertainty descriptions. The paper does not report numerical MAE/MSE tables across competing ML models, training speedups, an ablation of every pipeline node or a quantified improvement from each suggested refinement.

Figure 10 is explicitly an artificial statistical illustration; Figures 5 and 15 are schematic learning/bias–variance diagrams. Their shapes and illustrative statistics must not be presented as measured performance of the industrial surrogate. Numerical industrial observations and methodological recommendations are distinguished throughout this profile.

## Mathematical and computational methodology

### 1. Supervised regression, parameterization, and optimization

*Evidence: [Paper, §2, pp. 2–3; Eqs. (1)–(6)].*

The model is a parameterized map

\[
\widetilde{\mathbf Y}=\mathcal F(\mathbf X;\mathbf W),\qquad
\mathbf X\in S_X\subset\mathbb R^n,\quad
\widetilde{\mathbf Y}\in S_{\widetilde Y}\subset\mathbb R^m.
\]

The labeled dataset consists of input/ground-truth pairs, partitioned into disjoint training and test sets whose union is the full dataset, Eq. (1). Feedforward networks compose affine transformations and nonlinear activations such as ReLU. Training minimizes

\[
\mathcal L(\mathbf W)=E(\mathbf W)+\lambda R(\mathbf W),\qquad
\mathbf W^*=\arg\min_{\mathbf W}\mathcal L(\mathbf W).
\]

MSE and MAE aggregate squared or absolute prediction discrepancies, Eqs. (3)–(4). In the multi-output displays the paper leaves the componentwise aggregation implicit; this profile does not invent an output weighting. L2/Tikhonov regularization limits weight magnitude, while L1 encourages sparse parameters. The printed L2 expression is `R(W)=‖W‖₂`; it is not silently replaced with a squared norm.

**Gradient descent**, Eq. (6), updates `W ← W−η∇W L`; **backpropagation** computes derivatives. Stochastic/mini-batch variants and adaptive learning rates, including **Adam**, are discussed as standard choices. The nonconvex training objective motivates accepting sufficiently good local solutions rather than claiming a certified global minimum. The paper does not specify which optimizer/hyperparameter configuration generated every industrial figure.

### 2. Data preparation, uncertainty, and geometric encoding — node 1

*Evidence: [Paper, §4.1, pp. 3–5; Fig. 2].*

- **Space-filling design / Latin hypercube sampling:** choose feature combinations to cover relevant engineering regions when simulations or experiments are expensive. This is guidance, not an explicitly documented generation procedure for the complete application dataset.
- **Data uncertainty and multifidelity inputs:** experiments and simulations can have measurement/numerical errors and unequal fidelity. The pipeline can associate input/output uncertainty with nominal labeled samples rather than treating them as exact.
- **Uncertainty-based augmentation:** in a scalar example, independently draw `q` input and `q` output samples from prescribed distributions and form `q²` pairs. Independence is an assumption; the footnote allows known covariance to modify sampling. Percentile bounds alone do not specify a unique sampling law. The replicas represent assumed uncertainty, not newly measured error-free physical truth.
- **Curse of dimensionality:** increasing feature dimension increases the number of combinations requiring coverage. More samples, dimensionality reduction and feature selection offer different responses; duplicating/perturbing existing samples need not fill genuinely unexplored regions.
- **Geometry-aware categorical encoding:** frame position becomes an ordinal axial coordinate; stringer position becomes a periodic pair `(cos θ,sin θ)`, with `θ_k=2πk/q`. This preserves circumferential adjacency without an artificial discontinuity at the angle wraparound, and avoids high-cardinality one-hot expansion where physical ordering is known.
- **Normalization and PCA:** min–max scaling/standardization place features on comparable scales. PCA constructs orthonormal variance-ranked combinations of training features to reduce effective dimension. Fit normalization statistics and PCA **on training data only**, then apply the same transformations to held-out data, avoiding preprocessing leakage.

### 3. Train–test adequacy, interpolation, and VTPM — node 2

*Evidence: [Paper, §4.2, pp. 5–6; Eq. (7); Definition 1; Figs. 3–4].*

The paper focuses on holdout validation, commonly 80/20, while acknowledging k-fold cross-validation. It asks whether the split avoids duplicated/nearly duplicated cases and whether training/test input distributions adequately resemble one another. Equation (7) expresses distributional equality as the desired ideal, not an empirically proved identity.

**Convex-hull interpolation:** Definition 1 requires every test input to belong to the convex hull of training inputs. Explicit high-dimensional hull construction and membership checks can be costly; hull membership also fails to detect interior data holes. The paper additionally recognizes that successful neural prediction can involve extrapolation in high dimensions. Thus hull membership is discussed as a possible diagnostic, **not established as a necessary-and-sufficient generalization theorem**.

The proposed **VTPM** operationalizes split inspection:

1. Partition training points by combinations of **categorical** feature values. These subsets are called voxels; they are not an arbitrary regular grid over all continuous variables.
2. Assign test points to their categorical voxel. Unsupported categorical combinations go into a residual voxel.
3. Reject adequacy if more than **5%** of test points occupy the residual voxel. Otherwise compare voxel-frequency distributions through a **two-sample chi-square test**, using **0.05** as the rejection threshold. Nonrejection is a compatibility check, not proof of equal distributions.
4. Within each represented voxel, compute a test point's distance to its nearest training point. Compare it with the voxel's training nearest-neighbor-distance reference distribution.
5. Use its **2.5th and 97.5th percentiles** as bounds: distances between them are valid; larger distances flag isolated/poorly supported points; smaller distances flag excessive train/test proximity.
6. The split passes the stated criterion if at least **95%** of test points are valid. Underrepresented voxels feed the augmentation loop.

Figure 3 illustrates the three proximity categories with 100 training points per depicted 2D example; Figure 4 shows similar train/test proportions across about 800 voxels and reports more than 95% valid test points. The paper does not provide an exact valid fraction or chi-square statistic for that illustration.

The source calls the excessively close category “p-hacking”; here that means its proximity flag, **not evidence of deliberate statistical manipulation**. The text's phrase “shortest distance between all pairs” is imprecise; the Figure 3 caption and nearest-neighbor illustration identify the intended shortest-distance reference. Distance metric, sparse-voxel handling, exact-boundary ties and implementation complexity are not fully specified.

### 4. Architecture, loss, and training-duration choices — node 3

*Evidence: [Paper, §4.3, pp. 6–8; Fig. 5].*

The pipeline aligns architecture with input structure: feedforward/MLP models for generic tabular prediction; convolutional layers when spatial organization is useful; recurrent/reservoir/echo-state approaches for temporal dependence; graph neural networks for relational inputs. For fuselage loads, frame/stringer geometry motivates potentially exploiting spatial structure, but the article does not disclose a complete implemented network diagram, layer widths/depth, parameter count or a definitive convolutional configuration.

The industrial discussion starts with **MSE plus L2 regularization**, then considers output-dependence and safety-aware refinements. Bias–variance reasoning uses training/test errors to diagnose underfitting versus overfitting. Number of layers/neurons, regularization and epochs are tuning choices. Error-versus-epoch inspection selects a stable low-error region before overfitting; it is a methodological recommendation, not a reported early-stopping experiment with documented patience or epoch counts.

### 5. Pointwise performance and safety-relevant residual signs — node 4

*Evidence: [Paper, §4.4, p. 8; Eq. (8); Fig. 6].*

Define the signed residual as

\[
\mathbf e(i)=\mathbf Y(i)-\widetilde{\mathbf Y}(i).
\]

MSE/MAE measure discrepancy magnitude; signed mean residual can cancel large errors. A zero mean establishes neither zero error nor equal numbers of over/underpredictions. The paper also uses per-output **R²/coefficient of determination** and prediction-versus-truth scatterplots.

For this application:

- **Positive residual:** predicted reserve factor is too small; the model overstates failure concern, giving a conservative prediction.
- **Negative residual:** predicted reserve factor is too large; failure concern is understated, making the error safety-relevant.

Figure 6 reports **R²=0.999** for an illustrated failure-mode output over approximately a million test points. Residual spread increases at larger reserve factors. The result demonstrates strong aggregate fit, **not absence of dangerous tail errors, simultaneous accuracy of all six outputs, or certification**.

### 6. Marginal residual distributions, outliers, and bootstrap quantiles — node 5

*Evidence: [Paper, §4.5, pp. 8–10; Figs. 7–8; Eq. (9)].*

The empirical marginal distribution `P(e)` reveals heterogeneity hidden by averages. The paper compares **Gaussian, Cauchy and Laplace** fits through **Kolmogorov–Smirnov (KS)** and **Anderson–Darling (AD)** tests; AD emphasizes tails more strongly.

- All three full-range fits are reported inadequate, **p<0.001**.
- Laplace visually describes the central region well, but Gaussian/Laplace underestimate extreme residuals across the full range.
- Cauchy overestimates tails and would yield unnecessarily broad intervals.
- A four-parameter **Johnson SU** fit is reported to pass a KS test in this example; no fitted parameters or exact acceptance p-value are given.

Log-density plots expose rare negative errors that are especially undesirable for reserve-factor risk interpretation. The source discusses a tail-count outlier heuristic, comparing `N·P(e≥e_x)` with one, and proposes transforming residuals before **generalized Extreme Studentized Deviate (gESD)** testing. The exact Johnson normalization printed in Eq. (9) is problematic; its role is recorded without adopting it as a validated implementation formula (see limitations).

**Nonparametric bootstrap procedure:** repeatedly draw `N` observations with replacement, recompute a statistic such as a residual percentile, and use the resampled-statistic distribution to estimate its confidence interval. This is uncertainty in the estimated statistic, distinct from the prediction interval derived from residual quantiles.

The paper's numerical example gives:

| Statistic | Empirical estimate | Reported bootstrap endpoints, reordered low-to-high | Authors' rounded midpoint-based offset |
|---|---:|---|---:|
| 5th residual percentile | −0.0432 | [−0.0548, −0.0353] | −0.045 |
| 95th residual percentile | 0.0448 | [0.0379, 0.0586] | 0.048 |

This yields the illustrated interval **[ŷ−0.045, ŷ+0.048]**, intended for **90%** prediction coverage. It is separate from the later **95%** uncertainty-model validation. The paper labels midpoint estimates more accurate, but does not independently establish that improvement or a finite-sample coverage guarantee. It also overgeneralizes Gaussian convergence of arbitrary bootstrap statistics; the extraction does not treat that sentence as an unconditional theorem.

### 7. Conditional residuals in input space — node 6

*Evidence: [Paper, §4.6, pp. 10–11; Figs. 9–12].*

Estimate interpretable portions of `P(e|X)` rather than conditioning exhaustively on every feature combination:

- For categorical features, group residuals by category and inspect boxplots. **ANOVA** examines differences in means and **Levene's test** differences in variance. In the stringer example, both reject their null hypotheses with **p<0.005**; Str19, Str06, Str19p and Str06p have conspicuously larger dispersion.
- For continuous features, **Pearson correlation** tests linear association and **Spearman correlation** monotonic association. Binning plus ANOVA/Levene can detect localized or nonmonotonic structure missed by one global trend.
- For the illustrated load, the linear trend has **p=0.59**, but binned residual means differ with **ANOVA p=0.01**. Lack of a linear trend therefore does not establish homogeneous errors.
- Joint frame/stringer conditioning generates a color-coded map of the failure mode with greatest relative error for each location. This is Figure 12's tabular heatmap, not a table of exact numeric losses.

These diagnostics inform uncertainty calibration, targeted data acquisition, physics-expert review and model/loss refinement. They do not prove that every high-error region is caused by a physical discontinuity; inadequate sampling and nonlinear response are discussed explanations. The number of feature subsets grows exponentially, motivating expert judgment or XAI prioritization rather than exhaustive reconstruction.

### 8. Conditional residuals in output space — node 7

*Evidence: [Paper, §4.7, pp. 11–12; Fig. 13].*

Residuals are also conditioned on output magnitude. Accuracy at small reserve factors is especially consequential; larger residual variability at larger predicted values establishes **heteroscedasticity** in the illustration.

Figure 13 bins predicted output into **ten bins** and compares Gaussian, Laplace, Cauchy and Johnson SU residual fits through one-sample KS tests at **0.05**. The text describes Gaussian compatibility only over the limited region **y<2.25**; Johnson SU covers a broader region but not the largest-output bins. The local fit comparisons distinguish a globally attractive distribution from one suitable across all operating regimes.

The prose alternates conditioning on true `y` and predicted `ŷ`; Figure 13's axis is predicted output, and deployable output-conditioned intervals need an available predicted value. This distinction is preserved rather than presenting the two conditioning operations as identical. The tests' fitting/parameter-estimation calibration is not documented sufficiently to reproduce exact p-values.

### 9. Explainability and permutation feature importance — node 8

*Evidence: [Paper, §4.8, pp. 12–13; Fig. 14].*

The paper distinguishes transparency of parameter/prediction generation, human interpretability and quantifiable explanation. Its substantive implemented-style procedure is **permutation feature importance (PFI)**:

1. Retain an unmodified held-out set and its baseline MSE.
2. Shuffle one input feature across samples while keeping the rest fixed; the shuffled feature's marginal distribution is preserved.
3. Evaluate the trained model on the perturbed set.
4. Rank features by **ΔMSEℓ=MSE[ℓ]−MSEbaseline** and compare the ranking with engineering expectations.

Figure 14 illustrates 22 inputs with three clearly dominant features. Physical identities and exact tabulated importance values are not supplied; no feature names or numerical effects are invented. PFI guides which inputs deserve conditional error analysis and may support feature removal. SHAP/LIME are mentioned alternatives, not analyzed procedures or reported experiments.

The text claims every shuffled MSE must increase; this is not a general mathematical guarantee. The extraction preserves the measured-score procedure without imposing that inequality universally. Correlation/dependence between inputs and the difference between predictive reliance and causal effect remain relevant interpretation limits; the paper does not perform a causal identification study.

### 10. Iterative model/data improvement and applicability — node 9

*Evidence: [Paper, §4.9, pp. 13–15; Figs. 15–16].*

**Diagnostic feedback:** large similar train/test errors motivate increased capacity or weaker regularization; a large train/test gap motivates stronger regularization, lower capacity, fewer features or revised architecture. These are practical heuristics, not proofs that a particular intervention will succeed.

**Learning curves** vary training-set size while holding the test set fixed. The four schematic cases distinguish a persistent high-variance gap, high-bias plateau, test error still improving with added data, and both errors converging to a low plateau. This is a data-acquisition diagnostic, distinct from error-versus-epoch monitoring.

**Dataset augmentation:** obtain additional simulation/experimental points if possible, or use the uncertainty-based sampling procedure in underrepresented voxels. VAE/GAN augmentation is mentioned but explicitly not developed. “Boosting” here means iterative improvement, not a documented AdaBoost/gradient-boosted-tree ensemble.

**Feature selection:** PCA, negligible permutation effect and near-zero outgoing weights from input nodes under L1 regularization provide three proposed routes. Sparse parameters alone are not evidence of an implemented group-sparse selector or a new accuracy result.

**Applicability domain** `A_X⊂S_X` separates representable inputs from those eligible for model use:

- **Hypercube/range layer:** every continuous input must lie inside training coordinate ranges. It is cheap but can admit poorly supported combinations.
- **Convex-hull layer:** require membership in the training-input hull; tighter geometrically, computationally expensive, and not by itself an accuracy certificate. PCA/nonlinear latent-space hulls are discussed alternatives.
- **Error-based classifier layer:** train a predictor of whether error exceeds tolerance, recasting rare large-error events as imbalanced classification/anomaly detection. This is a proposed guard, not a fully specified tested classifier.

**Safety-weighted loss:** replace absolute error with absolute relative error, effectively averaging `|(ŷ−y)/y|`, to emphasize small true reserve factors. Since §3 includes `y=0` in the stated range, the paper leaves zero/near-zero denominator handling unresolved; no epsilon-clipping implementation is inferred.

**Correlation-preserving regularization:** add

\[
\gamma\,\|C(\mathbf Y)-C(\widetilde{\mathbf Y})\|_F,
\]

where `C` contains inter-output Pearson correlations over training samples. Figure 16 supplies the ground-truth matrix, including **0.79** for forced crippling/column buckling and **0.81** for column buckling/pure compression. This encourages matching dependence among failure-mode reserve factors. It does not guarantee accurate marginal predictions or define a PDE-residual PINN. PINNs are explicitly a further topic not developed here; no ablation quantifies the penalty's benefit.

**Concept drift:** the paper identifies the need to monitor evolving industrial databases and performance; it provides no specific drift detector, alert threshold or drift experiment.

### 11. Calibrated multiscale prediction intervals — node 10

*Evidence: [Paper, §4.10, p. 15; Eq. (10); Fig. 17, p. 16].*

The uncertainty stage explicitly separates **training**, **calibration** and **validation** data. Train the ANN, estimate residual distributions/quantiles on calibration data, then measure prediction-interval coverage on independent validation data. Percentile uncertainty is assessed through bootstrap confidence intervals; conservative endpoint choices are discussed.

For signed residual `e=y−ŷ`, a sign-consistent expression of a residual-quantile interval is **[ŷ+q_low, ŷ+q_high]**. If written as `[ŷ−ε₁,ŷ+ε₂]`, its lower width is `ε₁=−q_low`. This is an explicit notation clarification, not a new experiment: §4.10 describes the lower width as the lower residual percentile without resolving that sign.

The three scales are:

- **GUM:** a global uncertainty model from marginal `P(e)`.
- **oMUM:** an output-conditioned model; Figure 17B uses predicted output.
- **iMUM:** an input-conditioned model; Figure 17C illustrates conditioning on one load. One interval per input variable yields `n` iMUMs, not a demonstrated full joint high-dimensional conditional model.

For each output, the proposed combination is

\[
\mathrm{FUM}=\mathrm{GUM}\cap\mathrm{oMUM}\cap
\left(\bigcap_{j=1}^n\mathrm{iMUM}[j]\right),
\]

with GUM∩oMUM mentioned as a simpler alternative. This faithfully records Eq. (10), **not an endorsed guarantee of conservative coverage**. Intersections are narrower than their constituent intervals and can have lower coverage; the combined interval requires its own validation. Figure 17 reports the three illustrated components, not a numerical validation of the full intersection or simultaneous coverage across all six outputs.

Reported validation coverage is around **95%**, with bootstrap CI95:

| Model illustrated | Figure | Bootstrap CI95 of coverage |
|---|---|---|
| GUM | 17A | [94.63%, 95.44%] |
| oMUM | 17B | [94.77%, 95.56%] |
| iMUM for one load | 17C | [94.68%, 95.09%] |

The output-conditioned interval adapts width to the observed heteroscedastic pattern, while input conditioning varies bounds with load. All intervals include nominal 95% in the reported coverage confidence range. This supports approximate **empirical marginal calibration for the illustrated settings**, not exact distribution-free conditional coverage or a certified safety level. The paper's criteria “coverage≥95%” and “95% lies within its CI” are not mathematically identical; the figures substantiate the latter/around-95% statement.

## Main findings and technical interpretation

- The ten-node graph makes validation a connected process with refinement loops rather than a single fit score; its worked split audit passes the stated >95% valid-point criterion.
- **R²=0.999** coexists with heterogeneous and extreme residuals. Excellent aggregate regression fit alone is inadequate for safety-sensitive reserve-factor assessment.
- Gaussian/Laplace central fits can miss dangerous tails; Cauchy can be excessively pessimistic. Johnson SU improves the illustrated residual fit, but output-conditioned analysis still exposes regions where it fails.
- Significant categorical mean/variance differences and a load with nonsignificant linear trend but significant binned means show why input-conditioned diagnostics add information.
- PFI supplies a tractable ordering for engineering review and targeted conditional analysis; it is not a substitute for physical interpretation.
- Global and local residual-based intervals show approximately nominal 95% validation coverage, while local intervals express heteroscedasticity more specifically.

These are published collective findings. The paper does not demonstrate a universally optimal architecture, universal calibration guarantee, achieved regulatory approval or comparative speedup over structural simulation. [Paper, §§4–5; Figs. 3–17.]

## Assumptions, source ambiguities, and reproducibility limits

### Stated scope and evidence gaps

- Validation is predominantly **frequentist** and tailored to supervised models. Bayesian methods and extension to reinforcement/collective learning are future work. High-dimensional conditioning/hull computation are acknowledged limitations. [§§4.2, 4.6, 5.]
- Input/output uncertainty sampling starts with an independence assumption unless covariance information is available. Adequate data coverage and useful residual calibration depend on the operating domain; data augmentation does not necessarily create new physical coverage. [§§4.1, 4.9.]
- The industrial data cannot be shared. No code link, programming language, ML framework, library, software version, hardware configuration, random seed, bootstrap repetition count or complete model/hyperparameter specification is given. Exact reproducibility and implementation attribution cannot be established from this source. [Entire paper; data availability, p. 16.]
- Network-type alternatives, SHAP/LIME, VAE/GAN augmentation, PINNs and concept-drift monitoring vary in depth; they must not be promoted to implemented techniques or additional experiments. Exact feature identities and the 26-versus-22 distinction remain unspecified.

### Material mathematical/notation cautions found during validation

1. **Eq. (9), p. 9:** visual inspection confirms the printed expression `z=γ+sinh((x−ξ)/λ)∼N(0,1)` after defining a four-parameter Johnson SU family including δ. The displayed transform contains no δ and is not established as a valid general normalization by the surrounding text. The profile records the proposed transform/gESD idea, but does not silently substitute a formula from outside literature. This source-level issue does not block the rest of the analysis.
2. **§4.10, Eq. (10), p. 15:** calling an intersection the most conservative interval conflicts with set containment/coverage logic. The equation is documented as a proposal; no unreported combined-coverage result is invented.
3. **§4.10 lower-quantile sign:** the signed-residual definition and interval-width notation require the clarification given above. The earlier 90% example supplies consistent negative/positive offsets; it is not the later 95% example.
4. **§4.5 bootstrap wording:** arbitrary bootstrap statistics do not unconditionally become Gaussian, and midpoint-of-endpoints estimation is not automatically more accurate. Printed numerical endpoint order is reversed and is explicitly reordered in this profile.
5. **§4.8 PFI:** a nonnegative loss increase is not guaranteed for every shuffle. The empirical comparison is retained without asserting the universal inequality.
6. **§4.10/Fig. 17:** text/caption sometimes refer to true reserve factors while axes/conditional notation use predicted reserve factor. The operational distinction is made explicit; precise binning/calibration settings remain undisclosed.
7. **§4.9 relative loss and correlation penalty:** zero denominators are not specified; matching correlations does not alone ensure that other outputs become accurate. These refinements are not treated as mathematically proved safety guarantees.

These cautions preserve source fidelity and prevent downstream overclaims. They do not trigger repository forensics or expand this task beyond the paper.

## Computational tools and technical knowledge represented

**Explicit software evidence:** the paper attributes Software contributions, but names **no programming language, package or ML library**. Python, NumPy, SciPy, pandas, scikit-learn, PyTorch, TensorFlow, MATLAB, plotting libraries and particular solver products must therefore not be attached to this publication on the basis of its PDF alone. Adam/ReLU/PCA are named algorithms or mathematical components, not proof of a software stack.

The substantive knowledge represented by the paper includes:

- Multi-output supervised regression, feedforward neural parameterization, loss/regularization design, backpropagation and stochastic optimization concepts.
- Design of experiments, space filling, uncertainty-aware augmentation, geometric/categorical encoding, train-only preprocessing and PCA.
- Train/test distribution assessment, categorical tessellation, nearest-neighbor geometry, convex-hull applicability and leakage/near-duplicate risk.
- Statistical inference for residual distributions, non-Gaussian tails, goodness-of-fit, outlier procedures and bootstrap quantile/coverage estimation.
- Conditional error analysis, heteroscedasticity, ANOVA/Levene/Pearson/Spearman diagnostics and interpretable engineering visualizations.
- Permutation explanations, learning curves, bias–variance diagnostics, feature selection and iterative data/model refinement.
- Applicability guards and calibrated global/input-/output-conditioned prediction intervals, with clear distinctions between point accuracy, statistical uncertainty and safety claims.
- Fuselage structural-design context, loads/geometric indexing, strength/buckling failure modes and safety-asymmetric reserve-factor errors.

## Relevant thematic categories

- Statistics, uncertainty quantification, and statistical validation.
- Machine learning and data science.
- Optimization and numerical/computational methods.
- Aerospace engineering and structural design.
- Explainable AI, model assurance, and applicability-domain assessment.

The work also connects technically to quantitative-risk concerns through tail modeling and asymmetric errors, but does not constitute an insurance/actuarial experiment. Its control/robotics connection is the transferable validation of learned surrogates, not an implemented GNC or robot controller. These are thematic connections, not new source claims or thematic synthesis files.

## Complete-paper coverage and validation record

The full 17-page text, all ten numbered equations and all 17 figures were inspected; references/end matter were read for publication, attribution and availability, not used to attribute entire cited works to this project. Layout-preserving text extraction was complemented by rendered figure pages 4, 6–16, the mathematical page 3 and a high-resolution Eq. (9) crop. No mathematical content was reconstructed from presumed implementation knowledge.

| Paper material | Profile coverage / validation purpose |
|---|---|
| §1, pp. 1–2 | Motivation, certification boundary and Airbus–UPM context |
| §2, pp. 2–3; Eqs. (1)–(6) | Data/model parameterization, losses, regularization and training |
| §3, pp. 3–4 | All six failure modes, input/output dimensions and engineering scope |
| §4.1; Figs. 1–2 | Ten-node architecture, feedback, geometry and preprocessing |
| §4.2; Eq. (7), Definition 1; Figs. 3–4 | Hull discussion, full VTPM sequence, thresholds and split illustration |
| §4.3; Fig. 5 | Architecture/training choices; schematic versus measured evidence |
| §4.4; Eq. (8); Fig. 6 | Error metrics, sign semantics, reported R² and test volume |
| §4.5; Eq. (9); Figs. 7–8 | All fit families, tail behavior, bootstrap example and formula caution |
| §4.6; Figs. 9–12 | Categorical/continuous/joint conditioning; artificial example distinguished |
| §4.7; Fig. 13 | Ten-bin conditional fits and predicted-output dependence |
| §4.8; Fig. 14 | PFI procedure, 22-feature illustration and interpretation boundary |
| §4.9; Figs. 15–16 | Learning/refinement alternatives, applicability layers, relative loss and correlation regularization |
| §4.10; Eq. (10); Fig. 17 | Train/calibrate/validate separation, all interval scales, all reported coverage ranges and aggregation caution |
| §5, p. 15 | Frequentist scope, future Bayesian/other-paradigm extensions |
| p. 16 end matter; pp. 16–17 references | Explicit user CRediT roles, collaboration/funding context, disclosure/data restrictions and bibliography |

The source has no independent numbered results tables; Figures 12 and 16 carry tabular/heatmap information and are included above. No additional experiment was inferred to fill an absent detail. The source hash matches the inventory. Extracted text and rendered evidence are regenerable under `.cache/scientific_paper/`; the stable citation remains the original PDF.
