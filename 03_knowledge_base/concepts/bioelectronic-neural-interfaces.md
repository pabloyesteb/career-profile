---
id: "bioelectronic-neural-interfaces"
title: "Neural recording, stimulation and auditory prosthetic interfaces"
domains:
  - "computational-neuroscience"
  - "numerical-mathematics"
evidence_refs:
  - "ei7646:cell-chip"
  - "ei7646:stimulation"
  - "ei7646:auditory-prostheses"
status: "reviewed"
relations:
  -
    type: "related_to"
    target: "population-dynamics-neural-memory"
  -
    type: "related_to"
    target: "spiking-neuron-plasticity"
---

# Neural recording, stimulation and auditory prosthetic interfaces

## Measuring a coupled physical system

Patch/planar clamp, extracellular MEAs, FET sensing and dense CMOS arrays trade invasiveness, spatial sampling, amplitude and culture compatibility. A cell–electrode signal depends on cleft/seal impedance, electrode impedance and leakage, not neural activity alone. A simplified interface is
\[
Z=R_s+(1/R_i+i\omega C_i)^{-1}.
\]
Johnson resistor voltage-noise variance is \(4kTR\Delta f\); broader noise reasoning uses the real part of impedance/admittance. Electrode material, effective area, platinum black/iridium oxide/carbon nanotubes/porous gold alter coupling.

Rigid-silicon/soft-tissue mismatch motivates flexible/stretchable polymers, parylene, PEDOT:PSS, organic transistors and printed carbon/gold. Patterned PDMS, guided cultures, organoids and 3-D/kirigami electrodes address tissue organization/sampling. Electrohydrodynamic fabrication, passivation and electrochemical characterization are lecture methods, not personal fabrication experience.

## Chemical transport and neurotransmitter measurement

Dopamine oxidation/reduction and carbon-fiber amperometry turn transport into measured current. Diffusion, migration and convection differ; the illustrated diffusion model assumes a perfectly absorbing electrode. Cottrell's planar current decays as \(t^{-1/2}\), while Shoup–Szabo's microelectrode comparison introduces radial transport and nonzero steady current. Release/uptake/pharmacological examples and charge integration support event quantification, not an unqualified concentration estimate independent of geometry.

## Electrical and optical actuation

Sensory/motor/modulatory neuroprostheses include cochlear/retinal/vestibular/tactile systems, FES, deep-brain/spinal stimulation and invasive/noninvasive BCIs. EEG, TMS/electrical stimulation and optogenetics are different modalities, not synonymous interventions.

For a compartmental myelinated axon \(V_m=V_i-V_e\). A point electrode in a homogeneous conductor gives potential proportional to \(\rho I/(4\pi r)\); the activating function is proportional to the second spatial derivative of extracellular potential **along the axon**. Polarity, trajectory, boundaries and field curvature matter: constant potential or constant field is not a localized activating profile.

ChR2 optogenetics uses a four-state open/closed kinetic account, optical attenuation and fiber/LED delivery with energy/selectivity constraints. Optical cochlear stimulation and nerve-regeneration examples establish research context, not clinical efficacy or personal experimentation.

## Auditory coding as a complete signal chain

Cochlear hair-cell damage, lost amplification/compression and tonotopy motivate electrode coding. F0/formant/MPEAK feature schemes differ from compressed analog, CIS, ACE and FS4 temporal strategies. CIS uses AGC → band-pass channels → envelopes → compression → sequential/interleaved pulses, reducing electrical interaction. Vocoders distinguish envelope from fine-structure cues.

Monopolar/bipolar spread, current steering, strength–duration response, noisy-threshold LIF/reset and pulse-train adaptation link electrical input to firing. Threshold-to-comfort mapping/compression, temporal integration, loudness/rate/place-pitch and evoked compound responses support device fitting/assessment.

Speech/noise testing and bilateral ITD/ILD localization assess different outcomes. Independent ear compression can distort ILDs; high-rate envelope representation can conflict with low-rate temporal-cue benefits. These engineering trade-offs connect sensing, dynamics and task evaluation without reducing the subject to a generic ML application.

[EI7646 interface/stimulation/auditory claims](../evidence/ei7646.yaml) cover these late lecture blocks. No programming stack, personal device construction or clinical outcome is evidenced.
