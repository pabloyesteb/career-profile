---
id: "nonlinear-model-predictive-control"
title: "Impedance-aware nonlinear model predictive control"
domains:
  - "control-estimation"
  - "optimization"
  - "robotics-planning-geometry"
  - "numerical-mathematics"
evidence_refs:
  - "ma6018:impedance-formulation"
  - "ma6018:impedance-in-prediction"
  - "ma6018:multirate-feedback"
  - "ma6018:recovery-versus-prediction"
  - "ma6018:reference-interpolation"
  - "ma6018:contact-prediction"
  - "ma6018:runtime-study"
  - "ma6018:feedback-model-audits"
  - "tum-mobile-robotics:feedback-control"
status: "reviewed"
relations:
  - 
    type: "related_to"
    target: "progress-triggered-recovery"
---

# Impedance-aware nonlinear model predictive control

## Formulation

The thesis optimizes feedforward linear/angular accelerations \(u=(a_{ff},\alpha_{ff})\) with state \(x=(p,q,v,\omega)\), unit quaternion \(q\), perceived initial state \(\hat x\), and desired reference \(x_{d,k}\):
\[
\begin{aligned}
\min_{x_{0:N},u_{0:N-1}}\quad&
\sum_{k=0}^{N-1}\bigl(\|x_k-x_{d,k}\|_Q^2+\|u_k\|_R^2\bigr)
+\|x_N-x_{d,N}\|_{Q_f}^2\\
\text{s.t.}\quad&x_0=\hat x,\quad x_{k+1}=\Phi_h(x_k,u_k),\\
&u_{\min}\le u_k\le u_{\max}.
\end{aligned}
\]
Only the first optimized action is applied before replanning. The prediction includes impedance feedback:
\[
\dot p=v,\quad\dot q=\tfrac12[0,\omega]\otimes q,\qquad
\begin{bmatrix}\dot v\\\dot\omega\end{bmatrix}
=u+M^{-1}w_{imp}(x,x_d).
\]
The key modeling decision predicts a body already under compliant feedback, not one with an invisible downstream controller.

## Numerical/implementation structure

CasADi/acados direct multiple shooting uses SQP/Gauss–Newton and full-condensing HPIPM QPs. Two-stage Gauss implicit RK supplies the documented integration scheme. Reference interpolation adds a clock to the 13 mechanical components. Quaternion signs are aligned along the horizon; LINEAR_LS component residuals differ from relative-quaternion impedance errors.

Feedforward is held over a control interval while feedback is recomputed each physics substep. This is a documented multirate decision, not hard-real-time proof. [Control-design competency](../competencies/impedance-aware-control-design.md) records attributable formulation and integration.

The complete [transcription/reference interface](optimal-control-transcription.md) now records clock augmentation, interpolation grids, SLERP and increment-derived angular velocity, with the main solver/weight/limit settings. It contrasts this actual implicit-RK multiple shooting with the Case Studies team's Euler-defect/IPOPT planner, rather than treating all direct methods as interchangeable. [Impedance/contact modeling](impedance-contact-dynamics.md) retains wrench equations, measured-state initialization and implemented-only adaptive variants. Neither richer contact prediction nor longer preview enlarged the reported unrecovered successful set in the tested thesis configuration.

## Numerical evaluation and implementation interpretation

Mobile Robotics contributes a supplementary constrained-LQR/MPC teaching workflow and hill-driving QP example. This is a separate linear/model-based context, not evidence of another personally implemented impedance-aware NMPC. The distinction complements the new [policy-learning concepts](policy-optimization-geometry.md): optimizing a model-based horizon and updating a learned policy are not the same computation, even when both choose actions for future utility.

`ma6018:runtime-study` preserves mean solve times by preview separately from recovery/no-recovery medians and deadline-overrun counts; different statistics are not interchangeable speedup measurements. `ma6018:feedback-model-audits` retains the held/substep wrench-jump comparison and low-speed gyroscopic audit with their conditions. The audit supports interpreting a modeling choice, not a stability theorem. Structured values live in the [thesis evidence](../evidence/ma6018.yaml), together with the classification/simulation limits where applicable.

## Limits and evidence

Bounds constrain feedforward acceleration, not total wrench/joint torque. The base angular model omits the gyroscopic term; no general robustness, stability or recursive-feasibility proof follows. [Recovery](progress-triggered-recovery.md) and reported results remain separate from the OCP.

[Thesis claims](../evidence/ma6018.yaml) → [thesis](../../02_profiles/projects/thesis.md), Optimal control formulation, Numerical transcription and reference interpolation, Computational architecture and Controller, reference and recovery comparison. Experience simulation/disclosure limits also apply.
