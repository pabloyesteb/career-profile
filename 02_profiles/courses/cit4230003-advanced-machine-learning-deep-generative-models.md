# Advanced Machine Learning: Deep Generative Models (CIT4230003)

## Module metadata

| Field | Value |
|---|---|
| Official title | Advanced Machine Learning: Deep Generative Models |
| Module code | CIT4230003 |
| ECTS | 3 |
| Grade | 4.0 |
| Teaching term | Summer semester 2025 |
| Profile status | complete_validated |

## Evidence base and material structure

The transcript entry has an exact title match to the archive `Advanced Machin 950803071 (S25)_20261012_1600.zip`. The archive contains 23 PDFs totaling 312 physical pages, one introductory F4V recording, and one export index. Eight lecture decks (224 pages) form a complete sequence: introduction, normalizing flows, variational inference, variational autoencoders, generative adversarial networks, denoising diffusion, conditional flow matching, and summary. Four numbered exercise units have solutions (22 unique pages); the variational-inference sheet appears twice under different filenames with identical bytes. Three past examinations and their solutions provide a further 64 pages of assessment evidence.

The complete slide sequence is the syllabus backbone. All decks contain selectable text, but spatial extraction sometimes scrambles equations, subscripts, diagrams, and pseudocode; representative mathematical and visual slides were therefore checked from rendered pages. Every exercise and solution was inspected, and all three examination/solution pairs were used as a coverage check. The introductory recording was identified but not transcribed; the corresponding 24-page introduction deck supports the claims retained here, and no recording-only content is asserted. The archive advertises voluntary programming tasks on normalizing flows, VAEs, and denoising diffusion, but does not contain their task statements, repositories, submissions, or code.

## Technical content

### Generative-model formulation and design criteria

*Evidence: `Introduction  Normalizing Flows/Lecture Slides - Introduction.pdf`, pp. 3–12; `Conditional Flow Matching  Summary/Lecture slides Summary.pdf`, pp. 2–7.*

- Deterministic and statistical generative models, with a statistical model characterized by a model family, parameter-learning procedure, and resulting distribution over data.
- Core desiderata: efficient generation of new samples, efficient likelihood evaluation, latent representations, and sufficiently expressive distributions for continuous or discrete high-dimensional data.
- Limits of simple parametric families and finite mixtures for complex real-world distributions; deep neural transformations as the common device for flexible generative modeling.
- Comparative structure of normalizing flows, VAEs, GANs, diffusion models, and conditional flow matching in terms of latent/noise inputs, generation mechanisms, likelihood availability, and training objectives.

### Normalizing flows

*Evidence: `Introduction  Normalizing Flows/Lecture Slides - Normalizing Flows.pdf`, pp. 3–33; `Introduction  Normalizing Flows/Exercise Sheet Normalizing Flows Solution.pdf`, pp. 1–4.*

- Multivariate change-of-variables formula for an invertible differentiable map `x=f(z)`: the transformed density combines the base density at `f^{-1}(x)` with the absolute inverse-Jacobian determinant. The determinant represents local volume change.
- Sufficient validity conditions: equal input/output dimensions, invertibility, and continuous differentiability of the map and inverse; strict monotonicity in one dimension and nonzero determinant for linear maps.
- Composition of multiple transformations and conversion of products of Jacobian determinants into sums of log-determinants for log-likelihood optimization. The slides note universality results for some flow families.
- Forward versus reverse parameterization: forward maps make sampling direct, while analytically available inverse maps make arbitrary-point density evaluation and maximum-likelihood estimation direct. The course compares planar/radial flows, RealNVP, inverse and masked autoregressive flows (IAF/MAF), splines, and Glow as representative architectures rather than deriving all of them.
- Computational structure of Jacobians: diagonal and triangular designs permit determinant evaluation from diagonal entries, whereas unrestricted dense Jacobians are expensive; LU factorization is presented as an alternative for full Jacobians.
- Exercises establish invertibility for nonlinear and affine maps, apply support constraints under change of variables, exploit a triangular inverse Jacobian, and derive sampling and density evaluation for a sum-of-sigmoids transformation. Exams additionally test compositional expressiveness and the restriction imposed by volume-preserving (`|det J|=1`) transformations.

