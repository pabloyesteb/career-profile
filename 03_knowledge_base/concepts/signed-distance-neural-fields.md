---
id: signed-distance-neural-fields
title: Signed-distance geometry and learned implicit fields in optimization
domains: [robotics-planning-geometry, machine-learning, optimization, scientific-software-data-engineering]
evidence_refs: ["cit413042:distance-fields", "cit413042:neural-training", "cit413042:siren-implementation", "cit413042:representation-background"]
status: reviewed
---

# Signed-distance geometry and learned implicit fields in optimization

## Geometric meaning and approximations

An SDF is negative inside obstacles, zero at their boundary and positive outside. In Case Studies, analytic circle/square distances and Shapely polygon boundary/inside tests supply reference geometry. Obstacle unions use the minimum of individual fields. Smooth absolute/min/max/clamp functions and log-sum-exp soft minima make symbolic surrogates easier to differentiate, but can change the zero contour. An exact distance, smoothed analytic field and learned regressor are not interchangeable.

Footprint constraints query \(\Phi(p_k+R(\theta_k)v_j)+s_k\ge m\) at transformed local vertices. Code permits zero margin and slack, unlike a strictly positive-clearance conceptual statement. A single environment network still requires many node/footprint queries; fewer explicit obstacle descriptions do not imply one scalar constraint for a whole trajectory. Point-geometry slack handling and discrete collision sampling also limit safety claims.

## Data, network and differential loss

Supervised inputs are planar coordinates, targets reference signed distances. Uniform grids, uniform random points and boundary-informed mixtures trade near-contour detail against global coverage. The principal reported learner is a two-hidden-layer, typically width-128 ReLU MLP; sigmoid/smaller ReLU comparisons and trainable-cosine Fourier-feature MLPs appear separately.

Pablo's attributable SIREN implementation uses
\[
h^{\ell+1}=\sin(\omega_0(W_\ell h^\ell+b_\ell)),
\]
with a linear output. Initial bounds are \(\pm1/n_{in}\) in the first sine layer and \(\pm\sqrt{6/n_{in}}/\omega_0\) later, default frequency 30. This implements a published architecture; the shared trainer can reinitialize linear layers, so architecture-defined initialization is not automatically preserved in every route. SIREN/Fourier availability does not establish that they produced the main report benchmarks.

The implemented training objective is
\[
\mathcal L=\frac1M\sum_i(h_\vartheta(q_i)-d_i)^2
+\lambda_s\mathcal L_s
+\lambda_e\frac1M\sum_i(\|\nabla_qh_\vartheta(q_i)\|_2-1)^2.
\]
Autograd supplies the Eikonal gradient penalty; the report's displayed formula differs. The coded surface term uses predicted values at reference near-zero samples; reversing the evaluated surface gives a different measure. Training uses PyTorch DataLoader/Adam, a 10% validation split and patience/minimum-improvement early stopping with best-state restoration. Defaults include 200,000 samples, batch 256 and learning rate \(10^{-3}\), overridable by configuration. Validation excludes Eikonal loss. Code uses Kaiming uniform despite a Xavier comment; a positional sampling-argument mismatch prevents assuming exact reproduction of requested boundary fractions.

## Solver interface and alternative representations

L4CasADi connects PyTorch field evaluation/derivatives to CasADi Opti/IPOPT. ReLU is piecewise differentiable, not globally twice smooth; a neural field is not automatically a smooth Hessian oracle. Generated C++/TorchScript/binary products are toolchain artifacts, not individually authored solver evidence. Team integration and personal SIREN/model-selection contributions are separately recorded.

The corridor also uses convex trapezoids approximating four half-elliptical rings. Appendix alternatives include conic-duality collision avoidance (dual-cone/norm separation and penalized penetration), TT-SVD compression of voxelized **truncated** SDFs, and Bernstein-polynomial fields. The latter normalize coordinates to \([0,1]\), use nonnegative partition-of-unity tensor-product bases, least-squares fitting and analytically scaled derivatives. A normal-equation inverse needs full column rank; recursive least squares is mentioned, and minima across link fields can still be nonsmooth. These alternatives are reviewed background, not implemented benchmark replacements.

## Technical connection and evidence

Distance-field learning exposes geometry to an optimizer; graph learning exposes geometry/topology to a pressure predictor. The shared theme is a scientific representation and a correct numerical interface, not identical architectures or safety guarantees. See [geometric validation](geometric-field-validation.md), [SVD](matrix-low-rank-pca.md) and [trajectory transcription](optimal-control-transcription.md).

Evidence: [Case Studies claims](../evidence/cit413042.yaml) → both profiles' SDF/training/appendix sections. Personal `SineLayer`/`SIREN` implementation resolves to commit `717a0f367a4b1d4392643031a8f1b2e8ab5bbd5b`; team experimental results are separate.
