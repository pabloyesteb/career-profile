---
id: geometric-sampling-motion-planning
title: Configuration-space planning, roadmaps and sampling-based initialization
domains: [robotics-planning-geometry, optimization]
evidence_refs: ["in2138:planning-syllabus", "cit413042:rrt-initialization", "tum-mobile-robotics:planning-learning"]
status: reviewed
relations:
  - {type: related_to, target: heuristic-adversarial-search}
  - {type: related_to, target: optimal-control-transcription}
  - {type: related_to, target: signed-distance-neural-fields}
---

# Configuration-space planning, roadmaps and sampling-based initialization

## Geometry, information and planning strategy

Configuration spaces turn robot geometry into point-based planning in a representation of admissible configurations. IN2138's official syllabus distinguishes online Bug/wavefront approaches, complete-map visibility/Voronoi roadmaps, trapezoidal/Boustrophedon decomposition, and heuristic potential fields with partial maps. It also names multi-query/single-query PRM, obstacle-based PRM and RRT. Expansiveness/connectivity analysis informs roadmap node counts/parameters and connectivity improvements.

This source establishes a structured method map, not exact complexity, probabilistic-completeness or convergence theorems. Its edition is Summer Semester 2024; identical delivery across terms is not assumed. Videos/homework references are not analyzed submissions or personal implementations. No PRM/RRT equations are reconstructed from this thin source; the more detailed RRT account below comes separately from Case Studies.

## RRT as an initializer, not the complete optimizer

The Case Studies implementation builds a geometric tree by sampling workspace or goal, finding the nearest existing node, steering a bounded step, testing the connecting segment for collision, and storing parent links on accepted nodes. Goal proximity or an iteration cap ends growth. Bounds, goal bias, step length and obstacle margin are configurable. Following parents reconstructs a path, then shortcutting removes unnecessary waypoints after collision checks.

SciPy `CubicSpline` smooths/resamples XY. The function name `_bspline_curve` does not make this a B-spline algorithm. Although the report describes tangent/velocity/acceleration lifting, the checked initializer supplies XY only, zero-fills other states and does not initialize controls. A geometric warm start therefore need not satisfy the discrete dynamics. Post-spline collision freedom is not comprehensively rechecked; the rectangle-inflation calculation also has an upstream geometry limitation.

The refined path is obtained by a separate constrained NLP. A reported improvement from RRT initialization does not make basic RRT itself an optimal planner, nor certify every smoothed segment. RRT-Connect, RRT*, Informed RRT*, A*/Dijkstra and learned initialization are named alternatives/background, not all implemented benchmark variants.

## Relationship to control and uncertainty

Mobile Robotics supplies a distinct supplementary map of obstacle inflation, grid/roadmap search, exploration and Dijkstra/A*/RRT/RRT*/informed RRT*. Its named rewiring/collision details are not fully reconstructed. [Heuristic/game search](heuristic-adversarial-search.md) separately provides DFS/BFS/UCS/A* frontier and utility reasoning from accredited Deep RL. This adds algorithmic distinctions without assigning unimplemented variants to the Case Studies repository or promoting supplementary exercises to personal work.

Geometric feasibility, dynamic feasibility and task completion are different levels. The thesis starts with inherited offline scenario plans and studies online progress/recovery; it does not personally implement the Case Studies tree inside its MPC. A recovery spiral is a reference-search heuristic, not an RRT. IN2138's filtering/SLAM topic provides uncertainty context without establishing either project's use of a probabilistic mapping pipeline.

Evidence: [IN2138](../evidence/in2138.yaml), configuration/geometric/sampling syllabus sections; [Case Studies](../evidence/cit413042.yaml), initialization sections in both profiles. Team implementation is distinguished from individually attributed SIREN/Hausdorff work. See [trajectory transcription](optimal-control-transcription.md) for the subsequent dynamical optimization.
