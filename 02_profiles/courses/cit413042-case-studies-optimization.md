# Case Studies Optimization

## Module metadata

| Field | Value |
|---|---|
| Course ID | cit413042 |
| Official module | Case Studies Optimization — CIT413042 |
| ECTS | 10 |
| Grade | 1.0 |
| Academic record | Degree module; transcript PDF p. 2 |
| Case-study topic | Trajectory Optimization in Learned Environments |
| Profile status | complete_validated |

This is a course profile of a team case study, not an individual software-contribution audit. The report lists Jose Bedoya, Mariia Iavorskaia, Yelyzaveta Vodovozova, Jiefang Xiao and Pablo Yeste. Neither coauthorship nor the course grade attributes all implementations or results individually.

## Evidence base and reproducibility

- **[R]** `00_sources/case_studies/Trajectories-4.pdf`, 60 physical pages. Printed report numbers are two lower than physical PDF pages after the cover/front matter. All page references below are physical PDF pages. SHA-256: `2593dfc20c1e655304fab438cb15cfc7e4376467262cc353dad6b9d456188733`.
- **[C]** External repository `/home/pablo/TUM/SoSe 25/Case Studies/NLOTrajectories`, revision `934956c78c03d5581505a50652b2ab4302e6baa5`, checked on 2026-10-13. Tracked source files were unmodified; six top-level untracked status entries remain: `Midterm (Case Studies).zip`, `Midterm (Case Studies)/`, `docs/CV - Munique.pdf`, `docs/Midterm__Case_Studies_-5.pdf`, `docs/Trajectories-5.pdf`, and `results/`. Unrelated CV content was not analyzed.
- **[P]** Untracked `docs/Midterm__Case_Studies_-5.pdf`, 105 physical pages with progressive builds: a presentation of the same case-study sequence, ending with optimal-control, shooting, KKT and Newton-step backup slides. The full title sequence was checked against [R], not treated as 105 distinct topics.
- **[R2]** Untracked `docs/Trajectories-5.pdf`, same extracted report text as [R] apart from its internal date (16 September 2025 versus 12 October 2026). Its SHA-256 is `5fbd6df2cc9f4ff297e5bdd8885d5a3822ccaff6e8af58917912cada9b2c5815`. Both covers retain 20 July 2025. The configured local [R] is the citation backbone; file suffix alone does not establish a newer technical revision.

Analysis combined the complete report structure, section-level text inspection, eight rendered equation/table/plot pages, the presentation topic sequence, and static inspection of the Python pipeline, configurations and tests. No repository code, model checkpoint or compiled binary was executed or loaded. The main theoretical and methodological sections are supported directly; experimental outcomes are described as team-report observations, with limitations rather than independently reproduced guarantees.

## Technical content

### Optimal-control formulation and direct transcription

*Evidence: [R], §§1.2–2.2, pp. 6–12; [C], `core/runner.py` (all `core/` paths below are relative to `src/nlotrajectories/`).*

- Continuous optimal control with dynamics `ẋ=f(x,u)`, a running integral plus terminal cost, initial/terminal conditions, state/control path constraints and collision clearance. Contrast this infinite-dimensional formulation with a finite-horizon multistage state-transition problem.
- Dynamic programming/principle of optimality and Pontryagin-type indirect approaches are briefly contrasted with direct methods; the implemented study uses **discretize-then-optimize**, not a Hamilton–Jacobi or costate solver.
- **Single shooting:** parameterize controls, integrate the state from the initial condition, optimize over controls. **Multiple shooting:** introduce interval initial states and impose matching constraints between separately evolved intervals. **Direct collocation:** interpolate states at collocation points, enforce derivative consistency and continuity, and integrate the objective by quadrature.
- Comparison of control-only dimension and sensitivity in single shooting with initialization flexibility in multiple shooting and the sparse, larger NLP of collocation. These are method-design comparisons, not universal runtime rankings.
- The actual runner optimizes state/control arrays with **forward-Euler defect constraints**, `X_(k+1)=X_k+Δt f(X_k,U_k)`. The report calls the selected scheme multiple shooting; implementation evidence is specifically this one-step state/control transcription, not a higher-order integrator or collocation implementation.
- Path-length objective sums smoothed Euclidean segment lengths. Optional quadratic nonnegative slack penalties relax collision constraints; optional input-magnitude regularization trades task length against control effort. Endpoint conditions can constrain the complete state or omit final heading. Time horizon is fixed by `NΔt`; minimum-time optimization is not implemented.

### Point-mass, unicycle, and car kinematics

*Evidence: [R], §3.1, pp. 17–21; [C], `core/dynamics.py`, `core/config.py`, benchmark YAMLs.*

