# Career Profile --- Project Overview

## Purpose

This project builds a source-grounded representation of academic
knowledge, research, software work, and technical experience to support
professional profiling.

Its long-term outputs include a comprehensive professional profile,
technical interview preparation, exploration of expertise, and tailored
job applications. The underlying knowledge representation must remain
faithful to the sources and must not be organized around an assumed
career direction. Professional positioning is decided by the user.

## Architecture

The workflow separates source evidence, source-specific knowledge
extraction, and cross-source semantic synthesis:

**Sources → Tree → Graph → Professional outputs**

Each stage has a distinct responsibility. Later stages build on earlier
ones without rewriting their factual content to fit a professional
narrative.

### 00 --- Sources (`00_sources/`)

Contains the material from which knowledge is extracted:

-   `raw/`: original documents, course archives, and other source
    materials; treat as read-only.
-   `inventory/`: source registry and academic/archive catalogs,
    including `sources.yaml`, `courses.csv`, `archive_files.csv`, and
    `archive_matches.csv`.
-   `source_profiles/`: previously processed individual course, project,
    and supplementary profiles, plus relevant project analyses and
    contribution evidence.

The central registry is `00_sources/inventory/sources.yaml`. Its entries
identify conceptual Sources and point to their material locations.
Previously generated profiles help orient extraction, but do not
override original evidence or dictate the new knowledge structure.

### 01 --- Tree (`01_tree/`)

Contains source-specific hierarchical knowledge trees and their Items.

Each Source is processed incrementally, generally following the natural
order of its material. Structural nodes reflect the source's
organization; Items capture coherent, sufficiently substantial units of
knowledge or experience. Item boundaries are chosen by conceptual
coherence, not mechanically by page, slide, heading, theorem, or
paragraph.

Every Item retains its Source identity, one primary location in that
Source's tree, substantive technical content, and precise references.
Similar Items from different Sources remain distinct.

The tree preserves **what the source contains and where that knowledge
comes from**. It is not a semantic topic taxonomy.

Detailed instructions: `docs/instructions/01_tree.md`.

### 02 --- Graph (`02_graph/`, planned)

Will connect and synthesize Items across Sources through semantic
Topics, Competencies, and explicit relationships.

Topics must provide meaningful synthesis rather than simple grouping.
Competencies must be supported by evidence and distinguish theoretical
exposure from personal implementation or experience. Semantic
interpretations remain revisable and do not alter source-specific Items.

Graph persistence and extraction procedures will be defined when this
stage begins.

## Later outputs

-   `04_master_profile/` (planned; absent from the current checkout): downstream professional synthesis based on the
    knowledge model.
-   `05_cv/` (planned; absent from the current checkout): application-specific CVs and related outputs derived from
    that synthesis.

These stages are not the current implementation focus.

## Instructions and supporting material

-   `docs/instructions/AGENTS.md`: project-wide working rules.
-   `docs/instructions/knowledge_model.md`: conceptual model and
    authorized design decisions.
-   `docs/instructions/01_tree.md`: tree-specific extraction
    instructions.
-   `docs/legacy_inventory/`: historical processing reports retained as
    reference, not as governing methodology.
-   `scripts/codex-helpers/`: supporting utilities; verify their paths
    and assumptions before use.

Each stage should have its own focused instructions. Do not introduce
additional stages, schemas, or infrastructure merely to anticipate
future needs.

## Current focus

Begin with a small, reviewable pilot in `01_tree/`, extracting
consecutive Items from one Source. Validate Item boundaries, technical
depth, source references, and structural placement before scaling
extraction. Do not generate graph objects or professional outputs as
part of tree extraction.
