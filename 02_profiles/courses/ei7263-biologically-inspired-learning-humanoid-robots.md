# Biologically-Inspired Learning for Humanoid Robots

## Module metadata and identity

| Field | Value |
|---|---|
| Course ID | ei7263 |
| Official module code | EI7263 |
| Official course name | Biologically-Inspired Learning for Humanoid Robots |
| ECTS | 6 |
| Grade | 1.3 |
| Academic record | Degree course; transcript PDF p. 3 |
| Profile status | complete_validated |

Academic metadata comes from the transcript and `01_inventory/courses.csv`. The matching source is `00_sources/tum/archives/Biologically-In 950799123 (S25)_20261012_1600.zip`.

## Evidence base and course structure

The archive and recursively inspected tutorial packages contain **58 PDFs / 1,214 physical pages**, including two duplicate tutorial documents inside the Tutorial 2 submission. The core sequence is **Lectures 1–7 in eight decks / 341 pages**, with Lecture 6 split into two parts. Two single-page supplements clarify cerebellar circuitry and reciprocal/nonreciprocal basal-ganglia connections. Five tutorials cover ROS 2, robot perception/control, feedforward neural networks, CMAC and reinforcement learning. Templates, a solution package and four Team E submissions supply Python/ROS implementations, data, model files, plots and videos.

A substantial fraction of PDF volume is background reading: a 251-page artificial-cerebellum dissertation, cerebellar/neurorobotics and basal-ganglia reviews, RL-DT papers and 25 papers offered for student presentations. These were structurally inventoried and topic/abstract-screened; they were not all treated as delivered lectures or read as independent projects. The one supplied student presentation explicitly names Pablo Yeste Blesa and concerns distributional dopamine-based RL. Its specific technical content is included below, supported by its associated paper.

References identify exact archive members in the source register; page numbers mean **physical PDF pages**. All core decks and tutorial specifications were inspected through text/structure, complemented by 34 rendered mathematical, biological-circuit, algorithmic and geometric pages. Nested ZIP and TAR sources/notebook cells were inspected statically. No course code, robot command, model deserialization or installation instruction was executed. Videos were inventoried, not analyzed frame by frame; they are not a basis for claimed quantitative performance.

## Technical content

### Embodied learning and motor representations

*Evidence: [L1], pp. 7–32; [L2], pp. 2–27.*

- Neurorobotics joins neuroscience with robot control: perception–testing–learning–action rather than a fixed sense–act program. Human development, interaction and neural evidence motivate self-exploration, observation, goal-directed adaptation and transfer, without identifying a biological analogy as a proven optimal controller.
- Learning compensates for uncertain body/environment models and changing loads: nominal kinematics/dynamics alone do not determine actual sensory feedback during contact or manipulation. Task-space, joint-space and latent/potential-variable representations define different learning problems.
- **Supervised**, **unsupervised** and **reinforcement learning** are distinguished by target labels, hidden structure and scalar reward. Training versus testing and prediction on unseen data are explicit concerns. Introductory links between learning paradigms and brain areas are modeling heuristics, not an exhaustive anatomical decomposition.
- **Motor babbling** acquires body/environment mappings through exploratory joint movements and correlated visual/proprioceptive feedback. Own-body identification, internal/inverse model learning and reachable-space maps lead toward goal-driven exploration.
- **Learning by demonstration** supplies demonstrated trajectories rather than prescribing every control command. A worked research example combines **Gaussian mixture regression** and **PCA** to generalize trajectories using end-effector position, joint position and object distance. The slides introduce these methods at framework level; a complete GMR derivation or implementation is not supplied.
- **Motor coordination for drawing:** a **central pattern generator (CPG)** supplies motor patterns; multi-objective parameter optimization acquires coordination locally. A **self-organizing map (SOM)** represents end-effector coordination over Cartesian workspace, and **inverse-distance weighting** estimates motor-program parameters at map units to transfer drawing behavior to new regions. The illustration labels a GA initial solution, but does not supply a full genetic-algorithm specification or convergence result.
- Locomotion, slope adaptation, perturbation recovery, drawing and concrete action representations are teaching/research examples, not claims of personally reproducing every system.

