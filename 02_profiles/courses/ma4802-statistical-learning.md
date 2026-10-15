# Statistical Learning (MA4802)

## Module metadata

| Field | Value |
|---|---|
| Official title | Statistical Learning |
| Module code | MA4802 |
| ECTS | 6 |
| Grade | 3.0 |
| Transcript section | Degree modules, p. 3 |
| Teaching term | Summer semester 2024 |
| Profile status | complete_validated |

## Evidence base and material structure

The exact transcript match is `00_sources/tum/archives/Statistical Lea 950732556 (S24)_20261012_1548.zip`; its export index identifies Statistical Learning [MA4802]. Fabian J. Theis's 115-page **Statistical Learning Script** is the syllabus backbone. It contains introductory statistical decision theory, supervised learning, unsupervised learning, graphical models, and causal inference. Supplemental decks by Theis, Tingying Peng, and Vincent Fortuin extend the backbone with double descent, transformers, and deep generative representation learning.

The 46 outer archive members include 28 PDFs totaling 731 physical pages: the script (115), eight lecture decks (550), a double-descent presentation (11), ten exercise sheets (22), and eight PDF solutions (33). Nine `.json` files are Jupyter notebooks rather than miscellaneous JSON data. `Solution Exercise 2.imscc` is a ZIP containing another notebook and a three-page solution PDF, plus macOS resource files. Thus the inspected evidence includes ten notebooks and 734 PDF pages when the nested solution is included. Four CSV datasets accompany the exercises. `Polynomial Fit Data.dmg` is actually a pickle stream, established by static opcode inspection without deserialization.

Text was extracted from all PDFs with `pdftotext -layout`, retaining page boundaries. The script supplies readable prose and most formulas; imported textbook figures create interleaved text, and Lecture 2 and Lecture 6 lose substantial title/prose glyphs. Their mathematical syllabus is corroborated by the script and exercises. Visual inspection checked early decision theory, Newton/IRLS, boosting bounds, SVM geometry, transformer architectures, double-descent plots, ELBO derivations, and flow/BiGAN diagrams. Progressive slide builds were grouped by repeated headings and checked at their completed states. Source references below use **one-based physical PDF pages**, not printed slide numbers. The script's numbered body page is normally physical PDF page minus two.

All ten available exercise sheets (1–7 and 9–11), their available solutions, and all ten notebooks were inspected, with code read statically. No course code was run. Local sources are sufficient to establish the content; no external module description was needed. Limitations and contradictory source statements are recorded below.

## Technical content

### Statistical decision theory and generalization

*Evidence: [S], §§2.1–2.7, PDF pp. 3–12; [E1–E3]; [D], pp. 2–11.*

- Supervised regression and classification versus unsupervised density, cluster, and representation learning. Joint distributions `P(X,Y)`, conditional predictions, i.i.d. training samples, probabilistic predictions, and maximum a posteriori class decisions provide the common framework.
- Expected prediction error as expected loss. Pointwise minimization yields the conditional mean for squared loss, conditional median for absolute loss, and Bayes classifier `argmax_c P(Y=c|X=x)` for zero–one loss. Exercises compare theoretical Gaussian-classification risk with finite-sample empirical error and derive Bayes boundaries for mixtures of Gaussian class densities.
- Parametric versus nonparametric models. Ordinary linear regression is a global linear approximation; k-nearest neighbors uses locally constant predictions through neighborhood averaging or majority vote. The notes state kNN consistency under mild regularity with `N,k → ∞` and `k/N → 0`, without developing those regularity assumptions further.
- Bias–variance–irreducible-noise decomposition of prediction error; the distinction between estimating the noiseless regression function and predicting a noisy response. Exercises express least-squares and kNN predictions as weighted sums of responses and derive conditional/unconditional bias and variance.
- Curse of dimensionality: neighborhoods containing a fixed probability mass occupy increasingly large coordinate ranges in a high-dimensional cube. Gaussian random-vector experiments illustrate near-orthogonality as dimension increases. Polynomial-degree and training-size experiments connect model complexity to train/test error.
- No-free-lunch principle: no predictor is uniformly best independently of assumptions on the data-generating domain.
- The double-descent supplement distinguishes underparameterized and interpolating/overparameterized regimes, the interpolation threshold, and model-size versus training-epoch effects. Polynomial fits, MNIST MLPs, and CIFAR-10 ResNets illustrate nonmonotone test-risk curves. The plotted decomposition shows variance peaking near interpolation; this is presented as behavior of particular models, not as a universal performance theorem. Later slides give research outlooks on overparameterized loss landscapes and alternative complexity measures rather than full derivations.

### Linear inference, shrinkage, and sparse high-dimensional regression

*Evidence: [S], §§3.1–3.4, PDF pp. 13–27; [E3–E5], including notebook cells for regression paths and coordinate descent.*

