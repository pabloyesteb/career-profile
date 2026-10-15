# Nonlinear Optimization (MA3503)

## Module metadata

| Field | Value |
|---|---|
| Official title | Nonlinear Optimization |
| Module code | MA3503 |
| ECTS | 5 |
| Grade | 2.0 |
| Teaching term | Winter semester 2024/25 |
| Profile status | complete_validated |

## Evidence base and material structure

The transcript course is exactly matched to `NLOA (W24_25)_20261012_1553.zip`. Its materials identify the teaching unit as **Nonlinear Optimization: Advanced**, taught by Prof. Michael Ulbrich and Dr. Florian Lindemann in Winter 2024/25. The archive contains seven two-page exercise sheets and seven corresponding solutions (38 pages), for 52 PDF pages in total, plus an export index. The sheets form an ordered progression from constrained optimality theory through sequential quadratic programming and barrier methods.

No lecture notes, lecture slides, examination, program code, or datasets are present, although the sheets cite lecture-note theorem/equation numbers and three Moodle tests. The profile therefore reconstructs the locally evidenced syllabus from every problem and official solution, but does not claim topics that might have appeared only in the missing lectures or tests. Mathematical notation was recovered with layout-preserving text extraction and checked directly in the PDFs where extraction degraded cones, transposes, or multiplier symbols.

## Technical content

### Existence, convexity, and variational optimality

*Evidence: `NLOA (W24_25)_20261012_1553.zip :: Exercise materials/Exercise Sheet 1.pdf`, pp. 1–2, and `Solution Exercise Sheet 1.pdf`, pp. 1–5.*

- Existence of global minimizers for continuous objectives on closed feasible sets under coercivity, and on compact sets by the Weierstrass theorem. Counterexamples distinguish these assumptions from openness, convexity alone, and strict convexity on unbounded sets.
- Strong convexity as a sufficient mechanism for coercivity and uniqueness/existence on a nonempty closed convex set; strict convexity gives uniqueness when a minimizer exists but not existence by itself.
- Bouligand tangent cones and their explicit representation for convex feasible sets as the closure of positively scaled feasible directions. Basic properties include conic structure, closedness, the full-space tangent cone at interior points, and convexity for convex sets.
- First-order variational inequality `grad f(x_bar)^T(w-x_bar)>=0`: necessary for a differentiable objective over a convex set, and sufficient for global optimality when the objective is convex.
- Existence and uniqueness of Euclidean projection onto a nonempty closed convex set. The fixed-point condition `x_bar=P_X(x_bar-tau grad f(x_bar))` characterizes convex constrained minimizers for any positive step size, connecting variational inequalities to projected-gradient stationarity.
- A strict first-order growth condition on every nonzero tangent direction is proved sufficient for a strict local minimizer even without convexity.

### Constraint geometry and constraint qualifications

*Evidence: archive members `Exercise Sheet 2.pdf` / `Solution Exercise Sheet 2.pdf`, all pages; `Exercise Sheet 3.pdf` / `Solution Exercise Sheet 3.pdf`, pp. 1–4; `Exercise Sheet 4.pdf` / `Solution Exercise Sheet 4.pdf`, LICQ and slack-variable problem; `Exercise Sheet 5.pdf` / `Solution Exercise Sheet 5.pdf`, CQ2 problem.*

- Nonlinear feasible sets `X={x:g(x)<=0,h(x)=0}`, active inequality sets, the true tangent cone, and the linearized tangent cone obtained from active constraint gradients.
- Equality of the linearized cone with the tangent cone of the first-order affine constraint model. Examples show how zero gradients or higher-order geometry can make the linearized cone a poor approximation.
- Abadie constraint qualification (equality of tangent and linearized cones) versus Guignard constraint qualification (equality of their polar cones). Constructed planar sets show failure of both and a case where GCQ holds while ACQ fails.
- Mangasarian--Fromovitz constraint qualification (MFCQ), generalized MFCQ with equalities, and its relation to feasible strict directions. For convex inequalities and affine equalities, Slater's condition is shown equivalent to generalized MFCQ at feasible points in the exercise setting.
- Linear independence constraint qualification (LICQ), including preservation under transformation of inequalities into equalities with nonnegative slack variables.
- A second-order constraint qualification (CQ2) based on feasible twice-differentiable arcs. An example demonstrates that first-order cones may coincide while CQ2 fails, so a second-order necessary condition cannot be invoked.

### KKT theory and Lagrange multipliers

*Evidence: archive members `Exercise Sheet 3.pdf` / `Solution Exercise Sheet 3.pdf`, all pages; `Exercise Sheet 4.pdf` / `Solution Exercise Sheet 4.pdf`, pp. 1–3; `Exercise Sheet 7.pdf` / `Solution Exercise Sheet 7.pdf`, miscellaneous KKT problem.*

