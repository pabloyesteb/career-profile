# Introduction to Deep Reinforcement Learning (MGT001299)

## Module metadata

| Field | Value |
|---|---|
| Official title | Introduction to Deep Reinforcement Learning |
| Module code | MGT001299 |
| ECTS | 6 |
| Grade | 2.3 |
| Transcript section | Degree modules, p. 4 |
| Teaching term | Winter semester 2025/26 |
| Profile status | complete_validated |

## Evidence base and material structure

The exact transcript match is `00_sources/tum/archives/Introduction to 950839140 (W25_26)_20261012_1601.zip`. Its export index identifies Introduction to Deep Reinforcement Learning [MGT001299], and the introduction explicitly identifies Winter Term 2025/2026, Prof. Maximilian Schiffer, and TUM's Professorship for Business Analytics and Intelligent Systems. The course develops optimal sequential decision-making from search through Markov decision processes, learning from interaction, neural approximation, and advanced policy optimization.

The archive contains 43 regular outer members. Its 32 PDFs total 844 physical pages: nine lecture decks (589 pages), seven exercise sheets (18), seven solution decks (181), three coding instructions (16), an exam formula sheet (3), exam examples and solutions (25), and administrative material (11-page exam instructions/seating list plus a one-page guest-lecture invitation). Six `.imscc` files are ZIP packages containing templates and solutions for three coding assignments, not merely external links. Excluding macOS resource files, these packages contain 29 Python files (19 distinct byte contents), 18 CSV copies representing nine data filenames, seven Markdown documents, and five requirements files. Templates and solution packages intentionally repeat scaffolding and data.

The complete nine-deck lecture sequence is the backbone. All seven sheets, their solution structure, every coding assignment, the supplied implementations, formula sheet, and exam examples were checked for additional content. The 263-page search deck contains many progressive builds; repeated headings were grouped and final reveal states used for complete explanations. Text extraction with `pdftotext -layout` recovers headings and prose, but many equations and embedded exam questions disappear. Forty-five pages were rendered and inspected to recover key formulas, theorem conditions, algorithms, graphs, and assessment text. Page references below mean **one-based physical PDF pages**, which can differ from printed slide numbers.

Extracted PDFs/text, nested source packages, a PDF page-count manifest, and visual checkpoints are retained under `.cache/mgt001299/`. All code inspection was static; no archived code, environment simulation, training, dependency installation, or external tutorial was executed. Local material is sufficient for the profile without consulting external module descriptions.

## Technical content

### Rational agents, utilities, and search formulation

*Evidence: [L1], pp. 26–30; [L2], pp. 6–98; [E1], all problems, and its solution, pp. 7–17.*

- Algorithmic completeness versus optimality; heuristic solution methods; directed graphs, paths, cycles, rooted trees, state/action spaces, and successor functions as the representation of planning problems.
- Rational agents choose actions to maximize expected utility. Utilities encode preferences over outcomes; lotteries combine possible outcomes with probabilities. The lecture introduces orderability, transitivity, continuity, substitutability, and monotonicity as rationality axioms, with monetary-choice illustrations in the exercise solution.
- A search problem specifies a start state, available actions, successor transitions and costs, a goal test, and an action sequence/plan reaching a goal. Examples include travel routing, adjacent-swap book sorting, Pac-Man, and Breakout.
- State-space graphs contain one node per state, whereas an unfolded search tree can contain the same state along different paths. This representation distinction is separate from **tree search** versus **graph search**: graph-search algorithms keep a marked/closed list to avoid repeated state expansion.
- Frontier management, successor generation, goal testing, visited-state tracking, parent links, and path reconstruction establish the operational structure used again in the first coding exercise.
- Utility transformations require different treatment under certainty/adversarial choice and uncertainty. Order-preserving transformations preserve minimax decisions, but nonlinear transformations can change lottery rankings and expectimax choices because magnitudes, not just ordering, enter expectations. The late comparison corrects the overly broad introductory statement that a monotonic utility transformation always preserves choices.

### Uninformed, heuristic, adversarial, and stochastic search

*Evidence: [L2], pp. 99–261; [E1], §§2–5 and solution pp. 18–40; [C1S], `search/run_search_solution.py` and `search/util.py`.*

- **Depth-first search (DFS)** explores the deepest frontier node, implemented recursively or with a LIFO stack; **breadth-first search (BFS)** explores the shallowest frontier node with a FIFO queue. Exercises compare completeness and optimality on finite route graphs. BFS minimizes action count in the unit-cost setting; DFS need not find a shortest path.
- **Uniform-cost search (UCS)** orders the frontier by accumulated path cost `g(n)` using a priority queue, distinguishing least-cost paths from the shallowest BFS solution. The supplied implementation tests goals on removal from the priority queue, maintains a closed list, and replaces more expensive frontier paths with cheaper alternatives.
- **Greedy best-first search** selects the smallest estimated remaining cost `h(n)` and may commit to a poor goal/path. **A*** combines accumulated and estimated future costs, `f(n)=g(n)+h(n)`.
- **Admissibility** means that the estimated remaining cost does not exceed the true nearest-goal cost. The A* optimality proof is explicitly for tree search: an ancestor on an optimal path has `f(N)≤f(G_opt)<f(G_suboptimal)`, preventing a more expensive goal from being expanded first. Overestimating heuristics can defeat this guarantee. The sources do not develop a separate consistent-heuristic theorem for closed-list A*.
- Search contour diagrams contrast UCS's cost expansion with A*'s direction toward promising goals. Exercises use straight-line city distances as optimistic heuristics for road-route cost.
- **Minimax** backs up alternating maximum and minimum utilities in two-player zero-sum games, assuming rational adversarial play. The lecture relates exhaustive minimax to depth-first exploration and its exponential tree cost; depth-limited search replaces unexpanded positions with evaluation functions and loses exact-play guarantees.
- Non-zero-sum/multiplayer exercises propagate utility vectors and select each player's preferred component, distinguishing this from a scalar zero-sum objective. The match-breaking game provides a discrete game-tree model.
- **Expectimax** replaces adversarial minimum nodes with probability-weighted chance nodes, maximizing expected utility rather than worst-case performance. Applications include uncertain game outcomes and a racing strategy that trades lap speed against crash/repair costs; the latter is expressed as expected-cost minimization in the solution.
- Python teaching code supplies stack, queue, priority queue, closed-list, and graph/path classes for deterministic gridworld search. These are course-provided implementations, not attributed personal software contributions.

