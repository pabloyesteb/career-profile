# Combinatorial Optimization (MA4502)

## Module metadata

| Field | Value |
|---|---|
| Official title | Combinatorial Optimization |
| Module code | MA4502 |
| ECTS | 5 |
| Grade | 4.0 |
| Teaching term | Summer semester 2024 |
| Profile status | complete_validated |

## Evidence base and material structure

The exact-matched archive contains 52 PDFs totaling approximately 523 pages and 27 Python files. Its lecture material comprises a 96-page consolidated script plus 14 dated class-note sets (437 lecture-note pages in total). It also contains 11 exercise sheets with solutions (22 PDFs, 57 pages), Python starter/completion code for six sheets, and 15 student-submitted exercises (29 pages). The consolidated script and official sheets/solutions were treated as authoritative; student submissions were inspected structurally but not used for unsupported claims.

The 96-page script provides the syllabus backbone. All eleven exercise sets and the supplied Python files were audited to identify implementation work, reductions, applications, and techniques not obvious from the chapter headings.

## Technical content

### Algorithmic and optimization foundations

*Evidence: `Lecture Notes/lecture notes.pdf`, Chapter 1, pp. 2–9; Exercise Sheet 1.*

- Directed and undirected graphs, walks, paths, cycles, connectivity, acyclic digraphs, and incidence notation.
- Input-size and asymptotic running-time analysis using `O`, `Ω`, and `Θ`, including the distinction between numeric magnitude and binary encoding length.
- Linear and integer programming formulations, the integer hull, and polynomial-time solvability of linear programs via the ellipsoid method as prerequisites.
- Shortest paths in acyclic graphs, Dijkstra's algorithm for nonnegative edge weights, and Bellman–Ford for negative weights and negative-cycle detection.

### Minimum spanning trees and matroids

*Evidence: `Lecture Notes/lecture notes.pdf`, Chapter 2, pp. 10–21; Exercise Sheets 2–3.*

- Minimum spanning-tree formulation, tree and cut properties, and equivalent optimality characterizations.
- Prim's and Kruskal's greedy algorithms, correctness via cut/cycle arguments, and implementation/runtime tradeoffs.
- Independence systems, bases, circuits, rank-style properties, graphic matroids, and the exchange axiom.
- Matroid characterization through the success of the greedy algorithm for all weight functions; examples and counterexamples involving knapsack, matching, and traveling-salesman independence systems.

### Maximum flow

*Evidence: `Lecture Notes/lecture notes.pdf`, §§3.1–3.5, pp. 22–47; Exercise Sheets 4–5.*

- Capacitated networks, feasible flows, conservation, flow value, cuts, and cut-capacity upper bounds.
- Residual networks, augmenting paths, and the Ford–Fulkerson framework; integrality and the max-flow/min-cut theorem.
- Edmonds–Karp using shortest augmenting paths, Dinic's layered residual networks and blocking-flow phases, and push–relabel/preflow methods using vertex labels and admissible pushes.
- Reduction of feasible `b`-flow questions to maximum flow.

### Minimum-cost flow and circulations

*Evidence: `Lecture Notes/lecture notes.pdf`, §§3.6–3.8, pp. 48–65; Exercise Sheets 6–8.*

- Supplies/demands, `b`-flows, residual costs, circulations, and decomposition of the difference between feasible flows into residual circulations.
- Optimality characterization by absence of negative-cost residual cycles.
- Minimum mean cycle computation by dynamic programming over fixed-length walks, followed by minimum mean cycle-canceling.
- Successive shortest-path method, conservative reduced costs/potentials, feasibility detection, integrality, and runtime dependence on total supply.

### Matching theory

*Evidence: `Lecture Notes/lecture notes.pdf`, Chapter 4, pp. 66–95; Exercise Sheets 9–11.*

- Matchings, perfect matchings, alternating and augmenting paths, and symmetric-difference structure.
- Hall's marriage theorem and König's theorem for bipartite graphs.
- Augmentation algorithms for bipartite matching and the Hopcroft–Karp layered augmentation method.
- Weighted bipartite perfect matching/assignment and the Hungarian method using feasible dual potentials and equality graphs.
- Polynomial reductions between weighted matching and weighted perfect matching.
- Matching in general graphs through minimum-weight `T`-joins; negative-cycle formulations and cycle-cone arguments used in the presented algorithmic development.

## Algorithms and complexity results

