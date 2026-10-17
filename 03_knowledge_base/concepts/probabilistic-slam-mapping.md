---
id: probabilistic-slam-mapping
title: Nonlinear state estimation and sparse, dense and semantic mapping
domains: [robotics-planning-geometry, control-estimation, numerical-mathematics, language-vision-cognition]
evidence_refs: ["tum-mobile-robotics:estimation-mapping"]
status: reviewed
relations:
  - {type: related_to, target: signed-distance-neural-fields}
  - {type: related_to, target: state-feedback-observers}
---

# Nonlinear state estimation and sparse, dense and semantic mapping

## Geometry, residuals and observations

Mobile Robotics separates robot state, map and uncertainty, using unit/Hamilton quaternions and minimal local perturbations. Pinhole cameras, inertial/differential-drive observations and motion models connect coordinates to measurements. Gauss–Newton/Levenberg–Marquardt nonlinear least squares and bundle adjustment use reprojection residuals, camera/landmark Jacobians and per-observation structured system contributions.

The input profile does not provide exact Jacobians, perturbation conventions, normal systems or LM update formulas. These are not reconstructed. The represented distinction is important nonetheless: estimation optimizes measurement consistency, whereas trajectory optimization chooses an admissible motion/control path.

## Recursive versus optimization-based estimation

Bayesian filtering alternates prediction and measurement update; Kalman/EKF use Gaussian/linearized models, while particles use weighted samples and resampling. Sparse visual SLAM adds FAST-type features, geometric matching/pose estimation and RANSAC outlier rejection. Loop closure/submaps address drift through spatial/temporal structure, not by declaring a filter universally convergent.

This deepens IN2138's syllabus method map but remains a separate **supplementary** source. It does not supply evidence of personally implemented SLAM, bundle adjustment or filter code. The nonlinear/probabilistic update details remain at source-profile depth.

## Dense, semantic and dynamic representations

Occupancy grids represent per-cell probabilities/log-odds under inverse sensor models; OctoMap uses octree occupancy. TSDFs represent truncated geometric distances; ICP and direct photometric alignment support dense tracking. Locally rigid submaps and loop closure handle accumulated drift. Semantic labels, object decomposition and dynamic-scene maps extend geometric maps rather than replacing their uncertainty/association problems.

A volumetric TSDF is not the Case Studies learned collision SDF: they differ in acquisition, representation and numerical consumer. Both can encode distance, but neither an occupancy probability nor a learned distance is automatically a collision certificate. Exact log-odds and ICP/filter equations are absent from the input and not invented here.

## Represented computation and connections

Supplied Python exercises cover nonlinear least squares, bundle adjustment, differential-drive filtering and occupancy grids, using NumPy, SciPy optimization/spatial transforms, Matplotlib, PyQt5 and vedo across the material. Static resources establish numerical workflows, not personal results. [Mobile Robotics evidence](../evidence/tum-mobile-robotics.yaml) resolves to the nonlinear least-squares, recursive/sparse and dense/semantic map sections plus exercise register. Connections to [pose conventions](rigid-body-pose-kinematics.md), [feedback/observers](state-feedback-observers.md) and learned geometry preserve those different objectives.
