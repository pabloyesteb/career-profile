# Career Profile

A source-grounded knowledge resource for understanding academic and technical experience, preparing interviews and developing tailored professional applications.

## Current architecture

The project separates:

- A centralized **Source registry** and source-specific hierarchical trees.
- Relatively atomic **knowledge Items** extracted from those sources.
- A cross-source semantic graph of **Topics and Competencies**.
- A downstream **master professional profile** and application-specific outputs.

The current focus is a first five-Item pilot in `01_tree/`; graph construction and professional outputs are later stages. Read the [working instructions](docs/instructions/AGENTS.md), [project overview](docs/instructions/project_overview.md), [conceptual model](docs/instructions/knowledge_model.md) and [tree extraction guide](docs/instructions/01_tree.md).

## Existing reference material

- `00_sources/raw/`: original documents and archives, treated as read-only.
- `00_sources/inventory/`: `sources.yaml`, `courses.csv`, `archive_files.csv` and `archive_matches.csv`.
- `docs/legacy_inventory/`: historical processing reports and catalogs retained for reference.
- `00_sources/source_profiles/`: previously extracted academic and project knowledge, retained as reference—not as a template or classification for the new architecture.
- `01_tree/`: source-specific trees and Items, populated only during authorized extraction.
- `scripts/codex-helpers/`: source-inspection, processing and inventory utilities.
- `04_master_profile/` and `05_cv/`: planned downstream directories, absent from the current checkout.

[00_sources/inventory/sources.yaml](00_sources/inventory/sources.yaml) registers conceptual Sources with stable IDs, titles, broad types and primary locations. Related project documents and repositories share a Source; individual archive members are cataloged in [archive_files.csv](00_sources/inventory/archive_files.csv). Relative locations resolve against the registry directory.

The former extraction workflows have been retired. Preserve their knowledge and provenance without carrying their methodology into the redesign.