### Cerebellar anatomy, coding, and supervised adaptation

*Evidence: [L3], pp. 4–27; [L4], pp. 2–29; [SC].*

- Central nervous-system subdivisions and hierarchical motor organization situate cerebellar coordination relative to cortex, brainstem and spinal pathways. Cerebrocerebellum, spinocerebellum and vestibulocerebellum; dentate, interposed and fastigial nuclei; cerebellar peduncles and somatotopic maps distinguish functional structures.
- Cerebellar cortical layers comprise granule, Purkinje and molecular layers. Granule, Purkinje, Golgi, basket and stellate cells have distinct input/output and inhibitory roles. Mossy fibers convey sensory/proprioceptive and cortical input; granule-cell axons form parallel fibers; climbing fibers from the inferior olive provide the modeled teaching signal.
- **Marr–Albus associative-memory model:** context/body-state patterns are associated with motor commands. Storing overlapping patterns introduces interference/saturation; expansion to a larger granule-cell population yields sparser, less-overlapping codes. Golgi-cell inhibition regulates input activity; basket/stellate inhibition contributes threshold setting and lateral interactions.
- Purkinje-cell output inhibits deep cerebellar nuclei, shaping a deep excitatory pathway through a cortical inhibitory loop. The corrected single-page supplement preserves the sign/connectivity explanation rather than inferring it from flattened text.
- Simple spikes driven by parallel fibers versus complex spikes associated with climbing fibers; **long-term potentiation/depression** and concurrent parallel/climbing-fiber activation motivate changes in synaptic efficacy. The adaptive-filter interpretation and the parallel-fiber timing idea are alternative explanatory models, not identical mechanisms.
- Timing, spatial accuracy, skill acquisition and prediction-error comparison explain cerebellar roles. Lesion examples illustrate impaired coordination/timing without turning teaching slides into clinical guidance.

### Internal models, feedback, and coordinated control

*Evidence: [L3], pp. 28–44; associated neurorobotics chapter [RN], section 62.2.4; cerebellar review [RC] as cited by L3 p. 43.*

- **Schema theory** supplies functional perceptual, motor and coordinating modules without requiring a one-to-one localization to brain anatomy. A coordinated control program interleaves modules according to task/sensory state; multiple schema instances can track distinct objects.
- Reach-to-grasp decomposes transport, hand preshaping and final tactile closure while coordinating their timing. Perturbations of object location/size require feedback correction rather than replay of a fixed motion.
- **Forward/direct models** predict motor/sensory consequences from commands. **Inverse models** map desired outcomes or sensory targets to suitable motor commands. Their learning/inversion difficulties are distinct.
- **Efference copy**, predicted sensory feedback/corollary discharge and actual feedback/reafference permit prediction-error computation. That error can update the internal model and initiate force corrections, illustrated by grip-force adaptation to movement-induced load.
- Feedback corrects disturbances; feedforward/predictive components accommodate sensorimotor delays and reduce dependence on delayed corrections. The source's broad statement that delayed closed-loop control is not viable is treated as motivation for predictive augmentation, not a general mathematical impossibility theorem.

### Cerebellar Model Articulation Controller (CMAC)

*Evidence: [L4], pp. 30–54; formulas visually checked pp. 36–38; [T4], [TP], [C4].*

