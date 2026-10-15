# Master's thesis — technical reconstruction

Status: **reconstruction complete; substantive questions remain open; final thesis profile not started**. Assessment date: 2026-10-14. This is an internal reconstruction, not a CV-ready profile or independent experiment reproduction. Sources and repository remained read-only; no project code or experiment was executed.

## 1. Source inventory and reliability assessment

- Final thesis: `00_sources/master_thesis/root_signed.pdf`, 98 PDF pages; **Robust Contact Rich Control for Manipulation**, Pablo Yeste Blesa, submitted 17 August 2026. Chapters 1–7, Appendix A.1–A.6, end matter. Printed main-text page = physical PDF page minus 9 (e.g. Ch. 4 p. 23 = PDF p. 32).
- Defense: `00_sources/master_thesis/final_presentation_notes.pdf`, 70 pages, and `00_sources/master_thesis/final_presentation.tex`. These are representations of one presentation, not independent experimental confirmation.
- External thesis repository: `/home/pablo/TUM/SoSe 26/TFM/contact-rich-control`, branch `kleff`, HEAD `57efc6aa6119cd5ae969ed83fc67efcb40c71672`. Latest checked-in commit is dated 2026-09-24, after the thesis submission. It is historical research evidence, not presumed final submitted implementation.
- Worktree is dirty, predominantly presentation exports/figures/scripts; 105 status entries. Current status and relevant source hashes are recorded in regenerable `.cache/thesis_analysis/repository_snapshot.json`. HEAD alone does not freeze uncommitted presentation content.
- Existing course and scientific-paper profiles are outside this analysis and remain unchanged.

### Reference convention and reproducibility

**T** denotes the thesis; its references use printed pages unless marked PDF. **P** denotes the presentation; its references use physical PDF pages. **R** denotes the external repository above. **E** is R's `python_src/trajectory_execution/`; **C** is `E/impedance_mpc/`; **Runs** is R's `experiments/runs/`. Repository-relative references below resolve against R, not career-profile.

Inspected submodules: `docs/thesis` at `99168732f23fee733ac4c4c1a91d9646f62ca799`, `external/acados` at `6111f01f2220a241057b4d56d8fe3a2cddd0309f`, and `raptico_problem_data` at `9203bf67fe4867f06da2e227cacf5a7448721977`. These current revisions are not proof of the revisions used for the August runs. Local presentation TeX is byte-identical to the inspected external `docs/final_presentation/final_presentation.tex`, which is modified relative to Git.

| Local source | SHA-256 |
|---|---|
| Thesis PDF | `0bc33dd367353059fd99a38c7da96d46361ee71acc0e688d0c0b09b506cb6ac8` |
| Presentation PDF | `5b27637ece1f0081d1edb6719de3b44c32be5111e437f16f5ce9144ab23e15b9` |
| Presentation TeX | `94b9e2d65be7c83be04310c72ee85013859100968dcee347f66a0ebc671b54a0` |

**Documented (D)** means explicitly stated by T/P; **Implemented (I)** means identifiable static code/configuration; **Experimentally supported (E)** means saved artifacts or a reported experiment, with that distinction stated; **Proposed (P)** means planned without sufficient execution evidence; **Ambiguous (A)** means conflicting/incomplete support. Categories overlap. Code existence does not prove execution; saved results are not newly reproduced experiments.

T establishes the submitted argument but contains implementation discrepancies. P is a later presentation, with repeated builds and notes; commented TeX frames are not necessarily delivered slides. Code establishes the inspected implementation, not automatically the submitted one. CSVs establish stored counts/classifications, not automatically insertion under the written success criterion. Generated solver code, duplicate figures and literature slides are not independent corroboration.

Text extraction covered document structure and technical content; TeX recovered notation. Selective rendered inspection covered T PDF pp. 33 (OCP), 39 (force model), 62 (strategy comparison), and P pp. 31 (robustness region), 47 (contact equations). This was not visual inspection of every page. The trusted standard-library utility `scripts/inspect_thesis_evidence.py` hashes relevant sources/configurations, records Git state/history and counts selected CSV flags without importing repository code. Regenerable results include `thesis.txt`, `presentation.txt`, `repository_snapshot.json`, `history.txt`, `run_summary.json` and rendered pages under `.cache/thesis_analysis/`. The snapshot is not a complete archival copy of R. No dependencies were installed or original sources modified.

## 2. Research objectives and problem formulation

The thesis evaluates simulated peg-in-hole insertion with uncertain held-part pose. A pre-existing multi-scenario contact-implicit planner supplies impedance reference trajectories. The thesis investigates execution-time impedance MPC, online path-projection reference management, a contact-force-augmented prediction model and stagnation-triggered recovery. The abstract states that recovery accounts for the largest gains; it does not claim hardware deployment.

