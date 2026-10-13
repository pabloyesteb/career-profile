# Fundamentals of Optimization for Machine Learning

## Module metadata

| Field | Value |
|---|---|
| Official title | Fundamentals of Optimization for Machine Learning |
| Module code | Not stated in the transcript; `CIT413031` appears only in the archive filename |
| ECTS | 5 |
| Grade | 3.7 |
| Teaching term | Not established by the available TUM records |
| Profile status | complete_validated |

## Evidence base and material structure

The user-confirmed course archive contains 23 PDF slide decks and no exercise sheets, solutions, code, notebooks, examinations, or project files. The PDFs total 2,104 physical pages, inflated by progressive Beamer/PowerPoint reveal states.

The most complete and coherent backbone is a 21-lecture sequence totaling 1,811 physical pages: root member `lect1.pdf`, followed by `MIT_course/lect2.pdf` through `MIT_course/lect21.pdf`. The slides identify this sequence internally as **MIT 6.881 Optimization for Machine Learning**, taught by Suvrit Sra in spring 2021; Lecture 14 is an internally credited guest deck (“Gradient Flow and Diffusion,” PDF author metadata `Xiang`). Two additional root decks total 293 pages and identify themselves as a 2017 Machine Learning Summer School lecture at MPI-IS Tübingen and a 2017 PKU Summer School introduction. They overlap substantially with Lectures 1–8 and were used as supplementary cross-checks, not as independent evidence that extra topics belonged to the TUM delivery.

The archive-to-course association is user-confirmed, and the subject matter closely matches the transcript title. However, none of the PDFs is internally labelled TUM. The archive filename suggests `CIT413031`, but the transcript does not provide a module code; the filename is therefore not promoted to official metadata.

The `complete_validated` status applies to extraction and coverage of the available archive. It does not resolve the stated TUM-specific provenance limitation.

Every PDF contains selectable text on every physical page. Layout-preserving extraction is effective for headings and ordinary prose but not independently reliable for mathematical notation, multi-column comparisons, plots, geometric diagrams, embedded paper screenshots, or reveal-based algorithms. The profile was therefore built from a complete page-level text map plus targeted visual inspection across the full lecture sequence. Page references below are one-based **physical PDF pages**, not the smaller slide numbers printed in the footer.

## Technical content

### Convex analysis and mathematical foundations

*Evidence: `lect1.pdf`, pp. 14–68; `MIT_course/lect2.pdf`, pp. 2–104.*

- **Convex sets and functions:** closure properties under intersection, affine images/preimages, pointwise supremum, and partial minimization; Jensen's inequality; first-order and epigraph interpretations; matrix- and cone-valued convexity; indicator functions; and the Schur-complement construction.
- **Norms and geometry:** vector, mixed, induced matrix, operator, nuclear/trace, Frobenius, and dual norms; distance functions; support functions and their relation to dual norms and Hausdorff distance.
- **Fenchel duality at function level:** Fenchel conjugates, the Fenchel–Young inequality, biconjugation for closed convex functions, conjugates of norms and indicator functions, and examples used to derive dual formulations.
- **Nonsmooth convex analysis:** subgradients and subdifferentials, global affine underestimators, calculus rules and their constraint qualifications, pointwise-max/supremum rules, and subgradients of expectations and compositions.

### Convex problem classes, duality, and optimality

*Evidence: `MIT_course/lect3.pdf`, pp. 2–81; `MIT_course/lect4.pdf`, pp. 2–93.*

