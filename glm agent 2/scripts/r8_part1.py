#!/usr/bin/env python3
"""Eighth Edition (Computed Edition), Part 1: chapters 1-2.

The lineage's turn: the Seventh Edition specified the Level-2 protocol;
this edition reports its first two phases EXECUTED on open data, and the
Farnes et al. 2020 corpus resolved end to end through the user's Raw_data_2
release. Neutral academic voice; citations: L#### (GLM dialogue), E#/D# T##
(DeepSeek exchanges), P# (papers read from supplied PDFs), S# (the
decombination spec), F# (the Farnes 2020 paper and corpus).
"""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 1. EXECUTIVE SUMMARY ====================
    L.h1(story, '1. Executive Summary')

    L.body(story,
           'The seventh edition ended with a protocol: seven phases, '
           'named methods, open data, null models, preregistered failure '
           'conditions. The eighth edition begins its execution. Phases 1 '
           'and 2 \u2014 coupling-and-criticality estimation and the '
           'anesthesia arm \u2014 have now run as actual computations on '
           'open data across three successive compute rounds: the '
           'hierarchical Kuramoto pipeline on an individual structural '
           'connectome matched to open MEG (Round 19); the \u03b2 '
           'sedation ordering on four open anesthesia corpora plus the '
           'full convention grid (Round 20); and, in this round, the '
           'completion of the Farnes et al. 2020 evoked-EEG contrast '
           'through the interlocutor\u2019s Raw_data_2 release (Round 21). '
           'What was a schedule is now, for the first time in the '
           'corpus\u2019s history, a set of numbers with error bars, '
           'status tags, and recorded failures.')

    L.body(story,
           'The executed content, stated plainly. Phase 1 places the '
           'brain\u2019s fitted operating point inside the extended '
           'critical neighborhood for 7 of 7 connectomes \u2014 in the '
           'weak, edge-concentrated form, not the strong centered form '
           '\u2014 and computes \u03b2\u0302 = 0.12 in the primary '
           'convention (\u2248 0.02 in the Myrov convention), while '
           'recording an honest negative: at the operating point, the '
           'structure-function correlations the method is famous for are '
           'indistinguishable from shuffled connectomes. Phase 2 '
           'validates the \u03b2 row\u2019s ordering condition: within-'
           'subject \u03b2\u0302 rises from wakefulness to sedation in '
           '6 of 6 quality-passing subjects (6 of 8 raw, both exceptions '
           'independently artifact-flagged), the mechanism being the '
           'biphasic \u03b1-acceleration that pulls the fitted operating '
           'point to the subcritical side of the critical band. The '
           'preregistered LZ-tracking condition is supported at exit '
           'granularity: when the sedated fit exits the critical band, '
           'LZs falls in 4 of 4 subjects.')

    L.body(story,
           'This round\u2019s primary computation completes the evoked '
           'contrast that the seventh edition left unfilled. The '
           'Raw_data_2 release supplies the full Farnes corpus \u2014 '
           'ten subjects, TMS-evoked responses in both the awake (31) '
           'and ketamine (32) conditions, plus the complete spontaneous '
           'eyes-open and eyes-closed recordings \u2014 all '
           'sha256-verified against the release manifest. The completion '
           'required repairing an error first: the round-twenty analysis '
           'of the single supplied evoked file had reshaped the MATLAB '
           'column-major stream with row-major semantics, scrambling '
           'channels and samples; the repair (R32) reproduces the old '
           'numbers exactly from the wrong mapping, and the corrected '
           'mapping shows the textbook TMS-evoked structure the old '
           'numbers could not. The completed contrast then delivers a '
           'three-layer result: post-pulse single-trial LZ diversity '
           'increases under ketamine in 10 of 10 subjects (p = 0.002) '
           '\u2014 but the pre-pulse background increases equally '
           '(p = 0.002), and the background-corrected contrast is null '
           '(p = 0.375). The paper\u2019s headline dissociation \u2014 '
           'spontaneous complexity up, evoked complexity not \u2014 '
           'replicates with this corpus\u2019s own instrument once the '
           'background is accounted for. The spontaneous increase '
           'itself replicates directly: LZc rises in 9 of 10 subjects '
           'eyes-closed (p = 0.004), 8 of 10 eyes-open, and the '
           'eyes-open-over-closed ordering holds in both conditions.')

    L.body(story,
           'What the executions do not establish is recorded with the '
           'same care: one MEG subject, sensor-space matching, a '
           '\u03b2\u0302 whose absolute value is convention-bound (only '
           'the ordering is validated content), a mean-field leg that '
           'reproduces the pharmacology but not the \u03b1-trajectory, '
           'and an evoked measure that is sensor-level single-trial LZ '
           '\u2014 not PCI, not source-level, not the paper\u2019s '
           'exact statistic. The protocol\u2019s conventional-level '
           'ceiling and the equivalence doctrine are unchanged: even '
           'total success of all seven phases would license only '
           '\u201cthe differentiation program\u2019s predictions are '
           'tested and surviving,\u201d never \u201cthe Absolute is '
           'thereby evidenced.\u201d')

    # ==================== 2. CORPUS STATE ====================
    L.h1(story, '2. Corpus State Carried Forward')

    L.body(story,
           'The standing consolidation remains the sixth edition\u2019s '
           'sixteen chapters and the seventh edition\u2019s parameter-map '
           'turn: the eleven-party dialogue corpus, the non-dual '
           'culmination, the self-audit with its repairs R1\u2013R27, '
           'the adjudication record, the anchored empirical annex, the '
           'audited premise, the five newly-read sources (P1\u2013P5), '
           'the fragments-and-assembly verdict on the neural parameter '
           'map, and the seven-phase Level-2 protocol with its '
           'preregistration and adversarial-collaboration governance. '
           'This edition adds one thing to that state \u2014 execution '
           'records \u2014 and touches nothing else. The metaphysical '
           'tiers, the formalization boundary, the superdeterminism '
           'tension\u2019s grade, and the doctrine that governs '
           'interpretation of all empirical content are carried forward '
           'unchanged and are restated where the chapter context '
           'requires them.')

    L.body(story,
           'The corpus\u2019s source inventory has, however, moved \u2014 '
           'and the movement is the reason this edition exists. After '
           'the thirteenth supplied files were read in Round 19 and the '
           'Butler 5-HT2A article in Round 20, the appendix of '
           'unfetchable sources had narrowed to three items: the '
           'possible separate Butler article (resolved), the ETH '
           'provenance item (non-blocking), and the Farnes et al. 2020 '
           'Dryad raw EEG \u2014 the one data asset the protocol\u2019s '
           'Phase 3 observable demonstrably moves under. The '
           'interlocutor has now supplied it. The Raw_data_2 release '
           '(tagged at the repository, 101 assets, every file '
           'sha256-verified against the GitHub release manifest) '
           'contains the complete preprocessed Farnes corpus: for each '
           'of ten subjects, the TMS-evoked matrices in both conditions '
           '(60 channels, 251 samples, 270\u2013298 trials per file at '
           '312.5 Hz, TMS pulse at the 126th sample per the release '
           'readme), and the four spontaneous recordings (eyes open and '
           'closed, first two awake and last two under sub-anaesthetic '
           'ketamine, 62 channels at 250 Hz in EEGLAB .set/.fdt form, '
           '8-second epochs, post-ICA). The appendix\u2019s data row is '
           'therefore closed: every protocol-critical source and now '
           'every protocol-critical dataset is either read, verified, '
           'or both.')

    L.body(story,
           'One repair to the record accompanies the supply, logged as '
           'R32 and R33 in chapter 7 and stated here for the standing '
           'state: the round-twenty evoked reference point was computed '
           'on a channel-scrambled mis-mapping of the supplied file, '
           'and its recovery denominator carried an arithmetic slip '
           '(4,412,580 doubles were declared, not 4,414,380 \u2014 the '
           'Raw_data_2 copy of the same file is complete, all 293 '
           'trials, and the manual MAT5 recovery of the truncated '
           'eeg_data copy is thereby validated: 285 recovered trials '
           'against the now-known ground truth). The corpus\u2019s '
           'self-audit discipline \u2014 every edition logs its own '
           'corrections \u2014 continues uninterrupted.')
