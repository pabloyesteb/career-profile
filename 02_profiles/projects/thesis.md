# Master's thesis — Robust Contact Rich Control for Manipulation

## Identity, sources and attribution

| Field | Value |
|---|---|
| Stable identifier | ma6018 / thesis |
| Author | Pablo Yeste Blesa |
| Degree / institution | Master's in Applied Mathematics, Technical University of Munich |
| Official module | MA6018 — Master's Thesis |
| ECTS | 30 |
| Grade | 2.0 |
| Thesis title | Robust Contact Rich Control for Manipulation |
| Submission | 17 August 2026 |
| Defense material | September 2026; presentation dated 24 September |
| Research setting | TUM Chair of Automatic Control Engineering and Siemens AG |
| Supervisors listed | Martin Buss; Marion Leibold; Christian Dietz; Sebastian Albrecht |
| Profile status | complete_validated |

Academic metadata comes from `01_inventory/courses.csv`, extracted from the configured grade transcript; research identity comes from the thesis title page and defense. Validation completed 2026-10-14. This is the definitive technical knowledge profile, not independent experimental certification.

References use these source identifiers:

- **[T]** `00_sources/master_thesis/root_signed.pdf`, 98 PDF pages. Page references are **printed thesis pages**; main-text physical PDF page = printed page + 9.
- **[P]** `00_sources/master_thesis/final_presentation_notes.pdf`, 70 physical PDF pages, with `00_sources/master_thesis/final_presentation.tex` for precise expressions. Presentation page references are **physical PDF pages**, not slide footer numbers. PDF and TeX represent one presentation.
- **[R]** `/home/pablo/TUM/SoSe 26/TFM/contact-rich-control`, branch `kleff`, inspected HEAD **`57efc6aa6119cd5ae969ed83fc67efcb40c71672`**. Repository-relative paths below resolve against this external checkout. **E** abbreviates `python_src/trajectory_execution/`; **C** abbreviates `E/impedance_mpc/`.
- **[A]** `02_profiles/projects/_analysis/thesis_analysis.md`, the internal reconstruction/evidence map. It records document hashes, source-state qualifications, experiment lineage and detailed implementation questions; it is not the narrative template for this profile.

The defense guides the emphasis: lightweight compliant execution, a second feedback loop that monitors task progress, recovery when that progress stalls, and the interaction with the offline planning region. The thesis supplies the full formulation and evaluation. [P, pp. 14–19, 26–37; T, §1.3.]

**Contribution boundary.** The author formulated, implemented and investigated the thesis's impedance-aware MPC, path-projection reference management, contact-aware extension, and progress-triggered recovery framework and comparisons. The offline contact-implicit planner, its optimized common reference, scenario offsets and scenario trajectories are **prior work by Dietz et al.**, supplied as fixed inputs. The existing impedance law, known search heuristics, contact-model literature and external numerical libraries are building blocks, not claimed as original inventions. The recovery contribution lies in progress-based triggering and integration with reference-following execution, not inventing spiral search. [T, §1.3, pp. 3–4; §§2.2, 3.3–3.5; P, methodology.]

## Research problem and principal contributions

Robust offline planning does not automatically produce robust execution. In assembly, an uncertain grasp/part pose causes the controller to act on a biased state; even compliant, accurate tracking can then leave the part geometrically jammed outside the opening. The research asks whether a lightweight execution layer can exploit a precomputed robust plan and recover from stalls without solving a full contact-implicit optimization online. [T, Ch. 1; P, motivation and assembly task, pp. 2–4.]

Four connected contributions structure the work:

1. **Nonlinear impedance MPC:** embed the impedance feedback law inside the prediction dynamics, and optimize a feedforward acceleration while anticipating the compliant response.
2. **Scenario-path reference management:** infer progress by projecting perceived position onto the planner's scenario trajectories; compare projected reference timing with clock-based timing.
3. **Contact-aware prediction:** initialize a predicted contact-wrench state from the measured wrench, preserving a small smooth optimal control problem.
4. **Progress-triggered recovery:** detect stagnation through swept path length and perturb the impedance reference using tangential or search-based corrections.

The work retains technically meaningful negative findings: neither MPC alone nor the evaluated contact-force extension improved insertion robustness over direct impedance in the reported setup. Progress-triggered recovery did, and systematic transverse search outperformed the tested geometry-based directional estimate. [T, §§6.2–6.5, 7.1; P, pp. 26–37.]