- Gaussian linear model `y=Xβ+ε`, least-squares normal equations, Gaussian maximum likelihood, and residual variance estimation with degrees-of-freedom correction. Covariance `σ²(XᵀX)⁻¹` and Student-t coefficient tests are derived in the full-column-rank setting. The **Gauss–Markov theorem** establishes minimum covariance among linear unbiased estimators; biased shrinkage can nevertheless improve mean-squared error.
- Ridge regression minimizes squared residuals plus an `ℓ₂` penalty; with centered predictors and the intercept handled separately, `β̂=(XᵀX+λI)⁻¹Xᵀy`. Positive regularization stabilizes ill-conditioned or rank-deficient normal equations and trades bias for variance. Exercises show the effect of centering on the intercept and generalize ridge to **Tikhonov regularization** with a symmetric quadratic penalty `λβᵀQβ`, assuming the resulting normal matrix is invertible.
- SVD analysis of ridge: fitted responses are shrunk along left-singular-vector directions by `d_j²/(d_j²+λ)`, with stronger shrinkage for smaller singular values. The hat matrix `H_λ=X(XᵀX+λI)⁻¹Xᵀ` defines effective degrees of freedom `tr(H_λ)=Σ_j d_j²/(d_j²+λ)`.
- Gaussian parameter priors interpret ridge as MAP estimation. Under the script's Gaussian prior scaling, the posterior mean is the ridge estimate and posterior covariance is `σ²(XᵀX+λI)⁻¹`. The notes contrast this distributional treatment of uncertainty with point estimation and briefly identify robust-regression likelihood alternatives such as Laplace or Student noise.
- **Lasso**: constrained `ℓ₁` estimation, equivalent penalized least squares, sparse coefficients, nondifferentiability, subgradients of absolute value, and zero-containing subdifferential optimality. Coordinate descent computes partial residual correlations and applies soft thresholding. For the script's unscaled squared-loss objective, its coordinate update uses threshold `λ/2`; other tables and library objectives use different normalizations. A supplied notebook implements residual-updating coordinate sweeps, in addition to scikit-learn fits.
- Geometric comparison of ridge's smooth constraint ball with Lasso's corners and faces; proportional shrinkage versus thresholding; Laplace priors and posterior-mode interpretation. Rank deficiency can produce nonunique coefficient solutions, so sparsity and selection behavior require care.
- Additional sparse-estimation concepts: regularization paths and the named **LARS** approach; compressed sensing as an application area; **Dantzig selector** with an `ℓ∞` bound on residual–predictor correlations; **group Lasso** with group-size-weighted Euclidean penalties for selecting predefined groups, illustrated by genes in biological pathways. These are supplements rather than implemented algorithms in the archive.
- **Elastic net** combines squared `ℓ₂` and `ℓ₁` penalties to retain sparse selection while grouping correlated predictors. An exercise converts elastic-net estimation into a Lasso problem by augmenting the design matrix and response. The script weights `ℓ₂` by `α`, whereas the exercise/library `l1_ratio` convention weights `ℓ₁`; these parameters must not be equated.

### Model selection, validation, and statistical comparison

*Evidence: [S], §3.5, PDF pp. 28–30; [E2–E7], particularly Sheet 7, pp. 1–2, and its notebook.*

- Hold-out estimation, repeated random train/test splits, K-fold and leave-one-out cross-validation. K-fold tuning fits each candidate regularization strength on complementary folds, aggregates validation error, then refits the selected model on all training data.
- Separate training, validation, and final test sets prevent hyperparameter selection from contaminating final evaluation. Exercises standardize features and compare models across regularization paths; supplied notebooks demonstrate fitting a scaler on training data and transforming held-out data with those statistics.
- AIC/BIC as likelihood–complexity trade-offs using effective degrees of freedom; for Lasso, the active coefficient count is used as a complexity measure. The notes discuss asymptotic/model-correctness assumptions and limitations in poorly conditioned high-dimensional settings. Their exact penalty normalization is not used here as an independent formula reference.
- Likelihood-ratio testing of nested logistic models using the difference in log-likelihoods, with an asymptotic chi-square reference distribution and degrees of freedom equal to the number of added parameters. The heart-disease exercise compares intercept-only and single-feature models, performs forward selection by test p-value, and contrasts this with `ℓ₁` selection.
- Accuracy, mean-squared/prediction error, ROC curves and AUC, and training-versus-test performance as evaluation concepts. Forest exercises explore depth, feature subsampling, and bootstrap sample size. These are teaching experiments, not evidence of personal project results.

### Generative and discriminative classification

*Evidence: [S], §§4.1–4.3, PDF pp. 31–41; [L6], particularly PDF pp. 44–55; [E5–E7].*

