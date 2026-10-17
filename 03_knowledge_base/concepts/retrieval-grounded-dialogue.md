---
id: "retrieval-grounded-dialogue"
title: "Retrieval, grounded generation and dialogue-state interfaces"
domains:
  - "language-vision-cognition"
  - "machine-learning"
  - "scientific-software-data-engineering"
evidence_refs:
  - "in2361:retrieval-dialogue"
  - "additional-cognitive-systems:retrieval-workflow"
status: "reviewed"
---

# Retrieval, grounded generation and dialogue-state interfaces

## Retrieval stages and their objectives

Sparse lexical retrieval uses inverted indexes, TF–IDF/cosine or BM25 term-frequency saturation/document-length normalization. Dense bi-encoders embed query and document separately; cross-encoders rerank a pair jointly. ColBERT's token-level late interaction differs from a single independent-vector comparison.

Precision/recall, average precision/MAP and reciprocal rank assess ranking; answer exact matching/token F1 assess answers. Natural Questions, TyDi and multi-domain QA illustrate varying tasks/languages. A good ranking score does not establish factual answer correctness.

RAG conditions generation on selected passages. Query formulation, retrieval, multi-hop/context selection, reranking and generation can fail separately. Privacy/copyright and external-source access are design considerations, not a personally deployed retrieval service.

## Supplied pipeline versus requested functionality

Cognitive Systems supplies a concrete instructional workflow: overlap-chunk local Markdown, embed with multilingual MiniLM, retrieve up to 32 candidates, rerank with a QNLI ELECTRA cross-encoder and combine six passages in the generation prompt. It uses SentenceTransformers, LangChain splitting, Transformers/datasets, PyTorch and a hosted-model SDK.

The final example actually calls a hosted model. Requested conversational query rewriting, explicit citations and an open-model conversational implementation are absent; they must not be presented as completed features. Static notebook contents are not personal authorship or verified execution. [Cognitive Systems retrieval claim](../evidence/additional-cognitive-systems.yaml) retains these scope limits.

## Dialogue is more than retrieval plus a response

ELIZA pattern matching, retrieval-based responses and generative systems have distinct mechanisms. Turn taking, endpoint detection, speech acts, grounding, adjacency pairs, repair, initiative and implicature organize interaction.

Task-oriented dialogue represents frames/slots, recognizes intent/user acts, tracks dialogue state and selects system actions. Confidence-dependent confirmation/rejection addresses uncertain interpretation; an RL policy is introduced architecturally, not supplied as a trained user system. Content planning and linguistic realization are separate generation stages. ACUTE-Eval pairwise judgments, Wizard-of-Oz and iterative user-centered design assess interaction beyond token likelihood.

## Reusable connections

[Entity linking/discourse](entity-discourse-coherence.md) maintains referential context; [cognitive buffers](cognitive-architectures-binding.md) coordinate internal state. Neither is automatically a RAG conversation memory. Likewise corpus retrieval in this knowledge base is a future use of the documented theory, not a claim that this repository already implements a vector-search/RAG service.

[IN2361 retrieval-dialogue evidence](../evidence/in2361.yaml) supports theoretical comparison; [Cognitive Systems](../evidence/additional-cognitive-systems.yaml) supports the supplied pipeline. Distinct provenance is retained without repeating implementation caveats in every technical section.