- **Canonical formulations:** linear, quadratic, second-order cone, and semidefinite programs; regularized least squares; robust linear programming as an SOCP; eigenvalue optimization; support-vector-machine and norm-regularized formulations.
- **Lagrangian duality:** primal and dual value functions, weak duality, duality gaps, strong duality, Slater constraint qualification, dual attainment, Fenchel-conjugate derivations, and variable splitting. The trust-region subproblem is used as a nonconvex example with zero duality gap; the von Neumann minimax theorem is connected to duality.
- **First-order optimality:** unconstrained gradient conditions, constrained variational inequalities, Fermat's rule, indicator functions and normal cones, subdifferential optimality, and projection characterizations.
- **KKT theory:** Lagrangian stationarity, primal and dual feasibility, complementary slackness, necessity under strong duality/constraint qualification, sufficiency for convex problems, and nonsmooth KKT conditions expressed through subdifferentials and normal cones.
- **Worked models:** Euclidean projection onto a hyperplane and the simplex, total-variation minimization, constrained regression, SVM dualization, group-lasso-style regularization, and norm-dual constraints.

### Nonconvex optimality and structured nonconvex problems

*Evidence: `MIT_course/lect5.pdf`, pp. 3–77; `MIT_course/lect6.pdf`, pp. 4–67.*

- **Limits of global optimization:** hardness constructions for nonconvex global minimization, convex maximization, copositive formulations, and the distinction between global, local, and stationary solutions.
- **Smooth stationarity:** first- and second-order necessary conditions, second-order sufficient conditions, gradient-norm criteria, and approximate stationarity notions.
- **Nonsmooth nonconvex stationarity:** Clarke directional derivatives and Clarke subdifferentials, the condition `0 ∈ ∂°f(x)`, distance-to-subdifferential stationarity, calculus properties, and the role of local Lipschitz continuity and Rademacher's theorem.
- **Spectral and hidden-convexity examples:** Rayleigh quotients, ordinary and generalized eigenvalue problems, the trust-region subproblem, the Toeplitz–Hausdorff theorem/numerical range, PCA via low-rank approximation and the Fantope relaxation, and sparse optimization/compressed sensing.
- **Generalized convexity:** geometric programs and logarithmic transformations, quasiconvex and arcwise-convex functions, linear-fractional programming, generalized Perron–Frobenius problems, and the Polyak–Łojasiewicz condition as a nonconvex class permitting global convergence behavior.

### Gradient, subgradient, and stochastic methods

*Evidence: `MIT_course/lect7.pdf`, pp. 4–169; `MIT_course/lect8.pdf`, pp. 3–89; `MIT_course/lect9.pdf`, pp. 2–35.*

- **Gradient descent:** descent directions, exact/backtracking-style line search and fixed steps, Barzilai–Borwein steps, the descent lemma for `L`-smooth functions, monotonic descent for steps below `2/L`, and stationarity measured by the minimum gradient norm.
- **Convex convergence theory:** `O(1/k)` objective convergence for smooth convex functions and linear convergence for `L`-smooth, `μ`-strongly convex functions, with rates expressed through the condition number `κ=L/μ`. The slides contrast these upper bounds with lower bounds for smooth nonconvex, convex, and strongly convex first-order optimization.
- **Nonsmooth optimization:** subgradient descent with constant, diminishing, and Polyak-type step choices; weighted averaging; `O(1/√k)` objective accuracy (equivalently `O(1/ε²)` iterations under bounded subgradients); projected subgradient descent and the projection theorem; and a mirror-descent formulation using Bregman divergence.
- **Acceleration:** ravine and heavy-ball motivation, Nesterov's accelerated gradient method, estimate/potential-style analysis, the optimal `O(1/k²)` smooth-convex rate, and accelerated behavior for strongly convex problems.
- **Stochastic gradient descent:** finite-sum and expectation objectives, unbiased stochastic gradients, mini-batching, diminishing steps, strongly convex and convex analyses, averaged iterates, `O(1/k)`-type strongly convex bounds and `O(1/√k)` convex bounds under bounded gradients/noise.
- **Variance reduction:** SAG and SVRG as linearly convergent finite-sum methods under componentwise convexity and smoothness plus strong convexity of the mean objective. SVRG uses a snapshot full gradient and the control-variate estimator `∇f_i(x)-∇f_i(x̃)+∇f(x̃)`; the stated theorem gives geometric epoch-wise contraction when its step/epoch parameters make `ρ<1`. Runtime tables compare SGD, GD, accelerated GD, and SAG/SVRG in strongly and non-strongly convex regimes.