## Technical scope and mathematical foundations

### Rigid-part model and uncertainty

The part is represented as a free, fully actuated six-degree-of-freedom rigid body driven by a Cartesian force/torque wrench, with state

\[
x=(p,q,v,\omega)\in\mathbb R^3\times S^3\times\mathbb R^6.
\]

The pose is an element of \(SE(3)\), represented using position and a scalar-first unit quaternion. The stored mechanical state has 13 components because orientation uses four components under one unit-norm constraint. Quaternion conjugation/inversion, composition, rotation matrices and relative-orientation errors underpin the model. This is a task-space abstraction, not a joint-space robot-arm model. [T, §2.1, pp. 7–9; P, quaternion backup, p. 40.]

The perceived pose is constructed by composing the measured/true simulated pose with an offset:

\[
\mathcal P_q((p,q),(\delta p,\delta q))
 =(p+R(q)\delta p,\;q\otimes\delta q).
\]

The test offset acts on the state read by the controller at every control step, not merely on the initial physical pose. Translational bias is expressed through the current rotation. True simulated state is retained for evaluation and non-deployable diagnostic oracles. [T, §§2.2.1, 6.1.1.]

The evaluated scene is a tight-fit irregular hexagonal peg/opening, with **frictionless contact and no gravity**. Stalls therefore exercise geometric blockage rather than validating frictional wedging recovery. Main tests vary planar translational uncertainty; the general pose representation does not imply a complete six-dimensional uncertainty study. [P, assembly task, p. 4, and simulation backup; T, §§1.2, 6.1, Appendix A.2.]

### Cartesian impedance and compliance

For reference state \(x_d\) and perceived/measured state \(\hat x\), the feedback wrench is

\[
w_{imp}=\begin{bmatrix}
D_p(v_d-\hat v)+K_p(p_d-\hat p)\\
D_o(\omega_d-\hat\omega)+2\eta_e K_o\epsilon_e
\end{bmatrix},\qquad
q_e=\hat q^{-1}\otimes q_d=(\eta_e,\epsilon_e).
\]

Stiffness maps pose errors into restoring force/torque; damping attenuates relative motion. Quaternion error replaces a componentwise orientation difference in the feedback law. The angular term is associated with the orientation-error potential described in the thesis. Diagonal gains/inertia use

\[
K_p=k_pI_3,\quad K_o=k_oI_3,\qquad D=2\zeta\sqrt{KM}.
\]

The thesis investigates compliance and tracking under contact, rather than commanding a prescribed contact force. Energy/passivity arguments for ideal fixed-reference impedance are theoretical foundations, not a proven stability guarantee for the complete moving-reference MPC/recovery system. [T, §2.1.2, §4.2, Appendix A.1; P, impedance backup, p. 41; R, C/controller.py, `_compute_wrench`, `_impedance_accel`.]

### Inherited robust planning interface

The offline planner jointly reasons about several pose-offset scenarios through contact-implicit optimal control, returning a common impedance reference \(X_d\), scenario trajectories \(X_r^{(i)}\), and offsets \(\delta^{(i)}\). These describe anticipated compliant executions and provide geometric information for online progress estimation. The planner's contact reasoning remains offline; the thesis's online MPC uses smooth prediction, without newly solving contact-complementarity constraints at every control step. [T, §§2.2, 3.5.]

The principal input reference has 101 nodes spaced by 0.04 s (4 s). Data are supplied through the `raptico_problem_data` submodule, notably `peg_in_hole/peg_6/soldata/25_03_11_28_hom_iter_4_filtered.yaml` and its corresponding problem YAML. Reference/scenario data ingestion and execution are thesis work; original planner development is not. [R, data submodule; E/run_experiments.py; T, §6.1.]

## Impedance-aware nonlinear model predictive control

### Optimal control formulation

At each control step, MPC solves a finite-horizon tracking problem with optimized feedforward accelerations \(u=(a_{ff},\alpha_{ff})\):

\[
\begin{aligned}
\min_{x_{0:N},u_{0:N-1}}\quad&
\sum_{k=0}^{N-1}\left(\|x_k-x_{d,k}\|_Q^2+\|u_k\|_R^2\right)
 +\|x_N-x_{d,N}\|_{Q_f}^2\\
\text{s.t.}\quad&x_0=\hat x,\qquad x_{k+1}=\Phi_h(x_k,u_k),\\
&u_{min}\le u_k\le u_{max}.
\end{aligned}
\]

