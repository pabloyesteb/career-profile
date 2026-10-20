# Knowledge model

## Responsibility

This document defines the agreed conceptual model. [Project overview](project_overview.md) describes purpose and stages; [working instructions](AGENTS.md) govern Codex behavior; [tree extraction](01_tree.md) specifies processing order, Item boundaries and bounded batches.

## Objects

| Object | Responsibility | Persistence |
|---|---|---|
| **Source** | Identify one conceptual academic, scientific or professional source and its primary materials. | Existing stable mapping key and record in `00_sources/inventory/sources.yaml`. Related documents and repositories may belong to the same Source. Archive members remain in `00_sources/inventory/archive_files.csv`. |
| **TreeNode** | Organize a structural subdivision of one Source, such as a chapter, lecture or project subsystem. It is not a semantic Topic. | Source-specific YAML under `01_tree/trees/`, recording the Source and nodes with `id`, `title`, `parent`; root nodes have `parent: null`. |
| **Item** | Explain a coherent, relatively atomic unit of knowledge or experience from one Source. | Markdown under `01_tree/items/`, with YAML frontmatter `id`, `source`, `parent`, `title`; substantive explanation and precise references in the body. |
| **Topic** | Synthesize technical meaning and relationships across Items, including shared principles and important distinctions. A collection or list alone is insufficient. | Human-readable graph content; exact persistence is deferred to the graph stage. |
| **Competency** | Describe a capability reasonably supported by Items, explaining its theoretical or practical basis and scope. | Human-readable graph content; exact persistence is deferred to the graph stage. No confidence scores or proficiency ratings. |
| **Graph** | Express cross-source semantic relationships among Topics and Competencies and their supporting Items. | Planned graph stage; no schema or implementation is introduced here. |

A Source's tree consists of its TreeNodes and Items; a separate Tree object or object subclass hierarchy is unnecessary. These conceptual responsibilities do not require a Python class for every object.

The tree persistence paths above are intended outputs. Their directories are created only when extraction is authorized; the current `01_tree/` is empty.

## Tree and graph

The tree preserves the source's organization, order and provenance. Each Item has one Source and exactly one primary parent TreeNode within that Source. Structural parentage is acyclic. Source-specific Items remain distinct even when their content overlaps with another Source.

The graph provides revisable semantic abstraction across Sources. Topics may overlap and need not form an exclusive taxonomy. Competencies require support from Items; they are not inferred solely from Topic titles. Semantic relationships can evolve without changing source-specific factual content. Keep authoritative relationships explicit and avoid competing copies.

The downstream master profile draws on this model. Professional emphasis remains the user's decision and does not redefine source-grounded content.

## Identity and references

Keep Source, TreeNode and Item identifiers stable when titles, locations or tree order change. Resolve references by ID rather than treating display titles as identities. Preserve existing Source IDs, boundaries, academic associations and recorded ambiguities.

Locations in `00_sources/inventory/sources.yaml` resolve relative to that registry's directory; external absolute paths and URLs retain their own meaning. Repository-local paths quoted in instructions or source profiles are relative to the career-profile repository root unless explicitly identified as paths inside a source archive or external repository. Markdown links resolve relative to the containing Markdown file.

Each Item cites the supporting material with the available section, page, slide, theorem, archive-member path, code path or repository revision. A directory path alone is insufficient for a specific technical assertion. State material gaps and source limitations instead of inventing locators or details.

The profiles in `00_sources/source_profiles/` are reference material. They can orient extraction but do not impose a taxonomy or replace original evidence when important details need checking. Do not present a profile-based statement as independently verified against the original source.

## Technical content and attribution

Preserve supported formulations, assumptions, proofs or proof ideas, algorithms, numerical and implementation details, experimental conditions and limitations. Items should be independently useful without reproducing entire source documents.

Distinguish theoretical knowledge, practical implementation, reported or observed results, collaborative work and personally attributable contributions. Academic exposure can support analytical capability without establishing personal software implementation. Supplementary material does not establish academic credit or completed assignments. Coauthorship does not identify every individual contribution.

Quantitative results retain their units, experimental setting and material qualifications. External published findings remain distinct from results of the user's implementation. Topics and Competencies explain supported interpretations without scores or a prescribed professional taxonomy.

## Minimal structural checks

Check parsing, unique IDs, resolvable Source and parent references, one primary parent per Item, same-Source placement, acyclic node ancestry and usable source locators. Human review checks technical substance, coherent Item boundaries and accurate attribution; structural validation cannot establish those qualities by itself.

Use inspectable Markdown and YAML and only the minimal Python needed for concrete loading or checking tasks. Graph persistence remains deferred. The first tree pilot can use the conventions already specified in [tree extraction](01_tree.md); it does not require graph implementation or new validation infrastructure.
