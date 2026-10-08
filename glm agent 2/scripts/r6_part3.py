#!/usr/bin/env python3
"""Sixth Edition (Audited Edition), Part 3: chapters 5-6.

Chapter 5 is the fresh adversarial audit of the fifth edition's own new
claims (the interlocutor's instruction to turn the auditor's eye on the
Fifth Edition). Chapter 6 carries the empirical anchors with the corrected
summary language.
"""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 5. THE FRESH ADVERSARIAL AUDIT ====================
    L.h1(story, '5. The Fresh Adversarial Audit of the Fifth Edition')

    L.h2(story, '5.1 The instruction and the method')

    L.body(story,
           'The interlocutor\u2019s instruction for this round was to '
           'run a fresh adversarial audit of the Anchored Edition '
           'itself \u2014 to turn on the fifth edition\u2019s own new '
           'claims the same auditor\u2019s eye the fifth edition had '
           'turned on the external Claude audit. The method is the '
           'one the lineage already binds: identify the edition\u2019s '
           'load-bearing new claims (the ones that edition itself '
           'introduced, as opposed to carried), re-verify each '
           'against the primary sources rather than against the '
           'edition\u2019s own text, and rule on each as sustained or '
           'corrected. The fifth edition\u2019s new claims were five: '
           'the corpus count of twelve auditing parties; the '
           'adjudication result of roughly thirty points with '
           'twenty-four sustained, two partially overruled, and one '
           'reciprocity finding against the auditor; the anchor '
           'claim that every one of the four domains has at least '
           'one verified empirical anchor; the file-identification '
           'record that resolved the provenance questions; and the '
           'repair set R21\u2013R24 with the pre-registration '
           'discipline. The audit re-verified all five. Two survive '
           'unchanged (the file-identification record, with one '
           'interpretation corrected by the snapshot finding; the '
           'repair set, extended by this round). Three required '
           'correction, and the corrections are the chapter\u2019s '
           'findings.')

    L.h2(story, '5.2 Finding 1: the corpus double-count')

    L.body(story,
           'The fifth edition listed the first and second DeepSeek '
           'exchanges as two auditing parties, describing the first '
           'as a 53-turn conversation on the '
           'universal-consciousness audit line and the second as an '
           '88-turn conversation carrying the eliminative program and '
           'the S1\u2013S4 specification. Re-verification against the '
           'payloads proves they are one conversation. The damaged '
           'first snapshot preserves fifty-four messages '
           '(twenty-seven user turns with text). Every one of those '
           'twenty-seven turns appears in the second snapshot\u2019s '
           'user-turn sequence, in the same order, at exactly '
           'aligned positions: the first six at positions zero '
           'through five, the remaining twenty-one at positions '
           'thirty through fifty. Nothing is missing from the '
           'mapping and nothing is out of order; the gap \u2014 '
           'positions six through twenty-nine of the longer '
           'snapshot \u2014 is the block the first '
           'snapshot\u2019s payload lost to server-side deletion '
           '(the fifty-two deleted messages recorded since the '
           'third edition\u2019s recovery). The attachments '
           'confirm the identity: the critique pair and '
           'decombination.txt sit at identical message indices in '
           'both payloads, which the fifth edition read as the same '
           'files forwarded into two conversations and which the '
           'subsequence mapping shows to be the same files in the '
           'same messages of one conversation. The new 106-turn '
           'share completes the proof: its first 176 messages are '
           'the second snapshot entire, and its final eighteen '
           'turns extend the same line. The DeepSeek main line is '
           'one conversation known through three snapshots '
           '(53-turn damaged, 88-turn, 106-turn full). The ruling: '
           'the fifth edition\u2019s count of twelve auditing '
           'parties is corrected to eleven, with the counting unit '
           'stated and the snapshot relations recorded in the '
           'corpus map. The related observation is recorded without '
           'a separate finding: the fifth edition\u2019s closing '
           'enumeration of its own corpus (two dialogue lines, '
           'four external exchanges, one embedded audit, one '
           'treatise, seven lineage editions, one external audit, '
           'two critique files) does not reconstruct to twelve '
           'under any single unit \u2014 the count was asserted, '
           'not derived, which is precisely the claim-discipline '
           'failure the lineage exists to police.')

    L.h2(story, '5.3 Finding 2: the anchor summary overclaim')

    L.body(story,
           'The fifth edition\u2019s executive summary stated that '
           'the round\u2019s empirical readings gave \u201cevery one '
           'of the decombination program\u2019s four domains at '
           'least one verified empirical anchor.\u201d The '
           'edition\u2019s own anchor table is more honest than its '
           'summary. Three domains are anchored by verified '
           'findings read from source papers: split-brain by the '
           'Santander criticality result, DID by the Modesti '
           'caudate-switching review deepened by Schlumpf 2013 and '
           'Reinders 2019, and the psychedelic/ketamine domain by '
           'the Farnes open-data study with the Reynante '
           'complexity pipeline (an instrument-over-open-data '
           'anchor, itself a slightly weaker grade than a '
           'finding-anchor, but stated as such). The anesthesia '
           'domain\u2019s table row records what the summary '
           'glossed: open sedation EEG corpora identified and '
           'fetch-verified, sharing the Lempel-Ziv instrument '
           'family \u2014 Empirical-Verified as pathway, in the '
           'table\u2019s own words. A verified data pathway plus a '
           'shared instrument is not a verified empirical finding '
           'mapping onto the specification; no anesthesia paper '
           'was read in the anchor round. The ruling: summary '
           'overclaim; the corrected statement \u2014 three '
           'domains finding-anchored, the anesthesia domain '
           'pathway-anchored with its finding still to be read '
           '\u2014 is now the standing language of chapter 6 and '
           'the annex. The summary-fidelity rule adopted as repair '
           'R27 generalizes the correction: no summary layer may '
           'assert more than the table it summarizes, because the '
           'summary is what gets quoted and the table is what gets '
           'checked.')

    L.h2(story, '5.4 Finding 3: the reciprocity finding, retracted')

    L.body(story,
           'The fifth edition\u2019s single finding against the '
           'external auditor was a reciprocity finding: that the '
           'two unverifiable physics items the Claude audit named '
           'as its examples \u2014 a 2026 qubit result described '
           'as violations of Copenhagen bands, and a LIGO Klein '
           'bottle echo \u2014 \u201ccould not be located anywhere '
           'in the transcript by this edition\u2019s own '
           'verification pass.\u201d Re-verification locates both. '
           'The qubit claim appears three times: at L6165 '
           '(\u201crecent experiments with superconducting qubits '
           'have reported statistically significant violations of '
           'Copenhagen prediction bands at the 95% and 99% '
           'confidence levels\u201d), at L6192 (\u201ca 2026 '
           'qubit experiment reported statistically significant '
           'violations of Copenhagen prediction bands\u201d), and '
           'in the interpretation-ranking table at L6223. The '
           'LIGO claim appears across a five-line span: L8573 and '
           'L8621\u20138626, including \u201cthe contested '
           'LIGO/Virgo claim of a 1000 km 5th dimension with a '
           '\u2018Klein bottle\u2019 topology causing '
           'gravitational wave \u2018echoes\u2019\u201d and the '
           'elaboration that follows it. Both sit inside the very '
           'turns the Claude audit had flagged as pasted '
           'outside-model text. The ruling: the reciprocity '
           'finding is retracted in full. The auditor\u2019s '
           'charge \u2014 unverifiable citations in circulation in '
           'the transcript \u2014 is sustained in full, and its '
           'two headline examples are now exhibits for it. The '
           'adjudication count moves from twenty-four sustained, '
           'two partially overruled, one reciprocity finding to '
           'twenty-five sustained, two partially overruled, no '
           'reciprocity finding. What survives from the fifth '
           'edition\u2019s error is the rule it violated: the '
           'exclusion of unverified citations from the empirical '
           'ledger applies to everyone \u2014 and the '
           'verification pass that enforces it must itself be '
           'verifiable. The false negative is the founding case '
           'of the search-protocol rule (R25): '
           'failure-to-locate findings report their search strings '
           'and are re-run with different phrasings before they '
           'are believed. The lineage records the embarrassing '
           'part plainly: the fifth edition used its own '
           'unverified search result to overrule an external '
           'auditor \u2014 the exact pattern (absorbing a claim '
           'rhetorically rather than checking it) the whole '
           'apparatus exists to prevent.')

    L.h2(story, '5.5 Secondary observations')

    L.body(story,
           'Four observations short of findings are recorded. '
           'First, the two partial overrulings of the Claude '
           'audit were re-checked and stand: the pilot-wave '
           'revaluation is announced in-transcript ([114], '
           'L5039\u20135041), and the two-language discipline is '
           'enforced by the consolidations if not by the '
           'transcript. Second, the status-tag regime\u2019s '
           'application in the fifth edition\u2019s chapter 10 is '
           'consistent with its definitions; no tag was found '
           'assigned against its own criteria. Third, the '
           '\u201cseven editions of this audit lineage\u201d '
           'phrase counts companion deliverables (the Dream '
           'critique line, the FEP-inversion critique) as '
           'editions; loose but stated, and harmless once the '
           'counting-unit rule is in force. Fourth, the anchor '
           'chapter\u2019s equivalence-is-not-validation doctrine '
           'was searched for violations \u2014 passages mapping '
           'an anchor onto the framework without the '
           'Interpretive-Mapping tag \u2014 and none were found; '
           'the body\u2019s claim discipline held where the '
           'summary\u2019s did not. The pattern across all five '
           'claims audited is itself the finding: the fifth '
           'edition\u2019s defects concentrated exactly where an '
           'edition is least checked \u2014 its own headline '
           'layer (the party count, the anchor summary, the one '
           'finding that flattered the lineage against its '
           'external critic) \u2014 which is why the '
           'self-audit is now a standing step of the program '
           'rather than a one-time instruction.')

    L.h2(story, '5.6 The verdict on the fifth edition')

    L.body(story,
           'The verdict is that the fifth edition is structurally '
           'sound and summary-layer sloppy: its tables, rulings, '
           'and anchor records are accurate to their sources '
           '(with the one reciprocity exception, which was a '
           'verification failure, not a table failure), and its '
           'headline claims overstate them in two places and '
           'miscount in a third. The corrections are made in '
           'place by this edition, the ruling count is updated, '
           'and the three rules the failures taught '
           '(search-protocol, counting-unit, summary-fidelity) are '
           'adopted as repairs R25\u2013R27 and bound on every '
           'future edition. The net epistemic effect favors the '
           'corpus: the lineage has now demonstrated that its '
           'audit apparatus, turned on itself, finds and fixes '
           'real defects \u2014 including one that reversed a '
           'ruling \u2014 which is the only credential a '
           'self-policing system can earn.')

    # ==================== 6. THE EMPIRICAL ANCHORS ====================
    L.h1(story, '6. The Empirical Anchors, Carried and Corrected')

    L.body(story,
           'The anchor record of the fifth edition is carried '
           'forward with the summary corrected per Finding 2: '
           'three of the decombination program\u2019s four domains '
           'are anchored by verified empirical findings read from '
           'source \u2014 split-brain, DID, and the '
           'psychedelic/ketamine domain \u2014 while the '
           'anesthesia domain is anchored as a verified pathway: '
           'open sedation EEG corpora identified and '
           'fetch-verified, sharing the Lempel-Ziv instrument '
           'family, with its finding still to be read from source. '
           'An anchor, as before, is a verified empirical finding '
           'in the open literature satisfying three conditions: '
           'read from the source rather than secondary discussion; '
           'mapped onto a specific structure of the decombination '
           'specification (the partition threshold, the switching '
           'mechanism, or the complexity measure); and its data '
           'pathway identified. An anchor is not a discriminating '
           'prediction, and the culmination arc has now stated the '
           'reason from the counterpart\u2019s side: the anchors '
           'test the differentiation model at the conventional '
           'level; they never test the Absolute (chapter 4.6). '
           'Equivalence-is-not-validation therefore binds at two '
           'levels \u2014 findings do not validate the '
           'metaphysics, and conventional-level successes do not '
           'bridge to the ultimate \u2014 and every anchor '
           'statement below carries both limits.')

    L.h2(story, '6.1 Split-brain: the Santander criticality result')

    L.body(story,
           'Santander et al. (2025, PNAS 122(43):e2520190122) '
           'studied six adult callosotomy patients with '
           'neuroimaging and behavioral '
           'interhemispheric-transfer testing. The critical case '
           'is patient BT, who retained approximately one '
           'centimetre of the splenium \u2014 roughly ten percent '
           'of the corpus callosum\u2019s cross-sectional area '
           '\u2014 yet showed full interhemispheric integration, '
           'including tactile information transfer, with no '
           'disconnection syndrome; the paper\u2019s own language '
           'is a \u201cunique type of criticality\u201d in which '
           '\u201ca small proportion of posterior callosal fibers '
           'may be sufficient\u201d for integrated function. The '
           'analysis code is open '
           '(tsantander/splitBrainNetworks); patient data are '
           'available on request only. What this anchors is the '
           'threshold structure of the differentiation '
           'specification: integration survives radical substrate '
           'reduction with a threshold character rather than a '
           'linear one. The track\u2019s standing questions are '
           'unchanged \u2014 the posterior-fiber fraction below '
           'which integration collapses, and whether the collapse '
           'is the specification\u2019s predicted second '
           'threshold \u2014 and its failure condition is '
           'carried: if integration degrades linearly with fiber '
           'fraction across the full patient series, the '
           'threshold reading is an artifact of one '
           'patient\u2019s anatomy. Status: Empirical-Verified as '
           'a result; Interpretive Mapping as a reading of the '
           'specification; conventional level throughout.')

    L.h2(story, '6.2 DID: the Modesti caudate-switching result')

    L.body(story,
           'Modesti et al. (2022, Journal of Personalized '
           'Medicine 12:1405) is the systematic review of '
           'functional neuroimaging in dissociative disorders: '
           'thirteen studies, 2006 through 2022, fifty-one DID '
           'patients. Its convergent finding anchors the switching '
           'structure: identity-state alterations are consistently '
           'associated with alterations of the caudate nucleus '
           'and its functional network, with a described '
           '\u201cshift from hippocampal involvement to caudate '
           'involvement\u201d across identity states, alongside '
           'prefrontal and anterior-cingulate findings. What this '
           'supplies at review level is the second half of the '
           'specification\u2019s intervention-validated criteria: '
           'distinct partitions with distinct signatures require '
           'that switching between them have a locatable '
           'mechanism, and the caudate result locates one \u2014 '
           'a subcortical, basal-ganglia structure tied to '
           'action selection and egocentric processing whose '
           'activity shifts with identity state. The open '
           'question is parametric (coupled bistable, '
           'winner-take-all, or graded mixture); the failure '
           'condition is carried: if individual-level analyses '
           'show no state-dependent reorganization beyond the '
           'caudate\u2019s role, the multi-partition '
           'architecture over-describes the domain. Status: '
           'Empirical-Verified as a result; Interpretive Mapping '
           'as a reading; conventional level throughout.')

    L.h2(story, '6.3 Ketamine: the Farnes data and the Reynante pipeline')

    L.body(story,
           'The ketamine anchor is a two-part source: data and '
           'instrument. The data are Farnes et al. (2020, PLOS '
           'ONE 15(11):e0242056): ten subjects measured awake and '
           'under psychoactive ketamine, with EEG and an '
           'eleven-dimension altered-states questionnaire. The '
           'instrument is the re-analysis toolkit supplied to the '
           'corpus: Hilbert-transform amplitude and phase '
           'extraction, Lempel-Ziv complexity with normalized '
           'variants, spectral power, topographic mapping over '
           'standard montages, and the phenomenology-correlation '
           'design, with the source chain pinned to Dryad. What '
           'this anchors is the complexity measure itself: the '
           'domain\u2019s prediction \u2014 psychedelic states '
           'raise signal complexity while dissociative states '
           'reorganize it \u2014 is computable on open data with '
           'a supplied instrument, which upgrades it from '
           'conjectural to runnable. The failure condition is '
           'sharp: run the pipeline, and if the complexity change '
           'is fully accounted for by signal-to-noise artifacts '
           'or spectral redistribution without a '
           'partition-structure signature, the prediction fails '
           'on its own chosen instrument. The anesthesia domain '
           'shares the instrument family: the open propofol and '
           'sedation EEG corpora identified and fetch-verified in '
           'the dataset round carry the same Lempel-Ziv design, '
           'so one pipeline serves two domains \u2014 the '
           'pathway anchor recorded in Table 6.1, at its honest '
           'grade.')

    L.h2(story, '6.4 What anchoring establishes, and what it does not')

    L.data_table(
        story,
        'Table 6.1. The four domains after anchoring, corrected: '
        'three finding-anchors and one pathway-anchor, with failure '
        'conditions.',
        ['Domain', 'Anchor (source, status)', 'Data pathway',
         'Program failure condition'],
        [
            ['Split-brain',
             'Integration survives \u224890% callosal loss; '
             'posterior-fiber sufficiency; \u201cunique type of '
             'criticality\u201d (Santander et al. 2025; '
             'Empirical-Verified finding)',
             'Analysis code open (tsantander/splitBrainNetworks); '
             'patient data on request',
             'Integration degrades linearly with fiber fraction '
             'across the patient series, voiding the threshold '
             'reading'],
            ['DID',
             'Caudate-network switching across identity states; '
             'hippocampal-to-caudate shift (Modesti et al. 2022 '
             'review of 13 studies; Empirical-Verified finding), '
             'deepened by Schlumpf 2013 and Reinders 2019 '
             '(chapter 7)',
             'Papers-only; raw DID neuroimaging remains closed',
             'Individual-level analyses reduce the partition '
             'structure to a single switching node'],
            ['Ketamine / psychedelics',
             'Complexity pipeline over open data: Hilbert + '
             'Lempel-Ziv + 11D-ASC correlation design (Farnes et '
             'al. 2020 data; Reynante toolkit; '
             'Empirical-Verified as instrument-over-open-data)',
             'PLOS ONE open data via Dryad; toolkit fully supplied '
             'in the corpus',
             'Pipeline run shows complexity change fully explained '
             'by artifacts or spectral redistribution'],
            ['Anesthesia',
             'Open sedation EEG corpora identified and '
             'fetch-verified (PhysioNet GABAergic series and '
             'cognates; Empirical-Verified as pathway \u2014 the '
             'domain\u2019s finding-anchor is still to be read '
             'from source)',
             'PhysioNet open access; same LZ instrument family as '
             'the ketamine pipeline',
             'Domain\u2019s access-versus-cessation fork '
             '(chapter 10.2) unresolved by the graded-depth '
             'design'],
        ],
        [0.14, 0.34, 0.24, 0.28])

    L.body(story,
           'What anchoring does not establish is stated twice '
           'because the culmination arc now requires it. First, '
           'no finding in Table 6.1 discriminates '
           'consciousness-first monism from physicalism; every '
           'row is absorbable without remainder into a '
           'physicalist research program, and the '
           'equivalence-is-not-validation rule bars any '
           'announcement to the contrary. Second, no finding '
           'tests the Absolute: the anchors test the '
           'differentiation model \u2014 the conventional-level '
           'account of how the appearance forms domains, '
           'boundaries, and self-models \u2014 and a fully '
           'successful conventional-level program would still '
           'leave the metaphysical question exactly where the '
           'culmination arc left it, decided by coherence, '
           'explanatory power, and cost rather than by evidence. '
           'What the anchors earn is the right to be judged by '
           'stated failure conditions on open data, which is the '
           'graduation criterion the program wrote for itself '
           '\u2014 and which now operates one level down from '
           'where the fifth edition\u2019s rhetoric sometimes '
           'placed it.')
