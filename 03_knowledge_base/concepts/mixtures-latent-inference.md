---
id: mixtures-latent-inference
title: Latent mixtures, EM and clustering objectives
domains: [probability-statistics-uq, machine-learning, optimization]
evidence_refs: ["ma4802:mixtures", "cit4230003:variational-inference", "additional-foml:composite-methods"]
status: reviewed
relations:
  - {type: related_to, target: nonconvex-geometric-optimization}
  - {type: related_to, target: variational-generative-inference}
---

# Latent mixtures, EM and clustering objectives

## Responsibilities and constrained updates

Mixtures combine component densities with nonnegative weights summing to one; Gaussian and product-Bernoulli examples distinguish a hidden assignment from the observation. Posterior responsibilities give soft assignments, while maximum-responsibility labels give hard clustering. Density approximation, uncertainty/outliers and compression are not automatically meaningful class discovery.

EM computes the expected complete-data log-likelihood \(Q(\theta,\theta_{old})\) then maximizes it, optionally with a log prior for MAP. GMM weights/means/covariances use responsibility-weighted counts/moments, respecting covariance/weight constraints. Exact E/M improvements monotonically increase observed likelihood; local maxima and saddles remain possible. A generic unconstrained optimizer does not automatically preserve the model's feasible parameters.

## Different views of the same alternating structure

Deep Generative Models interprets EM as ELBO coordinate ascent: improve posterior inference for fixed model, then model parameters for fixed inference distribution. Restricting to a variational family changes tightness/correlation capacity. FOML gives an MM/auxiliary-majorizer interpretation and compares alternating minimization for NMF least-squares/KL objectives, CCCP/DC decompositions, Sinkhorn scaling and determinantal-kernel learning. Monotone objective progress is not global optimality or identical update formulas across these problems.

k-means/Lloyd arises from hard assignments with equal isotropic covariance/weights: nearest centers then cluster means, with assignment cost \(O(NKD)\). Hierarchical clustering is only a contrasting similarity-tree overview, not a fully specified linkage method. Old Faithful GMM/KDE and unequal-spread synthetic clusters expose different density/partition behavior; elbow curves investigate component count.

Evidence: [MA4802](../evidence/ma4802.yaml), [generative models](../evidence/cit4230003.yaml) and [FOML](../evidence/additional-foml.yaml). Exact GMM update matrices, auxiliary constructions and all likelihood-regularity hypotheses absent from these profiles are not reconstructed. [Variational generation](variational-generative-inference.md) and [factor/independence models](latent-factors-independent-components.md) preserve related but different latent assumptions.
