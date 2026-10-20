---
id: example-kkt
source: example-optimization
parent: example-constrained
title: Karush–Kuhn–Tucker Necessary Conditions
type: theorem
---

# Karush–Kuhn–Tucker Necessary Conditions

## Problem setting

Consider a differentiable optimization problem

$$
\min_{x\in\mathbb R^n} f(x) \quad \text{subject to}\quad
 g_i(x)\leq0\ (i=1,\ldots,m),\qquad h_j(x)=0\ (j=1,\ldots,p).
$$

The Lagrangian is $\mathcal L(x,\lambda,\mu)=f(x)+\sum_i\lambda_i g_i(x)+\sum_j\mu_j h_j(x)$.

## Necessary conditions

If $x^*$ is a local minimizer and a suitable constraint qualification holds, there exist multipliers $\lambda^*\geq 0$ and unrestricted equality multipliers $\mu^*$ for which

- **Stationarity:** $\nabla_x\mathcal L(x^*,\lambda^*,\mu^*)=0$.
- **Primal feasibility:** $g_i(x^*)\leq0$ and $h_j(x^*)=0$.
- **Complementary slackness:** $\lambda_i^* g_i(x^*)=0$ for each $i$.

Inactive inequalities necessarily have zero multipliers; active inequalities may have zero or positive multipliers.

## Scope and limitations

These are necessary conditions under a constraint qualification, not sufficient conditions for arbitrary nonconvex objectives. Constraint qualifications such as LICQ provide specific regularity assumptions. In differentiable convex problems with convex inequalities and affine equalities, any feasible KKT point is globally optimal; additional conditions may be needed to guarantee multipliers exist at an optimum.

## Granularity rationale

Stationarity, feasibility, and complementary slackness form one theorem rather than separate Items. A developed treatment of constraint qualifications could be an independent Item.

## Source references

Illustrative mathematics only. No claim that this result occurs at a particular location in MA3503; original course pages have not been checked.