- **CMAC** is a local function approximator/associative lookup memory inspired by cerebellar recoding, designed for fast online motor learning. Neural-network and lookup-table interpretations describe the same basic mapping.
- Input-feature units quantize bounded input coordinates; association units combine active feature ranges; outputs sum active association weights. In the slide's notation, `x_i = Σ_jk w_ijk a_jk`, where association activations are binary and only a small subset is active for a particular input.
- **Target training:** active weights receive a learning-rate-scaled share of output error, `Δw_ijk = α a_jk (t_i−x_i)/n_a`. **Error training** uses an externally supplied error direction instead of a target residual. For the illustrated fixed active set, α=1 moves the summed output to the target in that presentation; this is a local update property, not global nonlinear-control convergence.
- **Local generalization:** modifying one sample affects overlapping receptive fields rather than every input globally. Quantization makes the mapping piecewise constant; resolution increases memory requirements, while receptive-field size trades local detail against spatial smoothing. Input limits/clamping and coverage of the training region matter.
- Trajectory-ordered versus randomly presented samples; sparse training produces separated approximation bumps, while overlapping local neighborhoods improve interpolation. The plots compare several sampling densities and illustrate remaining gaps, not a universal error bound.
- Hashing compresses virtual weight space but introduces collisions/interference. The lecture treats hash-selection tradeoffs; **Tutorial 4 explicitly requires a lookup table without hashing**.
- Advantages are fast mapping/local updates and protection of distant regions from local retraining. Limitations include high-dimensional memory growth, discontinuities, poor interpolation across unobserved regions and hyperparameter/coverage design.
- The reaching exercise maps two image coordinates to two shoulder coordinates with fixed head/elbow and ignored depth. Required comparisons use resolution 50, receptive fields 3 and 5, and training sets of 75 versus 150 samples; MSE-over-epoch plots and an FFNN comparison connect coverage/locality to empirical behavior.
- Submitted code additionally tries receptive field 10 and a shuffled 85/15 train/validation split. Its table uses a grid of `n_a²` positions and averages outputs, differing from the lecture's fixed-`n_a` summed convention. The same update scaling must therefore not be described as an exact implementation of the slide formula. One prediction branch returns an unnormalized sum while the usual branch returns an average.

### Basal ganglia, action selection, and biological evidence

*Evidence: [L5], pp. 4–43; [SB]; complementary article abstracts [RB].*

- Striatum (caudate/putamen), GPe/GPi, substantia nigra pars reticulata/compacta and subthalamic nucleus form cortico–basal-ganglia–thalamo–cortical circuits. The input/output stages are distinguished from dopamine modulation.
- **Direct pathway:** cortical excitation of striatum, striatal inhibition of GPi/SNr and disinhibition of thalamocortical output. **Indirect pathway:** striatum inhibits GPe, disinhibiting STN, which excites GPi/SNr and increases output inhibition. D1/D2 receptor effects motivate opposing modulatory influences in the simplified circuit.
- Action initiation/termination, switching and suppression of competing programs explain why opposing pathways may cooperate rather than simply represent separate on/off commands. Voluntary motor, procedural-learning, eye-movement, cognitive and motivational functions broaden the scope.
- Motor, prefrontal and limbic loops; reciprocal connections maintain function within circuits, while nonreciprocal connections channel motivational/cognitive influence toward motor execution. Parallel specialization and cross-loop integration are complementary.
- **Optogenetics** combines light-sensitive cellular manipulation with electrophysiology to investigate identified pathways. Rapid-action-sequence studies motivate coordinated direct/indirect activity and action chunking; schematic all-pathway stimulation is not identical to selective physiological action representation.
- Selection machines, response gating, working-memory maintenance, reinforcement learning, dimensionality reduction and sequence processing are presented as hypotheses for basal-ganglia contributions, not a single proven comprehensive theory.
- Dopaminergic reward-prediction signaling links these circuits to RL; Parkinson/Huntington examples provide functional context without supplying a diagnostic or therapeutic model.

### Sequential decision models and reinforcement-learning algorithms

*Evidence: [L6a], complete deck; [L6b], pp. 2–68; [RE], pp. 1–6.*

