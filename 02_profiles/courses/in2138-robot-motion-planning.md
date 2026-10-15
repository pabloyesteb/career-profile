# Robot Motion Planning (IN2138)

## Module metadata

| Field | Value |
|---|---|
| Official title | Robot Motion Planning / Bewegungsplanung in der Robotik |
| Module code | IN2138 |
| Stable identifier | in2138 |
| ECTS | 5 |
| Grade | 3.0 |
| Record section | Degree |
| Profile status | complete_validated |
| Evidence qualification | Complete for the available official syllabus; limited sources |

Academic metadata is from `01_inventory/courses.csv` and the transcript, p. 3. The user identifies the official webpage as the IN2138 source; the webpage title agrees. Its edition is **Summer Semester 2024**, not an independently established attendance term. Identical delivery across editions is not assumed. The archive-match field remains `missing`: a web source does not create a matching ZIP.

## Technical content

### Configuration-space representation

Configuration spaces reduce robot geometry to point-based planning. [S1, Representation.]

### Geometric planning and map assumptions

Bug and wavefront methods address online paths. Complete-map strategies include visibility and Voronoi roadmaps, trapezoidal decomposition and Boustrophedon; partial-map planning uses heuristic potential fields. [S1, Direct Planning Methods; Planning Strategies.]

### Sampling-based planning and connectivity

The outline names multi-query and single-query probabilistic roadmaps, obstacle-based PRM and RRT. Expansiveness/connectivity analysis guides roadmap parameters, including node counts, and connectivity improvements. [S1, Planning Strategies; Expansiveness of the Space.]

### Uncertainty, filtering and mapping

Mapping combines uncertain information through Kalman filtering for linear Gaussian models, extended Kalman filtering for nonlinear models, unscented Kalman filtering for strongly nonlinear models, and Bayesian/particle filtering for arbitrary uncertainties. SLAM couples localization and mapping. [S1, Fusion of Uncertain Data for Mapping.]

## Computational and assessment evidence

The syllabus associates videos 1–7 and homework sets 1–3 with planning topics; recordings originate in earlier years. [S1, Syllabus; recording/homework guidance.]

No submitted assignments, personally implemented algorithms, executable examples, programming languages, libraries or measured results are independently documented for this module. Course-covered knowledge is recorded as such, not as project implementation experience. The separate Case Studies project and IN2404 archive do not substitute for IN2138 evidence.

## Thematic categories

Robotics; geometric and sampling-based planning; graph algorithms; probabilistic estimation and sensor fusion.

## Coverage validation and source limits

Reviewed the complete official outline on 2026-10-15. All five source blocks are represented above. No theorem statements, equations, algorithm variants beyond the named methods, convergence bounds or solver details are supplied by this evidence, so none is reconstructed from general knowledge. Lecture recordings and homework contents were not recovered or analyzed. Additional lecture material could deepen this syllabus-level profile but is not required for its qualified completion.

## Sources

- **S1:** [TUM Machine Vision and Perception — Robot Motion Planning syllabus](https://mvp.in.tum.de/courses/motion/syllabus.html#syllabus), Summer Semester 2024; accessed 2026-10-15; inventory ID `in2138_official_syllabus`. References use the webpage's section names rather than invented page numbers.
- **Academic record:** `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 3; `01_inventory/courses.csv`, row `in2138`.
