# Foundations of Data Analysis

## Module metadata

| Field | Value |
|---|---|
| Course ID | ma4800 |
| Official module | Foundations of Data Analysis — MA4800 |
| ECTS | 8 |
| Grade | 1.3 |
| Academic record | Degree module; transcript PDF p. 2 |
| Teaching material | Summer term 2024; Massimo Fornasier / Alessandro Scagliotti |
| Profile status | complete_validated |

## Evidence base and material structure

Source archive: `00_sources/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`, an exact module match. Internal course headers say “Foundations in Data Analysis”; the transcript's official English name above is retained.

The archive contains **42 PDFs / 155 physical pages**: a 79-page exercise/solution booklet, thirteen two-page weekly sheets numbered 0–12, thirteen one-page handwritten solution exports, thirteen one-page “All you … math” review exports, and a 12-page 2022 sample exam with 12-page sample solutions. There is also `peppers.png`, an extensionless JPEG erratum, and an HTML index. Most handwritten exports are extremely tall scroll pages: their physical page count seriously understates the volume. They have virtually no searchable mathematical text.

The six-chapter booklet [B] is the strongest structured backbone; current weekly sheets [E0–E12] establish progression and current task formulations. The mathematical-review sequence [N1–N13] was checked visually at representative top/middle/bottom positions in every document; the final review was tiled completely. Typed solutions provide complementary proofs; handwritten solutions were used selectively rather than interpreted as a second independent syllabus. There is **no separate comprehensive lecture script or slide sequence** in this archive, despite references to a script in exercises. Coverage here is comprehensive for the available structured syllabus, not a claim that every lecture-only result has been recovered.

## Technical content

### Linear algebra, Hilbert-space geometry, and projections

*Evidence: [B], Chapter 1, pp. 3–15; [E0–E1]; [N1–N5].*

- Vector spaces and linear maps, domain/range/kernel, rank–nullity, adjoints/transposes and inner-product identities. Symmetric-matrix orthogonal diagonalization, real eigenvalues and positive (semi)definiteness; trace as the sum of eigenvalues with multiplicity and cyclicity of trace.
- Norms and their geometry: Euclidean vector norm, Frobenius matrix norm, spectral/operator norm and their relationships; Cauchy–Schwarz and triangle inequalities. Spectral norm as a constrained maximization, including a Lagrange-multiplier calculation.
- Metric completeness and Cauchy sequences: contrast finite-dimensional convergence with continuous functions under an integral metric, where a sequence can approach a discontinuous limit outside the space. Hilbert-space completeness supports existence arguments.
- Convex sets, hyperplanes, finite convex combinations, intersections and balls; distinguish a convex closed ball from a generally nonconvex sphere. Minimum, infimum, minimizing sequence and attainment are separate notions.
- **Projection theorem:** for a nonempty closed convex subset `K` of a real Hilbert space, the nearest point exists uniquely. The proof uses a minimizing Cauchy sequence and the inner-product norm identity. Characterization: `p=P_K(v)` iff `p∈K` and `⟨z−p,v−p⟩≤0` for all `z∈K`.
- Projection onto the Euclidean unit ball is `x/max(1,||x||₂)`. Projection onto a finite-dimensional subspace with orthonormal basis is the sum of basis components; **Pythagoras–Fourier identity**, orthogonal decompositions and **Gram–Schmidt** connect geometry with computation. Closedness, convexity and the inner-product norm are meaningful hypotheses for existence/uniqueness.

### Singular value decomposition, low-rank approximation, and PCA

*Evidence: [B], Chapter 2, pp. 16–40; [E2–E6]; [N3–N7].*

