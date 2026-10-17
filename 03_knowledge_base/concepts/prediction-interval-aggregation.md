---
id: "prediction-interval-aggregation"
title: "Residual prediction intervals, calibration and aggregation"
domains:
  - "probability-statistics-uq"
  - "machine-learning"
  - "scientific-software-data-engineering"
evidence_refs:
  - "scientific_paper:paper-interval-intersection"
  - "scientific_paper:widest-interval-code"
  - "scientific_paper:calibration-method"
  - "scientific_paper:binned-coverage-code"
  - "scientific_paper:residual-methods"
  - "scientific_paper:bootstrap-quantiles"
  - "scientific_paper:coverage-intervals"
status: "reviewed"
---


# Residual prediction intervals, calibration and aggregation

## Conditional uncertainty context

The profile distinguishes marginal global residual uncertainty (GUM), predicted-output-conditioned models (oMUM) and per-input models (iMUM). Empirical marginal calibration is not a distribution-free conditional guarantee.

## Published intersection

The paper proposes
\[
\mathrm{FUM}=\mathrm{GUM}\cap\mathrm{oMUM}
\cap\left(\bigcap_{j=1}^{n}\mathrm{iMUM}[j]\right).
\]
An intersection narrows constituent intervals and may reduce coverage. The profile does not endorse the printed characterization as most conservative. Constituent illustrations do not establish full-intersection/simultaneous multi-output coverage.

## Code variant

The code uses nanargmax of candidate widths to select the widest interval for each sample/output. For notation \(I_k=[a_k,b_k]\), this selects the candidate with maximum \(b_k-a_k\); it is not the paper's intersection. Selecting one interval is not automatically a union/envelope or calibration guarantee.

This library-level implementation has individual authorship unspecified. The 2023 snapshot is not established as the exact 2025 experimental version.

## Evidence and gaps

[Contrasting paper/code claims](../evidence/scientific_paper.yaml) → [NGValidation](../../02_profiles/projects/ngvalidation.md), 11. Calibrated multiscale prediction intervals — node 10, Material mathematical/notation cautions found during validation and Uncertainty modeling and paper/code distinctions. Distinct scoped claims preserve disagreement instead of silently correcting sources.

The completed extraction below includes binning, calibration and reported constituent coverage; exact unpublished settings remain unavailable.

## Residual signs and three independent data roles

Training fits the ANN; calibration estimates residual distributions/quantiles; independent validation measures interval inclusion. With signed residual \(e=y-\hat y\), residual bounds give
\[
[\hat y+q_{\rm low},\hat y+q_{\rm high}].
\]
Writing a positive lower width instead requires \(\epsilon_1=-q_{\rm low}\). The printed paper's lower-width wording is ambiguous; the source profile's sign clarification is retained.

Global GUM uses marginal \(P(e)\); oMUM conditions on predicted output available at inference; iMUM supplies separate input-variable-conditioned models, not a fully joint high-dimensional conditional model. The text's true-output versus predicted-output conditioning is not interchangeable.

## Quantile estimation versus prediction coverage

Bootstrap resampling estimates uncertainty of residual quantiles. The earlier 5th/95th-percentile example has estimates −0.0432/+0.0448 and reordered bootstrap ranges [−0.0548,−0.0353] / [0.0379,0.0586]; rounded midpoint offsets produce \([\hat y-0.045,\hat y+0.048]\) at intended **90%** coverage. That is not the later **95%** interval-validation illustration and does not establish finite-sample coverage or superior midpoint accuracy.

For nominal 95%, Figure 17 reports bootstrap CI95 endpoints for measured constituent coverage: GUM [94.63,95.44]%, oMUM [94.77,95.56]%, one-load iMUM [94.68,95.09]%. These are confidence endpoints, not exact coverage point estimates. Counts/bootstrap repetition settings are undisclosed. Inclusion of nominal 95% in a CI differs from establishing true coverage at least 95%; marginal observations do not imply exact conditional or simultaneous all-output coverage.

## Implemented binning and coverage options

The repository's `BinnedUncertaintyModel` uses equal-spaced numerical bins/categorical groups, one-/two-tailed quantiles, calibration masks and lookup. Global is a single-bin case. `ModelCoverage` supports exact and Wilson binomial proportion intervals and bootstrap coverage; the inspected default is `exact`, not necessarily the article's bootstrap choice.

The widest-interval code and paper intersection above remain different procedures; neither inherits these constituent validation results automatically. [Residual diagnostics](residual-statistical-diagnostics.md) explains heteroscedasticity/tails and the separate Johnson transform discrepancy. The 2023-code/2025-paper boundary prevents treating code defaults as a reconstructed experimental specification.