- Karush--Kuhn--Tucker conditions for mixed inequality/equality constraints: primal feasibility, nonnegative inequality multipliers, stationarity of the Lagrangian, and complementary slackness.
- MFCQ as a condition supporting KKT necessity. Conversely, a KKT tuple implies the first-order tangent-cone necessary condition through stationarity, complementary slackness, and the inclusion of the tangent cone in the linearized cone.
- Strict complementarity and nonuniqueness of Lagrange multipliers. A geometric three-constraint example computes the full multiplier set while exhibiting failure of strict complementarity.
- The multiplier set at a KKT point is closed; a normalization/subsequence argument shows that MFCQ rules out unbounded multiplier sequences and therefore makes the multiplier set bounded.
- For convex constraints and a strictly convex objective, KKT points are unique in the primal variable. LICQ yields uniqueness of the multiplier tuple by linear independence of active constraint gradients.
- Slater's condition validates KKT analysis for the Celis--Dennis--Tapia subproblem with a trust-region constraint and a second norm constraint.

### Second-order optimality and quadratic growth

*Evidence: archive members `Exercise Sheet 4.pdf` / `Solution Exercise Sheet 4.pdf`, second-order problems; `Exercise Sheet 5.pdf` / `Solution Exercise Sheet 5.pdf`, CQ2 and second-order necessity.*

- Critical/positive tangent cones determined by active constraints and positive multipliers, and the Hessian of the Lagrangian restricted to these directions.
- Second-order sufficient conditions at a KKT tuple imply a strict local minimizer. The exercises apply the condition even when an active constraint has zero gradient, after explicitly deriving the relevant critical cone.
- A contradiction and normalized-direction argument strengthens the second-order sufficient condition to local quadratic growth: `f(x)-f(x_bar)>=alpha ||x-x_bar||^2` for nearby feasible points.
- Second-order necessary conditions depend on an appropriate second-order constraint qualification. The course gives a degenerate example with many KKT multipliers where the Lagrangian Hessian is not positive semidefinite on the proposed cone, without contradiction because CQ2 is violated.
- Debreu's lemma: positivity of a symmetric matrix on the null space of a constraint matrix can be extended to global positive definiteness by adding a sufficiently large quadratic constraint term. The solution both uses and proves the lemma in the augmented-Lagrangian context.

### Penalty and augmented-Lagrangian methods

*Evidence: `NLOA (W24_25)_20261012_1553.zip :: Exercise materials/Exercise Sheet 5.pdf`, pp. 1–2, and `Solution Exercise Sheet 5.pdf`, pp. 3–7.*

- Exact penalty functions `f+alpha*pi`: once exactness holds locally at a threshold penalty, it persists for larger penalties. If both the original objective and an exact nonnegative penalty are differentiable at a constrained local solution, their gradients vanish separately; this illustrates why useful exact penalties are generally nonsmooth at active constraints.
- Quadratic penalty for equality constraints and the augmented Lagrangian `f(x)+mu^T h(x)+(alpha/2)||h(x)||^2`.
- Under KKT and second-order sufficiency, fixing the correct multiplier and choosing a sufficiently large penalty parameter makes the augmented Lagrangian locally exact in the unconstrained sense.
- A modified quadratic-penalty iteration solves stationary subproblems for increasing penalty parameters. Under convergence and LICQ, the scaled residual multipliers are expressed by a least-squares normal-equation formula, converge, force feasibility, and yield a limiting KKT pair.

### Sequential quadratic programming

*Evidence: archive members `Exercise Sheet 6.pdf` / `Solution Exercise Sheet 6.pdf`, all pages; `Exercise Sheet 7.pdf` / `Solution Exercise Sheet 7.pdf`, pp. 1–3.*

- SQP subproblems combine a quadratic Lagrangian model with first-order linearizations of inequality and equality constraints. Convex original inequalities and affine equalities guarantee subproblem feasibility when the nonlinear problem is feasible; a circle/equality example demonstrates that feasibility can otherwise fail.
- Globalized SQP with step sizes and QP multipliers. Under convergence to a KKT triple and step sizes bounded away from zero, steps vanish and the QP active set eventually contains no constraint inactive at the limit.
- Complementarity of QP multipliers, and finite active-set identification under strict complementarity: eventually the QP and limiting nonlinear active sets coincide.
- For a convex quadratic program with affine constraints and a positive-semidefinite Hessian, KKT conditions are sufficient. Its exact-Hessian SQP subproblem reproduces the original problem after translating by the current iterate, so one accepted full step reaches a solution.
- The Lagrange--Newton step appears as the equality-constrained special case; a scalar problem demonstrates one-step termination at a KKT pair.
- A nonconvex QP subproblem may be infeasible or may lack a global solution, motivating stabilization.

