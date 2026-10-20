# Career Profile — Project Instructions

## Purpose

Build a trustworthy, technically rich representation of academic knowledge, research and software experience for professional exploration, interviews and tailored applications. Professional positioning remains the user's decision.

## Planned architecture

The project is being redesigned around:

1. A centralized registry of Source objects identifying source material and its provenance.
2. Source-specific hierarchical trees preserving each source's organization.
3. Relatively atomic knowledge Items extracted from sources.
4. A cross-source semantic graph of Topics and Competencies.
5. A downstream master professional profile and application-specific outputs.

The detailed data model is not finalized. Do not invent schemas, prescribe a professional taxonomy or implement infrastructure without a scoped request. Keep source-specific extraction distinct from cross-source semantic abstraction; neither source organization nor professional emphasis should dictate the other.

## Sources and legacy material

Consult `config/sources.yaml` for existing source locations, resolving relative paths against the configuration directory. It is a source-location configuration, not the finalized Source registry.

Treat original material in `00_sources/` and external repositories as read-only. Preserve `01_inventory/` and `02_profiles/` as reference material: their extracted knowledge and evidence remain useful, but their workflows, formats and classifications do not govern the new model. Do not restart the former profile-extraction process by default.

Preserve stable identifiers and traceable source provenance when reusing knowledge. Keep source locators and relevant repository revisions available; do not silently replace identifiers or imply unsupported equivalence between sources.

## Accuracy and interpretation

Preserve mathematical assumptions, algorithmic distinctions, implementation details and material limitations. Distinguish source-supported knowledge from revisable technical or professional interpretation. Record gaps rather than inventing content.

Represent personal contributions accurately: distinguish taught or supplementary material, personal implementation, collaborative work and externally reported results. Coauthorship or possession of material does not establish individual implementation. Do not change factual knowledge to fit a job posting.

## Working boundaries

- Follow the current task's scope strictly; do not initiate extraction, model construction or downstream profile/CV work without a request.
- Use minimal, inspectable infrastructure and human-readable outputs. Reuse suitable utilities; avoid unnecessary dependencies and frameworks.
- Do not execute untrusted source code or install dependencies without approval.
- Do not perform destructive operations without approval. Preserve unrelated work and original sources.
- Check retained utilities' paths, assumptions and output locations before running them; their legacy conventions are not architectural requirements.
- Retrieve relevant material progressively rather than rereading the entire corpus for every task.
- Report changes, verification results and unresolved decisions. Seek user direction when consequential professional positioning or scope is ambiguous.
