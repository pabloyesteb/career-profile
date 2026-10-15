# Advanced Seminar Course (MA6015)

## Module metadata

| Field | Value |
|---|---|
| Official title | Advanced Seminar Course |
| Module code | MA6015 |
| ECTS | 3 |
| Grade | BE (passed) |
| Seminar theme | Multilevel Monte Carlo Methods for Uncertainty Quantification |
| Teaching term | Summer semester 2025 |
| Profile status | complete_validated |

## Evidence base and material structure

The generic transcript module is matched by component title to `Hauptseminar_ MLMC for UQ (SoSe 25)_20261012_1600.zip`. The archive establishes the specific seminar theme and contains 15 PDF documents totaling approximately 343 pages: a 22-page instructor kick-off deck, seven participant presentations (263 pages), and seven paired handouts (58 pages). The available research-paper topics are P1, P2, P3, P4, P6, P7, and P12. Two nested IMSCC packages contain LaTeX templates for the slides and report; their structure and source were inspected statically.

The kick-off deck provides the common mathematical setup and the intended paper list. Each available handout/presentation pair was analyzed as one evidence unit, with the slides used for detailed formulas, algorithms, plots, and diagrams and the handout used for synthesis and critical discussion. Because these are participant-prepared research-paper presentations rather than instructor lecture notes, the profile records seminar coverage and preserves limitations and inconsistencies instead of treating every secondary statement as independently authoritative. Representative formula-, theorem-, algorithm-, and diagram-heavy pages were rendered and visually checked.

## Technical content

### Random PDE uncertainty and Monte Carlo foundations

*Evidence: `Hauptseminar_ MLMC for UQ (SoSe 25)_20261012_1600.zip :: Organisation/Slides Kick-off meeting (24.04.2025)`, pp. 10–18; P1 presentation, pp. 3–18; P1 handout, pp. 1–3.*

- Parametric and random PDEs `L(xi)u=0` with boundary operator `B`, random coefficient fields represented by series expansions, and discretization to random algebraic systems `A(xi)u(xi)=b(xi)`.
- Quantities of interest `Q(u)` and estimation of statistics such as `E[Q]`. Standard Monte Carlo uses independent samples; its mean-square error separates sampling variance from spatial-discretization bias.
- Multilevel Monte Carlo (MLMC) uses approximations `Q_0,...,Q_L` and corrections `Y_0=Q_0`, `Y_l=Q_l-Q_{l-1}` to telescope `E[Q_L]`. Fine and coarse terms in each correction must share the same random input to obtain variance reduction.
- Level-dependent sample allocation balances correction variance against cost. Most samples are assigned to inexpensive coarse levels, while the diminishing variance of fine corrections permits fewer expensive fine-grid samples.
- MLMC complexity theorem under weak-error rate `alpha`, correction-variance rate `beta`, and work rate `gamma`: cost is `O(epsilon^-2)` for `beta>gamma`, `O(epsilon^-2(log epsilon)^2)` for equality, and `O(epsilon^(-2-(gamma-beta)/alpha))` for `beta<gamma`, subject to the stated compatibility condition `alpha >= min(beta,gamma)/2`.
- Practical level selection through a bias estimate from the last correction and allocation `N_l` proportional to the square root of variance divided by per-sample cost.

### Elliptic PDEs with lognormal random coefficients and finite elements

*Evidence: archive member `Slides and Handouts of Presentations/Presentation P2 Pablo Yeste Ble___ment Error and MLMC (12.06.25)`, pp. 3–30; paired P2 handout, pp. 1–3; P1 presentation/handout.*