### Constrained, composite, coordinate, and majorization methods

*Evidence: `MIT_course/lect10.pdf`, pp. 2–81; `MIT_course/lect11.pdf`, pp. 2–96; `MIT_course/lect12.pdf`, pp. 2–124; `MIT_course/lect13.pdf`, pp. 3–94.*

- **Frank–Wolfe/conditional gradient:** linear-minimization oracles in place of projections, step-size and line-search choices, affine invariance, curvature constants, the Frank–Wolfe dual gap as a stopping certificate, and the `2LR²/(k+1)` smooth-convex bound over a compact set of diameter `R`.
- **Frank–Wolfe variants:** sparse iterates over `ℓ₁` balls, low-rank iterates under trace-norm constraints, submodular polytopes, zigzagging, away steps and their linear rate under strong convexity plus finite-polytope facial-distance assumptions, fully corrective steps, nonconvex Frank–Wolfe stationarity, and stochastic variants. A counterexample shows that simply substituting subgradients need not solve nonsmooth objectives.
- **Proximal optimization:** proximity operators as resolvents, firm nonexpansiveness, Moreau decomposition, projected gradient as a special case, and proximal-gradient/ISTA for smooth-plus-nonsmooth composite objectives. The slides establish `O(1/k)` for proximal gradient and introduce accelerated proximal gradient/FISTA-style updates with the optimal `O(1/k²)` convex rate.
- **Operator splitting:** fixed-point formulations for sums of subdifferentials, reflection operators, Douglas–Rachford splitting with relaxation and its convergence conditions, best-approximation problems, and three-operator splitting.
- **Coordinate and block-coordinate descent:** exact or proximal coordinate updates; cyclic, essentially cyclic, randomized, and Gauss–Southwell selection; Gauss–Seidel versus parallelizable Jacobi block updates; stationarity/convex-optimality conditions for limit points; separable nonsmooth terms; randomized BCD and nonasymptotic rates.
- **Dykstra and product-space methods:** projection onto intersections through product-space Douglas–Rachford or proximal Dykstra, including the interpretation of Dykstra updates as coordinate descent.
- **Alternating minimization and MM:** nonnegative matrix factorization with least-squares or KL objectives, correct block updates, auxiliary majorizers, multiplicative-update reasoning, monotonic descent, and stationarity guarantees under suitable block-minimization assumptions.
- **EM, CCCP, and DC programming:** expectation maximization as a majorize–minimize construction using posterior responsibilities; the convex–concave procedure as an MM method; difference-of-convex decompositions; Sinkhorn row/column scaling as a CCCP example; and determinantal point-process kernel learning.

### Gradient flow, sampling, and optimization over probability measures

*Evidence: `MIT_course/lect14.pdf`, pp. 1–17. Formulas and the two-column comparison on pp. 8–15 were checked visually.*

- Probability densities equipped with the 2-Wasserstein distance, transport maps/push-forwards, and relative entropy `H(μ)` with respect to a target density `π`.
- Langevin MCMC and its continuous-time Langevin diffusion; the Fokker–Planck equation connects sample-space stochastic dynamics to evolution of the probability density.
- Wasserstein gradient flow of relative entropy is compared term-by-term with Euclidean gradient flow: geodesic strong convexity/HWI, log-Sobolev gradient dominance, Talagrand-type distance control, objective dissipation, and exponential continuous-time convergence under strong log-concavity.
- Euler discretization connects Langevin diffusion back to the unadjusted Langevin algorithm; the slides discuss how discretization error enters iteration-complexity guarantees.

### Convex–concave and nonconvex minimax optimization

*Evidence: `MIT_course/lect15.pdf`, pp. 2–100; `MIT_course/lect16.pdf`, pp. 2–93.*

