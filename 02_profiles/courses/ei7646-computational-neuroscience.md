# Computational Neuroscience: A Lecture Series from Models to Applications

## Academic identity and evidence scope

- **Module:** EI7646; **credits:** 3 ECTS; **grade:** 2.0; degree module, transcript PDF p. 3.
- **Stable identifier:** `ei7646`.
- **Teaching source:** `00_sources/tum/archives/Computational N 950766500 (W24_25)_20261012_1552.zip` (WS 2024/25). Source paths below are members of this archive; page references are physical PDF pages, not necessarily printed slide numbers.
- **Coverage:** 12 lecture decks (599 pages), three one-page self-assessment/takeaway documents, a six-page systems-neuroscience study guide, and an 11-page historical sample examination: 17 PDFs / 619 pages altogether. Two lecture PDFs have no filename extension. Eight MP4 demonstrations and an HTML index are also present. Videos were inventoried, not transcribed; their narrated content is outside the recovered evidence.
- **Processing:** complete lecture-sequence text/structure inspection, complementary assessment inspection, and targeted rendering of mathematical, circuit, signal-flow and experimental figures. No programming assignments, solution sets, or executable course code were found. This is a conceptual/modeling and experimental-methods course, not evidence of personal implementation or experimental results.

## Technical knowledge

### Modeling levels, neural representations, and spatial decoding

*Evidence: [L1], pp. 1–32 and 33–49; [L6], pp. 4–8.*

- Computational neuroscience connects experiments to models across spatial and temporal scales: membrane/ion-channel biophysics, single neurons, synaptic interactions, circuits, populations and behavior. Model selection balances physiological detail with tractable abstraction; the introductory comparison includes Hodgkin–Huxley, Tsodyks–Markram synaptic dynamics and Izhikevich-type spiking models, without deriving every named model.
- Mathematical models as predictive and falsifiable explanations rather than collections of fitted descriptions; missing data and predictive neuroinformatics in large-scale brain modeling.
- **Marr's levels:** the computational problem and objective, representation/algorithm, and physical implementation. These levels separate a normative account of behavior from a particular neural mechanism.
- **Grid-cell spatial coding:** periodic firing patterns; modules with common orientation and spatial scale but differing spatial phase; ambiguity of any single periodic module; combining modules with different spatial scales to improve position representation.
- Population-vector and **maximum-likelihood decoding** of population responses; von Mises-type periodic tuning curves, dependence on firing-rate peak and tuning width, and likelihood combination across cells/modules. The introductory tuning display uses `Ω_j(x)=n_max exp(k[cos(2π(x−c_j)/λ_j)−1])`.
- Scale selection and the range–resolution trade-off: decoding-error plots compare module scale ratios and show catastrophic aliasing when separation becomes too large in the particular model studied. The displayed recommendation below approximately 1.5 is a model-specific result, not a universal theorem about grid cells.
- Two-dimensional grid alignment and goal-directed navigation as applications of population codes.

### Anatomical and cellular foundations

*Evidence: [L2], pp. 1–29; [A1]; [L3], pp. 1–36; [A2].*

- Vertebrate nervous-system organization: forebrain, midbrain and hindbrain; gray/white matter, nuclei and tracts; cortical lobes, gyri/sulci and six-layer organization. Cortical columns, pyramidal neurons, interneurons and glia; axons, dendrites and spines; afferent sensory pathways and spinal organization.
- Hearing: outer/middle/inner ear, cochlear mechanics and basilar-membrane tonotopy, hair-cell transduction and ascending pathways. Vision: rods/cones, fovea, retinal circuitry and dorsal/ventral cortical processing streams.
- Membrane capacitance and resistance, electrochemical ion gradients, sodium–potassium pumping, and voltage-, ligand- and mechanically gated channels. **Nernst equilibrium potential** for an ion and **Goldman–Hodgkin–Katz** permeability-based resting potential distinguish single-ion equilibrium from a multi-ion membrane.
- Action-potential initiation and propagation: sodium activation/inactivation, potassium-mediated repolarization, refractoriness, all-or-none spikes versus graded potentials, passive electrotonic attenuation, myelination and saltatory conduction at nodes of Ranvier.
- Chemical and electrical synapses; neuromuscular acetylcholine example; excitatory/inhibitory postsynaptic effects depend on receptor and reversal potential. **Shunting inhibition** increases membrane conductance and reduces responses rather than acting as a simple additive negative voltage.
- Dendritic computation and spines: electrical and biochemical compartmentalization, calcium signaling, active dendritic channels, amplification and back-propagating action potentials relevant to plasticity.

