---
id: proximal-block-optimization
title: Proximal, conditional-gradient, block and majorization methods
domains: [optimization, numerical-mathematics, machine-learning]
evidence_refs: ["additional-foml:composite-methods", "ma4802:linear-inference"]
status: reviewed
relations:
  - {type: related_to, target: regularized-linear-inference}
---

# Proximal, conditional-gradient, block and majorization methods

## Avoiding or changing a projection

Frank–Wolfe replaces projection with a linear-minimization oracle. For a compact convex set of diameter R and smooth convex objective, the represented error bound is \(2LR^2/(k+1)\). Curvature/affine invariance, line search and the FW dual gap guide interpretation/stopping. Sparse ℓ₁ iterates and low-rank trace-norm iterates expose structure. Away steps can be linear under strong convexity and finite-polytope facial-distance assumptions; fully corrective, stochastic and nonconvex-stationarity variants differ. Simply substituting subgradients can fail on nonsmooth problems.

Prox operators are resolvents with firm-nonexpansiveness/Moreau relationships. Projected gradient is a special case; smooth-plus-convex-nonsmooth objectives yield proximal-gradient/ISTA \(O(k^{-1})\) and accelerated/FISTA-style \(O(k^{-2})\) accuracy. Soft thresholding in Lasso has an objective-normalization-dependent threshold, not one universal λ convention. Exact general prox definitions absent from the profile are not added as invented source equations.

## Splitting and blocks

Douglas–Rachford uses reflections/fixed points for subdifferential sums. For the presented proper convex terms with a minimizer, relaxation \(\gamma_k\in[0,2]\) and \(\sum_k\gamma_k(2-\gamma_k)=\infty\), the stated primal prox iterates converge. Three-operator and product-space methods extend the construction. Dykstra intersection projection admits a coordinate-descent interpretation; it is not merely naive alternating projection with another name.

Coordinate/block updates may be exact/proximal and cyclic, essentially cyclic, randomized or Gauss–Southwell selected. Gauss–Seidel sequential and Jacobi parallelizable updates differ; separable nonsmooth structure, limit-point stationarity and randomized rate assumptions are material. Statistical Learning's residual-updating Lasso exercise is a concrete method example with known augmented-column-loop defects, not a verified implementation result.

## Majorization and alternating models

NMF least-squares/KL block updates, auxiliary majorizers and multiplicative rules illustrate MM monotonicity and conditional stationarity. EM uses posterior responsibilities; CCCP uses difference-of-convex structure, with Sinkhorn row/column scaling and determinantal-kernel learning as applications. Exact MM surrogate equations are not supplied in these profiles, so they are not reconstructed. A decreasing objective does not automatically imply global optimum or finite-step correctness.

Evidence: [FOML](../evidence/additional-foml.yaml) Lectures 10–13 and [linear-regression teaching](../evidence/ma4802.yaml). [Mixtures/EM](mixtures-latent-inference.md) provides the statistical interpretation; [convex geometry](convex-conjugacy-sparse-optimization.md) retains underlying duality/projection definitions.