Document structure: Ch. 2 rigid-part state/impedance and baseline planning; Ch. 3 literature; Ch. 4 MPC/contact-aware formulations and implementation; Ch. 5 reference construction/detection/recovery; Ch. 6 simulation comparisons; Ch. 7 conclusions/future work; Appendix A conventional baselines, MuJoCo parameters, interpolation, substep feedback and gyroscopic omission.

Repository inspection prioritized `python_src/trajectory_execution/impedance_mpc/`, execution/reference helpers, `experiments/run_battery.py`, configurations/results, planning data, figure scripts and relevant history. Generated acados C/JSON and legacy notebooks were treated as supporting/historical artifacts, not independent demonstrations.

The questions investigated are whether impedance-aware predictive feedforward, scenario-based reference progression, measured-contact-force prediction, and stagnation-triggered reference recovery improve insertion. The important engineering distinction is **tracking a perceived pose accurately versus actually finding the opening**: biased perception can make excellent tracking insufficient. The major result is that recovery helps more than the tested MPC/contact refinements. This is a simulation comparison, not an impossibility result for contact-aware MPC. [T abstract; §§1.1–1.3, 3.5; Chs. 4–7.]

The plant is a free, fully actuated rigid part driven by Cartesian wrench. It is not a manipulator with joint dynamics, inverse kinematics, joint-torque limits or arm collision constraints. The principal uncertainty grid tests translational perception errors in a plane, not systematic six-dimensional uncertainty. Offline planner/scenario solutions are inherited inputs, not established here as a planner newly authored in this thesis. Contact-implicit MPC, C3/ADMM, STORM/MPPI, diffusion policies and RL in Ch. 3 are literature context, not demonstrated implementations. [T §§2.1–2.2, 3.1–3.5, 6.1; `E/run_experiments.py`.]

## 3. Mathematical and theoretical foundations

### 3.1 State, perception and impedance

The physical state is \(x=(p,q,v,\omega)\), with \(p,v,\omega\in\mathbb R^3\) and scalar-first unit quaternion \(q\in S^3\). A pose offset is applied as

\[
\mathcal P_q((p,q),(\delta p,\delta q))=(p+R(q)\delta p,\ q\otimes\delta q).
\]

This maps positional bias through the current orientation; it is not necessarily a constant world translation. The controller receives biased pose throughout execution, while true state is available for evaluation and diagnostic oracles. [T §2.1; `E/run_experiments.py`.]

Cartesian impedance feedback is

\[
w_{\rm fb}=\begin{bmatrix}
D_p(v_d-\hat v)+K_p(p_d-\hat p)\\
D_o(\omega_d-\hat\omega)+2\eta_eK_o\epsilon_e
\end{bmatrix},\quad q_e=\hat q^{-1}\otimes q_d=(\eta_e,\epsilon_e).
\]

Diagonal mass/inertia and stiffness use \(D=2\zeta\sqrt{KM}\). Main parameters are approximately mass 0.666 kg, inertias \((2.422,2.379,0.362)10^{-3}\,\mathrm{kg\,m^2}\), translational stiffness 50 N/m, rotational stiffness 5 Nm/rad and damping ratio 0.7. Angular-frame consistency remains unresolved (§8), so this equation should not conceal convention differences between code paths. [T §§2.1, 4.2, Table 6.1; `C/controller.py::_impedance_accel`, `_compute_wrench`; target configuration.]

### 3.2 Inherited scenario planning

The offline contact-implicit planner optimizes a common impedance reference against multiple plausible pose perturbations. Its predicted scenario motions/terminal placement requirements shape the reference; contact modes are resolved offline. Inputs to execution are the common reference \(X_d\), scenario trajectories \(X_r^i\) and offsets \(\delta^i\). The online smooth MPC does not solve new contact-complementarity constraints at every control step. [T §2.2, §3.5.]

The principal reference has 101 nodes at 0.04 s spacing, hence 4 s duration. Relevant input files are `raptico_problem_data/peg_in_hole/peg_6/soldata/25_03_11_28_hom_iter_4_filtered.yaml` and `25_03_11_28_probdat.yaml`. Main scenario offsets are 25 mm; alternative instances use 15 and 5 mm on the same geometry. They are not broad cross-geometry validation. [T §§6.1, 6.6; data and experiment configurations.]

### 3.3 Guarantees and numerical qualifications