### Information theory, efficient coding, and active sensing

*Evidence: [L4], pp. 15–23, 25–40, 42–54 and 56–63; formulas and major plots checked visually.*

- Shannon uncertainty axioms and **entropy** `H(R)=−Σ_r p(r)log₂p(r)`. **Mutual information** compares joint stimulus–response probability with the product of marginals: `I(S;R)=Σ_s,r p(s,r)log₂[p(s,r)/(p(s)p(r))]`. It detects dependencies that Pearson correlation can miss, including nonlinear relationships.
- Neural responses as communication channels: stimulus variability, response noise, repeated trials, rate coding versus precise spike timing, binary response words, and temporal-bin choice. Finer temporal resolution may expose information hidden by coarse rate summaries; plotted estimates depend on the response representation and experimental data.
- **Efficient-coding hypothesis:** representation adapted to environmental statistics under response/noise constraints. The Laughlin example relates a nonlinear input–output response to the cumulative stimulus distribution, approximately equalizing response use.
- Adaptation to changing stimulus statistics in the blowfly H1 motion system; sensory ecology and natural versus artificial acoustic stimuli; information efficiency `I(R;S)/H(R)`.
- **Sparse coding of natural image patches:** learned localized, oriented receptive fields compared with primary visual-cortex receptive fields (Olshausen–Field example). The evidence establishes the coding principle and empirical comparison, not a fully specified optimization implementation.
- Active information acquisition: odor transport in turbulent plumes, moth search, **infotaxis** as entropy-reducing search under uncertain source location, and nematode foraging. These are biological examples of information-guided behavior, not convergence guarantees for an optimization method.

### Development, Hebbian learning, and synaptic plasticity

*Evidence: [L5], pp. 1–17, 18–24 and 25–47; [A3].*

- Circuit development combines molecular/innate mechanisms with activity-dependent organization, including structured spontaneous activity before mature sensory experience.
- Rate-based **Hebbian plasticity** averages products of pre- and postsynaptic activity. With linear postsynaptic rate and a separation between fast neuronal and slow weight time scales, correlation learning gives `τ_w ẇ=Cw`, with `C=⟨ρρᵀ⟩`; mean-centered **covariance learning** gives `τ_w ẇ=Qw`.
- Eigenstructure links weight growth/selectivity to input statistics, but unconstrained Hebbian/covariance dynamics are unstable. Hard bounds, subtractive normalization and divisive normalization constrain growth. Subtractive normalization promotes strong competition; weight-proportional normalization preserves graded representations of correlated inputs.
- **Long-term potentiation/depression (LTP/LTD):** dependence on firing statistics and stimulation protocol. **Spike-timing-dependent plasticity (STDP)** depends on pre/post ordering: an asymmetric, approximately exponential window potentiates causal pre-before-post pairs and depresses the opposite ordering, with separate amplitudes and time constants.
- Pair-based STDP is insufficient for some frequency/burst effects; **triplet STDP** (Pfister–Gerstner example) and **burst-timing-dependent plasticity** extend the phenomenology. Distinguish empirical plasticity windows from voltage-dependent and calcium-based biophysical explanations.
- Trace-based event-driven modeling: presynaptic and postsynaptic traces decay exponentially, are changed at spikes, and determine weight changes at spikes of the opposite neuron. Weight bounds matter. The last slide's displayed upper-bound formula uses `max` despite prose specifying an upper bound; it is not adopted as a verified implementation equation.

### Probabilistic perception and sensorimotor inference

