# Round 19 — The 13 Supplied Files: Reading Record and Appendix-A Mapping

## 1. Inventory and identification

`upload/level 2 decombiniation/` now holds 13 files. Five were read in Round 18
(P1-P5 below, digests in `new_uploads/digests/`). Eight arrived via the four
user commits 68a3977/6be1d3d/e835eb8/7770198 and were extracted
(`new_uploads/l2b_*.txt`, cleaned cores in `new_uploads/cores/`) and read this
round (P6-P13).

| # | File | Identity | Status |
|---|------|----------|--------|
| P1 | 1-s2.0-S1053811916300891-main.pdf | Jirsa et al. 2017, VEP (NeuroImage) | read R18 |
| P2 | 2024.05.08.593146v4.full.pdf | Myrov et al., hierarchical Kuramoto (bioRxiv) | read R18 |
| P3 | The_Dream_That_Must_Be_Critique_Steelman_Survival_Test.pdf | Deco et al. 2018, Curr Biol (misnamed upload) | read R18 |
| P4 | elife-35082-v3.pdf | Preller et al. 2018, eLife | read R18 |
| P5 | riedl-et-al-2015-...pdf | Riedl et al. 2016, PNAS (MCM) | read R18 |
| P6 | 1-s2.0-S245190222300191X-main.pdf | Avram et al. 2024, Biol Psychiatry CNNI 9:522-532 | read R19 |
| P7 | Bedfordetal-2023-...pdf | Bedford et al. 2023, Neuropsychopharmacology | read R19 |
| P8 | s42003-025-07576-0.pdf | Piccinini et al. 2025, Commun Biol 8:409 (DMT) | read R19 |
| P9 | file.pdf | Liang et al. 2015, PLOS ONE 10(12):e0145959 (PK-NMM) | read R19 |
| P10 | Fabus_2023_...pdf | Fabus 2023, Oxford DPhil thesis (496 KB text) | read R19 |
| P11 | 1-s2.0-S0165027026001895-main.pdf | Butler et al. 2026, J Neurosci Methods 435:110859 | read R19 |
| P12 | s41593-025-02016-y.pdf | Taxidis et al. 2025, Nat Neurosci 28:1946-1958 | read R19 |
| P13 | s41597-025-04832-0.pdf | Diosdi et al. 2025, Sci Data 12:492 (spheroids) | read R19 — see flag |

**Flag on P13**: this is a cancer-imaging data descriptor (tumour-stroma
spheroid multicultures); its author list contains *Filippo* Piccinini
(Bologna/IRST — cancer image analysis), a different person from *Juan
Ignacio* Piccinini (Buenos Aires — first author of P8, the DMT
destabilization paper the Appendix-A list pointed to). The relevant Piccinini
paper is P8 and is now read; P13 appears to be a same-surname retrieval and
is not needed for the parameter map (kept in the upload folder, unused).

## 2. Appendix-A mapping (Table 8.1 of the Seventh Edition)

Appendix A = "Sources This Environment Still Cannot Fetch" — the list of
papers I could not open from this environment (publisher 403/400 blocks),
delivered with full titles so the user could supply any of them. The new
uploads resolve it as follows:

| Appendix-A item | Supplied? | Notes |
|---|---|---|
| Bedford et al. 2023 (LSD rDCM) | YES — P7 | the NPP open-access version |
| Avram et al. 2024 (CNNI) | YES — P6 | archival report, CC BY-NC-ND |
| Liang et al. 2015 (PK-NMM) | YES — P9 | PLOS OPEN ACCESS |
| Butler et al. (5-HT2A / monoaminergic, ScienceDirect) | PARTLY — P11 | the supplied Butler paper is the same Bordeaux group's *neurochemical connectivity* methods paper; if a separate "5-HT2A receptors shape whole-brain monoaminergic dynamics" article exists it remains unfetched |
| Piccinini et al. 2025 (destabilization) | YES — P8 | Commun Biol, not "Nature" as guessed in the Appendix |
| Fabus et al. 2023 (Oxford thesis) | YES — P10 | full thesis, ora.ox.ac.uk blocked |
| Farnes et al. 2020 (Dryad raw EEG) | NO | data-only item; the supplied ketamine zip lacks the raw .fdt/.set files |
| ETH research collection (Schlumpf provenance) | NO | provenance-only item |

Two additional papers (P12 Taxidis, P13 Diosdi) were not on the list; P12 is
a substantive addition (see below), P13 is the flagged same-surname item.

## 3. Digests of the newly read sources

### P6. Avram, Müller, Preller, Razi, ... Borgwardt 2024 — "Effective Connectivity of Thalamocortical Interactions Following d-Amphetamine, LSD, and MDMA Administration" (Biol Psychiatry: CNNI 9:522-532, doi 10.1016/j.bpsc.2023.07.010)
- n=25 healthy (12 F, 28.2±4.35 y), 4-session double-blind placebo-controlled
  crossover: LSD 100 μg, MDMA 125 mg, d-amphetamine 40 mg, placebo.
