# Seventh Edition — Research Notes (Round 18)

## The five user-supplied PDFs (upload/level 2 decombiniation/), read in full

### 1. Jirsa et al. 2017 — "The Virtual Epileptic Patient: Individualized whole-brain models of epilepsy spread" (NeuroImage 145:377-388, doi 10.1016/j.neuroimage.2016.04.049)
- File `1-s2.0-S1053811916300891-main.pdf` (12 pp). The ScienceDirect-blocked paper, now read from source.
- Node model: **Epileptor** (5 state variables, 3 time scales; x1,y1 fast discharges; x2,y2 spike-and-wave; z permittivity). **x0 = excitability parameter — THE fitting target**; critical value x0C = -2.05; tissue epileptogenic iff x0 > x0C (autonomous seizure triggering).
- Network coupling: **permittivity coupling** K_ij = G·C_ij (global scalar G × dMRI connectome C); seizure spread via slow z-coupling. Delays neglected for spread.
- EZ/PZ/other classes: EZ x0 ≥ x0C+0.4; PZ x0C < x0 < x0C+0.4 (patient: right hipp Δ1.3, left hipp/hypothal Δ0.4...; other Δ-0.2).
- **Bayesian inversion** (Stan; HMC + ADVI) of the spatial x0 map from SEEG high-frequency power (>10 Hz, log-detrended, baseline-corrected); observation model with SEEG forward solution; uninformative priors; posterior violin plots per region; identifies bilateral mesial temporal EZ — agrees with clinical reading; correct seizure propagation reconstructed.
- Validation: Proix et al. (under review 2016), **N=15 patients**: VEP-predicted EZ/PZ correlates with SEEG expert opinion; individual DTI connectomes improve prediction significantly.
- Parameter-space navigation charts (G, Ghyp, x0_RH, x0_other) → clinical decision tool; **non-bijective model↔physiology mapping explicitly acknowledged** (x0 ↔ excitation/inhibition balance, synaptic efficacy, ions, glia).
- Lesion integration: hypothalamic hamartoma via local coupling scalar Ghyp.
- TVB pipeline: github.com/timpx/scripts; FreeSurfer+FSL+MRtrix.

### 2. Myrov et al. — "Hierarchical whole-brain modeling of critical synchronization dynamics in human brain" (bioRxiv 2024.05.08.593146v4, compiled 2025-04-24; PNAS-format)
- File `2024.05.08.593146v4.full.pdf` (12 pp). The biorxiv-blocked paper, now read from source.
- **Hierarchical Kuramoto**: each node = population of coupled oscillators. Three terms: Natural (ω), Internal = (K/N)Σ sin(φ_i - φ_j) (**K = local/intra-node coupling**), External = Σ_j L_nj·W_nj·sin(φ_i - Φ_j)·R_j (**L = global/inter-node coupling**, W = SC weight, R_j = node order), + white noise. Complex-valued implementation.
- **KL surface**: order + DFA exponent as functions of (K, L). **Critical regime defined operationally: >10% of nodes with DFA exponent > 0.65** (surrogate 95th pct of white noise); ridge structure; inter-subject variance maximal at criticality.
- Phase transition: node order (low→high sync); DFA peaks ≈1 at transition; inter-node PLV/CC transitions.
- **Structure-function coupling**: node-order vs node strength ~0 in low-L region, rises supercritically; **DFA-vs-structure correlation peaks AT criticality**; edge CC vs edge weight peaks at criticality; PLV-vs-SC peaks subcritical, dips at critical peak. Null models (shuffled SC, uniform random): correlations non-significant → realistic topology required.
- **MEG comparison (N=24 models, individual SCs)**: best match on the **subcritical side of the extended critical regime** (theta 3-8 Hz for DFA/phase-sync; theta 4.2/alpha 12.3/beta 28.3 for CC); spectral multi-peak structure best matched at criticality (PSD correlation); alpha-peak alignment optimal near-critical.
- Frequency distributions sampled per-parcel from MEG PSD (FOOOF 1/f-removed) → multi-peak spectra preserved.
- Implication for us: **a per-subject, per-frequency distance-to-critical-ridge estimator on real connectomes is published methodology** — the J/J_c arm of the map.

