---
id: "progress-triggered-recovery"
title: "Progress-triggered reference recovery"
domains:
  - "control-estimation"
  - "robotics-planning-geometry"
evidence_refs:
  - "ma6018:spiral-grid-result"
  - "ma6018:recovery-versus-prediction"
  - "ma6018:progress-projection"
  - "ma6018:recovery-state-machines"
  - "ma6018:comparison-sensitivities"
  - "ma6018:sampled-region"
status: "reviewed"
---

# Progress-triggered reference recovery

## Trigger and controlled quantity

Recovery perturbs the reference equilibrium consumed by impedance/MPC, not the physical state or a prescribed contact force. A second feedback loop monitors task progress:
\[
s(n)-s\!\left(n-\left\lfloor t_{bloq}/h_{ctrl}\right\rfloor\right)
<\alpha v_{stag}t_{bloq}.
\]
Here \(s\) is swept path progress, \(h_{ctrl}\) control interval, \(t_{bloq}\) the observation window, \(v_{stag}\) characteristic scenario-path speed and \(\alpha\) the permitted progress fraction. Suppression near intended settling and recovery-state management avoid inappropriate repeated triggers. A force threshold/contact-mode estimate is not required.

## Variants and findings

### Scenario geometry and reference timing

Closest-point projection onto each scenario polyline supplies distance \(d_i\), arc coordinate \(s_i\), and \(t_i=\mathrm{ArcToTime}_i(s_i)\). The alternative local start time is
\[
t_0=\sum_iw_it_i,\qquad
w_i=\frac{d_i^{-\beta}}{\sum_jd_j^{-\beta}},\quad\beta=1,
\qquad x_{d,k}=X_d(t_0+kh_{ctrl}).
\]
Near-zero-distance safeguards are part of implementation. Clock timing instead uses \(t_0=nh_{ctrl}\). If progress stalls, projected time can stall too, reducing the growing tracking discrepancy that clock timing supplies. Projection is still useful for detection/local geometry even though its timing comparison was worse. It is not probabilistic state estimation. Main detector settings (71.8 mm/s, 0.3 s, allowed fraction 0.9) imply about 19.4 mm expected minimum progress over the window.

### Distinct recovery state machines

Tangential displacement chooses a temporary direction from scenario geometry. Discrete spiral/ring probing retains a transverse displacement and changes probes on stagnation events; continuous spiral sweeps a growing displacement over an active interval then clears. These are distinct timing/state machines. Known search primitives are integrated with reference execution, not invented here.

The supported lesson separates compliant tracking from progress-based corrective action: detailed prediction alone did not enlarge the reported baseline set in this setup, while recovery did. Exact counts/denominator/criterion are stored once in [ma6018:spiral-grid-result](../evidence/ma6018.yaml).

The tangential variant uses distance-weighted local tangents, freezes projection during correction, grows displacement at 0.1 m/s for 0.8 s (up to 80 mm), then releases it. Discrete probing starts at 10 mm with eight 45° probes per ring, growing up to 40 mm; stagnation events advance persistent probes rather than applying the tangential reset cycle. Continuous search grows from 5 to 40 mm over 0.8 s for 1.5 turns (675°/s), then clears. Scenario switching retargets the path and has separate ban/clearing state. These are different timing/geometry algorithms, not interchangeable spiral parameters.

## Comparative evidence and limits of interpretation

`ma6018:comparison-sensitivities` consolidates controller/recovery, preview, detector-threshold and planning-size counts. The planning-size experiment holds test offsets fixed while reducing scenario coverage and uses tangential recovery, not the best spiral. Recovery helps but does not remove dependence on the offline plan. True-geometry and known-offset oracles diagnose direction quality; the former changes both geometry and weights, so it is not a clean weighting-only ablation. The known-offset method is not a learned estimator.

`ma6018:sampled-region` preserves the defense's geometric area-expansion observation separately from insertion success rates. A sampled rhombus is not continuous pose-region certification. Both claims remain reported/unreproduced with the known classifier limitation, not additional validated achievements.

## Limits and evidence

Biased perceived geometry can give poor correction directions. True-geometry/known-offset oracles are diagnostic, not deployable results. The classifier discrepancy, simulation assumptions and lack of general robustness guarantees travel with the result.

[Recovery claims](../evidence/ma6018.yaml) → [thesis](../../02_profiles/projects/thesis.md), Stagnation detector, Discrete and continuous spiral search, Search versus estimated-direction recovery and Evidence note and profile validation.