Only the first optimized feedforward action is applied before replanning. Prediction includes the feedback response:

\[
\dot p=v,\quad\dot q=\tfrac12[0,\omega]\otimes q,\qquad
\begin{bmatrix}\dot v\\\dot\omega\end{bmatrix}
 =u+M^{-1}w_{imp}(x,x_d).
\]

The quaternion equation follows the formulation displayed in the thesis/presentation. The key modeling choice is that the optimizer predicts a body **already under impedance control**, rather than leaving compliance to an invisible downstream loop. Applied wrench combines mass/inertia-scaled feedforward with feedback. The base angular model omits the gyroscopic term; its numerical assessment is discussed below. [T, §4.2, Eqs. 4.1–4.7, pp. 24–29; P, pp. 14–16 and OCP backup; R, C/controller.py, `_build_model`, `_build_ocp`, `run_optimization`.]

The implementation uses **LINEAR_LS** residuals, including quaternion component error. Quaternion reference signs are aligned along the horizon to avoid artificial penalties between antipodal representations of the same attitude. This least-squares attitude cost is distinct from the quaternion feedback error above. Bounds constrain feedforward accelerations, not the sum of feedback/feedforward wrench or robot-joint torques. [R, C/controller.py, `_build_ocp`, `run_optimization`.]

### Numerical transcription and reference interpolation

- **Direct multiple shooting** with CasADi symbolic dynamics and acados OCP construction.
- **Sequential quadratic programming**, **Gauss–Newton** Hessian approximation and **full-condensing HPIPM** QP solution in the target experiment configuration.
- **Two-stage Gauss implicit Runge–Kutta**, one integration step per shooting interval, giving the fourth-order A-stable scheme discussed in the thesis.
- An internal clock \(\dot\theta=1\), reset per solve, enables a continuously varying reference in the symbolic dynamics. Thus the implemented base state has 14 components: 13 mechanical plus clock.
- Linear interpolation of position/velocity and shortest-arc **SLERP** of quaternion orientation reconcile the planner, controller and integration grids. Antipodal alignment and small-angle handling avoid numerical interpolation pathologies.
- Stage angular reference velocity is recovered from the quaternion increment \(q_1\otimes q_0^*\) through an atan2 axis-angle calculation divided by stage duration. It is not simply a linear interpolation of unrelated angular-rate samples.

[T, §4.2, Appendix A.4; R, C/controller.py, `_interpolated_reference`; E/quat_utils.py, `slerp_ca`, `stage_omega_from_quat_ca`, `stage_omega_from_quat_np`; `experiments/config/peg_6/_target_config_core.yaml`.]

### Main operating point

| Parameter | Main value |
|---|---|
| Mass / principal inertias | Approximately 0.666 kg / [2.42, 2.38, 0.36] × 10⁻³ kg m², read from plant |
| Translational / rotational stiffness | 50 N/m / 5 Nm/rad |
| Damping ratio | 0.7 |
| Horizon / shooting intervals | 0.5 s / 20 |
| Nominal control interval | 25 ms |
| MuJoCo physics interval / substeps | 0.73 ms / 34 |
| State weights | Position \(I_3\), quaternion \(I_4\), velocities \(0.1I_3\) each |
| Feedforward weight | \(0.01I_6\) |
| Linear / angular feedforward limits | 5 m/s² / 5 rad/s² |

[T, Table 6.2, p. 43; R, target configuration.]

## Contact-aware prediction and model extensions

The contact-aware formulation adds a predicted wrench \(\lambda=(\lambda_f,\lambda_\tau)\) to the mechanical state:

\[
\begin{bmatrix}\dot v\\\dot\omega\end{bmatrix}
 =u+M^{-1}(w_{imp}+\lambda),\qquad
\dot\lambda_f=-b_{env}v,\quad
\dot\lambda_\tau=-b_{env,o}\omega.
\]

Measured wrench initializes the added state at each solve. This is a local, smooth elastic approximation, adapted from the contact-force-as-state literature; it does not explicitly infer contact topology, enforce unilateral contact or optimize a friction cone. The augmented mechanical state has 19 components, or 20 including the interpolation clock. [T, §4.3, Eqs. 4.15–4.17, pp. 30–31; P, p. 47; R, C/contact_aware_mpc.py, `ContactAwareMPCController`.]

