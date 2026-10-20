# Career Profile — Codex Working Instructions

## Instruction hierarchy

Read [project_overview.md](project_overview.md) to understand the project's purpose, directories, and stages.

Follow [knowledge_model.md](knowledge_model.md) for authorized conceptual definitions and persistence decisions. Open design decisions are not permission to invent conventions.

For tree extraction, also read [01_tree.md](01_tree.md). Follow other stage-specific instructions when those stages are authorized.

This file defines **how to work**, not the project's domain architecture. Do not duplicate stage specifications here.

## Scope and authorization

- Follow the current task's scope strictly.
- Do not start large-scale extraction, graph construction, or downstream synthesis without explicit authorization.
- Do not introduce new object types, required metadata, directories, dependencies, or infrastructure just because they seem useful.
- Resolve open design decisions with the user before implementing affected structures.
- Preserve unrelated work and existing identifiers unless changes are explicitly required.
- Do not commit changes unless requested.

## Evidence and accuracy

- Treat original source materials and external repositories as read-only.
- Never execute untrusted code from archives or external repositories.
- Use inventories and prior profiles to orient work, but verify important technical details against original evidence where necessary.
- Do not invent technical facts, results, implementation details, or personal contributions.
- Distinguish what was taught, implemented, observed, and personally contributed.
- Preserve meaningful mathematical assumptions, technical limitations, and precise source references.
- State unresolved ambiguities rather than guessing.
- Do not infer career priorities or make consequential professional positioning decisions for the user.

## Implementation discipline

- Prefer simple, inspectable Markdown and YAML for knowledge content.
- Use minimal Python only when it solves a concrete loading, validation, or navigation need.
- Do not introduce databases, vector stores, RAG systems, generic frameworks, or unnecessary dependencies.
- Avoid duplicate representations of the same relationship.
- Do not install dependencies without approval.
- Do not perform destructive operations without approval.

## Incremental workflow

- Work source by source and in bounded, reviewable batches.
- Respect the source's natural organization and reading order during tree extraction.
- Choose Item boundaries by conceptual coherence and significance; do not mechanically split every slide, theorem, or paragraph.
- Stop at the requested boundary and record a precise continuation point.
- Validate changed data and references with available checks; do not create elaborate validators for one-off tasks.

## Reporting

At the end of a task, report concisely:

1. Files created, changed, or removed.
2. Work completed and checks run.
3. Remaining ambiguities, broken references, or decisions requiring approval.

Never report validation as successful unless it was actually run.
