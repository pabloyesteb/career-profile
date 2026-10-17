---
id: sobolev-distributions
title: Distributions, Sobolev spaces and weak PDE foundations
domains: [mathematical-analysis, numerical-mathematics]
evidence_refs: ["ma3001:sobolev-regularization", "ma5348:random-pde-galerkin", "ma6015:lognormal-fem-analysis"]
status: reviewed
relations:
  - {type: related_to, target: stochastic-pde-discretization}
---

# Distributions, Sobolev spaces and weak PDE foundations

## Generalized differentiation

Distributions are continuous linear functionals on smooth compactly supported test functions \(\mathcal D(\mathbb R^d)\), using the test-function convergence notion rather than an arbitrary norm. Locally integrable functions induce regular distributions; the Dirac distribution is a singular example. Distributional differentiation allows nonsmooth objects to be differentiated through their action on tests. The source treats the derivative of \(|x|\), weak derivatives, translations, convolution and mollifiers.

Sobolev spaces \(W^{m,p}\) collect functions with weak derivatives through order \(m\) in \(L^p\); \(H^m=W^{m,2}\) is the Hilbert setting. The course covers completeness, appropriate reflexivity/separability, smooth approximation and zero-boundary closure spaces. Neither every \(p\)-endpoint nor every boundary/domain assumption is supplied in the profile; blanket embedding or trace claims would exceed its detail. Its one-dimensional Hölder regularity and Rellich compactness illustrate how weak-derivative control can yield stronger regularity/compactness under the relevant hypotheses.

## Why this changes a PDE problem

The unknown and test functions can lie in \(H^1_0(D)\) even when classical second derivatives are unavailable. In the UQ/seminar diffusion setting, the pathwise problem is to find \(u(\omega)\in H^1_0(D)\) satisfying
\[
\int_D a(x,\omega)\nabla u(x,\omega)\!\cdot\!\nabla v(x)\,dx
=\langle f(\omega),v\rangle\quad\text{for all }v\in H^1_0(D).
\]
Here \(a\) is the diffusion/permeability field and the right side is a forcing functional. This equation expresses the weak bilinear-form formulation documented in the profiles, not a new boundary-value model. Lax–Milgram, Galerkin approximation and Céa-type best approximation connect the function-space formulation to finite elements. Their boundedness/coercivity constants matter, especially for random coefficients.

Mollification and Galerkin approximation are different operations: smoothing regularizes a function/distribution; a trial-space restriction creates a discrete variational problem. Rellich compactness can support compactness of PDE solution operators, but does not alone provide a finite-element error rate.

## Random regularity and numerical relevance

Bochner spaces \(L^p(\Omega;W)\) describe integrability of function-valued random solutions. For the seminar's lognormal coefficients, pathwise \(H^{1+s}\) regularity and coefficient-dependent constants must be lifted to these probabilistic norms; uniform ellipticity across all realizations is unavailable. The represented rate \(\|u-u_h\|_{L^p(\Omega;H^1)}\le Ch^s\), \(s<t\), is conditional on the profile's regularity/integrability assumptions, not on positivity of a coefficient alone.

See [stochastic PDE discretization](stochastic-pde-discretization.md) for the resulting numerical error budget. The sources establish theoretical coursework and an attributed seminar explanation; no personal PDE solver implementation follows from these statements.

Evidence: [Functional Analysis](../evidence/ma3001.yaml), [Numerical UQ](../evidence/ma5348.yaml), and [MLMC seminar](../evidence/ma6015.yaml), claims named in the metadata.