- Agent/environment interaction distinguishes observation, private environment state, internal agent state and history. Full versus partial observability determines whether observations alone are adequate state descriptions. **Markov decision processes** provide transition/reward models for sequential action selection.
- A policy may be deterministic or stochastic. **Discounted return**, state-value `vπ(s)` and action-value `qπ(s,a)` are expected future-reward quantities conditioned on policy; immediate reward is not equivalent to long-term value. Optimal policies/value functions and **Bellman expectation/optimality equations** express recursive consistency.
- **Dynamic programming:** model-based policy evaluation, one-step greedy improvement and policy iteration; value iteration appears explicitly in the RL-DT assignment/papers. FrozenLake/gridworld diagrams illustrate stochastic transitions and policy changes.
- **Monte Carlo policy evaluation** estimates value from complete sampled returns using empirical/running means. **TD(0)** bootstraps after one transition: `V(S) ← V(S)+α[R+γV(S′)−V(S)]`, with terminal value initialized to zero in the displayed algorithm. MC, TD and DP differ in full-return versus bootstrap targets and sampled versus expected backups.
- **SARSA** is on-policy control: its target uses the next action actually selected by the behavior policy, `R+γQ(S′,A′)`. **Q-learning** is off-policy control: its target uses `R+γ max_a Q(S′,a)`. ε-greedy exploration, random policies and cliff-walking examples show how risky behavior and target-policy evaluation differ.
- Model learning through observed transition counts and **passive adaptive dynamic programming** contrasts with passive TD and active Q-learning in the numerical supplement. Fixed-policy Bellman equations form a linear system; unvisited states remain unresolved rather than assigned learned values without evidence.
- Biological reward-prediction errors motivate TD learning, with Schultz–Dayan–Montague and Doya examples. The algorithmic formulations are substantive; actor–critic mechanisms in other offered papers are supplementary reading, not a supplied actor–critic lab.
- No rigorous full convergence theorem with sufficient assumptions is supplied for these robot implementations. The slides' claim that TD is generally “better” than DP/MC is not adopted; model availability, sample cost and bootstrap effects distinguish their appropriate uses.

### RL-DT: factored model learning and robot soccer

*Evidence: [T5], [TS5]; [RD1], sections 2–3; [RD2], physical pp. 2–4; implementation [C5].*

- **Reinforcement Learning with Decision Trees (RL-DT)** learns a model from state/action/next-state/reward experiences, then plans inside it. Learning **relative state changes** rather than absolute next coordinates promotes generalization of action effects to unvisited states.
- A separate tree predicts each state-variable change, and a reward tree predicts expected immediate reward. Combining marginal transition predictions into a joint distribution assumes **conditional independence of state-variable changes given state and action**; this modeling assumption may fail for coupled physical variables.
- The paper's **C4.5** split selection uses information gain and both numerical/categorical inputs. The local submission instead uses scikit-learn `DecisionTreeClassifier`/`DecisionTreeRegressor`; their presence is not evidence that this code implements C4.5.
- The algorithm updates its model from interaction, recomputes action values through **value iteration** after model changes, and switches between exploration and exploitation using a heuristic policy-value threshold. The humanoid paper uses 40% of known maximum one-step reward; least-visited state/action exploration and optimistic reward bonuses are discussed. This heuristic can stop before discovering the globally optimal policy.
- Penalty kicks hold ball location/distance fixed while the agent adjusts its leg and kicks past a keeper. Perception uses color blobs or **ArUco markers** and joint-state feedback; move-in, move-out and kick form the discrete action set. Cumulative-reward plotting and robot demonstration are required outputs. The specification still names NAO, but supplied 2025 implementation uses the AiNex ROS 2 framework.
- Local code discretizes leg/keeper/post measurements, classifies per-coordinate deltas, forms products of predicted probabilities and regresses reward. It records transitions, periodically refits trees, tracks visit counts and waits for human reward input following a kick. The adjusted version has four state features and plans over bounded discrete combinations; an older two-feature version is also present.
- These are statically observed intended methods, **not verified correct planning software**. In `model_based_rl_adj.py::compute_values`, value/Q assignment is outside the two innermost post-bin loops, so only the last post-bin combination is inserted into the next value table for each outer pair. That does not implement a complete Bellman sweep. Other limitations include inconsistent physical leg-offset/state updates, absent optimistic-bonus implementation, and readiness checks that do not guarantee valid goalpost measurements/divisors.

