# Numerical Methods for Uncertainty Quantification (MA5348)

## Module metadata

| Field | Value |
|---|---|
| Official title | Numerical Methods for Uncertainty Quantification |
| Module code | MA5348 |
| ECTS | 6 |
| Grade | 2.7 |
| Teaching term | Summer semester 2024 |
| Profile status | complete_validated |

## Evidence base and material structure

The exact-matched archive contains 33 PDF documents totaling approximately 573 pages: 109-page consolidated lecture notes, a 37-page Multilevel BLUE supplement, 19 dated lecture decks plus organization slides (372 pages), five problem sheets and five solutions (51 pages), and a four-page oral-exam topic list. Computational material comprises nine loose MATLAB files and two nested packages containing 16 MATLAB files in total, with some files duplicated between loose and packaged copies.

The updated consolidated notes define the main coverage. The oral-exam list independently confirms Chapters 1–10; the lecture decks add Multilevel BLUE. Every sheet/solution pair and all loose/nested MATLAB filenames and code structures were inspected statically.

## Technical content

### Probability in function spaces

*Evidence: `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Chapter 2, pp. 4–15; Problem Sheet 01.*

- Probability spaces, Borel σ-algebras, measurable maps, probability laws, moments, covariance, correlation, and independence.
- Banach-space-valued random variables, Bochner measurability and integration, Bochner spaces `L^p(Ω;W)`, weak versus strong measurability, and the Pettis measurability theorem.
- Convergence in `p`-th mean and almost surely, Chebyshev's inequality, the Borel–Cantelli lemma, and implications among convergence modes.
- Gaussian random vectors through linear-functional, characteristic-function, and density/covariance descriptions.

### Random fields and regularity

*Evidence: `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Chapter 3, pp. 16–24; Problem Sheet 01.*

- Random fields, realizations, finite-dimensional distributions, mean and covariance functions, and positive-semidefinite covariance kernels/matrices.
- Second-order, Gaussian, lognormal, and weakly/strictly stationary random fields.
- Hölder/Lipschitz sample paths, versions and continuous versions, and the Kolmogorov continuity theorem.
- Exercises extend the framework to Hilbert-valued Gaussian variables and covariance operators.

### Discretization and sampling of random fields

*Evidence: `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Chapter 4, pp. 25–42; Problem Sheet 02 and its MATLAB files.*

- Sampling a Gaussian field on a grid by Cholesky or spectral factorization of the covariance matrix, including positive-definiteness limitations.
- Toeplitz and circulant covariance matrices, minimal circulant extensions, complex Gaussian vectors, Fourier diagonalization, FFT-based circulant embedding, and the need for a positive-semidefinite embedding.
- Covariance integral operators, Hilbert–Schmidt spectral theory, Mercer's theorem, and the Karhunen–Loève expansion (KLE).
- Mean-square and uniform KLE convergence, optimality among finite-rank representations, and truncation error from the discarded covariance eigenvalues.
- Collocation/quadrature approximation of covariance-operator eigenpairs, including Brownian-bridge and Gaussian covariance examples.

### Elliptic PDEs with uncertain coefficients

*Evidence: `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Chapters 5–6, pp. 43–50; Problem Sheet 03.*

- Deterministic elliptic boundary-value problems in weak form, Sobolev spaces, Lax–Milgram well-posedness, conforming Galerkin approximation, best approximation, and quasi-optimality.
- Random diffusion coefficients, pathwise weak formulations, pathwise ellipticity/boundedness, and samplewise finite-element discretization.
- Lognormal coefficients, Gaussian measures on Banach spaces, Fernique's theorem, and integrability/well-posedness issues created by loss of uniform ellipticity.

### Monte Carlo and variance reduction

