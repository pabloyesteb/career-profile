# Technical Cognitive Systems

## Module metadata and identity

| Field | Value |
|---|---|
| Course ID | additional-cognitive-systems |
| Official transcript title | Technical Cognitive Systems / Kognitive Systeme |
| Official module code | Not supplied in transcript |
| ECTS | 5 |
| Grade | 4.0 |
| Academic record | Additional-credit course; transcript PDF p. 6 |
| Profile status | complete_validated |

The user confirmed that `00_sources/tum/archives/CogSys SS2025_20261012_1559.zip`, internally **Cognitive Systems: Neural Networks and Applied AI (IN2222)**, corresponds to this transcript entry. IN2222 is teaching-source metadata, not an inferred official transcript code. The material mixes summer-2025 organization and LLM updates with older exercise/slide versions.

## Evidence base and material structure

The archive has **38 PDFs / 939 physical pages**, including an ordered lecture sequence, computational/mathematical exercises, hints, a guest lecture and two copies of an 18-page 2023 sample exam. Source references below are exact ZIP member names or explicitly named groups under their archive directories; page numbers mean physical PDF pages.

Complementary sources include two `.imscc` files that are ZIP packages, six Python solution scripts, regression/perceptron notebooks, a JSON-format LLM solution notebook, Brian2/encoding notebooks, a Mathematica notebook, an old-API DQN program stored as `.txt`, a three-slide PowerPoint supplement and a three-document RAG corpus. AppleDouble sidecars are packaging metadata, not independent assignments. `dataset_1.npy` is supplied for regression.

All chapter/exercise/guest sequences were mapped, typed tasks and computational sources inspected statically, and 28 representative mathematical/architectural/diagram pages rendered. Repeated reveal states and overlapping older/corrected decks were consolidated. No source code, generated model output, API call or notebook installation command was executed.

## Technical content

### Cognitive systems, representation, and modeling paradigms

*Evidence: [H1–H2], [D1–D2], [C1–C2]; especially D1 pp. 16–23 and C1 pp. 17–21.*

- Historical progression from autonomous/bioinspired robots and threshold networks to symbolic problem solving, **expert systems/production rules**, statistical learning and modern generative language models. MYCIN, OPS5/XCON and early autonomous robots are explanatory examples, not implemented course projects.
- Cognition is distinguished from intelligence and learning. Cognitive systems perceive, learn from experience, anticipate events, act toward goals and adapt; embodiment, situatedness, environment and other agents constrain what a system can do.
- **Cognitive-processing cycle:** perception, cognition and action, incorporating anticipation, assimilation and adaptation. Capabilities include goal-directed autonomy, cooperation/communication, interpreting other agents, sensing unexpected events, predicting action outcomes, learning and anomaly detection.
- **Marr's abstraction levels:** computational theory/objective; representation and algorithm; physical implementation. **Ultimate–proximate distinction:** why an evolved behavior exists versus how it operates. These are complementary explanatory frameworks.
- **Cognitivist/physical-symbol-system approaches:** symbols, expressions, recursive interpretation and heuristic search. The physical-symbol-system and heuristic-search statements are presented as hypotheses, not established mathematical theorems.
- **Emergent paradigms:** connectionist networks; enactive systems developing through embodied interaction (phylogeny/ontogeny); dynamical models described by time-dependent differential equations, attractors, bifurcations, stability, dissipation, nonequilibrium operation and collective variables. Hybrid systems combine paradigms.
- Turing-test and Chinese-room discussions expose limits of behavioral tests and symbol manipulation as evidence of understanding. Ethical/social issues and appearance-versus-capability are introductory conceptual coverage, not a legal analysis.

### Brain organization, experimental evidence, and neuron models

*Evidence: [C1], pp. 3–13; [B1–B3]; [BN], pp. 8–54; [SN], [NB1].*