### Self-organizing maps, success/failure memory, and risk modulation

*Evidence: [L7], pp. 2–39; algorithm/geometry checked visually pp. 18–26 and 35–37.*

- **Kohonen self-organizing maps** represent a high-dimensional input distribution through grid-organized prototype vectors. The best matching unit minimizes input-to-prototype distance; winner and neighboring prototypes move toward the sample with learning-rate and neighborhood modulation, `w_r ← w_r+ε h(r,s,t)(v−w_r)`.
- Neighborhood width controls the extent of cooperative adaptation, linking competitive winner selection with topological organization. Frequent regions obtain finer representational coverage. The displayed “Gaussian” on p. 9 lacks a squared distance in its numerator; no silently repaired exact kernel is asserted here.
- **Success–failure learning** maintains separate maps of successful and failed motor-controller parameter vectors. Candidate vectors are evaluated by distances to both maps, accepted/rejected before robot trials, and added to the appropriate training set after observing outcome. Failure memory avoids repeatedly testing known bad regions.
- A **vigilance threshold** adjusts risk-taking versus risk-averse go/no-go decisions. Illustrations learn slope/sigmoid parameters of a hip-extensor sensory neuron and adapt a neural sensorimotor walking controller; a displayed sigmoid maps sensed angle through gain/threshold parameters.
- **Qualitative Adaptive Reward Learning (QARL)** augments success/failure with action quality and vigilance modulation. A reward factor scales SOM adaptation; walking-efficiency examples compare useful displacement and actuator energy. Distinguish avoiding failure from optimizing quality among successful behaviors.
- Anterior-cingulate error prediction and risk-taking studies motivate the architecture. These are embodied learning examples without a demonstrated universal safety or convergence guarantee.

### Distributional reward coding: documented student presentation

*Evidence: [P], physical pp. 1–11; [DP], pp. 2–4, Figures 1 and 4.*

- The presentation **A Distributional Code for Value in Dopamine-Based Reinforcement Learning**, attributed to Pablo Yeste Blesa, discusses Dabney et al. (Nature, 2020). It contrasts a scalar expected-return prediction with a population representing a reward/value distribution. This is evidence of the presentation topic, not authorship of the underlying research.
- Asymmetric positive/negative reward-prediction-error scaling (`α+` versus `α−`) produces optimistic/pessimistic value channels. With approximately linear response on each side, learned predictions relate to **expectiles**; the asymmetry ratio `α+/(α++α−)` indexes differing channels.
- Expectiles generalize the mean, whereas quantiles generalize the median; they should not be conflated. Reversal points identify rewards at which responses change sign. A set of reversal points plus asymmetries supports approximate decoding of outcome distributions.
- Variable-reward-magnitude and variable-reward-probability tasks test diversity in VTA dopaminergic/GABAergic responses. Repeated-trial consistency and associations between asymmetry and reversal point distinguish a distributional coding hypothesis from simply averaging neuronal noise.
- The supplied presentation summarizes published experimental findings and implications; no local neural-recording experiment, distributional-RL software implementation or original result is claimed.

## Computational methods, tools, and lab evidence

*Evidence: [T1–T5], [RT1], [C1–C5].*

