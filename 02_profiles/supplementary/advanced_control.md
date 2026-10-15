# Advanced Control — supplementary academic materials

## Identity and provenance

| Field | Value |
|---|---|
| Stable source ID | tum-advanced-control |
| Source course identity | Advanced Control, MW1420; TUM Chair of Automatic Control; Paul Kotyczka |
| Archive term | Winter Semester 2025/26 |
| source_category | supplementary_academic_material |
| academic_credit | not_established |
| learning_relationship | unspecified |
| Profile status | complete_validated |

The user authorizes inclusion as supplementary learning material. Auditing, independent study and resource collection are possible relationships; their distribution across these sources is unspecified. This profile describes available technical content, not accredited completion, personal implementation or demonstrated mastery. No ECTS/grade is assigned. Inspection date: 2026-10-15.

## Available materials and extraction scope

Archive: `00_sources/tum/archives/Advanced Control (W25_26)_20261012_1601.zip`. Existing inventory: 90 files, 58 PDFs, 17 MATLAB files, five Simulink models, six nested ZIPs and two videos. The main backbone is a **97-page lecture text**, complemented by a **40-page basic-concepts recap**, 12 numbered exercise/solution pairs, additional worked notes/code and historical exams. The lecture text's complete contents and preface were inspected; selected modeling/exercise/code evidence supplements that map. Nested packages and videos were not exhaustively processed.

## Structured technical topic map

### State-space modeling and stability

The notes build control design around nonlinear models and their equilibrium linearization, then linear time-invariant models \(\dot x=Ax+Bu+Ez,\ y=Cx\). Topics include control tasks, feedforward versus feedback, two-degrees-of-freedom structures, equilibrium/stability, eigenvalue criteria, BIBO stability and phase portraits. The basic recap adds state-transition solutions, time/frequency representations and invariant zeros through the Rosenbrock system matrix; transmission and invariant zeros must not be conflated. [A §§1, pp. 7–26; B contents/preface.]

### State feedback and optimal control

Design separates reference feedforward gains from feedback eigenvalue assignment. The topic sequence includes Kalman's controllability criterion, controller canonical form and transformations, Ackermann's formula for SISO feedback, Gilbert/Hautus criteria, and parametric MIMO feedback with eigenvector/design freedom. LQR provides an alternative to pole placement. [A §2, pp. 27–50.]

The supplied three-tank example uses a linearized three-state/two-input model, state/control weighting matrices and MATLAB `lqr(A,B,Q,Q_t)`, then inspects eigenvalues of `A-B*R`, builds `ss` and simulates with `lsim`. This is concrete evidence of the numerical workflow represented in the materials; it is not a personal simulation result. [C.]

### Observers, duality and decoupling

Luenberger observer design, separation principle, coefficient matching, controller–observer duality, observability tests and observer canonical form lead into a short Kalman-filter introduction and MIMO decoupling. Unobservability and inversion/zero structure matter for whether a decoupled design remains suitable. [A §3, pp. 51–70; B invariant-zero recap.]

### Disturbance rejection and tracking architectures

The notes distinguish disturbance-model-based constant compensation, piecewise-constant disturbances, disturbance-decoupling conditions, parametric-feedback decoupling, dynamic disturbance compensation and integral control. Extended architectures combine dynamic reference feedforward, state feedback, integral action and observers; this is a modular tracking/disturbance-rejection framework rather than one isolated controller formula. [A §§4–5, pp. 71–90.]

### Nonlinear input–output linearization

Relative degree, nonlinear feedback that linearizes input–output behavior, and zero dynamics form the final block. Exercise 12 models an elastic robot arm with coupled inertias, gravity and torsional elasticity and asks for relative-degree analysis. This connects state-space modeling to a mechanical control problem, while separating external linearized behavior from internal dynamics. [A §6, pp. 91–97; D, Problem 12.1.]

## Computational methods, tools and examples

MATLAB and Simulink are directly evidenced by `.m` and `.slx` files. The inspected three-tank script explicitly uses `eig`, `lqr`, `ss` and `lsim`. Archive paths also identify symbolic Euler–Lagrange derivation scripts for a cart–pendulum, numerical pole placement, Roppenecker-style three-tank feedback, decoupling, disturbance-observer models and dynamic feedforward packages. These paths identify worthwhile material; algorithms inside every auxiliary/nested file have not been independently reconstructed. Mechanical pendula, liquid tanks and an elastic robot arm supply engineering applications.

## Relationships and professional-domain relevance

This source adds a structured control-theory backbone alongside [thesis](../projects/thesis.md) robotics/control work and [Case Studies](../projects/case_studies_optimization.md) trajectory optimization. It relates thematically to [IN2138](../courses/in2138-robot-motion-planning.md) and supplementary [mobile robotics](mobile_robotics.md), but is not another credited instance of those experiences. Relevant domains include aerospace GNC, robotics, model-based engineering, estimation and tracking; these are content connections, not qualification assessments.

Thematic categories: control theory; dynamical systems and robotics; numerical mathematics; aerospace engineering.

## Sources and deeper-extraction priorities

References resolve inside the archive named above:

- **A:** `Lecture/Lecture notes and supplementary material/adv-lecture-notes-2025-26.pdf`; contents pp. 5–6 and chapter ranges above (printed/PDF page numbers agree).
- **B:** `Basic Concepts/Notes on basic concepts/adv-basic-concepts-2025-26.pdf`, 40 pages; preface/contents pp. 3–6. Its preface retains a 2021 date despite the 2025/26 cover; mixed historical material also appears elsewhere.
- **C:** `Additional Exercise/Material Additional Exercise 8/three_tank_system_ch02_LQR.m`, statically inspected model/design/simulation blocks.
- **D:** `Exercise Course/Material Exercise 12/adv_exercise_12_problems.pdf`, Problem 12.1.
- **Catalogs:** `01_inventory/archive_files.csv`, `archive_summary.csv`, `files_manifest.csv`; source ID above.

For deeper synthesis, prioritize A's LQR derivation, MIMO decoupling/invariant-zero conditions, disturbance-model assumptions and nonlinear zero-dynamics analysis; then compare their worked exercises/code. Recover exact theorem hypotheses and formulas directly rather than expanding this map from general knowledge. No experiments/code were executed. The six-chapter map is complete at the requested selective-inspection level, not an exhaustive validation of all auxiliary files.
