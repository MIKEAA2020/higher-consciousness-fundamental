# Round 20 — New Sources, EEG Release Identification, Appendix Resolution

## 1. Butler 5-HT2A article (P14) — SUPPLIED and read

User upload: `upload/level 2 decombiniation/S0278584625001915.html`
(ScienceDirect article page, Elsevier PII S0278-5846(25)00191-5).

**Full citation**: Butler JJ, Virgili M, Di Giovanni G, Chagraoui A,
Beyeler A, De Deurwaerdère P. **"5-HT2A receptors shape whole-brain
monoaminergic coherence in male mice."** *Progress in
Neuro-Psychopharmacology and Biological Psychiatry* 141:111437 (2025;
online 30 August 2025). DOI: 10.1016/j.pnpbp.2025.111437. Open access
(CC license). Read at abstract+highlights+abbreviations level from the
publisher page (full-text PDF remains behind the ScienceDirect block;
the page itself supplies the complete abstract, highlights, keywords,
the 28-region dissection list, and the full author/journal metadata).

**Content digest (P14)**:
- Design: post-mortem tissue quantification of serotonin (5-HT),
  dopamine (DA), noradrenaline (NA) and metabolites (5-HIAA, DOPAC,
  HVA, 3-MT, 5-HTP, L-DOPA) in **28 dissected brain regions** of male
  mice during **forced exploratory behavior** (the moving-animal
  instantiation of the group's neurochemical-connectivity method — the
  methods paper was P11, read R19).