- Brain anatomy: central/peripheral nervous systems, cerebrum/cortex, cortical layers/microcircuits, brainstem, autonomic systems, basal ganglia and hippocampus. Somatotopy, cortical homunculus, connectomes and comparative brain organization motivate functional decomposition without assuming brain size alone determines intelligence.
- Structural evidence through histology, **MRI** and **diffusion-tensor imaging**; functional recordings through **EEG**, **MEG**, **PET/SPECT** and blood-oxygen-dependent **fMRI**. Distinguish structural measurements from indirect activity measures and temporal resolution.
- Neuronal morphology, dendrites/axon/soma, ion gradients and membrane capacitance, resting potentials, **Nernst/Goldman-type equilibrium/permeability formulations**, action potentials, refractoriness, saltatory propagation, electrical/chemical synapses, excitatory/inhibitory effects and glial support.
- Model hierarchy: detailed/reduced compartments, single-compartment point neurons, cascade and black-box functional models. Biological plausibility, analytical tractability and computational cost guide selection.
- **McCulloch–Pitts threshold logic**, weighted analog neurons and nonlinear activations (step, sigmoid, tanh, ReLU, ELU and Gaussian). **Perceptron** and **ADALINE** illustrate distinct learning models; backpropagation is named historically, but a full backpropagation derivation is not supplied.
- **Hodgkin–Huxley conductance model:** capacitive membrane current plus sodium, potassium and leak currents; sodium conductance uses `m³h`, potassium `n⁴`; voltage-dependent gating equations produce a four-dimensional system. **Morris–Lecar** and **FitzHugh–Nagumo** are named two-dimensional reductions, not fully developed numerical implementations.
- **Leaky integrate-and-fire (LIF):** `C dv/dt=I(t)−(v−v_rest)/R`, membrane time constant `τ=RC`, threshold detection and reset. Exercise solutions derive exponential relaxation, threshold-crossing time and parameter effects on periodic firing under the stated reset/rest/threshold ordering; the problem deliberately omits refractoriness.
- **Adaptive exponential integrate-and-fire (AdEx):** membrane equation combines leak, exponential spike initiation and adaptation current; a second state governs adaptation. Phase-plane analysis illustrates richer firing patterns at lower cost than detailed conductance dynamics.
- **Izhikevich model** in the notebook: `dv/dt=0.04v²+5v+140−u+I`, `du/dt=a(bv−u)`, with threshold reset `v←c`, `u←u+d`. Brian2 tasks use dimensional/time scaling, Euler integration, state monitoring and optional phase-plane plotting; parameter sets demonstrate regular/fast spiking, chattering, bursting and thalamocortical patterns.
- Whole-brain modeling is treated as executable hypotheses. Visual cortex/thalamocortical simulations, **Spaun**, Human Brain Project and Blue Brain examples illustrate differing functional/biophysical abstraction levels, not personal model-building results.

### Neural coding, simulation, plasticity, and neuromorphic computation

*Evidence: [BN], pp. 50–54; [SN], pp. 4–29; [LP1–LP2]; [PS], Problems 1–3; [NB1–NB2].*

