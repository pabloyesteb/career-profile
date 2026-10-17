---
id: first-order-stochastic-optimization
title: First-order, accelerated and variance-reduced optimization
domains: [optimization, numerical-mathematics, machine-learning]
evidence_refs: ["additional-foml:first-order", "additional-foml:network-optimization", "tum-machine-learning-optimization:optimizers", "ma4802:classification"]
status: reviewed
relations:
  - {type: related_to, target: proximal-block-optimization}
  - {type: related_to, target: multilevel-multifidelity-estimation}
---

# First-order, accelerated and variance-reduced optimization

## Rates have an objective and a hypothesis

FOML separates descent, stationarity and global objective accuracy. For L-smooth objectives, steps below \(2/L\) give descent; smooth nonconvex stationarity reaches minimum gradient norm ≤ε with \(O(\epsilon^{-2})\) iterations in the represented setting. Smooth convex objective error is \(O(k^{-1})\); strong convexity gives condition-number-dependent linear behavior, κ=L/μ. These guarantees do not turn a general stationary point into a global minimizer.

Exact/backtracking and Barzilai–Borwein steps are distinct choices. Convex bounded-subgradient methods use constant/diminishing/Polyak-type steps and averaging to obtain \(O(k^{-1/2})\) under the stated bounded-distance/domain assumptions. Bregman mirror geometry changes the distance measure. Nesterov acceleration improves smooth convex accuracy to \(O(k^{-2})\) and strong-convex dependence from κ to √κ; heavy-ball motivation does not make every momentum schedule equivalent to that theorem. Lower bounds distinguish the nonconvex/convex/strongly convex classes.

## Stochastic objectives and control variates

SGD treats finite-sum/expectation objectives with unbiased gradients, mini-batches, averaging and diminishing steps. Under bounded gradient/noise assumptions, convex bounds are \(O(k^{-1/2})\), with \(O(k^{-1})\)-type strongly convex results. Sampling cost and gradient cost are separate complexity questions.

SVRG's control-variate estimate is
\[
\nabla f_i(x)-\nabla f_i(\widetilde x)+\nabla f(\widetilde x).
\]
SAG/SVRG geometric behavior requires convex smooth components and a strongly convex mean; SVRG step/epoch settings must give contraction ρ<1. It is not a generic linear rate for neural training. This resembles statistical control variates conceptually without asserting a shared implementation with MLMC.

## Adaptive training and numerical choices

Momentum/Nesterov, clipping/normalized directions, diagonal scaling, AdaGrad, RMSProp, Adam moment estimates/bias correction, AdamW and layerwise LARS/LAMB address different conditioning/training issues. FOML discusses heavy-tailed gradients, normalization/dropout/residual connections and perturbed GD/SGD for strict-saddle/negative-curvature escape. An AdaDelta comparison plot is not a complete additional derivation. Supplementary ML's AdaGrad proof is an illustrative diagonal least-squares analysis, not a universal rate; randomized Kaczmarz is explicitly additional reading, not delivered class content.

Statistical Learning's logistic Newton/IRLS and safeguarded searches supply a curvature-based contrast. pyLowOrder uses configurable optimizers, clipping/checkpoints and numerical guards; their implementation is separately evidenced and does not establish these mathematical convergence assumptions. Evidence: [FOML](../evidence/additional-foml.yaml), [supplementary ML](../evidence/tum-machine-learning-optimization.yaml) and [MA4802](../evidence/ma4802.yaml). No course code use or verified optimizer superiority is inferred.