- First-order planar point motion driven by velocity; second-order point motion augments position with velocity and uses acceleration control.
- **Unicycle model:** planar velocity is aligned with heading, `ẋ=v cosθ`, `ẏ=v sinθ`, `θ̇=ω`. Second-order form treats linear/angular velocities as states and their accelerations as controls, giving five states and two inputs.
- **Ackermann/bicycle-type kinematics:** `θ̇=v tanψ/l` with steering angle `ψ` and wheelbase `l`; first-order steering-rate control and a proposed second-order augmentation with longitudinal/steering accelerations. These are planar kinematic models, not tire-force or full rigid-body vehicle dynamics.
- Point, rectangular and triangular footprints are supported in the geometry abstractions. Local footprint vertices are rotated/translated into world coordinates using pose. Collision constraints query the SDF at those transformed points.
- Important limitation: sampled vertices/time nodes are not continuous swept-volume certification. Geometry sampling, safety margins and model approximation affect feasibility; a low cost or successful NLP status does not establish exact collision freedom between nodes.
- The second-order Ackermann source has an apparent derivative/state-order discrepancy and an inconsistent steering derivative factor (detailed below). Its presence establishes coverage of model construction, not a verified correct vehicle simulation.

### Sampling-based initialization and trajectory refinement

*Evidence: [R], §2.3, pp. 12–15; §4.3, pp. 40–42; [C], `core/trajectory_initialization.py`, `scripts/run_benchmark.py`.*

- Straight-line state interpolation, default initialization, and **rapidly-exploring random trees (RRT)** as warm starts for nonconvex trajectory optimization. Graph search (Dijkstra/A*) and learned initialization are introductory alternatives, not implemented benchmarks.
- Basic RRT: sample workspace/goal, find the nearest existing node, steer a bounded distance, test the connecting segment for collision, add the node/parent edge, stop on goal proximity or iteration limit. Parent links recover the geometric path.
- Goal bias, domain bounds, extension step, obstacle margin and iteration cap are configurable. The report contrasts basic RRT's nonoptimal path with **RRT-Connect**, **RRT*** and **Informed RRT*** as named variants; no implementations of those variants are present.
- Path shortcutting removes unnecessary intermediate points after collision checks. A SciPy **CubicSpline** smooths/resamples the planar path; the implementation's `_bspline_curve` name does not make it a B-spline implementation.
- The report's general initialization description includes tangent-derived heading, velocity/angular-velocity and acceleration estimates. The actual initializer returns only XY coordinates and zero-fills other states, corroborated by the later experiment description. It does not initialize controls. A smoothed geometric warm start is therefore not guaranteed dynamically feasible, nor is the post-spline path rechecked everywhere for collision.

### Signed-distance geometry and differentiable approximations

*Evidence: [R], §§2.4–2.5, pp. 15–17; §3.2, pp. 21–26; [C], `core/sdf/casadi.py`, `core/utils.py`, `core/geometry.py`.*

- **Signed distance fields (SDFs):** negative inside obstacles, positive outside, zero on the boundary; enforcing a positive clearance represents obstacle avoidance. Distinguish an exact geometric distance, a smoothed analytic surrogate and a learned field.
- Analytic circular and square distances; polygon boundary distances and inside/outside classification using **Shapely** as the reference geometry oracle. Multiple obstacles are combined through the minimum of individual fields.
- Smooth approximations to absolute value, minimum/maximum and clamping facilitate symbolic differentiation. **Log-sum-exp soft minimum** combines obstacle fields; smoothing changes the represented geometry and can shift the zero contour. Approximate smooth geometry is not identical to the reference SDF.
- Half-elliptical rings and S-shaped/nonconvex obstacles can be approximated by unions of convex trapezoids. Segment projections, signed supporting-line distances and softened min/max operations provide a symbolic surrogate for pieces.
- The report motivates fewer collision functions through a learned environment representation. Query cost, footprint sampling and solver differentiation remain significant: “one learned field” does not mean one scalar constraint for an entire trajectory.

### Neural implicit-field learning and solver integration

*Evidence: [R], §3.2, pp. 21–26; §4.5, pp. 46–50; [C], `core/sdf/l4casadi.py`, `core/nn_architectures.py`, `scripts/run_benchmark.py`.*