- **Spectral DCM** (SPM12 v7771, DCM12.5; power-law endogenous fluctuations
  fitted to cross-spectral density), two 6-ROI models: thalamus +
  unimodal cortex (auditory, postcentral, lingual, cuneus) and thalamus +
  SAL-derived transmodal (ACC, insulae, supramarginal). 8-mm sphere ROIs,
  first-PC time series, motion/physio/128-s-highpass regressors. PEB
  group-level + Bayesian model reduction. Explained variance 89-91%.
- Results: **all three substances increased thalamus→unimodal EC and
  decreased unimodal→thalamus EC** (bottom-up up, top-down down; e.g. LSD:
  lAU→TH −0.24, TH→lAU +0.07/+0.17-scale effects, posterior prob ≥.99).
  Amphetamines: opposite pattern for transmodal (cortex→thalamus up = top-down
  control). **LSD: increased thalamus→transmodal EC with NO corticothalamic
  change — a breach of hierarchical organization.** Thalamic self-inhibition
  increased under LSD (TH/TH +0.12). VAS: d-amph EC↔"speed of thinking"
  (p=.01); LSD thalamocortical EC↔"good drug effect"/"drug liking" (p=.03/.01).
- Project role (Phase 3): the directed, causal version of the psychedelic
  thalamic-gating evidence; strengthens the J-row's directional
  (asymmetrized) claims for the psychedelic arm; method = spectral DCM,
  directly compatible with the rDCM/DCM toolchain already anchored.

### P7. Bedford, Hauke, Wang, Roth, ... Diaconescu 2023 — "The effect of LSD on whole-brain functional and effective connectivity" (Neuropsychopharmacology, doi 10.1038/s41386-023-01574-8, OPEN)
- n=45 (two Basel trials, 20+25), 100 μg LSD vs placebo, eyes-closed resting
  fMRI ~140 min post-dose, crossover.
- **rDCM whole-brain EC**: 132 Harvard-Oxford ROIs → 17,424 directed
  connections + 132 self-connections; FC comparison (8,646 correlations);
  PLSC (2000 perms) + random-forest decoding (5-fold CV, 1000 label perms).
- Results: ~23% of FC / ~13% of EC connections change (p<.05); **mostly
  STRONGER inter-regional connectivity under LSD, EXCEPT occipital (weaker
  EC, MORE self-inhibition) and subcortical**. Thalamus↔cortex EC stronger
  in BOTH directions (positive-feedback reading). **~30% (39/132) of
  self-connections differ: widespread disinhibition (self-connection values
  toward zero = closer to a critical point, authors' own dynamic-systems
  framing) in temporal/subcortical/cerebellar regions; occipital increases
  inhibition.** Asymmetry present (10-14% of pairs) but unaffected by LSD
  (1.4% interaction). ML: EC decodes LSD vs placebo at **91.11% balanced
  accuracy** (FC 86%, n.s. difference); EC-behavioural PLSC r=0.932 with
  5D-ASC global.
- Project role (Phase 3): the at-scale rDCM evidence; the
  self-connection→critical-point statement is a published precedent for the
  specification's coherence threshold (Jβ) reading of local gain; the
  occipular anti-pattern is domain heterogeneity the GL domains picture
  predicts (sensory vs associative).

### P8. Piccinini, Sanz Perl, Pallavicini, Deco, Kringelbach, Nutt, Carhart-Harris, Timmermann, Tagliazucchi 2025 — "Transient destabilization of whole brain dynamics induced by N,N-Dimethyltryptamine (DMT)" (Commun Biol 8:409, doi 10.1038/s42003-025-07576-0)
- Re-analysis of the Imperial EEG-fMRI DMT dataset: 15 of 20 volunteers
  (motion-excluded), 20 mg IV DMT vs saline, 28-min eyes-closed resting
  scans, dose at minute 8, TR=2 s, AAL-90 time series.
- Model: **Stuart-Landau nonlinear oscillators on the AAL-90 connectome
  (DTI of 16 Aarhus subjects), dx/dt = a(t)x − ωy − (x²+y²)x + G Σ C(x_p−x_n)
  + γη** (same in y with +ωx); bifurcation at a=0 (limit cycle vs noise-
  dominated stable spiral); baseline a=0.07. **a(t) = gamma-function
  pharmacokinetics with amplitude λ and latency β**; DMT: λ=159.3±7,
  β=284±37 s (peak ~5 min, recovery by ~30 min); placebo: λ=65.6±9,
  β=588±69 s (peak not reached in-session); t-tests p<1e-4 both.
