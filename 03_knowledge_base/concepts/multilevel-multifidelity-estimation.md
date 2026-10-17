---
id: multilevel-multifidelity-estimation
title: Monte Carlo, multilevel and multifidelity error–work allocation
domains: [probability-statistics-uq, numerical-mathematics, optimization]
evidence_refs: ["ma5348:mc-multifidelity", "ma5348:teaching-code", "ma6015:mlmc-foundations", "ma6015:finite-volume-cgv", "ma6015:hierarchy-optimization", "ma6015:blue-multifidelity", "ma6015:p2-presentation"]
status: reviewed
relations:
  - {type: related_to, target: sensitivity-rare-event-estimation}
  - {type: related_to, target: stochastic-pde-discretization}
---

# Monte Carlo, multilevel and multifidelity error–work allocation

## Separate stochastic error from numerical bias

For independent Monte Carlo samples of a discretized quantity \(Q_L\), the profile's error separation is expressed as
\[
\mathbb E[(\widehat Q_L-\mathbb E Q)^2]
=\operatorname{Var}(Q_L)/N+(\mathbb E Q_L-\mathbb E Q)^2.
\]
This scalar identity is the sampling-variance/discretization-bias decomposition represented by the sources, not a guarantee for dependent samples. Hilbert-valued and field expectations extend the setting with corresponding norm/integrability conditions. Confidence intervals need their sampling assumptions; dimension-independent MC sampling rate does not imply dimension-independent forward-model work.

Antithetic and control variates reduce variance through dependence structure. Control coefficients depend on covariance, which may need pilot estimation. Gaussian/Clenshaw–Curtis quadrature, tensor/sparse grids and quasi-MC are alternative integration strategies, with smoothness/dimension dependence distinct from crude MC; the profile does not supply their full rate theorems.

## Telescoping MLMC and its hypotheses

Set \(Y_0=Q_0\), \(Y_\ell=Q_\ell-Q_{\ell-1}\). Then
\[
\mathbb E Q_L=\sum_{\ell=0}^L\mathbb E Y_\ell,
\qquad \widehat Q^{ML}=\sum_{\ell=0}^L\frac1{N_\ell}\sum_{n=1}^{N_\ell}Y_\ell^{(n)}.
\]
Fine/coarse evaluations within a correction must use the **same random input** to exploit correlation; independent averaging across level estimators gives the represented variance budget. Samples are allocated proportional to \(\sqrt{V_\ell/C_\ell}\), with \(V_\ell\) correction variance and \(C_\ell\) sample cost. Bias controls the finest resolution; variance controls sampling. Last-correction bias estimates require the modeled asymptotic behavior, not blind extrapolation.

With bias exponent \(\alpha\), correction-variance exponent \(\beta\), work exponent \(\gamma\), and compatibility \(\alpha\ge\min(\beta,\gamma)/2\), the seminar states work to RMS tolerance \(\varepsilon\):
\[
\begin{cases}
O(\varepsilon^{-2}),&\beta>\gamma,\\
O(\varepsilon^{-2}(\log\varepsilon)^2),&\beta=\gamma,\\
O(\varepsilon^{-2-(\gamma-\beta)/\alpha}),&\beta<\gamma.
\end{cases}
\]
These regimes follow the profile's consistent P1/P2 account. P3's reversed generic labels are explicitly not used. P2 connects FEM regularity to these rates, while the finite-volume random-layer setting has different bounds.

## Optimize the hierarchy, not only the sample count

P4 optimizes number of levels, mesh sizes and counts under a probabilistic tolerance. A split \(\theta\) separates bias/statistical budgets; a Lindeberg–Feller approximation introduces a Gaussian quantile. Bias \(Q_Wh_L^{q_1}\), variance \(Q_Sh_{\ell-1}^{q_2}\), and cost \(h_\ell^{-d\gamma}\) models yield a relaxed continuous allocation before integer implementation. Log-mesh optimality conditions distinguish \(\chi=q_2/(d\gamma)=1\) from other cases, with \(\eta=q_1/(d\gamma)\).

Optimized geometric refinement can share general hierarchies' asymptotic work; choosing \(\theta\) can matter more practically than nongeometric meshes in the presented studies. These are reported seminar findings, not personal speedups. Continuation MLMC, GMRES and MUMPS examples show why solver costs change the allocation problem. Coarse-grid variates exploit stationarity: average the \(2^d\) valid coarse subvectors of a fine coefficient sample, preserving expectation while reducing correction variance. Its roughly-less-than-twofold correction cost is setting-specific, not a universal bound.

## Correlated model families and BLUE

MFMC uses cheap correlated surrogates as control variates with nested sample counts. Correlation/cost ordering determines useful model selection, coefficients and ratios; poor correlation or allocation can erase savings. A lower-fidelity model is not automatically a useful control variate.

MLBLUE allows arbitrary jointly sampled groups. With block model \(Y=H\mu+e\), generalized least squares/Gauss–Markov–Aitken yields the BLUE. For information matrix \(\Psi\), a scalar target \(a^T\mu\) has variance \(a^T\Psi^{-1}a\) under the stated invertibility/covariance conditions. Reused data for covariance estimation can bias weights; independent pilots cost evaluations. SAOB optimizes allocation under a budget and coupling-group limit, potentially among \(2^L-1\) groups. Even infinitely many cheap evaluations leave a nonzero variance lower bound with fixed high-fidelity sample count in the presented setting. This unifies MC/MLMC/CV/MFMC/approximate CV without claiming identical computational complexity.

## Applications and evidence

Darcy pressure/outflow, random elliptic PDEs, a random-initial-condition Euler IVP and a geometric-Brownian-motion option payoff illustrate estimator design. Numerical UQ supplies MATLAB MC/two-level intervals and empirical MLMC-rate exercises; the seminar supplies theoretical comparisons, not participant solver submissions. [Sensitivity/rare events](sensitivity-rare-event-estimation.md) target different statistics with related budget reasoning.

Evidence: [MA5348](../evidence/ma5348.yaml) and [MA6015](../evidence/ma6015.yaml); `ma6015:p2-presentation` supports personal mathematical explanation, not authorship of these research methods or reproduced benchmark gains.
