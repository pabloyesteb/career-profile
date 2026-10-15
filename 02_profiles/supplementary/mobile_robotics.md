# Mobile Robotics — supplementary academic materials

## Source identity and provenance

| Field | Value |
|---|---|
| Stable source ID | tum-mobile-robotics |
| Source course | Mobile Robotics / Mobile Robotik, IN2404; TUM Smart Robotics Lab |
| Teaching context | Prof. Stefan Leutenegger; assistants Jaehyung Jung and Jiaxin Wei; Winter Semester 2024/25 |
| source_category | supplementary_academic_material |
| academic_credit | not_established |
| learning_relationship | unspecified |
| Profile status | complete_validated |

User-authorized supplementary learning materials; individual auditing/study/download history is unspecified. These sources do not establish accredited completion, personally implemented exercises or demonstrated mastery. IN2404 is distinct from transcript module IN2138. Inspected 2026-10-15.

## Available materials and processing scope

Archive: `00_sources/tum/archives/Mobile Robotik 950765148 (W24_25)_20261012_1552.zip`, approximately 2.1 GB, with 108 files: 56 PDFs, 28 `.f4v` recordings, 22 Python files and HTML. The 13-lecture sequence includes paired classroom/non-classroom decks, an aggregate `All Lecture Slides.pdf`, exercise/template/solution material, revision and historical WS23/24 exams. Existing inventory notes a byte-identical exercise/solution pair; labels alone do not establish different content. Some recording labels refer to W23.

The complete lecture sequence was identified; non-classroom decks were used as the topic backbone with targeted technical text and static Python/import inspection. Repeated recap/progressive material was consolidated. Lecture 11 p. 18 was rendered to inspect its quadratic-objective/constraint geometry. Videos, all duplicate decks, historical exams and every source line were not exhaustively processed.

## Structured technical map

### Foundations: state, geometry, sensors and motion

Introduction and representations distinguish robot state, world/environment maps and uncertainty. Rotation representations include Hamilton/unit quaternions, conversions and minimal local parameterization; probabilistic representations use Bayesian statistics. Sensor/actuator material and pinhole-camera/differential-drive exercises connect geometric states to measurements and control inputs. Kinematics/temporal models cover rigid-body rotation and differential-drive/quadrotor dynamics, alongside continuous/discrete model and linearization viewpoints. [L1–L3, L5; E2/E3 source paths below.]

### Probabilistic nonlinear least squares

Gauss–Newton and **Levenberg–Marquardt** address nonlinear estimation. Visual bundle adjustment uses reprojection residuals and camera/landmark Jacobians, with structured systems assembled from contributions of individual observations. Exercises include nonlinear least squares, motion-capture differential-drive examples and bundle adjustment. This connects probabilistic sensor models to numerical optimization rather than treating SLAM as a single black box. [L4–L5; E4/E5.]

### Recursive estimation and sparse visual SLAM

Bayesian filtering separates prediction and measurement update; particle filters approximate distributions with weighted samples/resampling. Kalman and extended Kalman filters represent Gaussian/linearized estimation, including inertial and differential-drive examples. Sparse visual SLAM includes FAST-type features, geometric matching/pose estimation and **RANSAC** outlier rejection, linking filtering and optimization-based estimation to visual navigation. [L6–L7; E7.]

### Dense, semantic and dynamic maps

Occupancy mapping maintains per-cell probabilities/log-odds using inverse sensor models. Dense 3D representations include **truncated signed-distance fields (TSDF)** and octree occupancy (OctoMap); dense tracking includes **iterative closest point (ICP)** and direct photometric alignment. Loop closure and locally rigid submaps address accumulated drift. The next lecture extends maps with semantic labels, object-level decomposition and dynamic-scene representations. These are related but distinct geometric/probabilistic representations. [L8–L9; E8.]

### Feedback and model-predictive control

Continuous/discrete LTI stability, SISO/MIMO distinctions, PID, anti-windup, reference filtering and feedforward precede model-based LQR/MPC. Quadrotor examples discuss input remapping, cascaded loops, hover assumptions and imperfect inter-loop decoupling. Constrained optimization geometry motivates MPC's treatment of control/state restrictions; supplied hill-driving Python separates `LqrController`, `MpcController` and a simulator and imports `qpsolvers.solve_qp`. [L10–L11, especially L10 pp. 16–24 and L11 pp. 18–31; E11.]

### Planning, exploration and learned decisions

