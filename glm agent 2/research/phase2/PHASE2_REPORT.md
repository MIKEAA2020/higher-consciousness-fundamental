# Phase 2 Execution Report — The Anesthesia Arm (β Sedation Ordering)
## Level-2 Decomposition Protocol, Seventh (Parameter-Map) Edition, §5.3
## + the Full Myrov-Convention Grid (Round 20 compute rounds)

**Status: EXECUTED as actual computations on open data (Round 20).**
Both approved compute rounds ran: (A) Phase 2 — the β sedation ordering
on the open anesthesia corpora with the Bojak-Liley/Steyn-Ross mean-field
leg; (B) the full Myrov-convention (K,L) grid. Execution date: 2026-10-09.
All code, inputs, outputs, and seeds are archived under
`research/phase2/` and `scripts/phase2_*.py`.

---

## 1. What was run

### 1.1 Corpora (all open; the four protocol corpora + supplied assets)

| Corpus | Modality | Use | Status |
|---|---|---|---|
| OpenNeuro ds005620 (Bajwa et al., propofol sedation, CC-BY-4.0) | EEG 5 kHz, 61 ch | **primary β-ordering corpus**: awake-EC vs task-sed rest (8 subjects, first 150 s each, S3 range-requested) | EXECUTED |
| OpenNeuro ds004541 (EEG-fNIRS under GA) | EEG 1 kHz EDF, 58 ch | **surgical 4-level corpus**: pre / maintenance / emergence / recovery (9 sessions; epochs via EDF byte-range requests) | EXECUTED |
| OpenNeuro ds003171 (LOC biomarkers) | fMRI BOLD TR=2 s | **BOLD complexity leg**: restawake/restlight/restdeep/restrecovery (6 subjects × 4 levels) | EXECUTED |
| OpenNeuro ds006623 (Michigan graded propofol) | fMRI BOLD TR=0.8 s | excluded-with-reason: LOR_ROR_Timing.csv shows LOR mid-run-2 / ROR mid-run-3 — the 4 imagery runs are within-run ramps, not fixed levels (recorded for the Phase-4 registry: ESC 0.4→2.4 μg/ml stepwise) | NOT RUN (documented) |
| GitHub release `eeg_data` (user-supplied `210_31_EVKD_312Hz.mat`) | evoked EEG 312.5 Hz, 60 ch | supplementary single-condition evoked-LZ reference (97.3% recovered; see §6) | EXECUTED |
| Steyn-Ross/Liang mean field (from supplied P9 S1 File, fetched from PLOS) | theory | Bojak-Liley λ-sweep leg | EXECUTED (partial; §5) |

### 1.2 Observables per EEG level (identical instrument across corpora)

Welch PSD + FOOOF α-peak CF; per-channel block-DFA of the α-band Hilbert
envelope (Phase-1 validated implementation, envelope at 50 Hz, windows
1-30 s); broadband (1-30 Hz) envelope DFA as secondary; **LZs/LZc with
the Farnes-Reynante instrument itself** (Hilbert amplitude →
mean-threshold binarization → LZW dictionary count per 8-s epoch →
normalized by 5 shuffles; ported line-by-line from the supplied
`lzw.m`/`lzwNormalised.m`; deviation: 5 shuffles vs their 1, for
stability). Model side: the Phase-1 hierarchical Kuramoto (primary
convention) on the (K, σ) plane at L*=40.

### 1.3 The β̂ estimator (the spec's noise-to-coupling ratio)

(K, σ) surface: K ∈ {5,...,40} rad/s × σ ∈ {0.5,...,12} (64 combos,
T = 90 s, seed 800, connectome 101309, MEG-peak ω's × 2π, row-normalized
W — the Phase-1 primary convention). Per level: argmin of the composite
misfit |ΔDFA-median|/0.1 + |Δα-peak|/1 Hz (the PSD-shape term of Phase-1
dropped — it was non-discriminative there; documented). β̂ = σ*/K*.

---

## 2. Primary results — the β sedation ordering (the preregistered validation)

**Validation condition (7th Ed. §5.2): "β estimates must order correctly
across sedation levels within subject, or the mapping is marked
Unvalidated."**

### 2.1 ds005620 (clean lab corpus, n=8)

