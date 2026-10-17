---
id: stochastic-pde-discretization
title: Random elliptic PDE discretization and stochastic Galerkin methods
domains: [numerical-mathematics, probability-statistics-uq, mathematical-analysis, scientific-software-data-engineering]
evidence_refs: ["ma5348:random-pde-galerkin", "ma5348:teaching-code", "ma6015:lognormal-fem-analysis", "ma6015:p2-presentation", "ma6015:finite-volume-cgv", "ma6015:rare-events"]
status: reviewed
---

# Random elliptic PDE discretization and stochastic Galerkin methods

## Pathwise formulation and error constants

Elliptic diffusion with random coefficient and forcing is posed in weak form in \(H^1_0(D)\), as detailed in [Sobolev foundations](sobolev-distributions.md). Deterministic Lax–Milgram well-posedness and Galerkin best approximation require boundedness/coercivity. For lognormal \(a=\exp(g)\), the seminar analysis tracks realization-dependent \(a_{\min}\), \(a_{\max}\) and the coefficient's spatial Hölder norm rather than assuming uniform ellipticity across \(\Omega\). Integrability of these constants and the forcing lifts pathwise estimates to Bochner spaces.

For the P2 setting with Hölder exponent \(t\), the profile records regularity \(u(\omega)\in H^{1+s}\), \(s<t\), and piecewise-linear conforming FEM error
\[
\|u-u_h\|_{L^p(\Omega;H^1(D))}\le Ch^s.
\]
For its bounded linear quantities of interest, the represented MLMC rates are \(\alpha=s\), \(\beta=2s\). The P2 handout conflicts with its more detailed slides; the profile explicitly follows the latter. Domain/coefficient/forcing conditions are essential; this is not an unrestricted FEM rate for every lognormal field. Pablo's named P2 presentation supports analysis and explanation of this relationship, not authorship of the underlying research theorem or an executable solver.

## Alternative physical discretizations

The finite-volume seminar uses cell-centered unknowns, midpoint fluxes and conservation on uniform boxes for random-layered Darcy media. Its sparse SPD systems are solved by AMG-PCG with residual stopping; circulant embedding contributes to sampling cost. Equivalence to a finite-element scheme with quadrature supports functional error \(O(h^s)\), \(s<1/2\), and corresponding weak/variance-rate restrictions. These are different assumptions/rates from P2's conforming-FEM analysis.

Lowest-order Raviart–Thomas mixed finite elements appear in the rare-event flow-cell example, where outflow is the failure quantity. No assertion is made that the user implemented either numerical workflow.

## Stochastic Galerkin: physical × random approximation

Numerical UQ also treats a coupled variational formulation in \(L^2(\Omega;H^1_0(D))\), with conditional expectation/measurability relative to finite noise and perturbation from truncated random coefficients. Trial spaces combine physical finite elements and stochastic polynomials:

- Tensor-product versus complete/total-degree multi-index sets control basis growth.
- Orthogonal-polynomial recurrences give Legendre bases for uniform variables, with multivariate orthonormal products for independent inputs.
- Expansion coefficients provide solution mean/variance.
- Coupled systems have sparse stochastic factors and Kronecker-product structure; matrix-free products and mean-based preconditioning avoid treating the full coupled matrix as an unstructured dense array.

The error budget distinguishes **coefficient/KL truncation**, **spatial FEM discretization**, and **stochastic polynomial approximation**. Best approximation and regularity govern their estimates. The profile does not provide the complete operator coefficients or preconditioner bounds; these are not invented here.

## Computational evidence and connections

MATLAB `oned_linear_FEM.m` and `oned_MC_FEM.m` support assembly and MC-FEM mean/variance examples. `SG_matlab.zip`, `A_mats.m`, `G_mats.m`, total-degree index generation and matrix-free `pcg` supply stochastic Galerkin workflows and MC comparisons. Forward Euler on a two-state uncertain IVP is a separate hierarchy example, not an elliptic spatial scheme. Surveyed packages (UQLab, MUQ, UM-Bridge, hIPPYlib, sparse-grid tools, S-IFISS, CUQIpy) are background, not demonstrated user tool use.

The reusable engineering issue is preserving basis/index/operator structure; this is conceptually related to graph/data contracts in the existing scientific-ML corpus, without claiming the projects shared code or discretization. Evidence: [UQ claims](../evidence/ma5348.yaml) and [seminar claims](../evidence/ma6015.yaml). Source code was previously inspected statically; no personal numerical benchmark is established.