- **Rate codes**, **time-to-first-spike codes**, population activity and synchrony/correlation codes distinguish different information-bearing properties of spike trains. Population models aggregate activity rather than simulate every microscopic neuron.
- Brian2 simulation workflow: define differential equations/units, create `NeuronGroup` with threshold/reset, connect weighted `Synapses`, use `StateMonitor`, and simulate with exact linear or Euler integration. Provided solutions demonstrate dimensional consistency, excitatory voltage jumps and network connectivity.
- Encoding exercises map scalar values and grayscale pixel intensities to periodic spike trains using bounded frequency/period mappings, then visualize time-indexed spike images/GIFs. A slide task describes a **two-layer threshold/spiking integer adder**; it is labeled NEST and not silently equated with the supplied Brian2 notebook.
- Basic **Hebbian learning** strengthens correlated pre/postsynaptic activity; correlation versus mean-centered covariance rules, locality, unbounded growth, saturation and competition are distinguished.
- **Oja's rule** emerges by normalizing a discrete Hebbian update and using a first-order expansion. In rate/covariance form it links normalized weight dynamics to a principal component: `ẇ=Cw−(wᵀCw)w` after absorbing time-scale factors. The exercise compares the conceptual learning result with PCA; the separate referenced `Oja_rule.ipynb` is absent.
- **Bienenstock–Cooper–Munro (BCM)** theory uses a sliding activity-dependent threshold separating LTD from LTP. This is presented as an adaptive rate-based learning rule, not a reinforcement-learning algorithm.
- **STDP:** asymmetric dependence on pre/post timing, exponential learning windows and modulation by firing frequency/bursts/biophysical state. A direct all-pairs spike sum is replaced by exponentially decaying local pre/post traces, updated on spikes, with weight changes using the opposite neuron's trace. The solutions establish how trace accumulation reproduces contributions from preceding spike pairs without retaining all timestamps.
- Longer-term neuroplasticity, innate/epigenetic structure, **independent component analysis (ICA)** receptive-field examples and uncertainty-weighted sensory cue integration complement synaptic rules; these sections do not establish an implemented ICA or sensor-fusion estimator.
- **Neuromorphic hardware:** analog LIF circuits, memristive/RRAM devices, SpiNNaker and IBM TrueNorth; compare event-driven spiking communication with dense analog-valued network computation and its energy/latency motivations. Historical device specifications are not current product recommendations or independently verified performance claims.

### Statistical learning, generalization, and feature representations

*Evidence: [ML1–ML2], especially ML2 pp. 1–19, 20–26 and 29–57; [NP], [NR], [PY].*

- Supervised, unsupervised, semisupervised and reinforcement-learning paradigms; labeled/unlabeled datasets, feature vectors, hypothesis spaces and the training/inference workflow. Generative models represent/generate data distributions; discriminative models infer labels/conditional outputs.
- Model capacity, **underfitting/overfitting**, generalization, Occam's razor, held-out evaluation, cross-validation, additional data and regularization. Ensemble/boosted decision-tree regression is illustrative coverage, not a detailed AdaBoost derivation.
- **Perceptron learning:** update misclassified feature/bias vectors along the label-weighted input direction. **Perceptron convergence theorem:** finite termination for a finite linearly separable dataset; initialization/sample order affect the separator. XOR exposes nonseparability. The supplied notebook is an interactive teaching implementation, not a verified training experiment.
- Linear basis-function/polynomial regression minimizes sum-of-squares loss. Normal equations and the geometric projection interpretation connect fitting to linear algebra; the explicit inverse requires a nonsingular Gram matrix. Gaussian prediction noise makes least squares equivalent to maximum-likelihood estimation.
- The regression notebook builds a scikit-learn **PolynomialFeatures + Ridge** pipeline on `dataset_1.npy`, varying polynomial degree and regularization. This establishes an implemented regularized regression example, not a completed personal data-science project.
- Classification through linear scores, multiclass decision regions and one-hot labels; least-squares classification is sensitive to outliers. **Support vector machines** maximize geometric margin through a constrained minimum-norm formulation, support vectors and quadratic programming; no detailed soft-margin/kernel-dual theory is inferred from the short introduction.
- Python/NumPy exercises cover arrays, vectorized matrix operations versus explicit loops, timing, memoized versus recursive Fibonacci, functions, classes/inheritance and Matplotlib visualization.

### Deep feature learning, convolutional networks, and binding

*Evidence: [DL1], pp. 3–26; [DL2], pp. 1–39; [QA].*