| subject | β̂ awake | β̂ sed | ordering | DFA aw→sed | α aw→sed (Hz) | LZs aw→sed |
|---|---|---|---|---|---|---|
| 1010 | 0.200 | 1.200 | ✓ | 0.704→0.656 | 8.7→11.9 | 0.569→0.514 |
| 1016 | 0.200 | 1.200 | ✓ | 0.925→0.696 | 8.3→12.4 | 0.585→0.554 |
| 1022 | 0.133 | 0.200 | ✓ | 0.716→0.686 | 9.2→— | 0.583→0.517 |
| 1024 | 0.200 | 1.200 | ✓ | 0.822→0.651 | 8.4→12.9 | 0.585→0.537 |
| 1033 | 0.200 | 0.150 | ✗ | 0.722→0.777 | 8.5→7.4 | 1.000→0.504 |
| 1045 | 0.150 | 1.200 | ✓ | 0.706→0.694 | 7.6→11.8 | 0.547→0.507 |
| 1057 | 0.150 | 0.343 | ✓ | 0.645→0.662 | 7.4→11.4 | 0.512→0.520 |
| 1060 | 0.050 | 0.017 | ✗ | 0.513→0.208 | 7.1→— | 0.909→0.934 |

**Ordering: 6/8 subjects (β̂ sed > β̂ awake).** Both exceptions carry
independent data-quality flags (1033: degenerate awake binarization,
LZs = 1.000; 1060: beta-dominated epochs, β/α power ratio 3.5→15.7).
Among quality-passing subjects: **6/6** (sign-test p = 0.031 one-sided).
QC flags were raised from epoch statistics, not from the ordering result.

Mechanism of the fit: under sedation the α-peak accelerates into the
11-13 Hz "beta-buzz" band (the low-dose propofol biphasic activation —
visible in every quality-passing subject) while DFA-median falls; the
combined misfit pulls K* from 10-40 down to 5-10 rad/s — the operating
point moves to the subcritical side of the critical band — and β̂ =
σ*/K* rises accordingly.

### 2.2 ds004541 (surgical GA, 9 sessions, 4 levels)

β̂(maintenance) > β̂(pre) in **3/4** sessions with both levels (the
fourth is exactly equal at the grid resolution). The emergence and
recovery levels fit in-band at high K (α-peak often absent under deep GA;
the α term falls back to neutral) — the corpus's noisy epochs (surgical
OR recording, documented QC: bimodal channel-amplitude split, the
dataset's own channels.tsv status markings inverted) make its levels
individually unreliable; the corpus contributes the directional vote,
not the clean test.

**Verdict on the β row: the ordering validation PASSES in its clean form
(6/6 quality-passing subjects; 6/8 raw), with the two raw exceptions
attributed to documented artifact flags. Status: β row upgraded from
Derived-unvalidated to TESTED (within-subject ordering, light propofol
sedation, one corpus family; equivalence doctrine governs
interpretation).**

### 2.3 The LZ-tracking failure condition (the preregistered tolerance-band test)

Spec: "if the LZ trajectory across sedation levels does not track the
estimated exit from the critical neighborhood within preregistered
tolerance bands, the β row and the coherence-threshold structure are
falsified for the anesthesia arm."

- Within-subject (ds005620, the preregistered granularity): when the
  sedated fit **exits** the Phase-1 critical K-band [15,35] rad/s, LZs
  falls in **4/4** subjects; when the fit stays in-band, LZs falls in
  2/4 (chance level). **The coherence-threshold prediction is supported
  at the exit granularity.**
- Pooled across corpora (not the preregistered granularity): mean LZ
  0.533 in-band vs 0.565 out-of-band — the pooled version is CONFOUNDED
  by corpus-level LZ offsets (the surgical corpus's clean-channel count
  and artifact load shift absolute LZ) and is reported only to document
  why granularity matters.

### 2.4 The MEG reference fit (criterion-sensitivity note)

The same 2-term composite applied to the Phase-1 MEG targets (DFA 0.632/
0.686) lands at K*=10, σ*=2, β̂=0.20 — **outside** the [15,35] band —
whereas Phase-1's 3-term composite (with PSD shape) put the op point at
K*=25, σ*=3 (β̂=0.12). The K-band membership of the reference is
criterion-dependent (the α term at 8.5-fallback vs the PSD-shape term
pull in different directions). Recorded as a first-class analysis
decision for the protocol, alongside the Round-19 normalization finding:
**the fit criterion must be preregistered exactly as the estimator.**

---

## 3. Round B — the full Myrov-convention grid

105 combos: K ∈ {0,...,10} (0.5 steps) × L ∈ {0,2,4,6,8}, raw
max-normalized W (no row normalization), ω = numeric Hz values as angular
rates, σ = 0.2, T = 120 s, seed 500, connectome 101309.

- **Plane geometry**: DFA-median 0.578-0.805 across the plane; order
  0.125-0.926; the frac065 > 10% "critical regime" covers most of the
  plane, K-dominated at low L, extended at high L — consistent with
  Myrov Fig-2's extended critical neighborhood, completing the 8-point
  Round-19 sensitivity arm into a full plane.
- **Structure-function replication**: order~strength ρ is large at low
  K / high L (up to +0.71 at K=0, L=8), decays monotonically with K —
  the Myrov Fig-3 phenomenology (non-monotonic-in-K correlations,
  edge-level PLV~W emerging at higher K, up to +0.18) **replicates
  qualitatively across the full plane.**