- Fit target: **FCD** (windowed-FC similarity matrices), compared by
  Euclidean/Frobenius distance (0.19±0.03 DMT vs 0.14±0.02 placebo);
  n=50 simulations.
- Perturbation analysis: periodic driving at endogenous frequency →
  reactivity χ(t) peaks with DMT (fronto-parietal + extrastriate visual);
  **Δχmax across 6 RSNs correlates with local 5HT2a receptor density,
  ρ=0.9059±0.0003** (bootstrap), peaking ρ>0.9 at intermediate intensity.
- Project role (Phase 3, decisive): the **a-parameter (attractor depth /
  distance to bifurcation) is given a pharmacokinetic driver and a receptor
  density gradient — published, peer-reviewed**. This upgrades the
  psychedelic arm's a-row from "derived-unvalidated" to "published
  estimator exists (Stuart-Landau + PK + 5HT2A density)"; also the
  criticality-proximity transient ("minimal perturbation, maximal effect")
  is the mechanistic version of the specification's J→J_c approach.

### P9. Liang, Duan, Su, Voss, Sleigh, Li 2015 — "A Pharmacokinetics-Neural Mass Model (PK-NMM) for the Simulation of EEG Activity during Propofol Anesthesia" (PLOS ONE 10(12):e0145959, OPEN)
- **Schnider three-compartment PK model + effect compartment (ke0)**:
  Ceff(t) from the actual infusion regimen, personalized (age, weight,
  height, gender; V1=4.27 L, V2=18.9−0.391(age−53), V3=238 L, clearances
  per Table 1). Linear map rCeff = 1 + 0.49·Ceff/max(Ceff) ∈ [1, 1.49].
- **NMM = Steyn-Ross/Liley mean-field macrocolumn** (85:15 E:I; he, hi soma
  voltages; EEG = fluctuation of he about steady state). Drug entry:
  **propofol lengthens IPSP by factor λ → γi → γi/λ** (GABAA chloride
  channels open longer); phase change into unconsciousness at λ≈1.5.
- Validation: 9 volunteers (Waikato), propofol 1500 mg/h infusion to LoC
  (syringe-drop), Fp1-F7 EEG at 256→100 Hz. sEEG vs rEEG: **permutation
  entropy correlation 0.80±0.13; SynchFastSlow correlation 0.77±0.13**;
  spectral peak migration to low frequencies and the biphasic effect
  reproduced. Data on Figshare (10.6084/m9.figshare.1485719).
- Project role (Phase 2, decisive): the **explicit drug-level→EEG bridge**
  (infusion → Ceff → IPSP kinetics → mean-field → sEEG) that the anesthesia
  arm's parameter rows need; combined with Bojak-Liley sweeps it closes the
  "anesthetic concentration ↔ β/J rows" chain with published code-level
  detail.

### P10. Fabus 2023 — "Spatiotemporal brain dynamics induced by propofol and ketamine in humans" (Oxford DPhil thesis, St John's College; supervisor Warnaby; with Woolrich, Quinn, Sleigh)
- **Ch. 2 — slow-wave activity saturation (SWAS)**: ultra-slow propofol
  infusion; **local concentration needed for SWAS (C_SWAS) correlates with
  local GABAA receptor density: Spearman ρ=−0.6861, Bonferroni p=0.0018
  (N=26 electrodes)**; LZW complexity at peak anesthesia also correlates
  with GABAA (ρ=−0.70, p=0.0013); BIS at SWAS = 49±4 but fluctuates
  (σ=4.7 within 10 min); BIS-at-SWAS ↔ SW power ρ=−0.675.
- **Ch. 3 — heart**: propofol raises HR dose-dependently (+4.2±1.5
  bpm per μg/ml, p<.001); heartbeat incidence peaks ~450 ms BEFORE slow-wave
  onset (cortico-cardiac coupling, p<.001); brainstem-generator hypothesis.
- **Ch. 4 — itEMD**: iterated-masking EMD (published, J Neurophysiol
  126:1670-84) → **three distinct low-frequency (<4 Hz) wave types** with
  different topographies and dose-responses in propofol.
- **Ch. 5 — HMM**: propofol shifts dynamics to anterior-alpha states with
  reduced switching rate (p<.01); low-density montage translation
  (posterior best captures reduced switching).
- **Ch. 6 — ketamine healthy volunteers**: HMM states; **receptor
  fingerprinting of dynamic states via neuromaps against N=19 receptor
  maps** — ketamine-affected states carry multi-receptor profiles (α4β2
  nicotinic, GABAA, CB1, NMDA, NET, MOR; Bonferroni-corrected, r>0.3),
  beyond NMDA antagonism alone; heartbeat-evoked potential amplitude drops
  under ketamine (impaired interoception → dissociation reading).
