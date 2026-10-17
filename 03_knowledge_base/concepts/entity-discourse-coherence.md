---
id: "entity-discourse-coherence"
title: "Entity identity, coreference and discourse structure"
domains:
  - "language-vision-cognition"
  - "machine-learning"
evidence_refs:
  - "in2361:entity-discourse"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "retrieval-grounded-dialogue"
  -
    type: "related_to"
    target: "semantic-knowledge-extraction"
---

# Entity identity, coreference and discourse structure

## Referring expressions and persistent entities

Mentions are text spans, not automatically distinct entities. Anaphora, cataphora, zero reference, givenness/definiteness and nonreferential expletives constrain interpretation. Pairwise classifiers plus transitive closure can propagate one erroneous link; mention-ranking models include a no-antecedent option, while entity-level models represent clusters more directly.

End-to-end span coreference uses contextual endpoints, attention-based soft heads and span width; mention/antecedent scores define antecedent probabilities. Marginalizing valid antecedents handles latent choices, and pruning controls candidate growth. B-cubed averages mention-level cluster precision/recall; it is not ordinary independent-label accuracy. Gender bias remains an evaluation concern.

TAGME links using mention/anchor priors and cross-entity coherence. ELQ jointly detects spans and scores entity candidates using contextual mention/title/text representations. RDF, SQL/SPARQL and semantic QA connect identification to structured knowledge access, not an implemented personal database.

## Coherence across sentences

RST builds elementary discourse units and nucleus/satellite trees; Penn Discourse Treebank explicit/implicit argument relations are complementary annotations, not identical tree structures. Neural EDU segmentation and shift–reduce discourse parsing use contextual encodings, pooled unit/subtree representations and action classification; nuclearity choices distinguish NN/NS/SN configurations.

Centering tracks backward-looking, forward-looking and preferred centers and ranks Continue, Retain, Smooth Shift and Rough Shift. Entity grids encode subject/object/other/absent roles over sentences and learn transition features. Self-supervised natural-versus-permuted discourse objectives model ordering plausibility, not a proof of truth.

Argument mining separates claims, premises and other text and finds support/attack relations. Persuasion and scientific-discourse examples connect linguistic structure with reasoning analysis without equating persuasive language with valid inference.

## Cross-domain retrieval value

[Retrieval/dialogue](retrieval-grounded-dialogue.md) needs referential state to understand successive queries; [logical extraction](semantic-knowledge-extraction.md) needs persistent identities to avoid contradictory duplicate facts. Cognitive [binding](cognitive-architectures-binding.md) poses a related representational question—what belongs together—but its neural hypotheses are not coreference algorithms.

[IN2361 entity-discourse evidence](../evidence/in2361.yaml) preserves theoretical and evaluation detail. There are no local software labs or achieved personal coreference/linking/discourse results. These methods remain retrievable as taught knowledge rather than being flattened into generic “NLP.”
