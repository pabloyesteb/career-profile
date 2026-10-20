---
id: example-second-order
source: example-optimization
parent: example-unconstrained
title: Second-Order Sufficient Condition for a Strict Local Minimum
type: theorem
---

# Second-Order Sufficient Condition for a Strict Local Minimum

## Statement

Let $f:\mathbb R^n\to\mathbb R$ be twice continuously differentiable near $x^*$. If

$$
\nabla f(x^*)=0,\qquad \nabla^2 f(x^*)\succ 0,
$$

then $x^*$ is a strict local minimizer of $f$.

## Explanation

The Taylor expansion has a positive quadratic term in every nonzero sufficiently small displacement. Continuity of the Hessian controls the remainder locally, so $f(x)>f(x^*)$ for all nearby $x\neq x^*$.

## Important distinctions

At a twice differentiable local minimum, stationarity and a positive-semidefinite Hessian are necessary, but generally not sufficient for strict local minimality. Positive definiteness is sufficient, but it is not necessary: $f(x)=x^4$ has a strict local minimum at zero with $f''(0)=0$.

## Granularity rationale

This compact result can stand alone when treated as a distinct reusable theorem. In an actual brief lecture section, it may fit better into a larger optimality-conditions Item.

## Source references

Illustrative mathematics only. Not yet matched to a source document, section, or page.
