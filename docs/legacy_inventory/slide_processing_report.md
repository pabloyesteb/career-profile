# Slide-processing validation: Fundamentals of Optimization for Machine Learning

Historical reference retained during inventory simplification. Links and source locations have been updated; dated processing statuses and workflow instructions below describe the retired extraction phase. The active registry is `01_inventory/sources.yaml`; document fingerprints remain in the relevant project profiles.

Validation completed: 2026-10-13. Scope is limited to course ID `additional-foml` and archive `00_sources/tum/archives/fund_opt_ML_CIT413031.zip`.

## Result

Text extraction is necessary and useful for this archive, but **text alone is not sufficient** for a technically reliable course profile. All 23 PDFs contain selectable text, and layout-preserving extraction recovers most titles, prose, algorithm names, assumptions, and many formulas. It does not consistently preserve mathematical symbols or spatial semantics, and it omits the meaning carried by plots, geometric diagrams, arrows, color, and reveal order.

The validated method is therefore hybrid: extract every page with layout information, build a complete page/topic map, then render and visually inspect mathematically dense, low-text, multi-column, tabular, diagrammatic, plot-heavy, embedded-screenshot, and progressive-reveal pages. This method was used to produce `02_profiles/courses/additional-foml-fundamentals-of-optimization-for-machine-learning.md`.

## Source identity and complete PDF inventory

The archive is user-confirmed as corresponding to the transcript course. Its internal provenance is more specific—and different from the earlier inventory description:

- The coherent 21-deck sequence is root `lect1.pdf` plus `MIT_course/lect2.pdf`–`lect21.pdf`. Its slides identify themselves as **MIT 6.881 Optimization for Machine Learning**, Suvrit Sra, spring 2021. It totals 1,811 physical PDF pages.
- `mlss_lect1.pdf` identifies itself as a Suvrit Sra lecture for the Machine Learning Summer School at MPI-IS Tübingen, June 2017.
- `pkuLectIntro.pdf` identifies itself as a Suvrit Sra introduction for the PKU Summer School on Data Science, July 2017.
- Lecture 14 is titled “Gradient Flow and Diffusion”; its PDF metadata names `Xiang` as author. It sits in the MIT sequence and is treated as a guest/special-topic lecture.
- No PDF is internally labelled as a TUM course deck. The archive may have been assembled for the TUM course, but the files themselves do not establish which slides were delivered there. The filename suggests `CIT413031`; the transcript has no module code, so this remains archive metadata rather than official transcript metadata.

