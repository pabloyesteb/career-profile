---
id: impedance-aware-control-design
title: Formulate and integrate impedance-aware predictive control
concepts:
  - nonlinear-model-predictive-control
  - constrained-nonlinear-optimization
  - impedance-contact-dynamics
  - rigid-body-pose-kinematics
  - progress-triggered-recovery
evidence_refs:
  - ma6018:impedance-formulation
  - ma6018:impedance-in-prediction
  - ma6018:multirate-feedback
  - ma3503:constraint-optimality
  - ma3503:sqp-barriers
  - ma6018:pose-impedance
  - ma6018:contact-prediction
  - ma6018:reference-interpolation
  - ma6018:progress-projection
  - ma6018:recovery-state-machines
status: reviewed
---

# Formulate and integrate impedance-aware predictive control

## Supported mathematical and methodological activity

The thesis contribution explicitly includes formulating a tracking OCP with compliant feedback inside the prediction model, distinguishing optimized feedforward accelerations from the resulting wrench, and integrating the receding-horizon problem with multirate feedback execution. This captures analytical modeling and numerical-method selection as well as software integration—not merely familiarity with an MPC library.

The [canonical formulation](../concepts/nonlinear-model-predictive-control.md) retains dynamics, objective, constraints and representation choices. The [supporting claims](../evidence/ma6018.yaml) distinguish the user's formulation, implementation and multirate decision. They resolve to the thesis profile's Contribution boundary, Optimal control formulation, Numerical transcription and reference interpolation, and Computational architecture.

## Operating boundary

The completed thesis extraction adds a second layer of attributable capability: quaternion-aware reference interpolation, smooth measured-wrench prediction, geometric progress estimation and recovery state machines acting on the reference equilibrium. [Impedance/contact modeling](../concepts/impedance-contact-dynamics.md) explains the prediction assumptions; [progress recovery](../concepts/progress-triggered-recovery.md) explains the distinction between tracking and correcting task stagnation. These activities demonstrate model/interface reasoning and integration of known primitives, not invention of impedance or spiral search. Implemented-only adaptive extensions and reported experiment outcomes have separate attribution/verification limits.

The completed [constrained-optimization theory](../concepts/constrained-nonlinear-optimization.md) adds an educational basis for reasoning about KKT conditions, linearized-constraint feasibility, critical-cone curvature and SQP active sets. This strengthens the analytical interpretation of the implemented control formulation; it does not establish that every course theorem's hypotheses hold for the thesis solver or that the user authored acados/HPIPM. Personal implementation support remains the thesis claims, while MA3503 supplies theoretical knowledge.

Supported tools are CasADi/acados and HPIPM in a simulated Cartesian rigid-body assembly workflow. The offline robust planner, existing impedance law and numerical libraries are inherited building blocks. This competency does not assert proof of closed-loop robustness, comprehensive safety constraints, hardware deployment or hard-real-time execution.

The reported spiral-recovery result is not required to establish this formulation/integration activity; if retrieved for context, its classifier discrepancy and simulation limitations must remain visible. Public reuse must respect the thesis's disclosure qualification in [experiences.yaml](../experiences.yaml).