Appendix A's ideal fixed-reference impedance/passivity discussion does not prove passivity, robust feasibility or convergence of the full moving-reference MPC/recovery architecture. Feedforward limits do not bound total wrench. No general insertion guarantee is established. The appendix's broad unconditional-stability wording for semi-implicit Euler should not be promoted to a general theorem for arbitrary elastic dynamics/timesteps. The MPC integration and MuJoCo physics integration are different numerical layers. Numerical quaternion normalization and SLERP do not independently prove exact unit norm at every integration stage. [T Appendix A.1–A.4, Ch. 7; `C/controller.py`; `E/impedance_dynamics.py`.]

## 4. Technical methods and algorithms

### 4.1 Impedance-aware nonlinear MPC — D/I/E

The shooting formulation penalizes tracking and feedforward effort:

\[
\min_{x_{0:N},u_{0:N-1}}\sum_{k=0}^{N-1}
 (\|x_k-x_{d,k}\|_Q^2+\|u_k\|_R^2)+\|x_N-x_{d,N}\|_{Q_f}^2,
\quad x_0=\hat x,\quad x_{k+1}=\Phi_h(x_k,u_k).
\]

The prediction embeds impedance feedback:

\[
\dot p=v,\quad\dot q=\tfrac12[0,\omega]\otimes q,\quad
\dot v=a_{\rm ff}+M_p^{-1}w_{{\rm fb},p},\quad
\dot\omega=\alpha_{\rm ff}+M_o^{-1}w_{{\rm fb},o}.
\]

This preserves the left-multiplication form of Ch. 4 without resolving its frame ambiguity. The base model omits the gyroscopic term \(-I^{-1}(\omega\times I\omega)\). Optimized controls are six feedforward accelerations, with linear/angular limits 5 m/s² and 5 rad/s². Feedback is added subsequently; these are not total-wrench, joint-torque or contact-force safety bounds. [T §4.2, Eqs. 4.1–4.7; `C/controller.py::_build_model`, `_build_ocp`, `run_optimization`.]

An internal clock \(\dot\theta=1\), reset each solve, supports symbolic reference interpolation. The base model therefore has **14 states** (13 physical plus clock). Position and velocity interpolate linearly; orientation uses shortest-arc SLERP with antipodal alignment and a small-angle branch. Stage angular velocity comes from the axis-angle increment \(q_1\otimes q_0^*\), using atan2 and stage duration. Independently interpolating position and velocity does not ensure exact derivative consistency. [T §4.2, Appendix A.4; `C/controller.py::_interpolated_reference`; `E/quat_utils.py::slerp_ca`, `stage_omega_from_quat_ca`, `stage_omega_from_quat_np`; `C/tracking_mpc.py::_interp_xd`.]

Target settings: horizon 0.5 s, 20 intervals, 25 ms control period, nonlinear **SQP**, Gauss–Newton Hessian, **FULL_CONDENSING_HPIPM**, and two-stage, one-step implicit Runge–Kutta (the fourth-order A-stable Gauss collocation scheme discussed in T). Base default SQP_RTI is explicitly overridden to SQP in `experiments/config/peg_6/_target_config_core.yaml`; it is not evidence the target runs used RTI. [T §§4.2, 6.1; `C/controller.py::_build_ocp`.]

Implementation uses a **LINEAR_LS** residual including quaternion component differences, rather than an explicitly geodesic attitude cost. `run_optimization` aligns quaternion signs along the horizon with the initial state to avoid penalizing antipodal representations of the same rotation. Solver output/status and KKT residuals are logged; one successful solve status is not proof of global optimality or closed-loop convergence. [C/controller.py, `_build_ocp`, `run_optimization`.]

### 4.2 Contact-wrench augmentation — D/I/E, interpretation A

Six extra states \(\lambda=(\lambda_f,\lambda_\tau)\) yield

\[
\dot v=a_{\rm ff}+M_p^{-1}(w_{{\rm fb},p}+\lambda_f),\quad
\dot\omega=\alpha_{\rm ff}+M_o^{-1}(w_{{\rm fb},o}+\lambda_\tau),
\quad\dot\lambda_f=-b_{env}v,\quad\dot\lambda_\tau=-b_{env,o}\omega.
\]

This is a smooth isotropic local elastic model initialized with measured wrench at each solve, not geometric multi-contact, friction-cone or unilateral-complementarity optimization. There are **20 implemented states**, including clock, versus 19 physical augmented states in the equations. Contact preparation rotates measured torque. `ContactSwitchingMPC.run_optimization` chooses free/contact branches by measured wrench norm (target threshold 0.001); the free branch zeroes initial wrench, while the contact branch retains it. [T §4.3, Eqs. 4.15–4.17; P p. 47; `C/contact_aware_mpc.py::ContactAwareMPCController`, `_lambda_dynamics`, `_prepare_initial_state`; `C/switching_mpc.py::ContactSwitchingMPC.run_optimization`.]