- Pathwise weak formulation of elliptic diffusion: for almost every realization, find `u(omega)` in `H^1_0(D)` such that the random-coefficient bilinear form equals the forcing functional for every test function.
- Lognormal coefficients `a=exp(g)` with Gaussian `g`, spatial Hölder regularity `C^t`, integrability of the reciprocal minimum coefficient, and random forcing in negative-order Sobolev spaces. Lack of uniform ellipticity and boundedness prevents direct use of classical uniform FEM theory.
- Pathwise elliptic regularity `u(omega) in H^(1+s)(D)` for `s<t`, with constants whose dependence on `a_min`, `a_max`, and the Hölder norm is tracked and then lifted to Bochner-space estimates using integrability and Hölder inequalities.
- Piecewise-linear conforming Galerkin approximation, Céa quasi-optimality for each realization, and the Bochner-space energy-norm estimate `||u-u_h||_{L^p(Omega;H^1(D))} <= C h^s` for `s<t`.
- For bounded linear quantities of interest, the presentation identifies MLMC weak and strong rates `alpha=s` and `beta=2s`, connecting FEM regularity directly to estimator bias, correction variance, and total cost.
- Groundwater-flow model based on Darcy diffusion with lognormal permeability; Karhunen--Loève representations of random fields and numerical comparisons of standard MC and MLMC over mesh hierarchies.

### Finite-volume MLMC and coarse-grid variates

*Evidence: archive members `Presentation P3 Alessio Rocco C___ume Discretizations (26.06.25)`, pp. 3–36, and `Handout P3 Improved Multilevel ___ume Discretizations (26.06.25)`, pp. 1–4.*

- Steady Darcy flow with incompressibility in two and three dimensions, scalar random permeability, and randomly layered polygonal/polyhedral subdomains. Permeability models include piecewise lognormal variables and piecewise correlated lognormal Gaussian fields with exponential covariance.
- Cell-centered finite-volume discretization on uniform boxes, midpoint quadrature, flux balance, and the resulting sparse symmetric positive-definite algebraic systems.
- Equivalence of the chosen finite-volume scheme to a finite-element discretization with quadrature. For bounded linear functionals and the random-layer models, the stated estimate is `L^q(Omega)` error `O(h^s)` for any `s<1/2`; the corresponding MLMC assumptions use weak rate below `1/2` and variance rate below `1`.
- Three-dimensional solution with preconditioned conjugate gradients and algebraic multigrid (AMG-PCG), including residual-based stopping. Random-field sampling by circulant embedding is identified as a contributor to level cost.
- Coarse-grid variates (CGV): partition a stationary fine-grid coefficient sample into `2^d` valid coarse-grid subvectors, average their coarse quantities of interest, and subtract this average from the fine result. The estimator remains unbiased while reducing correction variance, at less than roughly twice standard per-correction cost in the presented setting.
- Numerical examples use pressure averages and boundary outflow in randomly layered media and compare two- and three-dimensional variance decay with and without CGV.

### Optimization of MLMC hierarchies

*Evidence: archive members `Presentation P4 Iacopo di Pippo___tilevel Monte Carlo (26.06.25)`, pp. 3–57, and `Handout P4 Optimization of Mesh___tilevel Monte Carlo (26.06.25)`, §§2–5, pp. 2–16.*

- MLMC hierarchy as the joint choice of number of levels, mesh sizes, and samples per level. Total work is minimized subject to a probabilistic tolerance constraint.
- Error splitting parameter `theta` allocates tolerance between discretization bias and statistical error. A Lindeberg--Feller normal approximation converts the tail-probability requirement into a variance constraint involving the corresponding Gaussian quantile.
- Asymptotic models for bias `Q_W h_L^q1`, correction variance `Q_S h_(l-1)^q2`, and work `h_l^(-d gamma)`. The relaxed continuous optimization permits real mesh sizes and sample counts before implementable integer hierarchies are constructed.
- Lagrange-multiplier allocation gives `M_l` proportional to `sqrt(V_l/W_l)` times the total sum of `sqrt(V_k W_k)`, and the finest mesh is fixed by the bias constraint.
- Optimality conditions for intermediate meshes produce a second-order difference equation in logarithmic mesh size. Parameters `eta=q1/(d gamma)` and `chi=q2/(d gamma)` separate the cases `chi=1` and `chi!=1`, yielding explicit optimal hierarchies, level counts, error splits, and asymptotic work regimes.
- Optimized geometric meshes have an analytically selected refinement ratio and can attain the same asymptotic work as fully optimized non-geometric hierarchies under the stated model. The slides emphasize that optimizing `theta` often provides more practical gain than replacing a well-chosen geometric hierarchy.
- Numerical studies use a three-dimensional random elliptic PDE and a geometric-Brownian-motion option payoff. Continuation MLMC (CMLMC), GMRES, and MUMPS illustrate how solver-dependent work exponents affect the optimal hierarchy.