- Feature engineering versus learned hierarchies: coordinate transformations, Fourier representations for speech/DTMF, color/shape/texture features, **SIFT**, and the transition from raw pixels to learned visual representations. Iris and face datasets illustrate feature-space geometry.
- Deep feedforward layers compose representations of increasing abstraction. Visual-cortex simple/complex cells, ventral/dorsal pathways and receptive-field organization motivate convolutional architectures without equating CNNs with full cortical models.
- **Discrete convolution**, spatial kernels and position-shared feature detection; **Sobel** edge filters and **Gabor** orientation/frequency filters. Pooling reduces spatial resolution and adds limited translation invariance; the PowerPoint supplement provides worked kernel and 2×2 max-pool examples.
- **Neocognitron**, **LeNet-5**, **AlexNet** and Inception appear as architecture milestones. Convolution/pooling hierarchies distinguish local connectivity, shared kernels and feature-map aggregation from full connectivity.
- **Convolution theorem/Fourier-domain multiplication** as an acceleration idea; transform overhead and representation are relevant, but the archive supplies no implemented FFT-CNN.
- Limits of static feedforward simplifications, adversarial patches, feature separation/binding and **capsule networks** with transformation-aware representations; EM routing is cited as an example, not derived or implemented.

### Reinforcement learning and neural Q approximation

*Evidence: [RL1–RL6]; [DQ], [DC].*

- Agent–environment interaction, classical/operant conditioning, reward hypothesis, states/actions, return/discount and policies. **Markov processes and MDPs** formalize transition/reward probabilities; CartPole is a concrete discrete-action continuous-state example.
- **State and action values** as expected returns; **Bellman expectation** and **Bellman optimality equations** express recursive evaluation and maximizing choices. **Generalized policy iteration** couples policy evaluation and improvement.
- Model-based **dynamic programming**: iterative policy evaluation, greedy policy improvement, policy iteration and value iteration; gridworld examples expose backup operations.
- Model-free **Monte Carlo prediction/control**, first-visit returns, exploring starts and ε-greedy alternatives; full sampled returns avoid bootstrapping but require episodic outcome information in the presented method.
- **TD(0)** prediction combines sampling with bootstrapping through error `r+γV(s′)−V(s)`. **SARSA** uses the next action from the behavior policy; **Q-learning** uses a greedy maximum target, separating on-policy from off-policy control. Cliff walking demonstrates policy/exploration consequences.
- **n-step bootstrapping** interpolates between one-step TD and Monte Carlo. Backup width/depth compares expected versus sampled transitions and rollout horizon; approximate value functions extend tabular methods to larger state spaces.
- CartPole **DQN-style** implementation: two 32-unit ReLU hidden layers and linear action-value outputs, replay buffer, minibatch sampled transitions, ε-greedy behavior, terminal reward shaping and MSE/Nadam fitting. It bootstraps with the same online network and has no separate target network; do not claim the full stabilized canonical DQN architecture.
- Robotic reaching/grasping and simulation-to-real transfer are lecture applications, not implemented personal deployments. The code uses an older Gym four-result `step`/single-result `reset` API and older Keras optimizer arguments; compatibility was not tested.

### Embodied neurorobotics and central pattern generators

*Evidence: [NRP], pp. 4–46; [CPG], pp. 2–8.*

- **Neurorobotics Platform** couples simulated brain, body and environment. Gazebo supplies rigid-body physics, OpenSim supports muscle simulation, ROS provides topics, NEST spiking networks, Blender robot design and Python transfer functions connect sensory variables to neural activity and neural outputs to actions.
- Experiment configuration, morphology/kinematics, neural visualization, state machines, virtual-coach scripting and automated parameter studies. Hardware-in-loop, neuromorphic backends, vision and simulation-to-real examples show integration options, not supplied executable end-to-end experiments.
- **Central pattern generators (CPGs)** generate rhythmic locomotor activity; half-center organization uses excitation/inhibition, descending drive and optional sensory feedback. The exercise diagram identifies excitatory/inhibitory populations and opposing motor outputs coupled to biomimetic muscles, with a salamander locomotion example.

### Cognitive architectures and ACT-R

