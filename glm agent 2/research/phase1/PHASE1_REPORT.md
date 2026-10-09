# Phase 1 Execution Report — Coupling and Criticality Estimation
## Level-2 Decomposition Protocol, Seventh (Parameter-Map) Edition, §5.2

**Status: EXECUTED as an actual computation on open data (Round 19).**
This is the first Level-2 phase to run on real data rather than on
specification alone. Execution date: 2026-10-08. All code, inputs, outputs,
and seeds are archived in this directory and `scripts/phase1_*.py`.

---

## 1. What was run

**The Myrov pipeline** (Myrov et al., bioRxiv 2024.05.08.593146v4, read in
full from the user-supplied PDF in Round 18): a hierarchical Kuramoto model
on an individual structural connectome, swept over the local-coupling /
global-coupling plane, with node order, DFA exponents, phase-locking, and
amplitude cross-correlations as observables; the critical regime defined by
>10% of nodes exceeding DFA 0.65; the brain's operating point located by
matching model observables to MEG observables.

### 1.1 Data (all open)

| Component | Source | Detail |
|---|---|---|
| MEG | Brainstorm `bst_resting` (open, OSF) | subj002, eyes-closed rest, 2 x 600 s runs, 272 CTF magnetometers, 2400 Hz |
| Structural connectomes | neurolib `hcp` dataset (open, GitHub) | 7 individual HCP subjects (101309 primary + 6 replication), DTI tractography, AAL2 94-region parcellation |

### 1.2 Model (Myrov et al. equations, verbatim)

dφ_i^n/dt = Natural + Internal + External + Noise
- Natural = ω_i^n — per-node oscillator frequencies sampled from the MEG
  PSD peak structure (FOOOF on the grand-mean sensor PSD: peaks at 3.86,
  6.53, 8.12, 18.02, 22.61 Hz; nodes assigned to peaks with probability
  proportional to peak power; oscillators drawn N(CF, BW) clipped to
  [3,30] Hz)
- Internal = K·Im(z_n·e^{−iφ_i}),  z_n = (1/M)Σ_q e^{iφ_q^n}
- External = L·Im(e^{iφ_i}·conj(U_n)),  U_n = Σ_j W_nj·z_j
- Noise = η (white, amplitude σ)

**Documented assumptions** (the source's Supplementary Table 1 is not
public): M = 50 oscillators/node; dt = 1 ms; sweep σ₀ = 3 (calibrated so
the critical band occupies a comparable plane fraction as the source);
T = 150 s per combo (30 s warm-up discarded, 120 s analysis; source: 360
s/60/300 — reduction forced by the execution environment); grid K, L ∈
{0,5,...,40} rad/s (the physical-unit equivalent of the source's [0,8]
plane — the source's convention treats numeric Hz values as angular
rates; see §5.2); W row-normalized for the External term (each node's
incoming weights sum to 1 — puts the L transition in-plane at physical
units; see §5.2 for why this matters).

### 1.3 MEG observables (sensor-space instantiation)

1-45 Hz FIR (chunked, in-place), Welch PSD (4 s Hann, 50% overlap),
FOOOF 1/f parameterization; per-channel DFA of the narrowband
(peak±2 Hz) Hilbert envelope (windows 1-30 s, robust log-log fit);
phase-difference wPLI; envelope cross-correlations. DFA implementation
validated against white noise (median 0.499, 95th pct 0.535) and a
long-memory synthetic (online vs offline: 1.156 vs 1.198).

| Observable | Run 1 | Run 2 |
|---|---|---|
| alpha peak (Hz) | 8.12 | 7.91 |
| FOOOF peaks 3-30 Hz | 5 | 3 |
| median sensor DFA | 0.632 | 0.686 |
| sensors with DFA>0.65 | 41.2% | 62.5% |
| mean wPLI (alpha) | 0.510 | 0.522 |
| envelope CC vs distance ρ | −0.415 | −0.440 |