### Elastic-mode SQP and logarithmic barriers

*Evidence: `NLOA (W24_25)_20261012_1553.zip :: Exercise materials/Exercise Sheet 7.pdf`, pp. 1–2, and `Solution Exercise Sheet 7.pdf`, pp. 1–4.*

- Elastic-mode relaxation introduces nonnegative violation variables for linearized inequalities and positive/negative slacks for equalities. An explicit construction proves that the relaxed SQP subproblem is always feasible.
- Eliminating the elastic variables produces an equivalent nonsmooth objective with positive-part penalties for inequalities and absolute-value penalties for equalities, linking elastic SQP to an `l1` exact-penalty model.
- Logarithmic barrier `B_tau(x)=f(x)-tau sum_i log(-g_i(x))` on the strict interior, with a barrier algorithm that globally minimizes each subproblem while decreasing `tau` to zero.
- The exercise proof establishes monotonic increase of the aggregate log-barrier term and monotonic decrease of the original objective values. Under the stated special assumption that strict interior equals the feasible set, every accumulation point is globally optimal and both objective and barrier values converge to the optimum.

## Algorithms and numerical methods

- Euclidean projection and the projected-gradient fixed-point characterization for convex constrained problems.
- Modified quadratic-penalty iteration with increasing penalties and residual-based multiplier estimates.
- Globalized sequential quadratic programming with QP search directions, line-search step sizes, multiplier updates, active-set identification, and elastic-mode feasibility restoration.
- Lagrange--Newton iteration for equality-constrained KKT systems.
- Interior logarithmic-barrier continuation with a decreasing barrier parameter.

## Computational work and tools

No programming language, numerical software, implementation assignment, or executable code is evidenced. The material is analytical: algorithms are studied through formulations, optimality systems, feasibility, and convergence arguments rather than implemented experiments.

## Applications and model problems

- Euclidean projection onto closed convex sets and projected optimality conditions.
- Convex quadratic programs with affine equality and inequality constraints.
- The Celis--Dennis--Tapia trust-region subproblem with simultaneous step-norm and linearized-residual norm bounds.
- Degenerate nonlinear constraints used to diagnose failures of ACQ, GCQ, CQ2, strict complementarity, uniqueness, and SQP feasibility.

## Exercise and assessment evidence

- All seven official sheet/solution pairs were analyzed. The solutions supply the proofs and counterexamples behind the stated existence, constraint-qualification, KKT, second-order, penalty, SQP, and barrier results.
- The sheets reference Theorems 2.12, 2.21, 2.33, 4.24 and equation (18) from unavailable lecture notes. Their operative statements are restated in the exercises, allowing the corresponding claims to be checked, but the surrounding lecture development is unavailable.
- Three Moodle tests are assigned on Sheets 3, 5, and 6 but are absent from the archive. Their topics and contribution to course coverage cannot be recovered.
- No examination is available for an independent assessment cross-check.

## Thematic categories

- Nonlinear and constrained optimization
- Convex analysis
- Optimality conditions and constraint qualifications
- Sequential quadratic programming
- Penalty, augmented-Lagrangian, and barrier methods
- Numerical optimization

## Coverage validation

| Source structure | Profile coverage | Result |
|---|---|---|
| Sheet 1: existence, convex tangent cones, variational inequalities, projection | Existence, convexity, and variational optimality | Covered |
| Sheet 2: tangent geometry, ACQ, GCQ, first-order sufficiency | Constraint geometry and qualifications | Covered |
| Sheet 3: KKT, MFCQ, Slater, multiplier sets | Constraint qualifications; KKT theory | Covered |
| Sheet 4: uniqueness, LICQ, second-order sufficiency, CDT problem | KKT theory; second-order optimality; applications | Covered |
| Sheet 5: CQ2, exact penalties, augmented Lagrangian, penalty convergence | Second-order optimality; penalty methods | Covered |
| Sheet 6: SQP feasibility, active sets, quadratic programs | Sequential quadratic programming | Covered |
| Sheet 7: elastic SQP, Lagrange--Newton, barrier method | Elastic-mode SQP and logarithmic barriers | Covered |
| Moodle tests, lectures, and examination | Not present | Explicit source limitation; no unsupported reconstruction |

## Sources

- **Transcript metadata:** `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 2.
- **Archive:** `00_sources/tum/archives/NLOA (W24_25)_20261012_1553.zip`.
- **Complete local evidence:** archive members `Exercise materials/Exercise Sheet 1.pdf` through `Exercise materials/Exercise Sheet 7.pdf` and `Exercise materials/Solution Exercise Sheet 1.pdf` through `Exercise materials/Solution Exercise Sheet 7.pdf`.