- **Ch. 7 — ketamine in treatment-resistant depression**: reduced temporal
  lobe alpha and theta power associated with dissociation (p=0.0109).
- Project role (Phase 2 + receptor rows): **the anesthesia-arm twin of Deco
  2018 — regional drug effect tracked to local receptor density (GABAA for
  propofol ↔ 5-HT2A for psychedelics)**; the Ch.-6 receptor-fingerprinting
  recipe (neuromaps + spatial nulls) is the published, generalizable
  procedure for the map's receptor parameterization rows; itEMD/HMM supply
  the state-switching observables for the DID/ketamine arm's S-instrument.

### P11. Butler, Aman, Bharatiya, Cathala, Chagraoui, De Deurwaerdère 2026 — "Neurochemistry and post-mortem neurotransmitters: Toward the study of neurochemical connectivity" (J Neurosci Methods 435:110859, OPEN)
- Methods/review paper (Bordeaux/CNRS): how to turn post-mortem
  quantitative monoamine tissue content (DA, 5-HT, NA + metabolites, in
  multiple CNS regions, vertebrate and invertebrate) into a third form of
  connectivity — **neurochemical connectivity** — distinct from anatomical
  and functional connectivity: within-compound and between-compound
  correlation matrices / correlagrams, undirected weighted networks and
  directed multigraphs (R1-R3 example), variability as signal (inter-
  individual differences drive resting-state correlation profiles),
  drug-action readouts when quantitative changes are absent.
- Limitations honestly stated: no temporality; tissue content ↔ release
  interpretation is speculative; correlations low in number at rest;
  technical variability sources catalogued (dissection, analytics,
  turnover indices); "mobilized" systems (post-manipulation) give richer
  links.
- Project role (receptor/neurotransmitter rows): a **published template for
  a neurotransmitter-level parameter prior** (regional monoamine content
  correlational structure) — usable as an independent prior for the
  receptor-density parameterizations in Phases 2-3 and as the
  cross-species anchor; NOT the missing unified map (the authors
  explicitly position it as pre-hypothesis-generating).

### P12. Taxidis, Madruga, Safaryan, Dorian, Melin, Day, Lin, Golshani 2025 — "Voltage imaging reveals hippocampal inhibitory dynamics shaping pyramidal memory-encoding sequences" (Nat Neurosci 28:1946-1958)
- kHz-rate GEVI (ASAP3) voltage imaging of CA1 PV and SST interneurons in
  mice during odor-cued working memory (n=5+5 mice, 107 PV + 93 SST cells,
  1000 fps, up to 48 trials/cell, Volpy pipeline); + electrophysiology,
  optogenetics, two-photon calcium.
- Results: interneurons encode odor DELIVERY (not identity/time); PV
  interneurons briefly spike at odor onset then **widespread
  hyperpolarization + theta-paced rebound spiking**; **PV silences most
  pyramidal cells during odor delivery; SST suppresses other interneurons
  (disinhibition)**; odor-selective pyramidal cells fire with the
  interneuronal post-hyperpolarization rebound; **inhibition raises the
  signal-to-noise ratio of pyramidal cue representations**.
- Project role (g/a rows' microcircuit grounding): a direct, intervention-
  backed microcircuit account of inhibitory stabilization and gain
  control — the biological substrate the GL local-stabilization
  parameters (g, a) gloss. Supports the "a ↔ attractor depth" row's
  plausibility at the cellular level (PV timing control, SST gain
  gating); no macro-scale parameter estimator — status: supporting
  evidence, not a map ingredient.

### P13. Diosdi, Piccinini (F.), Boroczky, Dobra, Castellani, Buzas, Horvath, Harmati 2025 — "3D images of tumour-stroma spheroid multicultures" (Sci Data 12:492)
- Cancer-biology data descriptor (light-sheet fluorescence microscopy of
  3-line tumour spheroids at 24/48/96 h; melanoma/breast/osteosarcoma +
  fibroblast + endothelial). **Not related to the parameter map**;
  different Piccinini (see flag in §1). Archived, unused.

## 4. Status after this round

- Every protocol-critical source is now read from full text; the
  Appendix-A paper list is exhausted except (a) the possible separate
  Butler "5-HT2A monoaminergic dynamics" article (uncertain existence),
  (b) the Farnes Dryad raw-EEG data item, (c) the ETH provenance item.
- New capability unlocked by P8+P9: the drug→parameter chain now has
  published anchors on BOTH arms (5-HT2A/PK for psychedelics via
  Piccinini+Deco; GABAA/PK for anesthesia via Fabus+Liang).
- Phase 1 executes this round on open data (Myrov pipeline on
  Brainstorm bst_resting MEG + neurolib HCP connectomes) — see
  `research/phase1/` and `PHASE1_REPORT.md`.
