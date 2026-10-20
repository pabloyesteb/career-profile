# Career Profile — Codex Working Instructions

## Documentation map

The authoritative project documentation lives in `docs/`. Each file has a distinct responsibility:

| File | Responsibility |
| --- | --- |
| [`project_overview.md`](project_overview.md) | Goals, stage boundaries, repository layout and current scope |
| [`00_sources.md`](00_sources.md) | Source registry, original evidence, inventories, source profiles and path conventions |
| [`01_tree.md`](01_tree.md) | TreeNode and Item definitions, schemas, granularity, coverage and worked examples |
| [`plumbing.md`](plumbing.md) | File discovery, validation, rendering, commands, fixtures and future Graph plumbing |
| `AGENTS.md` (this file) | Working behavior, authorization, evidence standards and reporting |
| `legacy_inventory/` (when present) | Historical reports, not current specifications |

Read the project overview and the documents relevant to the task before making changes. Tree infrastructure work uses `01_tree.md` and `plumbing.md`; source extraction uses `00_sources.md` and `01_tree.md`. Future stages receive separate documentation when designed.

This file governs **how to work**, not the data schemas or command interface. Do not duplicate stage or infrastructure specifications here.

**Discovery:** `docs/AGENTS.md` is not a root-level `AGENTS.md`. An agent started at the repository root may not automatically load it. Until a root-level entry point exists, prompts should explicitly direct the agent to read `docs/AGENTS.md`.

## Scope and change control

- Respect the explicit task boundary; do not extend extraction or introduce a graph stage without authorization.
- Reuse established file formats and fields; do not introduce new object types, mandatory metadata, infrastructure or dependencies merely for convenience.
- Do not make destructive changes or commits unless requested.
- Preserve existing identifiers and unrelated content. Resolve unspecified design choices before implementing changes that depend on them.

## Evidence and accuracy

- Treat original source files and external repositories as read-only; do not execute untrusted source code.
- Use `00_sources/inventory/` to locate registered Sources and `00_sources/source_profiles/` to benefit from previous per-source analysis. Profiles are secondary aids, not substitutes for original evidence.
- Ground important technical claims and personal contributions in identifiable originals, archive members, source files or repository revisions.
- Distinguish academic coverage from implemented work and source claims from personally attributable contributions.
- Do not invent technical results, provenance, unsupported details or presumed career priorities.

## Implementation style

- Prefer small, transparent, auditable Markdown/YAML data structures and minimal focused Python helpers.
- Avoid databases, RAG systems, vector stores, generalized pipelines and unnecessary libraries.
- Do not introduce multiple competing representations of the same relationships.
- Validate changed data and paths with the relevant existing checks, and report limits of what those checks establish.

## Incremental extraction

- Work Source by Source, in the original material's natural order, with bounded consecutive batches.
- Delimit Items by independent technical significance and conceptual coherence, not arbitrary page or file boundaries.
- Maintain exhaustive coverage over the full Source, while keeping administrative or repeated content out of unnecessary standalone Items.
- Record a precise continuation point whenever an extraction batch stops.

## Reporting

Summarize changed files, completed work, checks actually run, and unresolved ambiguities. Do not describe planned infrastructure as implemented or unverified evidence as confirmed.
