---
id: banach-duality-weak-compactness
title: Banach spaces, duality and weak compactness
domains: [mathematical-analysis, optimization]
evidence_refs: ["ma3001:banach-duality", "ma3001:weak-compactness"]
status: reviewed
relations:
  - {type: related_to, target: convex-conjugacy-sparse-optimization}
  - {type: related_to, target: neumann-series}
  - {type: related_to, target: sobolev-distributions}
---

# Banach spaces, duality and weak compactness

## Completeness and bounded operators

A Banach space is a complete normed vector space. Closed subspaces, product and quotient spaces, and function/sequence spaces provide distinct settings for analysis: the profile covers continuous functions, \(L^p\), \(\ell^p\), \(\ell^\infty\), convergent sequences and \(c_0\). Density and separability must be checked in the chosen norm; they cannot be transferred indiscriminately between these examples. A bounded linear map defined on a dense subspace extends uniquely and continuously into a Banach target. Convergent Banach-space series underpin [Neumann inversion](neumann-series.md).

The fundamental principles explain why pointwise information sometimes controls operators:

- Baire category is the completeness-based foundation for uniform boundedness, open mapping and closed graph arguments.
- Banach–Steinhaus controls a pointwise-bounded family of bounded operators on a Banach domain; pointwise convergence is not operator-norm convergence.
- A bounded surjective linear map between Banach spaces is open. Consequently, a bounded bijection has bounded inverse.
- For a linear map between Banach spaces, a closed graph ensures boundedness. Dropping completeness can invalidate these conclusions.

These are analytical well-posedness tools, not convergence certificates for arbitrary numerical software.

## Duality and separation

The continuous dual \(X^*\) contains bounded linear functionals, and its norm measures their action on the unit ball. Hahn–Banach extends a dominated linear functional while preserving the relevant bound; the course treats real/complex versions, sublinear and Minkowski functionals, dual norm representation and separation. Geometric separation distinguishes a point from a closed subspace or convex set under the appropriate hypotheses; strict separation needs stronger assumptions than mere disjointness.

The canonical map \(X\to X^{**}\) leads to reflexivity. Hilbert spaces and \(\ell^p\), \(1<p<\infty\), are covered positive examples; \(c_0\) and \(\ell^1\) illustrate limitations. Reflexivity is not automatic in infinite dimensions.

## Weak convergence and variational existence

Weak convergence tests a sequence against every continuous functional; weak-star convergence on a dual tests against the predual. The course covers boundedness of weakly convergent sequences, weak lower semicontinuity of the norm, and weak sequential closedness of norm-closed convex sets. Banach–Alaoglu gives weak-star compactness of the dual unit ball. Subsequence statements require the profile's separable/reflexive settings: compactness alone is not a general sequential-compactness shortcut.

The direct method separates two tasks: extract an appropriately weakly convergent minimizing subsequence and pass to the limit using closedness and lower semicontinuity. Strict convexity supplies uniqueness **if** a minimizer exists, not compactness or existence by itself. Finite \(\varepsilon\)-nets/total boundedness, Arzelà–Ascoli and Fréchet–Riesz–Kolmogorov give complementary strong-compactness criteria for continuous and \(L^p\) functions. Mollification supplies approximation without making weak and strong convergence interchangeable.

## Connections and evidence boundary

This supplies the existence/duality vocabulary behind [convex optimization](convex-conjugacy-sparse-optimization.md) and [Sobolev formulations](sobolev-distributions.md). The link is mathematical synthesis, not a claim of personally implementing an infinite-dimensional solver. Exact compactness-domain hypotheses beyond those summarized in the source profile and full theorem proofs are not reconstructed.

Evidence: `ma3001:banach-duality` and `ma3001:weak-compactness` in [Functional Analysis evidence](../evidence/ma3001.yaml), resolving to the normed-space, fundamental-principle, duality and compactness sections of the [profile](../../02_profiles/courses/ma3001-functional-analysis.md).