Planning uses free configuration space, collision checking, obstacle inflation and roadmaps/grids; algorithms include **Dijkstra, A*, RRT, RRT* and informed RRT***. Slides distinguish discrete-space and sampling-based planning, plus robot exploration. Learning-to-act material adds finite-horizon/discounted MDP utility, value/policy iteration, model-learning versus model-free approaches, direct evaluation, Q-values, **Q-learning** and ε-greedy exploration, with a final deep-RL overview. [L12, pp. 1–58; L13, especially pp. 12–36; E12/E13.]

## Tools and represented exercise work

Python code pairs cover airplane/state representations, pinhole projection, differential-drive models, nonlinear least squares, bundle adjustment, filtering, occupancy grids, hill-driving control, RRT and gridworld MDPs. Static imports establish **NumPy, SciPy optimization/spatial transforms, Matplotlib, PyQt5, qpsolvers and vedo**. Lecture 10 also displays a C++ PID-controller example; this is demonstrated syntax, not evidence of a personal C++ software project. No executable behavior or training/solver results were tested.

## Relationships and potential professional relevance

This source deepens the syllabus-level [IN2138](../courses/in2138-robot-motion-planning.md) planning/filtering map while remaining a separate supplementary identity. Estimation/rigid-body/control topics relate to the [thesis](../projects/thesis.md); geometric planning and signed-distance representations relate to [Case Studies](../projects/case_studies_optimization.md), without equating volumetric TSDF mapping with its learned collision SDF. Decision models relate to [deep RL](../courses/mgt001299-introduction-to-deep-reinforcement-learning.md) and supplementary [ADPRL](approximate_dynamic_programming.md). These are useful thematic connections, not additional accredited experiences or expanded contribution attribution.

Potential domains: robot autonomy, navigation/GNC, perception, probabilistic estimation, constrained control and numerical optimization. Thematic categories: dynamical systems and robotics; control theory; optimization; computer vision and scientific computing; reinforcement learning.

## Source references and deeper-extraction priorities

All references resolve inside the named archive; use the following exact directory/file combinations:

| Ref | Directory | Document |
|---|---|---|
| L1 | `16. Oktober - 22. Oktober/` | `L1 Introduction.pdf` |
| L2 | `23. Oktober - 29. Oktober/` | `L2 Representations.pdf` |
| L3 | `30. Oktober - 5. November/` | `L3 Sensors and Actuators.pdf` |
| L4 | `6. November - 12. November/` | `L4 Probabilistic Nonlinear Least Squares.pdf` |
| L5 | `13. November - 19. November/` | `L5 Kinematics and Temporal Models.pdf` |
| L6 | `20. November - 26. November/` | `L6 Recursive Estimation.pdf` |
| L7 | `27. November - 3. Dezember/` | `L7 Sparse Visual SLAM.pdf` |
| L8 | `4. Dezember - 10. Dezember/` | `L8 Dense Mapping and SLAM.pdf` |
| L9 | `11. Dezember - 17. Dezember/` | `L9 Semantic, Object-level and Dynamic Mapping.pdf` |
| L10 | `8. Januar - 14. Januar/` | `L10 Feedback Control.pdf` |
| L11 | `15. Januar - 21. Januar/` | `L11 Model-based Control.pdf` |
| L12 | `22. Januar - 28. Januar/` | `L12 Planning.pdf` |
| L13 | `29. Januar - 4. Februar/` | `L13 Learning to Act.pdf` |

Exercise anchors: **E2** `23. Oktober - 29. Oktober/E2_aeroplane_sol.py`; **E3** `11. Dezember - 17. Dezember/E3_pinhole_camera_sol.py`; **E4** `6. November - 12. November/E4_least_squares_sol.py`; **E5** `13. November - 19. November/E5_bundle_adjustment_sol.py`; **E7** `27. November - 3. Dezember/E7_diff_drive_sim_sol.py`; **E8** `4. Dezember - 10. Dezember/E8_diff_drive_occ_sol.py`; **E11** `15. Januar - 21. Januar/E11_hill_driving_sol.py`; **E12** `22. Januar - 28. Januar/E12_rrt_sol.py`; **E13** `29. Januar - 4. Februar/E13_gridworld_sol.py`. Catalogs: `01_inventory/archive_files.csv` and `files_manifest.csv` under the stable source ID.

Prioritize L4–L8 for exact Jacobians, perturbation conventions, filter equations and mapping updates; L11/E11 for horizon/cost/constraint/solver contracts; L12/E12 for collision checking and tree rewiring; and L13/E13 for MDP versus learning distinctions. Render relevant mathematical slides because extraction loses notation and some spatial relationships. The 13-part topic backbone is mapped sufficiently for initial synthesis; detailed derivations and uninspected examples remain optional targeted extraction, not evidence of personal implementation.