### Markov models and dynamic programming

*Evidence: [L3], pp. 4–49; [E2], §§1–6 and solution pp. 6–33; [F], pp. 2–3.*

- **Markov chains** encode current-state-dependent transition probabilities. The Markov property makes future evolution independent of earlier history conditional on the current state. Exercises model repeated level completion and a branching population whose next-generation count depends only on the current population.
- **Markov decision processes (MDPs)** add state-dependent actions, transition probabilities `P(s'|s,a)`, transition rewards `R(s,a,s')`, initial/terminal conditions, and a policy. Policies may be deterministic state-to-action maps or stochastic action distributions.
- Finite-horizon, terminating episodic, and continuing tasks are distinguished. Finite-horizon decisions can depend on time remaining; a wheel-of-fortune optimal-stopping exercise uses backward Bellman reasoning without discounting. A recycling robot and stochastic gridworlds illustrate continuing and terminating models.
- Discounted return sums rewards with powers of `γ`; for bounded rewards and `0≤γ<1`, a geometric-series bound controls infinite-horizon values. Finite horizons and absorbing terminal states are alternative mechanisms for making the objective well-defined. These conditions are not interchangeable with arbitrary undiscounted continuing tasks.
- State values `V^π` and action values `Q^π` evaluate a policy; optimal values use the best subsequent policy. **Bellman optimality equations** relate them by `Q*(s,a)=Σ_s' P(s'|s,a)[R(s,a,s')+γV*(s')]` and `V*(s)=max_a Q*(s,a)`.
- **Value iteration** repeatedly applies the Bellman optimality update and extracts a greedy policy by one-step lookahead. The lecture states convergence for the discounted infinite-horizon setting, gives a vanishing discounted-tail argument, and identifies Banach's fixed-point theorem as the alternative fixed-point justification. The proof's tail bound is proportional to `γ^(H+1)/(1−γ)` times the reward bound.
- **Policy iteration** alternates evaluation of a fixed policy with greedy improvement. Policy evaluation uses iterative Bellman updates or a linear equation system when the state space is small. The lecture gives `O(|S|²)` work per dense iterative policy-evaluation pass.
- The policy-iteration proof sketch uses improvement and the finite number of deterministic policies to explain termination at Bellman-optimal values in the finite setting. This assumes exact evaluation and appropriate treatment of ties; it is not a general guarantee for neural actor–critic methods or arbitrary undiscounted MDPs.
- Exercises compute distributions after prescribed stochastic moves, early value-iteration sweeps, policy extraction, and policy evaluation/improvement on a small transition graph. They distinguish known-model planning from later sample-based learning.

### Learning from interaction: model estimation, Monte Carlo, TD, and Q-learning

*Evidence: [L4], pp. 4–32; [E3], all four exercises and solution pp. 4–44; [C1S], reinforcement-learning source files.*

- In reinforcement learning, the reward and transition model are unknown and must be learned through action/outcome experience. **Model-based RL** estimates transition probabilities from normalized counts and rewards from observations, then solves the empirical MDP, for example by value iteration. Dyna is named as a classical example; no Dyna implementation or detailed planning loop is supplied.
- **Passive direct evaluation/Monte Carlo evaluation** follows a fixed policy, records discounted returns from state visits, and averages them. It requires completed returns, estimates states separately, and initially fails to exploit Bellman links between related states. Exercises construct both direct value estimates and an empirical MDP from the same episodes.
- **TD(0) policy evaluation** updates after each transition: `V(s)←V(s)+α[r+γV(s')−V(s)]`. The TD error compares the old value with a sampled reward plus a bootstrapped successor estimate; exponential moving averages and decreasing learning rates explain the update mechanism.
- Learning only `V` does not give model-free action selection when transition/reward functions are unknown. **Q-learning** instead learns action values and extracts greedy actions directly: `Q(s,a)←Q(s,a)+α[r+γ max_a' Q(s',a')−Q(s,a)]`.
- The maximization target distinguishes Q-learning's learned greedy policy from its exploratory behavior policy; it is an active, model-free, off-policy method. Exercises perform updates from given transition sequences and distinguish deterministic environment information from estimates acquired by interaction.
- **Exploration–exploitation** trade-offs: `ε`-greedy action selection, possible decay of exploration, and optimistic visit-count bonuses. The lecture's example exploration function is `f(q,n)=q+k/n` for visited state–action pairs, propagated into bootstrapped targets; treatment of the zero-count case is not specified. Regret is introduced as accumulated loss relative to optimal behavior, with references rather than a derived regret bound.
- The learning-rate exercise studies stochastic-approximation conditions `Σ_n α_n=∞`, `Σ_n α_n²<∞`, and positive bounded step sizes. Constant, harmonic, and overly fast-decaying schedules illustrate their role. The local convergence statements do not fully enumerate exploration/visitation and MDP assumptions; the profile does not treat the step-size conditions alone as a sufficient general Q-learning theorem.
- Coding 1 implements dictionary-based tabular Q-learning in a `4×3` gridworld with walls, terminal rewards, and stochastic perpendicular slips. Environment/agent separation, reward timing, action selection, hyperparameter configuration, and greedy policy extraction are explicit computational content.