- **Reduced and full SVD:** `A=Σ_i σ_i u_i v_iᵀ`, ordered nonnegative singular values, orthonormal singular vectors and rank-one terms. Right vectors derive from `AᵀA`, left vectors from `AAᵀ`, with eigenvalues `σ_i²`; full orthogonal extensions expose bases of the range, kernel and orthogonal complements.
- Geometric interpretation: a linear map sends the unit sphere to an ellipsoid; singular values give semi-axis lengths and left/right vectors specify output/input directions. Transposition exchanges left/right vectors; one can use the smaller Gram matrix for a rectangular example.
- Spectral, Frobenius and nuclear norms in terms of singular values. Singular vectors are not unique at repeated singular values, even though the represented matrix is fixed; sign changes and rotations within degenerate subspaces must not be confused with genuinely different operators.
- **Best rank-k approximation by truncated SVD** (the Eckart–Young result used by the exercises): retain leading singular terms and compare discarded error in spectral/Frobenius norms. Concrete rank-one calculations and the `peppers.png` grayscale exercise compare ranks 10, 25 and 100, image quality and matrix errors.
- **Power method:** compute leading singular directions through repeated application of `B=AᵀA`; spectral-gap-dependent convergence. When the largest singular value has multiplicity `d`, the normalized powers `B^ℓ/Σ_iσ_i^(2ℓ)` tend to `P_E/d`, not necessarily a single rank-one projector. The decay is controlled by powers `δ^(2ℓ)`, where `δ` is the largest strictly smaller singular-value ratio. The exercise booklet also asks for successive low-rank reconstruction and comparison with MATLAB `svd`.
- **SVD perturbation and stability:** small perturbations can rotate individual singular vectors by an order-one amount when leading values are nearly repeated. A companion example with a separated leading value contrasts that behavior; distinguish stability of singular values/subspaces from arbitrary vector choices.
- **Moore–Penrose pseudoinverse:** four Penrose conditions, full-column-rank normal-equation expression `(AᵀA)⁻¹Aᵀ`, and construction by reciprocal nonzero singular values. The handwritten review explains least-squares projection and the minimum-norm solution orthogonal to the kernel.
- **Principal component analysis:** SVD-based low-dimensional coordinates and visualization of the MATLAB `ovariancancer` dataset, with diagnosed/control groups plotted in the first three components. This is a teaching exercise, not a personally reported predictive model or medical finding.
- **Principal angles between subspaces:** cosines are singular values of the cross-Gram matrix of orthonormal bases; invariance under basis changes. The Frobenius norm of `P_W⊥P_V` equals the Euclidean norm of the sine-angle vector. Concrete projection matrices and two-dimensional subspaces illustrate the calculation.

### Alternating projections and convergence arguments

*Evidence: [B], Exercises 2.1.7–2.1.8 and solutions, pp. 18–19, 31–33; [E3–E4].*

- Composition of projections onto two lines gives an explicit repeated-product expression involving powers of their inner product, linking angle to convergence speed.
- **Alternating projections onto two nonempty closed convex sets in finite dimensions:** under nonempty intersection, alternate `y_k=P_D(x_k)`, `x_(k+1)=P_C(y_k)`. Projection inequalities show nonincreasing distance to any intersection point and summability/vanishing of successive projection gaps.
- Boundedness, an accumulation point, closedness and the distance inequalities yield convergence of both sequences to a common intersection point. This proof is not generalized here to empty intersections or arbitrary infinite-dimensional norm convergence.

### Probability, concentration, and high-dimensional geometry

*Evidence: [B], Chapter 3, pp. 41–56; [E7–E9]; [N8–N11].*

- Probability spaces and events, random variables, discrete/continuous laws and independence; expectations, variance and covariance under affine transforms and sums. Linear combinations of Gaussian vectors remain Gaussian, with projected variance given by a covariance quadratic form; independent components give a diagonal covariance.
- Densities of sums of independent variables via **convolution**; Gaussian moment-generating function and factorization of MGFs for independent sums. The review also derives exponential-distribution memorylessness.
- **Markov inequality**, higher-moment bounds and the exponential/Chernoff method: choose a positive exponential tilt to sharpen a tail bound. **Chebyshev**-type variance control and the law of large numbers are discussed through aggregate device-insurance returns; cumulant-generating functions and **Cramér-type exponential bounds** distinguish light-tail information from finite variance alone. The handwritten example is an elementary risk illustration, not an actuarial specialization or a universal large-deviation theorem without assumptions.
- **Mean-square versus probability convergence:** mean-square convergence implies convergence in probability; the exercise `P(X_n=n)=1/n` provides the converse counterexample.
- **Subgaussian random variables:** an MGF bounded by an exponential quadratic yields Gaussian-type tail decay; independence and the coefficient Euclidean norm control weighted sums. **Subexponential variables** have exponentially decaying tails; squares of standard Gaussians furnish the key example.
- **Bernstein inequality for subexponential sums** supports concentration of squared Gaussian norms. **Gaussian Annulus Theorem:** an isotropic Gaussian vector in dimension `n` lies in a thin shell around radius `√n`, with exponentially small deviation probability in the squared shell width over the stated range.
- High-dimensional ball volumes and surface areas through the Gamma function, asymptotic small volume, concentration near equatorial sections, and boundary concentration for uniformly sampled balls. The radial identity `P(||X||₂≤α)=α^d` and union bounds extend to multiple random points; near-orthogonality and concentration explain counterintuitive geometry.
- Proposed simulations include sampling sphere points by normalizing Gaussian vectors, histograms of pairwise distances, one-dimensional projections and random nearly orthogonal directions. The archive specifies experiments but does not include their programs or resulting measurements.

### Random projections and Johnson–Lindenstrauss embeddings

*Evidence: [B], Chapter 4, pp. 57–61; [E9]; [N10–N11].*