### 3. Deco et al. 2018 — "Whole-Brain Multimodal Neuroimaging Model Using Serotonin Receptor Maps Explains Non-linear Functional Effects of LSD" (Current Biology 28:3065-3074)
- File uploaded under the name "The_Dream_That_Must_Be_Critique_Steelman_Survival_Test.pdf" (19 pp) — content is the cell.com-blocked paper (my own Survival Test PDF remains intact in download/).
- DMF model: 90 AAL regions; nodes = mean-field of I&F populations (80% exc / 20% inh); SC from dMRI tractography (n=16); **two parameters only: G** (global coupling, same for all fibers) **and sE** (neuromodulator gain-scaling added to regional gains, weighted by empirical 5-HT2AR density).
- Fitting: placebo FCD (Kolmogorov-Smirnov distance over FCD distributions; sliding-window 30-TR FC) → **G = 2.1**; then LSD condition fit by **sE ≈ 0.2** with G fixed → non-linear receptor-density-scaled gain change explains LSD FCD.
- Controls: **200× shuffled 5-HT2AR maps significantly worse** (Wilcoxon); uniform map worst; 5-HT1A better than 1B/4/T but worse than 2A; 50/50 train-test generalization holds.
- 5-HT2AR atlas: Beliveau et al., [11C]Cimbi-36 agonist radioligand, HRRT PET, 210 subjects, MNI.
- Code: github.com/decolab/cb-neuromod. LSD 75 μg IV, music condition (also confirmed without music).
- Implication: **the psychedelic arm's parameter map exists in published, replicated form: receptor density → regional gain; drug state → single scalar sE.**

### 4. Preller et al. 2018 — "Changes in global and thalamic brain connectivity in LSD-induced altered states of consciousness are attributable to the 5-HT2A receptor" (eLife 7:e35082)
- File `elife-35082-v3.pdf` (31 pp). The 406-blocked paper, now read from source.
- Design: double-blind randomized crossover; **n=24**; (i) Pla+Pla, (ii) Pla+LSD (100 μg po), (iii) Ketanserin+LSD.
- Method: **GBC (global brain connectivity)**, data-driven, with GSR; TFCE-permutation protected (10,000).
- Results: LSD **hyper-connectivity in sensory/somatomotor** (occipital, STG, postcentral, precuneus) + thalamus; **hypo-connectivity in associative** (mPFC/lPFC, cingulum, insula, TPJ) + subcortical; **ketanserin fully blocks both neural and subjective effects** (5D-ASC: all scales except spiritual experience/anxiety, Pla vs Ket+LSD all p>0.90); LSD>Pla and LSD>Ket+LSD Z-maps correlate r=0.91 (p<0.001); hyper/hypo anti-correlated across subjects r=-0.90 → systems-level perturbation.
- Spatial pattern of LSD effects matches **5-HT2A (HTR2A) cortical gene expression** (AHBA mapping, Burt et al. 2018) — preferentially for 5-HT2A vs other receptors.
- Implication: receptor attribution with causal blockade in humans — the **intervention-validated** anchor for the psychedelic arm's key variable.

