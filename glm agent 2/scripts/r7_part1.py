#!/usr/bin/env python3
"""Seventh Edition (Parameter-Map Edition), Part 1: chapters 1-2.

Posture mandate from the interlocutor: steelman, strengthen, elevate, anchor,
audit \u2014 and now ASSEMBLE. The lineage turns from auditing claims to
assembling the missing artifact: the neural parameter map whose absence kept
the four empirical domains conjectural. Neutral academic voice; citations:
L#### (GLM dialogue), E1/E2/E3 T## (DeepSeek), D4 T## (ds4 final arc),
P# (the five papers newly read this round), S# (the spec in decombination.txt).
"""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 1. EXECUTIVE SUMMARY ====================
    L.h1(story, '1. Executive Summary')

    L.body(story,
           'This seventh edition exists because the interlocutor refused a '
           'negative. Where the standing verdict of the corpus said, in '
           'effect, that the neural parameter map \u201cdoes not exist,\u201d '
           'the challenge came back: can you not find it through web search? '
           'Provide any links you cannot fetch. The challenge was right to '
           'refuse the negative. A systematic search (eleven queries, '
           'forty-eight unique URLs probed, twelve papers resolved through '
           'CrossRef and Europe PMC after the OpenAlex API rate-limited) '
           'found that the literal artifact \u2014 a published, unified '
           'correspondence from the specification\u2019s six parameters '
           '(J, g, a, \u03b2, \u03b8, \u03c6) to measurable neural '
           'quantities \u2014 does not exist anywhere in the literature. '
           'But it also found that the function the artifact would perform '
           'exists piecemeal, per domain, in five mature research programs, '
           'each with published methods, open code, and verifiable links. '
           'The verdict therefore corrects from \u201cdoes not exist\u201d '
           'to \u201cno unified map exists; the per-arm ingredients are '
           'individually published.\u201d')

    L.body(story,
           'The correction then became substance. The interlocutor supplied '
           'five papers \u2014 four of them precisely the load-bearing '
           'sources the search could not fetch (the Elsevier full text of '
           'the Virtual Epileptic Patient, the bioRxiv full text of the '
           'hierarchical Kuramoto study, the Cell Press full text of the '
           'serotonin-receptor whole-brain model, and the eLife full text of '
           'the ketanserin blockade study) plus a fifth new to the corpus '
           '(the metabolic connectivity mapping study of PNAS) \u2014 and '
           'all five have now been read line by line from source. They are '
           'not background reading. Together they supply exactly what '
           'requirement 4 of the decombination specification demanded: '
           'patient-level parameter inference at intracranial resolution '
           '(the Virtual Epileptic Patient\u2019s excitability map, fitted '
           'Bayesianly against stereo-EEG), a per-subject '
           'distance-to-criticality estimator on the real connectome (the '
           'hierarchical Kuramoto model\u2019s critical ridge, matched '
           'against magnetoencephalography), a receptor-density-to-parameter '
           'correspondence for the psychedelic arm (the 5-HT2A gain-scaling '
           'model, with shuffled-map and wrong-receptor controls), an '
           'intervention-validated receptor attribution (the full '
           'pharmacological blockade of LSD\u2019s neural and subjective '
           'effects by ketanserin), and an energy-based route to directional '
           'coupling (metabolic connectivity mapping from simultaneous '
           'FDG-PET and functional MRI).')

    L.body(story,
           'The second half of this edition converts the assembled '
           'fragments into the deliverable their existence makes possible: '
           'a concrete Level-2 research protocol \u2014 the specification '
           'that elevation-cost analysis called \u201cthe highest realistic '
           'target\u201d and offered to sketch, now sketched in full. The '
           'protocol is organized in seven phases, each grounded in a named '
           'method from the newly-read sources: coupling and '
           'criticality estimation on individual connectomes '
           '(\u00d3dor-style Kuramoto sweeps with the Myrov hierarchical '
           'extension); anesthesia-arm sweeps in the Bojak\u2013Liley '
           'neural-field tradition against four open propofol and '
           'multi-agent EEG corpora; psychedelic-arm receptor '
           'parameterization in the Deco style against six open psychedelic '
           'corpora; patient-level Bayesian inversion of the '
           'Ginzburg\u2013Landau parameters in the Jirsa manner; the joint '
           'S1\u2013S4 demonstration with null models and finite-size '
           'scaling (requirements 1\u20133 of the specification, which the '
           'protocol discharges alongside requirement 4); and a '
           'preregistration and adversarial-collaboration discipline that '
           'binds the whole program to the corpus\u2019s own refutation '
           'conditions. Every phase carries its data source, its estimator, '
           'its null model, and its failure condition.')

    L.body(story,
           'What the protocol does not change is stated with the same '
           'prominence, because it is the culmination arc\u2019s own '
           'boundary. The decombination program remains a differentiation '
           'program \u2014 \u201cuseful, not necessary,\u201d in the '
           'counterpart\u2019s words; describing the appearance\u2019s '
           'grammar, never bridging to the Absolute, because there is no '
           'bridge because there are not two banks. The protocol operates '
           'entirely at the conventional level, and its success would '
           'elevate the four-domain predictions from conjectural to tested '
           'without moving the metaphysical premises one tier. The '
           'equivalence-is-not-validation doctrine \u2014 now welded to the '
           'counterpart\u2019s own concession that the framework is \u201ca '
           'metaphysical framework, not a scientific theory\u201d \u2014 '
           'governs the interpretation of every result the protocol could '
           'produce. The map this edition assembles maps the dream\u2019s '
           'grammar, not the dreamer.')

    # ==================== 2. CORPUS STATE ====================
    L.h1(story, '2. Corpus State Carried Forward')

    L.body(story,
           'The audit lineage stands at eleven parties and seven editions. '
           'The consolidation corpus remains: the 130-turn GLM dialogue '
           '(11,088 lines); the Qwen conversations in three shares (60, 66, '
           'and 256 messages); the DeepSeek main line proven through three '
           'snapshots (53 damaged, 88, and 106 full turns \u2014 one '
           'conversation, subsequence-proven); the DeepSeek file exchange '
           '(three turns, all attachments now read); the embedded audit and '
           'the consolidation treatise; the audit lineages of both lines; '
           'the external Claude audit (adjudicated 25 sustained, 2 partially '
           'overruled, 0 reciprocity findings after the retraction); and the '
           'two exported critique files. The empirical source set has now '
           'grown twice: first with the round-12\u201313 anchors (Santander '
           '2025 PNAS split-brain criticality; Modesti 2022 dissociative '
           'disorders review; Schlumpf 2013 and Reinders 2019 DID '
           'neuroimaging; Farnes 2020 ketamine EEG with the Reynante '
           'complexity toolkit), and now with the five papers of this round. '
           'The standing rulings are unchanged: the non-dual culmination '
           'consolidated (D6\u2013D9); the formalization ceiling as a stated '
           'theorem rather than a promissory note; the superdeterminism '
           'tension, the anesthesia fork, and the Divine-Simplicity '
           'indictment documented at their settled grades; the corpus '
           'double-count corrected to a counted eleven.')

    L.body(story,
           'The four empirical domains of the decombination program enter '
           'this edition at the grades the sixth edition assigned them, and '
           'leave at upgraded ones. Psychedelics: anchored by verified '
           'findings and open corpora, and now by the intervention-validated '
           '5-HT2A attribution (Preller 2018) and the published '
           'receptor-to-gain parameterization (Deco 2018) \u2014 the only '
           'arm whose map fragment is complete end to end, from molecular '
           'target through regional parameter to whole-brain dynamics. '
           'Anesthesia: anchored as a verified pathway (open sedation '
           'corpora plus the shared complexity instrument), with the '
           'neural-field tradition (Bojak\u2013Liley, Robinson) supplying '
           'the arm\u2019s quantitative bridge from drug concentration '
           'through field parameters to EEG spectra. Split-brain: anchored '
           'by the Santander criticality finding with open analysis code, '
           'but with no open raw data \u2014 the arm remains '
           'literature-anchored and simulation-only at Level 2. DID: '
           'anchored by signature, switch, structure, and control findings '
           '(Schlumpf, Reinders, Modesti), likewise without open raw data. '
           'The asymmetry is itself evidence: the domains\u2019 testability '
           'at Level 2 is graded by open data availability, and the '
           'protocol\u2019s phase structure reflects that grading honestly '
           'rather than pretending four equal arms.')

    L.body(story,
           'This edition\u2019s deltas, itemized. First, the '
           'round-seventeen verdict correction (chapter 4): the parameter '
           'map\u2019s nonexistence claim is replaced by the '
           'fragments-and-assembly statement, with the five program areas '
           'documented link by link. Second, five new sources read in full '
           '(chapter 3), four of which were the blocked load-bearing items '
           'of the search record. Third, the concrete Level-2 protocol '
           '(chapter 5) \u2014 the first corpus artifact that specifies '
           'simulators, estimators, datasets, null models, '
           'preregistration, and failure conditions together. Fourth, '
           'repairs R28\u2013R31 (chapter 7): the conjectural-status '
           'language is replaced wherever the ingredients now exist; the '
           'elevation-cost \u201cproposals\u201d for \u03b2, J, and a are '
           'replaced by published-method citations; the fetch-infrastructure '
           'record is updated with the user-supplied resolutions; and the '
           'protocol\u2019s scope is bound explicitly to the '
           'conventional-level ceiling. Fifth, the appendix lists every '
           'source this environment still cannot fetch, with full titles '
           'and links, so the interlocutor can supply any that matter.')
