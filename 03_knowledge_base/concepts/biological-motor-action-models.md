---
id: "biological-motor-action-models"
title: "Biological motor representations, internal models and action selection"
domains:
  - "computational-neuroscience"
  - "robotics-planning-geometry"
  - "control-estimation"
  - "machine-learning"
evidence_refs:
  - "ei7263:embodied-circuits"
  - "ei7646:probabilistic-perception"
  - "additional-cognitive-systems:embodied-platform"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "distributional-value-coding"
  -
    type: "related_to"
    target: "impedance-contact-dynamics"
  -
    type: "related_to"
    target: "local-adaptive-function-approximation"
---


# Biological motor representations, internal models and action selection

## Embodied learning and coordinated prediction

Motor babbling correlates exploratory joint movements with visual/proprioceptive feedback to learn body, inverse and reachable-space mappings. Task/joint/latent representations define different learning problems; changing loads/contact make nominal models insufficient. Demonstration-based examples combine PCA/Gaussian mixture regression at framework level. Drawing uses CPG patterns, locally optimized coordination, SOM workspace representation and inverse-distance transfer; a GA initialization label does not supply a full genetic algorithm.

Schema theory separates perceptual, motor and coordinating modules without one-to-one anatomical localization. Reach/grasp coordinates transport, preshaping and tactile closure with perturbation feedback. Forward models predict sensory consequences of commands; inverse models seek commands from desired outcomes. Efference copy/corollary discharge and reafferent feedback support prediction-error computation and grip-force adaptation. Predictive augmentation addresses sensorimotor delays; the source's motivation does not prove that delayed feedback is universally impossible.

## Cerebellar coding and adaptation

Cerebro-, spino- and vestibulocerebellar functions, dentate/interposed/fastigial nuclei, peduncles and somatotopy situate coordination. Granule/Purkinje/molecular layers contain granule, Purkinje, Golgi, basket and stellate cells. Mossy/parallel fibers convey context; climbing fibers from inferior olive supply a modeled teaching signal. Purkinje inhibition of deep nuclei shapes a deep excitatory pathway; circuit signs matter.

Marr–Albus associative recoding expands overlapping contexts into sparser granule codes, limiting interference/saturation. Golgi regulation and basket/stellate threshold/lateral effects complement this view. Simple/complex spikes, parallel/climbing coincidence and LTP/LTD motivate synaptic adaptation; adaptive-filter and timing interpretations are not identical models. [CMAC](local-adaptive-function-approximation.md) is a computational abstraction of local recoding, not proof of exhaustive biological equivalence.

## Basal ganglia and action organization

Striatum, GPe/GPi, STN and substantia nigra pars reticulata/compacta form cortico–basal-ganglia–thalamo–cortical loops. In the simplified direct pathway, striatal inhibition reduces GPi/SNr output inhibition and disinhibits thalamocortical activity. The indirect pathway inhibits GPe, disinhibits STN and increases GPi/SNr inhibition; D1/D2 modulation motivates opposing influences. Initiation, switching and chunking need coordinated pathways, not a simple independent on/off pair.

Motor/prefrontal/limbic loops and reciprocal/nonreciprocal connections organize specialization and integration. Optogenetic/electrophysiological studies probe pathway roles; all-pathway stimulation differs from physiological action coding. Selection, gating, working memory, procedural learning and dimensionality reduction remain hypotheses rather than one proven complete theory. Dopaminergic prediction errors connect to RL; lesion/Parkinson/Huntington examples are functional context, not medical guidance or personal experiments.

Evidence: `ei7263:embodied-circuits` in [humanoid evidence](../evidence/ei7263.yaml). Locomotion, drawing and grasping are teaching/research examples; only the separately named distributional-value presentation and collaborative comparison have their explicit personal/team artifact attribution.

## Sensory inference and rhythmic motor structure

Neuroscience adds perception as an ill-posed inverse problem, environmental priors and uncertain sensory/motor evidence, with hierarchical predictive-coding hypotheses. [Information/sensory inference](information-coding-sensory-inference.md) develops this normative account; it does not identify one unique biological mechanism or provide the absent blackboard derivation.

Cognitive Systems' half-center CPG circuitry supplies a different motor primitive: rhythmic opposing excitation/inhibition under drive and optional feedback, coupled to a simulated body. This extends earlier locomotion/drawing examples while preserving the distinction between a generative rhythm, an internal forward/inverse model and an optimized trajectory. Complete NRP experiments and personal gait implementation are not established.
