# 01 — Source-specific Knowledge Tree

## Purpose and boundaries

`01_tree/` represents each registered Source as a navigable hierarchy of structural **TreeNodes** and technically substantive **Items**. It captures the source's own organization and preserves precise provenance. It is not a taxonomy of recurring Topics across Sources; those interpretations belong to the future graph.

The Tree is a **representation of knowledge**, not a mirror of ZIP members, PDFs or file-system paths. Each Source is examined in full, generally in its original order. The resulting tree is complete in **coverage** but selective in **segmentation**: it resembles a technical index, not a transcript split into paragraphs.

## Conceptual components

### Source

A Source is the registered course, thesis or project being decomposed. The authoritative identifier and primary locations come from `00_sources/inventory/sources.yaml`; see [`00_sources.md`](00_sources.md). One Source may have many original files and many extracted Items.

### TreeNode

A TreeNode is a **structural division within one Source**, such as a chapter, lecture, section, subsystem or group of experiments. Nodes express *where* Items sit in the organization of the Source. They do not need technical summaries, type labels, Topic memberships or separate Markdown bodies.

A TreeNode has three required fields:

| Field | Meaning |
| --- | --- |
| `id` | Stable, unique node identifier within the source tree |
| `title` | Human-readable name of the division |
| `parent` | ID of another TreeNode in the same Source, or `null` for a top-level division |

Node-parent relationships form an acyclic forest within each Source; multiple `parent: null` nodes are valid.

### Item

An Item is a **coherent, independently useful unit of technical knowledge or experience** grounded in exactly one Source and assigned to exactly one primary TreeNode. It may describe a theorem, concept, algorithm, method, implementation, experiment or technical result. A single Item may contain supporting statements, derivations, assumptions, examples, limitations and routine corollaries: independence, not shortness, determines its boundary.

Every Item is a standalone Markdown file with five required YAML frontmatter fields:

| Field | Meaning |
| --- | --- |
| `id` | Globally unique, stable Item identifier; identical to the Markdown filename stem |
| `source` | Registered Source ID; matches one source tree YAML |
| `parent` | Primary TreeNode ID in that Source |
| `title` | Meaningful, human-readable title |
| `type` | Dominant nature of the knowledge represented |

The `type` vocabulary is deliberately small:

| Type | Typical content |
| --- | --- |
| `concept` | Definition, mathematical object, key construction or conceptual principle |
| `theorem` | Proposition, theorem or consequential corollary with its assumptions and arguments |
| `method` | Analytical or engineering approach without a fully defined computational algorithm |
| `algorithm` | Defined computational procedure, its formulation and behavior |
| `implementation` | Evidence of a concrete software/system implementation or component |
| `experiment` | Experimental design, measurements, comparisons or evaluation |
| `result` | Distinct technical finding not better described by the other kinds |

`type` records the dominant character of an Item; it does not force an Item containing mathematics and computation to be artificially split. There are no required `topic`, `order`, `confidence`, `category` or career-rating fields. Topic assignment and cross-source links belong to the future graph.

## Physical layout

Production data is divided by origin:

```text
01_tree/
  projects/
    trees/<source-id>.yaml
    items/<item-id>.md
  tum/
    trees/<source-id>.yaml
    items/<item-id>.md
  example_tree/
    projects/
      trees/example-research-project.yaml
      items/example-sparse-solver.md
    tum/
      trees/example-optimization.yaml
      items/example-kkt.md
      items/example-second-order.md
      items/example-newton.md
```

The `projects/` and `tum/` branches reflect `00_sources/raw/projects/` and `00_sources/raw/tum/`. This category is encoded by location, not by an additional data field. Sources are identified by the registry, **not** inferred from directory names. A Source's YAML tree and all its Items stay in the same category.

The files under `01_tree/example_tree/` are **isolated fixtures**. They are not production knowledge, their IDs do not need to occur in `sources.yaml`, and the project implementation must validate/render them in a separate example mode rather than by silently mixing them into production. Production directories and tree files are created only as extraction reaches each Source; unused Sources need no empty tree files.

## Single master navigation root

The read-only explorer presents one default, expanded master root and two category headings:

```text
▼ Career Profile                 (virtual master root)
  ▼ Projects                     (virtual category)
    ▼ <project Source>           (registered Source)
      ▼ <section>                (TreeNode)
        • <knowledge Item>       (Item)
  ▼ TUM                          (virtual category)
    ▼ <course Source>            (registered Source)
      ▼ <lecture or section>     (TreeNode)
        • <knowledge Item>       (Item)
```

**Career Profile**, **Projects** and **TUM** are synthetic navigation headings, not persisted TreeNodes or additional knowledge objects. The master root is displayed by default; no `master.yaml` or per-source synthetic root is necessary. `00_sources/aux/` is supporting evidence and has no default navigation branch.

## Tree YAML format

The YAML file for a Source records only the Source ID and structural nodes; it does not duplicate Item listings:

```yaml
source: example-optimization
nodes:
  - id: example-foundations
    title: Mathematical Foundations
    parent: null

  - id: example-optimality
    title: Optimality Conditions
    parent: null

  - id: example-constrained
    title: Constrained Optimization
    parent: example-optimality

  - id: example-algorithms
    title: Numerical Algorithms
    parent: null
```

An example Item associated with `example-constrained` carries the relation in its own frontmatter. The association is therefore stored **once**, not repeated as an `items:` list in the tree YAML. Nodes can be added incrementally as a source's actual structure becomes clear. YAML listing order and alphabetical Item filename order do not promise the source's original teaching chronology.