- A map formed from inner products with independent standard Gaussian vectors sends a fixed `v` to a Gaussian vector with covariance `||v||₂²I`. Its norm concentrates near `√k||v||₂`; normalizing by `1/√k` gives near-isometric scaling.
- **Random Projection Theorem:** Gaussian-annulus concentration gives a failure probability exponentially small in `kε²` for distortion of a fixed vector. Applying concentration to difference vectors and a union bound motivates the finite-set **Johnson–Lindenstrauss lemma**, preserving pairwise distances while reducing dimension.
- Distinguish a random embedding from an orthogonal projection and fixed-vector/finite-set guarantees from a uniform guarantee over every vector in the original ambient space. The historical sample exam explicitly tests this distinction using a random matrix and its own row vectors.
- Numerical distortion checks use entries `N(0,1/k)`; the booklet also proposes random signs `±1/√k`. The task compares relative squared-norm distortion over selected differences and several embedding dimensions rather than claiming an observed accuracy/runtime result.
- Storage reduction while retaining geometric structure motivates the method; uniform-ball sampling and union bounds additionally demonstrate simultaneous boundary concentration and near-orthogonality of many points.

### Convex analysis, conjugacy, sparse formulations, and duality

*Evidence: [B], Chapter 5, pp. 62–76; [E10–E12]; [N11–N12].*

