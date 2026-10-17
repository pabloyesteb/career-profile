---
id: local-adaptive-function-approximation
title: Local motor-function approximation, CMAC and self-organizing maps
domains: [machine-learning, control-estimation, computational-neuroscience]
evidence_refs: ["ei7263:local-adaptation", "ei7263:team-comparison"]
status: reviewed
---

# Local motor-function approximation, CMAC and self-organizing maps

## CMAC: sparse associative coding and local updates

CMAC quantizes bounded coordinates, combines active feature ranges and sums active association weights. In the lecture notation,
\[
x_i=\sum_{jk}w_{ijk}a_{jk},\qquad
\Delta w_{ijk}=\alpha a_{jk}(t_i-x_i)/n_a.
\]
Activations are binary; a small overlapping active set gives local generalization. With that fixed summed convention, α=1 reaches the illustrated target locally, not global control convergence. Error training substitutes an externally supplied error direction. Resolution raises memory cost; receptive fields trade detail against overlap/smoothing. Sparse coverage yields separate bumps and gaps; clamping and training-region coverage matter. Hashing compresses virtual tables with collisions/interference, but Tutorial 4 explicitly requires no hashing.

The reaching task maps two image coordinates to two shoulder coordinates. Required resolution 50, receptive fields 3/5 and sample sets 75/150 are specifications, not completed personal measurements. Submitted code also tries field 10 and an 85/15 shuffled split; it uses an \(n_a^2\) active grid and averages outputs, with one prediction branch summing instead. Its update scaling is therefore not exactly the lecture's summed/fixed-count convention.

## SOMs and adaptive success/failure memory

Kohonen SOMs choose a closest prototype and adapt it plus neighboring grid units:
\[
w_r\leftarrow w_r+\epsilon h(r,s,t)(v-w_r).
\]
Neighborhood width controls cooperative adaptation; frequent regions gain representation. The source's displayed Gaussian neighborhood omits a squared distance, so no corrected kernel is invented. SOM topology-preserving prototypes differ from CMAC's quantized local lookup, despite both supplying regional generalization.

Success–failure learning maintains separate maps of motor-parameter outcomes. Candidate distances to both maps inform go/no-go trials; observations update the corresponding memory. A vigilance threshold modulates risk. QARL adds action quality and reward-scaled SOM adaptation, distinguishing safe/successful behavior from efficient behavior. Hip-extensor neuron gain/threshold and walking displacement/energy examples connect these ideas to embodied adaptation, not guaranteed robot safety.

## Representation comparisons and evidence

The named Team E CMAC/FFNN comparison includes Pablo among five authors and qualitatively contrasts CMAC learning speed with FFNN generalization. It does not isolate individual coding or establish universal controlled rankings. [Humanoid claims](../evidence/ei7263.yaml) separate this collaborative artifact from supplied implementations. [Neural training](neural-training-data-contracts.md) covers the complementary global-parametric model/data workflow. No personal robot experiment is inferred from stored NPZ/video/data files.
