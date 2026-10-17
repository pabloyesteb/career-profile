---
id: rigid-body-pose-kinematics
title: Pose representations, rigid-body states and planar robot kinematics
domains: [robotics-planning-geometry, dynamical-systems, numerical-mathematics]
evidence_refs: ["ma6018:pose-impedance", "ma6018:reference-interpolation", "cit413042:trajectory-models", "tum-mobile-robotics:representations-tools"]
status: reviewed
relations:
  - {type: related_to, target: signed-distance-neural-fields}
---

# Pose representations, rigid-body states and planar robot kinematics

## State coordinates are part of the model

The thesis represents a free, fully actuated rigid part by
\[
x=(p,q,v,\omega)\in\mathbb R^3\times S^3\times\mathbb R^6.
\]
The pose belongs to \(SE(3)\); the scalar-first quaternion stores four coordinates subject to unit norm, giving thirteen mechanical components. This task-space body is not a joint-space arm. Perception bias is composed at every controller observation:
\[
\mathcal P_q((p,q),(\delta p,\delta q))
=(p+R(q)\delta p,\;q\otimes\delta q).
\]
Thus translational bias rotates with the current attitude; it is not merely an initial physical displacement. True, perceived and reference states play different roles in control and evaluation.

Quaternion inversion/composition, relative errors and antipodal equivalence matter numerically. The thesis aligns reference signs before least-squares comparison, interpolates orientation by shortest-arc SLERP with small-angle handling, and derives stage angular velocity from the quaternion increment using an atan2 axis-angle calculation divided by stage duration. Component residuals in the optimizer are different from the relative-quaternion error in impedance feedback. A representation convention must remain consistent across dynamics, interpolation and costs.

## Planar models and finite footprints

Case Studies uses first/second-order point models, unicycles and Ackermann/bicycle-type models. The basic unicycle satisfies
\[
\dot x=v\cos\theta,\quad\dot y=v\sin\theta,\quad\dot\theta=\omega.
\]
Adding \(v,\omega\) as states with acceleration inputs produces five states/two controls. The car heading rate is \(\dot\theta=v\tan\psi/l\), with steering \(\psi\), wheelbase \(l\) and a steering-rate input in the first-order version. These are kinematics, not tire-force vehicle dynamics. The inspected second-order car model has derivative/state-order and steering-factor inconsistencies; its presence is not validation of a correct seven-state simulator. The first-order point implementation also has extra stored states relative to the report.

Point, rectangular and triangular footprint abstractions transform local vertices into world coordinates, \(p+R(\theta)v_j\). Signed-distance constraints at those points relate a robot model to environmental geometry. Vertex/time-node checking does not certify collision freedom of the complete swept volume.

## Representation and capability boundaries

Mobile Robotics adds Hamilton/unit-quaternion conversions, minimal local parameterizations, continuous/discrete linearization and sensor-coupled differential-drive/quadrotor examples. Pinhole/motion exercises connect coordinates to measurements, not just a commanded path. Exact perturbation conventions and Jacobians are absent from that selective profile, so they are not assumed identical to the thesis. [Mobile source claims](../evidence/tum-mobile-robotics.yaml) preserve supplementary status and no personal implementation attribution.

The thesis's quaternion state supports general attitudes, but its principal evaluation varies planar translational offsets under frictionless/no-gravity contact. Case Studies supports planar kinematic planning, not six-DOF rigid-body contact. Their shared capability is explicit coordinate/model/interface reasoning, not equivalence of their physical assumptions.

See [impedance/contact dynamics](impedance-contact-dynamics.md), [trajectory transcription](optimal-control-transcription.md) and [distance geometry](signed-distance-neural-fields.md). Evidence: [thesis claims](../evidence/ma6018.yaml), Rigid-part model and uncertainty / Numerical transcription and reference interpolation; [Case Studies claims](../evidence/cit413042.yaml), robot/vehicle models in both profiles.
