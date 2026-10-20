# Infrastructure — Storage, Validation and Exploration

## Scope and status

This document describes the **operational plumbing** connecting the project's human-readable data files to lightweight consistency checks and browsing tools. It describes file discovery, paths, commands, outputs, and technical boundaries—not the conceptual meaning of Sources, TreeNodes, or Items. Those are specified in [`00_sources.md`](00_sources.md) and [`01_tree.md`](01_tree.md).

The project evolves by stage. **Tree plumbing is the immediate implementation target; Graph plumbing is future work.** Commands and output paths below are the proposed contract until the helper is implemented and tested. The data files, not generated HTML, remain authoritative.

## Repository layout

```text
career-profile/
  00_sources/
    inventory/sources.yaml          # registered production Sources
    raw/projects/                  # primary project materials
    raw/tum/                       # primary course materials
    aux/                           # auxiliary evidence, not a tree category
    source_profiles/               # earlier source inspections and analyses
  01_tree/
    example_tree/                  # isolated demonstration data
      projects/
        trees/*.yaml
        items/*.md
      tum/
        trees/*.yaml
        items/*.md
    projects/                      # production, created when needed
      trees/*.yaml
      items/*.md
    tum/                           # production, created when needed
      trees/*.yaml
      items/*.md
    index.html                     # proposed generated production viewer
  scripts/
    codex-helpers/
      tree.py                       # planned single-purpose helper
  docs/
    project_overview.md
    00_sources.md
    01_tree.md
    plumbing.md
    AGENTS.md
```

The directories and helper marked as planned are **not presumed to exist yet**. No empty production trees are required.

The physical branches `projects` and `tum` mirror the two principal source categories under `00_sources/raw/`. The auxiliary materials under `00_sources/aux/` support verification but do not automatically produce a tree branch. Production Source IDs come from the registry; demonstration Source IDs remain isolated and need not be registered.

## Input discovery and ownership

| Input | Used for | Ownership |
| --- | --- | --- |
| `00_sources/inventory/sources.yaml` | Resolving valid production Source IDs and original evidence locations | Sources stage |
| `00_sources/raw/` and linked original repositories | Primary evidence when *extracting* Items | Sources stage; read-only |
| `00_sources/source_profiles/` | Orientation, earlier analysis and cross-checking during extraction | Sources stage; not primary proof |
| `01_tree/{projects,tum}/trees/*.yaml` | Production structural hierarchy | Tree stage |
| `01_tree/{projects,tum}/items/*.md` | Production content and references | Tree stage |
| `01_tree/example_tree/{projects,tum}/{trees,items}/` | Demonstration and plumbing tests | Isolated fixtures |

The tree helper **does not extract content** from raw files or profiles. These materials guide a separate source-grounded extraction workflow.

Paths inside `sources.yaml` are resolved **relative to `00_sources/inventory/`**, not the process working directory. The helper locates its own project root relative to its script location, so the commands work when invoked outside the repository root.

## Tree plumbing: command interface (planned)

One script is sufficient for the initial tree stage:

```sh
python3 scripts/codex-helpers/tree.py validate
python3 scripts/codex-helpers/tree.py render
```

These commands operate on **production data by default**, excluding `example_tree/`. A clearly named example-mode flag (proposed `--examples`) runs against only the fixture subtree:

```sh
python3 scripts/codex-helpers/tree.py validate --examples
python3 scripts/codex-helpers/tree.py render --examples
```

The example-mode syntax is an implementation convention proposed here; it is not an existing command until built. The example viewer writes a separate file, proposed `01_tree/example_tree/index.html`, while production rendering writes `01_tree/index.html`. Generated viewers are disposable outputs and can be regenerated from authoritative YAML/Markdown.

### Validation responsibilities

Validation is structural, not a proof that a source was extracted completely or that a theorem is true. Its checks cover:

- Readable YAML and Markdown YAML frontmatter, with the agreed required fields.
- Unique TreeNode IDs within a Source, unique Item IDs across production data, and file-stem/Item-ID consistency.
- Registered production Source IDs, matching source tree and Item references, and matching `projects`/`tum` placement.
- TreeNode parent existence, same-Source ownership and acyclicity; `parent: null` is valid.
- Item parent existence, valid `type` vocabulary, substantive Markdown body and an identifiable provenance section.
- Clear diagnostics with file locations and nonzero exit status when invalid.

An empty production tree is valid during initial setup. Example validation is independent of the production registry and must not change or append to it.

### Rendering responsibilities

Rendering produces a **read-only, static HTML explorer**. Its navigation structure is synthetic above the Source level:

```text
▼ Career Profile
  ▼ Projects
    ▼ <project Source>
      ▼ <TreeNode>
        • <Item>
  ▼ TUM
    ▼ <course Source>
      ▼ <TreeNode>
        • <Item>
```

`Career Profile` is expanded by default. `Projects` and `TUM` are view categories, not persisted YAML nodes or extra Item fields.

The explorer provides:

- Collapsible Source/TreeNode navigation and selectable Items.
- A readable content panel with rendered Markdown and mathematical notation.
- Search over Item titles and display of Item `type`.
- Clear empty-state behavior when no production data exists.

Sibling presentation order is for navigation convenience and does not assert an original teaching sequence; there is **no `order` field**. Renderers must treat Markdown content as data, not executable HTML or JavaScript. Math/Markdown rendering may use small established libraries, with offline/CDN behavior stated in the implementation report. No editing UI, backend server or authentication is required.

## Example workflow

For a demonstration tree already present in `01_tree/example_tree/`:

```sh
python3 scripts/codex-helpers/tree.py validate --examples
python3 scripts/codex-helpers/tree.py render --examples
```

The resulting example explorer should show `Career Profile → TUM → Example Optimization Course → … → KKT` alongside the project implementation example. The example IDs are fictional; this is **a plumbing test, not verified personal experience or course extraction**.

For real extraction, the future tree writer creates a registered Source tree and referenced Item Markdown files in the matching production branch. Running `validate` checks their consistency; `render` rebuilds the explorer. Neither command edits extracted content.

## Graph plumbing (future)

`02_graph/` will have separate persistence, validation and exploration needs, **defined when the Graph stage is designed**. It may consume stable Item IDs and references from the production tree. Any future graph tooling should follow the same principles:

- Human-inspectable authoritative files and reproducible derived views.
- A distinct stage boundary: graph analysis does not silently rewrite source-grounded Items.
- Validation against existing Source/Item identities where relevant.
- Lightweight tooling justified by actual graph operations, not by a speculative framework.

This document **does not prescribe** the graph file format, commands, object schema or visualization technology. When those choices are made, they can be documented in a new *Graph plumbing* section here, while semantic objects and relations belong in `02_graph.md`.

## Non-goals and safety

Tree plumbing does not include archive extraction, PDF parsing, content segmentation, source-profile regeneration, Topic inference, Competency scoring, graph construction, semantic search, databases or a persistent web service. It must not modify original materials, existing profiles, inventory IDs or the agreed knowledge schemas.

## Implementation verification

A completed tree helper can be checked by validating and rendering isolated examples, testing broken parent/duplicate ID/invalid type/cycle cases, verifying production excludes fixtures, running commands from the repository root and another working directory, and running `git diff --check`. Report test outcomes and limitations rather than treating this planned description as evidence of a completed implementation.