## Item Markdown format and worked examples

### Example 1 — Theorem (KKT necessary conditions)

`01_tree/example_tree/tum/items/example-kkt.md` illustrates a mathematical result. The following abbreviated excerpt shows the essential format:

```markdown
---
id: example-kkt
source: example-optimization
parent: example-constrained
title: Karush–Kuhn–Tucker Necessary Conditions
type: theorem
---

# Karush–Kuhn–Tucker Necessary Conditions

## Setting
For differentiable functions, consider minimizing
\(f(x)\) subject to \(g_i(x) \leq 0\) and \(h_j(x)=0\).

## Result
At a local minimum satisfying an appropriate constraint
qualification, multipliers exist that satisfy stationarity,
primal feasibility, dual feasibility and complementary slackness.

## Interpretation and limitations
The conditions are generally necessary, not sufficient, for
nonconvex optimization. Constraint qualifications matter.

## Source references
Demonstration example — not verified against MA3503 materials.
```

The complete illustrative Item can develop the Lagrangian, list the multiplier equations, explain complementary slackness and discuss cases where assumptions fail. These belong together; they do not automatically become separate Items.

### Example 2 — Compact, independently useful theorem

`01_tree/example_tree/tum/items/example-second-order.md` demonstrates why a short second-order sufficiency result may be an independent Item. For twice continuously differentiable \(f\), the conditions \(\nabla f(x^*)=0\) and \(\nabla^2 f(x^*)\succ0\) imply that \(x^*\) is a strict local minimizer. Whether this becomes its own Item or part of a broader "Unconstrained Optimality Conditions" Item depends on the source's depth and presentation; its brevity alone does not decide.

### Example 3 — Algorithm (Newton's method)

An algorithm Item such as `01_tree/example_tree/tum/items/example-newton.md` keeps its formulation, update rule, convergence hypotheses and limitations together:

```markdown
---
id: example-newton
source: example-optimization
parent: example-algorithms
title: Newton's Method for Unconstrained Optimization
type: algorithm
---

# Newton's Method for Unconstrained Optimization

## Formulation
The Newton direction solves
\(\nabla^2 f(x_k)p_k=-\nabla f(x_k)\), when the system is solvable.

## Procedure
Evaluate derivatives, solve for a direction and update the iterate.

## Convergence and limitations
Quadratic local convergence requires suitable regularity and
nonsingularity conditions. An indefinite Hessian need not yield a
descent direction; globalization variants address this issue.

## Source references
Demonstration example — not verified against MA3503 materials.
```

Variants such as trust-region Newton or BFGS can merit independent Items if the source develops distinct algorithms or theory.

### Example 4 — Implementation evidence

`01_tree/example_tree/projects/items/example-sparse-solver.md` illustrates an implementation Item linked to a project subsystem. Such an Item would normally describe the implemented component, design decisions, integration, tests, measured behavior, limitations and precise code references. **The existing example is fictional** and must not be interpreted as personal contribution evidence. A real implementation Item would cite actual repository files, commits or documented outputs.

### Example status

The mathematical material above is established mathematics, but **these examples have not been verified against the specific MA3503 course archive**. The project example is fictional. The example tree is exclusively for learning the format and testing tooling; no example Source belongs in the production inventory.

## Granularity and extraction coverage

Item boundaries follow **the smallest independently useful unit that remains technically coherent**:

- A theorem, its hypotheses, essential argument and routine corollaries normally form one Item.
- A major corollary or characterization with independent reuse can justify another Item.
- A numerical algorithm generally includes its derivation, steps, convergence assumptions, computational behavior and limitations.
- Supporting definitions or minor lemmas can stay inside a larger Item; independently reusable concepts may stand alone.
- A substantial implementation or experimental investigation can be its own Item, rather than being folded into a broad project summary.

This is neither one-Item-per-slide fragmentation nor one-Item-per-lecture summarization. Course credit values and page counts do not determine an Item quota. An index, syllabus or chapter list helps reconstruct the source's sequence and plan its extraction, but should not cause selective harvesting of highlights. Extraction proceeds linearly through all accessible substantive content, with reviewable batches and exact continuation points. A batch is **not** a representative sample or a statement of completion.

At the end of a Source, coverage is reviewed against its original contents and supporting material. Administrative notices and duplicated explanations need not become Items; inaccessible portions and uncertainty must be identified rather than silently ignored. The absence of a mandatory `order` field is intentional. A viewer can organize siblings for convenience without claiming a recovered chronology.

## Evidence and provenance

Item bodies preserve what the original material actually supports: definitions, notation, equations, assumptions, proof ideas, algorithms, implementation decisions, experiments, results, counterexamples and limitations. In projects, the difference between source claims, observed behavior and personally attributable contributions is material.

An Item includes a **Source references** section with source document/repository identifiers and precise pages, sections, archive-member paths, theorems, code paths or revisions whenever possible. Reference precision is limited by the source; unsupported citations must not be invented. The Source ID alone does not constitute an adequate reference.

`00_sources/source_profiles/` holds previous source inspections and technical analyses. These are useful orientation and cross-checking aids for extraction, but are not a substitute for the original lecture materials, project artifacts or repository history. The primary references recorded in production Items should point to original evidence.

## Validation and visualization

YAML and Markdown remain the authoritative Tree data. Structural checks, isolated example mode, command interfaces and read-only HTML exploration are documented in [`plumbing.md`](plumbing.md). These are operational concerns separate from the TreeNode and Item definitions above.