### Multilevel best linear unbiased estimation

*Evidence: archive members `Presentation P6 Emily Gasmann o___Unbiased Estimators (03.07.25)`, pp. 3–41, and `Handout P6 On Multilevel Best L___Unbiased Estimators (03.07.25)`, pp. 1–4.*

- Multiple model outputs `Z_1,...,Z_L` with finite means, variances, covariances, and correlations. Subsets of models evaluated with common inputs define statistically coupled model groups.
- Block linear model `Y=H mu+epsilon` assembled from all groups and samples. Generalized least squares and the Gauss--Markov--Aitken theorem yield the multilevel BLUE (MBLUE), with covariance equal to the inverse information matrix.
- Scalar BLUE `alpha^T mu_hat` estimates the finest-model expectation or an arbitrary linear combination; its variance is `alpha^T Psi^-1 alpha`. Positive-definite group covariance matrices support uniqueness and the variance-minimality proof.
- Unknown model covariance can be approximated either by reusing estimator samples, which introduces bias through data-dependent weights, or by independent pilot samples, which require additional evaluations and can increase variance.
- Sample Allocation Optimal BLUE (SAOB) minimizes BLUE variance under a cost budget and an upper bound on models coupled in one group. Unlike classical MLMC's analytic allocation, this group-allocation problem is numerical and may involve up to `2^L-1` coupling groups.
- A sharp nonzero variance lower bound is derived in the infinite-low-fidelity-data limit with a fixed number of high-fidelity evaluations. SAOB approaches this bound under appropriate allocations.
- MC, MLMC, control variates, MFMC, approximate control variates, and fully coupled estimators are represented in the common framework. The seminar contrasts MLMC's simple structure with MBLUE/SAOB's covariance-system solves and stronger variance optimality.

### Multifidelity variance and global sensitivity estimation

*Evidence: archive members `Presentation P7 Yufei Wang on M___idelity Monte Carlo (10.07.25)`, pp. 3–37, and `Handout P7 Multifidelity Monte Carlo (10.07.25)`, pp. 1–4.*

- Functional ANOVA/high-dimensional model representation decomposes model output into main and interaction components over subsets of independent inputs.
- Sobol main-effect indices measure variance caused by one input alone; total-effect indices include all interactions containing that input. Conditional-variance forms and Owen estimators are used for stable unbiased sensitivity estimation.
- Multifidelity Monte Carlo combines one high-fidelity model with correlated, cheaper surrogates through control-variate differences. Separate estimators target output mean, variance, and Sobol main/total contributions.
- Model management orders surrogates by correlation with the high-fidelity model and uses model costs and correlations to derive optimal control-variate coefficients and nested sample ratios under a total computational budget.
- The Ishigami function provides an analytic sensitivity benchmark. A convection--diffusion--reaction model of two-dimensional hydrogen combustion demonstrates sensitivity analysis for an expensive time-dependent PDE with uncertain reaction parameters.
- The method depends on strong cross-fidelity correlation and useful low-cost models; poor correlation or a badly chosen allocation can eliminate its advantage.

### Rare-event probability estimation

*Evidence: archive members `Presentation P12 Lucas Vicentim___evel estimation of rare events.pdf`, pp. 3–22, and `Handout P12 Multilevel Estimation of Rare Events (03.07.25)`, §§2–6, pp. 4–22.*

