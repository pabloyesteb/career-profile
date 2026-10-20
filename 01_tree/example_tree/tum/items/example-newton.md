---
id: example-newton
source: example-optimization
parent: example-algorithms
title: Newton's Method for Unconstrained Optimization
type: algorithm
---

# Newton's Method for Unconstrained Optimization

## Formulation and derivation

For a twice-differentiable objective $f:\mathbb R^n\to\mathbb R$, the local second-order model at $x_k$ is

$$
m_k(p)=f(x_k)+\nabla f(x_k)^\top p+\tfrac12 p^\top\nabla^2 f(x_k)p.
$$

A stationary point of this model satisfies the **Newton equation**

$$
\nabla^2 f(x_k)p_k=-\nabla f(x_k).
$$

When this linear system is solvable, the full Newton step is $x_{k+1}=x_k+p_k$. In numerical implementations it is preferable to solve the linear system rather than explicitly compute a Hessian inverse.

## Procedure

1. Choose $x_0$ and a stopping criterion.
2. Evaluate $\nabla f(x_k)$ and $\nabla^2 f(x_k)$.
3. Solve the Newton equation for $p_k$.
4. Set $x_{k+1}=x_k+p_k$ and repeat.

## Convergence and limitations

Under standard local smoothness and nonsingularity assumptions, including sufficiently regular Hessian behavior near the target stationary point, full Newton steps can converge quadratically when started sufficiently close. An indefinite Hessian can produce a non-descent direction; singular or poorly conditioned systems can fail or be inaccurate. Line search, trust-region restrictions, and modified Hessians address some robustness problems but constitute distinct algorithmic developments where substantially treated.

## Granularity rationale

The quadratic model, Newton equation, procedure and local behavior constitute one coherent algorithmic Item.

## Source references

Illustrative mathematics only; not a verified MA3503 extraction.