Target coefficients are 266.31 and 0.14489, force/torque cost weights zero and wrench-state bound 500. This is not a demonstrated force-regulation objective. Zero stiffness gives \(\dot\lambda=0\), not \(\lambda=0\); initialized force remains a constant disturbance. The zero-stiffness ablation is therefore not equivalent to contact-blind MPC. [Contact/strategy target YAML; §8.]

### 4.3 Projection and reference progression — D/I/E

`E/path_projection.py` projects perceived position onto polyline segments, computes closest distance/progress and maps arc length to time. Scenario time estimates are blended with weights proportional to \(d_i^{-\beta}\), safeguarding near-zero distances; target sharpness is 1. Position-only geometry cannot uniquely identify orientation/contact mode. `C/tracking_mpc.py::_compute_blend_t0` supports projected progression alongside wall-clock progression and builds the horizon reference. This is a geometric heuristic, not a probabilistic state estimator. The tested projected-time variant underperforms clock-based execution. [T §§4.2, 5.1, 6.3.]

### 4.4 Stagnation and recovery — D/I/E

`C/recovery.py::StagnationDetector.update` tracks recent arc progress and triggers when it falls below \(\alpha v_{stag}t_{bloq}\), with near-end suppression and buffer resets. Main values are 0.3 s, 0.9, approximately 71.8 mm/s, giving a **19.4 mm progress threshold** over the window. This is not simply contact-force thresholding. [T §§5.2–5.3; target YAML.]

- **TangentialOffset:** distance-weighted scenario tangents define a normalized direction; reference displacement ramps at 0.1 m/s over 0.8 s (up to 80 mm). Target `fix_projection: true` freezes projection during recovery. It changes the impedance equilibrium/reference, not measured state or directly prescribed search velocity. [T §5.3; `TangentialOffset.on_stagnation`, `step`, `_weighted_tangent`.]
- **SpiralSearch:** persistent discrete search offset, 8 angular steps/ring, 10 mm initial radius, 40 mm cap and 10 mm ring increments; basis fixed at first trigger. `is_active=False` and a no-op `step` mean there is no tangential-style 0.8 s active/reset interval. Further stagnation events advance the search. [T §§5.3, 6.5; class and target strategy YAML.]
- **SpiralDecoy:** continuous reference spiral, 5→40 mm over 0.8 s, 1.5 turns (675°/s), then cleared. It is not the persistent discrete algorithm. [Same evidence.]
- **TrajectorySwitch:** bans the active scenario and selects another. Code contains ban-clearing/progression options and no direct reference-position offset or active refractory interval. Time-mode evaluation does not establish failure of every possible path-mode switching policy. [T §6.5; class and strategy YAML.]
- **RealNearestTangentialOffset:** diagnostic oracle uses true geometry, changing both distances and tangents; it does not isolate distance weighting alone. **CheatTangentialOffset** uses true perception discrepancy and is not deployable with unknown offset. [T §6.5; corresponding classes.]

Recent-motion tangential, lateral/random and composite strategies also exist. Their artifact-supported results are separated from the principal reported comparison (§7).

## 5. Software and repository architecture

| Component | Evidence and role | Qualification |
|---|---|---|
| Plant/reference input | `raptico_problem_data/peg_in_hole/peg_6/`, YAML, MuJoCo XML/meshes | Inherited planning/geometry, not planner authorship |
| Symbolic OCP | `C/controller.py`, `C/contact_aware_mpc.py` | CasADi/acados free/contact prediction and solver construction |
| Execution | `C/tracking_mpc.py`, `E/run_experiments.py` | Reference, perception, feedback, solver, physics stepping/logging |
| Geometry | `E/path_projection.py`, `E/quat_utils.py` | Polyline progress, arc/time mapping, quaternion interpolation |
| Recovery | `C/recovery.py` | Detector, strategy interface, practical/oracle perturbations |
| Batteries | `experiments/run_battery.py`, `experiments/config/`, `experiments/offsets/` | Named branches, grids, sweeps and resolved config |
| Artifacts/figures | `experiments/runs/`, `E/make_fig_success.py`, `experiments/audit_results.py` | CSV, HDF5, JSON, video, aggregate figure lineage |
| Numerical audits | `experiments/bench_substep_feedback.py`, `experiments/bench_gyroscopic_term.py`, `experiments/audit_gyroscopic_term.py` | Identifiable procedures, not executed here |
| Extensions | `C/stiffness_estimator.py`, `C/anisotropic_cost.py`, additional contact classes | Implementation evidence beyond evaluated main model |
| Documents | `docs/thesis`, `docs/final_presentation/` | Thesis submodule, presentation/plots and duplicate exports |