- Generative classifiers model class priors and class-conditional feature densities; discriminative classifiers model `P(Y|X)` directly. Indicator-response least squares extends linear regression to classification but can mask intermediate classes in multiclass problems.
- Gaussian discriminant analysis: MLE of class means, priors, and covariances; **QDA** with class-specific covariance and quadratic decision boundaries; **LDA** with pooled covariance and linear boundaries. Whitening gives a nearest-class-mean interpretation of LDA, adjusted for priors.
- Covariance estimation under limited samples, diagonal Gaussian/naive Bayes assumptions, diagonal LDA, shrinkage between class-specific and pooled covariance, and shrinkage toward isotropic covariance. The notes connect covariance priors to inverse-Wishart regularization and introduce projection before classification.
- Nonlinear generative extensions include Gaussian-mixture class densities and kernel density estimation. Exercises compare GMM density fitting with a Gaussian-kernel density estimator; the archive does not develop a general RKHS theory.
- Binary logistic regression uses Bernoulli probabilities with a sigmoid of a linear predictor, giving linear log-odds and a linear threshold boundary. Cross-entropy/negative log-likelihood has gradient `Xᵀ(μ−y)` and Hessian `XᵀSX`, where `S=diag(μ_i(1−μ_i))`. The Hessian is positive semidefinite and is positive definite when the design has full column rank at finite parameters. Complete separation can prevent a finite unregularized MLE despite convexity; the notes discuss regularization for this case.
- Numerical fitting: gradient descent; steepest descent under a positive-definite quadratic metric; exact and backtracking line searches with sufficient decrease; diminishing learning rates; objective/parameter-change stopping criteria; Newton steps from a local quadratic model; trust-region/Hessian-regularization safeguards and quasi-Newton methods as extensions.
- The optimization discussion contrasts local quadratic convergence of Newton with linear convergence of steepest descent in their regular convergence settings; it does not supply a complete assumptions-and-rate theorem. Positive-definite curvature is needed for the stated Newton direction to minimize the local quadratic model. The backtracking discussion explains finite termination for a descent direction by sufficiently small steps satisfying the decrease condition.
- **Iteratively reweighted least squares (IRLS)** is derived from Newton's method: weighted normal equations use working response `z_k=Xβ_k+S_k⁻¹(y−μ_k)`. The changing weights distinguish this from one ordinary least-squares solve.
- `ℓ₁`, `ℓ₂`, and elastic-net logistic penalties; multinomial logistic regression via softmax and a reference class for identifiability. Computational exercises compare LDA, QDA, and logistic regression on simulated Gaussians and the wine dataset, including one-versus-rest classification.

### Trees, random forests, boosting, and margin methods

*Evidence: [S], §§4.4–4.8, PDF pp. 41–51; [B], PDF pp. 6–65; [E7–E9], including Notebook 8 and the proof in `Solution Exercise 7.pdf`, p. 3.*

- **CART** partitions feature space by recursive axis-aligned binary splits. Regression leaves use response averages; classification leaves use class frequencies/majority labels. Greedy split selection minimizes within-region squared error or uses misclassification, entropy, and Gini impurity. Tree depth, pruning, and cross-validation control complexity; XOR illustrates limitations of immediate-improvement stopping rules.
- **Bagging** averages predictions or takes majority votes over bootstrap-trained learners to reduce variance. **Random forests** additionally sample candidate features at each split to decorrelate trees. Out-of-bag predictions use only trees whose bootstrap samples omitted the observation and provide an internal error estimate.
- **AdaBoost** builds an additive score from sequential weak learners, commonly decision stumps. It minimizes exponential loss, a surrogate for classification error; weighted misclassification determines the next learner. The learner coefficient is `α_t=(1/2)log((1−ε_t)/ε_t)`, and sample weights are multiplied by `exp(−α_t y_i h_t(x_i))` and renormalized.
- The derivation connects the sample weights to cumulative exponential loss, derives the coefficient by minimizing that loss, and interprets the population optimum as half the log-odds. Early stopping controls the number of learners. Bagging/forest versus boosting comparisons distinguish resampling and parallel training from sequential reweighting.
- The exercise solution bounds empirical training classification error by `∏_t 2√(ε_t(1−ε_t))`. The completed lecture slide gives the consistent edge-based bound `exp(−2Σ_t γ_t²)` for `γ_t=1/2−ε_t`, hence `exp(−2Tγ²)` when every edge is at least `γ>0`. This concerns training error, not a generalization guarantee. The same slide's first product formula omits the factor 2 and is not adopted.
- **Support vector machines**: affine separating hyperplanes, signed distance, support vectors, maximum margin, and the convex hard-margin program minimizing `||β||²/2` subject to `y_i(βᵀx_i+β₀)≥1`. Hinge loss extends the formulation to nonseparable data through a soft margin.
- A supplemental slide introduces the kernel trick geometrically as nonlinear feature mapping followed by linear separation. This establishes introductory kernel-SVM coverage, but not particular kernels, a detailed dual derivation, or reproducing-kernel Hilbert-space theory.
- Applications include interpretable medical decision rules, genetic-fingerprint population classification, ROC evaluation, and a lecture example of the Viola–Jones boosted cascade for object detection.

### Perceptrons, multilayer networks, and convolutional learning

*Evidence: [S], §§4.9–4.11, PDF pp. 51–77; [N], PDF pp. 8–130; [E9], all pages and its solution.*

