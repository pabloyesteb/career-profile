# Functional Analysis (MA3001)

## Module metadata

| Field | Value |
|---|---|
| Official title | Functional Analysis / Funktionalanalysis |
| Module code | MA3001 |
| ECTS | 9 |
| Grade | 4.0 |
| Teaching term | Winter semester 2024/25 |
| Profile status | complete_validated |

## Evidence base and material structure

The exact-matched course archive contains 33 PDFs totaling approximately 189 pages: a 94-page comprehensive script, a 10-page current-course supplement on distributions and Sobolev spaces, 14 problem sheets (27 pages), 14 full solution sheets (46 pages), an 8-page tutorial introduction, and a mock exam with solutions (4 pages). The main script is an older TUM script labeled WS 2017/18 but spans the archived WS 2024/25 syllabus; the current exercise sequence, supplement, and mock exam were used to validate its relevance.

The backbone sources are `Materials/Lecture notes.pdf` for the thirteen-chapter theory sequence and `Materials/Distributions.pdf` for the current supplement. All problem sheets and the mock exam were checked for additional emphases and applications.

## Technical content

### Normed, Banach, and operator spaces

*Evidence: `Materials/Lecture notes.pdf`, Chapter 1, pp. 2–19; `Problem Sheet 1.pdf`–`Problem Sheet 4.pdf`.*

- **Function and sequence spaces:** normed spaces, completeness, Banach spaces, closed subspaces, product spaces, and the standard spaces `C(D)`, `L^p`, `ℓ^p`, `ℓ^∞`, `c`, and `c_0`; density of finitely supported sequences and separability/non-separability results.
- **Linear operators:** continuity and boundedness of linear maps, operator norms, composition, isomorphisms, dual spaces, seminorms, quotient spaces, and quotient norms.
- **Extension from dense subspaces:** unique continuous extension of a bounded linear operator from a dense subspace into a Banach space.
- **Series and operator equations:** convergence of series in Banach spaces and Neumann-series inversion; exercises apply the latter to a linear integral equation.

### Hilbert-space geometry

*Evidence: `Materials/Lecture notes.pdf`, Chapter 2, pp. 20–31; `Problem Sheet 4.pdf`–`Problem Sheet 5.pdf`.*

- Inner products, the Cauchy–Schwarz inequality, parallelogram identity, orthogonal complements, and orthogonal projection onto closed convex sets and closed subspaces.
- Riesz representation theorem for continuous linear functionals on Hilbert spaces.
- Orthonormal systems and bases, Bessel-type estimates, Fourier coefficients, completeness/Parseval characterizations, and the representation of separable infinite-dimensional Hilbert spaces by `ℓ²`.

### Fundamental principles of functional analysis

*Evidence: `Materials/Lecture notes.pdf`, Chapter 3, pp. 32–36; `Problem Sheet 5.pdf`.*

- Baire category theorem and nowhere-dense sets.
- Banach–Steinhaus (uniform boundedness) principle, including pointwise limits of bounded operators.
- Open mapping theorem, bounded inverse theorem, and closed graph theorem.
- Exercises explicitly test why completeness assumptions matter and contrast pointwise, strong-operator, and operator-norm convergence.

### Duality, extension, reflexivity, and separation

*Evidence: `Materials/Lecture notes.pdf`, Chapter 4, pp. 37–45; `Problem Sheet 6.pdf`–`Problem Sheet 8.pdf`.*

- Sublinear and Minkowski functionals and the Hahn–Banach extension theorem over real and complex scalar fields.
- Dual norm representation and separation of a point from a closed subspace.
- Canonical embedding into the bidual; reflexive spaces, including Hilbert spaces and `ℓ^p` for `1 < p < ∞`, with counterexamples such as `c_0` and `ℓ¹` explored in exercises.
- Separation theorems for a point and a closed convex set, for two convex sets, and strict separation under the stated hypotheses.

### Compactness and weak topologies

*Evidence: `Materials/Lecture notes.pdf`, Chapters 5–6, pp. 46–58; `Problem Sheet 7.pdf`–`Problem Sheet 9.pdf`.*

- Compactness and total boundedness through finite ε-nets.
- Arzelà–Ascoli theorem for subsets of spaces of continuous functions.
- Mollification and the Fréchet–Riesz–Kolmogorov compactness criterion in `L^p`.
- Weak and weak-star convergence, lower semicontinuity of the norm, boundedness of weakly convergent sequences, and weak sequential closedness of closed convex sets.
- Banach–Alaoglu theorem and weak/weak-star subsequence results in separable and reflexive settings; direct-method existence of minimizers on weakly compact convex sets and uniqueness under strict convexity.

### Distributions and Sobolev spaces

*Evidence: `Materials/Lecture notes.pdf`, Chapter 7, pp. 59–65; `Materials/Distributions.pdf`, pp. 1–10.*

- Test-function space `D(R^d)`, its convergence notion, mollifiers, translations, and convolution.
- Distributions as continuous linear functionals on test functions; regular versus singular distributions, including the Dirac distribution.
- Approximation of arbitrary distributions by smooth functions and distributional differentiation.
- Weak derivatives, their relationship to distributional derivatives, mollified approximation, and examples such as the derivative of `|x|`.
- Sobolev spaces `W^{m,p}` and `H^m`, completeness, reflexivity and separability, density of smooth functions, zero-trace closure spaces, and one-dimensional Hölder regularity.
- Rellich compact embedding as used later for compactness of PDE solution operators.