Explicit technologies: **Python, NumPy, CasADi, acados, HPIPM, MuJoCo, YAML, HDF5/h5py logging interfaces, Matplotlib, LaTeX, Git/submodules**. Generated C solver files establish an acados toolchain, not separately demonstrated handwritten C expertise. Quadrotor examples, robot models and legacy notebooks are not proof of thesis hardware execution.

Relevant history: metric logic is identifiable at `c79fc69` (July 19); a large code import appears in `f999e46` (September 14), config/presentation tracking in `51b1141`, and presentation completion in `54427e2` (September 23). Thesis submodule history includes August final-text corrections and later figure updates. Bulk imports/current dirty content limit reconstruction of the exact August executable. They also prevent exclusive authorship attribution to every line or inherited dependency.

## 6. Implementations and computational workflows

### Main simulation pipeline

1. Load problem YAML, common reference/scenario trajectories, matching MuJoCo scene, and inertia parameters.
2. Resolve named controller/reference/recovery configuration and offset grid; battery expansion saves configuration for each run.
3. Construct perceived state each control step; project scenario progress, update stagnation/recovery and form the horizon reference.
4. Solve MPC and keep the first feedforward acceleration; impedance-only branches omit predictive feedforward. Combine with feedback into wrench.
5. Hold feedforward across physics substeps while **recomputing impedance feedback each substep**; advance MuJoCo and log true/perceived/reference state, contact/wrench, solver timing/status, progress and recovery.
6. Write HDF5/JSON per-offset evidence, CSV metrics and selected aggregate figures. [T §§4.2, 6.1, Appendix A.5; `E/run_experiments.py`, `C/tracking_mpc.py`, `C/run_log.py`, battery/config and plotting sources.]

Target physics timestep 0.00073 s and rounding 0.025/0.00073 produce 34 substeps: **0.02482 s** simulated per nominal 25 ms step. For 176 steps this is 4.36832 s versus nominal 4.4 s. Physics and reference/control schedule are not exactly equal. This is not a wall-clock real-time execution test.

For example, run A (defined below), `blind_mpc_no_recovery/offset_000_0.meta.json`, reports 176 steps, `[101,13]` reference shape, five projected scenarios, MuJoCo dynamics, solver statuses `[0]`, mean solve approximately 15.01 ms and max KKT residual approximately \(9.56\times10^{-7}\). Its final reference-tracking error is about 0.189 m, a different quantity from insertion-goal error. It must not be substituted for a success predicate. Its top-level keys are timestamp/config/summary/projection/logs_h5_file, without a per-run Git revision.

### Additional implemented variants

The contact source includes planar-normal, Han-style, unilateral and adaptive variants. `C/stiffness_estimator.py` estimates local stiffness from displacement/force increments:

\[
\Delta\Lambda\approx-K\Delta P,\qquad
K=-\Delta\Lambda\Delta P^T(\Delta P\Delta P^T+\rho I)^{-1},
\]

then symmetrizes and clips/projects eigenvalues to bounded PSD stiffness. Defaults include window 20, regularization 1, stiffness limits 10–5000 and displacement gating. `C/anisotropic_cost.py` adds contact-normal-oriented position cost of the form \(\alpha nn^T\) with force/trajectory information. These are **implemented**, not proven better, not necessarily final-submission methods, and not established as executed in the headline comparison. Generated solver files alone do not provide that result evidence.

## 7. Experiments, evaluation and results

### 7.1 Design and lineage

The principal test is **121 planar translational perception offsets**, one hexagonal geometry and one planning instance. It is a systematic grid, not independent random population sampling. T's practical difference threshold of about 2.5 percentage points (three offsets) is not a significance test or confidence interval. [T §§6.1–6.2.]

| ID | Directory beneath Runs | Supported comparison |
|---|---|---|
| A | `peg_6/25_03_11_28/grid/20260811_034501_target_config_core` | Main impedance/MPC/projection |
| B | `peg_6/25_03_11_28/grid/20260813_011410_tc_contact_core` | Contact and zero-stiffness |
| C | `peg_6/25_03_11_28/grid/20260813_040416_tc_recovery_strategies` | Spirals, oracle, alternatives |
| D | `peg_6/25_03_11_28/grid/20260813_090811_tc_alpha_ablation` | Detector sensitivity |
| E | `peg_6/25_03_11_28/grid/20260813_153132_tc_preview_sweep_25ms` | Preview at fixed control rate |

Each contains `metrics.csv`. `E/make_fig_success.py::RUNS_TC` explicitly selects target runs, with search fallback. Earlier 40 ms and older strategy runs are not interchangeable with the target 25 ms comparisons; config comments explicitly describe replacing non-comparable older strategy data. The trusted inspection script counted 41 selected saved experiment branches, preserving paths/hashes in `run_summary.json`.

### 7.2 CSV-verified classifications