- **Rosenblatt perceptron** updates weights and the intercept for misclassified examples, interpreted through signed hyperplane distances and stochastic gradient steps on a piecewise-linear criterion. For a linearly separable finite dataset, the perceptron convergence theorem guarantees a separator after finitely many updates. Sheet 9 proves this using normalized augmented observations and decreasing squared distance to a suitably scaled separating vector. Nonseparability prevents that conclusion; initialization changes which separator is found.
- MLPs compose affine maps with nonlinear activation functions and use regression or class-probability output layers. The notes construct sigmoid combinations approximating smooth functions to illustrate universal approximation; linear activations collapse a multilayer model back to a linear map.
- Gaussian regression likelihood versus cross-entropy classification; nonconvex weight optimization; batch and stochastic gradient descent. **Backpropagation/delta rule** derives local output errors and propagates them through hidden-layer activation derivatives, combining a forward evaluation with reverse derivative accumulation.
- Weight decay, dropout, early stopping/validation monitoring, and the brief use of repeated test-time dropout for uncertainty heuristics. Vanishing gradients and plateaus motivate generative pretraining, ReLU activations, and residual-network architectures. These are discussed techniques, not supplied network-training experiments.
- CNNs exploit locality and spatial weight sharing. The notes derive cross-correlation from a dense image-to-image layer, distinguish it from kernel-flipped mathematical convolution, and extend it to multiple input/output channels.
- Standard convolution has `k_h k_w c_in c_out` weights; **depthwise separable convolution** separates channelwise spatial filtering from `1×1` channel mixing, using `k_h k_w c_in+c_in c_out` weights. The notes compare operation counts and connect this construction to Xception/MobileNet.
- Padding, stride, dilation, receptive fields, pooling/downsampling, and fully connected heads. ReLU versus sigmoid includes vanishing-gradient behavior; leaky ReLU addresses inactive negative-side units. Batch normalization computes minibatch mean/variance, normalizes with a stabilizing epsilon, and learns scale and shift.
- Model interpretation: learned filter visualization, input occlusion, class-score maximization over the input image with fixed weights, input-gradient saliency, class activation maps, and PCA/t-SNE visualization of learned features. Weakly supervised localization and cell-cycle representation are examples; a full t-SNE algorithm derivation is not supplied.
- Multitask learning shares internal representations with task-specific heads; multimodal models combine modality-specific inputs; transfer learning repurposes pretrained features when target-domain labels are limited. Examples emphasize microscopy, genomics, and medical images.

### Transformers and introductory foundation-model applications

*Evidence: [T], PDF pp. 3–16; [I], PDF pp. 47–63.*

- RNN sequence processing and its limitations in parallelization and long-range dependencies motivate transformer encoder/decoder architectures. Diagrammatic coverage includes token embeddings, positional encodings, multi-head self-attention, masked decoder attention, encoder–decoder attention, feed-forward blocks, residual additions, and normalization.
- Translation examples distinguish cross-sequence attention from relationships among tokens in a single sequence. The slides explain the architecture rather than deriving scaled dot-product attention or implementing it.
- **Vision Transformer (ViT)** splits images into patches, linearly embeds patches, adds positional/class embeddings, and applies transformer encoders followed by a classification head. The comparison with CNNs contrasts global token interactions with stacked local convolutions.
- **HistoGPT** illustrates multimodal image-to-report generation: a pretrained histology vision encoder supplies image representations through a resampler and cross-attention to a biomedical language model. The diagram distinguishes frozen pretrained components from trained connecting components.
- The introductory lecture adds contextual examples of GPT pretraining and alignment, language/image foundation models, diffusion-based image generation, and reinforcement learning for games. These are overview/application coverage, not evidence that this course taught detailed RL algorithms or full diffusion mathematics.

### Latent mixture models, EM, and clustering

*Evidence: [S], §§5–5.3, PDF pp. 77–84; [M], PDF pp. 15–59; [E10] and its notebook.*

- Latent-variable generative models distinguish observed and hidden quantities. Mixtures combine component densities using nonnegative weights summing to one. Examples include histograms, multivariate Gaussian mixtures, and mixtures of product-Bernoulli distributions.
- Posterior responsibilities give soft cluster assignments; maximum-responsibility/MAP assignments yield hard labels. The notes discuss assignment uncertainty, limitations of interpreting clusters, density approximation, outlier detection, compression, and nonlinear class-density modeling.
- **Expectation maximization** alternates an E-step computing the expected complete-data log-likelihood `Q(θ,θ_old)` with an M-step maximizing it, optionally adding a log prior for MAP estimation. For GMMs with fixed component count, responsibilities are normalized component likelihoods; mixing weights, means, and covariances are updated from responsibility-weighted counts and moments.
- EM increases the observed-data log-likelihood monotonically under exact updates. The material discusses local maxima and saddle points rather than promising a global optimum. The constraints on mixture weights and covariance matrices motivate using model-specific updates instead of an unconstrained generic optimizer.
- **k-means/Lloyd iteration** follows from hard assignments with equal isotropic covariance and equal mixture weights: assign to the nearest center, then recompute centers as cluster means. The notes give an `O(NKD)` assignment-step cost for `N` observations, `K` centers, and dimension `D`. Hierarchical clustering is introduced as a contrasting similarity-tree approach, without a specific linkage algorithm.
- Computational comparisons fit GMMs and kernel density estimates to Old Faithful waiting times, then compare k-means and GMM clustering on synthetic clusters of unequal sizes/spreads. Elbow curves investigate cluster count.