- **ROS 2:** workspaces/packages, Python `rclpy` nodes, messages/topics, publisher–subscriber communication, request–response services and long-running action concepts. **Ament**, `ament_python`, `ament_cmake`, **colcon**, CMake target/dependency/install configuration, `package.xml`, `setup.py` console entry points and sourcing the installed workspace constitute the development workflow. C++ is covered in build examples/prerequisites; the substantive supplied lab logic is Python, not an independently established C++ application.
- **Robot interfaces:** joint-position commands, lock/unlock services, custom servo messages/services, `sensor_msgs/JointState`, compressed camera images and camera calibration metadata. Timers/subscriptions separate sensing and control; `rqt_graph`, RViz2 and **PlotJuggler** support visualization/inspection. Library imports and package dependency declarations are explicit exercises.
- **OpenCV perception:** decode compressed image bytes through NumPy and `cv2.imdecode`, convert BGR to HSV, threshold color ranges, find external contours, select the largest blob and compute its centroid from image moments. ArUco identification later supplies keeper/post pixel coordinates. The code's camera intrinsics are logged, not evidence of a complete calibrated 3D reconstruction.
- **Visual–motor regression:** collect synchronized marker coordinates and shoulder angles during manual guidance; normalize inputs/outputs, train a predictor and denormalize joint outputs. Fixed head/elbow and ignored depth constrain the learned map to the chosen setup, not general inverse kinematics.
- **MLP from scratch:** NumPy affine layers, sigmoid/tanh/ReLU/leaky-ReLU, softmax classification versus linear regression output, cross-entropy/MSE, chain-rule backpropagation, biases, random scaled initialization, shuffled mini-batch SGD and train/validation curves. MNIST digit classification precedes a 2D-to-2D reaching regressor. Template notebook cells 14–62 and submitted methods `forward`, `backprop`, `update_batch`, `train` document the mechanics.
- **Python ecosystem:** NumPy, Matplotlib, Jupyter, pandas, seaborn, python-mnist, scikit-learn and OpenCV appear in relevant teaching or submission files. VS Code is suggested; MATLAB and C/C++ are introductory prerequisites, not proof of their use in the supplied solutions.
- Local submission data contain 62 MLP examples and 154 CMAC examples (excluding headers), alongside model NPZ files and images. Task specifications request approximate/different sample counts, so required and supplied counts are distinguished. The RL CSV has 38 numbered rows and a duplicate header; despite its name, it contains per-episode reward totals rather than a running cumulative sum. No reproducible performance comparison is inferred from these artifacts alone.
- The Team E CMAC/FFNN comparison explicitly lists Pablo Yeste Blesa among five authors. It reports qualitative advantages of faster CMAC learning versus FFNN generalization, but does not isolate individual coding contributions or establish controlled universal performance rankings. No claim of sole implementation is made.

## Coverage validation and limitations

- Lecture 1 motivation, Lecture 2 learning/coordination, Lecture 3 cerebellar/internal-model control, Lecture 4 CMAC, Lecture 5 basal ganglia, both Lecture 6 parts and Lecture 7 SOM/success–failure/QARL are all represented. Five tutorial sequences, their templates/submissions and the supplied named presentation contribute additional evidence rather than being ignored after lecture extraction.
- Text extraction loses embedded equations and circuit/flow-diagram relations. Thirty-four rendered pages recovered CMAC update formulas, policy/TD algorithms, distributional coding figures, circuit signs and success/failure/vigilance flow. Repeated diagram builds were consolidated; not every physical page was separately rendered.
- The introduction advertises nine lectures/eight tutorials on one slide but five tutorials on another. Locally only Lectures 1–7 and Tutorials 1–5 are supplied; additional sessions cannot be inferred or reconstructed. No oral-exam questions or full set of student presentations is present.
- Tutorial files mix SS2025 labels with 2023/2024 deadlines and 2019 lecture filenames. Current robot materials emphasize AiNex while older wording names NAO. The profile captures the accessible material, not an invented exact session-by-session historical schedule.
- The MLP submission uses z-score standardization where the task requests [0,1] scaling, and several scripts disagree on output normalization/model paths. The notebook has placeholder/demo code and derivative-label typos. Tutorial 4 inference imports an absent `ainex_inference.mlp` module. These sources are not treated as turnkey tested software.
- CMAC sum/average and activation-count conventions differ between slides and code; the adjusted RL planner has the incomplete-sweep defect described above. Hardcoded machine paths, build/install artifacts, binary models/pickles and video evidence limit reproducibility. Binary models were not loaded, and robot/API/code execution was out of scope.
- Offered paper collections remain background opportunities; their complete mathematical content is not attributed to taught or personally presented knowledge without corresponding evidence. The 251-page dissertation is a supplied reference, not 251 pages asserted as delivered syllabus.