| Branch | No recovery | Tangential recovery | Evidence |
|---|---:|---:|---|
| Direct impedance | 47/121 | 68/121 | A; T §6.2 |
| Contact-blind impedance MPC | 47/121 | 66/121 | A; T §6.2 |
| Projected-time reference | 32/121 | 58/121 | A; T §6.3 |
| Contact-aware MPC | 47/121 | 67/121 | B; T §6.4 |
| Zero-stiffness augmented | 46/121 | 67/121 | B; T §6.4 |

Under the **saved classifier**, recovery helps; predictive feedforward and the tested force extension do not improve on recovered direct impedance. The zero-stiffness ablation cannot isolate absence/presence of measured-force prediction (§8).

Strategy C gives **78/121 discrete spiral**, **74/121 continuous spiral**, **106/121 true-geometry oracle**, and **47/121 switching**; tangential's comparator is A's 68/121. Other C branches: recent-motion tangent 72/121 (lookback 5), 67/121 (lookback 10), lateral 63/121 and composite 53/121. These extra rows are not all principal thesis conclusions. T reports exact-offset cheat 121/121; its algorithm exists, but that count was not independently matched in the selected target CSV summary. Missing linkage is not proof the experiment never ran. [T §6.5, Table 6.7/Fig. 6.7; target strategy YAML/CSV.]

47→78 means **31 additional offsets, 25.6 percentage points or about 66% relative improvement**. P's “66%” is not 66 percentage points or a demonstrated real-world probability.

### 7.3 Sensitivities, other instances and timing

- D gives 51, 51, 55, 66 successes for \(\alpha=0.01,0.3,0.5,0.7\); main \(0.9\) gives 68. This supports sensitivity, not a universally optimal threshold. [T §6.2.]
- Fixed-25-ms horizons 0.2/0.4/0.5/1.0 s give recovered counts 69/67/66/66, unrecovered 47 each (0.5 s from A). Longer preview does not help this setup. Reported mean solve times are about 3.9/7.2/10.2/17.5 ms, not independently recalculated here. [T §6.2; E.]
- Smaller-scenario runs include `peg_6/_escalability_full121/20260813_134511_tc_escalability_b_14_07_10_13` (30→52/121) and a run ending `tc_escalability_b_14_07_10_29` (25→35/121). Full paths are in the cached summary and figure selection. They change scenario/planning instance on the same geometry. [T §6.6.]
- `test_lab/_escalability_check/20260813_114025_tc_test_lab_check` gives 4→5/25; its name is **not hardware evidence**.
- T reports median solve times 9.3 ms with recovery versus 13.2 ms without, first-solve medians about 21–28 ms, and deadline overruns: median fractions about 0.6%/3.4%, only 44/121 recovered and 8/121 unrecovered offsets with no overrun. Simulation waits for solving before physics advances. This does not demonstrate hard-real-time robot execution. [T §6.2.]

### 7.4 Defense additions

P p. 31/TeX and `docs/final_presentation/scripts/make_success_maps.py` show an L1/rhombus planning region at 25 mm versus displayed robust region at 30 mm. Area ratio \((30/25)^2=1.44\) means **44% geometric area increase**, not 44% success-rate improvement. The drawing script explicitly selects 30 mm. Sampled 100% inside a displayed region is not continuum robustness, and inherits the metric uncertainty. Related scripts use L1 offset size, not necessarily Euclidean magnitude. Tangential maps and spiral counts must not be merged into an unsupported single guarantee.

Later P backups report high success values from other researchers' learned systems, not thesis experiments. Main interpretation/comments allow that the best practical result needs no MPC. No learned policy is demonstrated.

### 7.5 Appendix experiments and raw-data limits

Appendix A.5 reports that holding full wrench across substeps causes force jumps/instability, whereas held feedforward plus recomputed feedback improves execution. Reported force-jump medians are about 7.3 N versus 0.003 N, with lower final error. A matching benchmark procedure exists, but the table was not independently reconstructed from matched outputs: **documented experiment plus code**, not verified numerical reproduction.

Appendix A.6 reports gyroscopic torque ratios (median about 0.07%, 95th percentile 1.1%, worst 8.3%) and generally small short-horizon angular discrepancies, reduced by stronger rotational feedback. Benchmark/audit scripts exist. This supports a tested low-speed modeling simplification, not generally neglecting gyroscopic dynamics.

Raw `.h5`, JSON and video artifacts exist, but this environment lacks h5py/HDF5 command-line access; nothing was installed. Raw final-pose success, timing distributions, contact histories and appendix quantities were not independently reevaluated. Static schema/CSV inspection does not replace that computation.

## 8. Cross-source consistency and discrepancies

### 8.1 Critical: success definition and goal — D/I/E/A