- Vehicle organization: dense, highly organized pattern of correlations
  within and between monoamine systems across regions ("neurochemical
  coherence").
- **TCB-2** (5-HT2A agonist, 0.3 / 3 / 10 mg/kg): disrupts the
  monoamine correlation structure **dose-dependently**; decreases 5-HT
  turnover (5-HIAA/5-HT) across all regions; decreases striatal DA
  turnover (3-MT/DA); enhances DA/NA markers in select regions
  (notably anterior cingulate cortex); induces head twitches.
- **MDL-100,907** (5-HT2A antagonist, 0.2 mg/kg): also disrupts the
  correlation structure **without altering monoamine tissue levels**;
  reduces TCB-2-induced head twitches; increases ACC monoamine
  concentrations; does NOT reverse the TCB-2-induced 5-HT turnover
  decrease.
- **Combination (MDL + TCB-2): partially RESTORES correlations** —
  receptor-specific bidirectional modulation of whole-brain
  neurochemical coherence.
- Relevance to the parameter map: this is the receptor-perturbation
  logic of the psychedelic arm (Phase 3's Deco-style receptor
  parameterization + the ketanserin-anchor test) demonstrated at the
  **tissue neurochemistry level** in rodents: agonist disrupts
  coherence dose-dependently, antagonist blocks the behavioral
  signature and partly restores coherence. The desynchronization claim
  ("psychedelics may desynchronize activity between brain regions")
  is tested by the authors at the inter-region correlation level —
  exactly the J-coherence row of the map, cross-species.

Status: read at abstract level; source registered; the Appendix-A
"Butler 5-HT2A / monoaminergic dynamics" item is now RESOLVED.

## 2. EEG release asset — identification and repair

User release: `releases/tag/eeg_data`, asset `210_31_EVKD_312Hz.mat`
(33,423,360 bytes; sha256 verified identical to the GitHub-stored
asset).

- MATLAB 5.0 file, single variable `Y`, shape (60, 251, 293) double,
  EEG-scale values (−41.2 to +32.4 μV, mean 0.0003).
- The file is **internally truncated by ~1 MB at source** (the zlib
  stream declares 35,300,640 bytes of numeric payload; 34,375,849
  bytes are present). Manual MAT5 parse + fault-tolerant zlib recovery
  (scripts/mat_recover.py) recovers 4,296,981 / 4,414,380 doubles
  (**97.3%**; ≈ the first ~286 of 293 axis-2 slices intact).
  Recovered array saved as `phase2/eeg/Y_partial.npy`.
- Interpretation: 60 channels × 251 samples × 293 trials at 312.5 Hz
  (251 samples = 803 ms epochs; "EVKD" = evoked-ketamine-data naming),
  consistent with the **Farnes et al. 2020 Dryad raw EEG** (the
  evoked-EEG branch of the ketamine study; the dataset's zip
  `Farnes_et_al_PLOS_ONE_Dryad.zip` is what the filename style matches).
  The .mat contains no embedded metadata, so subject/condition labels
  are taken from the filename only — recorded as a presumption, not a
  verified fact.
- Role in Phase 2: single-condition supplementary computation
  (per-trial LZ complexity + DFA of the recovered evoked data); the
  within-subject placebo contrast is NOT possible from this file alone
  (only one condition file supplied).

## 3. Appendix-A remaining items after this round

After the Butler supply (P14) and the EEG release (partial Farnes raw
data), the remaining Appendix-A items are:

1. **Farnes et al. 2020 — raw EEG (Dryad; data item, now PARTIALLY
   supplied).** Full title: "Increased signal diversity/complexity of
   spontaneous EEG, but not evoked EEG responses, in ketamine-induced
   psychedelic state in humans." PLOS ONE 15(11):e0242056 (2020).
   Authors: Nadine Farnes, Bjørn E. Juel, André S. Nilsen, Luis G.
   Romundstad, Johan F. Storm. DOI: 10.1371/journal.pone.0242056.
   Links: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0242056
   (article); https://datadryad.org/dataset/doi:10.5061/dryad.j9kd51c9q
   (raw data zip `Farnes_et_al_PLOS_ONE_Dryad.zip`; the file_stream
   download 403s from this environment — the user-supplied release
   asset above is a partial workaround).
2. **ETH Zurich Research Collection (provenance-only item).** The
   Schlumpf 2013 doctoral-thesis provenance record
   (research-collection.ethz.ch — HTTP 403 to this environment for all
   items). The thesis version of the already-read paper "Dissociative
   part-dependent biopsychosocial reactions to backward masked angry
   and neutral faces: An fMRI study of dissociative identity disorder"
   (NeuroImage: Clinical 3:54-64, 2013); an open alternative record for
   the group's related work exists at
   https://www.zora.uzh.ch/entities/publication/5ae81efc-0b90-4ad9-a315-a5e12e39bc75
   (University of Zurich repository). Non-blocking: the paper itself
   was read in full in Round 12 from user supply.

Neither remaining item blocks the protocol.

## 4. Corpus inventory for the Phase-2 computation (probed this round)

| Corpus | Modality | Structure | Phase-2 role |
|---|---|---|---|
| OpenNeuro ds004541 | EEG (EDF, 1000 Hz, 58 ch) + fNIRS | 8 surgical patients, 9 sessions; events: baseline / start / loc / verbal-soft / verbal-strong / motor / tetanic / end / roc | **primary β-ordering corpus** (awake → maintenance → emergence → recovery) |
| OpenNeuro ds005620 | EEG (BrainVision, 5000 Hz, 61 ch) | 21 subjects; task-awake EC/EO (300 s) + task-sed rest runs + sed2 (1-min pre-awakening) — public snapshot CONFIRMED to contain sedation recordings | **awake vs sedated ordering** (propofol light sedation) |
| OpenNeuro ds003171 | fMRI BOLD (TR 2 s) | 17 subjects × 4 sedation levels (awake / light / deep / recovery), rest + audio | **BOLD complexity leg** (LZc ordering) |
| OpenNeuro ds006623 | fMRI BOLD (TR 0.8 s) | 26 subjects × 6 runs (4 imagery + 2 rest), graded propofol with behavioral concentrations (Huang et al.) | **BOLD complexity leg** (levels from behavioral files) |
| GitHub release eeg_data | EEG .mat (312.5 Hz, 60 ch, evoked) | 1 presumed-Farnes subject file, ketamine condition | supplementary LZ/DFA demo |

Download route verified: `https://s3.amazonaws.com/openneuro.org/{dsid}/{path}`
(HTTP range requests supported — epochs fetched without full-file
downloads). ds005620's README confirms task-sed naming (initial probe
regex missed lowercase acq-rest labels; corrected).

## 5. Answers owed to the user (round 20 message)

1. Seventh Edition on repo: **present** — pushed in Round 18 (commit
   0b6b316) as `download/Fundamental-Higher-Consciousness-Premise_Audit-and-Consolidation_Parameter-Map-Ed.pdf`
   (+ its cover HTML); Round 19's Phase-1 artifacts pushed in af148a3.
   Discoverability fix this round: README.md edition index (the file
   was 34 bytes with no listing). Verified byte-identical local/remote
   (217,063 bytes).
2. Two remaining Appendix-A papers: full titles/links in §3 above
   (Farnes 2020 + ETH provenance item) — Butler resolved by supply.
3. Phase 2 + full Myrov-convention grid: **both merited, both run**
   (user: "why not both if merited?").