*Evidence: [ACT], pp. 4–22 and 23–51.*

- Cognitive architectures specify coordinated perception, memory, action, learning and reasoning mechanisms. Symbolic, emergent and hybrid classifications; functional, behavioral and development requirements; compactness versus completeness and biological realism.
- **ACT-R** combines symbolic declarative chunks/production rules with subsymbolic activation/utility. Modules operate in parallel but expose limited buffers, while production selection serially coordinates their operations.
- Chunk types/slots, named buffers, pattern matching, buffer queries, modifications/clearing and module requests. Counting examples use goal and retrieval productions; the historical sample exam additionally asks for a declarative multiplication chunk.
- Declarative retrieval activation combines base-level recency/frequency, spreading activation, partial-match penalties and noise. The base-level display is `B_i=ln(Σ_j t_j^(−d))+β_i`; buffer-context associations contribute spreading activation.
- Procedural utility learning uses `U_i←U_i+α(R_i−U_i)`. **Production compilation** combines compatible sequential productions into new rules subject to buffer-specific constraints. The material is architectural/pseudocode coverage; no standalone ACT-R source program is packaged.

### Language models, evaluation, quantization, and retrieval augmentation

*Evidence: [H2], pp. 18–40; [LL], pp. 3–37; [LT], Tasks 1–5; [LN], static code; [RC].*

- Generative next-token modeling, learned word/context representations, transformer/self-attention overview, pretraining and dialogue fine-tuning. Historical model examples situate the topic; slide-era product specifications are not treated as current facts.
- Architectural comparisons: dense transformers, sparsely routed **mixture of experts**, and **state-space sequence models**; capacity, routing/load balancing, memory and sequence-length trade-offs are introductory comparisons, not implemented architecture research.
- **Quantization:** post-training, quantization-aware training, mixed precision and dynamic/static activation calibration. The notebook configures 4-bit **NF4**, double quantization and float16 computation through Transformers/BitsAndBytes for a Qwen model, comparing with unquantized inference.
- Direct, contextual, iterative, few-shot, role, contrastive, self-reflective and chain-of-thought prompting are compared as instructional strategies, without treating generated explanations as faithful internal reasoning.
- **HumanEval-style code benchmarking:** common wrapper for hosted/local models, code extraction, unit-test success fraction and a timeout. Tasks request a 50-item suite and accuracy/latency comparison, while supplied code instantiates only five items and reports single-generation task success. This is not a robust pass@k estimate or completed latency study.
- **RAG pipeline:** chunk local Markdown documents with overlap; embed via a multilingual MiniLM bi-encoder; retrieve by semantic similarity; rerank using a QNLI ELECTRA cross-encoder; insert selected passages into a generation prompt. Supplied code retrieves up to 32 candidates and combines six reranked passages. It does not implement the requested conversational query rewriting or explicit source citations, and actually invokes the hosted model for the final example.
- Hallucination approaches: self-reported confidence, scorer-based uncertainty, **self-consistency** through sampled-answer aggregation, **multiagent debate**, and **RECSIP** repeated semantic clustering/callback until agreement or stable disagreement. Agreement can still be wrong; score thresholds and additional inference cost remain limitations.
- Explainability taxonomy: local feature/attention/example/natural-language explanations, global probing/neuron/concept/mechanistic views, prompting-related explanations and evaluation of plausibility versus faithfulness. The lecture's taxonomy diagram was inspected visually; no implementation of every listed technique is claimed.
- Notebook tooling includes Hugging Face datasets/Transformers, PyTorch, BitsAndBytes, a hosted-model SDK, SentenceTransformers and LangChain text splitting. Its direct `exec` of model-generated programs is not a security sandbox and was never run in this analysis; API access, installation and generated outputs are not verified personal accomplishments.

### Guest lecture: neural code and dynamic-link representations

*Evidence: [G], pp. 18–40, 41–55 and 56–66; key diagrams and the Häussler equation checked visually.*