An external switching wrapper selects free/contact predictors using the measured wrench norm. In the free branch the wrench initialization is zero; in contact the measured wrench is passed through. Target settings include switching threshold 0.001, translational/rotational stiffness coefficients 266.31/0.14489, zero wrench cost weights and a wrench-state bound of 500. The switching logic lies outside the smooth OCP. [R, C/switching_mpc.py, `ContactSwitchingMPC.run_optimization`; `experiments/config/peg_6/_tc_contact_core.yaml`.]

The evaluated force model did not improve reported insertion performance. The interpretation is that a fixed local elastic belief struggles when the peg's contact mode changes within the horizon; this does not establish that all contact-aware MPC methods are ineffective. Setting the stiffness coefficients to zero retains the initialized wrench as a constant predicted disturbance, so that ablation must not be described as exactly removing all contact information. [T, §§6.4, 7.2.5; R, C/contact_aware_mpc.py.]

The repository additionally contains planar-normal, Han-style, unilateral and adaptive model variants, plus anisotropic costs. These clarify the explored computational direction but are **not promoted to established final experimental improvements**. In particular, `C/stiffness_estimator.py` implements regularized local fitting

\[
\Delta\Lambda\approx-K\Delta P,\qquad
K=-\Delta\Lambda\Delta P^T(\Delta P\Delta P^T+\rho I)^{-1},
\]

followed by symmetrization and PSD eigenvalue clipping; `C/anisotropic_cost.py` implements normal-oriented position-cost adaptation. Their code exists, but the principal evaluated contribution remains the isotropic wrench-state controller. [R, those files and C/contact_aware_mpc.py; T, §7.2.5.]

## Reference management and progress feedback

### Local horizon and scenario projection

The local reference is sampled as

\[
x_{d,k}=X_d(t_0+k h_{ctrl}),\quad k=0,\ldots,N.
\]

Clock-based progression sets \(t_0=n h_{ctrl}\). The alternative projects perceived position onto each scenario polyline, producing nearest distance \(d_i\) and arc coordinate \(s_i\). Arc-to-time inversion gives \(t_i=\mathrm{ArcToTime}_i(s_i)\), blended as

\[
t_0=\sum_iw_it_i,\qquad
w_i=\frac{d_i^{-\beta}}{\sum_jd_j^{-\beta}},\quad\beta=1
\]

with near-zero-distance safeguards in implementation. This supplies both reference timing and local trajectory geometry. It is a positional geometric progress heuristic, not a probabilistic pose estimator or contact-mode observer. [T, §5.1, Eqs. 5.1–5.4, pp. 33–34; R, E/path_projection.py; C/tracking_mpc.py, `_compute_blend_t0`.]

The negative timing result has a concrete control interpretation: if progress stalls, projected reference time also stalls, reducing the growing tracking error that clock-based progression would generate to push through the obstruction. Projection remains useful as **geometry and progress feedback** for detection/recovery even when it is a poor source of reference timing. [T, §§1.3, 6.3, 7.1; P, progress-monitoring methodology.]

### Stagnation detector

The detector compares measured swept arc length with expected progress:

\[
s(n)-s(n-\lfloor t_{bloq}/h_{ctrl}\rfloor)
 <\alpha v_{stag}t_{bloq}.
\]

Here \(v_{stag}\) is characteristic scenario-path speed, \(t_{bloq}\) a time window, and \(\alpha\) the allowed progress fraction. Main values are 71.8 mm/s, 0.3 s and 0.9: roughly 19.4 mm minimum progress over the window. Detection is suppressed near intended end-of-trajectory settling, with buffer/recovery-state management to avoid inappropriate repeated triggers. No force threshold or contact-mode estimate is required for this trigger. [T, §5.3, Eq. 5.5, Fig. 5.1; R, C/recovery.py, `StagnationDetector.update`.]

## Recovery strategies and diagnostic comparisons

Recovery perturbs the **reference equilibrium** consumed by the impedance law/MPC, rather than replacing the physical state or directly prescribing a contact force. It forms a second feedback loop around task progress. Known recovery primitives are integrated with this detector and the planned scenario geometry. [T, §§3.3, 5.3–5.4; P, pp. 17–19, 29–31.]

### Tangential reference displacement

Scenario distances weight local path tangents, which are combined and normalized into a correction direction. A translational reference offset grows at 0.1 m/s during a 0.8 s recovery interval, reaching at most 80 mm under these settings. The target implementation freezes projection while the correction is active, then releases the temporary displacement. Direction quality is limited by biased perceived geometry. [T, §5.4, Eq. 5.6; R, C/recovery.py, `TangentialOffset`; target YAML.]

