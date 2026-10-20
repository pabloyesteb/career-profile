# Source-specific knowledge tree

## Purpose and scope

The source-specific tree is a navigable, technically substantive decomposition of a registered **Source**. It retains the structure of the original material and the provenance of each extracted unit of knowledge or experience. The tree does not provide a cross-source semantic taxonomy: that belongs to the planned graph.

The conceptual meanings of **Source**, **TreeNode**, and **Item** are defined in [`knowledge_model.md`](knowledge_model.md). This document describes their tree-stage representation, extraction granularity, coverage, and presentation. The registry of Sources is [`00_sources/inventory/sources.yaml`](../../00_sources/inventory/sources.yaml) when these instructions are installed at `docs/instructions/` (the link assumes a repository checkout).

## Storage

```text
01_tree/
  trees/<source-id>.yaml
  items/<item-id>.md
```

The filename stem of each Item matches its globally unique `id`; the item ID convention may include its Source prefix (for example `ma3503-kkt`). One YAML tree exists per Source being processed. No empty tree files are required for other registered Sources.

A tree file contains the Source ID and its structural nodes:

```yaml
source: example-optimization
nodes:
  - id: example-optimality
    title: Optimality Conditions
    parent: null
  - id: example-constrained
    title: Constrained Optimization
    parent: example-optimality
```

`parent: null` marks a top-level node. All other node parents identify a TreeNode in the same Source. Node IDs are unique within the Source, and a node cannot be its own ancestor. The listing order of nodes is not a required semantic property, and no explicit numeric order field exists.

The tree YAML holds **structural nodes only**. Items refer to their primary TreeNode through their own frontmatter, avoiding redundant parent-to-items lists.

An Item is a Markdown file with YAML frontmatter:

```yaml
---
id: example-kkt
source: example-optimization
parent: example-constrained
title: Karush–Kuhn–Tucker Necessary Conditions
type: theorem
---
```

The five fields are required:

- `id`: stable, globally unique Item identifier, matching the Markdown filename stem.
- `source`: existing Source ID, matching the owning tree.
- `parent`: ID of exactly one TreeNode in that Source's tree.
- `title`: a descriptive, human-readable title.
- `type`: primary nature of the knowledge unit.

There is deliberately no `topic`, `order`, confidence score, career-relevance rating, or graph relationship field. Topics and cross-source relationships will be inferred and maintained by the graph stage; Items do not preempt that synthesis.

### Item types

The initial descriptive vocabulary is:

| `type` | Meaning |
| --- | --- |
| `concept` | Definition, construction, or conceptual foundation. |
| `theorem` | Mathematical statement, including significant lemmas or corollaries. |
| `method` | Analytical or technical methodology that is not necessarily a formal algorithm. |
| `algorithm` | Explicit computational or procedural method. |
| `implementation` | Substantive realized software or technical component. |
| `experiment` | Evaluation, study, test, or empirical investigation. |
| `result` | Substantive finding not better represented by another type. |

The type describes the **main contribution**, not every element included in the Item. A theorem Item may contain definitions and examples; an algorithm Item may contain a convergence theorem. Types do not force content fragmentation.

## Extraction coverage and granularity

A Source is covered by traversing its accessible substantive material from beginning to end. Small consecutive batches are operational checkpoints, not representative samples. Completing a sample batch does not make a Source complete.

A table of contents, syllabus, lecture sequence, chapter outline, or documentation structure provides the initial structural map. Consulting this map before extraction is compatible with linear processing. The detailed material is then processed in its actual intended order, rather than alphabetical ZIP-member order. Archives are inspected or unpacked into temporary working locations; originals and external repositories remain untouched.

The unit of extraction is the **smallest coherent, independently useful body of knowledge**, not a fixed page, slide, theorem, or paragraph. Granularity balances independent discoverability with technical self-sufficiency:

- A theorem, its assumptions, essential proof, interpretations, and routine corollaries usually form one Item.
- A major corollary with independent significance can form a separate Item.
- An algorithm generally includes its formulation, computational steps, theoretical behavior, and limitations.
- Definitions, lemmas, examples, and implementation details may support a broader Item unless their independent reuse warrants separation.
- Major algorithmic variants, substantive experiments, and distinct implementation contributions may justify separate Items.
- Administrative material, repetition, and transitions require examination but need not produce Items.

ECTS and source size may inform rough planning, but **no expected count is a quota or acceptance criterion**. Coverage is assessed against the original structure and accessible evidence, not against an arbitrary number of Items. Missing or unreadable material remains an explicit limitation rather than silently becoming a coverage claim.

### Content quality and provenance

The Markdown body is flexible rather than a rigid template. Depending on the unit, it includes precise statements, definitions, mathematical notation, assumptions, reasoning or proofs, algorithms, experimental setups, implementation choices, results, examples, and limitations.

Each extracted Item contains a **Provenance** or **Source references** section with references precise enough to relocate its evidence: source/archive member or repository path, document, section, page, slide, theorem, or revision when available. Source identity alone is not a sufficient reference. References are not invented. Academic exposure, source claims, implemented work, observed results, and personally attributable contributions remain distinct.

Duplicate knowledge within one Source is normally consolidated or cross-referenced; similar content from distinct Sources remains separately grounded. No item is discarded merely because it appears irrelevant to a particular career direction.

## Example: tree and Items

The included example uses **real and mathematically correct optimization concepts**, but its Source and hierarchy are **illustrative**. It is **not** a verified extraction of the user's MA3503 materials, and its provenance sections say so explicitly. These files belong outside production `01_tree/` and must not count as extracted Items.

```text
docs/instructions/examples/01_tree/
  trees/example-optimization.yaml
  items/example-kkt.md
  items/example-second-order.md
  items/example-newton.md
```

The hierarchy is:

```text
example-optimization
├── Mathematical Foundations
├── Optimality Conditions
│   ├── Unconstrained Optimization
│   │   └── Second-Order Sufficient Condition [theorem]
│   └── Constrained Optimization
│       └── KKT Necessary Conditions [theorem]
└── Numerical Methods
    └── Newton's Method [algorithm]
```

The three Markdown examples illustrate meaningful variation in unit size:

1. **KKT necessary conditions** combine a structured mathematical statement and its immediate interpretation.
2. **Second-order sufficiency** is a compact result with independent value, though in some actual sources it belongs with other optimality conditions.
3. **Newton's method** integrates derivation, procedural steps, local behavior, and limitations instead of splitting a single algorithm into fragments.

The example YAML and Markdown files are the canonical concrete examples accompanying this document; snippets here only illustrate their shape.

## Navigation and consistency

The on-disk structure remains the source of truth. An optional, read-only static HTML explorer can render the existing YAML hierarchy and Markdown Items, with title search, type labels, and mathematical notation. It is a derived view, not an editable database or a replacement storage format.

Consistency checks include valid YAML/frontmatter, unique IDs, registered Sources, correct Item-to-Source and Item-to-parent references, valid node ancestry without cycles, nonempty substantive bodies, and meaningful provenance sections. The validator can enforce the presence of references but cannot independently guarantee their factual correctness. Completion of a Source additionally requires a coverage review against its original material; structural validation alone does not establish exhaustive coverage.

No implicit chronology is claimed from alphabetical filenames or node listings. The absence of `order` is intentional. Where a batch ends, a precise continuation location is recorded in the batch report rather than stored as mandatory Item metadata.