### 5. Riedl et al. 2015/2016 — "Metabolic connectivity mapping reveals effective connectivity in the resting human brain" (PNAS 113(2):428-433)
- File `riedl-et-al-2015-...pdf` (6 pp). New addition (not previously on any list).
- **MCM**: spatial correlation between voxel-wise FC (fMRI) and FDG-PET metabolism, acquired simultaneously; **postsynaptic energy assumption** (up to 75% of signaling energy consumed at target neurons) → metabolic load marks the afferent/target side of directed signaling; voxel-wise, whole-brain, per-subject (unsmoothed, no spatial normalization).
- Validation: eyes-open vs eyes-closed; persistent bidirectional early↔higher visual; stable frontoparietal top-down; **salience-network top-down onto early visual only in eyes-open**; consistent with tracer hierarchies.
- Implication: an **alternative, non-DCM route to directional weights** (the coupling matrix's asymmetrization) usable as a prior for the map's J-direction structure — and an energy-based observable (FDG) matching the GL free-energy's "energy" reading.

## Round-17 verdict being folded in (from NEURAL_PARAMETER_MAP_REPORT.md)
- Literal unified (J,g,a,β,θ,φ)→neural map: **does not exist anywhere**; θ, φ have NO published neural assignment.
- Five program-area fragments verified (with fetch tests): anesthesia NFT (Bojak-Liley 2005 PRE 71:041902; Bojak 2013 Front Comput Neurosci; Robinson 2001 PRE 63:021903); DMF G-fitting (adrianponce/neurolib; Deco-Kringelbach 2025 book; Luppi 2022 Commun Biol; Eisen 2024 Neuron PMC11923585); psychedelic receptor parameterization (Deco 2018 Curr Biol; Herzog 2023 Sci Rep; Preller 2019 PNAS PMC6377471); TVB/VEP patient-level (Jirsa 2017; Penas 2024 PLOS Comput Biol PMC11265693; BVEP); critical coupling on connectome (Ódor 2019 Sci Rep PMC6928153; Haldeman-Beggs 2005 PRL 94:058101; Dörfler-Bullo via NTNU mirror).
- Unfetchable (13): cell.com 403, pnas.org 403, sciencedirect 400/403, biorxiv 403, researchgate 403, epubs.siam.org 403, wiley×2, liebertpub 403, ora.ox.ac.uk 403, biologicalpsychiatrycnni.org 403, jmsgr.tamhsc.edu no-route, ETH collection 403; pubmed challenge-gated.
- Four of the load-bearing blocked papers have NOW been supplied by the user and read (Jirsa, Myrov, Deco, Preller). Remaining blocked load-bearing items needing user supply (if wanted): none blocking — all protocol-critical papers now read; remaining unfetched are peripheral (Fabus thesis, Avram 2024 CNNi, Bedford 2023 Sci Rep full text, Liang 2015 PK-NMM, Butler 2025, Piccinini 2025 Nature).

## Level-2 protocol grounding
- decombination.txt consolidated spec: F[Ψ] = Σ g/4(||Ψ_i||²-a)² + J/2 Ψ^T L Ψ; projected Langevin dΨ = -P∇F dt + √(2/β) P dW; H = JL - gaI; domains form when J < J_c = ga/λ₂; amplitude c² ∝ (ga - Jλ₂)/gΣ(v⁽²⁾)⁴; two thresholds (bifurcation vs coherence Jβ); honest theorem D+I+S+P ⇒ candidate subject; requirements 1-4.
- elevation_cost.txt Level 2: map β↔arousal, J↔effective connectivity, a↔attractor depth (proposals, "derived from known biophysics", not arbitrary).
- Dataset search: psychedelics 8 open (ds006072, ds006110, ds003059, ds006644, ds007768, ds005917, Mendeley zxt5zsfhjr, Mendeley dmk2dmzzwn+Farnes Dryad); anesthesia 13 open (incl. ds006623, ds005620, ds003171, ds004541); split-brain: none (IDEAS ds005602/ds007401 = surgical candidates, not callosotomy); DID: none open.
- Santander 2025 (read round 12): ~10% posterior callosal fibers sustain full integration; criticality analysis code tsantander/splitBrainNetworks.
- Modesti 2022 (read round 12): DID n=51, caudate switching + prefrontal/ACC findings (the switch instrument).
- Schlumpf 2013 + Reinders 2019 (read round 13): DID part-dependent fMRI signatures; GPC 72.8%.