### Discrete and continuous spiral search

- **Discrete spiral/ring probing:** persistent search displacement in a plane transverse to the path, 10 mm first ring, 45° angular increments (8/ring), increasing radius up to 40 mm. Successive stagnation events move the probe; the code does not use the tangential variant's active/refractory reset cycle.
- **Continuous spiral:** displacement grows from 5 to 40 mm over 0.8 s, completing 1.5 turns (675°/s), then clears. It sweeps directions rather than committing to one estimated direction.

The distinction is algorithmic, not simply two names for the same perturbation. [T, §5.4, Eq. 5.7, Table 6.3, §6.5.2; R, C/recovery.py, `SpiralSearch`, `SpiralDecoy`; `_tc_recovery_strategies.yaml`.]

### Scenario switching and oracles

Scenario switching retargets progression to another scenario rather than adding a spatial correction. It did not improve the reported time-mode baseline. The implementation includes scenario bans and clearing options; the negative result is not a universal statement about path-switching methods. [T, §§5.4, 6.5.2; R, `TrajectorySwitch`.]

Diagnostic tangential variants use true-position geometry or known perception offset, information unavailable in ordinary execution. They assess whether poor direction estimation limits the practical recovery. Code's true-geometry variant changes both tangent geometry and distance weighting; it should not be interpreted as a clean isolation of the weights alone. Exact-offset correction is a non-deployable upper-bound comparison, not an estimator of the unknown offset. [T, §6.5.3, Table 6.8; R, `RealNearestTangentialOffset`, `CheatTangentialOffset`.]

## Simulation, implementation and experimental methodology

### Computational architecture

The Python pipeline loads planning YAML and MuJoCo geometry, configures controller/reference/recovery branches, expands the offset grid, constructs perceived states and horizon references, solves the OCP, applies wrench and records outcomes. **CasADi/acados** implement symbolic dynamics and generated solver interfaces; **HPIPM** solves condensed QPs; **MuJoCo** supplies the contact simulation. [R, E/run_experiments.py; C/controller.py; C/tracking_mpc.py; `experiments/run_battery.py`.]

Optimization and feedback operate at different rates: the first feedforward action is held over the control interval, but impedance feedback is recomputed at each physics substep. The nominal 25 ms interval uses 34 × 0.73 ms substeps (24.82 ms actual simulated advance), a small grid-rounding difference. Appendix A.5 compares feedback held for the whole interval with substep feedback and reports much smaller wrench jumps and improved stability for the latter. This is a substantive multirate implementation choice, not merely simulator configuration. [T, §4.2, Appendix A.5; R, C/tracking_mpc.py; `experiments/bench_substep_feedback.py`.]

Configuration-driven experiments save per-offset **HDF5 trajectories**, **JSON metadata**, **CSV summary metrics**, plots and selected videos. Logging includes true/perceived/reference states, wrench/contact information, solver status/KKT/timing, progress and recovery. **NumPy**, **YAML**, **h5py/HDF5**, **Matplotlib**, **LaTeX** and **Git/submodules** support numerical processing, reproducibility and reporting. Generated C solver artifacts are part of the acados workflow, not a separate claim of handwritten C development. [R, C/run_log.py; E/make_fig_success.py; battery and configs.]

### Evaluation design

The principal comparison uses **121 fixed planar translational perception offsets** shared across methods, extending outside the convex planning region. Each offset produces a separate simulation. The intended success criterion, confirmed by the user for profiling, is

\[
\|p_{true,final}-p_{d,final}\|<2.5\ \mathrm{mm}.
\]

Results are shown as counts and maps over the offset plane. A difference of at least three offsets (about 2.5 percentage points) is used as a practical comparison threshold, motivated by one-offset variation between two planner runs; it is not a formal significance test. [T, §6.1, pp. 41–46, Tables 6.1–6.3.]

**All quantitative findings below are reported by the thesis/defense, not independently reproduced outcomes under that intended criterion.** The known classification implementation discrepancy is recorded concisely in the internal evidence note at the end; it does not replace the intended methodology or become the profile's research narrative.

## Principal findings and technical interpretation

### Controller, reference and recovery comparison

