# Phase 1.5 — The Fiedler-Boundary Test (P2): Report

Round 22 (Task ID 23). Triggered by the user's P1/P2 separation critique.
Executed 2026-10-10 on the standing corpus: 7 HCP connectomes (AAL2 94,
neurolib hcp dataset, sha-verified against the canonical GitHub files) + the
same subjects' empirical BOLD (TC_rsfMRI_REST1_LR, 94 x 1200) + the Farnes
2020 spontaneous EEG corpus (Raw_data_2, 40 recordings).

**Status: EXECUTED as an actual computation. P2 is now tested.**

## 0. The P1/P2 re-interpretation (the user's critique, verified)

The Round-19 Phase-1 report conflated two predictions:

- **P1 (operating point)**: the system sits near the bifurcation
  J_c = ga/lambda_2 with marginally unstable zero field and metastable
  domains. Phase 1 tested this: operating point inside the extended critical
  K-band for 7/7 connectomes, edge-concentrated. The status table graded
  this "Supported, weak form - Partial" — as if partial underperformance.
- **P2 (domain structure)**: the domains are the sign regions of the Fiedler
  vector psi^(2); different connectomes should produce different domain
  geometries correlated with spectral structure. Phase 1 did NOT test this —
  but its "honest negative" (op-point structure-function coupling not
  topology-specific) is a P2-ADJACENT failure, reported next to the P1
  verdict without distinction.

Both halves of the user's critique check out against the record
(PHASE1_REPORT.md lines 217-232; worklog R19). Re-tagged below (section 6).

**The regime reading is confirmed quantitatively.** At the fitted operating
point (primary convention): mean order = 0.498, mean pairwise PLV = 0.0098
(both UNFITTED observables — the fit criteria were DFA median and alpha
peak). This is the predicted low-beta regime: the bifurcation threshold is
crossed (in-band) but the coherence threshold is not (PLV ~ 0.01) — domains
form metastably, never lock. "Weak, edge-concentrated" is the SIGNATURE of
this regime, not underperformance. The user's noise-amplitude figure
sqrt(2/0.12) = 4.1 is one convention; in the Kuramoto fit's own units
sigma* = 3 at K* = 25. The two readings agree qualitatively
(noise-dominated mesoscale); the quantitative gap between them is exactly
the unwritten Kuramoto-to-GL dictionary — the standing parameter-map gap
(flagged again in section 7).

## 1. Methods

**Spectral battery.** For each connectome W (symmetrized raw DTI fiber
counts): L_sym = I - D^{-1/2} W D^{-1/2}; full eigendecomposition; the
Fiedler vector psi^(2) (mode 2) and modes 3-7. Sign convention fixed to
transmodal-positive; all reported statistics sign-invariant.

**Functional references** (phase15_labels.py, documented hand mapping):
Yeo-7-style network assignment for all 94 AAL2 regions (Visual 12, SomMot
14, DorsalAttn 4, VentralAttn 8, Limbic 26, Cont 6, Default 16, Subcortical
8); coarse sensory->transmodal axis score (Visual/SomMot 0-0.15, attn 1.0,
Limbic 1.5, Cont 2.0, Default 3.0, subcortical excluded); hemisphere;
cortical/subcortical; DID key sets from the Schlumpf thesis (EP cluster =
Postcentral, Precentral, Supp_Motor_Area, Frontal_Sup_Medial bilaterally;
ANP marker = bilateral Thalamus). Label order validated empirically: median
homotopic FC r = 0.638 +- 0.077, at the 87-95th percentile of all pairs in
7/7 subjects — the LRLR AAL2 ordering is correct.

**Statistics**: hemisphere/subcortical/axis |Spearman|; network-boundary
contrast (cross- minus within-network mean |dpsi|, normalized); DID
separation (|mean psi_EP - mean psi_ANP| in psi sd units); bipartition
agreement for every network; spectral-embedding ARI (k-means on modes 2-5 vs
Yeo labels at k = 2/4/7); eigengap profile.