*Evidence: [L6], pp. 9–30, 31–42 and 43–51; visually inspected inverse-problem and hierarchy figures.*

- Perception is an ill-posed inverse problem: a sensory image can arise from multiple three-dimensional scenes. Internal/generative models describe how latent causes generate observations; inference combines sensory likelihood with prior environmental knowledge.
- **Bayesian inference:** prior, likelihood and posterior as distinct quantities; uncertainty-aware explanations of perceptual judgments, including sound localization and visual interpretation. Examples include neural representations of uncertainty and fly heading.
- Natural-scene statistics shape perceptual priors. Motor-control experiments combine prior movement information with uncertain visual feedback; behavior is compared with probabilistic internal-model predictions, not asserted universally optimal.
- **Hierarchical Bayesian/predictive-coding accounts:** successive visual areas represent increasingly complex features and larger receptive fields; generative feedback and sensory evidence support inference. Hierarchical feature-learning and filling-in examples illustrate these hypotheses.
- A slide explicitly reserves a Bayesian derivation for the blackboard. No blackboard notes are supplied, so the derivation and any unstated implementation details cannot be recovered from the deck.

### Bioelectronic interfaces and cell–chip communication

*Evidence: [L7], pp. 1–31, 32–50, 51–86 and 87–100; equivalent circuits, noise and mass-transport figures checked visually.*

- Organ-on-chip and neural/cardiac culture interfaces; intracellular patch clamp, planar patch clamp, extracellular **microelectrode arrays (MEAs)**, field-effect-transistor sensing and high-density CMOS arrays. Measurement choices trade invasiveness, spatial sampling, signal amplitude and culture compatibility.
- **Hodgkin–Huxley equivalent circuit:** membrane capacitance in parallel with leak and voltage/time-dependent sodium and potassium conductances. Kirchhoff current balance includes capacitive current and ionic currents `g_i(V_m−E_i)`; reversal potentials act as batteries.
- Cell–electrode coupling depends on the cell–substrate cleft, seal/junction impedance, electrode impedance and leakage into recording electronics. The simplified interface has solution resistance in series with parallel interface capacitance and resistance: `Z=R_s+(1/R_i+iωC_i)⁻¹`.
- Electrode material, effective area and geometry control impedance. Platinum black, iridium oxide, carbon nanotubes and nanopatterned/porous gold are discussed. **Johnson noise** is related to the real part of impedance/admittance; the resistor example gives voltage-noise variance `4kTRΔf`.
- Mechanical mismatch between rigid silicon devices and soft tissue motivates flexible/stretchable polymers, parylene, PEDOT:PSS, organic transistors, and inkjet-printed carbon/gold interfaces. Guided culture, microcontact-patterned PDMS, organoids and three-dimensional/kirigami electrode interfaces address tissue organization and 3-D sampling.
- Electrohydrodynamic fabrication of three-dimensional microelectrodes, passivation and electrochemical characterization; flexible peripheral nerve cuffs as a bioelectronic-medicine example. These are lecture examples, not evidence of fabrication experience.
- **Electrochemical neurotransmitter sensing:** dopamine oxidation/reduction, carbon-fiber electrodes and amperometric multichannel recording; diffusion, migration and convection as transport mechanisms. Diffusion equations for oxidized/reduced species and a perfectly absorbing electrode assumption connect geometry to measured current.
- **Cottrell** planar-electrode current decays as `t⁻¹ᐟ²`; the **Shoup–Szabo** microelectrode comparison introduces radial transport and nonzero steady current. Local release, uptake and pharmacological perturbations are illustrated; charge integration of release events supports quantification.

### Neuroprostheses and neural stimulation

*Evidence: [L9], pp. 1–32; [L10], pp. 1–16 and 17–27.*

