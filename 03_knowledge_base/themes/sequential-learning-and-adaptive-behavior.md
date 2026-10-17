# Sequential learning and adaptive behavior

## Central theme: choosing a representation, feedback signal and update

The corpus now connects mathematical decision models, biological motor-learning abstractions and robotic perception/control. The important pattern is not that all systems “use feedback”: they represent different objects, observe different errors and adapt at different levels. A trajectory controller changes an input, TD changes a future-value estimate, policy optimization changes action probabilities, and an internal motor model predicts or inverts sensory consequences. Keeping those distinctions makes the combined knowledge more useful than an algorithm inventory.

## Mathematical foundations and levels of approximation

[Bellman evaluation](../concepts/bellman-policy-evaluation.md) gives exact policy/optimal-value structure under specified horizon and discount assumptions. [Sample-based learning](../concepts/temporal-difference-learning.md) asks how that structure is estimated from interaction: known-model expectation, completed Monte Carlo return and bootstrapped TD target have different information and bias/variance requirements. [Projected evaluation](../concepts/projected-policy-evaluation.md) adds feature space, weighting distribution and norm compatibility. Thus adding a neural model is not merely replacing a table with a faster representation; it changes the approximation and convergence question.

[Nonlinear dynamics](../concepts/dynamical-flows-bifurcations.md) contributes a different mathematical lens: equilibria, invariant manifolds, normal forms and qualitative parameter changes. [Invariant measures and mixing](../concepts/invariant-measures-chaos.md) address long-run behavior, helping identify what a stationary-distribution-weighted learning objective presumes. This is an editorial connection, not a proof that deterministic ergodic theory establishes off-policy TD convergence or that a robot experiment exhibited chaos. The supplementary profiles retain their incomplete theorem hypotheses and unspecified learning provenance.

## Error signals have distinct computational meanings

[CMAC/SOM adaptation](../concepts/local-adaptive-function-approximation.md) links sparse local coding, overlap, prototype neighborhoods and learning-region coverage. A target residual can alter active local weights, whereas success/failure memories and QARL change trial selection or quality weighting. Biological [forward/inverse models](../concepts/biological-motor-action-models.md) separately predict sensory consequences or seek commands for desired outcomes. These connect prediction and control without turning a cerebellar analogy into a general stability guarantee.

TD prediction error is a sampled recursive-value mismatch, not a direct physical tracking error. [Policy gradients and traces](../concepts/policy-gradient-credit-assignment.md) distribute credit through score functions, baselines, n-step targets and eligibility; fixed-weight trace equivalence must not become an arbitrary online guarantee. [Trust-region/PPO methods](../concepts/policy-optimization-geometry.md) regulate policy change through distributional geometry or clipped incentives, not guaranteed state-space safety. The thesis's progress-triggered reference recovery supplies a practical counterpoint: task-level stagnation may require a separate corrective loop even when the local model/controller is sophisticated. These methods were not historically combined into a learned thesis controller.

## Distributions, representations and autonomous decisions

[Distributional dopamine-value coding](../concepts/distributional-value-coding.md) makes future-return structure explicit: different asymmetric channels need not collapse into a mean. This is conceptually related to distributional additions in [deep value learning](../concepts/deep-value-learning.md), but neither is equivalent to a risk-sensitive objective or a calibrated prediction interval. The named presentation supports personal scientific interpretation, not implementation of Rainbow or biological recording.

Robotic decision-making additionally depends on what is observed. [SLAM/mapping](../concepts/probabilistic-slam-mapping.md) and [middleware/perception interfaces](../concepts/robot-perception-control-interfaces.md) distinguish latent state, map, measurement and actuator command. A state supplied to a Bellman model is not automatically Markov just because it is stored in an array. Geometric [search](../concepts/heuristic-adversarial-search.md), learned world models and model-free control offer different responses to information/model constraints, not one universally superior autonomy pipeline.

## Mechanisms, memory and symbolic coordination broaden adaptation

[Spiking/plasticity models](../concepts/spiking-neuron-plasticity.md) add membrane versus weight timescales, bounded/normalized Hebbian growth, Oja's principal-direction link and event-driven timing traces. A synaptic trace records spike history for a plasticity rule; an RL eligibility trace assigns value/policy credit. Their similar bookkeeping does not make their targets or biological interpretation identical.

[Population attractors and memory](../concepts/population-dynamics-neural-memory.md) concern persistent/replayed neural patterns and consolidation evidence. [ACT-R and binding](../concepts/cognitive-architectures-binding.md) instead coordinate chunks, buffers and production selection or propose dynamic structured links. Biological replay is not a DQN experience buffer; scalar ACT-R utility adaptation is not a complete tabular Q-learning system.

[Information-guided sensing](../concepts/information-coding-sensory-inference.md) links ambiguous sensory inverse problems and useful observations to adaptive action. CPG/brain–body platform examples add rhythmic circuit dynamics and transfer-function interfaces, while [dialogue-state systems](../concepts/retrieval-grounded-dialogue.md) organize interaction at a linguistic level. These are technically useful cross-level comparisons, not a single personally implemented cognitive robot.

## Practical activity and transferable capabilities

The evidence supports substantial theoretical knowledge of search, MDPs, TD/DQN, policy gradients and adaptive motor representations. Specific personal analytical activity is the distributional-value presentation; the CMAC/FFNN artifact supports collaborative comparison. Supplied CartPole, ROS and mobile-robot exercises provide computational context, not new personal implementation outcomes. The thesis separately supplies implemented control/recovery experience; those claims retain simulation/classification boundaries.

This combination supports **formulating sequential problems**, **discriminating learning targets and information assumptions**, **comparing local/global representations**, and **explaining the scope of a scientific model's evidence**. The demonstrated analytical scope is detailed in [computational-learning analysis](../competencies/analyze-computational-learning-models.md); implemented controller integration remains in the [control competency](../competencies/impedance-aware-control-design.md). Potential applications include autonomous decision systems and adaptive simulation/control, without implying a deployed learned policy or a professional financial outcome.

## Evidence and navigation

[Deep RL evidence](../evidence/mgt001299.yaml), [humanoid evidence](../evidence/ei7263.yaml), [ADPRL](../evidence/tum-approximate-dynamic-programming.yaml), [dynamics](../evidence/tum-dynamical-systems.yaml) and [mobile robotics](../evidence/tum-mobile-robotics.yaml), [neuroscience](../evidence/ei7646.yaml), [Cognitive Systems](../evidence/additional-cognitive-systems.yaml) and [NLP](../evidence/in2361.yaml) resolve to exact profile sections; [experiences](../experiences.yaml) retains accredited versus supplementary provenance. The companion mathematical-modeling and scientific-computing themes cover numerical formulation/software contracts; this theme adds learning, adaptation and long-run behavior rather than duplicating them.
