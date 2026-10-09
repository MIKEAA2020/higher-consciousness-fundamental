#!/usr/bin/env python3
"""Eighth Edition (Computed Edition), Part 4: chapters 4-5 \u2014 the
parameter map re-graded after execution, and the amended protocol with its
remaining phases."""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 4. THE PARAMETER MAP AFTER EXECUTION ====================
    L.h1(story, '4. The Parameter Map After Execution')

    L.body(story,
           'The seventh edition\u2019s verdict \u2014 no unified map '
           'exists; the per-arm ingredients are individually published '
           '\u2014 was a statement about the literature. Execution '
           'changes what can be said about the map itself, row by row. '
           'A published estimator and a computed value are different '
           'kinds of object: the first is a promise that a quantity is '
           'measurable, the second is a measurement with an error '
           'trail. After the three compute rounds, the map\u2019s J '
           'row and \u03b2 row hold computed values (in stated '
           'conventions, with fitted operating points and recorded '
           'honest negatives); the anesthesia arm\u2019s validation '
           'condition has actually been run and passed in its clean '
           'form; and the psychedelic arm\u2019s complexity '
           'observable \u2014 the quantity the J-crossing test of '
           'Phase 3 was designed to detect moving \u2014 has now '
           'been demonstrated to move under a psychedelic, with this '
           'corpus\u2019s own instrument, on user-supplied data. The '
           'fragments have begun to assemble; the assembly is no '
           'longer purely prospective.')

    L.data_table(
        story,
        'Table 4.1 \u2014 The parameter map\u2019s rows: status at the '
        'seventh edition versus status after the executions.',
        ['Map row', 'Seventh-edition status', 'Status after execution'],
        [
            ['J (effective coupling) vs J<sub>c</sub>',
             'Published estimators (Myrov ridge; \u00d3dor criticality; '
             'VEP Bayesian inversion)',
             'EXECUTED, Partial \u2014 operating point computed, '
             'in-band 7/7 connectomes (weak form); convention-'
             'amendment logged; structure-function honest negative '
             'recorded'],
            ['\u03b2 (noise-to-coupling)',
             'Derived, validation condition named (sedation ordering)',
             'TESTED \u2014 ordering condition passed (6/6 '
             'quality-passing); \u03b2\u0302 values attached '
             '(0.12 primary; \u2248 0.02 Myrov scaling)'],
            ['g, a (gain / attractor depth)',
             'Derived-unvalidated (receptor\u2192gain, Deco-'
             'parameterization route)',
             'Unchanged \u2014 Phase 3 not yet run; but its LZ '
             'observable is now empirically anchored (Farnes '
             'replication, Table 3.3)'],
            ['\u03b8, \u03c6 (phase parameters)',
             'Gap \u2014 no published neural assignment',
             'Unchanged \u2014 the gap stands; no execution touched '
             'these rows'],
            ['\u03ba, K (permittivity / coupling constants)',
             'Gap at patient level (VEP spec read; inference route '
             'published)',
             'Unchanged \u2014 Phase 4 territory'],
            ['Psychedelic-arm observable (LZc under 5-HT2A agonism)',
             'Finding-anchored (published: LZc up under psychedelics)',
             'REPLICATED with the corpus\u2019s instrument \u2014 '
             'spontaneous LZc up under ketamine, 9\u201310/10; the '
             'evoked dissociation reproduced at the corrected level'],
        ],
        [0.20, 0.36, 0.44], font_size=7.9, header_font=8.3)

    L.body(story,
           'Two asymmetries in the table deserve statement. First, '
           'execution widened, rather than closed, the honest '
           'uncertainty on two rows: the J row acquired a convention-'
           'dependence that the seventh edition\u2019s literature '
           'reading could not see, and the \u03b2 row acquired the '
           'criterion-sensitivity of its fit \u2014 the MEG reference '
           'moves from K<super>+</super> = 25 to K<super>+</super> = 10 between two '
           'defensible composite criteria. These are not failures of '
           'the map; they are the map\u2019s first real error bars, '
           'and the protocol absorbs them as preregistration '
           'decisions (amendments one and two). Second, the Farnes '
           'replication gives the psychedelic arm something the '
           'seventh edition could only cite: a complex-instrument '
           'demonstration, run end to end inside this corpus\u2019s '
           'own instrument family, that the arm\u2019s observable '
           'moves in the published direction under the published '
           'manipulation. When Phase 3 eventually computes the '
           'J-crossing test on a receptor-parameterized model, the '
           'empirical anchor it will be tested against is no longer '
           'someone else\u2019s number \u2014 it is Table 3.3.')

    # ==================== 5. THE AMENDED PROTOCOL ====================
    L.h1(story, '5. The Amended Protocol: Four Amendments and the '
                'Remaining Phases')

    L.body(story,
           'The seventh edition specified the protocol as a concrete, '
           'preregistrable design. Execution has now amended it four '
           'times, each amendment earned by a computation rather than '
           'proposed in the abstract. They are collected here because '
           'they bind every future phase:')

    L.bullet(story,
             'Amendment 1 (Round 19, normalization): the connectome '
             'normalization \u2014 raw / max-normalized versus '
             'row-normalized W \u2014 is a first-class preregistration '
             'decision; under row normalization the structure-function '
             'nulls have no content to destroy, under the Myrov '
             'convention they do.')
    L.bullet(story,
             'Amendment 2 (Round 20, fit criterion): the fit '
             'criterion must be preregistered exactly as the '
             'estimator; the composite\u2019s term composition moves '
             'the reference operating point between in-band and '
             'out-of-band.')
    L.bullet(story,
             'Amendment 3 (Round 20, null granularity): the '
             'structure-function null discipline must be evaluated at '
             'the preregistered operating point and in the low-'
             'coupling region where the coupling exists; the two '
             'locations answer different questions.')
    L.bullet(story,
             'Amendment 4 (Round 21, evoked-complexity statistics): '
             'any evoked-complexity comparison must either compute '
             'PCI itself \u2014 source estimation, significance '
             'binarization, the LZ76-asymptotic normalization \u2014 '
             'or explicitly correct for the pre-stimulus background; '
             'the uncorrected single-trial post-stimulus statistic '
             'conflates the evoked response with the background and '
             'is not an evoked measure.')

    L.body(story,
           'The remaining phases stand as specified, now with their '
           'first empirical anchors named. Phase 3 (the psychedelic '
           'arm) runs the Deco-style receptor parameterization with '
           'the J-crossing test on the open psychedelic corpora; its '
           'complexity observable is anchored by this round\u2019s '
           'replication, and the Farnes corpus itself \u2014 now '
           'fully in hand, both conditions \u2014 supplies a within-'
           'subject ketamine contrast at the observable level should '
           'the arm want one at EEG resolution. Phase 4 (patient-'
           'level inversion) proceeds toward the Bayesian '
           'patient-level estimation of the GL parameters, with the '
           'ds006623 ramp design registered for its depth-gradient '
           'leg. Phase 5 (the joint demonstration with its four null '
           'models and finite-size scaling) and Phase 6 (adversarial '
           'collaboration and reporting under the preregistration '
           'governance) are unchanged. The protocol\u2019s failure '
           'conditions are unchanged \u2014 and two of them have now '
           'actually been faced: the scatter condition (not '
           'triggered, 7/7 concentration) and the ordering condition '
           '(passed in its clean form). A protocol whose failure '
           'conditions have been exercised, even in part, is a '
           'different epistemic object from one whose failures are '
           'all still hypothetical.')
