Read AGENTS.md and review the current state of the
Career Profile project.

The academic course profiles and scientific paper
profile have already been completed.

We are now beginning the analysis of the master's
thesis.

IMPORTANT

This task is NOT to produce the final thesis profile.

The objective is to reconstruct and critically assess
the technical work represented by the thesis documents
and its associated Git repository.

The available sources contain valuable technical
information, but their reliability is uneven.

In particular, the thesis repository is poorly
organized, contains redundant or potentially obsolete
material, and may not accurately represent the final
state of the research.

Do not assume that every documented method was
implemented or that every repository file represents
completed research.

OBJECTIVE

Produce a detailed, evidence-based technical
reconstruction of the master's thesis.

Identify what was investigated, formulated, implemented,
tested, demonstrated, and concluded.

Distinguish verified work from incomplete, proposed,
ambiguous, or unsupported claims.

SOURCES

Locate the thesis sources using config/sources.yaml
and the existing repository inventory.

Analyze:

1. The final master's thesis PDF.
2. The final defense presentation PDF:
   00_sources/master_thesis/final_presentation_notes.pdf
3. The presentation LaTeX source:
   00_sources/master_thesis/final_presentation.tex
4. The associated local Git repository, including
   relevant source code, configuration files,
   experiment artifacts, documentation, and history.

Use the presentation LaTeX source to recover precise
mathematical expressions and technical details when
PDF extraction is incomplete.

Treat the PDF and its LaTeX source as two representations
of the same presentation, not as independent evidence.

Do not modify the original sources or the thesis
repository.

ANALYSIS STRATEGY

Work systematically, but avoid unnecessary exhaustive
inspection of redundant files.

Begin with a high-level map of the thesis and repository.

Identify:

- Main research objectives.
- Mathematical and engineering problems.
- Theoretical models and assumptions.
- Algorithms and computational methods.
- Software architecture and major components.
- Experimental workflows.
- Evaluation methods and reported results.

Then investigate the relevant components in detail.

Use the thesis and presentation to identify candidate
methods and experiments.

Use repository evidence to investigate whether and how
those methods were implemented.

Conversely, use the repository to identify relevant
technical work that may be missing or insufficiently
explained in the written documents.

Do not assume that the absence of an easily identifiable
implementation proves that a method was not implemented.

MATHEMATICAL AND TECHNICAL RECONSTRUCTION

Preserve the technical depth of the work.

Where supported by evidence, reconstruct:

- Mathematical formulations and governing equations.
- Dynamical models and modeling assumptions.
- Optimization problems and constraints.
- Control methods and controller architectures.
- Numerical methods and solver configurations.
- Data-processing and computational pipelines.
- Algorithms and implementation details.
- Experimental setups and evaluation metrics.
- Quantitative results and their interpretation.

Trace important relationships between:

research objective
-> mathematical formulation
-> computational implementation
-> experimental configuration
-> reported result

Use exact references to equations, sections, figures,
tables, source files, functions, and commits when useful.

REPOSITORY INVESTIGATION

Treat the Git repository as historical research evidence,
not as a clean software product.

Inspect its structure and relevant Git history.

Identify:

- Main code paths and computational components.
- Scripts associated with reported experiments.
- Relevant configurations and parameter values.
- Alternative or abandoned implementations.
- Duplicate or obsolete files.
- Dependencies between important components.
- Evidence supporting or contradicting thesis claims.

Prioritize files that are relevant to the documented
research questions and results.

Do not infer that the newest file is necessarily the
correct or final implementation.

Use Git history to resolve meaningful ambiguities
where possible.

Avoid spending disproportionate effort cataloging
irrelevant duplicates or unrelated files.

Do not refactor, clean up, reorganize, or repair the
historical repository.

Do not execute untrusted project code, install
dependencies, or launch expensive experiments.

EVIDENCE AND CONFIDENCE

For each important technical claim, distinguish:

- Documented: explicitly stated in the thesis or
  presentation.
- Implemented: supported by identifiable code or
  configuration.
- Experimentally supported: backed by identifiable
  experiment artifacts or reported results.
- Proposed or planned: described without sufficient
  evidence of implementation.
- Ambiguous or inconsistent: conflicting or
  insufficient evidence.

These categories are not mutually exclusive.

Do not confuse:
- A method being discussed with its implementation.
- Code existing with proof that it was executed.
- A reported result with independently reproducible
  experimental evidence.
- Technical knowledge with individual achievement.

Explain material discrepancies without inventing
resolutions.

When evidence is incomplete, identify what additional
information would resolve the uncertainty.

OUTPUT

Create:

02_profiles/projects/_analysis/thesis_analysis.md

This is an internal technical reconstruction document,
not a CV-ready profile.

Organize it into clear sections covering:

1. Source inventory and reliability assessment.
2. Research objectives and problem formulation.
3. Mathematical and theoretical foundations.
4. Technical methods and algorithms.
5. Software and repository architecture.
6. Implementations and computational workflows.
7. Experiments, evaluation, and results.
8. Cross-source consistency and discrepancies.
9. Verified technical knowledge and experience.
10. Proposed, incomplete, or uncertain work.
11. Open questions requiring user clarification.
12. Evidence references and overall assessment.

Adapt the structure when necessary to represent
the actual technical content of the thesis.

Make the document technically detailed and useful
as the basis for a later validated thesis profile.

CHECKPOINTING

This investigation may be substantial.

Work incrementally.

Save meaningful progress to the target analysis
document as the investigation develops.

Clearly distinguish provisional findings from
validated conclusions.

Avoid overwriting verified findings with unsupported
later interpretations.

If interrupted, the repository should preserve
enough information to resume without restarting
the entire investigation.

COMPLETION

Before finishing:

- Check coverage of the main thesis sections.
- Check coverage of the final presentation.
- Check that relevant repository components have
  been investigated.
- Verify that important mathematical methods,
  implementations, experiments, and results have
  traceable evidence.
- List unresolved contradictions and uncertainties.
- Identify questions that require the user's input.

Report:

- Analysis document created.
- Main technical components reconstructed.
- Strongest evidence supporting the implemented work.
- Important inconsistencies or limitations.
- Questions requiring user clarification.

SCOPE

Analyze only the master's thesis and its associated
sources.

Do not produce the final thesis profile yet.

Do not analyze pyLowOrder or revisit the scientific
paper.

Do not generate thematic knowledge-base files,
the master profile, or CVs.

Do not modify the original thesis repository.

Stop after completing the technical reconstruction.