- Limit-state functions, failure domains, and failure probabilities as expectations of indicator functions. The crude MC estimator is unbiased with Bernoulli variance `P_F(1-P_F)/N`, but its relative error requires sample counts proportional to the inverse rare-event probability.
- Subset simulation decomposes a rare failure event into nested intermediate domains and a product of less extreme conditional probabilities. A Metropolis--Hastings-type Markov chain samples successive conditional input distributions; thresholds are chosen adaptively to maintain a target conditional probability.
- Multilevel failure domains combine changing thresholds with progressively refined numerical models. Since these domains need not be nested, repeated Bayes factorization introduces both forward and reverse conditional probabilities, estimated through MCMC.
- The MLE analysis establishes relative bias and variance of order `O(N^-1)` under its assumptions, while exposing costs from fine-level burn-in and a fixed high-dimensional random-field parameterization.
- MLE-var increases both physical resolution and Karhunen--Loève dimension by level. It seeds conditional chains from previous failure samples, adds new Gaussian KL coordinates as required, and discards unnecessary components after transitions; this reduces coarse-level over-parameterization at the price of more complex bookkeeping.
- The numerical flow-cell example combines lowest-order Raviart--Thomas mixed finite elements, lognormal permeability from a KL expansion, and an outflow failure threshold. Subset simulation, MLE, and MLE-var are compared through empirical failure-probability distributions and computational cost.

## Algorithms and numerical methods

- Crude Monte Carlo, telescoping MLMC, optimal levelwise sample allocation, and continuation MLMC.
- Conforming piecewise-linear finite elements, cell-centered finite volumes, midpoint quadrature, and lowest-order Raviart--Thomas mixed finite elements.
- KL expansion and circulant embedding for Gaussian/lognormal random fields.
- AMG-preconditioned conjugate gradients, GMRES, MUMPS direct solves, and mesh-hierarchy optimization.
- Coarse-grid variates, classical and approximate control variates, MFMC, MBLUE, fully coupled BLUE, and SAOB.
- Sobol/Owen global sensitivity estimators and ANOVA-HDMR decomposition.
- Metropolis--Hastings conditional sampling, subset simulation, multilevel rare-event estimation, and variable-complexity MLE-var.

## Computational work and tools

- **Document preparation:** supplied nested packages contain LaTeX source for a TUM Beamer presentation and a `scrartcl` handout, with `algorithm2e`, `biblatex`/Biber, mathematical, graphics, and scientific-units packages. The template comments identify Overleaf and `latexmk` workflows.
- **Numerical software/methods discussed:** AMG-PCG, GMRES, MUMPS, and CMLMC appear in the analyzed research examples. No executable solver implementation, notebook, raw dataset, or participant source-code submission is present, so software use by the course participant cannot be established beyond the documented seminar materials.

## Applications and model problems

- Groundwater and subsurface flow through uncertain or randomly layered porous media; pressure, outflow, and breakthrough-time quantities of interest.
- Safety and reliability through rare-event/failure probabilities, including flow-cell thresholds and broader engineering-system risk.
- Random elliptic diffusion PDEs with rough lognormal coefficients and stochastic forcing.
- Geometric Brownian motion and option-payoff estimation.
- Ishigami global-sensitivity benchmark and hydrogen-combustion convection--diffusion--reaction modeling.
- Multifidelity analysis in computational fluid dynamics, materials, Bayesian inverse problems, and other expensive simulation settings is discussed as extension scope.

## Seminar and assessment evidence

- The seminar required a 45-minute presentation, 15-minute discussion, a two-to-four-page handout, attendance, and active participation. Assessment was pass/fail.
- Participants were expected to explain the paper's main method, numerical evidence, strengths and limitations, and possible extensions/applications. This explains the combination of theorem-level analysis, computational experiments, and critical discussion in each evidence unit.
- The archive contains seven of the thirteen research-paper topics listed in the kick-off deck. There is no local evidence that the six absent topics (P5, P8–P11, P13) were actually presented; they are excluded from technical claims.
- Two internal formula inconsistencies were found. The P2 handout's displayed FEM error rates conflict with its more detailed presentation, which gives the energy-norm rate `h^s` and MLMC rates `alpha=s`, `beta=2s`. The P3 handout/presentation reverses the `beta>gamma` and `beta<gamma` labels in the generic complexity theorem; the profile follows the mutually consistent P1 and P2 statements and uses P3 only for its finite-volume-specific results.