### Factor analysis, PCA, and independent component analysis

*Evidence: [S], §§6.1–6.3 and 6.6, PDF pp. 84–89 and 99–103; [E11], its solution and notebook; [G], PDF pp. 14–19.*

- **Factor analysis** uses Gaussian latent factors, a linear loading map, and diagonal observation-noise covariance. Marginalization gives mean `Wμ₀+μ` and covariance `WΣ₀Wᵀ+Ψ`. Rotational ambiguity and absorbed latent means/scales motivate normalization, structural assumptions, and non-Gaussian alternatives. Gaussian conditioning provides posterior latent scores; EM is discussed for fitting, including missing-data settings.
- **PCA/Karhunen–Loève transformation** minimizes squared reconstruction error under orthonormal loadings. Theorem 6.6 identifies the leading covariance eigenvectors and projected scores as optimal. Its proof equates reconstruction-error minimization with maximum projected variance, then imposes successive orthogonality constraints for further components.
- SVD of centered data yields principal directions and scores without explicitly forming the feature covariance matrix. Truncated reconstruction provides a least-squares low-rank approximation. Exercises prove the second-component result and compare unsupervised PCA projections with label-informed LDA projections.
- **Probabilistic PCA** specializes factor analysis to isotropic noise. The notes give the loading-matrix likelihood solution from leading covariance eigenpairs, with orthogonal rotational ambiguity, and estimate noise variance from discarded eigenvalues. The zero-noise limit connects to ordinary PCA. Component-count discussion distinguishes monotonically improving reconstruction from likelihood-based model selection on held-out data.
- **ICA/blind source separation** assumes an invertible instantaneous linear mixing `X=AS` of independent sources. Independence is stronger than decorrelation; whitening/PCA preprocessing reduces the remaining transformation search. Source scaling, signs, and order are indeterminate.
- The linear-BSS separability theorem identifies mixing up to scaling/permutation when independent sources have finite covariance and at most one Gaussian/deterministic component under the stated setting. A two-dimensional proof with positive twice-differentiable densities uses vanishing mixed derivatives of log densities to show that nontrivial alternative independent mixing forces Gaussian sources.
- Maximum-likelihood ICA uses `log|det B|+Σ_i log p_i(b_iᵀx)` for unmixing matrix `B`. Unknown source densities make estimation semiparametric; approximate source-density families and score functions enter the local-consistency discussion. The source's score-sign terminology is ambiguous, so its exact consistency inequality is not promoted to a verified standalone theorem here.
- The supplied **FastICA** exercise separates noisy mixed sine, square, and sawtooth signals and compares the recovered sources with PCA. Olivetti faces illustrate factor loadings, reconstructions, and pixelwise noise variance; wine data illustrates PCA versus LDA projections. FastICA is evidenced as a library method, not a fully derived fixed-point iteration in these sources.

### Autoencoders and deep generative representation learning

*Evidence: [S], §§6.4–6.5, PDF pp. 89–99; [G], PDF pp. 3–54, especially 33–46 and 48–52.*

- The manifold hypothesis motivates lower-dimensional representations for downstream prediction, visualization/clustering, imputation, and scientific interpretation. Self-supervised learning predicts one part of an observation from another. Disentanglement is illustrated through latent traversals and discussed in relation to data efficiency, generalization, fairness, and abstract reasoning.
- **Autoencoders** learn an encoder and decoder by reconstruction loss with a bottleneck or other restriction against trivial copying. Linear autoencoders recover the principal subspace without requiring their learned basis vectors to equal orthonormal PCA eigenvectors; the notes connect this with Moore–Penrose pseudoinverses and orthogonal projection.
- Deep-autoencoder training includes greedy restricted-Boltzmann-machine pretraining followed by backpropagation fine-tuning as a historical strategy. **Sparse autoencoders** penalize latent activations, linked to Laplace priors and dictionary learning. **Denoising autoencoders** reconstruct clean inputs from deliberately corrupted observations; image and single-cell RNA-sequence denoising provide examples.
- **Variational autoencoders** use a generative decoder `p_θ(x|z)`, latent prior `p(z)`, and approximate posterior encoder `q_φ(z|x)`. The ELBO is expected reconstruction log-likelihood minus `KL(q_φ(z|x)||p(z))`, and is at most the marginal log-likelihood. The identity `log p(x)=ELBO+KL(q(z|x)||p(z|x))` is explicitly supported by [G], p. 37, resolving the reversed inequality in [S], p. 95.
- Gaussian reparameterization `z=μ_φ(x)+σ_φ(x)⊙ε`, `ε~N(0,I)`, enables gradients through latent sampling; Monte Carlo approximates the reconstruction expectation. **β-VAE** increases the KL weight (`β>1` in the lecture) to encourage disentanglement. The discussion distinguishes posterior uncertainty and sample generation from reconstruction-quality and tractability limitations.
- **Normalizing flows** use exactly invertible maps and the change-of-variables determinant to optimize exact likelihood. The supplement derives `log p(x)=log p(z)−log|det ∂g(z)/∂z|` for `x=g(z)`. **Real NVP** affine coupling leaves one block unchanged and scales/translates the other using functions of the unchanged block; a block-triangular Jacobian makes the determinant tractable. Equal-dimensional latent spaces, invertibility constraints, and determinant computation are discussed as trade-offs. The displayed component indices in one determinant summation are ambiguous; the profile retains the verified structural property.
- **GANs** alternate stochastic discriminator ascent and generator descent using real examples and generated samples. The generator maps noise into data space while the discriminator separates real from generated data. Training instability and the absence of a straightforward inverse encoder limit representation learning; a **BiGAN** diagram adds an inference network and discrimination of paired data/representations.
- GAN applications include synthetic-data augmentation, paired/unpaired image translation, **CycleGAN**, and super-resolution. Diffusion models appear as a teaser/overview, with no developed loss, sampler, or convergence result. Comparisons distinguish exact flow likelihood, variational lower bounds, ordinary autoencoder reconstruction, and adversarial generation.

