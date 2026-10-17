# Statistical inference and generative modeling

## Central theme: choosing what a learned model is supposed to recover

The corpus now supports a coherent distinction between predicting a response, recovering latent structure, generating a distribution and answering an intervention question. These are not progressively more sophisticated versions of the same task. They require different assumptions, objectives and interpretations of success. Statistical Learning, Deep Generative Models, optimization material and scientific-ML implementation together explain how a statistical question becomes an objective, an algorithm and an evaluation protocol.

This theme develops that inferential perspective; [scientific computing and ML](scientific-computing-and-machine-learning.md) develops the complementary software-contract perspective. The [registry](../experiences.yaml) preserves accredited, project and supplementary origins. Connections below are mathematical synthesis, not claims that all methods were combined in personal project work.

## Prediction, estimation and representation are different targets

[Decision risk](../concepts/statistical-risk-model-selection.md) makes the target explicit: squared loss favors a conditional mean, absolute loss a conditional median, and zero–one loss the most probable class. This links classroom statistical decisions to the implemented pyLowOrder distinction between a training loss and physical-output MAE. It does not establish that focal/weighted MSE estimates the same population target as ordinary squared loss, nor that adding either improved pressure prediction.

[Regularized linear inference](../concepts/regularized-linear-inference.md) exposes another distinction: unbiased coefficient estimation, minimum prediction MSE, sparsity and stable inversion need not choose the same estimator. Ridge shrinks singular directions; Lasso's nonsmooth geometry produces thresholding; effective degrees of freedom and held-out selection address complexity. A Gaussian-prior interpretation explains a particular posterior, not an automatic guarantee of frequentist coverage. This complements [NGValidation interval interpretation](../concepts/prediction-interval-aggregation.md), where an interval operation must not be confused with a validated coverage property.

[PCA](../concepts/matrix-low-rank-pca.md), factor analysis and [ICA](../concepts/latent-factors-independent-components.md) make the representation question equally concrete. Orthogonal low-rank reconstruction, covariance-plus-noise explanation and independent-source identification have different objectives and identifiability conditions. Functional Analysis's [projection geometry](../concepts/hilbert-projection.md) provides a common language for a chosen approximation space, without turning ICA or nonlinear representation learning into orthogonal projection. The theoretical value is the ability to ask which structure is retained and which ambiguity remains.

## Latent inference connects statistical models with numerical algorithms

[Mixture EM](../concepts/mixtures-latent-inference.md) links hidden assignments to an iterative optimization procedure: posterior responsibilities inform model updates. The same construction can be viewed through [majorization/block methods](../concepts/proximal-block-optimization.md). These perspectives complement one another—one explains the hidden-variable model, the other explains why a surrogate/update can improve an objective—without giving a nonconvex likelihood a global optimum guarantee.

[Variational inference](../concepts/variational-generative-inference.md) extends this reasoning when exact posterior inference is unavailable. The ELBO plus posterior KL equals log marginal likelihood under the stated support/integrability conditions. A restricted mean-field family trades tractability for dependence information; an amortized VAE encoder shares inference parameters across observations. Reparameterization makes a sampled latent variable differentiable with respect to variational parameters, whereas a deterministic autoencoder has a different computational graph.

These connections support explaining what an approximation sacrifices, not merely naming a model family. They also separate inference approximation, finite Monte Carlo error, numerical optimization error and held-out predictive error. Educational derivations establish this knowledge even though the advertised generative programming repositories are absent.

## Generating a distribution changes the computational bargain

[Invertible flows](../concepts/invertible-generative-flows.md) pay for exact density transformation through invertibility and Jacobian structure. VAEs instead optimize a tractable lower bound for a latent model. [Adversarial learning](../concepts/minimax-adversarial-learning.md) compares implicit sample distributions through a discriminator or discrepancy; an optimal-discriminator divergence identity does not guarantee alternating gradient updates solve the game. FOML's monotone saddle analysis clarifies why convex–concave gap rates cannot be assigned to a general GAN.

[Diffusion and probability flows](../concepts/diffusion-score-probability-flows.md) introduce another bridge: noisy-data regression learns a direction used by a sampler. Langevin/Fokker–Planck connects sample dynamics to density evolution; probability-space entropy geometry supplies conditional continuous-time results. Conditional flow matching instead regresses a time-dependent velocity without an ODE solve during training, while generation still integrates the field. “Flow,” “gradient” and “sampling” therefore do not denote one interchangeable algorithm.

