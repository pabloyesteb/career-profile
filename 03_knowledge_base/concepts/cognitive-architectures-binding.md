---
id: "cognitive-architectures-binding"
title: "Cognitive architectures, embodied paradigms and dynamic binding"
domains:
  - "language-vision-cognition"
  - "computational-neuroscience"
  - "dynamical-systems"
evidence_refs:
  - "additional-cognitive-systems:cognitive-architectures"
  - "additional-cognitive-systems:dynamic-binding"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "entity-discourse-coherence"
  -
    type: "related_to"
    target: "population-dynamics-neural-memory"
---

# Cognitive architectures, embodied paradigms and dynamic binding

## Explanatory levels and competing paradigms

Marr separates computational objective, representation/algorithm and physical implementation. The ultimate–proximate distinction separates evolutionary purpose from mechanism. Cognitive Systems contrasts cognitivist symbol/production-rule approaches, connectionist emergence, enactive embodied development, dynamical accounts and hybrids. Physical-symbol-system/heuristic-search statements are hypotheses, not mathematical theorems; Turing-test/Chinese-room arguments distinguish behavior from understanding.

A perception–cognition–action cycle includes anticipation, assimilation and adaptation, goal-directed autonomy, cooperation/communication and unexpected events. MYCIN/OPS5/XCON and early robots are historical explanations. Embodiment, environment and other agents constrain the modeled system; a large generic network is not automatically a complete cognitive architecture.

## ACT-R coordinates symbolic structure and subsymbolic dynamics

ACT-R combines declarative chunks/types/slots and production rules with activation and learned utility. Modules run in parallel but expose limited buffers; serial production selection coordinates them. Buffer queries/pattern matching, modification/clearing and module requests form a control interface. Counting and multiplication-chunk exercises illustrate it without a packaged standalone ACT-R program.

Retrieval combines recency/frequency base activation, spreading context, partial-match penalties and noise. The source gives
\[
B_i=\ln\left(\sum_jt_j^{-d}\right)+\beta_i.
\]
Here \(t_j\) are past-use elapsed times; the display supplies the represented recency/frequency structure, not a fully specified runtime retrieval model. Procedural utility updates
\[
U_i\leftarrow U_i+\alpha(R_i-U_i).
\]
Production compilation combines compatible sequential rules under buffer constraints. Its scalar reward-like update is not proof that ACT-R is implemented as tabular Q-learning.

## Binding through dynamic structure

The guest neural-code account addresses superposition/binding ambiguity by structured nets. Cooperative alternate pathways versus competitive converging pathways motivate self-organization. Häussler retinotopic-map dynamics balance growth/cooperation with row/column competition/normalization; no missing full equation or convergence proof is reconstructed.

Dynamic projections/shifter circuits, neural fields versus topological mappings, net-fragment composition and dynamic-link recognition offer another representation strategy. Schema–instance matching preserves element types/relations (“homeomorphy” in the slides), not a formal topology theorem. Consciousness/global-integration proposals remain theoretical hypotheses.

CNN feature binding/capsules and EM routing are related architectural examples, not demonstrated equivalence to biological dynamic links. [Entity/discourse inference](entity-discourse-coherence.md) also needs identity and binding at a different level; [population attractors](population-dynamics-neural-memory.md) model persistent neural representations, not symbolic buffers.

[Cognitive Systems architecture/binding claims](../evidence/additional-cognitive-systems.yaml) retain the distinction between covered theory, supplied examples and personal implementation. These concepts complement existing adaptation/RL pages rather than inventing a cognitive-software project.