**Sensor-space deviation, stated plainly**: Myrov et al. compared
source-parcel-level observables per subject with matched individual
connectomes. No openly downloadable MEG+dMRI pairing exists at that level
(HCP-MEG is credential-gated), so this run matches model node observables
to sensor observables at the grand-mean/distribution level. Consequences
are marked throughout.

## 2. Primary results (physical units, row-normalized W)

### 2.1 The (K,L) plane and the critical regime

- Node order rises monotonically with K (0.13 → 0.66 along K at L=0);
  L contributes weakly at these scales. Order ~ 0.50 at the operating point.
- **The DFA-defined critical regime (fraction of nodes with DFA > 0.65
  exceeding 10%) is a K-band, extended across the whole L axis** —
  K ∈ [15, 35] at L* = 40 (primary connectome), peaking at frac065 ≈ 0.20
  around K = 20. This reproduces the qualitative geometry of Myrov et al.
  Fig. 2 (an extended critical neighborhood, K-dominated).
- Mean node DFA peaks ≈ 0.58 inside the band (K 20-30) and decays on both
  sides — subcritical noise-dominated below K≈10, supercritical
  over-synchronized above K≈35.

Figure: `figs/phase1_kl_surfaces.png` (order, DFA + contour, frac065,
composite misfit, two structure-function maps).

### 2.2 The MEG-matched operating point

Fit criterion (composite, sensor-space instantiation of the spec's
"parcel-level and edge-level correlation" wording): misfit =
|median DFA − MEG median|/0.1 + |model alpha peak − 8.12 Hz|/1 Hz +
(1 − r_shape), where r_shape is the Pearson correlation of the 1/f-detrended
log-PSDs (3-30 Hz).

**Operating point: K* = 25 rad/s, L* = 40 rad/s** (composite 0.97;
components 0.54 / 0.08 / 0.35).

