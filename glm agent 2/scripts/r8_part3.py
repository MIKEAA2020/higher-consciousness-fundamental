#!/usr/bin/env python3
"""Eighth Edition (Computed Edition), Part 3: chapter 3, sections 3.4-3.7
2014 the completed Farnes evoked-LZ contrast, post-execution status
tags, honest limits, and reproducibility. Embeds the two round-21 figures."""
import os

from reportlab.platypus import Image, KeepTogether, Spacer, Paragraph
from PIL import Image as PILImage

import fhcp_pdf_lib as L

FIGDIR = ('/home/z/my-project/glm agent 2/research/phase2/farnes/figs')


def figure(story, path, caption, max_h=250):
    """Block-level figure with preserved aspect ratio + caption (brief
    conventions: fit to available width, cap height, KeepTogether)."""
    pil = PILImage.open(path)
    ow, oh = pil.size
    ratio = min(L.AVAIL_W / ow, max_h / oh, 1.0)
    img = Image(path, width=ow * ratio, height=oh * ratio)
    img.hAlign = 'CENTER'
    story.append(Spacer(1, 14))
    story.append(KeepTogether([img, Spacer(1, 6),
                               Paragraph(caption, L.S['caption'])]))
    story.append(Spacer(1, 14))


def add_content(story):
    # ---- 3.4 the Farnes completion ----
    L.h2(story, '3.4 The Evoked-LZ Contrast, Completed (the Farnes Corpus '
                'Resolved)')

    L.body(story,
           'The seventh edition closed its execution record with an '
           'unfilled role: the round-twenty evoked file was '
           'single-condition, its provenance presumed rather than '
           'verified, and \u201cthe within-subject evoked-LZ contrast '
           'of Farnes et al. 2020 cannot be reproduced from this '
           'asset.\u201d The Raw_data_2 release closes the gap '
           'decisively. Its readme identifies the corpus and the '
           'conditions without residue: Farnes, Juel, Nilsen, '
           'Romundstad and Storm, PLOS ONE 15(11):e0242056, '
           '\u201cIncreased signal diversity/complexity of spontaneous '
           'EEG, but not evoked EEG responses, in ketamine-induced '
           'psychedelic state in humans\u201d \u2014 ten volunteers, '
           'TMS-EEG and spontaneous EEG before and during sub-'
           'anaesthetic ketamine, open-label within-subject. Recording '
           'ID 31 is the awake (placebo) condition; 32 is ketamine; '
           'the TMS pulse sits at the 126th sample of each 251-sample '
           'epoch; the spontaneous recordings are four per subject, '
           'the first two awake and the last two under ketamine, eyes '
           'open and closed. All 101 assets verified against the '
           'release\u2019s sha256 manifest.')

    L.h3(story, 'The R32 repair: the round-twenty mapping error')

    L.body(story,
           'Completing the contrast required first correcting the '
           'round-twenty analysis of the single supplied file. The '
           'EVKD matrices are MATLAB column-major arrays of shape '
           '(channels, times, trials); the round-twenty recovery '
           'script reshaped the flat double stream with row-major '
           'semantics and a transpose, which interleaves channels and '
           'samples \u2014 each \u201cchannel\u201d stream was in '
           'reality 251 consecutive samples spanning roughly four '
           'physical channels. The diagnosis is exact, not '
           'interpretive: re-running the round-twenty computation on '
           'the now-complete file reproduces its reported reference '
           'values to the third decimal (waveform LZ 0.855, envelope '
           'LZ 0.881), and the same data under the corrected '
           'column-major mapping yield 0.626 and 0.618. The corrected '
           'mapping also shows the structure the scrambled mapping '
           'could not: the pre-pulse baseline is flat to 0.006 '
           '\u03bcV RMS (the data are baseline-corrected), and the '
           'trial-averaged global field power peaks 64\u201383 ms '
           'after the pulse \u2014 the textbook TMS-evoked complex '
           '\u2014 at 20\u201325 \u03bcV<super>2</super>. The repair is logged '
           'as R32; the recovery itself is validated by the supply '
           '(the truncated eeg_data copy\u2019s 285 recovered trials '
           'are the exact prefix of the complete file\u2019s 293, and '
           'the truncated-prefix statistics equal the complete-file '
           'statistics to the third decimal).')

    L.h3(story, 'The completed contrast: a three-layer result')

    L.body(story,
           'The analysis applies the corpus\u2019s established LZ '
           'instrument \u2014 the line-by-line port of the supplied '
           'lzw.m / lzwNormalised.m code: Hilbert amplitude, '
           'mean-threshold binarization, LZW dictionary count, '
           'shuffle-normalized \u2014 to all ten subjects in both '
           'conditions, per trial, with the multichannel LZc (the '
           'Schartner-style channel concatenation) and the per-channel '
           'LZs, in three windows: the 400 ms before the pulse, the '
           '400 ms after it, and the full epoch. Statistics follow the '
           'paper\u2019s own design: Wilcoxon signed-rank across the '
           'ten subjects, with bootstrap confidence intervals. The '
           'result has three layers, and the layers are the finding:')

    L.data_table(
        story,
        'Table 3.2 \u2014 The evoked-LZ contrast, completed (n = 10 '
        'subjects, awake vs ketamine; envelope-instrument LZc and LZs, '
        'medians per subject; \u0394 = ketamine \u2212 awake; Wilcoxon '
        'signed-rank; bootstrap 95 percent CI).',
        ['Layer / metric', 'Awake', 'Ketamine', '\u0394 mean [95% CI]',
         'p', 'Up'],
        [
            ['Pre-pulse background LZc (400 ms)', '0.520', '0.555',
             '+0.032 [+0.022, +0.043]', '0.002', '10/10'],
            ['Post-pulse LZc, unadjusted (400 ms)', '0.522', '0.546',
             '+0.028 [+0.018, +0.039]', '0.002', '10/10'],
            ['Post-pulse LZc, background-corrected', 'n/a',
             'n/a', '\u22120.004 [\u22120.011, +0.002]', '0.375',
             '4/10'],
            ['Pre-pulse background LZs', '0.680', '0.701',
             '+0.019 [+0.012, +0.027]', '0.008', '9/10'],
            ['Post-pulse LZs, unadjusted', '0.682', '0.697',
             '+0.018 [+0.012, +0.025]', '0.002', '10/10'],
            ['Post-pulse LZs, background-corrected', 'n/a',
             'n/a', '\u22120.001 [\u22120.005, +0.002]', '0.678',
             '4/10'],
            ['Raw-waveform LZc, background-corrected', 'n/a',
             'n/a', '\u22120.0024 [\u22120.0033, \u22120.0014]',
             '0.004', '1/10'],
            ['TMS-evoked GFP peak (\u03bcV<super>2</super>)', '6.6', '5.8',
             '\u22120.8 [\u22125.4, +2.9]', '0.846', '5/10'],
        ],
        [0.34, 0.10, 0.11, 0.26, 0.09, 0.10], font_size=7.9,
        header_font=8.3, center_cols=(1, 2, 4, 5))

    L.body(story,
           'Read in order: the background diversity of the very same '
           'trials rises under ketamine (layer one, 10 of 10 subjects); '
           'the post-pulse window\u2019s diversity rises with it '
           '(layer two, 10 of 10); and once the background rise is '
           'subtracted \u2014 the contrast of contrasts, post-minus-'
           'pre within each subject \u2014 the evoked response itself '
           'shows no diversity increase (layer three: p = 0.375, 4 of '
           '10, CI spanning zero). The raw-waveform variant of layer '
           'three runs slightly negative (\u22120.0024, CI exclusive '
           'of zero, 1 of 10 up): under ketamine the evoked waveform '
           'is fractionally more stereotyped, not less. This is '
           'exactly the paper\u2019s headline dissociation \u2014 '
           'spontaneous complexity up, evoked complexity not \u2014 '
           'arrived at independently, and it explains why the '
           'uncorrected post-pulse comparison misleads: single-trial '
           'post-pulse LZ conflates the evoked deflection with the '
           'ongoing background, and the background is where the '
           'ketamine effect lives. The reconciliation with the '
           'original study is exact in kind: their evoked measure is '
           'PCI \u2014 source-estimated, bootstrap-thresholded '
           'significance binarization, the 8\u2013300 ms window, LZ76 '
           'normalized by the asymptotic maximum \u2014 which removes '
           'the background by construction; the sensor-level '
           'background-corrected contrast reproduces its verdict. The '
           'methodological contribution is the fourth protocol '
           'amendment: any evoked-complexity comparison must either '
           'compute PCI itself or correct for the pre-stimulus '
           'background; the uncorrected single-trial statistic is not '
           'an evoked measure at all.')

    figure(story, os.path.join(FIGDIR, 'farnes_evoked_contrast.png'),
           'Figure 3.1 \u2014 The completed evoked contrast. (A) '
           'per-subject post-pulse LZc, awake vs ketamine; (B) the '
           'same for per-channel LZs; (C) the grand-mean TMS-evoked '
           'GFP across the ten subjects, both conditions, time-locked '
           'to the pulse (dashed line). The post-pulse diversity '
           'increase rides the background increase; the corrected '
           'contrast is null.', max_h=235)

    L.h3(story, 'The spontaneous replication: the paper\u2019s main '
                'finding, with the corpus\u2019s own instrument')

    L.body(story,
           'The spontaneous recordings close the other half of the '
           'dissociation. With the same instrument at the corpus\u2019s '
           'native 8-second epoching (up to ten epochs, 80 s per '
           'recording, per channel and concatenated), the spontaneous '
           'LZc rises from wakefulness to ketamine in 9 of 10 '
           'subjects eyes-closed and 8 of 10 eyes-open; the per-'
           'channel LZs rises in 10 of 10 eyes-closed. The paper\u2019s '
           'secondary finding replicates with it: eyes-open diversity '
           'exceeds eyes-closed in 10 of 10 awake subjects and 8 of '
           '10 under ketamine. As a sanity marker, the \u03b1-peak '
           'of the mean PSD collapses toward the 7 Hz search floor '
           'under ketamine in most subjects \u2014 the known '
           'ketamine desynchronization, visible in the same data that '
           'carry the complexity increase. Two instrument deviations '
           'are recorded and stand: the ported code computes the LZW '
           'dictionary count where the paper applies LZ76 \u2014 both '
           'Lempel-Ziv family estimators, shuffle-normalized; the '
           'effects replicate in direction and significance \u2014 '
           'and the port uses five shuffles where their normalization '
           'used one, for stability, a deviation inherited from the '
           'Phase-2 instrument and kept for continuity.')

    L.data_table(
        story,
        'Table 3.3 \u2014 The spontaneous-LZ replication (n = 10; same '
        'statistics as Table 3.2).',
        ['Contrast', 'Awake', 'Ketamine', '\u0394 mean [95% CI]', 'p',
         'Up'],
        [
            ['LZc, eyes closed', '0.460', '0.504',
             '+0.045 [+0.029, +0.062]', '0.004', '9/10'],
            ['LZs, eyes closed', '0.534', '0.574',
             '+0.043 [+0.028, +0.057]', '0.002', '10/10'],
            ['LZc, eyes open', '0.532', '0.569',
             '+0.030 [+0.012, +0.049]', '0.027', '8/10'],
            ['LZs, eyes open', '0.596', '0.631',
             '+0.032 [+0.016, +0.049]', '0.010', '9/10'],
            ['Eyes-open vs closed, awake', 'n/a', 'n/a',
             '+0.061 (open over closed)', '0.002', '10/10'],
            ['Eyes-open vs closed, ketamine', 'n/a', 'n/a',
             '+0.046 (open over closed)', '0.014', '8/10'],
        ],
        [0.30, 0.10, 0.12, 0.28, 0.09, 0.11], font_size=7.9,
        header_font=8.3, center_cols=(1, 2, 4, 5))

    figure(story, os.path.join(FIGDIR, 'farnes_spont_contrast.png'),
           'Figure 3.2 \u2014 The spontaneous replication. (A) '
           'per-subject spontaneous LZc, awake vs ketamine, eyes '
           'closed; (B) eyes open; (C) the within-subject deltas, '
           'eyes closed. The paper\u2019s main positive finding '
           'replicates with the corpus\u2019s ported instrument.',
           max_h=235)

    # ---- 3.5 status tags ----
    L.h2(story, '3.5 Status Tags After Execution')

    L.data_table(
        story,
        'Table 3.4 \u2014 The map rows and structures, re-graded after '
        'the three compute rounds (seventh-edition conventions).',
        ['Map row / structure', 'Status after Phases 1\u20132 and the '
         'Farnes completion'],
        [
            ['J (effective coupling) vs J<sub>c</sub>',
             'EXECUTED \u2014 operating point in-band for 7/7 '
             'connectomes, weak edge-concentrated form; sensor-space, '
             'one MEG subject, normalization-convention-dependent '
             '\u2014 Partial'],
            ['\u03b2 (noise-to-coupling)',
             'TESTED \u2014 within-subject ordering across sedation '
             'levels: 6/6 quality-passing (6/8 raw) + 3/4 surgical; '
             'values 0.12 primary convention, \u2248 0.02 Myrov '
             'convention, \u03c3-conventioned'],
            ['Coherence-threshold structure',
             'Supported at exit granularity (LZs falls 4/4 when the '
             'fit exits the critical band; 2/4 when in-band); pooled '
             'version confounded \u2014 documented'],
            ['Structure-function coupling',
             'Absent at the operating point under the primary '
             'convention (honest negative); full-plane replication '
             'under the Myrov convention; op-point coupling there is '
             'not topology-specific (generic weight effect)'],
            ['Bojak\u2013Liley \u03b1-trajectory (theory leg)',
             'Partial / failed-to-replicate from the printed '
             'parameters; the \u03bb\u2192hyperpolarization direction '
             'survives; diagnostic trail archived'],
            ['BOLD LZ (ds003171)',
             'Weak corroboration at light sedation (5/6); deep level '
             'unresolved at this power and estimator'],
            ['Psychedelic-arm LZ observable (Farnes)',
             'REPLICATED \u2014 spontaneous LZc/LZs up under '
             'sub-anaesthetic ketamine (9\u201310/10 eyes-closed), '
             'eyes-open>closed in both conditions; evoked dissociation '
             'reproduced at the background-corrected level'],
            ['\u201cExtended critical neighborhood\u201d presupposition',
             'Supported, weak edge-concentrated form, 7/7 connectomes '
             '\u2014 Partial'],
        ],
        [0.34, 0.66], font_size=7.9, header_font=8.3)

    # ---- 3.6 limits ----
    L.h2(story, '3.6 What the Executed Phases Do Not Establish')

    L.body(story,
           'The executions\u2019 limits are part of their record. '
           'Phase 1: one MEG subject (two consistent runs); no '
           'source-space, topology-matched parcel comparison, because '
           'no openly downloadable MEG-plus-dMRI pairing exists at '
           'that level; supplementary parameters assumed; the DFA '
           'median shortfall at the fitted point unexplained by the '
           'run; no finite-size scaling; no per-frequency-band '
           'operating points. Phase 2: no within-subject depth '
           'gradient (no multi-depth titration corpus was runnable); '
           '\u03b2\u0302 absolute values convention-bound, only the '
           'ordering validated; the deep-GA slowing phase present but '
           'directional only; the theory leg without its \u03b1-'
           'trajectory. The Farnes completion: the evoked measure is '
           'sensor-level single-trial LZ, not PCI \u2014 no source '
           'model, no significance binarization, no LZ76-asymptotic '
           'normalization \u2014 and the dissociation is reproduced '
           'via background correction, not by computing the '
           'original statistic; the spontaneous replication runs on '
           '80 seconds per recording and does not compute ACE or SCE; '
           'no subjective-experience correlate (the paper\u2019s '
           'questionnaire link) is testable from the release; and '
           'one .set header (the ketamine eyes-open recording of '
           'subject 210) carries a char-element corruption that '
           'defeats strict parsers \u2014 tolerated via a documented '
           'sidecar (channel count, rate, and epoch length from the '
           'same subject\u2019s other recordings; trial count from '
           'the sha256-verified .fdt size), a workaround recorded '
           'rather than hidden.')

    # ---- 3.7 reproducibility ----
    L.h2(story, '3.7 Reproducibility')

    L.body(story,
           'Everything in this chapter re-runs from the archived '
           'record. Scripts: phase1_meg.py, phase1_kuramoto.py, '
           'phase1_fit.py, phase1_convention_test.py, phase1_smoke.py '
           '(Phase 1); phase2_ds4541_plan.py, phase2_ds4541_epochs.py, '
           'phase2_ds5620_epochs.py, phase2_ds3171_bold.py, '
           'phase2_grid_myrov.py, phase2_grid_analysis.py, '
           'phase2_ksigma.py, phase2_beta_fits.py, phase2_liley_sweep.py, '
           'phase2_farnes_evoked.py, phase2_figures.py (Phase 2); '
           'rd2_download.py, rd2_lib.py, rd2_evoked_contrast.py, '
           'rd2_spontaneous_contrast.py, rd2_aggregate.py (this '
           'round). Inputs: the OpenNeuro corpora (range-request '
           'fetches), the OSF MEG archive, the neurolib connectomes, '
           'the Raw_data_2 release (101 sha256-verified assets), the '
           'PLOS S1 equations file. Outputs: the two phase reports '
           'with their JSON and npz result sets, 14 figures, and this '
           'round\u2019s farnes/ directory (20 evoked and 40 '
           'spontaneous per-file JSONs, the aggregate contrast '
           'summary, the two figures embedded above). Seeds: grid '
           '500, \u03c3-sweep 600, nulls 700 and 11, K\u00d7\u03c3 '
           '800, \u03c9-sampling 7, Farnes LZ 7/42 (round 20) and the '
           'round-21 per-file seeds (subject and condition coded, 21 '
           'offset); the fast LZW port is verified identical to the '
           'established lzw_count on 250 random cases before every '
           'run. Compute: roughly five CPU-hours across the three '
           'rounds, under 200 MB per process.')
