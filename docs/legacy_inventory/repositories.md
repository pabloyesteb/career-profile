# External repository access

Historical reference retained during inventory simplification. Links and source locations have been updated; dated processing statuses and workflow instructions below describe the retired extraction phase. The active registry is `01_inventory/sources.yaml`; document fingerprints remain in the relevant project profiles.

Inventory date: 2026-10-13. Repositories were inspected read-only. Revisions are the checked-out commits at inventory time; dirty worktrees mean uncommitted files may also be relevant and must be handled explicitly during later profiling.

| Source | Configured local path | Access | Branch | Revision | Worktree | Origin |
|---|---|---|---|---|---|---|
| Master's thesis | `/home/pablo/TUM/SoSe 26/TFM/contact-rich-control` | Accessible Git repository | `kleff` | `57efc6aa6119cd5ae969ed83fc67efcb40c71672` | Dirty (105 status entries) | `git@code.siemens.com:Autonomous-Systems-Control/students/masterthesis-2026-pablo-yeste-blesa/contact-rich-control.git` |
| pyLowOrder | `/home/pablo/pyLowOrder` | Accessible Git repository | `140-GNN-implementation` | `f79ad1d67660eb9502c17398aa5c196cda90cc97` | Clean | `https://github.com/ArnauMiro/pyLowOrder.git` |
| Case studies | `/home/pablo/TUM/SoSe 25/Case Studies/NLOTrajectories` | Accessible Git repository | `main` | `934956c78c03d5581505a50652b2ab4302e6baa5` | Dirty (6 status entries) | `https://github.com/pyMSE/NLOTrajectories.git` |

The thesis PDF, thesis presentation PDF and LaTeX source, article PDF, previous CV, and case-studies PDF are separately recorded in `01_inventory/sources.yaml`.

## Case Studies project checkpoint — 2026-10-14

Definitive project profile completed at `02_profiles/projects/case_studies_optimization.md`, paired with existing course profile under `cit413042`. Original report `/home/pablo/TUM/SoSe 25/Case Studies/Trajectories-4.pdf` is registered as `case_studies_final_report` and hash-identical to the existing local report copy. Repository remains at `934956c78c03d5581505a50652b2ab4302e6baa5`; tracked files clean and the same six untracked status entries retained. Targeted author/diff inspection establishes personal SIREN/metric/benchmark/integration evidence while retaining team attribution. No repository/report content was modified or executed.

## pyLowOrder contribution checkpoint — 2026-10-14

Subsequent same-day completion: `02_profiles/projects/pyloworder.md` is complete_validated and MA8102 project profiling is complete. The checkpoint paragraph below records the earlier analysis stage; its final-profile deferral is now superseded. Source revision and clean worktree are unchanged.

Read-only analysis completed in `02_profiles/projects/_analysis/pyloworder_analysis.md` at `f79ad1d67660eb9502c17398aa5c196cda90cc97`, branch `140-GNN-implementation`, clean worktree. Repository is non-shallow but only this local branch and origin tracking ref are available; no remote fetch/release verification performed. The 242 associated `P. Yeste <p.yesteb@upm.es>` commits are inventoried in `02_profiles/projects/_analysis/pyloworder_commits.csv`; script-generated patches/snapshot are regenerable under `.cache/pyloworder_analysis/`. Final professional profile not created; MA8102 remains deferred to that phase.

## Thesis reconstruction checkpoint — 2026-10-14

Subsequent same-day completion: definitive profile `02_profiles/projects/thesis.md` is now complete_validated under `prompts/projects/thesis_profile.md`. The paragraph below preserves the earlier reconstruction checkpoint; final-profile status is no longer unstarted. Inspection revision remains unchanged and the historical repository remained read-only.

Read-only reconstruction completed in `02_profiles/projects/_analysis/thesis_analysis.md`; final thesis profile remains unstarted. Thesis HEAD/branch and 105-entry dirty state remain as above. Inspected submodules: `docs/thesis` at `99168732f23fee733ac4c4c1a91d9646f62ca799`; `external/acados` at `6111f01f2220a241057b4d56d8fe3a2cddd0309f`; `raptico_problem_data` at `9203bf67fe4867f06da2e227cacf5a7448721977`. Relevant file/config hashes and status are captured in regenerable `.cache/thesis_analysis/repository_snapshot.json` by `scripts/inspect_thesis_evidence.py`. Current checkout is not asserted to be the exact August experiment revision; code imports and defense changes postdate submission. No source repository code was executed or modified.