## Thematic categories

- Dynamical systems and robotics.
- Control theory and adaptive motor control.
- Machine learning and artificial intelligence.
- Reinforcement learning and sequential decision-making.
- Computational neuroscience and biologically inspired computation.
- Scientific computing and robot software integration.

## Source register

All paths below are members of the primary ZIP. `::` indicates a member inside a nested package. Directory prefixes are defined once for readable, unambiguous references.

| ID | Exact member | Pages |
|---|---|---:|
| L1 | `24. April - 30. April/BILHR L1.pdf` | 33 |
| L2 | `1. Mai - 7. Mai/BILHR L2.pdf` | 28 |
| L3 | `8. Mai - 14. Mai/BILHR L3.pdf` | 45 |
| L4 | `22. Mai - 28. Mai/BILHR L4.pdf` | 55 |
| L5 | `12. Juni - 18. Juni/BILHR2019SS L5.pdf` | 44 |
| L6a | `19. Juni - 25. Juni/Lecture 6_part1.pdf` | 24 |
| L6b | `26. Juni - 2. Juli/Lecture 6 _ part2.pdf` | 73 |
| L7 | `10. Juli - 16. Juli/Lecture 7.pdf` | 39 |
| SC | `29. Mai - 4. Juni/BILHR2019SS L4 sup.pdf` | 1 |
| SB | `19. Juni - 25. Juni/BILHR2019SS L5 2.pdf` | 1 |
| T1 | `8. Mai - 14. Mai/BILHR T1/BILHR T1.pdf` | 12 |
| RT1 | `8. Mai - 14. Mai/BILHR T1/T1 ROS2 Introduction.pdf` | 23 |
| T2 | `15. Mai - 21. Mai/BILHR T2/intro/tutorial_2_SS25.pdf` | 3 |
| T2H | `15. Mai - 21. Mai/BILHR T2/intro/T2 AiNex Robot Hands-on.pdf` | 4 |
| T3 | `29. Mai - 4. Juni/Tutorial 3 Feed Forward Neural Network/intro/tutorial_3_SS24.pdf` | 1 |
| T4 | `5. Juni - 11. Juni/Tutorial 4 CMAC/intro/tutorial_4_SS25.pdf` | 1 |
| TP | `5. Juni - 11. Juni/Tutorial 4 CMAC/intro/CMAC_neuron_pos.pdf` | 1 |
| T5 | `26. Juni - 2. Juli/Tutorial 5 Reinforcement Learning/intro/tutorial_5_SS25.pdf` | 1 |
| TS5 | `26. Juni - 2. Juli/Tutorial 5 Reinforcement Learning/intro/tutorial_5_slides_SS25.pdf` | 6 |

Computational packages:

