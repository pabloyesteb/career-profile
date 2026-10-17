---
id: "hilbert-projection"
title: "Hilbert-space projection and approximation"
domains:
  - "mathematical-analysis"
  - "numerical-mathematics"
evidence_refs:
  - "ma3001:hilbert-projection"
  - "ma4800:projection-geometry"
  - "ma3503:constraint-optimality"
status: "reviewed"
relations:
  - 
    type: "related_to"
    target: "projected-policy-evaluation"
---

# Hilbert-space projection and approximation

## Setting and precise meaning

The course treats inner products, Cauchy–Schwarz, orthogonal complements and projection onto closed convex sets/closed subspaces in Hilbert spaces. Completeness and the inner-product-induced norm distinguish this setting from an arbitrary vector-space approximation.

For a nonempty closed convex set \(C\subset H\), write the best-approximation problem as
\[
P_Cx\in\operatorname*{arg\,min}_{z\in C}\|x-z\|_H.
\]
Completeness, nonemptiness, closedness and convexity give existence and uniqueness. Foundations of Data Analysis supplies the explicit real-Hilbert characterization missing from the original pilot selection:
\[
p=P_Cx\quad\Longleftrightarrow\quad p\in C,\quad
\langle z-p,x-p\rangle\le0\quad\text{for all }z\in C.
\]
Its proof uses a minimizing Cauchy sequence and the inner-product norm identity. This is theoretical coursework, not a personally implemented optimizer.

## Theoretical context

For a closed subspace, projection provides the orthogonal decomposition; with an orthonormal basis, its components are the corresponding inner products. Riesz represents continuous Hilbert-space functionals by inner products. Orthonormal systems satisfy Bessel estimates; completeness/Parseval characterizations and Fourier coefficients connect separable infinite-dimensional Hilbert spaces to \(\ell^2\). Gram–Schmidt and Pythagoras–Fourier provide the finite-dimensional computational counterpart. The Euclidean unit-ball projection is \(x/\max(1,\|x\|_2)\). Norm geometry matters: these are not statements about arbitrary Banach norms.

## Alternating projections and constrained optimality

For nonempty closed convex sets \(C,D\) in finite dimensions with nonempty intersection, alternate \(y_k=P_Dx_k\), \(x_{k+1}=P_Cy_k\). Distances to any intersection point are nonincreasing; the projection inequalities imply vanishing gaps. Boundedness, accumulation and closedness yield convergence to a common point. Two-line examples relate the rate to their angle. Neither empty intersections nor infinite-dimensional norm convergence are claimed by this source argument.

For a differentiable convex objective on a closed convex feasible set, the variational inequality corresponds to \(x=P_C(x-\tau\nabla f(x))\), any \(\tau>0\). This is a stationarity/optimality characterization, not a convergence proof for an arbitrary iterative schedule. See [convex optimization](convex-conjugacy-sparse-optimization.md) and [SVD/least squares](matrix-low-rank-pca.md) for distinct uses of the same geometry.

## Cross-domain connection

[Projected policy evaluation](projected-policy-evaluation.md) also uses approximation and projection, but its stationary-distribution weights, Bellman operator and norm-mismatch issues must remain explicit. This is an editorial mathematical relationship, not evidence that the user historically applied this course theorem to implement ADPRL. A projection in one norm does not establish convergence for another operator/norm combination.

## Evidence

[ma3001:hilbert-projection](../evidence/ma3001.yaml) → [Functional Analysis](../../02_profiles/courses/ma3001-functional-analysis.md), Hilbert-space geometry; `ma4800:projection-geometry` → [FDA](../evidence/ma4800.yaml), linear algebra and alternating projections; `ma3503:constraint-optimality` → [Nonlinear Optimization](../evidence/ma3503.yaml), variational optimality. Detailed proofs not reproduced in the profiles remain outside extraction; the projection characterization is now supported by FDA rather than reconstructed from general knowledge.
