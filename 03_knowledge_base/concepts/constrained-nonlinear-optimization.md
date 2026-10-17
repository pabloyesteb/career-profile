---
id: constrained-nonlinear-optimization
title: Constrained optimality, penalties and sequential quadratic programming
domains: [optimization, numerical-mathematics]
evidence_refs: ["ma3503:constraint-optimality", "ma3503:penalty-augmented", "ma3503:sqp-barriers", "cit413042:solver-architecture", "additional-foml:convex-foundations", "additional-foml:newton-barriers"]
status: reviewed
relations:
  - {type: related_to, target: convex-conjugacy-sparse-optimization}
  - {type: related_to, target: nonlinear-model-predictive-control}
---

# Constrained optimality, penalties and sequential quadratic programming

## Constraint geometry and KKT

Consider \(\min f(x)\) subject to \(g(x)\le0\), \(h(x)=0\), with active set \(I(x)=\{i:g_i(x)=0\}\). The Bouligand tangent cone describes actual limiting feasible directions; the linearized cone uses \(\nabla g_i(x)^Td\le0\) for active inequalities and \(\nabla h(x)d=0\). Vanishing gradients or higher-order geometry can make them differ. ACQ equates the cones, GCQ their polars; neither is automatic. LICQ requires independent active gradients, MFCQ combines equality regularity and a strict feasible linearized direction, and CQ2 controls second-order feasible arcs. The exercises distinguish their consequences rather than using “regular constraints” generically.

For \(L=f+\lambda^Tg+\mu^Th\), KKT conditions are
\[
\nabla_xL=0,\quad g\le0,\ h=0,\quad\lambda\ge0,\quad\lambda_i g_i=0.
\]
MFCQ supports necessity and boundedness of the multiplier set; LICQ gives multiplier uniqueness. Strict complementarity is stronger than complementarity and may fail. With the appropriate convexity, KKT becomes sufficient; strict convexity yields primal uniqueness, not necessarily unique multipliers. Slater/generalized-MFCQ equivalence is established in the exercises' convex-inequality/affine-equality setting, not for arbitrary nonlinear constraints.

KKT stationarity/complementarity also implies the first-order tangent-cone necessary condition through inclusion in the linearized cone. Independently, strict first-order growth in every nonzero tangent direction suffices for a strict local minimum in the studied setting.

Second-order conditions concern \(\nabla^2_{xx}L\) on critical directions, not indiscriminate positive definiteness. Sufficiency yields a strict local minimum and local quadratic growth: for some \(c>0\), \(f(x)-f(\bar x)\ge c\|x-\bar x\|^2\) on nearby feasible points. Necessity requires the stated second-order qualification; a degenerate example with coinciding first-order cones still violates CQ2. Debreu's lemma adds a sufficiently large constraint quadratic to extend null-space positivity to positive definiteness.

## Penalization and augmented Lagrangians

Exact penalties \(f+\alpha\pi\) retain local exactness above a threshold; useful exact penalties are generally nonsmooth at active constraints. Equality constraints yield the augmented Lagrangian
\[
L_\alpha(x,\mu)=f(x)+\mu^Th(x)+\tfrac\alpha2\|h(x)\|^2.
\]
With a correct KKT multiplier, second-order sufficiency and sufficiently large \(\alpha\), the profile establishes local unconstrained exactness. This is not a global guarantee for arbitrary estimated multipliers. A modified quadratic-penalty sequence uses increasing penalties and scaled residual multiplier estimates; convergence plus LICQ supports feasibility and a limiting KKT pair, through a least-squares normal-equation argument.

## SQP, restoration and barriers

SQP solves a quadratic Lagrangian model with linearized constraints, then applies a step and multiplier update. Even a feasible nonlinear problem may have an infeasible QP linearization. Under the source's convergence and step-size assumptions, QP steps vanish and eventually exclude inequalities inactive at the limit; strict complementarity permits finite active-set identification. For convex affine-constrained QPs with positive-semidefinite Hessian, exact-Hessian SQP reproduces the original problem after translation, allowing one accepted full step. Lagrange–Newton is the equality-constrained special case, not a universal one-step method.

Elastic mode adds nonnegative inequality violations and positive/negative equality slacks, guaranteeing relaxed-subproblem feasibility. Eliminating them gives positive-part and absolute-value penalties, connecting SQP restoration to nonsmooth exact penalties. Feasibility does not by itself guarantee a global QP solution.

Logarithmic continuation minimizes \(B_\tau=f-\tau\sum_i\log(-g_i)\) in the strict interior while \(\tau\downarrow0\). The exercise's global accumulation-point result assumes global subproblem minimization and the **special condition that strict interior equals the feasible set**. Its monotone objective/barrier conclusions must not be generalized to practical inexact interior-point algorithms without those assumptions.

The Celis–Dennis–Tapia trust-region subproblem and degeneracy counterexamples anchor the theory. This coursework is analytical; no language, executable solver or personal SQP implementation is evidenced. The thesis's [implemented NMPC](nonlinear-model-predictive-control.md) provides a separate application of SQP/Gauss–Newton, not proof that every course theorem applies to its solver.

Evidence: the three grouped claims in [MA3503 evidence](../evidence/ma3503.yaml), covering all seven exercise/solution pairs and their source limitations.

## Primal–dual interior-point interpretation in a project

Case Studies supplies a concrete solver-use counterpart: positive inequality slacks/multipliers, perturbed complementarity \(\Lambda Ye=\tau e\), and Newton systems coupling Lagrangian Hessians, constraint Jacobians and slack/multiplier diagonal blocks. Fraction-to-the-boundary steps preserve positivity, potentially with distinct primal/dual steps; stationarity, feasibility and complementarity residuals answer different questions. The report's plus-sign logarithmic barrier is inconsistent with minimization and is not adopted.

The team integrates IPOPT through CasADi Opti with iteration cap 1000, tolerance \(10^{-4}\), adaptive barrier updates, a quality-function oracle and barrier tolerance factor 0.05. A separate `sqpmethod` branch exists, but the benchmark does not forward its configuration, so it is not an evaluated SQP comparison. This is external-solver integration, not personal implementation of IPOPT or proof of global optimality of learned nonconvex planning. ReLU fields do not automatically provide globally smooth Hessians. `cit413042:solver-architecture` in [project evidence](../evidence/cit413042.yaml) connects the theory with [transcription](optimal-control-transcription.md) and [learned field derivatives](signed-distance-neural-fields.md).

## Newton geometry and self-concordant convex barriers

The FOML slides add affine-invariant Newton reasoning. Where \(H=\nabla^2 f(x)\) is positive definite, the direction solves \(Hp=-\nabla f(x)\), and the Newton decrement is \(\lambda(x)^2=\nabla f(x)^T H^{-1}\nabla f(x)\). Damped steps provide a globalizing phase; sufficiently close to a regular minimizer, full steps have local quadratic convergence under the stated Hessian regularity. These are different claims from unrestricted global convergence of Newton's method.

Self-concordance controls curvature variation in local Hessian norms. The slides study closure under affine transformations/sums, logarithmic barriers for linear inequalities and \(-\log\det X\) on the positive-definite cone. Path-following tracks penalized central-path problems as the barrier parameter changes; complexity depends on barrier structure and target accuracy. Exact constants or a universal iteration bound are not reconstructed from the profile.

This supplies a theoretical counterpart to the IPOPT-based planning workflow, while remaining a convex-complexity theory—not a guarantee for its learned nonconvex constraints. [FOML claims](../evidence/additional-foml.yaml) distinguish Newton/barrier assumptions from the MA3503 exercise-specific continuation result above.