- [C1] `8. Mai - 14. Mai/BILHR T1/T1_solution.zip`; `tutorial_ws/src/t1_pkg/t1_pkg/publisher.py`, `subscriber.py`, library/import examples and package configuration.
- [C2] `15. Mai - 21. Mai/BILHR T2/intro/template.zip`; supplied implementation in `15. Mai - 21. Mai/BILHR T2/Einreichungen/Gruppe Team E/Tut2.zip :: Tut2/template/ainex_bilhr_ws/src/`, notably `ainex_vision/ainex_vision/camera_sub.py` and `ainex_motion/ainex_motion/{joint_controller,joint_visualization_node,keyboard_input_node,ainex_motion_node}.py`.
- [C3] `29. Mai - 4. Juni/Tutorial 3 Feed Forward Neural Network/intro/tutorial_3_1_.tar.xz :: tutorial_3_1_/tutorial_3/Tutorial 4 MLP.ipynb`; implementation in `29. Mai - 4. Juni/Tutorial 3 Feed Forward Neural Network/Einreichungen/Gruppe Team E/tutorial_3_ws.tar.gz :: tutorial_3_ws/`, particularly `mnist_nn/mnist_neural_network.py`, `robot_data_processing.py`, `src/ainex_inference/ainex_inference/neural_network.py`, `inference_blob2joint_node.py` in that same package, and `src/tut3/tut3/data_collection_node.py`.
- [C4] `5. Juni - 11. Juni/Tutorial 4 CMAC/Einreichungen/Gruppe Team E/Assignment4_upload.zip`; `src/ainex_inference/ainex_inference/{cmac,cmac_validation,inference_blob2joint_node}.py`, `data/minmax_normalized_data_tut4.txt`, `BILHR_SS25_TeamE_T4_Task4_CMACvsFFNN.txt` and `README.txt`. Root-level code copies and several model versions are also present.
- [C5] `26. Juni - 2. Juli/Tutorial 5 Reinforcement Learning/Einreichungen/Gruppe Team E/Abgabe_T5.zip :: Abgabe_T5/tutorial_5_ws/`; `src/rl_controller/rl_controller/{model_based_rl_adj,model_based_rl_old,setup_node,data_viz}.py`, `src/ainex_vision/ainex_vision/aruco_detect.py`, and `cumulative_rewards.csv`.

Assigned RL readings under `26. Juni - 2. Juli/Tutorial 5 Reinforcement Learning/intro/`:

- [RD1] `Generalized model learning for ___arning in factored domains.pdf`, 8 pages: Hester and Stone, RL-DT algorithm and model factorization.
- [RD2] `Generalized Model Learning for ___arning on a Humanoid Robot.pdf`, 6 pages: Hester, Quinlan and Stone, robot-soccer adaptation.
- [RE] `Reinforcement Learning Examples.pdf`, 6 pages: passive ADP/TD and active Q-learning worked examples.

Student presentation and supporting paper:

- [P] `10. Juli - 16. Juli/Students Presentation Session B - slides submission/Einreichungen/Pablo Yeste Blesa/Presentation_Template___LDV___T___iversity_of_Munich__TUM_-5.pdf`, 12 pages.
- [DP] `10. Juli - 16. Juli/Paper for students presentation Session B on 17.07.2025/B - A distributional code for v___sed reinforcement learning.pdf`, 21 pages; main article versus extended data are distinguished.

Background references, used for provenance/topic scope rather than claiming complete taught coverage:

- [RC] `22. Mai - 28. Mai/Roles of the Cerebellum in Motor Control 20212.pdf`, 56 pages.
- [RN] `22. Mai - 28. Mai/62 Neurorobotics From Vision to Action.pdf`, 28 pages.
- [RB] `12. Juni - 18. Juni/Basal ganglia subcircuits disti___ation of action sequences 2014.pdf` (12 pages), `Computational models of basal-g___n functional neuroanatomy 2013.pdf` (18 pages) and extensionless PDF `Working together.. basal gangli___in action selection friend2014` (3 pages), all in that date directory.
- `5. Juni - 11. Juni/Tutorial 4 CMAC/intro/Intelligent Motion Control with an Artificial Cerebellum.pdf`, 251 pages; CMAC reference dissertation.
- `3. Juli - 9. Juli/A Neural Substrate of Prediction and Reward.pdf`, 8 pages, also repeated in the Session B paper collection.
- Other papers are retained under `10. Juli - 16. Juli/Paper for students presentation Session A  on 15.07.2025/` and `10. Juli - 16. Juli/Paper for students presentation Session B on 17.07.2025/`; offered reading is not equivalent to evidence of each presentation's delivery.

Regenerable evidence: `.cache/ei7263/evidence_manifest.json`, `text/`, `nested/`, `nested_text/` and `rendered/`. The original archive is the stable source; generated cache paths are not required to preserve the profile's citations.