| Method | Without recovery | With tangential recovery |
|---|---:|---:|
| Direct impedance | 47/121 (38.8%) | 68/121 (56.2%) |
| Impedance-aware MPC | 47/121 (38.8%) | 66/121 (54.5%) |
| Projected-time reference | 32/121 (26.4%) | 58/121 (47.9%) |
| Contact-aware MPC | 47/121 (38.8%) | 67/121 (55.4%) |

[T, §§6.2–6.4, 6.5.1; P, pp. 26–28 and contact backup.]

MPC and direct impedance reportedly succeed on the same unrecovered offsets; adding prediction alone does not enlarge the successful set. Contact-force augmentation likewise provides no meaningful gain in this setup. Projection-based timing underperforms clock timing. In contrast, reference recovery substantially improves both reactive and predictive execution. These findings favor separating **compliant tracking** from **progress-based task correction**, rather than assuming more detailed prediction necessarily supplies the missing robustness.

### Search versus estimated-direction recovery

| Recovery / diagnostic | Reported count |
|---|---:|
| Discrete spiral | 78/121 (64.5%) |
| Continuous spiral | 74/121 (61.2%) |
| Tangential displacement | 68/121 (56.2%) |
| Scenario switching | 47/121 (38.8%) |
| True-geometry tangential oracle | 106/121 (87.6%) |
| Known-offset oracle | 121/121 (100%) |

[T, §§6.5.2–6.5.3, Tables 6.7–6.8, Figs. 6.7–6.8; P, pp. 29–31.]

Discrete spiral's 47→78 change is **31 additional offsets**, **25.6 percentage points**, or about **66% relative improvement** over the baseline count. The oracle gap indicates that good corrective directions exist but biased scenario geometry does not reliably select them; systematic search avoids reliance on one direction estimate. Oracle success is not achievable performance without unavailable information.

The defense reports a fully successful **sampled** rhombus at 30 mm versus the 25 mm planning rhombus, a geometric area ratio \((30/25)^2=1.44\), or **44% area expansion** with spiral recovery. This is a reported grid-region observation, not a guarantee for every continuous pose in that region or arbitrary geometries. [P, p. 31 and conclusions, pp. 34–37.]

### Sensitivity and dependence on planning

- **Preview length:** at fixed 25 ms control, horizons 0.2/0.4/0.5/1.0 s all report 47/121 without recovery; with recovery they give 69/67/66/66. Longer preview does not resolve the robustness limitation. Reported mean solve time rises approximately 3.9→7.2→10.2→17.5 ms across these horizons. [T, §6.2, Table 6.4.]
- **Detector threshold:** \(\alpha=0.01,0.3,0.5,0.7,0.9\) yields 51/51/55/66/68 successes with tangential recovery. Earlier intervention at the chosen operating point helps this setup; the study does not establish a universal optimum. [T, §6.5.4, Table 6.9.]
- **Planning-region size:** with identical unscaled test offsets, scenario magnitudes 25/15/5 mm give unrecovered 47/30/25 and recovered 68/52/35. Recovery improves all three, but cannot eliminate dependence on informative scenario coverage. This experiment uses tangential recovery, not the best spiral strategy. [T, §6.6, Table 6.10; P, pp. 32–33.]
- **Runtime:** reported solve medians are 9.3 ms with recovery and 13.2 ms without, but cold solves and some later steps exceed 25 ms. Only 44/121 recovered and 8/121 unrecovered runs have no overrun. These are shared-machine timing measurements, not hard-real-time hardware certification. [T, §6.2, pp. 48–49.]
- **Numerical/model audits:** Appendix A.5 reports substep-feedback wrench-jump medians near 0.003 N versus 7.3 N with held feedback. Appendix A.6 studies omitted gyroscopic torque (median ratio about 0.07%, 95th percentile 1.1%) and shows small discrepancies under the tested low-speed/feedback settings. These qualify implementation choices, not general stability or model-validity theorems. [T, Appendix A.5–A.6; repository benchmark/audit scripts.]

## Technical knowledge represented by the work

### Formulated, implemented and evaluated

- Cartesian impedance control, quaternion attitude errors, rigid-body task-space modeling and compliance/tracking trade-offs.
- Nonlinear optimal control and receding-horizon execution: impedance-in-the-model prediction, direct multiple shooting, feedforward constraints, least-squares costs and clock-augmented reference dynamics.
- CasADi symbolic models, acados solver integration, SQP/Gauss–Newton, implicit RK and condensed QP methods.
- Contact-force-as-state prediction, measured-wrench initialization and smooth-model switching.
- Polyline closest-point geometry, arc-length/time inversion, distance-weighted trajectory blending and time-versus-progress reference management.
- Windowed stagnation detection, reference-level tangential/discrete/continuous search recovery and oracle diagnostics.
- Multirate MuJoCo simulation, experiment automation, structured logging, numerical sensitivity analysis and interpretation of negative results.

