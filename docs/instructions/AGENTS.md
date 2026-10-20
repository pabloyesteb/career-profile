# Career Profile — Project Instructions

## Purpose

Build a structured, technically detailed representation
of academic knowledge, research, and software experience.

The knowledge model should support technical exploration,
interview preparation, professional synthesis, and
tailored applications.

Professional positioning remains the user's decision.
Do not organize or filter the underlying knowledge
according to presumed career goals.

## Architecture

The project separates two complementary structures:

1. A source-specific hierarchical knowledge tree.
2. A cross-source semantic knowledge graph.

The tree preserves the organization and provenance
of knowledge extracted from individual sources.

The graph provides higher-level semantic abstractions
and relationships across sources.

The two structures serve different purposes and
must not be conflated.

The authoritative model specification is maintained
in `docs/knowledge_model.md`.

Its open design decisions must be resolved before
implementing the affected structures. A specification
or illustrative example is not authorization to create
model objects or infrastructure.

Follow that specification when creating or modifying
model objects. Do not introduce new object types,
required fields, or architectural conventions without
explicit authorization.

## Sources

`01_inventory/sources.yaml` is the centralized registry
of conceptual Sources. Stable mapping keys identify Sources;
records provide titles, broad types, primary material locations
and established academic associations. Resolve relative
locations against the registry directory. Individual archive
members belong in `01_inventory/archive_files.csv`.

Each Source identifies an academic, scientific,
or professional source and references its associated
materials, which may include documents, archives,
repositories, and external resources.

Original materials under `00_sources/` and external
repositories are read-only.

`01_inventory/` and `02_profiles/` contain reference
material produced during an earlier extraction phase.

Use these resources to accelerate knowledge extraction,
but do not treat their organization, classifications,
or conclusions as binding on the new model.

Historical inventory reports are retained under
`docs/legacy_inventory/`; their workflows and processing
statuses do not govern the new model. Project-specific
contribution records remain with the relevant project analysis.

## Knowledge tree

Build the knowledge tree source by source.

Each Source has a hierarchical structure composed
of structural nodes and knowledge Items.

Structural nodes organize content according to
the source's organization. They are not themselves
semantic knowledge abstractions.

An Item represents a relatively atomic,
self-contained unit of knowledge or experience.

Items may describe mathematical concepts,
theorems, algorithms, methods, implementations,
experiments, results, or other substantive content.

Do not impose an unnecessarily restrictive
classification of Item types.

Choose Item granularity according to conceptual
coherence and independent usefulness.

Avoid both excessive fragmentation and broad,
vague Items that combine unrelated content.

Preserve relevant mathematical assumptions,
technical details, limitations, and distinctions.

Items belong to their originating Source.
Do not merge source-specific Items merely because
they describe similar concepts.

Use stable identifiers and preserve source references.

## Semantic graph

Build the semantic graph from the extracted Items.

The graph contains Topics and Competencies.

### Topics

A Topic is a higher-level semantic abstraction.

It has its own title, description, and associated
knowledge Items.

A Topic must synthesize the meaning and relationships
of its associated Items, not merely list or group them.

Topics may overlap and may relate to other Topics,
including through broader/narrower relationships.

Do not force Topics into a single exclusive taxonomy.

### Competencies

A Competency describes a technical or professional
capability reasonably supported by the knowledge and experiences
represented in the Items.

Competencies are interpretive abstractions, not
mechanical aggregations of keywords or course titles.

Distinguish theoretical knowledge from practical
implementation and personal experience.

Do not attribute hands-on experience solely from
academic exposure.

Do not introduce numerical confidence scores,
proficiency ratings, or evidence-weighting systems.
Explain a capability's scope and limitations in words;
theoretical knowledge can support analytical capabilities
without implying hands-on implementation.

### Graph relationships

Relationships must be explicit, inspectable,
and consistent with the model specification.

Do not duplicate relationship definitions across
multiple files.

Semantic relationships may evolve without changing
the underlying source-specific Items.

Treat Topics and Competencies as revisable interpretations,
not definitive classifications of the user's identity.
Present consequential positioning choices to the user.

## Accuracy and provenance

Treat the supplied source material as generally
trustworthy, while preserving distinctions between
what was taught, what was implemented, what was
observed, and what was personally contributed.

Do not invent technical content, implementation
details, results, or personal contributions.

Maintain sufficient source references to locate
the supporting material.

Prefer precise technical descriptions over generic
summaries.

Do not create artificial certainty where source
material is ambiguous or incomplete.

Do not introduce confidence scoring or elaborate
evidence-assessment frameworks.

## Persistence and infrastructure

Use simple, human-readable files as the primary
persistent representation of knowledge.

Prefer Markdown and YAML where appropriate.

Use minimal Python infrastructure for loading,
validating, and navigating the model.

Python defines and checks structural rules.
It does not determine semantic meaning or
professional positioning.

Avoid databases, vector stores, RAG frameworks,
complex class hierarchies, and unnecessary
dependencies unless a demonstrated need arises.

All generated objects and relationships must remain
inspectable and editable without specialized software.

## Working practices

- Follow the current task's scope strictly.
- Do not initiate large-scale extraction without
  explicit authorization.
- Do not modify original source materials.
- Do not execute untrusted code from source archives
  or external repositories.
- Do not install dependencies without approval.
- Do not perform destructive operations without approval.
- Preserve unrelated work.
- Reuse existing reference material when useful,
  but verify important technical details against
  original sources when necessary.
- Process sources incrementally.
- Validate generated objects using the available
  model validators.
- Record unresolved ambiguities instead of guessing.
- Report files changed, validation results, and
  unresolved questions.

## Downstream synthesis

The master professional profile and tailored CVs
are downstream products.

They must be derived from the knowledge model,
not used to reshape its underlying factual content.

Do not generate downstream outputs unless requested.