### Neural approximation, supervised learning, and optimization

*Evidence: [L5], pp. 3–45; [E4], all exercises and solution pp. 4–14; [C1], pp. 9–10; [C1S], `deep_neural_network/`.*

- Tabular state/action storage becomes infeasible in large or continuous spaces. Handcrafted feature vectors support linear value and Q-functions, while multilayer networks provide nonlinear generalization. The **universal approximation theorem** is introduced as a representational result with sufficiently many hidden units, not a guarantee that training finds an accurate model.
- Fully connected feed-forward architectures compose affine maps and activations. Sigmoid, hyperbolic tangent, and ReLU are compared; classification outputs become probabilities through logistic/softmax transformations. CNNs and recurrent networks are introduced as alternative architectures, without a full architectural course or corresponding assignment implementation.
- Binary **logistic regression** models linear log-odds using a sigmoid; multiclass/log-linear models use class-specific weights and a normalizing partition function/softmax. Maximum likelihood connects probability modeling with negative log-likelihood minimization.
- Mean-squared loss for regression, logarithmic loss for binary classification, and cross-entropy for class distributions. The neural exercise derives logistic gradients, performs two gradient steps, constructs XOR with threshold units, and shows that squared-error prediction for identical inputs with inconsistent labels recovers the average label.
- **Batch, stochastic, and minibatch gradient descent/ascent** distinguish full-data, single-sample, and small-batch derivative estimates. Learning-rate selection includes constant, time-based, stepwise, exponential, and adaptive schedules; epochs in supervised training are distinguished from environment episodes.
- **Backpropagation** applies the chain rule recursively through the computational graph. The exercise solution explicitly traces multiplication, addition, negation, exponential, and reciprocal nodes for a logistic unit, obtaining derivatives with respect to weights and inputs. A sheet informally calls this a softmax layer, but its displayed formula is a scalar sigmoid.
- Independent training/validation/test roles, architecture/hyperparameter selection, underfitting and overfitting, and stopping before validation deterioration. The lecture's examples illustrate regularization as a tunable model property rather than deriving a generalization bound.
- Coding 1 provides **TensorFlow 2/Keras** model subclassing, Sequential API, and functional API implementations. Dense-network examples include two 64-unit ReLU layers for wine-quality regression, two 10-unit ReLU layers for Iris classification, and 100/100/10 sigmoid layers for bank-deposit classification, followed by task-appropriate linear/logit outputs.
- The supplied training solution demonstrates CSV-to-`tf.data` pipelines, feature stacking, `GradientTape` derivative calculation, explicit optimizer updates, metric tracking, and the alternative `compile`/`fit`/`evaluate` workflow. SGD, Adam, and RMSprop are implemented options; sparse categorical cross-entropy from logits and mean-squared loss support classification/regression, with accuracy and mean absolute error for evaluation.
- Data preparation includes missing-row handling, one-hot encoding, label conversion, train/test splitting, and wine-feature standardization using training-set means/standard deviations. Provided bank-data preprocessing has target leakage, recorded below; this is not endorsed as a valid evaluation workflow.

### Value-function approximation and deep Q-networks

*Evidence: [L6], pp. 4–21; [E5], both pages and solution pp. 3–24; [C2] and [C2S].*

- Approximation parameterizes `V̂(s;w)` or `Q̂(s,a;w)` instead of storing all values. The lecture formulates squared value error weighted by policy-induced state visitation and derives gradient/SGD updates. For linear features, the derivative is the feature vector.
- A sampled bootstrapped target gives the **semi-gradient TD update** `Δw=αδ∇_w V̂(s;w)`, with `δ=r+γV̂(s';w)−V̂(s;w)`: the target is treated as fixed during differentiation even though it depends on current parameters. The analogous Q-learning update uses the maximum successor Q-value. General convergence guarantees from the tabular setting do not transfer automatically.
- Network input/output choices: a state input can produce one Q-value per discrete action; alternatively, a state–action pair can produce a scalar Q-value. A state-only scalar network approximates the value function. Feed-forward, convolutional, and recurrent architectures are possible approximators.
- Two instability mechanisms motivate **DQN**: correlated successive transitions and a moving bootstrapped target. **Experience replay** stores `(s,a,r,s',done)` tuples, draws random minibatches, decorrelates training inputs, and reuses experience. A **target network** supplies comparatively stationary successor values and periodically copies the online network's weights.
- DQN fits targets `y=r+γ(1−done) max_a' Q̂(s',a';w_target)` using a mean squared TD loss and gradients of the online selected-action values. The terminal mask prevents bootstrapping beyond terminal states. The loop separates action selection, transition collection, replay sampling, gradient updates, and target synchronization.
- Important hyperparameters include network architecture, exploration/learning rates, replay capacity, minibatch size, and target-update frequency. Atari examples show end-to-end pixel-to-action-value learning and replay/target-network ablation comparisons; these are published examples reproduced in teaching slides, not individually executed projects.
- Sheet 5 uses linear Q-features as a transparent stand-in for a neural approximator, works through target-network versus online weights, minibatches across episodes, and parameter updates. This supports algorithm mechanics without claiming that the hand calculation itself is deep-network training.
- Coding 2 applies DQN to **CartPole**: four observations (cart position/velocity and pole angle/angular velocity), two push actions, and upright-survival reward. The solution uses two 64-unit tanh layers, linear Q outputs, Adam, a bounded `deque` replay buffer, random minibatches, indexed selected-action values, and target synchronization. Saving/loading weights and evaluation/rendering loops are included. The task's reward goal is an instructional target, not an achieved personal result.

