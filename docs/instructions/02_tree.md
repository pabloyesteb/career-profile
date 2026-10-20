# Source-specific knowledge tree

## Purpose

The tree is a faithful, navigable decomposition of each Source into relatively atomic, technically useful knowledge Items. It preserves **where knowledge comes from and how the source presents it**. It does not group knowledge across Sources by meaning; that is the later semantic graph's responsibility.

## Components

- **Source:** An existing conceptual source registered in `01_inventory/sources.yaml`. The registry identifies the source and its primary material locations; it is not a catalog of extracted concepts.
- **TreeNode:** A structural subdivision of one Source (for example, a chapter, lecture, section, project subsystem, or experiment group). Nodes organize content; they are not Topics and do not need independent conceptual summaries.
- **Item:** A self-contained unit of substantive knowledge or experience extracted from one Source. An Item has a stable ID, one Source, one primary TreeNode, a descriptive title, technical content, and precise source references.

A Source's tree consists of its TreeNodes and Items. A separate Tree object is unnecessary.

## Extraction procedure: follow the source

1. Identify the Source in `01_inventory/sources.yaml` and locate its original materials. Read relevant existing profiles only as orientation; original materials take precedence when details matter.
2. Establish the source's **actual reading or processing order** (e.g., syllabus and lecture sequence; thesis chapters; project documentation and code structure). Use `archive_files.csv` and `archive_matches.csv` when useful. Do not treat alphabetical ZIP-member order as the intended teaching order.
3. Unpack or inspect the next bounded portion of material into temporary working space, without changing the original archive or repository. Do not execute code found in source materials.
4. Follow the material **linearly**, creating structural nodes as its organization becomes clear. Do not build a speculative complete tree in advance.
5. Delimit the substantive content into Items. Decide which results deserve independent treatment and which details belong inside a larger Item. Preserve the order in which Items are encountered.
6. Write each Item with its own coherent explanation and references, validate its placement, and stop at the requested batch limit. Record the exact point at which the next batch should resume.

Do not skip ahead to select especially impressive or varied examples. Do not silently omit substantive material merely because it seems less relevant to a career application. Headings, administrative notices, repetitions and purely transitional text need not become Items.

## Deciding Item boundaries

An Item should express **one coherent, independently useful result, method, construction, argument, implementation, experiment, or tightly connected group of results**. It need not correspond to a single slide, paragraph, heading or theorem.

Prefer **one Item** when material is best understood together, for example:

- A theorem with its assumptions, proof sketch or proof, interpretation, and routine corollaries.
- An algorithm with its mathematical formulation, steps, convergence conditions and limitations.
- A method with the definitions and examples required to understand it.

Prefer **separate Items** when a component has substantial independent significance, for example:

- A corollary that is a major result in its own right, rather than a routine consequence.
- A distinct algorithm with its own assumptions or computational behavior.
- An implementation or experiment that makes a substantive contribution beyond illustrating a preceding concept.

Avoid both one-Item-per-slide fragmentation and broad Items that merely summarize an entire lecture. Definitions and supporting lemmas can remain within a larger Item unless their independent reuse justifies separation. When uncertain, favor conceptual coherence and explain the boundary decision briefly in the batch report rather than inventing metadata.

## Content and provenance

Write Items in English, using Markdown with YAML frontmatter. Preserve, where supported by the source:

- Precise definitions, notation, equations, assumptions, statements and conclusions.
- Proofs or essential proof ideas, algorithms and relevant computational details.
- Important examples, edge cases, limitations and distinctions.
- The difference between taught material, a source's claims, observed results, implemented work and personally attributable contributions.

An Item should stand on its own without reproducing entire source documents. Cite the exact supporting material as precisely as available: archive or repository path, document filename, section, page, slide, theorem number, code path or revision. Never invent page numbers or unsupported personal contributions. If source material is incomplete or ambiguous, state the limitation.

## Minimal persistence

Use the conventions authorized in `docs/knowledge_model.md` and the pilot implementation. The initial intended layout is:

```text
03_tree/
  trees/<source-id>.yaml
  items/<source-id>-<item-id>.md
```

A tree YAML file records its Source and structural nodes (`id`, `title`, `parent`; root nodes use `null`). An Item Markdown file uses YAML frontmatter with `id`, `source`, `parent`, `title`, followed by substantive content and source references. Each Item has exactly one primary parent node. Do not add Item types, semantic labels, confidence scores or graph links as mandatory fields.

Keep IDs stable once assigned. Do not duplicate the same knowledge merely because it is referenced again later in the source; extend or cross-reference the existing Item when appropriate, while retaining its primary location. Different Sources retain their own Items even when their content overlaps.

## Incremental batches and quality checks

Work in small, consecutive batches. The requested number of Items is a **stop condition**, not a reason to split or merge content artificially. If the batch limit falls inside a coherent unit, finish that unit and stop; do not force an unnatural boundary. If the accessible portion contains fewer substantive units, report that instead of inventing Items.

For each batch, check that IDs are unique, Source and parent references resolve, the hierarchy has no cycles, Items contain real technical content, and source references are usable. Report the Items created, material covered, decisions about boundaries, uncertainties, and a precise continuation point.

Do not create Topics, Competencies, graph relations, downstream profiles, or new extraction infrastructure unless separately requested.
