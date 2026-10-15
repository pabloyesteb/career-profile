Read AGENTS.md and review the current state of the
Career Profile project.

The academic course-profiling phase is complete.
We are now beginning research and software project
profiling, starting with the coauthored scientific paper.

OBJECTIVE

Create a detailed, source-grounded technical profile
of the scientific paper.

The paper is the primary and sufficient technical
source for this task. Its scientific content accurately
reflects the work and the technical knowledge involved.

SOURCE

Locate the scientific paper using config/sources.yaml
and the existing project inventory.

If necessary, use the publication identified by:

https://www.sciencedirect.com/science/article/pii/S0957417425007912

Prefer the locally available full text when possible.

ANALYSIS

Read the complete paper, including its mathematical
formulations, methodology, experiments, results,
figures, tables, and conclusions.

Identify and document:

1. Research problem, motivation, and objectives.
2. Mathematical models and theoretical foundations.
3. Algorithms, numerical methods, and computational
   procedures.
4. Methodological choices and technical architecture.
5. Experimental design, datasets, baselines, and
   evaluation metrics.
6. Main results and their technical interpretation.
7. Limitations and assumptions stated in the paper.
8. Programming languages, software tools, and
   libraries explicitly evidenced by the source.
9. Technical knowledge represented by the work.
10. Connections to relevant mathematical, computational,
    and application domains.

Preserve technical specificity. Include relevant
equations, algorithmic details, and quantitative
results where they are important to understanding
the work.

Do not replace the technical analysis with a generic
abstract or high-level publication summary.

ATTRIBUTION

This is a coauthored publication.

Distinguish between:
- Technical content documented in the paper.
- Contributions explicitly attributed to the user.
- Contributions whose individual authorship cannot
  be established from the available source.

The user confirms that the paper's technical content
corresponds to their knowledge.

Therefore, the complete technical content may inform
the knowledge base, but do not infer that the user
individually implemented every algorithm, performed
every experiment, or wrote every section.

If individual contributions cannot be established,
record that limitation without blocking the profile.

EVIDENCE AND VALIDATION

Use the paper as the authoritative technical source.

Reference relevant sections, equations, figures,
tables, and pages.

Verify that the profile covers the complete paper,
including important methodological and experimental
details.

Do not introduce unsupported technical claims,
additional experiments, or speculative contributions.

There is no need for a separate forensic analysis
stage unless a material inconsistency or ambiguity
is discovered.

OUTPUT

Create:

02_profiles/projects/scientific_paper.md

Follow the established profiling conventions where
appropriate, adapting the structure to a research
publication rather than an academic course.

Update the relevant processing inventory or manifest
if the project already tracks research publications.
Do not invent a new tracking system unnecessarily.

COMPLETION

Report:
- Profile created.
- Main technical areas identified.
- Important methods and results documented.
- Any unresolved attribution or source limitations.

SCOPE

Analyze only this scientific paper.

Do not analyze the master's thesis or pyLowOrder.
Do not generate thematic knowledge-base files,
the master profile, or CVs.
