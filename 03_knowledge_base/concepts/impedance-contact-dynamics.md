---
id: impedance-contact-dynamics
title: Cartesian impedance and smooth contact-wrench prediction
domains: [control-estimation, robotics-planning-geometry, dynamical-systems]
evidence_refs: ["ma6018:pose-impedance", "ma6018:contact-prediction", "ma6018:adaptive-model-extensions"]
status: reviewed
relations:
  - {type: related_to, target: nonlinear-model-predictive-control}
  - {type: related_to, target: state-feedback-observers}
---

# Cartesian impedance and smooth contact-wrench prediction

## Compliance through reference errors

For perceived state \(\hat x\) and desired state \(x_d\), the thesis uses
\[
w_{imp}=\begin{bmatrix}
D_p(v_d-\hat v)+K_p(p_d-\hat p)\\
D_o(\omega_d-\hat\omega)+2\eta_eK_o\epsilon_e
\end{bmatrix},\qquad
\hat q^{-1}\otimes q_d=(\eta_e,\epsilon_e).
\]
Stiffness converts pose error into restoring wrench; damping attenuates relative motion. The diagonal design uses \(K_p=k_pI\), \(K_o=k_oI\) and \(D=2\zeta\sqrt{KM}\). The orientation error is geometric rather than a four-coordinate subtraction. Ideal fixed-reference energy/passivity reasoning is a theoretical foundation; it does not prove stability of the moving-reference MPC/recovery architecture.

The operating point uses 50 N/m translation stiffness, 5 Nm/rad rotation stiffness and damping ratio 0.7. The modeled part has mass approximately 0.666 kg and principal inertias approximately \([2.42,2.38,0.36]\times10^{-3}\) kg m². These are simulation settings, not identified universal robot parameters. The feedback law is an existing building block; the personal contribution is its integration into prediction/execution and investigation under pose bias.

## Contact wrench as an augmented prediction state

The evaluated extension adds \(\lambda=(\lambda_f,\lambda_\tau)\):
\[
\begin{bmatrix}\dot v\\\dot\omega\end{bmatrix}
=u+M^{-1}(w_{imp}+\lambda),\qquad
\dot\lambda_f=-b_{env}v,\quad
\dot\lambda_\tau=-b_{env,o}\omega.
\]
Measured wrench initializes each solve. An external wrapper switches between free/contact predictors using wrench norm; switching is outside the smooth OCP. The augmented state has nineteen mechanical/wrench components, twenty with the interpolation clock. Target settings include threshold 0.001, stiffness coefficients 266.31/0.14489, zero wrench cost weights and wrench-state bound 500; the source profile does not establish physical units for each of these configuration entries.

This is a local elastic belief, not contact-topology inference, unilateral contact enforcement or friction-cone optimization. Setting stiffness coefficients to zero still retains initialized wrench as a constant disturbance. The reported failure to improve insertion is conditional on this model/setup, not a rejection of all contact-aware MPC.

## Implemented extensions versus evaluated findings

The source additionally documents local stiffness fitting
\[
\Delta\Lambda\approx-K\Delta P,\qquad
K=-\Delta\Lambda\Delta P^T(\Delta P\Delta P^T+\rho I)^{-1},
\]
with regularization \(\rho\), followed by symmetrization and PSD eigenvalue clipping. Normal-oriented/anisotropic costs and planar-normal, unilateral, Han-style and adaptive variants also exist. These establish implemented exploration, **not** principal validated improvements. The main experimental contact controller remains the isotropic wrench-state model.

This links model structure, local identification and predictive control. It does not establish an operational contact estimator or closed-loop robustness theorem. [Thesis evidence](../evidence/ma6018.yaml) separates the inherited impedance foundation, attributable contact implementation and implemented-only extensions. See [pose conventions](rigid-body-pose-kinematics.md) and [NMPC](nonlinear-model-predictive-control.md) for their interfaces.
