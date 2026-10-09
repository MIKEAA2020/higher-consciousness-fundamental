#!/usr/bin/env python3
"""Eighth Edition (Computed Edition), Part 2: chapter 3, sections 3.1-3.3
2014 the execution inventory, Phase 1, and Phase 2, folded from the two
phase execution reports."""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 3. PHASES 1 AND 2, EXECUTED ====================
    L.h1(story, '3. Phases 1 and 2, Executed: The Computations')

    L.body(story,
           'This chapter folds the two executed phases into the '
           'consolidation. The source documents are the phase execution '
           'reports \u2014 full methods, results, status tags, '
           'deviations, and reproducibility records, archived with every '
           'script, input, output, and seed \u2014 and this chapter is '
           'their consolidation: complete enough to stand alone, with '
           'the reports as the record of first resort. The chapter '
           'follows the protocol\u2019s own order: what was run (3.1), '
           'Phase 1 (3.2), Phase 2 (3.3), then the Farnes evoked-EEG '
           'contrast completed this round (3.4), the post-execution '
           'status tags (3.5), the honest limits (3.6), and the '
           'reproducibility inventory (3.7).')

    # ---- 3.1 inventory ----
    L.h2(story, '3.1 What Was Executed, and on What')

    L.body(story,
           'Three compute rounds, all on open or user-supplied data, all '
           'within the execution environment\u2019s documented '
           'constraints (single-node CPU, 3\u20134 GB RAM, synchronous '
           'process chunks). Round 19 executed Phase 1: the Myrov '
           'hierarchical Kuramoto pipeline on an individual structural '
           'connectome, swept over the local-coupling / global-coupling '
           'plane, matched to open MEG. Round 20 executed Phase 2: the '
           '\u03b2 sedation ordering on the open anesthesia corpora, '
           'the Bojak\u2013Liley / Steyn-Ross mean-field leg, and the '
           'full Myrov-convention grid as the approved second compute '
           'round. Round 21 \u2014 this round \u2014 completes the '
           'Farnes evoked contrast on the newly supplied corpus and '
           'folds everything into this edition. The data inventory:')

    L.data_table(
        story,
        'Table 3.1 \u2014 The execution corpus: every input, its source, '
        'and its use across the three compute rounds.',
        ['Component', 'Source', 'Use', 'Status'],
        [
            ['MEG, eyes-closed rest (subj002, 2 \u00d7 600 s, 272 CTF '
             'magnetometers)',
             'Brainstorm bst_resting (OSF, open)',
             'Phase 1 target observables: \u03b1-peak, DFA, wPLI, '
             'envelope correlations',
             'EXECUTED'],
            ['Structural connectomes, 7 individual HCP subjects (DTI, '
             'AAL2, 94 regions)',
             'neurolib hcp dataset (GitHub, open)',
             'Phase 1 model substrate; per-connectome consistency check',
             'EXECUTED'],
            ['EEG, propofol sedation, 8 subjects, awake-EC vs '
             'task-sed rest',
             'OpenNeuro ds005620 (CC-BY-4.0)',
             'Phase 2 primary \u03b2-ordering corpus',
             'EXECUTED'],
            ['EEG-fNIRS under surgical GA, 9 sessions, 4 levels',
             'OpenNeuro ds004541',
             'Phase 2 surgical corpus (directional vote)',
             'EXECUTED'],
            ['fMRI BOLD rest, 4 sedation levels, 6 subjects',
             'OpenNeuro ds003171',
             'Phase 2 BOLD complexity leg',
             'EXECUTED'],
            ['fMRI graded propofol with within-run ramps',
             'OpenNeuro ds006623',
             'Excluded with reason (ramp design; registered for Phase 4)',
             'NOT RUN (documented)'],
            ['TMS-evoked EEG, 10 subjects \u00d7 2 conditions (60 ch, '
             '312.5 Hz, 270\u2013298 trials/file)',
             'Farnes et al. 2020 corpus via the Raw_data_2 release '
             '(user-supplied, sha256-verified)',
             'The evoked-LZ contrast (3.4)',
             'EXECUTED (this round)'],
            ['Spontaneous EEG, 10 subjects \u00d7 4 recordings (62 ch, '
             '250 Hz, 8-s epochs, post-ICA)',
             'Same release, same verification',
             'The spontaneous-LZ replication (3.4)',
             'EXECUTED (this round)'],
            ['Steyn-Ross / Liang mean-field equations',
             'PLOS S1 File (fetched and archived)',
             'Phase 2 theory leg (\u03bb-sweep)',
             'EXECUTED (partial)'],
        ],
        [0.30, 0.24, 0.30, 0.16], font_size=7.9, header_font=8.3)

    # ---- 3.2 Phase 1 ----
    L.h2(story, '3.2 Phase 1 \u2014 Coupling and Criticality Estimation '
                '(the J Row)')

    L.body(story,
           'The pipeline implements the Myrov et al. hierarchical '
           'Kuramoto model verbatim \u2014 natural frequencies sampled '
           'from the MEG PSD peak structure, internal block coupling K, '
           'external connectome coupling L, white noise \u03c3 \u2014 '
           'on the primary HCP connectome, with the documented '
           'assumptions the source\u2019s unpublished supplementary '
           'forces (50 oscillators per node, 1 ms step, 150 s per '
           'combination). The DFA-defined critical regime \u2014 more '
           'than 10 percent of nodes exceeding DFA 0.65 \u2014 '
           'reproduces the source\u2019s qualitative geometry: a '
           'K-dominated band, K \u2208 [15, 35] rad/s at the fitted '
           'L, extended across the whole L axis. The MEG-matched '
           'operating point lands at K<super>+</super> = 25 rad/s, L<super>+</super> = 40 '
           'rad/s \u2014 inside the band, with model \u03b1-peak 8.20 '
           'Hz against the MEG 8.12 Hz and a PSD-shape correlation of '
           '0.65. The noise fit gives \u03c3<super>+</super> = 3 and therefore '
           'the derived estimate \u03b2\u0302 = \u03c3<super>+</super>/K<super>+</super> = '
           '0.12 \u2014 the spec\u2019s noise-to-coupling ratio with a '
           'computed value attached for the first time.')

    L.body(story,
           'Two findings discipline the number. First, the honest '
           'negative: at the operating point, the structure-function '
           'correlations that define the method\u2019s Figure 3 are '
           'essentially zero, and shuffled-label and random connectomes '
           'are indistinguishable from the real one \u2014 the null '
           'discipline \u201cmust destroy the correspondence\u201d has '
           'nothing to destroy under this convention. The cause is the '
           'W-normalization choice, and the replication arm in the '
           'inferred Myrov convention (raw weights, numeric-Hz '
           'frequencies as angular rates) restores the full '
           'phenomenology: order\u2013strength correlations of +0.18 to '
           '+0.36, non-monotonic in K as in the source, with the '
           'DFA-matched operating point extrapolating to K \u2248 '
           '9\u20139.5 and \u03b2\u0302 \u2248 0.02\u20130.03 in that '
           'scaling. The J-row estimator is normalization-convention-'
           'dependent \u2014 recorded as the first protocol amendment. '
           'Second, the per-connectome check: all seven connectomes '
           'concentrate their fitted operating points in the K = '
           '25\u201340 range, at or just beyond the supercritical edge '
           'of their respective bands \u2014 the failure condition '
           '(\u201coperating points scatter across the plane\u201d) is '
           'not triggered, and the specification\u2019s central '
           'empirical presupposition survives in the weak, '
           'edge-concentrated form for 7 of 7 connectomes, not the '
           'strong centered form. The residual DFA shortfall (model '
           '0.562 against MEG 0.632 at the fitted point) is recorded, '
           'not smoothed over.')

    # ---- 3.3 Phase 2 ----
    L.h2(story, '3.3 Phase 2 \u2014 The Anesthesia Arm (the \u03b2 Row)')

    L.body(story,
           'The \u03b2\u0302 estimator runs on a 64-combination '
           '(K, \u03c3) model surface at the fitted L, with a per-level '
           'composite misfit over the DFA median and the \u03b1-peak. '
           'The preregistered validation condition \u2014 \u03b2 '
           'estimates must order correctly across sedation levels '
           'within subject \u2014 passes in its clean form: 6 of 6 '
           'quality-passing ds005620 subjects show \u03b2\u0302(sed) '
           '> \u03b2\u0302(awake) (sign-test p = 0.031), and 3 of 4 '
           'surgical sessions with both levels; the two raw exceptions '
           'carry independent data-quality flags raised from epoch '
           'statistics, not from the ordering result. The mechanism is '
           'legible in every quality-passing subject: light propofol '
           'accelerates the \u03b1-peak from 8\u20139 Hz into the '
           '11\u201313 Hz beta-buzz band (the biphasic activation), '
           'the combined misfit pulls K<super>+</super> from 10\u201340 down to '
           '5\u201310 rad/s \u2014 the operating point moves to the '
           'subcritical side of the critical band \u2014 and '
           '\u03b2\u0302 = \u03c3<super>+</super>/K<super>+</super> rises accordingly. The '
           '\u03b2 row is upgraded from Derived-unvalidated to TESTED: '
           'the ordering is the validated content; the absolute value '
           'is convention-bound (the same MEG reference fits K<super>+</super> = '
           '10 under the two-term criterion where the three-term '
           'criterion gave 25 \u2014 the fit criterion is the second '
           'protocol amendment).')

    L.body(story,
           'The LZ-tracking failure condition \u2014 the preregistered '
           'tolerance-band test that would falsify the \u03b2 row and '
           'the coherence-threshold structure together \u2014 is '
           'supported at the preregistered within-subject granularity: '
           'when the sedated fit exits the Phase-1 critical K-band, LZs '
           'falls in 4 of 4 subjects; when it stays in-band, LZs falls '
           'in 2 of 4 (chance level). The pooled-granularity version is '
           'confounded by corpus-level LZ offsets and is reported only '
           'to document why granularity matters. Around the ordering '
           'result stand three supporting legs, each with its own '
           'honest grade: the full 105-combination Myrov-convention '
           'grid replicates the plane geometry and the Fig-3 '
           'phenomenology across the full plane, with the op-point '
           'nulls showing the structure-function coupling there is a '
           'generic weight-distribution effect, not topology-specific '
           '(the third protocol amendment: nulls must be evaluated at '
           'the operating point and in the low-K region where the '
           'coupling exists); the BOLD leg gives weak corroboration at '
           'light sedation (5 of 6 subjects, complexity decrease) with '
           'the deep level unresolved at that power and estimator; and '
           'the mean-field leg survives the pharmacology \u2014 the '
           'propofol surrogate \u03bb hyperpolarizes the equilibrium '
           'monotonically in the correct GABAergic direction \u2014 '
           'but fails to produce any \u03b1-band resonance from the '
           'printed parameters under any self-consistent units '
           'reading: the theory-side \u03b1-trajectory remains at the '
           'measured level, the diagnostic trail archived.')