This theoretical breadth is relevant to selecting and explaining generative methods, including likelihood cost, latent interpretability, sampling cost and objective mismatch. It is not evidence of personally building a VAE, GAN, diffusion model or foundation-model training system.

## Dependence, topology and causality must remain separate

[Causal graphical models](../concepts/causal-graphical-models.md) distinguish observation, intervention and counterfactual reasoning through structural assumptions. A probabilistic DAG encodes conditional dependence; a pyLowOrder [mesh graph](../concepts/geometry-conditioned-message-passing.md) encodes spatial locality and geometric orientation. A message-passing edge is not a causal arrow. This distinction matters when discussing an aerodynamic predictor: conditioning on Mach/AoA and predicting pressure does not establish a causal-identification experiment.

Likewise, supplementary data-curation material connects model quality to the distribution and selection of training examples. Deduplication, learned quality filters and reproducible sampling can change the training population; none alone establishes representativeness, intervention validity or out-of-domain reliability.

## Conditioning and uncertainty connect language, perception and assurance

[Language models](../concepts/neural-sequence-language-models.md) and [hidden-state/structured inference](../concepts/structured-sequence-parsing.md) make the inferred object concrete: next-token probability, a summed likelihood, best tag path and compatible parse tree are different outputs. Lexical associations, [logical extraction](../concepts/semantic-knowledge-extraction.md) and [entity/discourse coherence](../concepts/entity-discourse-coherence.md) also have distinct truth and identity requirements. A fluent or coherent answer is not automatically an entailed fact.

[Neural sensory inference](../concepts/information-coding-sensory-inference.md) complements statistical model inversion through environmental priors and uncertain observations. Mutual information measures dependence under a response code; it does not identify a causal mechanism. The same distinction constrains NGValidation's permutation reliance measure.

Completed [residual diagnostics](../concepts/residual-statistical-diagnostics.md) and [calibration](../concepts/prediction-interval-aggregation.md) supply an engineering application: excellent aggregate R² can coexist with dangerous signed tails and conditional heteroscedasticity. Bootstrap uncertainty in a quantile differs from prediction coverage; confidence endpoints around nominal 95% do not prove exact conditional coverage or validate a full intersection. This deepens the existing model-discrimination and validation reasoning rather than creating a generic uncertainty skill.

## Capabilities that emerge from the combination

The represented theoretical knowledge supports formulating statistical targets, comparing estimators, recognizing identifiability constraints, and explaining how an objective differs from the algorithm used to optimize it. This is substantive analytical preparation, not merely context for programming.

The personally documented counterpart is narrower and concrete: geometry-aware pressure learning, target/seed alignment, loss/scaler/metric implementation, typed experiments and numerical safeguards. The [scientific-ML competency](../competencies/scientific-ml-software.md) and [validation-workflow competency](../competencies/validation-data-workflows.md) connect those actions to transferable implementation and experimental-design reasoning. Statistical education strengthens the interpretation of that work without retroactively asserting that every studied method was implemented.

The resulting technical pattern combines mathematical model discrimination with practical scientific-data and learning interfaces. Potential transfers include surrogate-model evaluation, statistical ML tooling and generative-method selection; deployments or experiments in those additional settings are not claimed. Exact missing theorem conditions and unprovided programming work remain explicit in the linked concepts.

## Evidence routes

Additional exact source routes are [NLP](../evidence/in2361.yaml), [neuroscience](../evidence/ei7646.yaml), [Cognitive Systems](../evidence/additional-cognitive-systems.yaml) and [NGValidation](../evidence/scientific_paper.yaml). Core taught content is in [MA4802 claims](../evidence/ma4802.yaml), [CIT4230003 claims](../evidence/cit4230003.yaml) and [FOML claims](../evidence/additional-foml.yaml). [Supplementary ML claims](../evidence/tum-machine-learning-optimization.yaml) enrich learning theory, kernels, optimization and data curation without accredited-completion or personal-implementation attribution. [pyLowOrder claims](../evidence/ma8102.yaml) distinguish the user's code from the DLR paper's external results. Detailed source locations and limitations are reused there rather than repeated throughout this synthesis.