### Double DQN, prioritized replay, dueling networks, and Rainbow

*Evidence: [L6], pp. 22–31.*

- **Double Q-learning/Double DQN** addresses maximization overestimation: the online network selects the successor action and the target network evaluates it. This decouples selection from evaluation instead of taking the maximum of a single noisy estimator.
- **Prioritized experience replay** samples transitions with large absolute TD errors more frequently. Proportional priority adds a small positive offset; rank-based priority is less sensitive to outlier magnitude. Stochastic prioritization uses `P(i)=p_i^α/Σ_k p_k^α`, interpolating between uniform sampling and strong prioritization.
- Importance-sampling weights proportional to `(1/(N P(i)))^β` correct the altered sampling distribution; the displayed algorithm normalizes weights. The priority exponent and correction exponent have different roles. Diversity loss from greedy-only selection is a separate concern from sampling bias.
- **Dueling Q-networks** share an initial representation and split into state-value and advantage streams. The aggregation subtracts the mean advantage: `Q̂(s,a)=V̂(s)+Â(s,a)−mean_a' Â(s,a')`. It preserves the ordering of actions while sharing state-value information across actions with similar effects.
- **Rainbow** is presented as a combination of these improvements with multi-step learning, distributional return modeling, and noisy networks for exploration. The first three are developed in detail; distributional RL and noisy nets are named high-level additions, not fully derived or implemented in the archived coding tasks.

### Policy gradients, REINFORCE, and actor–critic theory

*Evidence: [L7], pp. 4–26; [E6], all tasks and its solution pp. 2–7.*

- Directly parameterized policies address stochastic decisions and continuous/high-dimensional actions. Rock–paper–scissors illustrates why a uniform stochastic Nash policy can be preferable to a deterministic move; an aliased-observation grid illustrates stochastic action selection under limited observations.
- Policy objectives include the initial-state value for episodic tasks and a state-distribution-weighted value objective for continuing tasks. Gradient ascent optimizes policy parameters. Finite-difference policy gradients perturb parameters and compare objective evaluations, but are computationally costly and noisy.
- The **likelihood-ratio/score-function identity** rewrites the gradient of an expectation as an expectation containing `∇_θ log π_θ(a|s)`. The **policy gradient theorem** weights this score by `Q^π(s,a)` under the corresponding policy/state-visitation measure; the lecture notes objective normalization and omits the general proof.
- For a Gaussian policy with mean `μ(s)=f(s)ᵀθ` and fixed variance, the score is `(a−μ(s))f(s)/σ²`. For a feature-softmax policy, the score is `f(s,a)−E_b~π[f(s,b)]`. The latter is derived in lecture and exercises; a two-action softmax reduces to a logistic probability.
- **REINFORCE** samples complete on-policy episodes, computes discounted reward-to-go, and applies return-weighted score updates. It avoids bootstrapped value-target bias but has high trajectory variance and cannot directly use arbitrary stale replay data. Its basic Monte Carlo form requires completed episodes. Stochastic policies provide action randomness, but do not by themselves guarantee adequate state/action exploration.
- **Q actor–critic** learns a policy (actor) and action-value approximation (critic). The actor takes score-weighted Q ascent steps; the critic uses a sampled next action under the current policy in its TD target, unlike Q-learning's maximum over next actions. Separate learning rates can be used, and updates occur after transitions rather than only after complete episodes.
- An action-independent **baseline** has zero expected score contribution, allowing variance reduction without changing the exact expected policy gradient. Choosing the state value yields the **advantage** `A^π=Q^π−V^π`.
- With the exact policy value, `δ=r+γV^π(s')−V^π(s)` is conditionally unbiased for the advantage at `(s,a)`. Replacing that value with a learned approximation generally introduces bias; advantage actor–critic trades this against variance and avoids needing separate learned Q and V functions.
- The **compatible function approximation theorem** identifies conditions under which a critic preserves the exact expected gradient: `∇_w Q̂(s,a;w)=∇_θ log π_θ(a|s)` and critic parameters minimizing the corresponding policy-weighted squared Q-error. The proof uses the first-order MSE condition. Exercises construct a compatible linear critic from centered softmax features; this is not a guarantee for an arbitrary neural critic.

### Multi-step learning, TD(λ), and eligibility traces

*Evidence: [L8], pp. 5–17; [E7], all five exercises and appendix; solution pp. 2–18; [F], p. 3; [C3S], `calc_advantage`.*