### Graphical models and causal reasoning

*Evidence: [S], §§7–8, PDF pp. 103–112.*

- Graph vocabulary: parents/children, paths, descendants, skeletons, colliders, v-structures, directed acyclic graphs, and blocked versus active paths. **d-separation** is defined by conditioning behavior along paths, including collider descendants.
- Bayesian networks factor joint densities into node-conditional distributions given parents. Sparse factorization reduces parameter requirements; a binary chain illustrates `2p−1` parameters versus `2^p−1` for an unrestricted joint law. First-order Markov chains exemplify conditional independence of future and past given the present.
- Theorem 7.7 states equivalence of local Markov, global Markov, and DAG factorization properties. Theorem 7.9 characterizes **Markov-equivalent DAGs** by identical skeletons and v-structures. Faithfulness excludes conditional independencies created by cancellation and, with the Markov property, connects graphical separations with statistical conditional independencies.
- Observational association alone generally identifies at most a Markov-equivalence class under the discussed assumptions, even with perfect independence tests and no latent confounders. The notes distinguish causal discovery from estimating effects given a causal structure; they do not supply a full discovery algorithm.
- **Structural equation models** specify `X_j=f_j(Pa_j,N_j)` with jointly independent exogenous noises and an acyclic graph. Topological ordering allows recursive sampling and gives a unique induced joint distribution. Mechanisms are treated as invariant modules rather than arbitrary conditional factors.
- **Interventions/do-operator** replace structural equations; perfect interventions fix a variable and remove its incoming causal influences. A linear Gaussian example distinguishes `P(Y|do(X=a))` from ordinary conditioning and demonstrates directional asymmetry. Absence of a directed path rules out a causal effect, while path cancellation shows that a path alone need not imply a nonzero total effect.
- **Counterfactual inference** updates the exogenous-noise distribution conditional on observations, intervenes in the resulting model, then predicts: abduction, action, prediction. Updated noises need not remain independent. An exam-preparation example and a comparison of SEMs illustrate why observational, interventional, and counterfactual knowledge have successively stronger identification requirements.
- Some graph and independence glyphs are absent even in rendered script pages. Their surrounding definitions and theorem statements remain legible; no detailed unreadable symbolic statement or numerical outcome from the final counterfactual exercise is reconstructed.

## Computational work and tools

- **Python**, NumPy, pandas, SciPy, Matplotlib, and Seaborn; Jupyter notebooks/JupyterLab, conda environments, and Google Colab are explicitly used or recommended. Arrays, broadcasting, distance computation, sorting, class voting, exploratory statistics, density plots, and repeated data splits appear in the first two notebook solutions.
- **scikit-learn**: `LinearRegression`, `Ridge`/`RidgeCV`, `Lasso`/`LassoCV`, `ElasticNet`/`ElasticNetCV`, `StandardScaler`, `KNeighborsClassifier`, `LinearDiscriminantAnalysis`, `QuadraticDiscriminantAnalysis`, `LogisticRegression`, `OneVsRestClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier`, `GaussianMixture`, `KernelDensity`, `KMeans`, `FactorAnalysis`, `PCA`, and `FastICA`. Tree/decision-boundary plots, feature importance, ROC displays, and accuracy metrics accompany model comparisons.
- Manual implementations complement library calls: kNN, data splitting/accuracy, residual-updating Lasso coordinate descent, and log-likelihood/likelihood-ratio computations. SciPy provides distribution functions, kernel-density helpers, and synthetic signal generation.
- **PyTorch** is explicitly assigned through a tutorial in Sheet 9; no PyTorch submission or network code is included. **Keras** appears in lecture code illustrations, rather than as a supplied executable assignment. No framework-based transformer, flow, GAN, or VAE implementation is present.
- Data examples are Iris, prostate clinical measurements, wine chemistry, coronary risk factors, genetic tandem-repeat fingerprints, Old Faithful eruption timing, Olivetti faces, and synthetic Gaussian/signal data. Clinical and biological examples in slides broaden applications to microscopy, cell-cycle/disease progression, genomics, single-cell atlases, and pathology reports. These describe taught use cases, not claimed individual research contributions.

