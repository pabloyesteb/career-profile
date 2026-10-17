---
id: nonconvex-geometric-optimization
title: Nonconvex stationarity, hidden structure and Riemannian optimization
domains: [optimization, mathematical-analysis, numerical-mathematics]
evidence_refs: ["additional-foml:nonconvex-geometry"]
status: reviewed
---

# Nonconvex stationarity, hidden structure and Riemannian optimization

## What a solution condition says

FOML contrasts hard global nonconvex minimization/convex maximization/copositive formulations with local or approximate stationarity. First/second-order necessary/sufficient conditions and gradient-norm criteria differ. Locally Lipschitz nonsmooth problems use Clarke directional derivatives/subdifferentials, \(0\in\partial^\circ f(x)\) and distance-to-subdifferential criteria, with Rademacher/calculus foundations. A stationary condition alone is not global optimality.

Rayleigh/generalized eigenproblems, trust regions, numerical-range/Toeplitz–Hausdorff structure, Fantope PCA relaxation and sparse recovery illustrate hidden tractability. Geometric programs/log transforms, quasiconvex/arcwise-convex and linear-fractional problems, generalized Perron–Frobenius and PL conditions identify structured nonconvex classes. Exact transformations/theorem hypotheses beyond the profile are not reconstructed; the PL label is not a property assigned to every neural objective.

## Geometry beyond Euclidean coordinates

Smooth manifolds, tangent spaces, Riemannian metrics, geodesics, exponential maps/retractions and Riemannian gradients change the optimization geometry. Geodesic convexity is not ordinary coordinate convexity. Spheres/Stiefel-type constraints, positive-definite matrices, eigenvectors and matrix factorization supply examples; Riemannian PL permits global behavior in a represented geodesically nonconvex example, not all manifold problems.

Positive-definite geometry supports metric learning, log-determinant/entropy-style divergences, Gaussian Wasserstein barycenters and Brascamp–Lieb optimization. A Gaussian-mixture likelihood is reparameterized over positive-definite matrices and compared with EM. Batch/stochastic algorithms are surveyed; this is not a personal implementation or verified comparative experiment.

Subgradient analysis uses a manifold law-of-cosines relation with sectional-curvature-dependent bounds. Riemannian SVRG/SPIDER/acceleration/FW are named extensions; optimal geodesically convex rates remain open in the presentation. Do not transplant Euclidean rates without geometry/curvature assumptions.

Evidence: `additional-foml:nonconvex-geometry` in [FOML claims](../evidence/additional-foml.yaml), Lectures 5–6/17–18. Internal slides are MIT/MLSS/PKU-branded despite the user-confirmed TUM course association; exact delivery is unestablished. Quaternion states in the thesis do not establish that its solver used Riemannian optimization.