### Compact, adjoint, and Fredholm operators

*Evidence: `Materials/Lecture notes.pdf`, Chapters 8–11, pp. 66–80; `Problem Sheet 10.pdf`–`Problem Sheet 12.pdf`.*

- Compact linear operators, sequential characterization, compact integral operators, closure of the compact-operator class, and compactness of compositions.
- Banach-space adjoint operators and relationships among kernels, annihilators, and closures of ranges.
- Complements of closed subspaces, factorization through quotient spaces, finite-dimensional kernels/cokernels, and closed-range results.
- Fredholm operators and the Fredholm index; stability under compact perturbations and the Fredholm alternative for `I-S` with compact `S`.

### Spectrum and compact-operator decomposition

*Evidence: `Materials/Lecture notes.pdf`, Chapters 12–13, pp. 81–94; `Problem Sheet 12.pdf`–`Problem Sheet 14.pdf`.*

- Resolvent and spectrum of a bounded operator; point, continuous, and residual spectrum.
- Compactness and non-emptiness properties of the spectrum over complex Banach spaces, polynomial spectral mapping, and the spectral-radius formula.
- Spectral structure of compact operators: nonzero spectral values as eigenvalues, finite-dimensional eigenspaces, and possible accumulation only at zero.
- Hilbert adjoint, normal/self-adjoint/positive operators, orthogonality of eigenspaces, and spectral decomposition of compact normal operators.
- Singular-value decomposition of compact operators, finite-rank truncation, best rank-constrained approximation, and continuity bounds for singular values.

## Algorithms and numerical methods

- Neumann-series construction of inverses for `I-T` when `||T|| < 1`.
- Mollification as a regularization/approximation procedure in `L^p`, distribution, and Sobolev settings.
- Spectral and singular-value truncation of compact operators, with operator-norm errors controlled by the omitted eigenvalue or singular value.
- No programming language or software implementation is evidenced in the archive; the course treatment is analytical and proof-based.

## Applications and model problems

- Reformulation of an ODE initial-value problem as a fixed-point/operator equation on `C(I; R^n)`.
- Linear integral equations and compact Volterra-type integration operators.
- Weak formulations and Sobolev-space foundations for PDEs.
- Existence and uniqueness of best approximations/minimizers on convex sets.
- Spectral analysis and low-rank approximation of infinite-dimensional operators.

## Exercise and assessment evidence

- Sheets 1–3 reinforce completeness, closures, operator convergence, separability, duality, and series in `ℓ^p`.
- Sheets 4–8 add a Neumann-series integral equation, Hilbert projections, Banach–Steinhaus, Hahn–Banach extensions, reflexivity, convex separation, weak convergence, and dual quotient-space arguments.
- Sheets 9–11 cover ε-nets, compactness counterexamples, compact diagonal and integral operators, adjoints, and complemented subspaces.
- Sheets 12–14 cover Fredholm index calculations, multiplication/shift operators, point/continuous/residual spectra, approximate eigenvalues, and isometric isomorphisms.
- The mock exam independently samples duality, Fredholm operators, weak continuity, reflexivity, and compact integral operators; it introduced no major topic absent from the profile.

## Thematic categories

- Functional analysis
- Operator theory and spectral theory
- Sobolev spaces and PDE foundations
- Variational analysis
- Numerical mathematics foundations

## Coverage validation

| Source structure | Profile coverage | Result |
|---|---|---|
| Chapters 1–2: normed and Hilbert spaces | First two technical sections | Covered |
| Chapters 3–4: uniform boundedness, extension, reflexivity, separation | Fundamental principles; duality and separation | Covered |
| Chapters 5–7: compact subsets, weak convergence, Sobolev spaces | Compactness and weak topologies; distributions and Sobolev spaces | Covered |
| Chapters 8–11: compact, adjoint, complemented, Fredholm operators | Compact, adjoint, and Fredholm operators | Covered |
| Chapters 12–13: spectrum and compact normal operators | Spectrum and compact-operator decomposition | Covered |
| Current distributions supplement | Distributions and Sobolev spaces | Covered |
| Fourteen sheet/solution pairs and mock exam | Exercise and assessment audit | Covered; no additional major area found |

## Sources

- **Transcript metadata:** `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 2.
- **Archive:** `00_sources/tum/archives/Functional Anal 950763320 (W24_25)_20261012_1552.zip`.
- **Backbone:** archive member `Materials/Lecture notes.pdf`, pp. 1–94, Chapters 1–13.
- **Current supplement:** archive member `Materials/Distributions.pdf`, pp. 1–10.
- **Exercises:** archive members `Problem sheets/Problem Sheet 1.pdf` through `Problem Sheet 14.pdf` and corresponding `Solutions to problem sheets/` files.
- **Assessment cross-check:** archive members `Mock Exam/Mock Exam.pdf` and `Mock Exam/Solutions to Mock Exam.pdf`.
