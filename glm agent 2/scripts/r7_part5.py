#!/usr/bin/env python3
"""Seventh Edition (Parameter-Map Edition), Part 5: chapters 6-8 \u2014
epistemic status, edition delta with repairs R28-R31, and the appendix of
unfetchable sources."""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 6. EPISTEMIC STATUS ====================
    L.h1(story, '6. Epistemic Status: What the Protocol Changes and Cannot')

    L.body(story,
           'The protocol changes the four domains\u2019 status '
           'labels, and only those labels. Before this edition the '
           'standing was: psychedelics, anesthesia, split-brain, and '
           'DID predictions conjectural \u2014 pending a neural '
           'parameter map that the corpus believed absent. The '
           'corrected standing is: conjectural, with the map\u2019s '
           'per-arm ingredients published and the assembly specified '
           'as an executable protocol. The distinction is not '
           'rhetorical. A conjectural claim pending an absent '
           'prerequisite can be deferred indefinitely; a conjectural '
           'claim pending an executable protocol has a falsification '
           'schedule, and the corpus\u2019s own refutation-conditions '
           'discipline requires the schedule to be stated \u2014 '
           'chapter 5 has stated it. What does not change: the '
           'metaphysical premises\u2019 tiers, the non-dual '
           'culmination, the formalization boundary, the '
           'superdeterminism tension\u2019s documented grade, the '
           'adjudication counts, and the equivalence doctrine. The '
           'protocol inherits the doctrine as a hard constraint: '
           'even total success would license only '
           '\u201cthe differentiation program\u2019s four-domain '
           'predictions are tested and surviving,\u201d never '
           '\u201cthe Absolute is thereby evidenced.\u201d')

    L.body(story,
           'The deeper unchanged thing is the two-level structure '
           'itself. The differentiation program is the '
           'appearance-level science of a consciousness-first '
           'metaphysics: it models how one reality\u2019s appearance '
           'differentiates into perspectives, using the grammar '
           'physics already speaks \u2014 coupling, criticality, '
           'domains, blankets, closure. The culmination arc ruled '
           'that this program is \u201cuseful, not necessary\u201d: '
           'the Absolute does not need its differentiation '
           'mechanism to be this one, and no empirical result could '
           'make it necessary, because necessity there is a '
           'category error \u2014 the framework\u2019s own words, '
           'conceded by its own dialectical partner. The protocol is '
           'therefore best understood as the corpus making its '
           'least-necessary component maximally honest: of all the '
           'things the corpus claims, the decombination program is '
           'the one that could fail, so it is the one that must be '
           'given every chance to fail well. An '
           'assembled-but-unexecuted map keeps that chance on the '
           'shelf; a specified protocol with named failure '
           'conditions puts it in writing. This edition\u2019s '
           'contribution to the corpus\u2019s integrity is exactly '
           'that: converting the last deferred empirical claim into '
           'a scheduled one.')

    # ==================== 7. EDITION DELTA ====================
    L.h1(story, '7. Edition Delta and Repairs R28\u2013R31')

    L.body(story,
           'This edition is an increment on the sixth, not a '
           're-typeset of it. The sixth edition\u2019s sixteen '
           'chapters and appendix \u2014 the eleven-party corpus, '
           'the non-dual culmination, the self-audit and its '
           'corrections, the adjudication record, the anchored '
           'empirical annex, the audited premise with its '
           'status-tagged axioms and thirty-five-row objection '
           'ledger \u2014 remain the standing consolidation and are '
           'not duplicated here. The reader of the two volumes '
           'together holds the full corpus state; the reader of '
           'this one alone holds the parameter-map turn: the verdict '
           'correction, the five new sources, the assembled '
           'fragments, and the protocol. The series convention '
           '(every edition self-contained in its front matter and '
           'appendices) is preserved by chapters 1, 2, and 8.')

    L.body(story,
           'Four repairs are logged, continuing the series '
           'numbering. R28 \u2014 the conjectural-status language: '
           'every occurrence of \u201cconjectural until the neural '
           'parameter map exists\u201d in the corpus\u2019s '
           'consolidation artifacts is now annotated \u201c(status '
           'superseded, seventh edition): conjectural until the '
           'assembly is executed; the per-arm ingredients are '
           'published.\u201d R29 \u2014 the elevation-cost '
           'proposals: the \u03b2-to-arousal, J-to-effective-'
           'connectivity, and a-to-attractor-depth proposals are '
           'replaced by the published-method citations of chapter 4 '
           'and the derived estimators of chapter 5, with their '
           'validation conditions named. R30 \u2014 the '
           'fetch-infrastructure record: the round-seventeen report '
           'is updated with the four user-supplied resolutions and '
           'the corrected OpenAlex status (rate-limited this '
           'session; CrossRef and Europe PMC as the standing '
           'fallback). R31 \u2014 the scope binding: the '
           'protocol\u2019s conventional-level ceiling is stated '
           'in the protocol itself (section 5.1 and 5.9), in the '
           'status chapter (this chapter\u2019s predecessor '
           'sections), and on every results-table template the '
           'protocol will ever print \u2014 so that no future '
           'citing artifact can detach the empirical program from '
           'the doctrine that governs its interpretation.')

    L.data_table(
        story,
        'Table 7.1 \u2014 The four domains: grade at the sixth edition '
        'versus grade at this edition (the mapping rows cited are '
        'chapter 4\u2019s).',
        ['Domain', 'Sixth-edition grade', 'Seventh-edition grade', 'Basis of change'],
        [
            ['Psychedelics',
             'Finding-anchored (verified findings + instruments + '
             'failure conditions)',
             'Finding-anchored + complete map fragment '
             '(receptor\u2192gain, intervention-validated target)',
             'P3 and P4 read in full; the arm\u2019s row of the '
             'correspondence table filled end to end'],
            ['Anesthesia',
             'Pathway-anchored (open corpora + shared complexity '
             'instrument)',
             'Pathway-anchored + published parameter-sweep method '
             '(drug\u2192field\u2192spectrum)',
             'Bojak\u2013Liley / Robinson tradition verified and '
             'protocol-embedded; \u03b2 estimator derived'],
            ['Split-brain',
             'Finding-anchored (Santander criticality; open analysis '
             'code)',
             'Unchanged + simulation-ready threshold test '
             '(J<sub>e</sub> shift under disconnection)',
             'Phase-1 estimator + \u00d3dor/Myrov critical-coupling '
             'methods supply the test'],
            ['DID',
             'Finding-anchored (signature + switch + structure + '
             'control findings)',
             'Unchanged + metastable-switch simulation target '
             '(literature-anchored only)',
             'Domain-vs-basin mapping of part switching specified; '
             'no open raw data \u2014 honest limit retained'],
        ],
        [0.13, 0.27, 0.33, 0.27], font_size=8.0, header_font=8.4)

    L.body(story,
           'Consistency checks against the standing ledger: the '
           'objection ledger\u2019s rows concerning empirical '
           'testability (the immunization-by-stratification row and '
           'the unique-confirmed-prediction standard) are '
           'unaffected \u2014 the protocol is the differentiation '
           'program\u2019s answer, and the stratification defense '
           'is precisely not available to it, by the program\u2019s '
           'own honest theorem. The glossary additions this '
           'edition: operating point, critical ridge, DFA exponent, '
           'functional connectivity dynamics (FCD), Kolmogorov\u2013'
           'Smirnov fit distance, receptor-density '
           'parameterization, gain scaling, global brain '
           'connectivity, metabolic connectivity mapping, '
           'permittivity coupling, excitability map, '
           'epileptogenicity threshold, and noise-to-coupling '
           'ratio \u2014 each defined in situ at first use, per the '
           'series convention of defining terms where they appear '
           'rather than compiling a separate apparatus.')

    # ==================== 8. APPENDIX: UNFETCHABLE ====================
    L.h1(story, '8. Appendix A \u2014 Sources This Environment Still Cannot Fetch')

    L.body(story,
           'The interlocutor asked for any links that cannot be '
           'fetched, with links or full titles supplied so that '
           'anything wanted can be uploaded. The table below is '
           'the complete current list, after the four '
           'load-bearing resolutions of this round. None of the '
           'remaining items blocks the protocol \u2014 every '
           'protocol-critical source is now read or verified '
           '\u2014 but several would strengthen specific phases, '
           'and each is listed with its full title, its link, and '
           'what it would add. Publisher-level blocks (HTTP 403 '
           'to this environment\u2019s requests) are marked; '
           'where an open mirror exists it is given instead.')

    L.data_table(
        story,
        'Table 8.1 \u2014 Remaining unfetchable sources (as of this '
        'round), with full titles for user supply.',
        ['Full title / item', 'Link', 'Status; what it would add'],
        [
            ['Bedford, P. et al. 2023. \u201cThe effect of lysergic '
             'acid diethylamide (LSD) on whole-brain functional '
             'connectivity: regression dynamic causal modelling.\u201d '
             'Scientific Reports',
             'nature.com/articles/s41598-023-39139-w (Nature domain '
             'fetchable; article page not probed this round)',
             'Phase 3 support: rDCM effective-connectivity changes '
             'at scale'],
            ['Avram, M. et al. 2024. \u201cEffective Connectivity of '
             'Thalamocortical Interactions under Psychedelics.\u201d '
             'Biological Psychiatry: CNNI',
             'biologicalpsychiatrycnni.org (403 to this environment)',
             'Phase 3 support: spectral DCM of substance-induced '
             'connectivity changes'],
            ['Liang, Z. et al. 2015. \u201cA Pharmacokinetics-Neural '
             'Mass Model (PK-NMM) for propofol-induced '
             'anesthesia.\u201d (PMC-indexed)',
             'pmc.ncbi.nlm.nih.gov (root fetchable; article '
             'challenge-gated from this IP)',
             'Phase 2 support: explicit drug-level\u2192EEG bridge'],
            ['Butler, J. J. et al. 2025. \u201c5-HT2A receptors '
             'shape whole-brain monoaminergic [dynamics].\u201d '
             'ScienceDirect',
             'sciencedirect.com (400/403)',
             'Phase 3 support: receptor-agonist/antagonist '
             'perturbation of the serotonergic organization'],
            ['Piccinini, J. I. et al. 2025. \u201cTransient '
             'destabilization of whole brain dynamics induced [by '
             'psychedelics].\u201d Nature journal',
             'nature.com (domain fetchable; specific article not '
             'yet resolved)',
             'Phase 3 support: molecular-signaling pathway account'],
            ['Fabus, M. et al. 2023. \u201cSpatiotemporal brain '
             'dynamics induced by propofol and [sedation].\u201d '
             'DPhil thesis, University of Oxford',
             'ora.ox.ac.uk (403)',
             'Phase 2 support: multi-line propofol investigation'],
            ['Farnes, N. et al. 2020 (raw EEG). \u201cIncreased '
             'signal diversity/complexity ... ketamine-induced '
             'psychedelic state.\u201d PLOS ONE \u2014 Dryad raw '
             'data',
             'datadryad.org/doi:10.5061/dryad.j9kd51c9q (200 '
             'fetchable \u2014 listed for data logistics only)',
             'Phase 2/3 data: raw .fdt/.set EEG (the supplied zip '
             'lacks them)'],
            ['Research-collection.ethz.ch \u2014 ETH Zurich research '
             'collection (institutional block, all items)',
             'research-collection.ethz.ch (403 to this IP range)',
             'Provenance: Schlumpf 2013 raw metadata (paper itself '
             'already read from user supply)'],
        ],
        [0.40, 0.32, 0.28], font_size=7.9, header_font=8.3)

    L.body(story,
           'Methodological note on the list: the search-protocol '
           'rule governs it. A blocked link is a fact about this '
           'environment\u2019s egress, not about a source\u2019s '
           'existence or quality; conversely, an item\u2019s '
           'absence from this list is not a claim that it is '
           'fetchable everywhere. The four load-bearing items '
           'resolved this round (Jirsa 2017 from Elsevier; Myrov '
           'et al. from bioRxiv; Deco et al. 2018 from Cell Press; '
           'Preller et al. 2018 from eLife) were all on the '
           'previous round\u2019s list and are now read in full '
           'from source, with the extractions archived. The '
           'protocol\u2019s critical path depends on no item '
           'remaining on this list; the items that would strengthen '
           'it are marked in the third column, and the '
           'interlocutor\u2019s supply channel \u2014 the upload '
           'directory \u2014 remains the standing resolution '
           'route.')