- Sensory, motor and modulatory interfaces: cochlear/retinal prostheses, vestibular and tactile stimulation, functional electrical stimulation, deep-brain/spinal stimulation, invasive/noninvasive brain–computer interfaces, EEG and intracortical arrays. Transcranial magnetic/electrical stimulation and optogenetics are compared as intervention modalities.
- Extracellular electrical stimulation of myelinated axons: compartmental cable circuits, intracellular/extracellular potentials and `V_m=V_i−V_e`. A point electrode in a homogeneous volume conductor gives potential proportional to `ρI/(4πr)`.
- The **activating function** is proportional to the second spatial derivative of extracellular potential along the axon. Electrode polarity, trajectory, boundaries and field curvature therefore matter; a spatially uniform potential or constant field is not equivalent to a localized activating profile.
- **Optogenetics:** channelrhodopsin ChR2, a four-state open/closed transition diagram, optical attenuation, fiber/LED illumination and kinetic/energy/selectivity constraints. Optical cochlear stimulation and nerve regeneration are examples, not a claim of clinical efficacy.

### Cochlear implant coding and auditory-nerve models

*Evidence: [L8], pp. 1–14, 15–36 and 37–56; pp. 15, 24, 26 and 34 checked visually.*

- Cochlear damage, lost hair-cell amplification/compression and tonotopic electrode placement motivate multichannel electrical coding. Contrast feature-extraction schemes (F0/formant/MPEAK) with waveform strategies: compressed analog, **continuous interleaved sampling (CIS)**, **ACE**, and **FS4** temporal coding.
- CIS processing chain: automatic gain control, band-pass filter bank, envelope extraction, compression and pulse mapping to electrodes; sequential/interleaved channels reduce electrical interaction. Acoustic envelopes versus temporal fine structure and noise/sine vocoders clarify which cues survive processing.
- Monopolar/bipolar stimulation and current spread; firing probability as a function of current amplitude and pulse duration; strength–duration behavior and pulse-train adaptation.
- **Stochastic leaky integrate-and-fire model:** current integration on a capacitor, resistive leak, noisy threshold and post-spike reset. It reproduces single-pulse firing-probability and threshold-versus-duration curves in the illustrated auditory-nerve example.
- Temporal integration and loudness growth, electrical dynamic range, rate discrimination, place pitch and current steering. Fitting maps acoustic levels between electrical threshold and comfortable levels through compression/AGC; evoked compound responses support device assessment.
- Speech recognition and speech-in-noise testing; bilateral localization using **interaural time differences (ITDs)** and **interaural level differences (ILDs)**, envelope/fine-structure distinctions, reverberation and diffuse noise. Independent ear compression can distort ILDs; high stimulation rates useful for envelope/speech representation can conflict with low-rate temporal-cue benefits.

### Systems electrophysiology, attractor dynamics, and memory

*Evidence: [L11], pp. 1–24, 25–34 and 35–49; [L12], pp. 1–24, 25–39 and 40–57; [A4], pp. 2–6.*

- Hippocampal roles in allocentric navigation, path integration, episodic/semantic memory and new-memory formation; the HM lesion example and **Marr's intermediate-storage/consolidation account**. Hebbian plasticity connects correlated experience to assembly formation; recurrent autoassociative/attractor networks provide a retrieval mechanism.
- Extracellular wideband recording separates fast spike waveforms from slower **local field potentials (LFPs)**. Tetrodes and silicon probes exploit waveform morphology and stable spatial amplitude patterns for **spike sorting**. A point-current-source forward model gives `V=I/(4πRσ_e)` in a homogeneous conductor.
- Population place-field maps permit decoding of animal location. Place, head-direction and grid cells represent different spatial variables; continuous attractors include a ring for heading and spatial manifolds for location. Environment-dependent **remapping**, multisensory cues, virtual reality and behavioral measurements link neural activity to reference frames and flexible memory.
- LFPs reflect superposed transmembrane sources/sinks, strongly influenced by synaptic inputs, neuronal polarization, layer geometry and spatial/temporal summation. **Current-source-density (CSD)** analysis is an inverse model using the negative spatial Laplacian of voltage, scaled by conductivity under the stated volume-conductor assumptions; laminar/2-D sampling relates sinks/sources to input pathways.
- Oscillations arise through intrinsic resonance, circuit connectivity and inhibitory interneurons. Theta and gamma dynamics have different spatial/temporal organization; layer-specific theta generators and cross-frequency coupling reveal interacting circuits.
- **Theta phase precession** relates place-cell spike phase to position within a field; theta sequences compress spatial order. Behavioral state changes population dynamics; **sharp-wave/ripple replay** during rest/sleep compresses experienced sequences, including forward/reverse replay.
- Neocortical slow UP/DOWN dynamics, spindles and hippocampal–neocortical coordination support systems-consolidation hypotheses. Closed-loop ripple-triggered interruption/enhancement provides causal tests, distinguishing intervention evidence from mere correlation.

