---
id: "population-dynamics-neural-memory"
title: "Population electrophysiology, attractor representations and memory"
domains:
  - "computational-neuroscience"
  - "dynamical-systems"
  - "robotics-planning-geometry"
evidence_refs:
  - "ei7646:population-memory"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "spiking-neuron-plasticity"
---

# Population electrophysiology, attractor representations and memory

## Signals, sources and inverse interpretation

Wideband extracellular recordings separate fast spike waveforms from slower LFPs. Tetrodes/silicon probes combine waveform morphology with stable spatial amplitude patterns for spike sorting. In a homogeneous conductor, the illustrated point-current forward model is
\[
V=I/(4\pi R\sigma_e).
\]
LFPs superpose transmembrane sources/sinks with synaptic, polarization, laminar and summation effects; they are not a direct isolated-neuron readout.

CSD infers sources through the negative spatial Laplacian of voltage scaled by conductivity under the volume-conductor assumptions. Laminar/2-D sampling and geometry affect that inverse interpretation. Spike sorting, field potentials and source localization therefore answer different questions from merely finding correlated channels.

## Attractors and spatial reference frames

Place fields support position decoding; place/head-direction/grid cells encode different spatial variables. Continuous attractors include heading rings and spatial manifolds. Remapping, multisensory cues, virtual reality and behavioral measurements expose dependence on environment/reference frame.

Recurrent autoassociative assemblies offer a retrieval mechanism through Hebbian organization. The hippocampus supports allocentric navigation/path integration and episodic/semantic/new-memory context; the HM lesion example and Marr's intermediate storage/consolidation account are hypotheses/evidence about function, not a single fully implemented memory algorithm.

## Temporal organization and causal testing

Intrinsic resonance, connectivity and inhibitory interneurons contribute to oscillations. Theta/gamma organization, layer generators and cross-frequency coupling reveal multiple circuit scales. Theta phase precession relates firing phase to position; theta sequences compress spatial order. Sharp-wave/ripple forward/reverse replay during rest/sleep compresses experienced sequences.

Cortical slow UP/DOWN states, spindles and hippocampal–neocortical coordination support systems-consolidation hypotheses. Closed-loop ripple interruption/enhancement provides intervention evidence distinct from correlational observation. That conceptual connection to [causal inference](causal-graphical-models.md) does not claim the experiments implemented a specific causal-discovery algorithm.

[Nonlinear dynamical systems](dynamical-flows-bifurcations.md) supplies a general language for stable patterns, not proof that all biological attractors satisfy every taught stability theorem. [Information/population codes](information-coding-sensory-inference.md) explains decoding, while [cognitive architectures](cognitive-architectures-binding.md) organizes symbolic memory at another abstraction level. Replay here is biological sequence reactivation, not a DQN replay-buffer implementation.

[EI7646 population-memory evidence](../evidence/ei7646.yaml) preserves the complete late systems-neuroscience sequence and the distinction between modeling knowledge and personal recording/decoding experiments. Demonstration videos were not transcribed in the source profile; narrated material is not newly inferred.