T §6.1 p. 41/Table 6.2 p. 43 defines success as **true final position within 2.5 mm of the final reference node**. Matching configs instead specify **`success_threshold_m: 0.012`** and a separate settled goal near \((0.007793,-0.006680,0.051600)\) m. `E/run_experiments.py` approximately lines 575–634 computes **minimum position error over the trajectory**, classifies `min_err < success_thr`, and stores that minimum as `final_pos_err_mm`.

Comments explain the final reference can pass through walls and that a settled zero-offset pose around step 85 was chosen before later simulation drift. Thus goal, tolerance and minimum-over-time semantics are intentional choices, not extraction errors. Plotting reads saved flags unchanged; those flags reproduce headline counts. Metric logic predates August runs in Git history, so the conflict cannot simply be dismissed as a later default change.

A **sensitivity calculation only**, applying 2.5 mm to A's stored minima around the **same settled goal**, yields impedance 40→44, MPC 40→45 and projection 22→21. This is **not** the thesis criterion: time aggregation and goal are still different. It shows material predicate dependence, not corrected insertion counts.

Consequently 47→78 and related figures must be described as saved-metric classifications. Do not claim 78/121 final insertions met 2.5 mm without clarification/raw-log evaluation. This does not negate the implemented methods or simulated trajectories.

### 8.2 Contact ablation and calibration — A

T/config comments say zero wrench derivative recovers contact-blind dynamics. Code retains initialized measured wrench in the contact branch; zero stiffness means constant predicted disturbance. That limits the ablation's causal interpretation.

`ContactAwareMPCController.stiffness_from_solref` documents \(K=m/\tau^2\). The target solref is 0.1 s, but mass about 0.666 kg gives about 66.6 N/m rather than recorded 266.31, a factor near four; rotational coefficient has a corresponding scale issue. An earlier 0.05 s setting, effective contact mass or another calibration might explain it, but none is established here. Exact MuJoCo-spring matching is unverified.

### 8.3 Frames and model agreement — A

T §2.1 calls angular velocity body-fixed, while Ch. 4 writes left quaternion multiplication. `E/quat_utils.py` uses \(q_1q_0^*\); controller skew-matrix dynamics use left multiplication, while `E/impedance_dynamics.py::Phi_d_ca` uses right multiplication. Contact preparation rotates measured torque into body coordinates. A full frame/sign audit is needed. Execution wrappers also differ in actuator-sign handling; branch context matters, so this document does not diagnose a universal sign error.

### 8.4 Recovery semantics — A

The blanket 0.8 s refractory/reset description does not apply to discrete spiral or switching. True-geometry oracle changes tangents as well as distances. Switching's time-mode result and ban-clearing machinery should not be compressed into a general failure of path switching.

### 8.5 Other qualifications and resolved differences

- September bulk imports and dirty presentation prevent exact August executable identification from HEAD alone; sampled metadata does not establish per-run commit provenance.
- Thesis submission/signature is August 2026, but disclaimer date reads 17.08.2025; likely clerical, not silently corrected. Defense revisions postdate submission.
- Base SQP_RTI versus target SQP is **resolved by configuration**. Physical 13/19 versus implemented 14/20 states is **resolved by the clock state**.
- T has a CC BY 4.0 statement; P carries Siemens restricted markings. No legal conclusion is drawn. Clarify disclosure before public reuse.
- Hard-real-time, manipulator deployment, full rotational uncertainty and continuum robustness are not established.

## 9. Verified technical knowledge and experience

Substantial evidence supports engagement with:

- Rigid-body pose/twist, quaternion errors/SLERP, Cartesian impedance and mass/stiffness/damping scaling.
- Smooth nonlinear MPC embedding feedback; direct multiple shooting, symbolic dynamics, clock augmentation, SQP/Gauss–Newton, implicit RK and condensed QP solution.
- Measured-wrench state prediction, local elastic approximations and contact switching, with model limitations during mode changes.
- Polyline scenario projection, arc/time mapping, distance-weighted reference construction and progress-based stagnation detection.
- Reference-level tangential/spiral recovery and diagnostic true-state/oracle comparisons.
- Python scientific software integration, MuJoCo simulation, multirate feedback, YAML-driven sweeps, HDF5/CSV/JSON logging and comparative analysis.
- Sensitivity/audit methodology for preview, detector threshold, scenario size, substep feedback and gyroscopic simplification.

The strongest evidence combines mathematical formulations, corresponding code/config, figure-to-run linkage and saved per-offset artifacts. This is implemented simulation research, not only a literature review. It does not establish exclusive authorship of inherited planning, third-party code or every imported file. Thesis authorship/context supports participation, but precise individual implementation boundaries remain open.