*Evidence: `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Chapter 7, pp. 51–58; Problem Sheets 03–04.*

- Standard Monte Carlo estimators for scalar, Hilbert-space-valued, and random-field expectations; unbiasedness, variance, mean-square convergence, bias/discretization error, and confidence intervals.
- Monte Carlo finite elements for elliptic PDEs with random data and combined sampling/discretization cost analysis.
- Gaussian and Clenshaw–Curtis quadrature, tensor-product and sparse-grid quadrature, and quasi-Monte Carlo; smoothness/dimension dependence contrasted with Monte Carlo's dimension-independent sampling rate.
- Antithetic variates and control variates, including optimal control coefficients and pilot estimation of unknown covariances.

### Multilevel and multifidelity estimators

*Evidence: `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Chapters 8–9, pp. 59–70; `Slides on Multilevel BLUE (27.06.24)`, pp. 1–37; Problem Sheet 04.*

- MLMC telescoping estimator based on coupled differences across discretization levels; allocation of samples by level and separation of bias, variance, and work.
- MLMC complexity theorem in terms of bias rate `α`, variance-decay rate `β`, and cost rate `γ`, with the three regimes `β>γ`, `β=γ`, and `β<γ`.
- Multifidelity Monte Carlo (MFMC) using correlated low- and high-fidelity models, nested sample counts, optimal control coefficients, optimal sample ratios, model-order/selection conditions, and corresponding error/cost analysis.
- Multilevel Best Linear Unbiased Estimation (MLBLUE): arbitrary groups of correlated model evaluations, generalized linear-model formulation, Gauss–Markov–Aitken BLUE, variance minimization, sample allocation, and comparison with MC/MLMC/MFMC.

### Stochastic Galerkin methods