### Latent-variable models and variational inference

*Evidence: `Variational Inference/Variational Inference Slides.pdf`, pp. 3–41; `Variational Autoencoders/Exercise Sheet Variational Inference Solution.pdf`, pp. 1–5.*

- Latent-variable factorization `p_theta(x,z)=p_theta(x|z)p_theta(z)` and marginal likelihood `p_theta(x)=integral p_theta(x,z) dz`; Gaussian mixtures illustrate latent assignments, inference of hidden variables, generation, and maximum-likelihood learning.
- Kullback--Leibler divergence `KL(q||p)`, including non-negativity and equality only when the distributions agree (almost everywhere). The course emphasizes that its direction matters.
- Evidence lower bound (ELBO)
  `L(theta,q)=E_q[log p_theta(x,z)-log q(z)]`, with the exact decomposition
  `log p_theta(x)=L(theta,q)+KL(q(z)||p_theta(z|x))`.
  This proves both the lower-bound property and tightness exactly when `q` equals the posterior.
- Expectation--maximization interpreted as coordinate ascent on the ELBO: the E-step sets or improves the approximate posterior for fixed model parameters, and the M-step improves model parameters for fixed `q`. Variational inference restricts `q` to a tractable parametric family when the exact posterior is unavailable.
- Joint optimization of model parameters and variational parameters by gradient ascent. Expectations and model-parameter gradients are estimated by Monte Carlo when analytic integration is unavailable.
- Pathwise/reparameterization gradients: express `z=T(epsilon,phi)` with parameter-free base noise, e.g. `epsilon~N(0,I)` and `z=R epsilon+mu` for covariance `RR^T`, so automatic differentiation can propagate through samples to variational parameters.
- Dataset-level mean-field factorization, its mini-batch-compatible ELBO decomposition, and its tradeoff: easier inference and fewer dependencies at the cost of inability to represent posterior correlations.
- Exercises derive an ELBO for an exponential-prior/Gaussian-likelihood model, demonstrate failure of tightness under variational-family mismatch, reparameterize exponential variables through scaling and inverse-CDF sampling, and prove componentwise KL decomposition for factorized distributions. Exams reinforce support mismatch, infinite KL, limits of mean-field approximations, graphical latent-variable models, and the difficulty of reparameterizing discrete latent variables.

### Variational autoencoders

*Evidence: `Variational Autoencoders/Lecture slides Variational Autoencoders.pdf`, pp. 3–21; `Generative Adversarial Networks/Exercise Sheet VAEs and GANs Solution.pdf`, pp. 1–2.*

- A VAE combines a prior `p(z)`, a neural decoder that parameterizes the conditional likelihood `p_theta(x|z)`, and an amortized neural encoder that maps each observation to parameters of `q_phi(z|x)`.
- Mean-field Gaussian approximate posteriors and the closed-form Gaussian KL term. The per-sample objective separates into expected reconstruction log-likelihood and regularization `-KL(q_phi(z|x)||p(z))`.
- Amortized inference replaces an independent variational parameter vector for every training instance with shared encoder parameters. Mini-batch training uses typically a one-sample Monte Carlo estimate and the reparameterization trick.
- The Gaussian VAE construction requires positive standard deviations/covariances; exercises enforce this by exponentiating unconstrained network outputs before sampling. They also distinguish architectures in which stochastic nodes require reparameterization from deterministic autoencoders.
- Generation after training samples `z` from the prior and uses only the decoder/conditional likelihood; the encoder is an inference-time component for observed data, not a requirement for unconditional generation.

### Likelihood-free learning and generative adversarial networks