- **n-step returns** combine observed discounted rewards over `n` transitions with a bootstrapped value at the last state. Their bias/variance behavior lies between one-step TD and full Monte Carlo. Random-walk experiments compare errors for different horizons and step sizes.
- **Forward-view TD(λ)** averages n-step targets with geometric weights `(1−λ)λ^(n−1)`; finite episodes put remaining weight on the full return. `λ` controls how far credit propagates and how strongly updates bootstrap. Full forward returns require future trajectory data unless truncated.
- **Backward-view TD(λ)** maintains accumulating state eligibility `E_t(s)=γλE_(t−1)(s)+1(S_t=s)` and updates each state's value by `αδ_tE_t(s)`. The trace combines visit frequency and recency; credit-assignment examples distinguish the contributions of bells and lights preceding reward.
- The exercise proof establishes forward/backward equivalence when weights/values are held fixed and changes are accumulated for an end-of-episode update. Online updates generally differ because intermediate values change; `λ=0` reduces both to TD(0), while small step sizes make the demonstrated difference small.
- With differentiable value approximation, parameter eligibility replaces state counts: `E_t=γλE_(t−1)+∇_w V̂(S_t;w)`, and `Δw=αδ_tE_t`. Related policy-score traces support actor updates; n-step or λ-return minus the value estimate supplies an advantage estimate.
- Sheet 7 proves the recursive λ-return relation and, for fixed weights, `G_t^λ−V̂(S_t)=Σ_k≥t (γλ)^(k−t)δ_k`, with terminal/limiting terms treated in the episode setting. This links forward targets to weighted TD errors and is directly used in the supplied PPO advantage calculation.
- **Generalized advantage estimation (GAE)** is explicitly named in the applied multi-agent lecture; Coding 3 implements the same exponentially weighted TD-error structure using `γλ` discounted cumulative sums. Its value-network targets are discounted reward-to-go, distinct from its policy advantages.

### Parallel actor–critic, trust regions, and PPO

*Evidence: [L8], pp. 19–35 and appendix p. 51; [C3], pp. 2–5; [C3S]; [F], p. 3.*

- **A2C/A3C** use multiple workers interacting with separate environment copies and contributing policy/value gradients to shared networks. A2C synchronizes workers; A3C allows asynchronous updates. Independent trajectories decorrelate samples without DQN-style replay.
- **Entropy regularization** adds a policy-entropy contribution to encourage exploration, with a coefficient controlling reward versus randomness. The discrete entropy is `−Σ_a π(a|s)log π(a|s)`; uniform action probabilities maximize it, deterministic choices minimize it.
- **Trust Region Policy Optimization (TRPO)** controls change in the action distribution rather than Euclidean parameter distance. The surrogate maximizes old-policy expectations of the likelihood ratio `π_new(a|s)/π_old(a|s)` times old-policy advantage, constrained by KL divergence between old and new policies.
- Importance sampling permits evaluating that surrogate using old-policy samples. A practical approximation averages statewise KL values on visited states. The lecture motivates monotonic improvement but does not derive a complete guarantee for the sampled/approximate implementation; that claim is not extended to arbitrary empirical training.
- The natural-gradient/Fisher view uses the expected outer product of policy scores as the **Fisher information matrix**, locally approximating KL geometry. An inverse-Fisher-scaled gradient follows from a quadratic/Lagrangian approximation. Explicit matrix inversion is costly at neural-network scale; approximate solves and a search for a constraint-respecting step are discussed. The appendix links natural actor–critic, surrogate/minorization–majorization reasoning, and TRPO, without a complete implementation.
- **PPO-Penalty** penalizes KL with an adapted coefficient. **PPO-Clip**, the developed variant, maximizes the expected surrogate `min(ratio·A, clip(ratio,1−ε,1+ε)·A)`. Positive advantages cap the incentive to increase the ratio beyond `1+ε`; negative advantages cap the incentive to decrease it below `1−ε`.
- Clipping changes the objective, rather than enforcing a hard bound on policy probabilities or an exact KL constraint. Multiple gradient epochs reuse a recent batch while storing its old-policy probabilities. The lecture explicitly relinquishes the claimed TRPO convergence guarantee in exchange for simpler implementation.
- Coding 3 trains separate categorical-policy and scalar-value networks on CartPole. The solution uses tanh MLPs, categorical sampling from logits, stable log-softmax action probabilities, stored old log probabilities, λ-weighted TD-error advantages, an empirical clipped objective, squared return regression, and separate Adam optimizers. It performs repeated actor/critic epochs on each batch.
- The supplied code stores several actor trajectories but collects them sequentially in one environment object; it demonstrates the batch structure, not actual parallel rollout execution. Its buffer masking and termination limitations are recorded below.

### Continuous-action actor–critic: DDPG and SAC

*Evidence: [L8], pp. 38–46.*

- Continuous actions make exhaustive `argmax_a Q(s,a)` impractical. **Deep Deterministic Policy Gradient (DDPG)** learns a deterministic actor `μ_θ(s)` approximating the Q-maximizing action and a critic differentiable with respect to actions. The actor maximizes the critic's value on replay states through differentiable action selection.
- Target actor and critic networks produce the bootstrapped critic target. **Polyak averaging**, `w_target←τw_online+(1−τ)w_target`, replaces occasional hard synchronization; the same principle updates target-policy parameters.
- DDPG is an off-policy continuous-action actor–critic method. Gaussian noise added to deterministic actions supplies exploration during training; the lecture notes that the original method used a different noise process but does not develop it.
- **Soft Actor–Critic (SAC)** is introduced at overview depth: a stochastic continuous policy parameterizes Gaussian means/positive variances, and a differentiable squashing transform such as tanh enforces action bounds.
- SAC combines replay with two Q-functions and takes their minimum (**clipped double Q-learning**) to reduce overestimation. A maximum-entropy objective adds an entropy bonus to discounted rewards. Its coefficient can be tuned manually or learned against a target entropy. The lecture distinguishes an older extra-value-network version from the newer twin-Q form and mentions a discrete-action variant.
- Comparative selection considers discrete/continuous actions, on/off-policy data, experience reuse, sample collection cost, and training stability. SAC's complete update equations, DDPG/SAC code, TD3, and ACER are not supplied; the latter two are outlook names rather than extracted full algorithms.