**Nulls (dense-graph regime).** DISCOVERY: these connectomes are FULLY DENSE
(4371/4371 nonzero pairs, 7/7 subjects) — Maslov-Sneppen degree-preserving
rewiring is formally inapplicable (every proposed double-edge swap is
rejected). The first implementation's "rewire null" was a silent no-op (all
p = 1.000) — caught in the first run and replaced. The correct nulls:
- **shuffle** — same weight multiset, random topology (the
  generic-weighted-graph null; defeats the "generic criticality /
  graph-structure-irrelevant" alternative);
- **block** — hemispheric-block-preserving weight shuffle (weights shuffled
  separately within intra-L, intra-R, inter blocks: preserves the coarsest
  cut exactly; the null for FINER-than-hemispheric structure);
- **perm** — region-identity label permutation, 10k, per mode (the primary
  P2 reference);
- **bipart** — random size-matched bipartitions (2k).
Confound control: partial Spearman vs node strength. Sensitivity arms:
unnormalized Laplacian; log1p weights; ambiguous-region exclusion.

**FC legs.** Per subject: FC = Pearson(BOLD); PC1 = leading eigenvector of
FC (gradient-1 proxy); psi_FC = Fiedler of L_sym(clip(FC, 0)); SC-mode vs
PC1/psi_FC Spearman with 10k label-permutation nulls; classic edge-level
SC-FC correlation.

**Dynamic leg.** Farnes spontaneous EEG (10 subjects x 4 conditions): 8-30
Hz Hilbert envelope FC over the 62 channels; eigengap lambda_3 - lambda_2 of
its Laplacian = leading domain-structure strength; awake vs ketamine
within-subject (Wilcoxon over 20 pairs); geometry stability =
|Spearman(psi_awake, psi_ketamine)|. Caveat: sensor-level envelope FC
retains volume-conduction bias; the within-subject contrast cancels it to
first order. Prediction tested (domain merging): eigengap decreases under
ketamine.

## 2. Results — the domain hierarchy of the human connectome

### 2.1 Level 1 (the Fiedler cut): the hemispheres

psi^(2) aligns with the interhemispheric axis at |rho| = 0.864 +- 0.004 in
7/7 subjects, vs 0.081 under the random-topology null (Wilcoxon p = 0.0078,
the n=7 floor; per-subject shuffle p = 0.005 = the 1/201 floor in 7/7).
**The coarsest spectral domain of the human connectome is the two
hemispheres.** In the decombination reading: the level-1 domains are the
hemispheres; the predicted boundary dA = {psi ~ 0} is the midline.

This is topology-SPECIFIC (vs random topology at the shuffle floor) — the
first half of P2 confirmed at the coarsest level, with the exact geometry
the split-brain arm requires (see section 5).

### 2.2 Levels 2-4 (modes 3-6): the network geometry

Network-boundary contrast by mode (group mean, 7 subjects, vs
hemispheric-block null):

| mode | net contrast | block null | Wilcoxon p | axis align (p) |
|------|-------------|------------|------------|-----------------|
| 2    | 0.07        | -0.05      | 0.0078     | 0.03 (0.95)     |
| 3    | 0.40        | -0.00      | 0.0078     | 0.34 (0.008)    |
| 4    | 0.40        | ~0.00      | 0.0078     | 0.21 (0.008)    |
| 5    | 0.25        | ~0.00      | 0.0078     | 0.07 (0.85)     |
| 6    | 0.39        | ~0.00      | 0.0078     | 0.10 (0.19)     |
| 7    | 0.10        | ~0.00      | 0.0078     | 0.08 (0.66)     |

Per-subject: mode-3/4 network contrast beats the block null at p = 0.005
(floor) in 7/7 subjects. **The network-level domain geometry is decisively
encoded in the connectome's fine topology, beyond the hemispheric block.**
Mode 3 additionally carries the sensory->transmodal alignment (0.34,
p = 0.008 vs block; per-subject perm p < 0.001 in 5/7). Strength confound:
node strength has no axis structure (rho = 0.023 +- 0.034), so the mode-3
axis alignment is not a strength artifact.

Spectral-embedding ARI vs Yeo: 0.089 at k=7 — weak. The k-means partition
match to Yeo networks is coarse (expected: Yeo is a functional parcellation;
the SC embedding is coarser and differently oriented).

### 2.3 SC -> FC: the structure-function test at domain granularity

- PC1 (the FC principal gradient) aligns with the sensory->transmodal axis
  at rho = 0.436 +- 0.102 in 7/7 — the canonical Margulies result reproduces
  from raw data (this VALIDATES the mapping).
- Edge-level SC-FC Spearman = 0.265 +- 0.073 — the classic moderate value.
- **SC Fiedler (hemispheric) does NOT predict the FC gradient** (group
  |rho| ~ 0.0005, perm p = 0.74): the leading structural domain is NOT the
  leading functional domain.
- **SC fine modes DO predict the FC gradient**: mode 3 (perm p = 0.016
  group mean; significant in 5/7 subjects, |rho| up to 0.51), mode 5
  (4/7), mode 6 (group p = 0.0074). Eigenvector signs flip arbitrarily
  across subjects; magnitudes and nulls are the reportable quantities.
- The FC's OWN Fiedler is transmodal-structured (|rho| to axis up to 0.72)
  and NOT hemispheric (0.094) — functional domain geometry is
  gradient-first.

Reading: the structural domain hierarchy predicts the functional domain
hierarchy at the finer levels (modes 3-6 -> gradient), while its level-1
boundary (the midline) is functionally integrated at rest. Structure-first,
function-second — see section 5.

### 2.4 The DID directional test: honest negative

DID separation (EP cluster vs bilateral thalamus) at the Fiedler level:
0.105 sigma, group p = 0.99 vs block, per-subject permutation p = 0.76-0.99.
Across modes 3-6 the raw separations reach 0.7-1.2 sigma but the
region-identity permutation null (random 8-vs-2 subsets of the same psi)
is equally wide — the correct test for a 2-region marker set — and is NULL
in every subject at every mode (best case p = 0.125). **The Schlumpf ANP/EP
geometry is NOT carried by the structural connectome's spectral domain
structure at AAL2 granularity.** Two readings, both recorded: (a)
underpowered (2 thalamic regions of 94; the perm null sd is large), (b) the
Schlumpf asymmetries are PERFUSION-level (functional), and the honest
conclusion is that they live on the functional side of the structure-function
divide, not in the structural domain geometry. The DID arm's raw-data
blockade (R11: zero open DID neuroimaging) stands; the thesis anchors remain
literature-level.

### 2.5 The dynamic leg: domain-structure strength under ketamine

Eigengap awake vs ketamine (20 within-subject pairs): awake 0.0120,
ketamine 0.0111, Wilcoxon p = 0.449, fraction lower = 10/20 — **NULL**. The
sensor-level leading domain-structure strength does not detectably change
under sub-anaesthetic ketamine in this instrument. Geometry stability
across states: |Spearman(psi_awake, psi_ketamine)| = 0.634 +- 0.277 — the
domain GEOMETRY is moderately stable across the state change. Caveats:
62-channel sensor level (volume conduction; within-subject contrast only),
2-minute recordings, and the eigengap is a blunt scalar. The domain-merging
prediction (from J-reduction) is NOT confirmed at this granularity —
recorded as an honest negative; the parcellated-cortex version remains open
(needs source-level or atlas-parcellated psychedelic data).

## 3. Reproducibility

Scripts: scripts/phase15_labels.py (mapping), phase15_lib.py (battery +
nulls), phase15_fiedler.py (runner: chunks 0-6, sens, aggregate),
phase15_fc.py (FC legs), phase15_eeg.py (dynamic leg). Outputs:
research/phase15/ (7 subj_*.json, sensitivity.json, phase15_results.json,
fc_results.json + fc_group.json, eeg_domain.json + summary, figs/ x3).
Compute: ~11 min total. All seeds fixed; nulls 200/10k; the dense-graph
no-op rewire bug and its fix are documented in the code.

## 4. What Phase 1.5 establishes and does not

ESTABLISHED (with the stated nulls):
1. P2 is testable and the test is decisive at two levels: the Fiedler cut
   is the hemispheres (7/7, shuffle floor), and the network-level domain
   geometry is encoded in fine topology (7/7, block floor).
2. The SC domain hierarchy and the FC domain hierarchy are related but
   non-identical: SC modes 3-6 -> FC gradient (significant), SC mode 2
   (hemispheres) -> no FC counterpart at rest.
3. The generic-criticality alternative ("graph structure doesn't matter for
   the domain signature") is REJECTED at both tested levels: the domain
   geometry is specifically the real topology's.

NOT ESTABLISHED:
1. The DID directional geometry (null at the structural level; power +
   granularity caveats).
2. Domain merging under psychedelia at sensor level (null eigengap).
3. Any link from this static geometry to the GL parameters (J, g, a, beta)
   — the parameter-map gap is untouched by Phase 1.5 (see section 7).

## 5. The split-brain synthesis (why the level-1 result matters)

The decombination model's level-1 domain boundary is the midline. In the
intact resting brain this boundary is structurally present (Fiedler cut,
7/7) but functionally integrated (no FC hemispheric cut; SC-Fiedler does
not predict the FC gradient). The model predicts that reducing callosal
coupling J below threshold reveals this structural domain as a
functional/consciousness-level boundary — which is what the split-brain
literature observes and what the corpus's Santander 2025 criticality
anchor addresses. Phase 1.5 supplies the structural half of that
prediction from data. The prediction now has a concrete, already-collected
test bed: the split-brain arm's datasets (when any become openly
available), or callosal-agency gradients (partial agenesis cases).

## 6. Re-tagged status table (replacing the conflated Phase-1 rows)

| Row | Status after Phase 1 + Phase 1.5 |
|---|---|
| P1: operating point near J_c | Weakly confirmed (7/7 in-band, edge-concentrated = the predicted low-beta metastable regime; order 0.498 / PLV 0.010 at the op point are unfitted observables landing in that regime) — Partial, regime-consistent |
| P2: domains = Fiedler sign regions | **Level 1 (hemispheres): confirmed, 7/7, shuffle floor. Levels 2-4 (network geometry): confirmed vs block null, 7/7. Axis assignment at mode 3: confirmed (p=0.008). ARI-level partition match: weak (0.09).** — Supported at the tested granularities |
| P2-adjacent: op-point dynamics topology-specificity | Failed (R19/R20 nulls stand) — now correctly tagged as a DYNAMICS-level result, NOT a domain-geometry result |
| DID directional geometry (Schlumpf) | NULL at the structural level (perm null, all modes); functional-level anchors unchanged — Unsupported-by-this-instrument |
| Domain merging under psychedelia (sensor EEG) | NULL (eigengap, p=0.449); geometry stable (0.63) — Open at parcellated granularity |
| beta parameter map | Unchanged: beta-hat = 0.12 (Kuramoto units) vs 4.1 noise amplitude (GL reading) — the dictionary gap stands |

## 7. Protocol amendment 5 (and the forward path)

1. **P1 and P2 are formally separated** in all future reporting; the
   conflation in the Phase-1 status table is repaired (this report, plus
   the addendum in PHASE1_REPORT.md).
2. **The Fiedler-boundary battery is the standing P2 instrument**, to be
   run on every connectome the program touches (patient-level Phase 4,
   psychedelic Phase 3 re-parameterizations).
3. **Dense-graph null discipline**: degree-preserving rewiring is
   inapplicable to fully dense weighted connectomes; the shuffle + block +
   permutation triple is the mandated null family (the no-op rewire bug is
   the cautionary tale, now documented in code).
4. **The dynamic domain tests need parcellated data**: sensor-level
   eigengaps are too blunt. Phase 3's psychedelic corpora should be
   processed to atlas parcellation before the domain-merging test is
   attempted again.
5. The parameter-map gap (J, g, a, beta -> measurable quantities) remains
   the binding constraint on interpreting beta-hat — unchanged from the
   user's flag; Phase 3 (Deco parameterization) and Phase 4 (Bayesian
   inversion) are where the dictionary gets built.

Standing metaphysics check (absolute.txt): all findings above are
appearance-level structure — connectome geometry, FC gradients, sensor
domain strengths. Nothing here attributes process or division to the
Absolute; the two-level doctrine and the conventional-level ceiling are
untouched. The split-brain synthesis in section 5 is an appearance-level
prediction register, not an ontological claim.
