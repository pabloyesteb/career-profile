---
id: compact-operator-spectral-theory
title: Compact operators, Fredholm solvability and spectral approximation
domains: [mathematical-analysis, numerical-mathematics]
evidence_refs: ["ma3001:compact-fredholm-spectrum", "ma5348:field-sampling"]
status: reviewed
relations:
  - {type: related_to, target: matrix-low-rank-pca}
  - {type: related_to, target: random-fields-sampling}
---

# Compact operators, Fredholm solvability and spectral approximation

## Solvability is more than matrix inversion

A compact linear operator sends bounded sequences to sequences whose images have convergent subsequences. Integral operators, including the source's Volterra-type integration examples, and compact diagonal examples give infinite-dimensional settings; compactness survives the compositions and limits treated in the course. Banach adjoints relate kernels, annihilators and closures of ranges. Complements and quotient factorizations separate a solvability obstruction from a choice of solution coordinates.

Fredholm operators have finite-dimensional kernel and cokernel and closed range; their index is the difference of these dimensions. The course covers index stability under compact perturbations and the Fredholm alternative for \(I-S\), \(S\) compact. The profile supplies this solvability framework but not its full adjoint compatibility formula; that formula is not silently reconstructed here.

## Spectrum and decomposition

For a bounded operator, the resolvent consists of scalar shifts for which the shifted operator has bounded inverse; its complement is the spectrum. Point, continuous and residual spectrum distinguish different failures of invertibility. Over complex Banach spaces the spectrum has compactness/nonemptiness properties, with polynomial spectral mapping and a spectral-radius formula covered in the source. Multiplication and shift examples prevent equating every spectral point with an eigenvalue.

For compact operators, **nonzero** spectral values are eigenvalues with finite-dimensional eigenspaces; possible accumulation is only at zero. Compact normal operators on Hilbert spaces admit spectral decompositions. Self-adjointness, positivity and normality are distinct structural conditions; their conclusions do not transfer to every bounded operator.

Compact-operator SVD supports finite-rank truncation and best rank-constrained approximation, with operator-norm error controlled by the omitted singular value. This infinite-dimensional result connects to [matrix SVD/PCA](matrix-low-rank-pca.md), but finite matrix identities and general Banach-space adjoints should not be conflated with a Hilbert singular system.

## Covariance and PDE applications

Numerical UQ turns a covariance kernel into an integral operator. Hilbert–Schmidt spectral theory, Mercer structure and covariance eigenpairs lead to the [Karhunen–Loève representation](random-fields-sampling.md), with a variance-tail truncation criterion. Rellich compactness and weak PDE solution operators provide a second application connection.

These examples identify a reusable question: which directions may be truncated, and in which norm is the resulting error meaningful? They do not establish a general observed compression rate or personal eigensolver implementation. Detailed spectral proofs and constants absent from the source profiles remain outside extraction.

Evidence: `ma3001:compact-fredholm-spectrum` in [Functional Analysis evidence](../evidence/ma3001.yaml) and `ma5348:field-sampling` in [UQ evidence](../evidence/ma5348.yaml).