## Tools, applications, and thematic categories

The course documents experimental technologies (patch clamp, MEA/CMOS/FET interfaces, tetrodes and silicon probes, EEG, stimulation and optogenetics), modeling formalisms and signal-processing methods. No particular programming language/library or student computational project is evidenced. Applications span spatial navigation, neural coding, sensory adaptation, motor inference, auditory prostheses, bioelectronic sensing, neural interfaces and memory research.

**Categories:** computational neuroscience; mathematical modeling; dynamical systems; probabilistic inference; information theory; machine learning; signal processing; biomedical engineering; sensors and neural interfaces.

## Source register and validation

All references below are archive-member paths. The original ZIP remains authoritative; regenerable extracted sources, text/page maps, manifest and rendered figures are under `.cache/ei7646/`, prepared by `scripts/prepare_course_materials.py`.

- **[L1]** `15. Oktober - 21. Oktober/Computational Neuroscience – an Introduction.pdf` — 52 pp.
- **[L2]** `22. Oktober - 28. Oktober/2. lecture neuroanatomy primer` — PDF, 29 pp.
- **[L3]** `29. Oktober - 4. November/3. lecture neurophysiology primer` — PDF, 36 pp.
- **[L4]** `5. November - 11. November/(Information) theory in (neuro) biology.pdf` — 63 pp.
- **[L5]** `12. November - 18. November/Plasticity and development of neural circuits.pdf` — 47 pp.
- **[L6]** `19. November - 25. November/Probabilistic inference in the brain.pdf` — 51 pp.
- **[L7]** `26. November - 2. Dezember/Cell-Chip communication.pdf` — 100 pp.
- **[L8]** `10. Dezember - 16. Dezember/Cochlear Implants.pdf` — 56 pp.
- **[L9]** `7. Januar - 13. Januar/Overview Neuroprostheses.pdf` — 32 pp.
- **[L10]** `7. Januar - 13. Januar/Electrical Stimulations of Neurons.pdf` — 27 pp.
- **[L11]** `21. Januar - 27. Januar/Systems Electrophysiology Slides of Lecture 1.pdf` — 49 pp.
- **[L12]** `28. Januar - 3. Februar/Systems Electrophysiology Slides of Lecture 2.pdf` — 57 pp.
- **[A1]** `22. Oktober - 28. Oktober/Self-Assessment Neuroanatomy.pdf` — 1 p.
- **[A2]** `29. Oktober - 4. November/Self-Assessment Neurophysiology.pdf` — 1 p.
- **[A3]** `12. November - 18. November/What you should know.pdf` — 1 p.
- **[A4]** `28. Januar - 3. Februar/Study topicsquestions.pdf` — 6 pp.
- **[X]** `Allgemeines/Example exam.pdf` — 11 pp., dated 2016. Topics not corroborated by the current lectures were not imported into the profile; no examination solutions supplied.

**Quality review:** all 12 lecture decks mapped to the technical sections above; the late hardware/electrochemistry and systems-neuroscience material is retained rather than reducing the course to neuron models. Self-assessments and final study questions cross-check development/plasticity, spike sorting, CSD, remapping and replay. Fifty-six representative pages were rendered for inspection across the mathematical and diagram-heavy decks. Mathematical displays with extraction loss were checked visually; the apparent bound typo in [L5] and the absent blackboard derivation in [L6] remain explicit. Historical assessment and demonstration videos do not establish additional current syllabus content. No external module description was needed.
