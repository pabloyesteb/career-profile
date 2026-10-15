Read AGENTS.md and review the current state of the
Career Profile project.

The academic course profiles, scientific paper profile,
and master's thesis profile have been completed.

We are now beginning the analysis of pyLowOrder.

IMPORTANT CONTEXT

pyLowOrder is a collaborative scientific software
project.

The repository contains contributions from multiple
developers, and its structure and history may include
redundant, experimental, or poorly maintained material.

The objective is NOT to profile the entire repository
as the user's personal work.

The objective is to identify and reconstruct the user's
individual technical contributions.

OBJECTIVE

Produce a source-grounded analysis of the user's
contributions to pyLowOrder.

Identify the mathematical methods, algorithms,
software components, computational techniques,
experiments, and technical knowledge represented
by those contributions.

This is professional technical profiling, not a
software quality audit.

SOURCES

Locate the configured local pyLowOrder Git repository
using config/sources.yaml.

The project's public remote is:

https://github.com/ArnauMiro/pyLowOrder.git

Prefer the configured local repository for Git history,
source code, and relevant project documentation.

Use the repository as historical evidence.

Do not modify it.

ATTRIBUTION FIRST

Begin by inspecting Git history.

Identify the user's commit identities using available
repository evidence.

Consider author names, email addresses, commit
metadata, and other relevant attribution evidence.

Do not assume that all commits under a vaguely
matching name belong to the user.

If identity is ambiguous, record the uncertainty.

Identify relevant commits and changes authored by
the user.

Inspect their diffs, affected files, and technical
purpose.

Where relevant, inspect surrounding code and project
history to understand how the changes fit into the
larger system.

Distinguish:

- Directly attributable contributions.
- Collaborative work with identifiable participation.
- Existing project infrastructure used or extended.
- Contributions by other developers.
- Changes whose authorship remains uncertain.

Do not attribute entire files or subsystems to the
user merely because they modified them.

TECHNICAL RECONSTRUCTION

For the user's identified contributions, reconstruct:

1. The problem or requirement addressed.
2. Relevant mathematical and numerical foundations.
3. Algorithms and computational methods.
4. Software components and implementation details.
5. Programming languages, libraries, and tools.
6. Tests, experiments, benchmarks, or validation.
7. Integration with the surrounding project.
8. Technical outcomes and limitations.

Inspect enough surrounding project code to understand
the contribution accurately.

Preserve meaningful technical details.

Do not reduce the analysis to a list of commits
or generic programming skills.

Do not infer that every method supported by pyLowOrder
was personally implemented by the user.

REPOSITORY INVESTIGATION

Prioritize:

- Git commits and diffs attributable to the user.
- Relevant source files and their history.
- Tests and examples associated with those changes.
- Documentation explaining the modified components.
- Dependencies and interfaces needed to understand
  the user's work.

Use Git history to distinguish original implementation,
modification, refactoring, bug fixes, and integration.

Avoid exhaustive analysis of unrelated modules.

Do not refactor or clean the historical repository.

Do not execute untrusted code or install dependencies.

EVIDENCE

For each substantial contribution, provide:

- Relevant commit hashes.
- Affected source files.
- Functions, classes, or modules where appropriate.
- Technical explanation of the change.
- Evidence supporting individual attribution.
- Relevant tests or results, if available.

Distinguish implemented functionality from proposed
work or unverified experimental outcomes.

If a contribution was later modified or replaced,
record the historical contribution rather than
assuming current HEAD still represents it.

OUTPUT

Create:

02_profiles/projects/_analysis/pyloworder_analysis.md

Organize the document around identifiable
contributions and their technical content.

Include:

1. Repository and attribution context.
2. User-associated Git identities.
3. Contribution inventory with evidence.
4. Detailed technical reconstruction.
5. Mathematical and numerical methods.
6. Software engineering and computational tools.
7. Tests, validation, and outcomes.
8. Collaborative boundaries and uncertainties.
9. Technical knowledge represented by the work.
10. Questions requiring user clarification.

This is an internal analysis document, not the final
professional profile.

CHECKPOINTING

Work incrementally and preserve useful progress.

If the repository is large, prioritize attribution
and relevant diffs before reading entire modules.

Save findings as the investigation progresses so
that interrupted executions can resume efficiently.

COMPLETION

Verify that the major attributable contributions
have been investigated.

Report:

- User-associated commits identified.
- Main components and methods contributed.
- Relevant technical knowledge.
- Attribution uncertainties.
- Any questions requiring user clarification.

SCOPE

Analyze only pyLowOrder.

Do not modify completed course, paper, or thesis
profiles.

Do not generate the final pyLowOrder profile yet.

Do not generate thematic knowledge-base files,
the master profile, or CVs.

Stop after completing the contribution analysis.
