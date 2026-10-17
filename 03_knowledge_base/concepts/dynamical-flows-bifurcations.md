---
id: dynamical-flows-bifurcations
title: Flows, invariant manifolds and bifurcation structure
domains: [dynamical-systems, mathematical-analysis, control-estimation]
evidence_refs: ["tum-dynamical-systems:local-reduction"]
status: reviewed
relations:
  - {type: related_to, target: invariant-measures-chaos}
  - {type: related_to, target: state-feedback-observers}
---

# Flows, invariant manifolds and bifurcation structure

## Evolution and qualitative structure

An evolution family satisfies \(\phi^0=Id\) and \(\phi^{t+s}=\phi^t\circ\phi^s\). Flows/semiflows and iterated maps provide different time structures; orbits, invariant sets, equilibria, periodic orbits and nullclines define their qualitative objects. The supplementary profile recalls ODE existence/uniqueness, smooth dependence and Banach fixed points, with matrix-exponential flows and logistic maps as examples.

Local analysis covers stability, stable/unstable manifolds, dynamical equivalence, Hartman–Grobman local conjugacy and Poincaré return maps. Structural stability and hyperbolic sets ask about persistence of orbit structure rather than just one eigenvalue calculation. Named manifold results apply to flows/maps; exact hyperbolicity and smoothness hypotheses are not stated at this profile's selective depth. No new theorem statement is inferred solely from its name.

## Nonhyperbolic dynamics and parameter changes

Fold/Hopf flow bifurcations, map flips and exercise-supported transcritical stability exchange introduce qualitatively different transitions. Coordinate changes, resonances and Poincaré normal forms simplify local dynamics; center manifolds provide reduction/approximation before higher-codimension phenomena. Parameterized polynomial/map examples and Sheet 7 normal-form exercises establish more than an abstract topic label.

The source does not give exact reduced equations, nondegeneracy conditions or center-manifold approximation formulas. These are unavailable detail, not license to invent standard textbook derivations. The map still identifies a substantive reasoning toolkit: phase planes, invariant structures, coordinate simplification and parameter-dependent changes of behavior.

## Connections and boundaries

Linearized feedback stability and nonlinear internal dynamics are related questions, not equivalent guarantees. The thesis's compliant/recovery behavior is not a demonstrated application of Hopf or center-manifold analysis. Locomotor CPG examples motivate a periodic-behavior connection without establishing that the user constructed/analyzed those dynamics. See [global/statistical dynamics](invariant-measures-chaos.md) for a different long-run viewpoint.

Evidence: `tum-dynamical-systems:local-reduction` in [supplementary dynamics](../evidence/tum-dynamical-systems.yaml), flows/local behavior and bifurcation sections. Credit is not established and the learning relationship is unspecified; no personal numerical experiment is inferred.