### Planning–learning combinations, extensions, and applications

*Evidence: [L9], pp. 6–43; [E1–E2]; [C2–C3].*

- **Monte Carlo tree search (MCTS)** follows selection, expansion, rollout/simulation, and result backup, accumulating outcomes along the traversed path. It replaces exhaustive game-tree evaluation with selective sampling.
- **AlphaGo** combines neural policy guidance, value evaluation, and MCTS; the teaching example distinguishes supervised expert-move training from self-play policy improvement/value learning. **AlphaGo Zero** starts from self-play and uses one residual network with policy and value outputs. Its search selects action value plus an exploration-confidence term dependent on priors and visit counts, then backs up network evaluations. Search policy improvement and terminal-outcome value evaluation are distinct components.
- Multi-agent hide-and-seek illustrates entity-centered observation embeddings, partial observation, memory, shared parameters, self-play, PPO/GAE, and a centralized omniscient training critic with decentralized observation-based execution. It is a case study, not an archived implementation task.
- **Inverse RL** aims to infer a reward function from expert execution traces before solving the resulting control problem. Nonidentifiability—many rewards explaining the same behavior—and assumptions about expert optimality are emphasized; no particular inverse-RL solver is derived.
- **Hierarchical RL** uses temporal/action abstraction. **Options** are macro-actions with subpolicies in a semi-MDP, while **feudal RL** assigns subgoals through manager/submanager levels and local rewards. Reusable skills, reduced action/observation spaces, and long credit-assignment horizons motivate these approaches.
- **Transfer learning** reuses Q-functions, policies, or learned representations across source/target tasks; zero-shot use differs from few-shot adaptation. Changes in action space and inadequate exploration from a converged source policy are difficulties. **Multitask RL** learns related tasks jointly through task identifiers or multiple outputs; conflicting gradients, reward-scale differences, and unequal resource allocation are challenges. Policy distillation and actor-mimic are briefly named approaches.
- **Multi-agent RL** distinguishes cooperative/competitive/mixed settings, homogeneous/heterogeneous agents, and centralized/decentralized control. Challenges include scalability, coordination, shared-reward credit assignment, partial observability, and nonstationarity as other policies learn. Centralized training with decentralized execution, shared parameters, learned communication, factorized values, and centralized critics are overview approaches.
- **Portfolio trading** is formulated through prices, holdings, balance, and market features, with buy/sell/hold or normalized continuous trade actions and portfolio-value-change rewards. A published ensemble of policy-gradient strategies is compared with alternatives; no financial outcome or trading skill is attributed to the student from these slides.
- **Autonomous lane keeping/control** uses vehicle/sensor observations and steering, acceleration, and braking actions. The case study compares discretized DQN actions with continuous actor–critic control and illustrates smoother trajectories from the latter in that example.
- Business/operations-research outlooks cover dynamic compensation on crowdsourced delivery platforms, pricing competition/collusion, and neural decision weights combined with a combinatorial optimizer for dynamic stochastic control. These are application/research examples, not student projects or evidence of implementing model-predictive control.
- Gridworld navigation, optimal stopping, route planning, game playing, CartPole balancing, and bank/Iris/wine prediction provide the concrete teaching and assignment problems.

## Computational work and tools

- **Python** is the implementation language. NumPy supports arrays, random sampling, and value/buffer calculations; pandas handles tabular data/one-hot encoding; scikit-learn supplies train/test splitting; Matplotlib plots learning curves.
- **TensorFlow/Keras** supplies neural models, differentiable losses, `GradientTape`, Adam/SGD/RMSprop, logits, categorical sampling, tensor indexing, and explicit/custom versus high-level training workflows. Requirements contain additional dependencies; they are not all claimed as substantively taught tools.
- **Gym** appears in older CartPole templates, while **Gymnasium** and `CartPole-v1` appear in updated solutions. Pygame is an environment/rendering dependency. SciPy's `signal.lfilter` implements efficient reverse discounted cumulative sums in PPO. Python's `collections.deque`, `random.sample`, and `argparse` support replay and configurable experiments.
- Coding 1 supplies deterministic DFS/BFS/UCS, stochastic tabular Q-learning, and supervised neural classification/regression. Coding 2 supplies neural DQN; Coding 3 supplies PPO-Clip with actor/critic training and λ-based advantage estimation. These are assignment specifications/templates/solutions, not personal submissions or proof that a target score was reached.
- CSV data for Iris, bank marketing, and wine quality are included in both Coding 1 template and solution packages. Original preprocessing inputs under `data_unprocessed/` are referenced but absent; processed data are sufficient to establish the assigned tasks and inspect their feature structure.

## Thematic categories

