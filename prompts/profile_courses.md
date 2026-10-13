# Incremental Course Profiling

Read AGENTS.md and review the current state of the
Career Profile project.

Consult the course inventory, processing manifest,
existing course profiles, and relevant processing reports.

## Objective

Continue building the technical knowledge base by
analyzing university courses that have not yet been
profiled.

Produce detailed, source-grounded Markdown profiles
consistent with the completed pilot courses.

## Batch selection

Review the remaining courses and their available
source materials.

Select a small batch that can reasonably be completed
within this execution.

Base the batch size on the amount and complexity of
the available material.

Prefer grouping courses with manageable workloads.
Process particularly extensive or complex courses
individually.

If no courses with available material remain pending,
report that the course profiling phase is complete
and stop.

## Analysis

Analyze each selected course independently.

For each course:

1. Inspect the available teaching materials and
   establish the structure of the course.

2. Identify the technical knowledge covered, including
   mathematical concepts, theories, theorems, algorithms,
   numerical methods, models, computational tools,
   and applications.

3. Use an appropriate combination of text extraction,
   source inspection, and selective visual analysis.

4. Cover the complete lecture sequence and incorporate
   relevant information from exercises, solutions,
   assignments, and computational material.

5. Create a technically detailed Markdown profile
   consistent with the established examples.

6. Include references to the original source documents.

7. Validate the profile against the available materials.

8. Save the completed profile and update the processing
   manifest before starting the next course.

## Processing efficiency

Inspect document structure before performing extensive
extraction.

Reuse existing extracted text and intermediate results
where available.

Prefer targeted inspection over repeatedly reading
large documents in full.

For slide-based material, identify the lecture structure
and topic coverage before examining detailed content.

Use visual inspection where necessary to understand
mathematical expressions, diagrams, plots, or other
information not reliably captured by text extraction.

Avoid redundant analysis of repeated material and
progressively revealed slides.

Use scripts for mechanical processing when appropriate.

Maintain technical depth and source coverage while
minimizing unnecessary context consumption.

## Quality requirements

Each profile must:

- Represent all major topics covered by the available
  teaching material.
- Identify specific methods, algorithms, mathematical
  results, and computational techniques.
- Preserve meaningful distinctions between concepts.
- Use accurate technical terminology.
- Provide traceable references to the source material.
- Follow the established profile structure and
  thematic categorization.

The objective is a reusable technical knowledge
inventory, not a generic course summary.

## Project updates

After completing each course:

- Save its profile under 02_profiles/courses/.
- Update 01_inventory/processing_manifest.csv.
- Record relevant ambiguities in
  01_inventory/review_issues.md.

Preserve previously completed profiles and the
established project organization.

## Scope

Process only the selected course batch.

Do not generate thematic knowledge-base files.

Do not analyze the thesis, scientific article,
pyLowOrder, or other research projects.

## Final report

Report:

1. Courses completed and processing status.
2. Profiles created.
3. Main technical areas covered.
4. Relevant source limitations or unresolved issues.
5. Remaining courses with available material.
