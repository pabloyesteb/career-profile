---
id: "matrix-low-rank-pca"
title: "Matrix SVD, low-rank approximation and principal components"
domains:
  - "numerical-mathematics"
  - "machine-learning"
evidence_refs:
  - "ma4800:svd-pca"
  - "cit413042:representation-background"
  - "ma4802:latent-factors"
  - "in2361:lexical-representations"
  - "additional-cognitive-systems:plasticity-simulation"
  - "scientific_paper:regression-preparation"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "random-fields-sampling"
---


# Matrix SVD, low-rank approximation and principal components

## Representation and best approximation

For a real matrix \(A\in\mathbb R^{m\times n}\), SVD represents
\[
A=\sum_{i=1}^{r}\sigma_i u_i v_i^T,\qquad
\sigma_1\ge\cdots\ge\sigma_r>0.
\]
Right singular vectors diagonalize \(A^TA\), left vectors diagonalize \(AA^T\), and the corresponding eigenvalues are \(\sigma_i^2\). Reduced/full SVD distinguish the rank-bearing factors from orthogonal extensions that expose kernels and complements. Geometrically, a sphere maps to an ellipsoid with singular-value axis lengths. The smaller Gram matrix can simplify a rectangular example.

Spectral, Frobenius and nuclear norms encode different combinations of singular values. Eckart–Young truncation retains leading rank-one terms and gives best rank-\(k\) approximation in the represented spectral/Frobenius settings; the relevant discarded-value errors must be interpreted in their respective norms. Rank-10/25/100 grayscale image reconstruction is an exercise, not a reported personal compression experiment.

## Iteration and stability

The power method uses repeated application of \(B=A^TA\). Convergence depends on a spectral gap and the initial directions; a repeated largest singular value does not select a unique vector. In the source's matrix-power normalization,
\[
\frac{B^\ell}{\sum_i\sigma_i^{2\ell}}\longrightarrow \frac{P_E}{d}
\]
when the top singular subspace \(E\) has multiplicity \(d\). The strictly smaller singular-value ratio \(\delta\) controls decay through \(\delta^{2\ell}\). This is not a claim that every vector-normalized power iteration has this exact limit.

Repeated or nearly repeated singular values allow sign changes, rotations within eigenspaces and large changes in individual singular vectors under small matrix perturbations. Stable singular values or invariant subspaces do not imply a unique stable vector basis. Principal angles measure subspace discrepancy through singular values of a cross-Gram matrix; \(\|P_{W^\perp}P_V\|_F\) corresponds to the Euclidean norm of the sine-angle vector in the source's setting.

## Inverse problems and data analysis

The Case Studies appendix reviews TT-SVD for voxelized truncated distance fields: clip to a narrow band and compress a 3D grid into low-rank tensor cores. This extends the mode-truncation viewpoint to a different representation, but is reviewed background, not an implemented/personal compression benchmark. Tensor ranks, voxel resolution and access to derivatives have different implications from matrix image reconstruction or covariance KL truncation. `cit413042:representation-background` in [Case Studies evidence](../evidence/cit413042.yaml) preserves that boundary.

The Moore–Penrose pseudoinverse satisfies four Penrose conditions and reciprocates nonzero singular values. For full column rank it reduces to \((A^TA)^{-1}A^T\); the general SVD formulation handles rank deficiency. Least-squares projection and the minimum-norm solution orthogonal to the kernel connect it to [Hilbert geometry](hilbert-projection.md).

PCA uses SVD-based low-dimensional coordinates; the course visualizes diagnosed/control observations from MATLAB's `ovariancancer` data in three components. This is descriptive teaching material, not an established clinical predictor. MATLAB `svd`, plotting, and Python alternatives are specified, but executable student solutions are absent.

The connection to covariance-mode truncation in [random fields](random-fields-sampling.md) is conceptual: both retain dominant modes, while matrix reconstruction error, explained variation and stochastic field truncation are different objectives. Evidence: `ma4800:svd-pca` in [FDA evidence](../evidence/ma4800.yaml), SVD chapter and exercises.

## Reconstruction, probabilistic and independent-component interpretations

Statistical Learning supplies a centered-data reconstruction interpretation: a rank-\(q\) orthogonal PCA subspace minimizes squared reconstruction error by retaining the leading covariance directions. Explained variance and residual reconstruction error refer to the fitted centered dataset, not predictive test risk. Linear autoencoder/PCA connections concern a constrained linear reconstruction problem, not arbitrary nonlinear networks.

[Latent-factor models](latent-factors-independent-components.md) explain the differences: factor analysis allocates structured covariance plus diagonal observation noise, probabilistic PCA uses isotropic noise, and ICA seeks statistically independent sources under stronger assumptions. Whitening or an SVD does not by itself identify independent non-Gaussian components. The PCA subspace can be well defined without a unique basis inside repeated-eigenvalue subspaces. This consolidates the statistical interpretation with the existing numerical SVD explanation rather than duplicating it. [MA4802 latent-factor evidence](../evidence/ma4802.yaml).

## Language, plasticity and preprocessing: related objectives

NLP uses truncated SVD/latent semantic analysis for term–document/context representations. The matrix approximation objective differs from SGNS binary discrimination. Cognitive Systems derives normalized Hebbian/Oja covariance dynamics toward a principal direction; [plasticity](spiking-neuron-plasticity.md) retains the rate/time-scale and growth-control interpretation instead of duplicating a PCA proof. A missing Oja notebook is not reconstructed.

NGValidation applies training-fitted PCA before held-out transformation and discusses latent-space hull checks. Variance retention is not automatically preservation of rare safety-relevant regions or a statistical coverage guarantee. Across these cases, “low rank” refers to different objects: data reconstruction, an adaptive direction, or a LoRA weight update in [language models](neural-sequence-language-models.md). The common algebra does not establish identical assumptions or historical joint use.