| Archive member | Pages | Internal title/topic | Evidenced provenance / role |
|---|---:|---|---|
| `lect1.pdf` | 68 | Lecture 1: Overview; Convex sets & functions | MIT 6.881, 2021; backbone |
| `MIT_course/lect2.pdf` | 104 | Conjugates, subdifferentials | MIT 6.881, 2021; backbone |
| `MIT_course/lect3.pdf` | 81 | Basic problems, duality | MIT 6.881, 2021; backbone |
| `MIT_course/lect4.pdf` | 93 | Optimality conditions | MIT 6.881, 2021; backbone |
| `MIT_course/lect5.pdf` | 77 | Nonconvex optimality, stationarity | MIT 6.881, 2021; backbone |
| `MIT_course/lect6.pdf` | 67 | Tractable nonconvex problems | MIT 6.881, 2021; backbone |
| `MIT_course/lect7.pdf` | 169 | First-order methods | MIT 6.881, 2021; backbone |
| `MIT_course/lect8.pdf` | 89 | Subgradient method; accelerated gradient | MIT 6.881, 2021; backbone |
| `MIT_course/lect9.pdf` | 35 | Faster stochastic methods | MIT 6.881, 2021; backbone |
| `MIT_course/lect10.pdf` | 81 | Frank–Wolfe methods | MIT 6.881, 2021; backbone |
| `MIT_course/lect11.pdf` | 96 | Proximal methods | MIT 6.881, 2021; backbone |
| `MIT_course/lect12.pdf` | 124 | Coordinate descent, BCD, alternating minimization | MIT 6.881, 2021; backbone |
| `MIT_course/lect13.pdf` | 94 | EM, CCCP, and related MM methods | MIT 6.881, 2021; backbone |
| `MIT_course/lect14.pdf` | 17 | Gradient Flow and Diffusion | MIT-sequence guest deck, 2021; backbone |
| `MIT_course/lect15.pdf` | 100 | Convex–concave minimax problems | MIT 6.881, 2021; backbone |
| `MIT_course/lect16.pdf` | 93 | Nonconvex saddle-point problems | MIT 6.881, 2021; backbone |
| `MIT_course/lect17.pdf` | 114 | Geometric Optimization I | MIT 6.881, 2021; backbone |
| `MIT_course/lect18.pdf` | 27 | Geometric Optimization II | MIT 6.881, 2021; backbone |
| `MIT_course/lect19.pdf` | 98 | Optimization for neural networks | MIT 6.881, 2021; backbone |
| `MIT_course/lect20.pdf` | 106 | Optimization for neural networks II | MIT 6.881, 2021; backbone |
| `MIT_course/lect21.pdf` | 78 | Interior-point methods: introduction | MIT 6.881, 2021; backbone |
| `mlss_lect1.pdf` | 147 | Optimization for Machine Learning, Lecture 1 | MPI-IS Tübingen MLSS, June 2017; supplementary overlap |
| `pkuLectIntro.pdf` | 146 | Optimization for Machine Learning, Introduction | PKU Summer School, July 2017; supplementary overlap |
| **Total** | **2,104** | 23 slide decks | 21-deck backbone + 2 external overview decks |

There are no separate exercises, solutions, projects, exams, notebooks, source-code files, or datasets in the ZIP. Exercises and challenges occur inside the slides.

## Processing performed

1. The ZIP member list was compared with the existing course/archive inventory.
2. `pdfinfo` was used to obtain page counts and metadata; `pdffonts` confirmed embedded font resources.
3. Every PDF was extracted page-by-page with `pdftotext -layout`. Form-feed boundaries were retained so topics and claims could be tied to one-based physical PDF pages.
4. A page-title map was built for all 23 decks. This exposed the complete Lecture 1–21 sequence and prevented late-course topics from being missed.
5. Keyword and heading passes identified theorem, assumption, algorithm, convergence, complexity, comparison, application, and exercise slides.
6. Representative pages were rendered with `pdftoppm` and inspected visually. Coverage included early, middle, and late lectures; formulas, diagrams, comparison tables, algorithms, plots, and multi-column layouts were all sampled.
7. The technical profile was drafted against the complete lecture map, then cross-checked lecture-by-lecture. The two 2017 decks were used only to confirm overlapping early material.

No course code or other untrusted archive content was executed.

## Selectable text and page-level behavior

All 23 PDFs have a text layer. Every one of the 2,104 physical pages produced at least some extracted text; on sparse or visual pages that may be only a title and footer. This is materially better than scanned-image slides, and OCR was not needed.

The raw page volume is misleading. Beamer/PowerPoint overlays create several physical pages for one logical slide, each adding a bullet, equation line, or algorithm step. Consequences include:

- extensive repeated text in a full-deck extraction;
- incomplete algorithms or theorems on early reveal pages;
- pages that look almost empty even though later physical pages with the same displayed slide number contain the full content;
- a mismatch between the physical PDF page cited by tools and the smaller logical slide number printed in the footer.

For this report and the course profile, page numbers mean one-based physical PDF pages. When a logical slide has several reveal states, the final state is the authoritative visual reference, while earlier states remain useful for understanding order.

## Reliability by content type