*Evidence: `Generative Adversarial Networks/Lecture slides Generative Adversarial Networks.pdf`, pp. 3–19; `Generative Adversarial Networks/Exercise Sheet VAEs and GANs Solution.pdf`, p. 3; `General Announcement/Old Exams/Solutions/exam_2023_solution.pdf`, GAN problem.*

- Implicit generators transform a tractable noise variable into samples without requiring a tractable model density. This motivates likelihood-free comparison of empirical and generated distributions.
- Moment matching minimizes discrepancies in expectations of test statistics, estimated by Monte Carlo. Maximum mean discrepancy generalizes this idea using test functions in a reproducing-kernel Hilbert space, including kernels for images, strings, and graphs.
- Density-ratio learning for `r*(x)=p*(x)/p_theta(x)`: class-probability estimation, divergence minimization, and ratio matching are presented as related approaches. Bayes' rule connects the density ratio to a classifier separating real and generated samples.
- GAN formulation with generator `f_theta(z)` and discriminator `D_phi(x)`, binary cross-entropy, and the minimax objective. For balanced classes, the optimal discriminator is `D*(x)=p*(x)/(p*(x)+p_theta(x))`; the exercise solution analyzes matched distributions and support mismatch.
- The bilevel problem is approximated by alternating discriminator and generator updates. The slides explicitly note instability and that alternating updates need not solve the exact bilevel optimum.
- Past-exam derivations connect the optimal-discriminator objective to Jensen--Shannon divergence and show why an overly strong discriminator can produce vanishing generator gradients. A separate assessment problem augments first-moment matching with covariance matching and differentiates the resulting objective.

### Denoising diffusion and score-based models

*Evidence: `Denoising Diffusion/Lecture slides Denoising Diffusion.pdf`, pp. 3–46; `Denoising Diffusion/Exercise 4 Denoising Diffusion Solution.pdf`, pp. 1–4.*

- Discrete-time latent Markov formulation: a fixed Gaussian forward process progressively corrupts data, while a learned Gaussian reverse process reconstructs samples from a simple terminal prior.
- Forward-process reparameterization gives a closed-form noisy sample at arbitrary time, `z_n=sqrt(alpha_bar_n)x_0+sqrt(1-alpha_bar_n)epsilon`, avoiding simulation of every preceding transition.
- ELBO derivation for the reverse model. Bayes' rule makes the forward posterior conditioned on the clean datum Gaussian in closed form; the bound decomposes into a reconstruction term, reverse-transition KL terms, and a terminal-prior KL term.
- Neural parameterization of the reverse mean and variance, and the equivalent noise-prediction training objective. The exercise solution derives the ELBO decomposition, proves the arbitrary-time Gaussian marginal by induction, and shows the equivalence between conditional-score and noise prediction, `score=-epsilon/sigma_n`.
- Score `grad_x log p(x)` and Langevin sampling. The update is presented as an Euler discretization of a Langevin SDE; in the limiting regime of vanishing step size and infinite time, the solution distribution becomes stationary at the target density under the stated lecture setup.
- Explicit score matching replaces the unavailable data score with an equivalent objective involving the divergence/trace of the learned score. The course then motivates denoising score matching across increasing Gaussian noise levels to cover low-density regions.
- Annealed sampling traverses the noise schedule from an approximately Gaussian distribution toward the data distribution, using a score network conditioned on noise level and (in the simplified implementation) one Langevin-style reverse step per level.
- Image synthesis examples include DALL-E 2 and Imagen, illustrating text/image encoders, a diffusion prior over representations, conditional diffusion decoding, and classifier-free guidance; the course also notes the sampling cost, limited latent interpretability, and lack of exact cheap likelihood evaluation.

### Conditional flow matching and continuous normalizing flows

*Evidence: `Conditional Flow Matching  Summary/Lecture slides Conditional Flow Matching.pdf`, pp. 3–20.*