- Convex functions and convex epigraphs; twice continuously differentiable convexity characterized by a positive-semidefinite Hessian on an open convex domain. Pointwise suprema preserve convexity; the maximum eigenvalue of a symmetric matrix is convex by its variational representation.
- Minkowski sums and convexity; **separating hyperplane** construction for disjoint closed/compact convex sets using nearest-point geometry.
- **Lower semicontinuity:** closed epigraph, stability under pointwise suprema, and lower semicontinuity of convex conjugates as suprema of continuous affine functions. Handwritten reviews connect sequential liminf, open/closed sets and indicator functions.
- **Legendre–Fenchel conjugate** `f*(y)=sup_x(⟨y,x⟩−f(x))`; computations for exponentials and power-type functions, inverse-derivative characterization where appropriate, and transformation rules under invertible affine changes plus linear terms. The formula involves the inverse function of the derivative, not its reciprocal.
- **Subgradient optimality** handles the nonsmooth absolute value, whose subdifferential at zero is `[-1,1]`. Minimizing a squared scalar discrepancy plus `λ|x|` gives **soft thresholding**, extended coordinatewise.
- Euclidean projection onto the **ℓ₁ ball** reduces to soft thresholding with a nonnegative multiplier. For an exterior point the multiplier enforces unit ℓ₁ norm; an already feasible point is unchanged (the sheet's unconditional boundary-equality wording omits this case). The thresholded ℓ₁ norm is continuous piecewise linear and decreasing in the threshold, which supports scalar parameter selection and plotting.
- **Basis pursuit:** minimize `||x||₁` subject to `Ax=y`. The Lagrangian yields dual objective `−⟨ξ,y⟩` with constraint `||Aᵀξ||∞≤1` under the source's multiplier sign convention; outside that domain the dual function is `−∞`. Derivation uses ℓ₁/ℓ∞ dual norm bounds and an unbounded coordinate direction. Linear-programming duality is an additional historical assessment example, not evidence of a separate implemented LP solver.

### Gradient methods and differential estimates

*Evidence: [B], Chapter 6, pp. 77–79; [E12]; [N11–N13]; [X], Problems 3–4 as cross-check.*

- Gradient descent `x_(k+1)=x_k−η∇f(x_k)`, choice of learning rate and convergence for an explicitly studied piecewise quadratic/radial objective. Inside the invariant unit ball the iteration is affine, `(1−2η)x_k+ηa`, tending to `a/2` for the stated initial points and compatible steps; at `η=1/4` the contraction factor is one half.
- A separate booklet task uses a **normalized gradient direction** with geometrically decreasing step lengths. It compares gradient-norm tolerance, objective-change tolerance and an iteration cap. These are distinct stopping criteria, not general convergence guarantees for arbitrary schedules.
- Distinguish Lipschitz continuity of `f` from Lipschitz continuity of `∇f`. For differentiable functions on a convex domain, bounded gradient controls the former; bounded Hessian operator norm controls the latter. Frobenius bounds provide computable, potentially conservative upper bounds.
- Handwritten reviews derive first/second derivatives along curves; along a gradient flow, the objective derivative is the negative squared gradient norm. Quadratic differentiation gives `∇(xᵀAx)=(A+Aᵀ)x`, reducing to `2Ax` only for symmetric `A`.
- Lipschitz estimation by triangle inequalities, bounded products and componentwise estimates; sharpness is not required for every bound. No Newton/quasi-Newton, accelerated, stochastic or proximal-gradient algorithm is inferred solely from the booklet chapter's broad title.

## Computational tools and applications

**MATLAB** is explicitly proposed, including `svd`, loading `ovariancancer`, plotting and numerical distortion tests. **Python** is an explicitly permitted alternative for several matrix/image tasks. No library beyond these named tools, no executable solution file and no personal code authorship is evidenced. Applications include low-rank image compression, cancer-data PCA visualization, least-squares systems, high-dimensional storage/embedding, elementary warranty/insurance risk and sparse linear recovery.

## Thematic categories

Data analysis; numerical linear algebra; dimensionality reduction; probability and concentration; high-dimensional geometry; convex analysis; optimization; sparse estimation; mathematical modeling.

## Coverage validation

| Backbone block | Current weekly evidence | Profile coverage |
|---|---|---|
| 1. Linear algebra | Sheets 0–1; reviews 1–2 | Geometry, completeness, projection theorem |
| 2. SVD | Sheets 2–6; reviews 3–7 | SVD, approximation, power method, PCA, perturbation, pseudoinverse, angles, alternating projections |
| 3. Probability | Sheets 7–8; reviews 8–11 | MGF/tails, convergence, Gaussian/subexponential concentration and geometry |
| 4. Dimensionality reduction | Sheet 9; reviews 10–11 | Random projections, JL, mass concentration |
| 5. Convex analysis | Sheets 10–12; reviews 11–12 | Convexity, conjugacy, semicontinuity, thresholding, duality |
| 6. Numerical optimization | Sheet 12, booklet additional task; review 13 | Gradient methods, invariant-set example, Lipschitz estimates and stopping tests |

All thirteen weekly task sheets and all six booklet chapters were checked. Review documents were visually sampled throughout the complete weekly sequence, with expanded final-week inspection. No missing late source block was silently replaced by generic knowledge. Assessment topics corroborate the main structure; dates, absent computational files and inconsistent formulas remain explicit below.

## Sources and limitations

References denote members of the original ZIP; cache files are regenerable and not substitutes for original evidence. Page numbers are physical PDF pages.

- **[B]** `Introduction and general information/Booklet of Exercises FDA.pdf`, 79 pp., dated 10 June 2024.
- **[X]** `Introduction and general information/Sample Exam (from SoSe 2022).pdf` and `Sample Solutions for the Sample Exam.pdf`, each 12 pp. Handwritten answer extraction is unreliable; the typed task and rendered mathematical pages were preferred.
- **[E0–E12]** Weekly sheets in calendar order: `15. April - 21. April/Exercise sheet 0.pdf`; `22. April - 28. April/Problem Set 1.pdf`; `29. April - 5. Mai/Problem Set 2.pdf`; `6. Mai - 12. Mai/Problem Set 3.pdf`; `13. Mai - 19. Mai/Problem Set 4.pdf`; `20. Mai - 26. Mai/Problem Set 5.pdf`; `27. Mai - 2. Juni/Problem Set 6.pdf`; `3. Juni - 9. Juni/Problem Set 7.pdf`; `10. Juni - 16. Juni/Problem Set 8.pdf`; `17. Juni - 23. Juni/Exercise sheet 9.pdf`; `24. Juni - 30. Juni/Exercise sheet 10.pdf`; `1. Juli - 7. Juli/Exercise Sheet 11.pdf`; `8. Juli - 14. Juli/Exercise Sheet 12.pdf`.
- **[N1–N13]** Single-scroll-page review files in the same weekly folders, starting one week after E0: `All you ... math 1`, `Notes All you... math week 2`, `All you ... math 3`, `All you... math 4`, `All you... math 5`, `All you... math 6`, `All you ... math 7`, `All you... math 8`, `All you... math 9`, `All you... math 10`, `All you... math 11`, `All you ... math 12`, and `15. Juli - 21. Juli/All you... math 13`. These are PDFs despite having no extension. Many retain 2023 internal timestamps.
- **[R]** `20. Mai - 26. Mai/Erratum Exercise 4.1` — JPEG despite no extension; corrects the signed coefficient in the normalized-power proof and explains estimating its absolute value.
- **[I]** `6. Mai - 12. Mai/peppers.png` — supplied image for the approximation task.

**Evidence cautions:** no comprehensive lecture script, MATLAB solution programs, `countries_data.txt` or `Bird_Data` is packaged, although the booklet refers to them. `ovariancancer` is requested as MATLAB-provided data, not an included dataset. The older review notes and current sheets agree at topic level but do not establish that every older example was separately delivered in 2024. Booklet p. 53 contains several tail-bound typos (including a missing square and reversed event inequality); the profile uses the consistent exercise definitions and MGF derivation rather than copying those displays. Booklet p. 78 has a minus sign in the specialized `η=1/4` recurrence despite the preceding general recurrence and following limit using a plus sign; the consistent general recurrence is retained. No official external module description was required to identify the available course structure.