- Reinforcement learning and sequential decision-making
- Dynamic programming and stochastic control
- Search, planning, and game trees
- Neural networks and deep learning
- Policy gradients and actor–critic methods
- Numerical and stochastic optimization
- Probability, Markov models, and decision theory
- Robotics and autonomous systems
- Operations research and data-driven optimization
- Quantitative decision-making and portfolio applications

## Coverage validation

| Source sequence | Profile coverage / review outcome |
|---|---|
| Introduction | Optimization/decision-making framework and nine-part syllabus; institutional/admin slides excluded from technical claims |
| Search, complete 263-page reveal sequence | Graph/tree distinctions, utilities, DFS/BFS/UCS, greedy/A*, admissibility proof, minimax, expectimax; final reveal states avoid duplicate counting |
| MDP | Markov/horizon/reward/policy models, Bellman equations, value/policy iteration and convergence scope |
| RL | Empirical model, direct evaluation, TD/Q-learning, exploration bonuses, learning rates, regret overview |
| NN | Features/approximation theorem, logistic/softmax, objectives, SGD variants/schedules, backpropagation, validation |
| DQN | Semi-gradients, replay, targets, terminal masking, Double DQN, prioritized replay/weights, dueling streams, Rainbow scope |
| PG | Objectives, score identity/theorem, Gaussian/softmax scores, REINFORCE, Q/advantage actor–critic, compatible-critic theorem |
| APG, including late pages/appendix | n-step/λ returns and traces, equivalence conditions, A2C/A3C/entropy, TRPO/Fisher, PPO, DDPG/Polyak, SAC, algorithm comparison |
| Applied topics | MCTS/AlphaGo variants, multi-agent case, finance/driving, inverse/hierarchical/transfer/multitask/multi-agent RL, OR/pricing outlooks |
| E1 + solution | Adds rationality examples, multiplayer utility vectors, uncertain racing costs and explicit algorithm traces |
| E2 + solution | Adds branching-population Markov argument, finite-horizon stopping, transition distributions, explicit value/policy evaluation |
| E3 + solution | Adds empirical model versus return estimates, update calculations, exploration convention, step-size series conditions |
| E4 + solution | Adds XOR, identical-input squared-loss optimum, logistic computational graph and derivative example |
| E5 + solution | Adds minibatch/target-copy accounting with linear features; no assumption of a neural implementation for that calculation |
| E6 + solution | Adds compatible softmax critic and binary-policy REINFORCE derivation |
| E7 + solution | Adds fixed-weight equivalence proof, online counterexample, feature eligibility, and λ-return/TD-error identity |
| Coding 1–3, all six packages | Templates, completed solutions, utility/environment scaffolding, datasets, and setup differences inspected statically |
| Formula sheet; 8 example-question pages + 17 solution pages | Confirms search, MDP, TD, logistic loss, approximate Q updates, baseline/REINFORCE, and λ/PPO assessment coverage; embedded questions read visually |

## Source limitations and unresolved issues

- **Version/provenance:** the introduction establishes WS 2025/26, but other files reuse older material: Coding 3's cover says WiSe21/22 while its footers say WiSe24/25; the applied lecture advertises a SoSe24 follow-up. Template dependencies target older TensorFlow/Gym versions, while updates introduce Gymnasium/Keras 3. Preserve the mixed versions rather than interpreting every date as a separate course taken.
- **Mathematical extraction:** headings/prose are searchable, but many native slide formulas and embedded exam paragraphs vanish from extracted text. Visual inspection recovered the key statements used above. Lecturer narration and live derivations remain absent; no missing formula was reconstructed merely from its expected subject matter.
- **Theory scope:** tabular Q-learning convergence and TRPO improvement are summarized more broadly in slides than the locally stated assumptions justify. The profile retains the step-size analysis, exploration requirements discussed, surrogate/KL formulation, and limits of approximation, without asserting an unconditional neural convergence theorem. The basic policy-gradient slides simplify state-distribution normalization and exploration; stochastic policies are not treated as guaranteeing coverage.
- **Bank data leakage:** Coding 1's `preprocess_bank_data` copies `y` to `target` but does not assign the result of dropping `y`. The supplied training/test CSVs retain both columns, and the neural script treats all but the final column as inputs. Thus the target is included as an input; bank prediction accuracy from this teaching setup would not establish valid held-out predictive performance. The source is preserved unchanged.
- **Teaching-code limitations:** the tabular agent initializes its greedy maximum to zero, so its action-selection function can return an empty action when all action values are negative. Q-updates are rounded to three decimals. Some template files intentionally have incomplete expressions/blocks and cannot parse before completion; solution packages also retain copies of these templates. Only the explicit `_solution.py` files are treated as completed algorithm examples.
- **CartPole termination and portability:** both updated solutions ignore Gymnasium's `truncated` signal and use only `terminated` as `done`. This affects time-limit handling and return/target semantics. DQN's stopping threshold/comment and older task reward goals do not agree; none is interpreted as a measured result. Packages would need compatibility/termination review before reuse, and no training was performed.
- **PPO specialization:** the solution collects actors sequentially, filters buffer entries by positive reward (valid only for its assumed reward structure), and calculates advantages when `done` occurs rather than handling arbitrary truncated rollouts. The sample demonstrates PPO/λ-return mechanisms but is not a verified generic PPO implementation.
- **Assessment/material limits:** exam examples, a formula sheet, instructions, and a seating list are present; no actual completed examination/submission is supplied. An invitation and external video/tutorial links do not provide enough content to infer an additional guest-lecture syllabus or implementation beyond local evidence. Administrative personal information was not used in the technical profile.

