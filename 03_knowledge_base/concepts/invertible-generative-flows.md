---
id: invertible-generative-flows
title: Invertible density models and conditional flow matching
domains: [machine-learning, probability-statistics-uq, numerical-mathematics, dynamical-systems]
evidence_refs: ["ma4802:generative-representations", "cit4230003:flows", "cit4230003:continuous-flows"]
status: reviewed
relations:
  - {type: related_to, target: variational-generative-inference}
---

# Invertible density models and conditional flow matching

## Volume change and density evaluation

For \(x=f(z)\),
\[
\log p(x)=\log p(z)-\log|\det Df(z)|.
\]
Equal dimensions, invertibility and continuous differentiability of map/inverse underpin this density transformation. Composition accumulates log-determinants. Support and nonzero affine determinants matter; volume-preserving maps restrict expressiveness. Direct forward sampling and efficient inverse density evaluation are different parameterization choices.

Diagonal/triangular Jacobians yield products of diagonal terms; LU factorization is a full-matrix alternative. RealNVP coupling keeps a block unchanged while scaling/translating the other, yielding triangular structure. Planar/radial, IAF/MAF, splines and Glow are compared architectures, not all fully derived. Exercises establish nonlinear/affine invertibility, sigmoid-map sampling and triangular inverse Jacobians. Ambiguous source determinant indices are not silently reconstructed.

## Continuous flows and training without trajectory solves

A time-conditioned field transports densities through \(\dot x_t=u_t(x_t)\). The represented sufficient regularity includes time continuity, state Lipschitz continuity and differentiability for an invertible differentiable flow. Instantaneous change of variables gives
\[
\frac{d}{dt}\log p_t(x_t)=-\operatorname{tr}(\partial v_t/\partial x_t).
\]
Likelihood evaluation/training can require ODE integration; adjoint sensitivities/Hutchinson trace estimates are mentioned accelerations, not locally implemented tools.

Conditional flow matching mixes data-indexed Gaussian transport paths. Its chosen optimal-transport conditional paths are affine with constant conditional velocity; exact path coefficients/noise conventions are not given in the profile and are not supplied from general knowledge. Equality of conditional/marginal objective **parameter gradients** permits regression on directly sampled time/data/noise interpolants without solving the ODE during training. This is not equality of every conditional density or all objective values.

Generation still integrates the learned field; forward Euler is shown, arbitrary solvers allowed. Straight transport paths differ from diffusion paths, but outlook claims of fewer evaluations are not personal benchmark speedups. Reversible latent representations, likelihood cost and discrete-domain extensions remain method trade-offs/open directions.

Evidence: [generative models](../evidence/cit4230003.yaml) flow/exercise/CFM sections and [Statistical Learning](../evidence/ma4802.yaml) RealNVP overview. This is algorithmic knowledge, not a personally implemented flow library.
