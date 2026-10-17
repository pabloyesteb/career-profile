---
id: state-feedback-observers
title: State feedback, observers and disturbance-rejection architectures
domains: [control-estimation, dynamical-systems, robotics-planning-geometry]
evidence_refs: ["tum-advanced-control:feedback-architectures", "tum-advanced-control:nonlinear-tools", "in2138:uncertain-mapping", "tum-mobile-robotics:estimation-mapping", "tum-mobile-robotics:feedback-control"]
status: reviewed
---

# State feedback, observers and disturbance-rejection architectures

## Model and control structure

Supplementary Advanced Control organizes design around nonlinear equilibrium linearization and LTI models
\[
\dot x=Ax+Bu+Ez,\qquad y=Cx.
\]
State, control, disturbance and measured output have distinct roles. Feedforward/feedback and two-degrees-of-freedom architectures separate reference generation from disturbance correction. Equilibrium stability, eigenvalue criteria, BIBO stability, phase portraits, state-transition solutions and time/frequency descriptions provide complementary viewpoints. Invariant zeros via the Rosenbrock matrix must not be conflated with transmission zeros.

State-feedback coverage includes Kalman controllability, canonical forms/transformations, Ackermann's SISO formula, Gilbert/Hautus tests and parametric MIMO eigenvector freedom. Here **Ackermann's pole-placement formula** is distinct from **Ackermann steering kinematics** in the vehicle project. LQR provides a weighting-based alternative to pole assignment. The profile names these design methods but does not supply Riccati equations or full stabilizability/detectability hypotheses; no unsupported theorem/derivation is introduced.

## Estimation, tracking and internal dynamics

Luenberger observers, observability/canonical forms, controller–observer duality, coefficient matching and the separation principle lead into a short Kalman introduction and MIMO decoupling. The source specifically flags unobservability and inversion/zero structure as design limitations. A named separation principle is not a proof for every nonlinear or constrained architecture.

Disturbance rejection covers constant/piecewise-constant disturbance models, disturbance-decoupling conditions, parametric decoupling, dynamic compensation and integral action. Combined architectures use dynamic reference feedforward, state feedback, integral action and observers. Nonlinear input–output linearization adds relative degree and zero dynamics: apparently linear external behavior does not settle internal behavior. An elastic robot-arm exercise includes coupled inertias, gravity and torsional elasticity.

## Filtering and mapping: a second source and a different scope

The accredited IN2138 syllabus names Kalman filtering for linear Gaussian models, EKF for nonlinear models, UKF for strongly nonlinear models, and Bayesian/particle filtering for arbitrary uncertainty, with SLAM coupling mapping/localization. These are the syllabus's coverage descriptions, **not universal rankings or guarantees** for arbitrary nonlinear/distributional problems. It supplies no recursion equations, noise assumptions beyond that outline, or convergence statements. Those details remain unavailable at profile depth. The Summer Semester 2024 edition is not proof of the user's attendance term.

## Computational examples and provenance

Supplementary Mobile Robotics adds PID/anti-windup, reference filtering/feedforward and LQR/MPC, including quadrotor input remapping, cascades, hover assumptions and imperfect loop decoupling. Its supplied hill-driving Python separates `LqrController`, `MpcController` and simulation and calls `qpsolvers.solve_qp`; exact QP contracts are not available at profile depth. These are represented examples, not personal implementation. [Nonlinear estimation/mapping](probabilistic-slam-mapping.md) now deepens the earlier filtering name map through residual-based and recursive approaches without importing absent equations into IN2138.

Advanced Control supplies MATLAB/Simulink material, including a three-tank linearized three-state/two-input workflow: `lqr(A,B,Q,Q_t)`, eigenvalues of `A-B*R`, `ss` and `lsim`. Here `R` is the script's feedback gain symbol, not an inferred universal input-weight convention. Paths also identify cart–pendulum Euler–Lagrange derivation, numerical pole placement, Roppenecker-style feedback, decoupling and disturbance-observer/dynamic-feedforward packages; their internals were not fully extracted upstream.

This is supplementary content with unspecified learning relationship, not accredited completion or personal simulation. [Advanced Control evidence](../evidence/tum-advanced-control.yaml) retains deeper-extraction limits. [IN2138 evidence](../evidence/in2138.yaml) independently establishes syllabus knowledge, not personal filtering/SLAM implementation. Connections to the thesis's feedback and multirate execution are conceptual, not an assertion that it implemented LQR or a Kalman observer.