| Method | Role | Complexity stated in the notes |
|---|---|---|
| DAG shortest paths | Shortest path in acyclic digraphs | `O(n+m)` |
| Dijkstra with Fibonacci heaps | Nonnegative shortest paths | `O(m+n log n)` |
| Bellman–Ford | Negative-weight shortest paths / negative-cycle detection | `O(mn)` |
| Prim | Minimum spanning tree | `O(n²)` basic; `O(m+n log n)` with an advanced data structure |
| Kruskal | Minimum spanning tree | `O(mn)` presented implementation; near-linear union–find refinement discussed |
| Edmonds–Karp | Maximum flow | `O(m²n)` |
| Dinic | Maximum flow | `O(n³)` bound developed in the notes |
| Push–relabel | Maximum flow | push/relabel operation analysis and an `O(n²m)` implementation bound; faster variants noted |
| Minimum mean cycle | Negative-cycle selection | `O(nm)` |
| Minimum mean cycle-canceling | Minimum-cost flow | polynomial bounds developed from cycle progress |
| Successive shortest path | Minimum-cost `b`-flow | `O(Bnm)`, with reduced-cost improvement discussed |
| Hopcroft–Karp | Maximum-cardinality bipartite matching | `O(√n m)` |
| Hungarian method | Assignment / weighted bipartite perfect matching | `O(n³)` |

## Computational work and tools

- **Language:** Python 3; no third-party library dependency is evidenced in the supplied starter files.
- **Graph representations:** adjacency matrices and custom graph/maze classes, random graph/network generators, capacities, costs, supplies/demands, flows, and residual-network state.
- **Implemented or completed algorithms:** Dijkstra shortest path (Sheet 1), Kruskal MST (Sheet 2), flow-network routines (Sheet 4), push and relabel operations (Sheet 5), minimum mean cycle and cycle recovery (Sheet 7), and minimum mean cycle-canceling for minimum-cost flow (Sheet 8).
- **Programming pattern:** incomplete scaffolds paired with completed reference implementations; students fill selected methods and run the supplied `main.py` drivers. The files were inspected statically and not executed.

## Applications and model problems

- Maze/graph shortest-path computation and random graph experiments.
- Edge-disjoint route feasibility formulated via maximum flow; a planar non-crossing variant highlights the boundary of the reduction.
- Assignment and school-allocation-style matching problems.
- Maximum order-preserving matching via dynamic programming.
- Minimum `T`-joins and the route-inspection/Chinese postman formulation (“Garbage Collecting”), including Eulerian augmentation.
- Feasible transportation/transshipment with capacities, costs, and node supplies or demands.

## Exercise and assessment evidence

- Sheets 1–3 cover asymptotic analysis, shortest paths, MST execution/uniqueness, independence systems, matroid examples, and greedy characterizations.
- Sheets 4–5 add BFS, Ford–Fulkerson behavior, disjoint paths, push–relabel execution, and Python implementation.
- Sheets 6–8 treat `b`-flows, circulations, unbounded negative cycles, minimum mean cycles, cycle-canceling, irrational-capacity behavior, successive shortest paths, and their implementations.
- Sheets 9–11 add matching reductions, dynamic programming for order-preserving matching, Hall's condition, Hungarian execution, minimum `T`-joins, and Chinese postman reduction.
- These exercises add concrete reductions and applications but no major lecture area outside the four backbone chapters.

## Thematic categories

- Combinatorial optimization
- Graph algorithms
- Network flows
- Matching and assignment
- Algorithm design and complexity
- Python algorithm implementation

## Coverage validation

| Source structure | Profile coverage | Result |
|---|---|---|
| Chapter 1: graph/running-time/LP/shortest-path prerequisites | Algorithmic and optimization foundations | Covered |
| Chapter 2: MST and matroids | Minimum spanning trees and matroids | Covered |
| Chapter 3: maximum and minimum-cost flows | Maximum flow; minimum-cost flow and circulations | Covered |
| Chapter 4: bipartite, weighted, and general matching | Matching theory | Covered |
| Eleven sheet/solution pairs | Exercise and assessment evidence | Covered; reductions and applications incorporated |
| Python scaffolds and solutions | Computational work and tools | Covered; all 27 files inspected statically by path and symbols |

## Sources

- **Transcript metadata:** `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 2.
- **Archive:** `00_sources/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- **Backbone:** archive member `Lecture Notes/lecture notes.pdf`, pp. 1–96, Chapters 1–4.
- **Lecture cross-check:** archive members `Lecture Notes/class notes for 19 April.pdf` through `class notes for 19 July.pdf`.
- **Exercises:** archive members `Problem Sheets/Exercise Sheet 1/exercise_sheet_1.pdf` through `Exercise Sheet 11/exercise_sheet_11.pdf` and their solution PDFs.
- **Code evidence:** Python files under `Problem Sheets/Exercise Sheet 1`, `2`, `4`, `5`, `7`, and `8`, together with the corresponding completed solution directories.
