---
id: optimal-control-transcription
title: Direct optimal-control transcription and numerical reference interfaces
domains: [optimization, numerical-mathematics, control-estimation, robotics-planning-geometry]
evidence_refs: ["cit413042:trajectory-models", "cit413042:rrt-initialization", "ma6018:reference-interpolation"]
status: reviewed
relations:
  - {type: related_to, target: rigid-body-pose-kinematics}
---

# Direct optimal-control transcription and numerical reference interfaces

## From trajectories to an NLP

The Case Studies formulation is
\[
\min_{x(\cdot),u(\cdot)}\int_0^T L(x,u)\,dt+E(x(T)),\quad
\dot x=f(x,u),\quad x(0)=x_0,\quad x(T)=x_g,
\quad g(x,u)\le0,\quad\Phi(q)>0.
\]
The state/control trajectories and path/endpoint constraints form a continuous problem. Direct methods discretize before optimizing; dynamic programming and Pontryagin-type indirect methods appear as background, not implemented HJB/costate solvers.

- Single shooting optimizes controls and integrates from the initial state, with sensitivity/initialization implications.
- Multiple shooting adds interval initial states and matching constraints, permitting independent state initialization.
- Collocation interpolates states, imposes derivative consistency/continuity and uses quadrature, producing a larger sparse NLP.

These structural comparisons are not universal runtime rankings. The project's actual runner uses state/control arrays with **forward-Euler defects**
\[
X_{k+1}=X_k+\Delta t\,f(X_k,U_k).
\]
The report's multiple-shooting label must not silently imply a higher-order integrator or an implemented collocation solver.

## Objective and admissibility details

The checked path objective is
\[
J=\sum_{k=0}^{N-1}\sqrt{\|p_{k+1}-p_k\|_2^2+10^{-8}}
+\rho\sum_ks_k^2+\lambda_u\sum_{k\in\mathcal I}\|U_k\|_2^2,
\quad s_k\ge0,\quad\mathcal I=\{0,\ldots,N-2\}.
\]
Slack/input terms are optional. The named smoothing option penalizes input magnitude, not jerk or successive differences, and omits the final input in this revision. Time \(N\Delta t\) is fixed, not optimized. Terminal heading may be free while other terminal states are fixed. Relaxation changes admissibility; it is not a proof of collision avoidance.

## A different discretization in receding-horizon control

The thesis uses CasADi/acados direct multiple shooting, SQP/Gauss–Newton, full-condensing HPIPM and two-stage Gauss implicit RK: one integration step per interval, the fourth-order A-stable scheme discussed in the profile. This is separate from Case Studies' Euler/IPOPT stack. The thesis adds \(\dot\theta=1\) as an interpolation clock, reset per solve, giving fourteen base-state components. Linear position/velocity interpolation and quaternion SLERP reconcile planner nodes (101 at 0.04 s) with the controller/integration grids. Angular reference velocity comes from the quaternion increment, not unrelated angular-rate interpolation.

The main NMPC operating point has 0.5 s preview/20 intervals, nominal 25 ms control, state weights \(I_3,I_4,0.1I_3,0.1I_3\), input weight \(0.01I_6\), and feedforward limits 5 m/s² and 5 rad/s². Multirate feedback at 34 physics substeps of 0.73 ms advances 24.82 ms, not exactly 25 ms. These parameter/interface choices are not hard-real-time guarantees.

## Evidence and interpretation

The reusable issue is alignment of variables, defect constraints, interpolants and solver derivatives. A feasible discrete trajectory does not establish continuous swept-volume safety; a converged NLP does not establish robust execution under a biased state. [Case Studies evidence](../evidence/cit413042.yaml) is team-level; [thesis evidence](../evidence/ma6018.yaml) establishes personal model/solver integration, not authorship of the inherited planner or external solvers. See [NMPC](nonlinear-model-predictive-control.md) and [constrained optimization](constrained-nonlinear-optimization.md).