- Continuous-time probability paths `p_t`, flows generated by the ODE `dx_t/dt=u_t(x_t)`, and transport from a simple prior at `t=0` to the data distribution at `t=1`.
- Mixtures of conditional probability paths indexed by data samples. The chosen Gaussian optimal-transport conditional path has an affine interpolation and constant conditional velocity; the slides contrast these straight paths with diffusion paths that may overshoot.
- A time-conditioned neural vector field approximates the marginal velocity. Continuity in time, Lipschitz continuity in state, and differentiability are given as sufficient regularity for an invertible differentiable continuous flow.
- Instantaneous change of variables and the continuity equation yield the likelihood ODE `d log p_t(x_t)/dt=-tr(partial v_t/partial x_t)`. Numerical integration is possible, but likelihood training requires an ODE solve; adjoint sensitivities and Hutchinson trace estimation are mentioned as accelerations.
- Conditional flow-matching regression minimizes squared vector-field error on directly sampled interpolants. The key result is equality of the parameter gradients of conditional and marginal flow-matching objectives, permitting training without solving an ODE.
- Training samples time, clean data, and prior noise, constructs the interpolated state and target velocity, and takes a gradient step. Sampling numerically solves the learned ODE; forward Euler is shown, while arbitrary ODE solvers are allowed.
- Outlook topics include marginal optimal-transport couplings, reversible latent representations, likelihood cost, fewer neural-function evaluations than early diffusion samplers, and the unresolved extension of flows to discrete domains.

## Algorithms and numerical methods

- Maximum-likelihood training of reverse-parameterized normalizing flows using accumulated log-Jacobian determinants; direct forward sampling from a base distribution.
- Monte Carlo ELBO and gradient estimates, mean-field factorization, mini-batch stochastic gradients, and pathwise gradients via reparameterization.
- VAE training with amortized Gaussian inference, analytic Gaussian KL regularization, and sampled reconstruction terms.
- Moment matching, kernel MMD, density-ratio/class-probability estimation, and alternating minimax GAN optimization.
- DDPM-style Gaussian noising and reverse denoising; score/noise-prediction regression and annealed Langevin sampling over a noise schedule.
- Conditional flow-matching regression and numerical ODE sampling, including the forward-Euler discretization shown in the slides.

## Computational work and tools

- The slides use framework-neutral, Python-like pseudocode for stochastic sampling, neural-network calls, loss construction, gradient updates, and Euler integration. PyTorch and TensorFlow are named as examples of automatic-differentiation libraries in the variational-inference lecture, but no executable code in either framework is included.
- Three voluntary programming project tasks are advertised through Artemis: normalizing flows, variational autoencoders, and denoising diffusion. Students were instructed to clone a template repository and push solutions, but the archive contains none of those repositories or task specifications. Consequently, no implementation language, library, dataset, or completed project can be established from the available evidence.

## Applications and model problems

- High-dimensional image generation and synthetic faces; text-conditioned image synthesis through diffusion systems.
- Conditional generation, missing-data imputation, translation tasks such as text-to-speech, and controllable generation.
- Nonstandard structured data including graphs, sequences, waveforms, molecules, images, and strings.
- Gaussian mixtures and low-dimensional transformed densities as analytical examples for latent-variable inference, density evaluation, and sampling.

## Exercise, project, and assessment evidence

- Exercise 1 adds hands-on density transformation: invertibility, affine determinants, triangular Jacobians, support, and sigmoid-based flows.
- Exercise 2 deepens variational inference through an explicit nonconjugate ELBO, variational-family mismatch, exponential reparameterization, inverse-CDF sampling, and factorized KL proofs. Its two problem-sheet filenames are exact duplicate content.
- Exercise 3 tests computational-graph placement of reparameterization, valid covariance parameterization, and the optimal GAN discriminator under different support relationships.
- Exercise 4 supplies full derivations behind diffusion ELBO simplification, arbitrary-time forward marginals, and score/noise equivalence.
- The 2023, 2023 retake, and 2024 examinations cover normalizing flows, variational inference/VAEs, GANs, and diffusion. They add volume preservation, support-induced infinite KL, graphical models, Jensen--Shannon divergence, discriminator saturation, covariance matching, and diffusion-schedule failure cases. Conditional flow matching is absent because these exams predate the Summer 2025 lecture sequence; its coverage is supported by the dedicated current-term deck instead.