- **Minimax foundations:** weak and strong minimax inequalities, saddle values and saddle points, compactness/convexity conditions, primal–dual gap certificates, and saddle reformulations of regularized problems.
- **Monotone-operator view:** the saddle subdifferential/vector field, variational-inequality optimality, bounded-domain and Lipschitz assumptions, and Bregman prox maps.
- **Mirror descent and Mirror Prox:** Euclidean and entropy/simplex geometries, averaged iterates, an `O(1/√T)` mirror-descent gap under bounded operators, and exploitation of Lipschitz operator structure by Mirror Prox/extragradient to reach `O(1/T)`; splitting extensions are introduced.
- **Nonconvex–nonconcave games:** global/local min–max and max–min notions, local Nash equilibria and their first-/second-order conditions, and the fact that these notions and algorithmically stable points need not coincide.
- **Algorithms:** simultaneous/two-timescale gradient descent–ascent, gradient descent with an approximate max oracle, momentum and Nesterov variants, extragradient, and optimistic gradient descent. The slides use Moreau-envelope stationarity for weakly convex value functions and compare local stability: extragradient and optimistic GD can be stable around local saddles where GDA/momentum fail; two-timescale versions converge under stated second-order sufficient conditions.
- **Machine-learning settings:** generative adversarial training, adversarial/robust learning, and other min–max models motivate the nonconvex treatment.

### Riemannian and geodesic optimization

*Evidence: `MIT_course/lect17.pdf`, pp. 3–114; `MIT_course/lect18.pdf`, pp. 2–27.*

- Smooth manifolds, tangent spaces, Riemannian metrics, geodesics, exponential maps/retractions, Riemannian gradients, and geodesic convexity as the non-Euclidean analogue of convexity.
- Matrix-manifold examples include spheres/Stiefel-type constraints and the positive-definite cone. Spectral/eigenvector problems and matrix factorization illustrate Riemannian gradient and stochastic-gradient methods; a Riemannian Polyak–Łojasiewicz property is used to explain global convergence in a geodesically nonconvex example.
- Positive-definite geometry supports metric learning, log-determinant/relative-entropy-style matrix divergences, and geodesically convex formulations. Further applications include the Brascamp–Lieb constant and Wasserstein barycenters of Gaussian distributions.
- Gaussian-mixture maximum likelihood is treated with EM and with a reparameterized Riemannian formulation over positive-definite matrices; the slides compare batch and stochastic Riemannian optimization empirically.
- Convergence material extends subgradient analysis through a manifold law-of-cosines inequality and curvature-dependent bounds; it surveys Riemannian SVRG, SPIDER, acceleration, and Riemannian Frank–Wolfe, while noting that optimal rates for geodesically convex optimization remain open in the presentation.

### Neural-network optimization

*Evidence: `MIT_course/lect19.pdf`, pp. 4–98; `MIT_course/lect20.pdf`, pp. 2–106.*

- **Training mechanics:** empirical-risk minimization with SGD/mini-batches, initialization and its effect on signal/gradient propagation, learning-rate selection, large-batch layerwise adaptive rate scaling (LARS), backpropagation, computational graphs, and automatic differentiation.
- **Stabilization and architecture:** exploding/vanishing gradients, clipping, normalization, dropout and decoupled weight decay, batch normalization, residual/identity connections, and their relationship to trainability.
- **Adaptive and momentum methods:** classical momentum and Nesterov momentum, normalized/clipped gradient descent, diagonal scaling, AdaGrad, RMSProp, Adam with first/second moment estimates and bias correction, AdamW, and LAMB for layerwise large-batch training. An experimental plot additionally compares AdaDelta; the slides compare optimizer behavior and discuss heavy-tailed gradient noise.
- **Nonconvex landscape and saddle escape:** strict saddles, negative curvature, second-order stationary points, random perturbations, perturbed gradient descent/SGD, and complexity-motivated mechanisms for avoiding exponentially slow saddle escape.

### Newton and interior-point methods

*Evidence: `MIT_course/lect21.pdf`, pp. 2–78.*