## Thematic categories

- Statistics and data science
- Statistical learning and model selection
- Bayesian and probabilistic modeling
- Convex and numerical optimization
- Sparse estimation and high-dimensional regression
- Classification and ensemble learning
- Neural networks and deep learning
- Representation learning and generative models
- Dimension reduction and signal processing
- Graphical models and causal inference
- Computational biology and medical imaging

## Coverage validation

| Evidence block | Profile coverage and review outcome |
|---|---|
| Script §§1–2 | Learning types, decision theory, kNN, high-dimensional geometry, generalization; introductory applications distinguished from methods taught in depth |
| Script §3, all five subsections | Linear inference, ridge/SVD/Bayes, Lasso variants, elastic net, validation/information criteria |
| Script §4.1–4.3 | Indicator regression, discriminant models and covariance regularization, logistic estimation and optimization |
| Script §4.4–4.8 | CART, bagging, forests, AdaBoost, hard/soft margins; kernel-map supplement added from [B] |
| Script §4.9–4.11 | Perceptron theorem, MLP approximation/backpropagation, CNNs, interpretation, transfer/multitask/multimodal learning |
| Script §5 | Mixtures, EM updates/monotonicity, k-means and brief hierarchical-clustering comparison |
| Script §6.1–6.6 | FA, PCA theorem/SVD/PPCA, component selection, autoencoder variants, VAE/GAN, ICA identifiability and likelihood |
| Script §§7–8 | DAGs, d-separation, Markov properties/equivalence, faithfulness, SEMs, interventions, counterfactuals; not omitted because they occur late |
| All available lecture decks | Early introductory/decision-theory/logistic decks corroborated by script; ensemble, neural, and mixture decks mapped above; transformer and generative-model additions separately captured |
| Double-descent supplement | Interpolation and model/epoch curves included; plot interpreted visually without inventing a universal theorem |
| Sheets 1–3 and notebooks | Python/Iris, implemented kNN and Bayes risk, regression bias/variance and near-orthogonality experiments |
| Sheets 4–6 and notebooks | Tikhonov/intercept/elastic-net derivations, coefficient paths and coordinate sweeps, CV, Gaussian-class MLE and LDA/QDA/logistic comparison |
| Sheet 7; notebooks 7–8; mislabeled PDF solution | Likelihood-ratio selection, trees/forests, feature importance, ROC/AUC, and AdaBoost proof; numbering discrepancy documented |
| Sheets 9–11 and notebooks 10–11 | Margin geometry/perceptron proof, PyTorch tutorial, GMM/KDE/k-means, PCA/FA/FastICA applications |
| Assessment | Exam link/feedback are present but no examination questions or exam syllabus are archived; no independent exam cross-check possible |

The script's concluding list of supposedly omitted topics is stale relative to its body and supplied slides: SVMs, DAGs, and deep learning are actually represented. The detailed content takes precedence. RKHS theory, developed PAC learning, support-vector regression, general undirected/Markov-random-field theory, and full diffusion/RL algorithms are not inferred from those closing lists or introductory mentions.

## Source limitations and unresolved issues

- Separate Lecture 3–5/7 files are not present, and archive-week labels do not consistently agree with lecture numbering or script dates. The consolidated script covers the intervening main topics, but the exact delivery calendar cannot be reconstructed. The late graphical/causal text contains a 2021 date and unfinished references; its inclusion in the supplied 2024 script is evidence of available course material, not confirmation of delivery in a particular session.
- There is no standalone Exercise 8 sheet. `Solution Exercise 7.pdf` is internally headed Sheet 8, while Sheet 7 includes the forest/boosting tasks; notebooks 7 and 8 split the corresponding computational material. This is an evidenced packaging/numbering mismatch, not an assumed missing topic.
- Several source equations require caution: the script reverses the ELBO inequality (PDF p. 95); the boosting slide omits factor 2 in its first product bound ([B], pp. 41–44), whereas the exercise solution and the slide's edge bound are consistent; the logistic discussion overstates positive definiteness without a rank qualification (script pp. 37, 40 together resolve this). FA rescaling signs, PPCA likelihood notation, and ICA score-sign terminology also contain ambiguous or inconsistent displays. Only the supported, internally consistent formulations above are retained.
- Exercise 6 prints a transposed symmetric covariance as if it were a different covariance; its notebook instead applies `A` versus `Aᵀ` as data-generating transforms, explaining the intended comparison. Exercise 5's notebook has implementation inconsistencies: its manual coordinate loop does not cover all columns of the augmented design; the nominal mixture-weight comparison varies `alpha` rather than `l1_ratio`; and model `.score()` output is labeled error. These establish intended techniques, not validated numerical results. A complete code correction/re-execution was outside profiling scope.
- The 2023 heading on the PDF solution to Exercise 5 and older paths in notebooks indicate reused teaching material. This does not invalidate topic coverage but limits assumptions about exact version chronology.
- Data filenames differ from notebook expectations: `Data Exercise 4.csv` contains prostate data, `Waiting Data.csv` supplies waiting times, and `Polynomial Fit Data.dmg` is statically identifiable as a pandas pickle stream rather than a disk image. Iris and Olivetti data are fetched externally in the examples; no network fetch or pickle deserialization was performed. Original data filenames would need mapping for future execution.
- Source rendering has some missing glyphs, especially in graphical-model notation. Readable prose supports the topics and named results, but absent symbols and unreliably printed formulas are not supplied from general knowledge.