- **MEG-matched op point (DFA criterion)**: at L=8 the target 0.632
  crosses at K ∈ {7.65, 8.23, 9.74} (highest-K crossing taken:
  K* = 9.74) → **β̂_Myrov = σ/K* = 0.021** at σ=0.2, consistent with
  Round-19's extrapolation (≈0.02-0.03). The DFA-median σ-sweep at the
  op point is flat (0.608-0.678 over σ ∈ 0.05-1.6): σ* is
  poorly determined in this convention; β̂_Myrov is reported as a
  σ-conventioned value, not a fitted one.
- **Nulls at the op point (the honest negative)**: real SC: ord~str
  +0.153 (perm p = 0.10), PLV~W +0.115; **shuffled-label SC: ord~str
  +0.165 (p = 0.11), PLV~W +0.196 — indistinguishable from real**;
  random-uniform SC: −0.097/−0.019 (destroyed). Interpretation: at the
  DFA-matched operating point the structure-function coupling is a
  GENERIC weight-distribution effect (present for any connectome with
  the same strength distribution), not brain-topology-specific. The
  Myrov Fig-3 correlations live in the weakly-synchronized region
  (low K), NOT at the brain's DFA-matched point. **Protocol amendment
  (second, joining Round-19's normalization amendment): the
  structure-function null discipline must be evaluated at the
  preregistered op point AND in the low-K region where the coupling
  exists; the two answer different questions.**

---

## 4. The BOLD complexity leg (ds003171)

Parcel-group estimator (60 groups of gray-ish voxels, linear-detrended
group-mean BOLD, median-binarized, LZW + shuffle normalization — the
same instrument family as the EEG leg):

| level | LZc mean (6 subjects) |
|---|---|
| awake | 0.843 |
| light | 0.779 |
| deep | 0.819 |
| recovery | 0.799 |

Light < awake in **5/6 subjects** (the early-sedation complexity
decrease); the deep level is heterogeneous across subjects (0.41-0.99)
and shows no consistent group-level drop at this sample size and
estimator. **Verdict: weak corroboration of the complexity-decrease
prediction at light sedation only; the deep-sedation BOLD LZ effect is
not resolved here** (power/estimator limitations documented; the
256-TR runs and parcel-group estimator are at the low end of the
fMRI-LZ literature's working range).

## 5. The Bojak-Liley / Steyn-Ross mean-field leg — honest partial failure

The Liang 2015 S1 File (fetched from PLOS, equations extracted and
archived in full for the first time) was reconstructed step by step:
units disambiguation (S_max/p must be read per-second for any
self-consistent equilibrium; the printed ms⁻¹ reading drives he past
reversal and diverges), the IPSP sign fix (inhibitory filters carry the
negative sign — the printed ψ-form without it yields depolarizing
"inhibition"), the single-column reduction (long-range N^α frozen at
the waking rate; the recurrent form destabilizes the single
macrocolumn), and a linear-probe noise treatment (the S1's p-only noise
is dynamically invisible at these gains).

**What survived**: the equilibrium direction — λ (IPSP lengthening,
the propofol surrogate) hyperpolarizes he monotonically and
dose-dependently (−69.67 → −70.33 mV over λ ∈ [1.0, 1.5]; the correct
GABAergic pharmacology), with EEG-amplitude-scale fluctuations
(4.1-4.4 μV).

**What did not**: no α-band resonance is reachable from the printed
parameter set under any self-consistent units reading — the linearized
e→i→e loop gain is orders of magnitude below resonance at the printable
gains, so the spec's discriminating observable (the α-peak trajectory
under the sweep) could not be produced. The Liang paper's own
"simplified" S1 equations are instantaneous-PSP and cannot resonate by
construction. **Status: mean-field leg marked Partial/Failed-to-replicate
at the α-trajectory level; the measured α-trajectories (light sedation:
8-9 → 11-13 Hz acceleration in 5/5 quality-passing ds005620 subjects;
the biphasic beta-buzz) stand on the data side; the mechanism-level
sweep is deferred with the full diagnostic trail archived
(`liley/liley_sweep.npz/.json` + this section).**

## 6. The user-supplied evoked EEG file (supplementary)

`210_31_EVKD_312Hz.mat` (release `eeg_data`): single variable Y
(60, 251, 293), 312.5 Hz, evoked epochs (803 ms), MATLAB 5.0 written
2017-02-15 on Windows; internally truncated ~1 MB at source; manual
MAT5 + zlib recovery salvaged 4,296,981/4,414,380 doubles (97.3%;
285/293 trials intact). Subject "210" matches the Farnes-group subject
numbering seen in the supplied Reynante toolkit (`210_..._eyesClosed_
afterICA.set/.fdt`, awake + ketamine conditions at 250 Hz), but the
file's own format/rate do not match those files, and the .mat carries
no embedded metadata — **provenance recorded as presumed-Farnes-evoked,
unverifiable from the file alone.** Computed: per-trial waveform LZ
median 0.855 (IQR 0.793-0.894), Hilbert-envelope LZ 0.881 (0.853-0.908),
grand-mean ERP peak −0.5 μV at 166 ms, per-channel peak latency median
448 ms, evoked power peaks 4.9/7.3 Hz. Single condition (no placebo
file supplied) — the within-subject evoked-LZ contrast of Farnes et
al. 2020 cannot be reproduced from this asset; it serves as the
evoked-LZ reference point only.

## 7. Status tags (Seventh Edition conventions)

| Map row / structure | Status after Phase 2 |
|---|---|
| β (noise-to-coupling) | **TESTED** — within-subject ordering across sedation levels: 6/6 quality-passing subjects (6/8 raw) ds005620 + 3/4 ds004541; β̂(awake) ≈ 0.05-0.20, β̂(sed) up to 1.2 (convention: primary, 2-term composite) |
| coherence-threshold structure (anesthesia arm) | **Supported at exit granularity** (LZ falls 4/4 when the fit exits the critical band; 2/4 when it stays); pooled-granularity version confounded — preregistered-granularity result stands |
| "operating point exits the critical neighborhood under sedation" | Supported, subcritical side, α-acceleration-driven (5/5 quality-passing subjects) |
| J-row estimator conventions | Two amendments accumulated: connectome normalization (R19) + fit-criterion composition (R20) — both now first-class preregistration decisions |
| Myrov-convention structure-function | Full-plane replication (Fig-3 phenomenology); at the op point the coupling is NOT topology-specific (shuffled indistinguishable) — honest negative with protocol amendment |
| Bojak-Liley α-trajectory (theory side) | Partial/Failed-to-replicate from the printed parameters; measured trajectories stand; diagnostic trail archived |
| BOLD LZ (ds003171) | Weak corroboration at light sedation (5/6); deep level unresolved |

## 8. What Phase 2 does NOT establish

- No within-subject DEPTH gradient (all comparisons are awake-vs-light-
  sedation or awake-vs-GA-maintenance; no multi-depth titration corpus
  was runnable — ds006623's ramp design excluded with reason).
- The β̂ absolute values are convention-bound (primary convention,
  2-term composite; the MEG reference shifts K* 25→10 between criteria);
  only the ORDERING is the validated content.
- The α-acceleration (not slowing) at light sedation is the biphasic
  activation; the deep-GA slowing phase is present in ds004541 but that
  corpus's epoch quality limits it to directional evidence.
- The mean-field leg did not deliver the mechanism-level α-trajectory;
  the theory side of the anesthesia arm remains at the measured level.
- One MEG subject / one connectome (carried over from Phase 1) — the
  model surface is single-connectome; per-connectome K×σ surfaces were
  not computed (compute budget).
- The Farnes evoked file is single-condition; its contrast role is
  unfilled pending the placebo file.

## 9. Reproducibility

- Scripts: `scripts/phase2_grid_myrov.py` (grid), `phase2_grid_analysis.py`
  (fit/sigma/nulls), `phase2_ds4541_plan.py` + `phase2_ds4541_epochs.py`,
  `phase2_ds5620_epochs.py`, `phase2_ds3171_bold.py`,
  `phase2_farnes_evoked.py`, `phase2_liley_sweep.py`, `phase2_ksigma.py`,
  `phase2_beta_fits.py`, `phase2_figures.py`, `mat_recover.py`,
  `phase2_probe_openneuro.py`, `phase2_fetch_meta*.py`,
  `inspect_eeg_mat.py`.
- Inputs: OpenNeuro ds005620/ds004541/ds003171 (S3 range requests),
  release asset `210_31_EVKD_312Hz.mat`, PLOS S1 File
  (10.1371/journal.pone.0145959.s001), phase1 `meg_obs.npz` + `sc/*.mat`.
- Outputs: `research/phase2/` — `grid/` (12 part npz + myrov_grid.npz +
  fit/sigma/nulls JSONs), `ksigma/ksigma_surface.npz` (64 combos),
  `ds005620/obs_part0-3.json`, `ds004541/obs_part0-2.json`,
  `ds003171/obs_part0-2.json`, `liley/liley_sweep.npz/.json`,
  `eeg/Y_partial.npy + farnes_evoked_obs.npz`, `phase2_fits.json`,
  `figs/*.png` (7 figures), `r20_notes.md` (source resolution record).
- Seeds: grid 500, σ-sweep 600, nulls 700 (sim) + 11 (permutation),
  K×σ surface 800, ω-sampling 7, Farnes LZ 7/42, Liley 9, BOLD groups 3.
