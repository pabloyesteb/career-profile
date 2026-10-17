---
id: "spiking-neuron-plasticity"
title: "Biophysical neuron models, event-driven simulation and plasticity"
domains:
  - "computational-neuroscience"
  - "dynamical-systems"
  - "machine-learning"
evidence_refs:
  - "ei7646:cellular-models"
  - "ei7646:plasticity"
  - "additional-cognitive-systems:spiking-models"
  - "additional-cognitive-systems:plasticity-simulation"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "temporal-difference-learning"
---

# Biophysical neuron models, event-driven simulation and plasticity

## Biological structure and model abstraction

Anatomical context includes central/peripheral organization, fore-/mid-/hindbrain, cortical layers/columns, pyramidal/interneuronal/glial roles, axons/dendrites/spines and afferent pathways. Structural histology/MRI/DTI differs from functional EEG/MEG/PET/SPECT/BOLD-fMRI, especially in indirectness and temporal resolution. Hearing cochlear tonotopy/hair-cell transduction and retinal rods/cones/circuitry situate the cellular models.

Membrane capacitance/resistance, electrochemical gradients, Na/K pumping and gated channels generate resting/action potentials. Nernst single-ion equilibrium differs from Goldman–Hodgkin–Katz multi-ion permeability balance. Na activation/inactivation, K repolarization, refractoriness, myelination/saltatory conduction and graded versus all-or-none responses explain why a spike is not simply an analog activation. Receptor/reversal potentials determine excitation/inhibition; shunting inhibition changes conductance rather than adding a negative voltage. Active dendrites, calcium and backpropagating spikes connect compartmentalization to plasticity.

## Conductance, reset and low-dimensional dynamics

Hodgkin–Huxley models capacitive current plus leak, sodium and potassium currents with reversal-potential terms \(g_i(V_m-E_i)\). Sodium \(m^3h\), potassium \(n^4\) and voltage-dependent gates give the represented four-state system. Morris–Lecar/FitzHugh–Nagumo are named reductions, not fully specified implementations; Tsodyks–Markram is a named synaptic-dynamics example.

LIF uses
\[
C\,dv/dt=I(t)-(v-v_{\rm rest})/R,\qquad\tau=RC,
\]
with threshold/reset. Exercise solutions derive exponential relaxation, threshold crossing and periodic firing under their reset/rest/threshold ordering, deliberately without refractoriness. AdEx adds exponential initiation and a second adaptation state. The Izhikevich notebook specifies
\[
\dot v=0.04v^2+5v+140-u+I,\qquad\dot u=a(bv-u),
\]
with \(v\leftarrow c,\ u\leftarrow u+d\) at threshold. Dimensional/time scaling is part of its simulation contract, not permission to mix these coefficients into physical SI units unchanged.

## Plasticity has its own state and timescale

Rate Hebbian learning with linear postsynaptic response and fast-neuron/slow-weight separation gives \(\tau_w\dot w=Cw\), \(C=\langle\rho\rho^T\rangle\); mean-centered covariance learning uses \(Q\). Eigenstructure selects growing directions, but unconstrained growth is unstable. Hard bounds, subtractive and divisive normalization have different competitive/graded effects.

Cognitive Systems derives Oja's normalized first-order rule
\[
\dot w=Cw-(w^TCw)w
\]
after absorbing timescales, connecting a principal-component direction to [PCA](matrix-low-rank-pca.md), not every nonlinear neural model. BCM uses a sliding activity threshold between LTD/LTP; it is not RL reward optimization.

STDP uses asymmetric pre/post exponential timing windows with separate amplitudes/time constants. Exponentially decaying local traces accumulate preceding spikes and apply weight changes on opposite-neuron spikes without retaining every timestamp. Triplet/burst rules address frequency/burst phenomena that pair timing alone misses. Bounds and biological state matter; the source's upper-bound `max` typo is not adopted. Synaptic traces and RL eligibility traces are related bookkeeping ideas, not identical targets.

## Supplied computational methods

Brian2 expresses differential equations/units, `NeuronGroup` threshold/reset, weighted `Synapses`, monitors and exact-linear/Euler integration. Rate/time-to-first-spike/population/synchrony codes differ; exercises encode scalars/pixels as bounded-frequency periodic trains and spike GIFs. A NEST-labeled two-layer integer-adder slide is not silently identified with the Brian2 notebook.

Analog LIF circuits, memristive/RRAM, SpiNNaker and TrueNorth motivate event-driven energy/latency trade-offs; no personal fabrication or measured hardware advantage is established. Referenced LIF/Oja notebooks are missing, while supplied related notebooks do not replace their exact content.

[EI7646](../evidence/ei7646.yaml) and [Cognitive Systems](../evidence/additional-cognitive-systems.yaml) jointly support these models. The value is theoretical/numerical understanding; source code was inspected previously, not personally attributed or executed here.