## Thematic categories

- Uncertainty quantification
- Monte Carlo, multilevel, and multifidelity methods
- Random PDEs and stochastic modeling
- Finite-element and finite-volume methods
- Variance reduction and optimal experimental allocation
- Global sensitivity analysis
- Rare-event simulation and reliability
- Scientific communication with LaTeX

## Coverage validation

| Source structure | Profile coverage | Result |
|---|---|---|
| Instructor kick-off: random PDEs, MC/MLMC, paper map | Foundations; evidence structure | Covered |
| P1: MLMC for elliptic PDEs with random coefficients | MC/MLMC foundations; applications | Covered |
| P2: FEM error analysis and MLMC | Lognormal random coefficients and FEM | Covered; presentation/handout discrepancy recorded |
| P3: finite-volume MLMC and CGV | Finite-volume MLMC and coarse-grid variates | Covered; generic theorem discrepancy recorded |
| P4: mesh-hierarchy optimization | Optimization of MLMC hierarchies | Covered |
| P6: MBLUE and SAOB | Multilevel best linear unbiased estimation | Covered |
| P7: MFMC variance and sensitivity indices | Multifidelity sensitivity estimation | Covered |
| P12: multilevel rare events | Rare-event probability estimation | Covered |
| Two IMSCC template packages | Computational work and tools | Inspected statically; LaTeX workflow recorded |
| Listed topics P5, P8–P11, P13 | No presentation/handout in archive | Explicit limitation; not reconstructed |

## Sources

- **Transcript metadata:** `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 4.
- **Archive:** `00_sources/tum/archives/Hauptseminar_ MLMC for UQ (SoSe 25)_20261012_1600.zip`.
- **Seminar organization and common setup:** archive member `Organisation/Slides Kick-off meeting (24.04.2025)`, pp. 1–22.
- **P1 evidence:** archive members `Slides and Handouts of Presentations/Presentation P1 Felix Wede on M___random coefficients (12.06.25)` and `Slides and Handouts of Presentations/Handout P1 Multilevel Monte Car___random coefficients (12.06.25)`.
- **P2 evidence:** archive members `Slides and Handouts of Presentations/Presentation P2 Pablo Yeste Ble___ment Error and MLMC (12.06.25)` and `Slides and Handouts of Presentations/Handout P2 Finite element error___Monte Carlo methods (12.06.25)`.
- **P3 evidence:** archive members `Slides and Handouts of Presentations/Presentation P3 Alessio Rocco C___ume Discretizations (26.06.25)` and `Slides and Handouts of Presentations/Handout P3 Improved Multilevel ___ume Discretizations (26.06.25)`.
- **P4 evidence:** archive members `Slides and Handouts of Presentations/Presentation P4 Iacopo di Pippo___tilevel Monte Carlo (26.06.25)` and `Slides and Handouts of Presentations/Handout P4 Optimization of Mesh___tilevel Monte Carlo (26.06.25)`.
- **P6 evidence:** archive members `Slides and Handouts of Presentations/Presentation P6 Emily Gasmann o___Unbiased Estimators (03.07.25)` and `Slides and Handouts of Presentations/Handout P6 On Multilevel Best L___Unbiased Estimators (03.07.25)`.
- **P7 evidence:** archive members `Slides and Handouts of Presentations/Presentation P7 Yufei Wang on M___idelity Monte Carlo (10.07.25)` and `Slides and Handouts of Presentations/Handout P7 Multifidelity Monte Carlo (10.07.25)`.
- **P12 evidence:** archive members `Slides and Handouts of Presentations/Presentation P12 Lucas Vicentim___evel estimation of rare events.pdf` and `Slides and Handouts of Presentations/Handout P12 Multilevel Estimation of Rare Events (03.07.25)`.
- **Templates:** archive members `Preparing your Presentation/Template for Slides.imscc` and `Preparing your Presentation/Template for Handout.imscc`, inspected as nested packages without executing their contents.
