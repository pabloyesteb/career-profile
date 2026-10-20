# 00 — Sources

## Role

`00_sources/` contains the primary evidence, a registry of conceptual Sources, supporting inventories, and prior source-by-source inspection. It supplies the material and identity against which Tree Items are grounded; it does not itself store the new extracted knowledge tree.

## Directory layout

```text
00_sources/
  inventory/
    sources.yaml
    courses.csv
    archive_files.csv
    archive_matches.csv
  raw/
    projects/
      article/
      case_studies/
      master_thesis/
      pyloworder/
    tum/
      archives/
      extracted/
  aux/
    old_cv/
    transcripts/
  source_profiles/
    courses/
    projects/
      _analysis/
    supplementary/
```

- **`raw/projects/`** holds original local evidence for research, theses, software and other project Sources; external repositories can also be original evidence when registered or explicitly associated.
- **`raw/tum/`** holds course archives and material extracted from them. Archived originals remain unchanged; an extracted copy is not a different conceptual Source merely because it lives in another directory.
- **`aux/`** holds corroborating or administrative material, such as transcripts and previous CVs. Auxiliary evidence does not automatically become a tree Source.
- **`inventory/`** identifies Sources and indexes existing course/archive files. Its four-file structure is retained rather than duplicated with new manifests.
- **`source_profiles/`** contains earlier per-source technical profiles and analyses. They are useful research aids, not replacements for originals.

## Source identity and registry

A **Source** is a coherent body of original material that is processed as a unit: a course, thesis, software project, research project, or similar work. Source boundaries and stable IDs are defined by `00_sources/inventory/sources.yaml`. A Source can refer to multiple documents, archive members, or repositories. A Source is **not** the same as an individual file, nor does every directory imply a Source.

Registry paths are interpreted **relative to the directory containing the registry** (`00_sources/inventory/`), not relative to the repository root or the current shell directory. The registry's *actual YAML structure* determines where Source IDs and locations are read; code should not assume it is a list if it is actually a mapping.

For example, a registry location of `../raw/tum/archives/NLOA (W24_25)_20261012_1553.zip` resolves to an archive under `00_sources/raw/tum/archives/`. This is an illustration of path resolution, not a new prescribed registry schema.

The registry is the authority on **which conceptual Source exists and where its materials are**, while the original documents, archives and repositories are the primary authority on technical claims.

## Supporting inventories

| File | Role |
| --- | --- |
| `inventory/sources.yaml` | Conceptual Source IDs, associations and material locations |
| `inventory/courses.csv` | Academic/course catalog information |
| `inventory/archive_files.csv` | Inventory of archive members |
| `inventory/archive_matches.csv` | Associations between archives and course Sources |

Archive-member listing order is not necessarily lecture order. A syllabus, table of contents, lecture numbering, or another original organizational cue is more reliable for sequential extraction.

## Previously processed source profiles

`source_profiles/courses/`, `source_profiles/projects/`, and `source_profiles/supplementary/` preserve earlier inspections, technical summaries and selected project analyses. For example, `source_profiles/courses/ma3503-nonlinear-optimization.md` may help locate covered topics and relevant documents; `source_profiles/projects/_analysis/` may contain more detailed project or contribution evidence.

These profiles can speed up orientation, identify already examined material, and flag uncertain details. They are **secondary aids**. A claim included in a Tree Item should be grounded in an identifiable original document or repository revision whenever possible. Summaries must not be treated as proof of personally implemented work without supporting evidence. An outdated or conflicting profile is a reason to inspect the original, not to silently copy the profile.

## Relationship to later stages

`01_tree/projects/` and `01_tree/tum/` mirror the two primary extractable branches under `00_sources/raw/` for navigation and storage. They **do not mirror every raw file as a TreeNode**: each registered Source receives its own content-based hierarchy. The auxiliary evidence directory has no default tree branch.

The source stage remains independently useful as an auditable evidence collection; the tree adds content decomposition, while the future graph adds cross-source semantic interpretations. The detailed TreeNode and Item formats are documented in [`01_tree.md`](01_tree.md).

## Integrity and maintenance

Original materials and external repositories are read-only. Moves and renames can invalidate registry locations, profile references and helper scripts. The existing validator is `scripts/codex-helpers/validate_inventory.py`; its passing result checks repository consistency, not the factual correctness of every source summary. Historical reports under `docs/legacy_inventory/` are retained as historical records rather than rewritten to match every new directory layout.
