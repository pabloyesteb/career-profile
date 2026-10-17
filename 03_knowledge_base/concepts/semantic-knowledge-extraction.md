---
id: "semantic-knowledge-extraction"
title: "Logical semantics, relation extraction and temporal knowledge"
domains:
  - "language-vision-cognition"
  - "probability-statistics-uq"
evidence_refs:
  - "in2361:semantic-extraction"
status: "reviewed"
---

# Logical semantics, relation extraction and temporal knowledge

## Logical truth and structured meanings

Model-theoretic semantics interprets expressions over domains/denotations; verifiability, expressiveness, ambiguity and vagueness are different representation criteria. First-order predicates, variables, quantifiers and relations support entailment, while proof procedures use modus ponens, forward/backward chaining and resolution. Soundness, completeness and undecidability delimit what such procedures establish; a general satisfiability decision is not a universally terminating complete prover.

Neo-Davidsonian semantics introduces an event variable with participants/roles and modifiers rather than a fixed-arity predicate for every combination. Higher-order/modal approaches are introduced, not fully developed. Description logics separate TBox concept/role axioms from ABox individual assertions; subsumption, disjointness, coverage and instance checking support OWL/RDF knowledge representations.

## Learning facts from text

Entity/relation/event templates turn language into structured candidates. Hearst patterns offer high-precision but limited-recall relation rules. Supervised extraction uses lexical, dependency and contextual features. Seed bootstrapping alternates tuples and patterns under confidence thresholds; error propagation and semantic drift are material. Distant supervision uses knowledge-base alignment to create noisy labels, not verified relation truth.

ReVerb/open IE uses POS/phrase patterns, nearby noun phrases and a confidence classifier without a fixed relation inventory. Correct-extraction criteria determine precision/recall. A plausible output triple is not automatically an entailed or temporally valid fact.

## Events, time and participant roles

Allen's interval algebra expresses relative temporal relations. Reichenbach separates speech, event and reference times for tense/aspect. TimeML/TimeBank EVENT/TIME annotations and TLINK/ALINK/SLINK links support temporal-expression recognition and normalization using rules/sequence models, reference dates and temporal arithmetic. Extracted temporal relations can define a partial ordering rather than a single exact timeline.

Semantic roles differ from surface subject/object. Diathesis and proto-agent/proto-patient properties motivate PropBank's predicate-specific numbered roles versus FrameNet's frame inventories. Semantic-role labeling prunes candidates, identifies arguments, classifies roles and applies global constraints, or uses neural sequence labeling.

WordNet synsets supply semantic classes/selectional restrictions. Resnik's selectional preference compares verb-conditioned class probabilities with a background distribution through KL divergence; class contributions measure association. Pseudoword discrimination/human plausibility evaluate a linguistic preference, not causal influence.

## Relationships and boundaries

[Structured parsing](structured-sequence-parsing.md) supplies syntactic constraints; [distributional vectors](distributional-lexical-representations.md) supply corpus associations; [entity/discourse inference](entity-discourse-coherence.md) establishes candidate referents. These support semantic interpretation but are not equivalent to logical truth. This distinction also complements [causal models](causal-graphical-models.md): observational association, linguistic entailment and intervention are different questions.

[IN2361 semantic-extraction evidence](../evidence/in2361.yaml) covers logic, relations/events/time and roles. RDF/OWL/SPARQL are represented knowledge-access technologies, not personally implemented databases or extracted industrial ontologies.
