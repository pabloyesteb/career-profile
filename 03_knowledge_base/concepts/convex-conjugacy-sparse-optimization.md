---
id: convex-conjugacy-sparse-optimization
title: Convex geometry, conjugacy and sparse optimization
domains: [optimization, mathematical-analysis, machine-learning]
evidence_refs: ["ma4800:convex-gradient", "ma3503:constraint-optimality", "additional-foml:convex-foundations"]
status: reviewed
relations:
  - {type: related_to, target: hilbert-projection}
---

# Convex geometry, conjugacy and sparse optimization

## Geometry, existence and first-order reasoning

Convex sets are closed under convex combinations; hyperplanes, intersections and Minkowski sums provide constructions. A closed ball is convex, whereas its sphere generally is not. Convex functions have convex epigraphs; for twice continuously differentiable functions on an open convex domain, a positive-semidefinite Hessian characterizes convexity. Pointwise suprema preserve convexity, including the variational representation of a symmetric matrix's largest eigenvalue.

Lower semicontinuity corresponds to closed epigraphs in the represented setting. Existence requires additional conditions: continuous objectives attain minima on compact feasible sets, or under the appropriate closedness/coercivity assumptions. Strict convexity implies at most one minimizer, not attainment on an unbounded domain; strong convexity provides the stronger coercivity/existence mechanism used in the optimization exercises. Weak compactness supplies the infinite-dimensional [direct-method counterpart](banach-duality-weak-compactness.md).

## Conjugacy, thresholding and duality

The Legendre–Fenchel conjugate is
\[
f^*(y)=\sup_x\{\langle y,x\rangle-f(x)\}.
\]
As a supremum of continuous affine functions it is convex/lower semicontinuous. The course computes exponential/power examples, affine-transformation rules and inverse-derivative relations where valid. Inverting a derivative function is not taking its reciprocal.

Subgradient optimality handles nonsmooth objectives: \(\partial|x|(0)=[-1,1]\). A squared discrepancy plus an absolute-value penalty produces soft thresholding; its threshold depends on the quadratic's normalization. For Euclidean projection onto an \(\ell_1\) ball, coordinatewise thresholding uses a nonnegative multiplier. An exterior point reaches the boundary; an already feasible point stays unchanged. The thresholded norm is continuous piecewise linear and decreasing, enabling scalar multiplier selection.

For basis pursuit,
\[
\min_x\|x\|_1\quad\text{subject to }Ax=y,
\]
the source's Lagrangian convention gives dual objective \(-\langle\xi,y\rangle\) under \(\|A^T\xi\|_\infty\le1\), and dual value \(-\infty\) outside this domain. Dual norm bounds and unbounded coordinate directions justify this constraint; multiplier sign conventions matter. Separation and historical LP examples supplement, rather than establish personal solver experience.

## Gradient and projected optimality

Gradient descent uses \(x_{k+1}=x_k-\eta\nabla f(x_k)\). Bounded gradient controls function Lipschitz continuity; bounded Hessian operator norm controls gradient Lipschitz continuity on the stated convex domain. Frobenius estimates can be conservative. Along gradient flow the objective derivative is minus the squared gradient norm. The quadratic derivative is \((A+A^T)x\), simplifying to \(2Ax\) only for symmetric \(A\).

The course's invariant-ball example gives \(x_{k+1}=(1-2\eta)x_k+\eta a\) and limit \(a/2\) under its initial-point/step conditions; at \(\eta=1/4\) the factor is \(1/2\). A separate normalized-gradient iteration uses geometric steps and compares gradient/objective-change/iteration stopping tests. These examples are not arbitrary-step convergence theorems.

For a differentiable convex objective on a nonempty closed convex set, the variational inequality is equivalent to \(x=P_C(x-\tau\nabla f(x))\), \(\tau>0\). This characterizes a solution, not convergence of every projected-gradient iteration. See [constrained optimization](constrained-nonlinear-optimization.md) for nonlinear constraint qualifications and local results.

Evidence: [FDA](../evidence/ma4800.yaml) and [Nonlinear Optimization](../evidence/ma3503.yaml). No acceleration, stochastic-gradient or proximal-gradient implementation is inferred from these topics.

## Convex structure beyond scalar penalties

The optimization slides extend this vocabulary with Jensen's inequality, affine composition, partial minimization and convex closure rules, Schur complements, vector/mixed norms and matrix operator/Frobenius/nuclear norms. Norm duality and support functions explain why apparently different constraints admit tractable representations. For a proper closed convex function, biconjugation recovers the function; Fenchel–Young gives \(f(x)+f^*(y)\ge\langle x,y\rangle\), with equality characterized by the appropriate subgradient relation. Closedness/properness cannot be dropped from the recovery statement. Subgradient sum/chain rules also require their stated domain qualifications.

LP, QP, SOCP and SDP are distinct modeling classes. Robust linear constraints can produce second-order cones; semidefinite formulations express spectral constraints. Lagrangian weak duality is general, whereas Slater-based strong duality applies to the specified convex setting. The slides' trust-region zero-duality-gap example is a structured nonconvex exception, not permission to apply Slater to arbitrary nonconvex programs. Normal cones and Fermat optimality connect these formulations to projection and [proximal/block methods](proximal-block-optimization.md).

This extends the earlier scalar conjugacy and basis-pursuit examples, rather than replacing them with a catalogue of solvers. [FOML evidence](../evidence/additional-foml.yaml), convex-foundations, retains the imported-slide/TUM-delivery limitation.
