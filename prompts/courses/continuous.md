Read AGENTS.md and review the current state of the
Career Profile project, including the course inventory,
processing manifest, completed profiles, and relevant
processing reports.

OBJECTIVE

Complete the remaining academic course profiling work
through successive adaptive batches.

Work autonomously and continue processing courses until
all eligible courses have been completed or execution
limits prevent further progress.

WORKFLOW

1. Identify courses that still require profiling using
   the processing manifest and source inventory.

2. Select a manageable batch based on document volume,
   formats, and expected processing complexity.

3. Analyze each course independently, following the
   methodology established in AGENTS.md and the
   completed validated profiles.

4. Produce a technically detailed, source-grounded
   Markdown profile for each course.

5. Validate the profile against the complete structure
   of its available teaching materials.

6. Save the profile and update the processing manifest
   immediately after completing each course.

7. Record relevant source ambiguities or inconsistencies
   in the existing review issues file.

8. Once a batch is completed, select the next batch
   and continue automatically.

Do not stop to request confirmation between batches.

ANALYSIS QUALITY

Maintain the technical specificity and evidence standards
established by the completed profiles.

Identify mathematical concepts, theories, theorems,
algorithms, numerical methods, computational techniques,
software tools, and applications.

Use text extraction, code inspection, and selective
visual analysis as appropriate for each source.

Ensure coverage of the complete available course material,
including relevant exercises, solutions, and computational
files.

Distinguish substantial technical coverage from brief
mentions or introductory examples.

Reuse existing extractions and intermediate results
where useful.

Preserve source references and document meaningful
inconsistencies.

PROGRESS AND RECOVERY

Treat each completed course as an independent checkpoint.

After completing and validating a course:
- Write its profile to 02_profiles/courses/.
- Update 01_inventory/processing_manifest.csv.
- Record unresolved source issues where relevant.

Do not postpone these updates until the end of a batch.

Before starting a course, check whether a validated
profile already exists to avoid duplicate processing.

If execution is interrupted, the repository should
retain all completed work and accurately reflect
the remaining tasks.

COURSE ELIGIBILITY

Focus on courses with available teaching materials.

IN2138 Robot Motion Planning has no available teaching
materials and should be skipped.

MA8102 Internship corresponds to the pyLowOrder project
and will be analyzed during project profiling.

Preserve the academic metadata of both courses.

Follow existing project conventions for any other
courses without sufficient source material.

COMPLETION

Continue selecting and processing batches until no
eligible courses remain.

Once all eligible courses have been profiled, perform
a final consistency review of the course inventory,
processing manifest, and completed profiles.

Verify that every course is accounted for and that
the manifest accurately represents the final state.

Report:
- Courses completed during this execution.
- Profiles created.
- Remaining courses, if any.
- Unresolved source issues.
- Final processing status.

SCOPE

Do not modify previously validated course profiles
unless necessary to correct a demonstrable error.

Do not generate thematic knowledge-base files.

Do not analyze the master's thesis, scientific article,
or pyLowOrder.

Do not begin CV generation.

Continue autonomously until the course profiling phase
is complete or execution limits prevent further work.
