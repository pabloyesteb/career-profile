---
id: concentration-random-embeddings
title: Concentration inequalities and random geometric embeddings
domains: [probability-statistics-uq, machine-learning, numerical-mathematics]
evidence_refs: ["ma4800:concentration-embeddings"]
status: reviewed
relations:
  - {type: related_to, target: multilevel-multifidelity-estimation}
---

# Concentration inequalities and random geometric embeddings

## From moments to tail guarantees

Markov and Chebyshev bounds use moment information; the exponential/Chernoff method uses a positive exponential tilt and an MGF bound. The course develops Gaussian MGFs, independent-sum factorization, affine covariance transforms and convolution of independent densities. Exponential-distribution memorylessness is a separate distributional property, not a general tail assumption.

Subgaussian variables admit an exponential-quadratic MGF bound, leading to Gaussian-type tails; independent weighted sums depend on the Euclidean norm of their coefficients. Subexponential variables have exponential-type tails, with squared standard Gaussians as the central example. Bernstein control of their sums gives concentration for squared Gaussian-vector norms. Finite variance alone does not justify these exponential bounds.

Mean-square convergence implies convergence in probability, but not conversely: \(P(X_n=n)=1/n\), with the remaining mass at zero, gives the source counterexample. Cramér-type aggregate-risk calculations additionally require the appropriate generating-function assumptions. The device-insurance illustration is elementary risk mathematics, not evidence of a personally fitted insurance model.

## High-dimensional geometry

Isotropic Gaussian vectors concentrate around radius \(\sqrt n\); the Gaussian Annulus Theorem quantifies a thin shell over its stated deviation range. Gamma-function ball volumes, equatorial concentration and near-orthogonality make Euclidean high-dimensional intuition nontrivial. For a uniform point in the unit ball in dimension \(d\),
\[
P(\|X\|_2\le a)=a^d,\qquad 0\le a\le1.
\]
Union bounds extend individual concentration to finitely many points; they do not convert a pointwise guarantee into one uniform over an entire continuous space.

## Random projection and the JL distinction

For a Gaussian matrix \(G\in\mathbb R^{k\times n}\) with independent entries of variance \(1/k\), the profile studies near preservation of a fixed vector's norm. Failure decays exponentially with \(k\varepsilon^2\). Applying this to pairwise difference vectors and a union bound yields the finite-set Johnson–Lindenstrauss mechanism.

This is a random embedding, not necessarily an orthogonal projection. A guarantee for a fixed vector or finite dataset is not a near-isometry on every ambient vector. The exam's comparison with the random matrix's own rows explicitly tests this distinction. Random-sign entries \(\pm1/\sqrt k\) appear as an exercise alternative; an unsupported theorem equating all constructions is not supplied here.

Numerical tasks propose Gaussian-normalized sphere samples, pairwise-distance histograms, projected marginals and relative squared-norm distortion across embedding dimensions. MATLAB/Python tasks are available, not personal measured outcomes. Exact constants and complete concentration proofs absent from the profile are not reconstructed.

Evidence: `ma4800:concentration-embeddings` in [FDA evidence](../evidence/ma4800.yaml). The connection to [Monte Carlo error budgets](multilevel-multifidelity-estimation.md) is disciplined probabilistic reasoning, not an assertion that JL embeddings were used by the UQ implementations.