## Sources

**Official metadata:** `01_inventory/courses.csv`, row `mgt001299`; transcript `00_sources/transcripts/Leistungsnachweis_03797442_07102026_1242_20261007124207_1.pdf`, p. 4. The archive index and `01_inventory/archive_matches.csv` establish the module/archive match.

All labels below refer to members of `00_sources/tum/archives/Introduction to 950839140 (W25_26)_20261012_1601.zip`. Thus `[L8], p. 33` resolves to that ZIP **::** `7. Januar - 13. Januar/Lecture Slides APG.pdf`, physical PDF p. 33. For coding sources, append **::** the indicated nested code path inside the `.imscc` ZIP.

| Label | Exact archive member | Pages |
|---|---|---:|
| L1 | `22. Oktober - 28. Oktober/Lecture Slides Introduction.pdf` | 34 |
| L2 | `22. Oktober - 28. Oktober/Lecture Slides Search Algorithms.pdf` | 263 |
| L3 | `29. Oktober - 4. November/Lecture Slides Markov Decision Processes.pdf` | 51 |
| L4 | `12. November - 18. November/Lecture Slides RL.pdf` | 34 |
| L5 | `19. November - 25. November/Lecture Slides NN.pdf` | 48 |
| L6 | `26. November - 2. Dezember/Lecture Slides DQN.pdf` | 33 |
| L7 | `3. Dezember - 9. Dezember/Lecture Slides PG.pdf` | 28 |
| L8 | `7. Januar - 13. Januar/Lecture Slides APG.pdf` | 51 |
| L9 | `21. Januar - 27. Januar/Lecture Slides AT.pdf` | 47 |
| F | `Allgemeines/Exam Formula Sheet.pdf` | 3 |
| C1 | `3. Dezember - 9. Dezember/Coding 1 Task Description.pdf` | 10 |
| C2 | `7. Januar - 13. Januar/Coding 2 Instructions.pdf` | 1 |
| C3 | `21. Januar - 27. Januar/Coding 3 Instructions.pdf` | 5 |

Exercise groups cite both the sheet and the corresponding solution deck:

- **E1:** `5. November - 11. November/Exercise Sheet 1 Search Algorithms.pdf` (4 pp.); `5. November - 11. November/Exercise Solution Search Algorithms.pdf` (40 pp.).
- **E2:** `12. November - 18. November/Exercise Sheet 2 MDP.pdf` (3 pp.); `12. November - 18. November/Exercise Solution MDP.pdf` (34 pp.).
- **E3:** `19. November - 25. November/Exercise Sheet 3 RL.pdf` (3 pp.); `19. November - 25. November/Exercise Solution RL.pdf` (44 pp.).
- **E4:** `26. November - 2. Dezember/Exercise Sheet 4 NN.pdf` (2 pp.); `26. November - 2. Dezember/Exercise Solution NN.pdf` (14 pp.).
- **E5:** `17. Dezember - 23. Dezember/Exercise Sheet 5 DQN.pdf` (2 pp.); `17. Dezember - 23. Dezember/Exercise Solution DQN.pdf` (24 pp.).
- **E6:** `14. Januar - 20. Januar/Exercise Sheet 6 Policy Gradients.pdf` (1 p.); `14. Januar - 20. Januar/Solution Exercise PG.pdf` (7 pp.).
- **E7:** `14. Januar - 20. Januar/Exercise Sheet 7 Advanced PG.pdf` (3 pp.); `14. Januar - 20. Januar/Solution Exercise APG.pdf` (18 pp.).
- **Assessment:** `28. Januar - 3. Februar/Example Questions.pdf` (8 pp.) and `28. Januar - 3. Februar/Example Questions Solutions.pdf` (17 pp.).

Computational references:

- **C1T:** `3. Dezember - 9. Dezember/Coding 1 Exercise Template.imscc`. Root `README.md`, `search/`, `reinforcement_learning/`, `deep_neural_network/`, and `requirements.txt` identify tasks and scaffolding.
- **C1S:** `3. Dezember - 9. Dezember/Coding Exercise 1 Solution.imscc` **::** root `CodingExerciseSolutions/CodingExercise/`. Specific paths relative to that root: `search/run_search_solution.py`, `search/util.py`, `search/environment.py`; `reinforcement_learning/run_Q_learning_solution.py`, `reinforcement_learning/util.py`, `reinforcement_learning/environment.py`; `deep_neural_network/train_deep_neural_network_solution.py`, `deep_neural_network/preprocessing.py`, and `deep_neural_network/data/`. The solution package retains incomplete template counterparts as well.
- **C2T:** `7. Januar - 13. Januar/Coding 2 Template.imscc` **::** `DQN_template/main.py`, `DQN_template/README.md`, `DQN_template/requirements.txt`.
- **C2S:** `7. Januar - 13. Januar/Coding 2 Solution.imscc` **::** `mainDQN_solution.py`, `Setup_guide.md`, `requirements_new.txt`.
- **C3T:** `21. Januar - 27. Januar/Coding 3 Template.imscc` **::** `mainPPO_empty.py`, `README.md`, `Setup_guide.md`, `requirements_new.txt`.
- **C3S:** `4. Februar - 10. Februar/Coding 3 Solution.imscc` **::** `mainPPO_solution.py` and `README.md`. Relevant functions are `runPPO`, `logprobabilities`, `discounted_cumulative_sums`, `calc_advantage`, `train_policy`, and `train_value_function`.