## Sources

**Metadata:** `01_inventory/courses.csv`, row `ma4802`; authoritative transcript `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 3. Archive identity: `01_inventory/archive_matches.csv` and the archive's `index.html`.

All source labels below refer to members of `00_sources/tum/archives/Statistical Lea 950732556 (S24)_20261012_1548.zip`. For example, `[S], §6.2, PDF pp. 86–88` means that ZIP **::** `Allgemeines/Statistical Learning Script.pdf`, section 6.2, physical pages 86–88. Notebook references identify source cells by task/section heading rather than line numbers of generated text.

| Label | Exact archive member | Role |
|---|---|---|
| S | `Allgemeines/Statistical Learning Script.pdf` | 115-page complete backbone |
| I | `17. April - 23. April/Lecture 1.pdf` | 77-page introduction, applications, organization |
| L2 | `24. April - 30. April/Lecture 2.pdf` | 64-page statistical decision theory |
| L6 | `29. Mai - 4. Juni/Lecture 6.pdf` | 64-page logistic/optimization lecture |
| D | `8. Mai - 14. Mai/Extra Presentation - Double Descent.pdf` | 11-page supplement |
| B | `19. Juni - 25. Juni/Slides 1.pdf` | 78-page ensemble/margin lecture |
| N | `19. Juni - 25. Juni/Slides 2.pdf` | 133-page perceptron/MLP/CNN lecture |
| M | `26. Juni - 2. Juli/Slides 1.pdf` | 62-page mixtures/EM/clustering lecture |
| T | `26. Juni - 2. Juli/Slides 2.pdf` | 16-page transformer supplement |
| G | `10. Juli - 16. Juli/Slides Lecture 11.pdf` | 56-page deep generative representation lecture |

Exercise source groups include the following exact members (each path is relative to the ZIP root):

- **E1:** `17. April - 23. April/Exercise 1.pdf`; `17. April - 23. April/Solution Exercise 1.json`.
- **E2:** `24. April - 30. April/Exercise 2.pdf`; `24. April - 30. April/Solution Exercise 2.imscc` **::** `solution_2.ipynb` and `Statistical_learning___Solution_2.pdf`.
- **E3:** `8. Mai - 14. Mai/Exercise 3.pdf`; `8. Mai - 14. Mai/Solution Exercise 3.pdf`; `8. Mai - 14. Mai/Notebook - Solution Exercise 3.json`; `8. Mai - 14. Mai/Polynomial Fit Data.dmg`.
- **E4:** `15. Mai - 21. Mai/Exercise 4.pdf`; `15. Mai - 21. Mai/Solution Exercise 4.pdf`; `15. Mai - 21. Mai/Notebook - Solution Exercise 4.json`; `15. Mai - 21. Mai/Data Exercise 4.csv`.
- **E5:** `22. Mai - 28. Mai/Exercise 5.pdf`; `22. Mai - 28. Mai/Solution Exercise 5.pdf`; `22. Mai - 28. Mai/Notebook - Solution Exercise 5.json`.
- **E6:** `29. Mai - 4. Juni/Exercise 6.pdf`; `29. Mai - 4. Juni/Solution Exercise 6.pdf`; `29. Mai - 4. Juni/Notebook - Solution Exercise 6.json`.
- **E7–E8:** `5. Juni - 11. Juni/Exercise 7.pdf`; `5. Juni - 11. Juni/Solution Exercise 7.pdf`; `5. Juni - 11. Juni/Notebook - Solution Exercise 7.json`; `5. Juni - 11. Juni/Notebook - Solution Exercise 8.json`; `5. Juni - 11. Juni/Data - Exercise 7, SAheart.csv`; `5. Juni - 11. Juni/Data - Exercise 7, prac7.csv`.
- **E9:** `19. Juni - 25. Juni/Exercise 9.pdf`; `19. Juni - 25. Juni/Solution Exercie 9.pdf` (source filename spelling preserved).
- **E10:** `26. Juni - 2. Juli/Exercise 10.pdf`; `26. Juni - 2. Juli/Solution - Exercise 10.pdf`; `26. Juni - 2. Juli/Notebook - Solution Exercise 10.json`; `26. Juni - 2. Juli/Waiting Data.csv`.
- **E11:** `3. Juli - 9. Juli/Exercise 11.pdf`; `3. Juli - 9. Juli/Solution Exercise 11.pdf`; `3. Juli - 9. Juli/Notebook - Solution Exercise 11.json`.

Regenerable extracted documents, page-delimited text, notebook-cell text, and visual checkpoints are retained under `.cache/ma4802/`. They are intermediate results; the original ZIP and transcript remain the authoritative evidence.