*Evidence: `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, Chapter 10, pp. 71–92; Problem Sheet 05 and `SG_matlab.zip`.*

- Variational formulation in `L²(Ω;H¹₀(D))`, existence and uniqueness, conditional expectation, and measurability with respect to finite-dimensional noise.
- Perturbation by truncated random-field/KLE coefficients and the resulting coefficient-truncation error.
- Tensor-product trial spaces combining physical finite elements and stochastic polynomial spaces.
- Tensor-product and complete polynomial index sets; univariate orthogonal polynomials, three-term recurrence, Legendre bases for uniform variables, and multivariate orthonormal bases for independent inputs.
- Extraction of stochastic Galerkin mean and variance from expansion coefficients.
- Kronecker-product structure of the coupled Galerkin linear system, sparsity of stochastic `G` matrices, matrix-free products, and mean-based preconditioning.
- Error decomposition into coefficient perturbation, spatial finite-element error, and stochastic polynomial approximation; best-approximation and regularity-based convergence estimates.

## Algorithms and numerical methods

- Covariance-matrix spectral/Cholesky sampling and FFT-based circulant embedding.
- KLE eigenpair computation by quadrature/collocation and truncation by leading eigenvalues.
- Piecewise-linear finite elements for one-dimensional elliptic PDEs with homogeneous Dirichlet conditions.
- Standard MC, antithetic/control-variate MC, MLMC, MFMC, and MLBLUE estimators with explicit bias/variance/cost balancing.
- Forward Euler time stepping as the multilevel model hierarchy in an uncertain nonlinear two-state IVP exercise.
- Stochastic Galerkin discretization with Legendre polynomial chaos, sparse Kronecker factors, matrix-free preconditioned conjugate gradients (`pcg`), and mean-based preconditioning.

## Computational work and tools

- **Language/environment:** MATLAB, including sparse matrices, `eig`, random sampling, plotting, and `pcg`.
- `sample1D.m`: covariance assembly and spectral sampling of Gaussian processes for multiple correlation lengths.
- `kle_bbridge.m`, `kle_gauss.m`, `kle_gauss_plots.m`: numerical covariance-operator eigenpairs, normalization, analytic comparison, and parameter studies.
- `oned_linear_FEM.m`: assembly and solution of a 1D linear finite-element diffusion/reaction problem.
- `oned_MC_FEM.m` and `oned_MC_FEM_plots.m`: sampling random diffusion coefficients and estimating solution mean/variance.
- `mlmc_matlab.zip`: forward model (`DynSys.m`), MC/two-level confidence intervals, and empirical MLMC complexity-rate estimation.
- `SG_matlab.zip`, `A_mats.m`, and `G_mats.m`: stochastic Galerkin physical/stochastic matrix factors, total-degree multi-index generation, matrix-vector products, preconditioning, solution, and error experiments.
- The notes also survey UQLab, MUQ, UM-Bridge, hIPPYlib, Sparse Grids MATLAB Kit, S-IFISS, MLMC software, and CUQIpy; the archive does not demonstrate that all were used in assignments.

## Applications and model problems

- Uncertainty in engineering, environmental-science, and biological mathematical models.
- Gaussian and lognormal spatial coefficients in elliptic diffusion PDEs.
- Brownian bridge and Gaussian-kernel random fields.
- Expected PDE solutions, mean/variance fields, and quantities of interest under limited computational budgets.
- Nonlinear two-state dynamical system with random initial data for empirical MC/MLMC complexity and confidence-interval studies.
- Multi-fidelity PDE hierarchies and correlated surrogate models.

## Exercise and assessment evidence

- Sheet 1 develops Gaussian fields, covariance calculations, `L²` closure of Gaussian variables, independence in Hilbert spaces, and Banach/Hilbert-valued Gaussian variables.
- Sheet 2 requires MATLAB sampling of Gaussian fields, analytic and collocation KLE eigenpairs for Brownian bridge and Gaussian kernels, and truncation-error investigation.
- Sheet 3 connects inverse elliptic operators, Rellich compactness, Gaussian covariance operators, Fernique-type integrability, pathwise PDE well-posedness, and MC-FEM.
- Sheet 4 derives multiple-control-variate coefficients and performs Euler/MC/MLMC experiments, empirical rate estimation, fixed-budget confidence intervals, and two-level comparisons.
- Sheet 5 develops Legendre recurrences, stochastic Galerkin Kronecker products, matrix-free `pcg`, preconditioning bounds, mean/variance computation, and MC-versus-Galerkin comparisons.
- The oral-exam topic list confirms all main areas through stochastic Galerkin methods. MLBLUE is supported separately by its dedicated 37-page slide deck and Lecture 15.

## Thematic categories

- Uncertainty quantification
- Probability and random fields
- Numerical PDEs and finite elements
- Monte Carlo, multilevel, and multifidelity methods
- Stochastic Galerkin and polynomial chaos
- Scientific computing with MATLAB

## Coverage validation

| Source structure | Profile coverage | Result |
|---|---|---|
| Chapters 2–4: probability, random fields, discretization | First three technical sections | Covered |
| Chapters 5–6: deterministic/random elliptic PDEs | Elliptic PDEs with uncertain coefficients | Covered |
| Chapters 7–9: MC, MLMC, MFMC | Monte Carlo; multilevel and multifidelity estimators | Covered |
| Chapter 10: stochastic Galerkin | Stochastic Galerkin methods | Covered |
| Dedicated MLBLUE slides / Lecture 15 | Multilevel and multifidelity estimators | Covered as supplemental lecture content |
| Five sheet/solution pairs | Exercise and assessment evidence | Covered; computational and theoretical additions incorporated |
| Nine loose `.m` files and two nested MATLAB packages | Computational work and tools | Covered by static inspection; code not executed |
| Oral-exam topic list | Independent syllabus cross-check | Covered; no missing major chapter found |

## Sources

- **Transcript metadata:** `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 2.
- **Archive:** `00_sources/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- **Backbone:** archive member `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, pp. 1–109, Chapters 1–10 and Appendices A–F.
- **Supplement:** archive member `Lecture Notes/Slides on Multilevel BLUE (27.06.24)`, pp. 1–37; also `Lecture Topics and Slides/Lecture 15 (27.06.24)`.
- **Syllabus check:** archive member `Oral exam/Topics and sample questions (08.07.24)`, pp. 1–4.
- **Exercises:** archive members under `Problem Sheets/`, Sheets 01–05 and Solution Sheets 01–05.
- **Code:** archive members `Problem Sheets/*.m`, `Problem Sheets/mlmc_matlab.zip`, and `Problem Sheets/SG_matlab.zip`.