- Supervised regression from planar coordinates to geometric SDF values. Compare uniform grids, independent uniform random samples and **boundary-informed sampling**, mixing global samples with points from a distance band around the obstacle.
- Main reported model: two-hidden-layer **MLP**, typically width 128, with ReLU; smaller sigmoid/ReLU models provide simple-geometry comparisons. The code additionally supplies **Fourier-feature MLPs** (learnable cosine features) and **SIREN** sinusoidal layers with frequency-dependent initialization; their availability is not evidence that the report benchmarked them successfully.
- Training uses PyTorch, minibatch **Adam**, shuffled tensors/DataLoader, a 10% validation split and patience/minimum-improvement early stopping with best-state restoration. Code initializes linear layers by Kaiming uniform despite comments calling this Xavier initialization.
- Loss components: SDF-value mean-square error; boundary-focused surface error; **Eikonal regularization** encourages unit spatial-gradient norm. The implementation computes `mean((||∇h||₂−1)²)` via autograd; the report's displayed Eikonal expression differs and is not copied as the implemented formula.
- Validation computes MSE plus optional surface loss but omits the Eikonal term. The code's positional forwarding of `boundary_fraction` also passes it into the `margin` slot of `sample_points`, leaving the actual boundary fraction at its default. Consequently the checked revision cannot by itself reproduce every reported boundary-fraction ablation.
- **CasADi** symbolic NLP construction and automatic differentiation, with **L4CasADi** bridging PyTorch field evaluation and solver derivatives. The repository includes generated C++/TorchScript/compiled-library artifacts; these were inventoried only, not loaded. ReLU fields are piecewise differentiable, not globally twice smooth; using them with Hessian-based solvers requires care rather than assuming smoothness from the word “neural.”

### Nonlinear programming and primal–dual interior-point methods

*Evidence: [R], §3.3, pp. 26–30; [P], backup pp. 104–105; [C], `core/runner.py`.*

- General constrained NLP `min f(x)` with inequalities `g(x)≤0`, equalities `h(x)=0` and a Lagrangian. First- and second-order derivative information enters Newton/KKT systems; continuous first differentiability alone does not ensure Hessians, despite the report's wording.
- **Log-barrier methods:** strictly feasible interior, decreasing barrier parameter, repeated approximate subproblem solves and warm starts. The report prints a plus sign before the logarithmic sum inconsistent with a minimization barrier and its subsequent multiplier equations; that formula is explicitly not endorsed.
- **Primal–dual central path and perturbed KKT conditions:** stationarity, primal feasibility, positive slacks/multipliers and relaxed complementarity `ΛYe=τe`; decreasing `τ` targets a KKT point under the necessary regularity assumptions, not a global solution of a nonconvex problem.
- **Newton step on the perturbed KKT system:** block structure couples the Lagrangian Hessian, constraint Jacobians and slack/multiplier diagonals. **Fraction-to-the-boundary** step selection preserves positivity, allowing distinct primal/dual step sizes. Residual norms measure stationarity, feasibility and complementarity.
- **IPOPT** is the primary solver; the runner also has a CasADi `sqpmethod` branch. Explicit IPOPT settings include iteration limit 1000, tolerance `1e-4`, adaptive barrier updates, quality-function oracle and a barrier tolerance factor. The benchmark entry point does not forward the configured solver type, so configuration support must not be equated with actually selecting SQP there.
- Solver diagnostics include objective, primal/dual infeasibility, barrier parameter, constraint residuals and failure handling. Theoretical central-path discussion is conditional and introductory; no complete convergence theorem for the implemented learned nonconvex planner is established.

### Evaluation methodology and engineering trade-offs

*Evidence: [R], §§2.5 and 4, pp. 16–17 and 30–50; [C], `core/metrics.py`, `core/visualizer.py`, benchmark YAMLs and GUI.*

- Separate **geometric fidelity** from **trajectory/solver performance**. Occupancy **IoU/Jaccard** measures intersection over union; near-zero contour samples support symmetric **Chamfer** average-nearest-neighbor distance and symmetric **Hausdorff** worst-nearest-neighbor distance. SDF-value MSE and surface error reveal different failure modes.
- The report evaluates reference distances on the predicted surface, whereas `metrics.surface_loss` evaluates predicted values at the reference surface. These one-sided surface measures are not interchangeable. Code guards against absent contour points; contour resolution/threshold changes computed distances.
- Benchmark progression: point-mass baseline; second-order unicycle with single/multiple convex obstacles; a star-shaped nonconvex obstacle; Ackermann car in a curved nonconvex corridor. Six repository configuration files and report B0/B1/B2/B3 labels are different organizational schemes, not six entirely independent report chapters.
- Ablations compare analytic/smoothed versus neural SDFs, linear versus RRT initialization, optional relaxation and input regularization, sample distributions/boundary fractions, and convex-decomposition granularity. The control penalty is input magnitude, not jerk or a difference-of-controls penalty, despite some explanatory wording.
- Reported geometric fidelity improves with increased boundary sampling in the tested corridor, while retained global samples protect representation away from the boundary. Finer trapezoid decomposition improves shape fidelity but increases per-iteration solver time without a clear path-objective benefit in the plotted experiment. These are scenario-specific observations, not universal superiority claims.
- Results use objective value, runtime, contour visualizations and control profiles. Inconsistent prose/table values preclude reliable general quantitative performance claims: for example, p. 38 prose says both learned IoUs exceed 0.97, while its table gives 0.8091 for B1.1 and contains a malformed Chamfer entry.
- **Tkinter/Matplotlib GUI:** obstacle/scenario editing, hand-drawn versus optimized trajectory visualization, benchmark invocation and presentation/demo support. YAML/Pydantic configurations separate scenario specification from model/solver classes; pytest contains a geometry test but is not evidence of a passing test suite.