## Thematic categories

- Machine learning and artificial intelligence
- Probabilistic modeling and Bayesian inference
- Deep generative models
- Optimization and stochastic gradient methods
- Monte Carlo methods
- Stochastic differential equations and dynamical systems
- Optimal transport and continuous normalizing flows

## Coverage validation

| Source structure | Profile coverage | Result |
|---|---|---|
| Introduction and course overview | Generative-model formulation and design criteria | Covered |
| Normalizing flows deck | Normalizing flows | Covered; formulas and Jacobian layouts visually checked |
| Variational inference deck | Latent-variable models and variational inference | Covered; ELBO and reparameterization diagrams visually checked |
| VAE deck | Variational autoencoders | Covered; encoder/reparameterization/decoder diagram visually checked |
| GAN deck | Likelihood-free learning and GANs | Covered; minimax sign convention visually checked |
| Denoising diffusion deck | Denoising diffusion and score-based models | Covered; ELBO and score/noise formulas visually checked |
| Conditional flow matching deck | Conditional flow matching and continuous normalizing flows | Covered; likelihood ODE and CFM objective visually checked |
| Summary deck | Cross-model comparison | Covered; used to reconcile generation, likelihood, and objective distinctions |
| Four exercise/solution units | Exercise and assessment evidence | Covered; one exact duplicate sheet identified |
| Three past exams and solutions | Assessment cross-check | Covered; no missing pre-CFM major topic found |
| Advertised programming tasks | Computational work and tools | Limited: projects are named, but task files and code are absent |

## Sources

- **Transcript metadata:** `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 3.
- **Archive:** `00_sources/tum/archives/Advanced Machin 950803071 (S25)_20261012_1600.zip`.
- **Lecture backbone:** archive members `Introduction  Normalizing Flows/Lecture Slides - Introduction.pdf`, pp. 1–24; `Introduction  Normalizing Flows/Lecture Slides - Normalizing Flows.pdf`, pp. 1–35; `Variational Inference/Variational Inference Slides.pdf`, pp. 1–43; `Variational Autoencoders/Lecture slides Variational Autoencoders.pdf`, pp. 1–23; `Generative Adversarial Networks/Lecture slides Generative Adversarial Networks.pdf`, pp. 1–22; `Denoising Diffusion/Lecture slides Denoising Diffusion.pdf`, pp. 1–48; `Conditional Flow Matching  Summary/Lecture slides Conditional Flow Matching.pdf`, pp. 1–21; and `Conditional Flow Matching  Summary/Lecture slides Summary.pdf`, pp. 1–8.
- **Exercises:** archive members `Introduction  Normalizing Flows/Exercise Sheet Normalizing Flows.pdf`, `Introduction  Normalizing Flows/Exercise Sheet Normalizing Flows Solution.pdf`, `Variational Autoencoders/Exercise Sheet Variational Inference.pdf`, `Variational Autoencoders/Exercise Sheet Variational Inference Solution.pdf`, `Generative Adversarial Networks/Exercise 3 VAEs and GANs.pdf`, `Generative Adversarial Networks/Exercise Sheet VAEs and GANs Solution.pdf`, `Denoising Diffusion/Exercise 4 Denoising Diffusion.pdf`, and `Denoising Diffusion/Exercise 4 Denoising Diffusion Solution.pdf`.
- **Assessment cross-check:** archive members under `General Announcement/Old Exams/Problems/` and `General Announcement/Old Exams/Solutions/`: `exam_2023`, `retake_2023`, and `exam_2024` with their solutions.
