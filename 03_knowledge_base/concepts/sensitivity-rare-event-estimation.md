---
id: sensitivity-rare-event-estimation
title: Global sensitivity and rare-event simulation
domains: [probability-statistics-uq, numerical-mathematics]
evidence_refs: ["ma6015:sensitivity", "ma6015:rare-events"]
status: reviewed
---

# Global sensitivity and rare-event simulation

## Which uncertainty question is being asked?

Estimating a mean, attributing output variance to inputs and measuring a rare failure probability are different tasks. They can use related simulation models without sharing a statistical guarantee. The seminar provides both global-sensitivity and rare-event methods; these are taught research topics, not personally implemented pipelines.

## Variance decomposition and multifidelity sensitivity

Functional ANOVA/HDMR decomposes output into main and interaction effects over **independent inputs**. Sobol main-effect indices measure the component attributable to one input alone; total effects include interactions containing that input. Conditional-variance representations and Owen estimators support the source's sensitivity estimation. Independence is material: the same decomposition must not be transferred unchanged to arbitrary dependent-input models.

MFMC uses high-fidelity outputs and correlated cheaper models to estimate mean, variance and Sobol components. Surrogate correlation, cost ordering, control coefficients and nested sample ratios jointly determine utility. The Ishigami function supplies an analytic benchmark; a 2D hydrogen-combustion convection–diffusion–reaction model with uncertain reaction parameters demonstrates an expensive PDE setting. The profile reports no numerical Sobol values or personal runtime gains; none are supplied here.

## Rare probabilities and conditional simulation

For failure event \(F\), crude MC estimates \(P_F=\mathbb E[1_F]\) with variance
\[
\operatorname{Var}(\widehat P_F)=P_F(1-P_F)/N.
\]
Thus fixed relative precision becomes expensive as \(P_F\) decreases: sample requirements scale inversely with the rare probability. Absolute error and relative error are not interchangeable measures.

Subset simulation replaces a rare event by nested less-extreme domains and a product of conditional probabilities. Adaptive thresholds aim to maintain usable conditional probabilities; Metropolis–Hastings-type chains sample the conditional distributions. Dependence/burn-in must remain part of the interpretation rather than importing iid MC uncertainty formulas uncritically.

Multilevel failure domains combine thresholds with resolution changes and may be **nonnested**. Repeated Bayes factorization then needs forward and reverse conditional probabilities. The represented MLE analysis gives relative bias and variance \(O(N^{-1})\) under its assumptions; it also exposes fine-level burn-in and fixed high-dimensional field costs. MLE-var increases both physical resolution and KL dimension, seeding chains from prior failure samples and adding/discarding Gaussian coordinates as required. More efficient coarse representations require additional cross-level bookkeeping.

The flow-cell example uses lognormal permeability, KL expansion, lowest-order Raviart–Thomas mixed FEM and an outflow threshold. Empirical distributions/cost compare subset simulation, MLE and MLE-var; exact quantitative outcomes are not in the source profile. Extrapolation to operational reliability or actuarial systems would be a potential application, not a demonstrated deployment.

## Connections and evidence

[Multilevel allocation](multilevel-multifidelity-estimation.md) supplies the error–cost viewpoint, while [random-field representations](random-fields-sampling.md) control input complexity. Sensitivity identifies which uncertain inputs matter; rare-event methods resolve a tail event. Neither one proves the validity of NGValidation prediction intervals or the thesis success classifier.

Evidence: `ma6015:sensitivity` and `ma6015:rare-events` in [seminar evidence](../evidence/ma6015.yaml), P7/P12 sections of the [profile](../../02_profiles/courses/ma6015-advanced-seminar-course.md). Missing advertised seminar papers are not reconstructed.