### Supplementary representations and collision-avoidance formulations

*Evidence: [R], Appendix A, pp. 55–60.*

- Literature-review coverage of **conic-duality collision avoidance**: convex obstacles in conic form, dual-cone multipliers, dual-norm constraints and separating certificates. Signed distance as separation distance minus penetration permits minimum-penetration formulations with penalized slack. This is reviewed methodology, not the implemented planner's collision model.
- **Tensor-train SVD (TT-SVD)** for voxelized **truncated signed distance fields (TSDFs)**: clip distances to a narrow band and compress the 3-D grid into low-rank cores. Contrast discrete/compressed representation with continuous derivative access. The appendix explicitly leaves detailed implementation for later.
- **Bernstein-polynomial SDF representation:** normalize local coordinates to `[0,1]`, construct nonnegative partition-of-unity basis polynomials, tensor-product the basis, fit coefficients by least squares, and differentiate analytically with coordinate scaling. The displayed normal-equation inverse requires full column rank; recursive least squares is mentioned as an alternative. A minimum across link fields need not remain globally smooth even if individual expansions are smooth.
- Comparisons cover memory/compute growth with polynomial degree, tensor ranks and voxel resolution, interpretability, data requirements and gradient availability. No TT-SVD/Bernstein implementation or experimental outcome is attributed to the case study.

## Computational tools and thematic categories

**Tools evidenced:** Python 3.12, NumPy, SciPy (`CubicSpline`), PyTorch/autograd/Adam, CasADi, L4CasADi, IPOPT, Shapely, Matplotlib/animation, Tkinter, YAML/PyYAML, Pydantic, Poetry, pytest and formatting/linting configuration. Generated C++/TorchScript artifacts are supporting build products, not proof of individual C++ authorship.

**Applications:** robot/vehicle motion planning, collision avoidance, learned implicit geometry, constrained optimal control, nonlinear-program initialization and interactive engineering demonstrations.

**Categories:** optimization; optimal control; numerical mathematics; dynamical systems and robotics; machine learning; scientific computing; computational geometry.

## Coverage validation and unresolved source issues

All main report blocks map above: introduction/formulation; three direct methods; initialization; SDF/metrics; six dynamic model variants; learning; NLP/barrier/IPOPT; full benchmark progression and GUI; all three appendix topics. The presentation sequence adds no independent major topic. Static code inspection adds neural architectures, training details and implementation qualifications absent from the report prose. Future-work suggestions (dynamic obstacles, uncertainty-aware fields, risk-sensitive planning and real-time MPC extensions) are not claimed as completed implementations.

Significant implementation caveats at the recorded revision:

1. `Ackermann2ndOrder` documents state order `(...,v,ω,ψ̇)` but returns `(...,ω̇,v̇,ψ̈)`, swapping the intended derivative positions. Its steering derivative uses `1/(1+ψ²)` while the heading uses `tanψ`; the report repeats that inconsistent factor. Do not treat either as a verified second-order Ackermann model.
2. The first-order point class has four stored states with two zero derivatives, unlike the two-state report formulation. Benchmark naming and “first/second order” wording also conflict in places.
3. `DotGeometry.sdf_constraints` ignores its slack argument; polygon checking defaults to vertices only. The RRT rectangle-inflation calculation uses the minimum coordinate rather than the complete vertex norm, and spline smoothing is not followed by a full collision recheck. These facts limit safety claims.
4. Trainer sampling arguments, Eikonal/surface definitions and full-state initialization differ between report and code as described above. `use_smooth` sums input squares only through `N−2`, not differences or a complete jerk penalty.
5. The geometry unit test calls `goal_cost`, absent from the current geometry class. No tests were run; this is an observed interface mismatch, not a claimed test result.
6. The PDF title dates and alternate file hashes differ. Additional untracked presentation/source/results are not fixed by the Git revision. Raw experimental reruns, environment reconstruction, bug correction and individual contribution attribution are outside this course-profile task.

These limitations do not prevent identifying the mathematical/computational knowledge covered, but they must accompany later descriptions of implementation reliability or experimental results. No official module description was needed, and no external research/software project was profiled.