| Content type | Text extraction result | Required treatment |
|---|---|---|
| Titles, headings, bullets, references | Generally reliable and in page order | Use extracted text; spot-check unusual fonts |
| Simple single-line formulas | Often readable, especially LaTeX-generated decks | Verify key assumptions, inequalities, exponents, and norms visually |
| Dense or Unicode-heavy mathematics | Partially reliable | Render the page; do not reconstruct missing symbols from subject knowledge |
| Algorithms revealed stepwise | Repeated and often incomplete on early states | Group identical logical titles/footer numbers and inspect the final reveal |
| Tables | `-layout` often retains rough rows/columns, but associations can drift | Render and confirm row/column labels and units |
| Two-column comparisons | Reading order may interleave left and right columns | Render; interpret each column spatially |
| Geometric diagrams and arrows | Labels may extract, geometry does not | Render; use the diagram only for claims visible on the page |
| Plots and experimental curves | Captions/legends may extract incompletely; curve ordering is absent | Render and avoid claiming numerical comparisons not visibly supported |
| Embedded paper screenshots | Text may be duplicated, densely interleaved, or garbled | Use surrounding slide claims; inspect screenshot visually only when needed |
| Color/emphasis | Not represented in plain text | Render when color encodes method, sign, selected condition, or comparison |

## Representative visual checks

The following one-based physical pages were inspected as representative checkpoints; adjacent/final reveal pages were consulted where the first checkpoint was incomplete.

| Deck/page | Content checked | Finding |
|---|---|---|
| `lect1.pdf`, p. 31 | Convex function and secant-line diagram | Extraction loses `λ` and much of the geometric relationship; visual inspection is essential. |
| `MIT_course/lect7.pdf`, p. 44 | Descent lemma | The main inequality is substantially recoverable, but superscripts/subscripts and norm powers still require confirmation. |
| `MIT_course/lect9.pdf`, pp. 8–11 | Strong/non-strong convex runtime comparisons | Early reveal pages omit table rows; the completed table must be viewed visually to preserve method-to-complexity mappings. |
| `MIT_course/lect10.pdf`, p. 50 | Frank–Wolfe zigzagging | Extracted text contains almost only the title; the feasible polytope, iterate path, selected atom, and optimum are visual. |
| `MIT_course/lect13.pdf`, p. 74 | Sinkhorn theorem | Prose and theorem statement extract well; visual check confirms matrix notation and the role of alternating row/column normalization. |
| `MIT_course/lect14.pdf`, p. 12 | Langevin diffusion versus Euclidean gradient flow | Two-column equations are interleaved and several norm squares/radicals disappear in extraction; the rendered page is necessary. |
| `MIT_course/lect16.pdf`, pp. 65–69 | GDA/max-oracle reveal sequences | Individual physical pages show only partial algorithms. Final reveals plus extracted surrounding text recover the intended iterations. |
| `MIT_course/lect17.pdf`, p. 62 | Geodesic convexity on positive-definite geometry | Formula text is partly recoverable, but the plotted ordinary concavity versus geodesic-convex interpretation is visual. |
| `MIT_course/lect19.pdf`, p. 34 | Backpropagation computation | Equations and labels mostly extract, but `θ`, the loss symbol, and alignment between formulas and network roles degrade. |
| `MIT_course/lect20.pdf`, pp. 34–43 | Adam sequence and MNIST optimizer plot | A title-only reveal contains no algorithm; the experiment's curve/legend relationship is entirely visual. |
| `MIT_course/lect21.pdf`, pp. 71–75 | Path-following and self-concordant barriers | Early reveal has only the first path-following step; later pages are required for the complete method and barrier properties. |

Additional inspection of headings and extracted page blocks covered every lecture, including late material on Riemannian optimization, neural-network training, saddle escape, and interior-point methods.

## Mathematical extraction findings

Text extraction is strongest in the LaTeX-generated MIT decks but still exhibits systematic loss:

- Greek symbols can vanish or become unrelated glyphs (`λ`, `μ`, `θ`, `ε`).
- Set-membership and mapping symbols can collapse (`x∈X` may appear as `x2X`; arrows and implication signs vary).
- Superscripts/subscripts and norm powers can be detached, causing squared norms or conjugates to look like ordinary terms.
- `ℓ₁`, `ℓ₂`, dual-norm stars, transposes, expectations, and probability-law notation are not uniformly preserved.
- Fractions and multi-line constraints can be linearized in an ambiguous order.
- In Lecture 14, the extracted version of the Langevin/gradient-flow comparison omits visible square roots and squared norms and interleaves left/right columns.
- Equations embedded in screenshots or imported paper excerpts are substantially less reliable than native slide equations.

Accordingly, the profile records only formulas and rates confirmed by legible slide text and/or rendering. Missing expressions were not reconstructed from general optimization knowledge.

## Visual information that changes the interpretation

- Convexity and epigraph slides use curves, chords, tangents, and shaded feasible regions to encode definitions.
- Frank–Wolfe slides use polytope geometry to explain sparse extreme-point steps, zigzagging, and away directions.
- Runtime and convergence comparisons rely on table alignment, not merely extracted tokens.
- Logistic-regression, Gaussian-mixture, neural-network, and optimizer experiments communicate relative behavior through curves and legends.
- Manifold and positive-definite-matrix slides use geometric paths and plots to distinguish Euclidean from geodesic convexity.
- Backpropagation and automatic-differentiation material uses aligned computational roles and diagrams.
- Reveal order is pedagogically significant for algorithm derivations, proofs, and progressively populated comparison tables.

## Information not recoverable from the PDFs

The visible slide content was recoverable to the level needed for the profile through combined text and rendering. The following evidence is absent rather than technically extractable:

- lecturer narration, derivations made live, and answers to embedded exercises;
- speaker notes and original animation timing;
- separate TUM syllabus, exercise sheets, solutions, assessments, projects, or code;
- a file-level indication of which decks or subset were actually delivered in the TUM course;
- an official TUM module code in the transcript.

These gaps prevent stronger claims about assessment, hands-on implementation, and TUM-specific coverage. They do not justify filling missing details from external knowledge.

## Recommended workflow for other slide-based courses

1. **Establish provenance per deck.** Read the title slide, footer, author, date, and PDF metadata; do not infer provenance from ZIP placement alone.
2. **Extract all pages with layout.** Retain page breaks and record both physical PDF page and displayed logical slide number when available.
3. **Map the entire sequence before profiling.** Generate a per-deck heading map and explicitly cover beginning, middle, and end so late topics are not omitted.
4. **Detect reveal groups.** Consecutive pages with the same title/footer slide number should be treated as one evolving logical slide. Use the final reveal for complete content and earlier reveals only to understand order.
5. **Flag pages for rendering.** Always render pages containing dense equations, theorem assumptions, convergence rates, pseudocode, tables, multiple columns, diagrams, plots, screenshots, or suspiciously little extracted text.
6. **Verify mathematics conservatively.** Compare extracted and rendered notation. If a symbol remains illegible, record the limitation; never repair it from expected theory.
7. **Use visuals for relationships, not decoration.** Capture geometry, table mappings, curve legends, arrows, and color-coded comparisons only when visibly supported.
8. **Cite physical pages.** State the numbering convention and give member path plus physical PDF page, especially when overlays make the printed slide number non-unique.
9. **Separate backbone from supplements.** Use a complete ordered course sequence as the syllabus backbone and externally branded/overlapping decks only as corroboration unless course-specific evidence says otherwise.
10. **Validate against the map.** Before completion, account for every deck and major block, check algorithm/rate assumptions, and record missing exercises, code, exams, and provenance as limitations.

## Profile and manifest outcome

- Created: `02_profiles/courses/additional-foml-fundamentals-of-optimization-for-machine-learning.md`.
- The 21-deck lecture sequence is fully mapped to profile sections.
- The two 2017 overview decks are explicitly supplementary.
- The processing manifest is marked `complete_validated`, with a follow-up note to retain the unresolved TUM-versus-internal-provenance distinction.
- No other course was processed.