- Newton's method, Hessian-based steps, affine invariance, Newton decrement, damped versus full steps, and local quadratic convergence under a Lipschitz-Hessian assumption.
- Barrier functions for inequality constraints, logarithmic barriers, the central path, warm-started path following, and the relation between barrier parameter, approximation accuracy, and polynomial-time solution of convex programs.
- Self-concordant functions and `ϑ`-self-concordant barriers, local Hessian norms, closure under sums and affine transformations, log barriers for scalar/linear inequalities and the `−log det` barrier for the positive-semidefinite cone.

## Algorithms and convergence results

| Method/result | Assumptions and guarantee emphasized in the slides |
|---|---|
| Gradient descent | For `L`-smooth objectives, steps below `2/L` give descent; stationarity reaches `min ||∇f|| ≤ ε` in `O(1/ε²)` in the general smooth nonconvex case. Smooth convex objectives obtain `O(1/k)` objective error; smooth strongly convex objectives converge linearly with condition-number-dependent contraction. |
| Subgradient / projected subgradient | With convexity, bounded subgradients, and bounded initial distance/domain, weighted averaging gives `O(1/√k)` objective error; projection preserves the distance recursion for closed convex constraints. |
| Nesterov acceleration | Smooth convex objective error improves from `O(1/k)` to the optimal `O(1/k²)`; the strongly convex dependence improves from `κ` to `√κ` in the linear-rate factor. |
| SGD | Under unbiased bounded stochastic gradients, averaging gives `O(1/√k)` for convex objectives; stronger convexity supports `O(1/k)`-type bounds with diminishing steps. |
| SVRG | Convex, `L`-smooth components and a `μ`-strongly convex mean objective yield geometric contraction per epoch when the specified step/epoch parameters give `ρ<1`. |
| Frank–Wolfe | Smooth convex optimization over a compact convex set: `f(x_k)-f* ≤ 2LR²/(k+1)`; away steps obtain a linear rate under strong convexity and finite-polytope facial-distance assumptions. |
| Proximal gradient / accelerated proximal gradient | Smooth-plus-convex-nonsmooth composite objectives: `O(1/k)` for proximal gradient and `O(1/k²)` for the accelerated method. |
| Douglas–Rachford | For proper convex terms with a minimizer and relaxation `γ_k∈[0,2]` satisfying `Σγ_k(2−γ_k)=∞`, the presented primal prox iterates converge to a minimizer. |
| Mirror descent / Mirror Prox | Bounded monotone saddle operator gives `O(1/√T)` gap for mirror descent; Lipschitz structure enables the two-step Mirror Prox/extragradient `O(1/T)` rate. |
| Riemannian subgradient methods | Geodesically convex objectives admit Euclidean-like distance recursions modified by sectional-curvature factors; the survey distinguishes established curvature-dependent bounds from open optimal-rate questions. |
| Path-following interior point | Self-concordant barriers make damped Newton globally controllable and full Newton locally quadratic; barrier parameter controls central-path accuracy and complexity. |

## Computational work and tools

No programming language, software library, code archive, notebook, or required computational assignment is present. The material contains mathematical pseudocode, experimental plots, and references to software/toolboxes (for example, Riemannian-optimization toolboxes), but these do not establish hands-on use by the student. The course profile therefore records algorithmic and mathematical coverage only.

## Applications and model problems

- Support vector machines, regularized least squares, lasso/group sparsity, total variation, constrained regression, and robust linear programs.
- PCA, sparse recovery/compressed sensing, eigenvalue problems, low-rank and nuclear-norm optimization, and nonnegative matrix factorization.
- Logistic-regression finite sums for comparing deterministic, stochastic, accelerated, and variance-reduced methods.
- Submodular polytopes, simplex/`ℓ_p`/trace-norm constraints, best approximation, and projection onto intersections.
- Gaussian mixtures, determinantal point processes, Sinkhorn matrix scaling, metric learning, Gaussian Wasserstein barycenters, and Brascamp–Lieb optimization.
- Langevin sampling and density evolution; minimax learning including adversarial and generative settings.
- Deep-network training on MNIST/CIFAR/ImageNet-style examples, including optimizer, normalization, residual-network, and saddle-escape behavior.

