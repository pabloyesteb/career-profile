Career Profile — Project Instructions
Purpose
This repository builds a reusable, evidence-based knowledge base of my academic background, technical expertise, research, and software work. Its primary purpose is to support the later creation of tailored CVs and job applications without having to re-examine the original material for each application.
My background combines a Bachelor's degree in Aerospace Engineering with a Master's degree in Applied Mathematics at the Technical University of Munich (TUM).
The intended career directions are:
- Aerospace engineering, especially guidance, navigation, and control (GNC).
- Insurance, actuarial mathematics, and quantitative risk.
- Robotics, especially modeling and control.
- AI, machine learning, and data science engineering.
These directions guide future applications; they must not narrow or bias the initial inventory of my knowledge. Capture relevant content even if it does not fit one of these sectors.
Sources and repository layout
Consult README.md for project context and config/sources.yaml for the configured locations of source material and external repositories. Resolve relative paths consistently with the configuration file's location.
- 00_sources/: original academic documents, course archives, thesis and publication PDFs, transcripts, and previous CV material.
- 01_inventory/: catalogs of courses, files, sources, and processing status.
- 02_profiles/courses/: one technical profile per course.
- 02_profiles/supplementary/: source-grounded maps of supplementary academic materials, separate from transcript-accredited courses and personal project implementations. Track their provenance and status in 01_inventory/supplementary_processing_manifest.csv; do not add them to the transcript course count.
- 02_profiles/projects/: definitive profiles of the master's thesis, scientific publication, and relevant software contributions.
- 02_profiles/projects/_analysis/: internal reconstruction and contribution-analysis reports; not definitive profiles or direct thematic-synthesis inputs.
- 03_knowledge_base/: thematic syntheses across courses and projects.
- 04_master_profile/: consolidated academic and technical profile.
- 05_cv/: CV templates and sector-specific CVs.
- scripts/: utilities for inventory, extraction, and validation.
- .cache/: regenerable intermediate processing results, including extracted PDF text; exclude from version control.
External repositories may be referenced by local path or remote URL; do not assume that they are copied into this project.
Core approach
Work from the underlying evidence rather than from course titles or generic descriptions. The goal is a technically specific inventory of the material covered in my education and of the substantive content of my research and software projects.
For completed courses, treat the taught material as part of my knowledge base. Focus on identifying the content, not grading my proficiency.
Favor precise concepts over vague labels. For example, name the actual optimization algorithms, control methods, statistical models, numerical schemes, mathematical results, and software tools covered when the sources support them.
Be comprehensive without being repetitive. Preserve distinctions between related technical concepts, but consolidate duplicates and avoid padding profiles with generic language.
Course research
Use the grade transcript as the authoritative list of completed modules and their official metadata. Match course archives to transcript entries using codes, names, and other available evidence; flag ambiguous matches rather than guessing. Materials not matched to the transcript may still contain relevant knowledge; keep their provenance and academic status explicit.
Investigate course content using available materials such as lecture notes, slides, syllabi, exercises, solutions, assignments, projects, and examinations. Use official TUM module descriptions to complement or fill gaps in local material. Actual teaching material is generally more informative about specific topics than a short catalog description.
Inspect the structure of large archives before reading their contents. Identify representative and information-rich documents, then expand the inspection when needed to cover the full syllabus. Do not equate processing every page with thoroughness, and do not omit entire topic areas merely because they occur late in a course.
Document processing
Choose the processing approach according to the source format and its information content. Text extraction is useful for searchable PDFs, but may lose mathematical notation, reading order, tables, diagrams, plots, or layout-dependent explanations. For slide decks, assess extraction quality and inspect relevant pages visually when necessary. Account for the complete lecture or slide sequence when checking topic coverage, while avoiding redundant inspection of progressive slide builds.
Use scripts for repeatable extraction and reuse intermediate results where practical. Store regenerable text extractions and similar artifacts under .cache/, rather than repeatedly processing the same source. Prioritize recovering the technical knowledge covered by the material, not reproducing documents or derivations in full.
Course profiles
Each course profile should capture, where applicable:
- Official course name, code, credits, and grade, when established by the transcript.
- Main subjects, organized into meaningful topics and subtopics.
- Specific theories, mathematical results, models, and methods.
- Algorithms, numerical techniques, and computational approaches.
- Programming languages, libraries, and software tools explicitly covered.
- Important scientific or engineering applications.
- References to the supporting source files or official descriptions.
- Relevant thematic categories.
Use a consistent overall format without forcing irrelevant sections. Place algorithms and methods within their relevant technical topics; add separate summary tables only when they contribute useful information, such as complexity comparisons. Incorporate substantive material from exercises and assessments into the technical sections rather than repeating the syllabus. Check profile coverage against the source's chapter, lecture, or topic structure.
Research and software projects
Create separate profiles for the master's thesis, the scientific article, and contributions to pyLowOrder.
For the thesis, use both the final document and its source repository to understand the research question, mathematical and computational methodology, implementations, experiments, and principal results.
For the article, capture the scientific problem, methods, findings, and publication details. Do not infer my individual role solely from coauthorship.
For pyLowOrder, focus on my identifiable contributions rather than summarizing the whole repository as my work. Use author identities, Git history, diffs, and relevant code to determine the scope and technical substance of those contributions. If attribution is unclear, record the unresolved point.
Record the repository revision used for each analysis so that findings remain reproducible.
Knowledge organization
First produce source-grounded profiles of individual courses and projects. Then synthesize them into thematic knowledge-base files. Themes may include control theory, optimization, machine learning, statistics and data science, numerical mathematics, dynamical systems and robotics, aerospace engineering, and other areas justified by the material.
Categories are not mutually exclusive: a course or project may contribute to several themes. Use consistent terminology for related categories across profiles. Avoid duplicating full course profiles inside thematic files; summarize their contributions and link back to the detailed profiles.
Finally, build a consolidated master profile that makes the overall technical background easy to understand and retrieve. The knowledge base should remain useful independently of any particular job posting.
Evidence and accuracy
Make technical claims traceable. Cite source paths and, when useful, page numbers, section names, code paths, or commit hashes. References must identify real, accessible evidence; never invent them.
Separate directly supported information from unresolved questions. When sources conflict, prefer the most specific and relevant evidence and note material discrepancies. When material is missing, record the gap rather than silently substituting plausible content.
Use the transcript for grades and credits; do not infer them from course files. Do not invent projects, quantitative outcomes, publication contributions, or technologies.
Working practices
- Write profiles and knowledge-base content in clear technical English.
- Treat original documents and external repositories as read-only.
- Do not execute untrusted code from course archives or repositories.
- Do not install dependencies or perform destructive operations without approval.
- Use scripts for mechanical, repeatable tasks such as archive inspection, file inventories, text extraction, and structural checks.
- Maintain an inventory and processing status so work can be resumed without unnecessary reanalysis. Process source profiles incrementally and record completed work before moving on.
- Keep generated files consistently named and linked to stable course or project identifiers.
- Check that referenced files exist and that every transcript course is accounted for.
- Record significant ambiguities and questions requiring my input in a review file instead of silently making assumptions.
CV generation
CV writing is a downstream use of this knowledge base, not part of source extraction. When explicitly asked to prepare a CV, select and emphasize material according to the target role and its requirements, while preserving factual accuracy. Never alter the underlying profiles merely to make a candidate appear better suited to a role.
Task boundaries
Follow the scope of the current user request. Do not launch a full inventory, profile every course, rewrite the knowledge base, or generate CVs unless that work has been requested. At the end of a task, report the files created or changed, unresolved issues, and the next logical step.