- Neural-code/binding problem and superposition ambiguity; representation by structured nets rather than isolated feature activations. **Cooperation of alternate pathways versus competition of converging pathways** motivates network self-organization.
- Retinotopic mapping development and the **Häussler weight equation**: growth/cooperative terms are opposed by row/column competition-normalization terms. The guest deck displays the dynamics and successive map states but does not give a complete convergence proof or computational assignment.
- **Dynamic projections/shifter circuits**, neural fields versus topological mappings, recognition through composing net fragments, **dynamic-link architecture** and face-recognition examples. Schema–instance matching preserves element types and relations (“homeomorphy” in the slides); coordinated fragments and loops are proposed for integrated perception.
- This is a guest theoretical perspective, including hypotheses about consciousness/global integration, not settled biological fact or a mathematical topology theorem.

## Tools, applications, and thematic categories

**Explicit tools:** Python, NumPy, Matplotlib, scikit-learn, Jupyter/Colab, Brian2, NEST, Mathematica notebook material, TensorFlow/Keras, Gym, PyTorch, Transformers/datasets, BitsAndBytes, SentenceTransformers, LangChain text splitting, ROS, Gazebo, OpenSim and Blender-based robot design. Distinguish implemented supplied code from platform/software examples; no authorship or successful execution is inferred.

**Applications:** classification/regression, visual/speech feature processing, neural simulation/coding, embodied robot control and locomotion, CartPole, cognitive memory/reasoning, code-generation evaluation and corpus-grounded question answering.

**Categories:** cognitive systems; machine learning; computational neuroscience; dynamical systems and robotics; reinforcement learning; natural language processing; data science; signal processing; scientific computing.

## Source register

All paths below are relative to the original archive. Cache manifest `.cache/additional-cognitive-systems/evidence_manifest.json` records every exact member, nested member, page count and extracted text location.