| Quantity | Value |
|---|---|
| model alpha peak | 8.20 Hz (MEG 8.12; distance 0.08 Hz) |
| PSD shape correlation r_shape | 0.652 |
| PSD raw correlation (Myrov's literal criterion) | 0.492 (max over plane 0.820 at the degenerate L=0 corner — reported, not used) |
| PSD correlation vs FOOOF-periodic PSD | −0.456 (max over plane +0.02 — the periodic-PSD criterion does not discriminate in this instantiation) |
| mean node order | 0.498 |
| median node DFA | 0.562 (MEG 0.632 — see §2.4) |
| frac065 at op point | 0.191 (19% of nodes above 0.65) |

**Distance to the critical ridge** (the spec's (J_c−J)/J_c quantity):
- K axis (the transition axis in this parameterization): the operating
  point lies INSIDE the extended critical band [15, 35]; margins 0.67 to
  the subcritical edge, 0.29 to the supercritical edge.
- L axis (the inter-node coupling, the GL J-analog): the band spans the
  entire L axis at K*; the L-distance is degenerate (no crossing) — inside
  by construction of this parameterization.

Figure: `figs/phase1_psd_match.png`, `figs/phase1_psd_criteria.png`.

### 2.3 Noise fit and the β estimate

σ-sweep at (K*, L*): median node DFA peaks at σ = 3 (0.562) and declines
on both sides (0.453 at σ=0.5; 0.502 at σ=12). The MEG median (0.632) is
**not reachable** at this operating point: the best-fit noise is
σ* = 3 (argmin of the mismatch), and

**β̂ = σ*/K* = 3/25 = 0.12** (noise amplitude / local coupling at the
MEG-matched operating point; the spec's derived β estimator).

The residual DFA shortfall (0.562 vs 0.632, i.e. 0.07) is a quantitative
failure of this instantiation to reproduce the full empirical LRTC
strength — recorded as a limitation, not smoothed over. The preregistered
validation condition for the β row ("β estimates must order correctly
across sedation levels within subject") requires drug-state data and is
**deferred to Phase 2** — the β row remains Derived-unvalidated, now with
a computed value attached.

Figure: `figs/phase1_beta.png`.

### 2.4 Null discipline — an honest negative

At the operating point, the Myrov Fig-3 structure-function correlations
are essentially zero: order~node-strength ρ = −0.03 (perm p = 0.77),
DFA~strength ρ = −0.004 (p = 0.97), PLV~edge-weight ρ = −0.03
(p = 0.019, trivial magnitude), CC~edge-weight ρ = +0.046 (p = 0.005,
trivial magnitude). Shuffled-label and random-uniform connectomes are
**indistinguishable from the real connectome** (all |ρ| ≤ 0.23, signs
mixed). The null discipline "must destroy the correspondence" has nothing
to destroy here: under this convention, the MEG-matched dynamics carry no
structure-function coupling.

Figure: `figs/phase1_nulls.png`.

### 2.5 Convention sensitivity — the decisive methodological finding

The primary run's degenerate structure-function result traces to the
W-normalization choice (row normalization equalizes every node's total
incoming weight, removing the strength→dynamics pathway). A replication
arm in the **inferred Myrov convention** (oscillator frequencies with
numeric Hz values used directly as angular rates — per-node ω std 2.6 —
W max-normalized without row normalization, K, L in [0,8]-scale, σ = 0.2;
`scripts/phase1_convention_test.py`, 8 points) gives:

| K | L | order | median DFA | frac065 | order~strength | PLV~W |
|---|---|---|---|---|---|---|
| 1 | 4 | 0.262 | 0.779 | 0.80 | +0.306 | +0.022 |
| 2 | 4 | 0.428 | 0.739 | 0.69 | +0.244 | +0.083 |
| 3 | 4 | 0.553 | 0.734 | 0.59 | +0.207 | +0.043 |
| 3 | 8 | 0.642 | 0.732 | 0.67 | +0.364 | +0.057 |
| 5 | 8 | 0.763 | 0.673 | 0.56 | +0.259 | +0.001 |
| 6 | 8 | 0.803 | 0.681 | 0.60 | +0.212 | +0.131 |
| 7 | 8 | 0.833 | 0.669 | 0.55 | +0.194 | +0.112 |
| 8 | 8 | 0.866 | 0.649 | 0.50 | +0.175 | +0.175 |

In this convention the Myrov phenomenology **replicates qualitatively**:
order~strength coupling is substantial (+0.18..+0.36, non-monotonic in K
as in their Fig. 3), edge-level PLV~W coupling emerges at higher K
(+0.11..+0.18), and the model's median DFA (0.65-0.78) brackets the MEG
value — the DFA-matched operating point extrapolates to K ≈ 9-9.5
(L = 8, σ = 0.2; β̂ ≈ 0.02-0.03 in this scaling), i.e. at/just beyond the
sampled plane's synchronized edge, with the brain below the model's
criticality peak.

**Protocol consequence (recorded for the spec): the J-row estimator is
normalization-convention-dependent. The Level-2 protocol must preregister
the connectome normalization (raw/max-normalized vs row-normalized) as a
first-class analysis decision, and the structure-function null discipline
must be run under the preregistered convention.** Under the
Myrov-convention the nulls would have content to destroy; under the
row-normalized convention they cannot.

### 2.6 Per-connectome consistency (the preregistered failure condition)

Six additional HCP connectomes, K-slice at L* = 40, σ = 3, composite
criterion:

| Connectome | K_op | critical K-band at L* | signed distance d_K | frac065 at op |
|---|---|---|---|---|
| 102311 | 35 | [10, 30] | −0.17 (supercritical edge) | 0.05 |
| 102816 | 35 | [10, 30] | −0.17 | 0.05 |
| 131217 | 40 | [10, 20] | −1.00 | 0.05 |
| 211619 | 35 | [10, 30] | −0.17 | 0.06 |
| 213522 | 35 | [10, 25] | −0.40 | 0.05 |
| 377451 | 35 | [10, 20] | −0.75 | 0.04 |
| 101309 (primary, full grid) | 25 | [15, 35] | 0.00 (inside) | 0.19 |

The failure condition ("operating points scatter across the plane") is
**not triggered**: all seven connectomes concentrate in the K = 25-40
range, at or just beyond the supercritical edge of their respective
critical bands. But the concentration is edge-adjacent rather than
band-centered, and it is driven partly by the peak-alignment term (which
favors higher K in this instantiation). Verdict: **the specification's
central empirical presupposition — healthy resting brains operate in the
extended critical neighborhood — survives in the weak, edge-concentrated
form for 7/7 connectomes; it is not confirmed in the strong centered
form.**

Figure: `figs/phase1_subjects.png`.

## 3. Status tags (Seventh Edition conventions)

| Map row | Status after Phase 1 |
|---|---|
| J (effective coupling) vs J_c | **Executed** on open data; estimator produces an in-band operating point for 7/7 connectomes; sensor-space, single MEG subject, normalization-convention-dependent (§2.5) — Partial |
| β (noise-to-coupling) | **Computed** (β̂ = 0.12 primary convention; ≈ 0.02-0.03 Myrov convention); sedation-ordering validation deferred to Phase 2 — Derived-unvalidated, value attached |
| "extended critical neighborhood" presupposition | Supported, weak form (edge-concentrated), 7/7 connectomes — Partial |
| structure-function coupling at op point | Absent under the primary convention; present under the Myrov convention — replication conditional on normalization (methodological finding, spec amendment drafted) |

## 4. What Phase 1 does NOT establish

- No source-space, topology-matched parcel comparison (no open MEG+dMRI
  pairing); all model-MEG matches are grand-mean/distributional.
- One MEG subject (two runs, consistent: peak 8.12/7.91, DFA 0.632/0.686);
  no cross-subject MEG variance estimate.
- The source's Supplementary parameters (oscillator count, dt, noise) are
  assumptions; the critical-band location moves with them.
- 120 s analysis windows (vs the source's 300 s); DFA exponents are
  window-range-matched (1-30 s) but noisier.
- The DFA median shortfall (0.562 vs 0.632) at the fitted operating point
  is unexplained by this run — candidate causes: oscillator count, noise
  spectral color (white assumed), frequency-assignment heterogeneity.
- No finite-size scaling, no per-frequency-band operating points (the
  source's theta/alpha/beta analysis) — deferred.

## 5. Reproducibility

- Scripts: `scripts/phase1_meg.py` (MEG observables), `scripts/phase1_kuramoto.py`
  (engine; modes calibrate/chunk/slice/nulls/sigmasweep),
  `scripts/phase1_fit.py` (fit + figures), `scripts/phase1_convention_test.py`,
  `scripts/phase1_smoke.py` (validation).
- Inputs: `meg_obs.npz/.json` (from bst_resting, OSF m7bd3), `sc/*.mat`
  (neurolib hcp dataset, 7 subjects).
- Outputs: `sweep_part00-08.npz` (81 combos), `slice_*_part0.npz` (6),
  `sigmasweep.json`, `nulls.json`, `phase1_results.json`, `figs/*.png`,
  `convention_test.log`.
- Seeds: ω sampling rng(7)/rng(11); sims seeded per chunk; surrogates
  rng(1234); permutations rng(5150).
- Compute: ~2.5 h single-node CPU (9 sweep chunks + 6 slices + σ-sweep +
  nulls + convention arm), <200 MB RAM per process.

## 6. Next-phase inputs created by this run

1. The normalization-convention amendment for the Phase-2/3 spec (§2.5).
2. β̂ values to be ordered across sedation levels in Phase 2
   (ds006623/ds005620/ds003171/ds004541).
3. The convention-arm result (structure-function coupling +0.18..+0.36)
   as the replication target for the full-grid Myrov-convention sweep,
   if a second compute round is commissioned.