## Exercise, project, and assessment evidence

Exercises and “challenge/explore” prompts are embedded in the lecture decks. They ask for proof completion, dual derivations, projection/prox calculations, convergence analyses, and method variants, including SVM/group-lasso duality, subgradient implementations, Frank–Wolfe rates, proximal identities, coordinate updates, and self-concordant barriers. There are no separate exercise solutions, projects, examinations, or code with which to verify whether all embedded prompts were assessed or implemented.

The 2017 MLSS deck (`mlss_lect1.pdf`) independently recaps convexity, subgradients, optimality, duality, SVM/norm-regularized duals, and KKT conditions. The PKU deck (`pkuLectIntro.pdf`) independently recaps convex analysis and develops gradient, momentum, and Nesterov methods. Their overlap supports the interpretation of the early backbone lectures, but their external provenance prevents treating them as TUM-specific assessment evidence.

## Thematic categories

- Convex and nonconvex optimization
- Convex analysis and duality
- First-order, stochastic, and variance-reduced algorithms
- Nonsmooth and composite optimization
- Constrained and interior-point methods
- Minimax and saddle-point optimization
- Riemannian and geometric optimization
- Optimization for machine learning and neural networks
- Sampling and Wasserstein gradient flows

## Coverage validation

| Source structure | Profile coverage | Result |
|---|---|---|
| Lectures 1–2: convexity, norms, conjugates, subgradients | Convex analysis and mathematical foundations | Covered; formulas visually spot-checked |
| Lectures 3–4: canonical problems, duality, optimality, KKT | Convex problem classes, duality, and optimality | Covered |
| Lectures 5–6: nonconvex stationarity and tractable structure | Nonconvex optimality and structured nonconvex problems | Covered |
| Lectures 7–9: GD, SGD, subgradients, acceleration, SVRG | Gradient, subgradient, and stochastic methods | Covered; tables/plots visually checked |
| Lectures 10–13: Frank–Wolfe, proximal splitting, BCD, MM/EM/CCCP | Constrained, composite, coordinate, and majorization methods | Covered; geometry/reveal sequences visually checked |
| Lecture 14: gradient flow and diffusion | Gradient flow, sampling, and probability measures | Covered; dense equations required visual inspection |
| Lectures 15–16: convex and nonconvex minimax | Convex–concave and nonconvex minimax optimization | Covered; embedded-paper and algorithm slides visually checked |
| Lectures 17–18: geometric optimization | Riemannian and geodesic optimization | Covered; plots/matrix geometry visually checked |
| Lectures 19–20: neural-network optimization | Neural-network optimization | Covered; diagrams and empirical plots visually checked |
| Lecture 21: interior-point methods | Newton and interior-point methods | Covered; final reveal states used |
| MLSS and PKU decks | Supplementary cross-check | Covered as external, overlapping evidence only |
| Exercises/projects/exams/code | Exercise, project, and assessment evidence | Limitation: embedded prompts only; no separate material |

All 21 backbone decks were mapped to profile sections, including the late-course geometric, neural-network, and interior-point material. Major named algorithms and the convergence assumptions/rates emphasized in the slides are represented. The remaining limitation is provenance, not content recovery: the available PDFs substantiate the profile technically but do not identify which subset, if any, was authored specifically for or delivered at TUM.

## Sources

- **Transcript metadata:** `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 6.
- **Archive:** `00_sources/tum/archives/fund_opt_ML_CIT413031.zip`.
- **Backbone sequence:** archive members `lect1.pdf` and `MIT_course/lect2.pdf` through `MIT_course/lect21.pdf` (2,104 total archive pages; 1,811 pages in this 21-deck sequence).
- **Supplementary cross-checks:** archive members `mlss_lect1.pdf` (147 physical pages; internally identified as MPI-IS Tübingen Machine Learning Summer School, June 2017) and `pkuLectIntro.pdf` (146 physical pages; internally identified as PKU Summer School on Data Science, July 2017).
- **Extraction/visual validation details:** `01_inventory/slide_processing_report.md`.