- **[H1]** `5. Mai - 11. Mai/Chapter 01-1 A Brief History of Cognitive Systems - Slides.pdf`; **[H2]** `12. Mai - 18. Mai/Chapter 01-2 A Brief History of Cognitive Systems - Slides.pdf`.
- **[D1–D2]** `12. Mai - 18. Mai/C02-1-Cognitive_Systems_Definition.pdf` and `C02-2-Cognitive_Systems_Definition_continued.pdf`.
- **[C1–C2]** `19. Mai - 25. Mai/C03-1-Basic_Concepts_in_Cognitive_Science.pdf` and `C03-2-Basic_Concepts_in_Cognitive_Science.pdf`.
- **[B1]** `26. Mai - 1. Juni/Chapter 04-1 Neurons and the Brain - Slides.pdf`; **[B2–B3]** `2. Juni - 8. Juni/Chapter 04-2 Neurons and the Brain - Slides.pdf` and `Chapter 04-3 Neurons and the Brain - Slides.pdf`.
- **[ML1]** `5. Mai - 11. Mai/E01-Machine_Learning_Part_1_corrected.pdf` (preferred to overlapping older Part-I deck); **[ML2]** `19. Mai - 25. Mai/E01-Machine_Learning_Part_2.pdf`; accompanying `E01 Machine Learning Part 2 hints.pdf`.
- **[PY]** `5. Mai - 11. Mai/Exercise 01-0 Python Cheatsheet - Slides.pdf`, `12. Mai - 18. Mai/E01-Python Cheatsheet QA solutions.pdf`, and `E1 solutions.imscc ::` six `.py` members.
- **[NP], [NR]** `19. Mai - 25. Mai/Perceptron.ipynb`, `Regression.ipynb` and `dataset_1.npy`.
- **[DL1–DL2]** `9. Juni - 15. Juni/C05-1-Deep_Neural_Networks.pdf` and `C05-2-Deep_Neural_Networks.pdf`; **[QA]** same folder, `QA session 4 - Deep Learning (additional slides).pptx` (3 slides).
- **[BN]** `16. Juni - 22. Juni/E04-Biological_Neural_Networks.pdf` (54 pp.).
- **[SN], [LP1–LP2], [PS]** `23. Juni - 29. Juni/ex05-SpikingNeuralNetworks.pdf`, `ex06-Part1_Learning_with_SNNs.pdf`, `ex06-Part2_Learning_with_SNNs.pdf` and `ex06-Problem_Sheets.pdf` (7 pp., tasks and solutions).
- **[NB1–NB2]** `23. Juni - 29. Juni/Ex05 - Problems.imscc :: ex05-problems/E05-Part_1-Introduction_to_Brian.ipynb` and `E05-Part_2_Encoding.ipynb`; same package includes `E05-Part_4-Izhikevich.nb`.
- **[RL1–RL6]** `30. Juni - 6. Juli/`: `C06-1-1-Reinforcement_Learning_Introduction_MDP.pdf`, `C06-1-2-Reinforcement_Learning_GPI.pdf`, `C06-1-3-Reinforcement_Learning_DP.pdf`, `C06-2-1-Reinforcement_Learning_MC.pdf`, `C06-2-2-Reinforcement_Learning_TD.pdf`, `C06-2-3-Reinforcement_Learning_Overview_DRL.pdf`.
- **[DQ], [DC]** `7. Juli - 13. Juli/E08-Reinforcement_Learning_DQN_CartPole1.pdf` and `E08-Reinforcement_Learning_DQN_CartPole2.txt`.
- **[NRP]** `2. Juni - 8. Juni/E02 The Neurorobotics Platform - Introduction.pdf`; **[CPG]** `7. Juli - 13. Juli/E07-Neurorobotics-Platform-Exercise-CPG.pdf`; **[ACT]** same folder, `E09-Cognitive_Architectures_and_ACT-R.pdf`.
- **[LL], [LT], [LN]** `14. Juli - 20. Juli/C07-Recent Developments - Large Language Models.pdf`, `E10-Recent Developement - Large Language Models.pdf` and `E10 - Notebook for Exercise on ___- Large Language Models (LLMs).json`.
- **[RC]** same folder, `Corpus for RAG/Bavaria.md`, `Munich.md`, `Roman_Empire.md`.
- **[G]** `21. Juli - 27. Juli/G01 slides.pdf`, 66 pp., “The Neural Code: Gateway to Understanding Brain and Mind.”
- **[X]** `General/Sample Exam.pdf` and `General/Literature  Software/data/Cognitive_Systems_Exam_2023_EndTerm.pdf` — duplicate 2023 assessment. Organization is in `28. April - 4. Mai/Chapter 00 Organization and Overview - Slides.pdf`.

## Coverage validation and limitations

Chapter 0 is administration; Chapters 1–3 map to history/foundations/paradigms, Chapter 4 to anatomy/neuron models, Chapter 5 to deep feature learning, all six Chapter 6 decks to RL, Chapter 7 to LLMs, and the final guest deck to dynamic-link/neural-code hypotheses. Every exercise family is represented, including late ACT-R and LLM material absent from the old exam. The two exam copies are not independent syllabus evidence.

Missing referenced `lif_neuron.ipynb` / `Oja_rule.ipynb` and complete NRP experiment packages limit implementation reconstruction; supplied Brian2 material partly overlaps the LIF topic but is not a substitute for those exact files. Older dates/labels (2021/2022/2023/2024) are retained as mixed teaching provenance. The DQN lacks a target network and uses obsolete interfaces. The LLM solution changes task scope (five rather than fifty tasks, single-sample success, no recorded latency study, no requested open-model conversational/citation implementation) and directly executes generated code. Perceptron plotting/sample-selection snippets have teaching-code limitations, so a reliable training run is not claimed. Some biology slides contain oversimplified quantitative statements; these were not adopted as independent scientific facts. No official web module description was necessary.
