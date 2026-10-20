# Career Profile

A source-grounded knowledge resource for understanding academic and technical experience, preparing interviews and developing tailored professional applications.

## Redesign in progress

The planned architecture separates:

- A centralized **Source registry** and source-specific hierarchical trees.
- Relatively atomic **knowledge Items** extracted from those sources.
- A cross-source semantic graph of **Topics and Competencies**.
- A downstream **master professional profile** and application-specific outputs.

The detailed data model has not been finalized or implemented by this cleanup. See [AGENTS.md](AGENTS.md) for current working instructions.

## Existing reference material

- `00_sources/`: original documents and archives, treated as read-only.
- `01_inventory/`: existing source catalogs and historical processing records.
- `02_profiles/`: previously extracted academic and project knowledge, retained as reference—not as a template or classification for the new architecture.
- `scripts/`: retained source-inspection, processing and inventory utilities; check legacy paths and assumptions before reuse.
- `04_master_profile/` and `05_cv/`: preserved downstream directories.

[config/sources.yaml](config/sources.yaml) records existing local and external source locations. Relative paths are resolved against its directory. It remains unchanged and does not yet define the new Source registry.

The former extraction workflows have been retired. Preserve their knowledge and provenance without carrying their methodology into the redesign.