These capabilities are supported by thesis formulations, corresponding implementation and reported comparative experiments, not inferred from topic names. [T, Chs. 4–6; R, core controller/recovery/execution/configuration files.]

### Implemented extensions, theoretical foundations and research exposure

Online stiffness fitting, PSD matrix conditioning and anisotropic/normal-oriented model variants have implementation evidence but no established principal performance improvement here. Impedance energy/passivity reasoning, quaternion geometry and offline scenario/contact-implicit optimization provide theoretical foundations. Contact-implicit MPC, ADMM-based contact optimization, sampling-based MPC, diffusion policies and residual RL are research exposure/future directions, **not demonstrated training or implementation accomplishments in this thesis**. [T, Chs. 2–3, §7.2; R, extension files.]

### Applications and thematic categories

Primary application: compliant robotic assembly and manipulation under perception/pose uncertainty, particularly tight-fit insertion. The mathematical/computational content contributes to **control theory; optimization; dynamical systems and robotics; numerical mathematics; simulation and scientific computing; experimental evaluation**. No aircraft GNC implementation, actuarial model, learned robot policy or hardware-deployed controller is implied by potential downstream relevance.

## Limitations and proposed extensions

Evidence is simulation-based on one hexagonal geometry and a small set of planning instances, under frictionless/no-gravity assumptions and mostly planar translational offsets. The arm itself, realistic friction, sensing/calibration imperfections and full rotational uncertainty are outside the demonstrated validation. No general robustness, stability, recursive feasibility or convergence guarantee is established for the full architecture; feedforward bounds alone are not comprehensive safety constraints. [T, §§1.2, 7.1–7.2; P, assembly assumptions.]

Proposed extensions include full-robot/hardware integration, realistic contact/friction, perception updates, broader assembly geometries, improved contact-normal/stiffness adaptation, more informative search and recovery directions, rotational recovery, and residual-learning layers around the structured controller. These remain future directions unless separately supported; repository examples or literature outcomes are not substituted for completed thesis experiments. [T, §7.2.]

## Evidence note and profile validation

**Known classification bug — internal use:** the user confirms that saved classification logic is buggy. Intended evaluation remains final position within 2.5 mm of the final reference. The matched runner/configurations instead use a 12 mm minimum-over-time error around another goal, storing that minimum as `final_pos_err_mm`. Therefore CSV count matching is not independent validation of the reported thesis results under the intended criterion. Results above are explicitly attributed to T/P; no corrected experiment or independent reproduction is claimed. Further details remain in [A], §8.1, rather than dominating this profile.

Repository HEAD and inspected submodules are recorded in [A]. Current worktree includes uncommitted presentation material, and HEAD postdates the August runs; it is the **inspection revision**, not an asserted exact run revision. Other model/frame/calibration questions remain technical qualifications in [A], not unsupported claims of implementation perfection. Public disclosure of Siemens-marked source details should be checked separately before CV/publication reuse.

Validation covered:

| Check | Outcome |
|---|---|
| Defense emphasis | Impedance-in-prediction, progress feedback, corrective search, 66% relative count change, 44% reported area expansion and planning-size dependence represented |
| Complete technical structure | T Chs. 2–5 formulations and algorithms; Ch. 6 comparisons/sensitivities; Ch. 7 limits/extensions; Appendix A numerical choices represented |
| Attribution | T §1.3 followed; offline planner/reference/scenarios and external software not misattributed |
| Mathematics and implementation | Equations checked against T/P and identified controller, projection, recovery and interpolation code; implemented-only extensions distinguished |
| Results | Reported-result attribution, intended 2.5 mm definition, known-bug note, oracle limits and negative findings retained |
| Scope | No hardware, hard-real-time, global robustness or learned-policy claim; no new experiments or source modifications |
| Traceability | Configured documents and repository paths checked; academic metadata agrees with inventory |

With the supplied clarifications, no material issue prevents a source-qualified professional technical profile. Reproduction/correction of quantitative outcomes is a separate task, not a prerequisite silently claimed to have been completed here.
