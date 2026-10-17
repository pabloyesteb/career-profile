---
id: "surrogate-domain-split-validation"
title: "Surrogate applicability, geometric coverage and split validation"
domains:
  - "probability-statistics-uq"
  - "machine-learning"
  - "optimization"
  - "aerospace-engineering"
evidence_refs:
  - "scientific_paper:domain-split-method"
  - "scientific_paper:domain-code"
  - "scientific_paper:engineering-context"
status: "reviewed"
---

# Surrogate applicability, geometric coverage and split validation

## Engineering risk determines what validation must examine

NGValidation's supervised aerostructural map predicts six reserve factors from 26 load/maneuver inputs for skin/stringer panels: forced crippling, column buckling, in-plane, net tension, pure compression and shear-panel failure. Outputs in [0,5] are continuous risk-related engineering quantities; no conversion to calibrated failure probability is supplied. One PFI illustration uses 22 features without explaining its relation to 26. Data are restricted, and exact split counts/feature identities are unavailable.

The ten-node workflow connects preparation, split auditing, training, residual diagnostics, explanation, refinement and calibration. It contributes evidence **toward** assurance, not achieved regulatory certification. High average fit is not sufficient operating-domain coverage.

## Geometry and preprocessing

Frame location can be ordinal; periodic stringer position uses \((\cos\theta_k,\sin\theta_k)\), \(\theta_k=2\pi k/q\), preserving wraparound adjacency. Fit normalization/PCA on training only, then apply unchanged to held-out data. Latin-hypercube/space-filling design and multifidelity/input uncertainty are guidance, not a documented full data-generation procedure.

A scalar uncertainty-augmentation example draws \(q\) input and \(q\) output values and forms \(q^2\) pairs under independence; known covariance can change sampling. Perturbed replicas are assumed-uncertainty representations, not new physical coverage.

## Voxel tessellation and proximity (VTPM)

The paper's voxels are **categorical-feature combinations**, not a regular continuous grid:

1. Group training cases categorically; unmatched test combinations enter a residual voxel.
2. More than 5% residual-voxel test points rejects adequacy; otherwise compare categorical frequencies using a two-sample chi-square test at 0.05.
3. Within each represented voxel, compare test-to-nearest-training distance against the distribution of training nearest-neighbor distances.
4. Distances between the 2.5th/97.5th percentile bounds count as valid; lower ones flag excessive proximity, higher ones isolation.
5. At least 95% valid points passes the stated criterion.

The illustration has about 800 voxels and reports more than 95% valid test points, without an exact fraction/test statistic. Nonrejection does not prove identical distributions; the paper's “p-hacking” label is a proximity flag, not evidence of misconduct. Distance metric, ties and sparse-voxel policy are incompletely specified.

## Hull membership as a numerical feasibility problem

Convex-hull containment is a geometric diagnostic, not a necessary-and-sufficient neural generalization theorem; interior holes remain possible. The repository implements membership by finding
\[
w_i\ge0,\qquad\sum_iw_iv_i=x,\qquad\sum_iw_i=1
\]
with zero-objective SciPy `linprog(method='highs-ds')`. This is a concrete LP representation, not individual authorship of the routine. It connects [convex geometry](convex-conjugacy-sparse-optimization.md) and numerical optimization with statistical domain auditing.

The code's split template also checks within-voxel coordinate ranges, test-neighbor versus that neighbor's training-neighbor distance, staged PCA99/ambient hulls and one-sided Mann–Whitney proximity comparison. This 2023 implementation is not asserted identical to the paper's 2025 percentile/chi-square procedure; PCA-index/small-voxel numerical behavior was not independently tested.

## Applicability and personally supported engineering

Coordinate-range, convex-hull and error-exceedance-classifier layers offer increasingly specific applicability guards, not accuracy certificates. Rare large-error classification is a proposed guard, not a measured deployed detector. Latent-space hulls and targeted acquisition are alternatives with their own representation assumptions.

The personal split-template changes add numerical-only/dummy-category single-voxel handling, explicit train copies and reporting/requirements corrections; the broader algorithms remain collaborative/library context. The same [validation workflow capability](../competencies/validation-data-workflows.md) is supported by concrete edge-case handling rather than a new generic certification claim.

[NGValidation claims](../evidence/scientific_paper.yaml) distinguish paper methodology, code and attributable changes. Restricted data, incomplete experimental version mapping and high-dimensional geometric limitations remain attached.