Relevant future categories: control theory; optimization; dynamical systems and robotics; numerical mathematics; simulation/scientific computing; experimental evaluation. Machine learning is principally background/future direction, not a demonstrated trained controller. No thematic files are generated.

## 10. Proposed, incomplete or uncertain work

- **Proposed:** robot-hardware deployment/full manipulator integration, vision/perception updates, realistic friction/uncertainty, systematic rotational recovery and broader geometries. [T Ch. 7.]
- **Proposed:** residual RL/learning adaptation; literature does not establish trained policies, demonstration datasets or RL experiments. [T §§3.4, 7.2; P backups.]
- **Implemented, experimental benefit unestablished here:** adaptive/anisotropic/planar/unilateral variants and stiffness estimation. Presence alone proves neither success nor abandonment.
- **Documented, specific output not independently matched:** cheat's 121/121 and all appendix benchmark numbers. Missing linkage is not absence of work.
- **Uncertain:** strict final-insertion counts, continuous robustness, exact run revisions, angular-frame agreement, disclosure permissions and individual component authorship.

## 11. Open questions requiring user clarification

1. **Highest priority — success:** Which should govern the final profile: written final-state/final-reference 2.5 mm or saved minimum-over-time/settled-goal 12 mm? Was the written definition superseded, and are corrected labels available?
2. **Run provenance:** Is there an archived environment/checkout/branch identifying the executable used for August target runs?
3. **Contact model:** Was retaining measured force under zero stiffness intentional? What calibration yielded 266.31/0.14489 with solref 0.1 s?
4. **Frames:** Which angular-velocity/quaternion/torque convention governed the evaluated branch, and was it audited?
5. **Additional evidence:** Where are cheat/appendix benchmark outputs? Were actual hardware tests performed outside these sources?
6. **Attribution/disclosure:** Which components were personally developed versus inherited/collaborative, and which details may be used publicly?

These do not block the reconstruction, but constrain a later validated profile, especially quantitative achievement/deployment claims.

## 12. Evidence coverage and overall assessment

Selected implementation hashes freeze the most consequential inspected bytes independently of the regenerable cache:

| File | SHA-256 |
|---|---|
| `E/run_experiments.py` | `ccecbfb1f5585715097983461f941b48201d1f1cc30b81a71d48ca017dea3c13` |
| `C/controller.py` | `1d17620814faf9680426db44c807735ab244f8527f2343ecc5d4dd506c614d7f` |
| `C/contact_aware_mpc.py` | `7d162b84eaf9a87a037c749a2baaa36345152a3220de15469f3bf5e5d189df53` |
| `C/recovery.py` | `53d3cfe136c91bd77ebc5c100831244961e40d08f6e0ad67fd950d42af6636f5` |

| Source area | Coverage/disposition |
|---|---|
| T Ch. 1, pp. 1–5 | Motivation, objectives and scope |
| T Ch. 2, pp. 7–14 | State/perception/impedance and inherited planning |
| T Ch. 3, pp. 15–22 | Contact/learning/search literature separated from implementations |
| T Ch. 4, pp. 23–31 | OCP, prediction, solvers/interpolation, force model checked against code |
| T Ch. 5, pp. 33–39 | Projection/detector/recovery, implementation differences |
| T Ch. 6, pp. 41–57 | Main/sensitivity/strategy/scenario results and metric audit |
| T Ch. 7, pp. 59–64 | Conclusions and proposed work distinguished |
| T Appendix A, pp. 65–72 | Baselines, physics/interpolation, feedback/gyro audits, limits stated |
| T end matter | Terminology/bibliography and date/license issues |
| P pp. 1–39 | Main narrative/results and robustness; repeated builds consolidated |
| P pp. 40–48 | Mathematical/implementation backups checked with TeX/T |
| P pp. 49–70 | Literature backups, not own experiments |
| R | Core code, configs, offsets, relevant artifacts/plots and targeted history; irrelevant duplicates not exhaustively cataloged |

The chain is traceable: uncertain-pose assembly → impedance predictive execution/progress-triggered recovery → CasADi/acados/MuJoCo implementation → named config/runs → count-matched comparisons. Evidence for substantive implemented work is strong. The major weakness is whether the written success narrative uses the artifact goal/predicate, not whether technical work exists. That distinction and the provenance/frame limits must survive later compression.

### Completion checkpoint

Earlier source/research/implementation checkpoints have been expanded after mathematical, code, configuration, history and CSV checks. Courses and the scientific paper were not reprocessed. The existing manifest retains `ma6018` final-profile status **not_started**, while recording reconstruction completion and its review prerequisite in the next action. Next logical step is user review of §11, then separately authorized final profiling or narrowly scoped metric/frame verification. Neither was begun here.
