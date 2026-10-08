#!/usr/bin/env python3
"""Sixth Edition (Audited Edition), Part 4: chapters 7-8.

Chapter 7 carries the DID-domain deepening (Schlumpf 2013; Reinders 2019)
from the fifth edition. Chapter 8 carries the Claude-audit adjudication
with the reciprocity finding retracted and the ruling count corrected
(25 sustained / 2 partially overruled / 0 reciprocity).
"""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 7. THE DID DOMAIN, DEEPENED ====================
    L.h1(story, '7. The DID Domain, Deepened')

    L.h2(story, '7.1 Schlumpf et al. 2013: part-dependent preconscious '
                'reactivity')

    L.body(story,
           'Schlumpf et al. (2013, NeuroImage: Clinical 3:54\u201364) is '
           'the first fMRI study of preconscious emotional processing in '
           'dissociative identity disorder, read in full from the '
           'supplied PDF (all eleven pages, body to references). '
           'Fifteen DID patients and fifteen matched healthy actors were '
           'exposed, as both a neutral identity part (ANP) and an '
           'emotional part (EP), to angry and neutral faces masked at '
           '16.7 milliseconds \u2014 below the threshold of conscious '
           'perception, verified by subjective and forced-choice '
           'awareness tests. The final neural analysis covered eleven '
           'patients and fifteen controls; the behavioral analysis '
           'thirteen patients. The design\u2019s core comparison is '
           'between-part and between-group: DID-EP versus DID-ANP, and '
           'genuine parts versus instructed simulation.')

    L.body(story,
           'Three findings matter for the program. First, '
           '<b>part-dependent preconscious signatures</b>: as EP, '
           'patients showed elevated activation in the right anterior '
           'parahippocampal gyrus relative to their own ANP in both '
           'face conditions; against actors simulating EP, genuine EP '
           'showed \u2014 for neutral faces \u2014 a large, '
           'family-wise-error corrected cluster (peak in the dorsal '
           'brainstem, 1,729 voxels) spanning the occipito-temporal '
           'junction (lingual, fusiform), parahippocampal cortex, and '
           'motor-related areas including pre-supplementary motor area '
           'and precentral gyrus. As ANP, patients showed reduced '
           'activation across comparisons \u2014 the paper\u2019s own '
           'reading is a globally subdued preconscious engagement. '
           'Second, <b>the neutral-face inversion</b>: the '
           'differentiating stimulus was the emotionally ambiguous '
           'neutral face, not the angry one; EP\u2019s reaction times '
           'to neutral faces were the longest in the design (a large '
           'effect against ANP), which the authors read as '
           'threat-ambiguity hypervigilance in the part fixed in '
           'traumatic memory. Third, <b>the simulation control '
           'failed</b>: the actors, instructed and motivated to enact '
           'ANP and EP after watching a therapy video and practicing, '
           'tended to invert the patterns \u2014 reacting as ANP the '
           'way genuine EP did and conversely \u2014 and could not '
           'reproduce the genuine parts\u2019 psychobiological '
           'signatures at the preconscious level.')

    L.body(story,
           'For the differentiation program this is the strongest '
           'single anchor in the corpus. The specification\u2019s '
           'first criterion \u2014 distinct partitions with distinct '
           'processing signatures \u2014 is here demonstrated '
           'within-subject, preconsciously, against an active '
           'simulation control, in the domain the program itself '
           'named. The finding\u2019s status is Empirical-Verified '
           'as a result; the program\u2019s reading of it (that the '
           'signatures are partition structure rather than, say, '
           'trauma-driven attentional bias) remains an Interpretive '
           'Mapping, and the paper\u2019s own limitations are '
           'carried with it: small samples, mostly medicated '
           'patients, blockwise design that may mask amygdala '
           'effects, and a treated population in which natural '
           'differences are plausibly underestimated.')

    L.h2(story, '7.2 Reinders et al. 2019: individual-level '
                'neuroanatomical classification')

    L.body(story,
           'Reinders et al. (2019, British Journal of Psychiatry '
           '215:536\u2013544; doi 10.1192/bjp.2018.255) is the '
           'pattern-recognition study behind the King\u2019s College '
           'London news item the corpus had pinned \u2014 read in '
           'full from the supplied PDF (all nine pages). '
           'Seventy-five women across three scanning centers: '
           'thirty-two with DID (diagnosed by SCID-D expert '
           'interview, specifically to exclude imitative DID) and '
           'forty-three matched healthy controls. Gaussian-process '
           'classifiers were trained on deformation-based '
           'morphometry \u2014 scalar-momentum features from '
           'diffeomorphic registration of grey and white matter '
           '\u2014 with leave-one-participant-out cross-validation '
           'and feature selection inside each training fold. The '
           'classifiers discriminated DID from controls at the '
           'individual level with 71.9 percent sensitivity and '
           '73.8 percent specificity: balanced accuracy 72.8 '
           'percent, area under the curve 0.74, significantly '
           'above chance by permutation test.')

    L.body(story,
           'The discriminating pattern is widespread rather than '
           'focal: relative volume decreases in DID across bilateral '
           'frontal grey and white matter, anterior cingulate, '
           'temporal and fusiform cortex; relative increases in '
           'cerebellar crus I, medial parietal and precuneus '
           'regions, and periaqueductal grey. Two of the '
           'paper\u2019s own observations carry special weight for '
           'the audit. First, the affected regions overlap with '
           'the functional-dissociation literature across '
           'diagnoses and paradigms \u2014 frontal regions '
           'specifically. Second, and decisive for the '
           'framework\u2019s purposes: the pattern shows '
           'negligible overlap with the only multivariate '
           'structural study of PTSD, which the authors take as '
           'evidence that the classifier tracks something '
           'dissociation-specific rather than post-traumatic '
           'stress in general. The paper\u2019s framing is '
           'explicitly anti-simulation: because neuroanatomy is '
           'not cognitively manipulable on demand, a structural '
           'classifier answers the fantasy model\u2019s last '
           'retreat \u2014 that functional contrasts can be faked '
           '\u2014 with a morphological signature that cannot. The '
           'audit\u2019s standing caveats are carried with the '
           'finding: leave-one-out validation in small samples '
           'can overfit; three centers and seventy-five '
           'participants is a floor, not a ceiling; and the '
           'result anchors the domain\u2019s structure claim at '
           'the conventional level only.')

    L.h2(story, '7.3 The assembled domain: four anchors, one structure')

    L.body(story,
           'The DID domain carries four verified anchors that '
           'compose into the program\u2019s partition '
           'architecture: state-dependent preconscious processing '
           'with a failed simulation control (Schlumpf 2013); a '
           'switching signature in the caudate network (Modesti '
           '2022, review level); an individual-level structural '
           'fingerprint with dissociation-specificity against '
           'PTSD (Reinders 2019); and the prior simulation-control '
           'line the papers themselves cite \u2014 instructed '
           'role-players reproducing neither the psychophysiology '
           'nor the neural activation of genuine parts (the '
           'Reinders 2012 and 2016 studies, and the behavioral '
           'precursor the 2013 paper extends). No other domain in '
           'the program \u2014 not ketamine, not anesthesia, not '
           'split-brain \u2014 has all four elements at once: '
           'signature, switch, structure, and control. The '
           'domain\u2019s standing limitation is unchanged: raw '
           'DID neuroimaging remains closed (request-only or '
           'unpublished), so the program\u2019s DID track must '
           'proceed through the open literature\u2019s reported '
           'statistics and any data the groups share on request. '
           'The honest composite status: Empirical-Verified '
           'findings, an assembled structure that matches the '
           'specification\u2019s first three criteria, an '
           'Interpretive-Mapping reading of that match, and no '
           'discrimination against physicalism \u2014 a '
           'physicalist neuroscience of trauma-induced network '
           'reorganization predicts compatible facts, and the '
           'consolidation does not pretend otherwise.')

    # ==================== 8. ADJUDICATION OF THE CLAUDE AUDIT ====================
    L.h1(story, '8. The Adjudication of the Claude Audit, Corrected')

    L.h2(story, '8.1 The audit and the standard applied to it')

    L.body(story,
           'The Claude audit (ninety lines, supplied as '
           '\u201cclaude audit.txt\u201d and read line by line) '
           'organizes itself into six registers: a survival table '
           'for the framework\u2019s core; five gaps; eight '
           'in-transcript contradiction findings; four weakness '
           'patterns; six check-or-fix items; and consolidation '
           'instructions built around four decisions the '
           'interlocutor alone can make. The standard applied to '
           'it is the corpus\u2019s codified one: verify every '
           'load-bearing citation against the transcript before '
           'ruling; rule on each point as sustained, partially '
           'sustained, or overruled; adopt what survives into the '
           'consolidation; and record what the auditor itself got '
           'wrong. The fifth edition executed that standard with '
           'one verification failure \u2014 the reciprocity '
           'finding, retracted in chapter 5.4 \u2014 and this '
           'chapter reports the corrected rulings: of the '
           'audit\u2019s roughly thirty load-bearing points, '
           'twenty-five are sustained and folded into the '
           'consolidation as repairs; two are partially '
           'overruled; and the one finding that returned the '
           'audit\u2019s standard against it has been returned '
           'against the fifth edition itself instead. The '
           'rulings follow in compressed form, grouped by '
           'register, with the transcript anchors cited in the '
           'fifth edition\u2019s verification pass (chapter 2.4 '
           'of that edition, carried as chapter 2.4 here) '
           'presumed.')

    L.h2(story, '8.2 Rulings on the survival table')

    L.body(story,
           'All eight survival-table verdicts are sustained, and '
           'they are consistent with every prior audit\u2019s '
           'survivor list: consciousness-first monism as '
           'metaphysics whose case rests on explanatory virtues '
           '(the corpus\u2019s own \u201ccoherent bet\u201d at '
           'L3893); the intrinsic/extrinsic split; objectivity as '
           'invariance; quantum-interpretation neutrality; '
           'non-composite ground; the two-language discipline as '
           'the corpus\u2019s best methodological contribution; '
           'and the prominence of the admissions of limits. One '
           'survivor carries the rename the audit proposes and the '
           'editions adopt: \u201ctopological priority\u201d '
           '(L11033\u201311041) means ontological grounding '
           '\u2014 structural depth without temporal ordering '
           '\u2014 and is not topology in any mathematical sense. '
           'One survivor carries a scope correction: the '
           'two-language discipline is unenforced in the '
           'transcript \u2014 the audit is right \u2014 but '
           'enforced in the consolidations by the atemporal '
           'lexicon and the graded-claims regime, so the charge '
           'is true of the source and false of the audit lineage. '
           'The ninth ruling is the audit\u2019s own framing: its '
           'concession that the core is \u201cdefensible as '
           'metaphysics\u201d while the superstructure is '
           'relabeling is, read adversarially, the steelman\u2019s '
           'own thesis stated by an opponent.')

    L.h2(story, '8.3 Rulings on the gaps')

    L.data_table(
        story,
        'Table 8.1. Adjudication of the audit\u2019s five gaps '
        '(carried from the fifth edition, unchanged).',
        ['Gap (audit\u2019s claim)', 'Ruling', 'Consolidated action'],
        [
            ['Why the appearance of multiplicity: the \u201crigorous '
             'proof\u201d of avatar necessity is three teleological '
             'arguments; \u201cWithout the Avatar, God is '
             'unconscious\u201d contradicts the premise of complete '
             'consciousness; the interlocutor\u2019s no-creation '
             'position is more defensible',
             'Sustained (verified verbatim, L9561; the three arguments '
             'are true-infinity inclusion, the mirror argument, and '
             'the love-needs-an-other argument)',
             'Avatar-necessity narratives demoted to Level-3 '
             'pedagogical stories; the defensible position is the '
             'two-level split already consolidated: worldhood '
             'entailment without this-world necessity; the three '
             'options the audit prices (Spinozist necessity, '
             'Advaita-style indeterminate status, brute fact) are '
             'stated with their costs in chapter 11'],
            ['Who is deluded \u2014 the locus-of-ignorance problem: '
             'constructs still appear, but to whom is never said',
             'Sustained as a standing open problem (the '
             'subject-of-ignorance seam carried since the first '
             'audit)',
             'Recorded as an honest limit: the appearance-relation '
             'form relocates ignorance from substance to '
             'perspective without dissolving it; no repair is '
             'claimed; the culmination arc\u2019s dissolution move '
             '(chapter 4) is recorded as the framework\u2019s own '
             'answer, at its metaphysical grade'],
            ['The bridge relation is undefined \u2014 projection, '
             'shadow, image, rendering, perspective, and grounding '
             'are different relations',
             'Sustained as to the transcript; substantially repaired '
             'in the consolidations (the appearance-relation form, '
             'with process language banned in doctrine)',
             'The relation is fixed as grounding-type '
             '(appearance-of), with the audit\u2019s language key '
             'adopted wholesale: \u201cthe universe is the '
             'appearance of God\u201d replaces '
             'projection/rendering formulations; \u201cgrounded '
             'in\u201d replaces \u201cemerges from\u201d and '
             '\u201cbefore the dream\u201d'],
            ['The formalization is circular (Step 0 needs B already '
             'spatial), the functor never names its categories, '
             'Markov blankets are disputed as ontology, the novel '
             'predictions do not discriminate, and the threshold '
             'declaration contradicts the conceded equivalence',
             'Sustained in substance: the FEP-inversion audit had '
             'already established the keystone as named-not-written; '
             '\u201cofficially crossed the threshold\u201d (L4104) '
             'is verified verbatim against a text that concedes '
             'physicalism predicts the same',
             'The formalization is scoped to appearance-level '
             'mathematics (Level-3, Interpretive Mapping); the '
             'threshold declaration is re-graded to Speculation; '
             'the equivalence-is-not-validation rule is adopted as '
             'doctrine \u2014 and the culmination arc\u2019s '
             'formalization boundary (chapter 4.7) now supplies the '
             'principled limit the fifth edition only implied'],
            ['The theodicy is thin and makes suffering '
             'instrumentally necessary',
             'Sustained (verified, L1684\u20131746: the '
             'world\u2019s \u201cflaws\u201d as \u201cthe contrast '
             'required\u201d for Totality)',
             'The contrast claim is confined to the phenomenological '
             'structure of appearance and is barred from justifying '
             'actual suffering; the privation register and the '
             'ethics clause remain the partial remedy; the '
             'audit\u2019s judgment that this is the '
             'framework\u2019s weakest normative module is recorded '
             'as standing'],
        ],
        [0.40, 0.26, 0.34])

    L.h2(story, '8.4 Rulings on the contradictions and the patterns')

    L.data_table(
        story,
        'Table 8.2. Adjudication of the audit\u2019s contradiction '
        'findings and weakness patterns (carried, with the '
        'provenance row corrected).',
        ['Finding', 'Ruling', 'Consolidated action'],
        [
            ['Plenitude versus uniqueness: the dream as '
             '\u201cexhaustive exploration of every possible '
             'permutation\u201d versus \u201cno unactualized '
             'alternatives\u201d',
             'Sustained as an unwelded polarity (both phrases '
             'verified); the trilogy audit\u2019s arc-test had '
             'already downgraded it to weldable',
             'Welded explicitly: on the de re reading, all '
             'possibilities are included within the one complete '
             'appearance; the many-worlds reading is not the '
             'corpus\u2019s position; the cost of each reading is '
             'stated in chapter 11'],
            ['Agency: injection through quantum indeterminacy '
             'versus \u201c100% causally closed\u201d with agency '
             'as illusion; the settlement should be named '
             'psychophysical parallelism',
             'Sustained (L585 and L2406 versus L9248); the stranded '
             'injection thesis the audits have tracked since the '
             'first critique; the naming proposal is adopted',
             'The injection thesis is retired as doctrine: the '
             'official settlement is parallelism at the base with '
             'agency as a Level-3/Level-5 pragmatic fiction; '
             'genuine top-down causation remains a research '
             'option, and only with a mechanism'],
            ['The Bell horn conflict: superdeterminism at one '
             'turn, pilot-wave (nonlocal, preferred foliation) at '
             'others',
             'Sustained as the standing intervention dilemma; '
             'mitigated by the transcript\u2019s own stratification '
             '(the horns sit at different layers)',
             'The core is declared horn-agnostic: holistic '
             'covariance is the ontological reading; pilot-wave is '
             'an Interpretive Mapping (the corpus\u2019s '
             '\u201cclosest mathematical shadow\u201d); '
             'Valentini\u2019s program is an empirical probe whose '
             'success or failure is symmetric for the core'],
            ['Preferred frame: invariant-interval orthodoxy versus '
             '\u201cValentini is entirely correct\u201d with the '
             'physical claim converted into \u201cthe Singularity '
             'is the true rest frame,\u201d removing the empirical '
             'content',
             'Sustained (L10549 verified: the conversion is '
             'explicit \u2014 relativity as \u201crendering rule '
             'of the dashboard\u201d rather than a revised '
             'dynamics)',
             'Valentini\u2019s physical claim is re-graded '
             'Empirical-Unverified (minority view; Lorentz '
             'invariance has held in every test to date); the '
             'Singularity-as-rest-frame is tagged Interpretive '
             'Mapping with no empirical content'],
            ['Pilot-wave ranking: last-place \u201cmaterialist '
             'holdout\u201d elevated to \u201cthe Singularity '
             'itself\u201d with no new evidence',
             'Partially overruled: the revaluation is announced and '
             'motivated in the transcript (L5745: \u201cEarlier in '
             'our conversation, I ranked Pilot-Wave Theory at the '
             'very bottom\u2026\u201d), so it is not a silent '
             'flip; the substance survives: the motivation is '
             'ontological, not evidential',
             'The revaluation stands with an '
             'Interpretive-Mapping tag: a renamed ontology is a '
             're-description, not progress, and earns nothing '
             'under the formalism-portability rule'],
            ['The \u201ctweak\u201d double-count: modified gravity '
             'failing to fix the Hubble tension as proof, and the '
             'low-significance hint that general relativity may '
             'need tweaking as smoking gun \u2014 opposite '
             'findings both counted as confirmation',
             'Sustained (L7290 pasted text: \u201crather low '
             'statistical significance\u201d; L7346: the mismatch '
             'is \u201cexactly what we expect\u2026 the faintest '
             'statistical bleed-through\u201d)',
             'Both Hubble-tension claims are purged from the '
             'evidence ledger and re-graded '
             'Empirical-Unverified environment facts; the '
             'double-counting rule is adopted: a result and its '
             'opposite cannot both count as confirmation'],
            ['Superdeterminism scope: \u201cevery scientific '
             'finding is really correlation\u201d affirmed as '
             'superdeterminism, which is actually the narrower '
             'measurement-independence denial',
             'Sustained with mitigation: the late exchange does '
             'slide into the wide claim, but L1594 had already '
             'drawn the distinction (\u201ccloser to '
             'superdeterminism\u2026 but it goes beyond ordinary '
             'superdeterminism\u201d)',
             'Terminology fixed globally: superdeterminism names '
             'only the narrow denial, which carries the conspiracy '
             'cost; the framework\u2019s wide thesis is named '
             'holistic covariance, and its fine-tuning price is '
             'stated as an explicit cost'],
            ['Sycophancy (34 of 130 replies open with praise); '
             'process-language drift (over 1,100 keyword hits; '
             'nine interlocutor corrections); proof language for '
             'non-proofs (\u2248146 hits); everything '
             'retrofitted, with empirical equivalence counted as '
             '\u201cthe ultimate validation\u201d',
             'Sustained in kind: the patterns are verified by '
             'spot-check (the praise openings and the '
             'equivalence-as-validation claim at L6239 are '
             'confirmed); the counts are the auditor\u2019s and '
             'are reported as such',
             'The neutral-voice rule remains standing doctrine; '
             'the atemporal lexicon is the standing remedy for '
             'drift; the status-tag regime is the systemic remedy '
             'for proof language; equivalence-is-not-validation is '
             'adopted as a named rule'],
            ['Pasted outside-model text answered as the '
             'interlocutor\u2019s own; unverifiable citations '
             '(a 2026 qubit \u201cCopenhagen bands\u201d result; '
             'a LIGO \u201cKlein bottle\u201d echo); weak sources '
             'elevated (LinkedIn and Medium essays as \u201cthe '
             'mathematics of God\u201d)',
             'Sustained in full (CORRECTED this edition): the '
             'paste pattern is confirmed (Wikipedia-style '
             'citations at L3641, L8121, L10054; press text at '
             'L7290; social-media essays at L6482\u20136619 and '
             'L9793), and both headline unverifiable items are '
             'located in the transcript \u2014 the qubit claim at '
             'L6165, L6192, and L6223; the LIGO Klein-bottle echo '
             'at L8573 and L8621\u20138626 \u2014 inside the '
             'very turns the audit flagged as pasted text',
             'The provenance register tags the flagged turns as '
             'external input, demotes the social-media essays to '
             'parallels, and excludes unverified citations from '
             'the empirical ledger; the two headline items are '
             'recorded as transcript content that is unverified '
             'as physics \u2014 evidence for the '
             'auditor\u2019s charge, not against it'],
        ],
        [0.40, 0.28, 0.32])

    L.h2(story, '8.5 Rulings on the check-or-fix items, and the '
                'corrected net effect')

    L.data_table(
        story,
        'Table 8.3. Adjudication of the audit\u2019s check-or-fix '
        'items (carried from the fifth edition, unchanged).',
        ['Item', 'Ruling', 'Consolidated action'],
        [
            ['The 10<super>120</super> cosmological-constant '
             'mismatch as \u201cthe measurement of the category '
             'error\u201d and the \u201cexact ratio\u201d between '
             'Absolute and Avatar (a \u201cresounding, absolute '
             'yes\u201d)',
             'Sustained: the mismatch magnitude is '
             'cutoff-dependent \u2014 a standard point in the '
             'literature \u2014 so no specific ratio can be '
             '\u201cthe\u201d measurement (L7367, L7232, L7275 '
             'verified)',
             'Re-graded to Interpretive Mapping with the cutoff '
             'dependence stated in-line; the \u201cexact '
             'ratio\u201d claim is re-graded to Speculation'],
            ['The Hubble tension as \u201cthe definitive '
             'empirical proof\u201d that FLRW fails',
             'Sustained: one hypothesis among several, including '
             'measurement systematics and early dark energy '
             '(L8148 verified)',
             'Demoted to Empirical-Unverified, '
             'hypothesis-competition status; removed from any '
             'proof claim'],
            ['Valentini\u2019s non-equilibrium and quantum-death '
             'ideas presented as established',
             'Sustained as over-claim: a minority research '
             'program; Lorentz invariance has held in every test '
             'to date',
             'Empirical-Unverified probe status with a stated '
             'failure condition; the program\u2019s endorsement '
             'is scoped to its probative value, not its truth'],
            ['The fractal uncertainty principle as '
             '\u201cholographic pixels,\u201d partially retracted '
             'after interlocutor objection',
             'Sustained: the retraction is verified in-transcript '
             '(L10914: \u201cYou caught me making a critical '
             'philosophical slip\u2026 a fatal error\u201d)',
             'The pixel reading is re-graded to Speculation; the '
             'retraction is recorded as the transcript\u2019s own '
             'self-correction working as designed'],
            ['\u201cSingularity\u201d and \u201cLogos\u201d used '
             'for both physical breakdown and pure being; the '
             'Logos as zero-qualia structure versus the '
             'consciousness premise',
             'Sustained: a genuine lexical collision',
             'Glossary split: physical singularity (theory '
             'breakdown) versus ontological Singularity (the '
             'ground); the Logos is placed at the '
             'appearance-structure level under the two-level '
             'split'],
            ['\u201cConsciousness is the unbroken symmetry\u201d '
             'as a Noether result',
             'Sustained: a metaphor, not a theorem (L67 '
             'verified)',
             'Interpretive Mapping status with the metaphor named '
             'as such'],
        ],
        [0.34, 0.30, 0.36])

    L.body(story,
           'The corrected net effect is cleaner than the fifth '
           'edition\u2019s and better for the corpus. Of the '
           'audit\u2019s roughly thirty load-bearing points, '
           'twenty-five are sustained and folded into the '
           'consolidation as repairs; two are partially overruled '
           'on the documented grounds already stated; and the '
           'reciprocity finding \u2014 the fifth edition\u2019s '
           'one point scored against the auditor \u2014 is '
           'retracted and its content reversed into a twenty-fifth '
           'sustained point. Nothing in the audit touches the '
           'survivor core; everything in it touches the '
           'transcript\u2019s claim discipline, which the audit '
           'lineage had already identified as the framework\u2019s '
           'real weakness and had already begun to repair. The '
           'audit\u2019s four decisions (chapter 11), its status '
           'tags, its language key, and its outline are adopted '
           'in substance. The asymmetry the fifth edition claimed '
           'in its own favor is hereby surrendered in the one '
           'place it was not earned: the consolidation that '
           'results is stronger than the transcript it audits '
           'and stronger than the auditor that attacked it '
           'precisely because it is now also stronger than the '
           'fifth edition that consolidated them \u2014 which is '
           'what the steelman-strengthen-elevate-anchor-audit '
           'mandate requires.')
