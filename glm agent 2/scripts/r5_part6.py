#!/usr/bin/env python3
"""Fifth Edition (Anchored Edition), Part 6: chapters 12-14 + Appendix A.

The extended objection-response ledger (24 carried rows compressed + 6 new),
the anchored empirical annex, the glossary and language key with the
collision fixes, and the updated corpus map.
"""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 12. THE OBJECTION-RESPONSE LEDGER ====================
    L.h1(story, '12. The Objection\u2013Response Ledger')

    L.body(story,
           'The ledger states every major objection at its strongest, the '
           'best response the corpus fields, and the verdict under the '
           'standing grades \u2014 Survives (defensible at its honest '
           'grade), Wounded (stands after repair), Open (no adequate '
           'response; carried as liability), and Elevated (open, with a '
           'research program and stated failure conditions). The '
           'twenty-four rows carried from the fourth edition are '
           'compressed here to their load-bearing content; six new rows '
           '(marked with an asterisk) enter from this round\u2019s '
           'materials: the adversarial audit, the exported critiques, and '
           'the anchors.')

    L.data_table(
        story,
        'Table 12.1. The consolidated objection\u2013response ledger, '
        'fifth edition.',
        ['Objection (strongest form)', 'Best corpus response', 'Verdict'],
        [
            ['Decombination: one mind becomes many private subjects; '
             'the mechanism is asserted, not derived',
             'The formal S1\u2013S4 specification with its correction '
             'chain and the Level-2 protocol; now anchored \u2014 '
             'signature, switch, structure, and control in the DID '
             'domain (chapter 5)',
             'Elevated'],
            ['Empirical underdetermination: the same data fit '
             'physicalism; the framework supplies no unique predictions',
             'Conceded at every grade; the two-program annex with its '
             'graduation criterion; equivalence-is-not-validation now '
             'binding in both directions',
             'Open (honest)'],
            ['Explains everything, therefore nothing: immunization by '
             'absorption',
             'The stratification\u2019s firewall acknowledged; '
             'refutation conditions written and extended (chapter '
             '11.3)',
             'Open'],
            ['Hard-problem inversion: mind creating matter is equally '
             'unexplained',
             'The inversion is stated as ontological, not dynamical; '
             'the phenomenal free-energy functional remains the '
             'uncollected promissory note',
             'Open'],
            ['Quantum-mind empirics: the brain is too warm, wet, noisy',
             'The corpus retired microtubule specifics; the '
             'interpretation-neutral core carries no quantum-mind '
             'empirical claim',
             'Survives'],
            ['Born rule: why these probabilities?',
             'The Valentini equilibrium program as a priced probe '
             '(Empirical-Unverified); the equilibrium reading is an '
             'Interpretive Mapping',
             'Wounded'],
            ['Why this branch, this outcome?',
             'The two-level split: this-world contingency is carried, '
             'not explained \u2014 the honest answer the audits '
             'enforced',
             'Open (honest)'],
            ['Boltzmann brains and typicality',
             'The atemporal reading dissolves the typicality question '
             'at the cost of refusing the measure-theoretic game',
             'Wounded'],
            ['Solipsism: are others unreal?',
             'Finite perspectives as modes of the one appearing; the '
             'appearance\u2019s objectivity grammar; the ethics clause',
             'Survives'],
            ['Privation: suffering as the cost of contrast',
             'The register\u2019s objective vocabulary; the new bar: '
             'contrast explains the structure of appearance, never '
             'justifies actual suffering',
             'Wounded'],
            ['Semantic externalism: dream-talk refers inside the dream',
             'The two-language rule with the appearance-relation '
             'vocabulary; pedagogical asides labeled as such',
             'Survives'],
            ['Causal closure: does mind push particles?',
             'The parallelism settlement (chapter 9): closure holds '
             'at the appearance level; the injection thesis retired '
             'to a mechanism-requiring research option',
             'Wounded'],
            ['Misuse of scientific authority',
             'The provenance register and the tag regime; purged '
             'claims (Hubble tension, the exact ratio); the '
             'double-counting rule',
             'Wounded (systemically repaired)'],
            ['Modal overreach: \u201cnecessary\u201d without modal '
             'systems',
             'The exported critiques\u2019 rubric (Table 7.1); the '
             'conditional core with the classical extensions re-graded',
             'Wounded'],
            ['The two-level structure is an internal contradiction',
             'The appearance-relation form: one reality appearing, '
             'not two coexisting (the eliminative exchange\u2019s own '
             'correction, E2 T74\u2013T75)',
             'Survives (repaired form)'],
            ['Brute fact is a stable alternative',
             'Priced, not refuted: A6 is conditional on rejecting it; '
             'the brute-fact self-undermining argument is recorded at '
             'its honest grade',
             'Open (priced)'],
            ['The impasse is fatal: regress, brute fact, or the '
             'necessary ground',
             'The three horns stated with costs; the ground option '
             'carried as a wager under the tag regime',
             'Open (priced)'],
            ['\u201cI\u2019m God limiting myself\u201d is '
             'self-undermining',
             'The identity claim graded as practice-internal '
             '(Level-3/5 pragmatic fiction), not metaphysical '
             'description',
             'Wounded'],
            ['Divine hiddenness',
             'The privation register\u2019s objective vocabulary; no '
             'theodicy claimed',
             'Open'],
            ['Wasted time: redundancy across the corpus',
             'The corpus map with completion markers; the '
             'consolidation\u2019s cut list; this edition\u2019s '
             'additions are all new classes of material',
             'Survives'],
            ['The eliminative program\u2019s constraints are optional',
             'The constraints are stated as the price of the program, '
             'not as theorems',
             'Wounded'],
            ['Pure circularity is incoherent as ultimate',
             'Grounded circularity as structural principle, scoped to '
             'the appearance',
             'Wounded'],
            ['The decombination model is borrowed mathematics',
             'Formalism portability adjudicated: borrowed mathematics '
             'earns nothing until a discriminating prediction '
             'survives \u2014 now with instruments to try',
             'Elevated'],
            ['The model\u2019s candidate subjects are structural, not '
             'experiential',
             'The subject-of-ignorance seam carried openly; the '
             'appearance-relation locates perspectives without '
             'dissolving them',
             'Open'],
            ['*Opposite findings both counted as confirmation (the '
             'Hubble-tension double-count)',
             'Purged from the ledger; the double-counting rule '
             'adopted; both items re-graded Empirical-Unverified '
             'environment facts',
             'Wounded (repaired)'],
            ['*The avatar-necessity proof contradicts the premise of '
             'complete consciousness',
             'Demoted to Level-3 stories; the two-level split carries '
             'the defensible entailment; the three options priced',
             'Wounded (repaired)'],
            ['*The anesthesia predictions contradict each other',
             'The fork stated and priced (chapter 8.2); written into '
             'the domain\u2019s failure conditions',
             'Open (stated)'],
            ['*Uniqueness of the ground is undemonstrated',
             'Admitted per the critiques\u2019 rubric; an '
             'individuation argument is listed as open',
             'Open'],
            ['*The consolidated framework is unfalsifiable metaphysics '
             'plus relabeling',
             'The core is held as a priced interpretation; the '
             'program is anchored with failure conditions and can '
             'now be run; the scaffold and the laboratory are '
             'separated',
             'Elevated (program) / Open (metaphysics)'],
            ['*The corpus cannot police its own claims without '
             'external audit',
             'The tag regime, the provenance register, and the '
             'pre-registration discipline are internalized policing '
             '\u2014 adopted from the external audit that proved the '
             'point',
             'Wounded (repaired)'],
        ],
        [0.34, 0.44, 0.22])

    # ==================== 13. THE EMPIRICAL ANNEX ====================
    L.h1(story, '13. The Empirical Annex: The Anchored Program')

    L.body(story,
           'The annex of the prior editions carried two programs: the '
           'wager on a rival\u2019s physics (the Valentini '
           'non-equilibrium probe) and the decombination program built '
           'from ontologically neutral mathematics. Both carry forward '
           'with their statuses unchanged \u2014 the first '
           'Empirical-Unverified by its own nature, the second now '
           'anchored per Table 4.1. What the annex gains in this '
           'edition is the governing discipline stated as doctrine, '
           'and the run order. The discipline: the annex reports runs, '
           'not rhetoric; every run is pre-registered against a stated '
           'failure condition; equivalence results are reported as '
           'neutral; and no result is mapped onto the framework '
           'without carrying the Interpretive-Mapping tag. The run '
           'order follows instrument readiness: first the ketamine '
           'pipeline (the instrument is complete and the data open); '
           'then the anesthesia corpora (the instrument family is '
           'shared); then the split-brain analysis code over the '
           'request-only patient data; then the DID track through the '
           'reported-statistics route, since raw data remains closed. '
           'The DID domain\u2019s assembled anchors make it the '
           'program\u2019s strongest explanatory target even as its '
           'data pathway is the weakest \u2014 a tension the annex '
           'states rather than resolves.')

    L.body(story,
           'The annex also records what the anchors cannot be made to '
           'do, because the transcript\u2019s history shows the '
           'temptation is systematic. The Santander criticality '
           'result cannot be announced as confirmation of the '
           'threshold structure until the threshold reading survives '
           'the full patient series. The caudate-switching finding '
           'cannot be announced as the switching mechanism until '
           'individual-level dynamics discriminate the coupled-'
           'bistable, winner-take-all, and graded-mixture readings. '
           'The complexity pipeline cannot be announced as validating '
           'the partition criterion until it runs without the '
           'artifact confounds it is designed to expose. Each of '
           'these would be exactly the retrofit pattern the Claude '
           'audit documented \u2014 result first, mapping after \u2014 '
           'and each is therefore written here as a barred move '
           'before any result exists. The annex\u2019s first '
           'pre-registered run, whenever it occurs, is the program\u2019s '
           'first opportunity to fail honestly, which is the only '
           'credential a research program cannot grant itself.')

    L.h2(story, '13.1 The rivals at the anchored position')

    L.data_table(
        story,
        'Table 13.1. Comparative context: the anchored verdict against '
        'the rival family, one line per rival.',
        ['Rival', 'Where the anchored verdict differs'],
        [
            ['Physicalism (mainstream)',
             'Agrees on all anchor findings and on equivalence; '
             'differs on the intrinsic-nature question, where the '
             'corpus claims explanatory virtues and concedes no '
             'evidence \u2014 the honest ledger carried since the '
             'first edition'],
            ['Classical theism',
             'Agrees on the non-derivative ground (the critiques\u2019 '
             'conditional core); differs on the property extensions '
             '(intellect, will, omniscience, omnipotence, goodness), '
             'which the rubric grades as undemonstrated by the core '
             'argument'],
            ['Radical non-dualism (Advaita)',
             'Agrees on appearance-relation and modal honesty; '
             'differs by carrying the locus-of-ignorance problem as '
             'an open seam rather than resolving it by maya\u2019s '
             'indeterminacy'],
            ['Analytic idealism (Kastrup)',
             'Agrees on dissociation as the model of the many; '
             'differs by requiring a formal partition specification '
             'with failure conditions rather than metaphorical '
             'dissociation'],
            ['Dual-aspect / neutral monism',
             'Agrees on the two-language discipline; differs by '
             'refusing any second aspect \u2014 the appearance is of '
             'the one reality, not beside it'],
        ],
        [0.26, 0.74])

    # ==================== 14. GLOSSARY AND LANGUAGE KEY ====================
    L.h1(story, '14. Glossary and Language Key')

    L.body(story,
           'The glossary carries the collision fixes of repair R23. '
           'Each entry names the term, its scoped meaning, and the '
           'status tag it carries in consolidated statements; the '
           'aliases preserve the transcript\u2019s own vocabulary for '
           'citation purposes. The language key converts the audit\u2019s '
           'recommended substitutions into binding rules.')

    L.data_table(
        story,
        'Table 14.1. Glossary: scoped entries for the collision terms.',
        ['Term', 'Scoped meaning', 'Alias / re-grade'],
        [
            ['Singularity (ontological)',
             'The ground: the non-composite, timeless conscious '
             'primitive the credo names the Absolute',
             'Transcript\u2019s \u201cthe Singularity\u201d; Premise-tier '
             'vocabulary'],
            ['singularity (physical)',
             'Where a physical theory breaks down \u2014 a boundary of '
             'the description, never a description of the ground',
             'Re-graded: the two senses may never be equivocated; '
             'holographic-pixel talk about singularities is '
             'Speculation'],
            ['Logos',
             'The ordering structure of the appearance \u2014 the '
             'appearance-level face of the ground\u2019s '
             'intelligibility, not the ground itself',
             'Re-graded under the two-level split: the zero-qualia '
             'structure reading applies here, not to the Absolute'],
            ['Holistic covariance',
             'The framework\u2019s own wide thesis: all apparent '
             'causation is correlation grounded in the one reality',
             'Replaces \u201csuperdeterminism\u201d for the wide claim; '
             'carries the fine-tuning and measure costs openly'],
            ['Superdeterminism (narrow)',
             'The physics term: hidden variables correlated with '
             'measurement settings \u2014 one Bell horn among three',
             'Reserved for the narrow denial only; the transcript\u2019s '
             'wide usage is re-labeled holistic covariance'],
            ['Ontological grounding',
             'Structural depth without temporal ordering: A grounds B '
             'when B is possible only through A',
             'The scoped sense of the transcript\u2019s '
             '\u201ctopological priority\u201d; alias retained for '
             'citation'],
            ['Appearance-relation',
             'The single bridge relation: the world is the appearance '
             'of the Absolute \u2014 one reality appearing',
             'Binding in doctrine; projection/rendering/creation '
             'vocabulary barred outside labeled pedagogical asides'],
            ['Partition (decombination)',
             'A bounded horizon of appearing with its own processing '
             'signature \u2014 the program\u2019s research object',
             'S1\u2013S4 specification; anchor findings tagged '
             'Empirical-Verified, readings tagged Interpretive '
             'Mapping'],
            ['Avatar / finite perspective',
             'A locus of the appearing; a mode of the Absolute\u2019s '
             'self-knowledge, not a fragment of it',
             'Avatar-necessity narratives are Level-3 stories, barred '
             'from doctrine'],
            ['Privation register',
             'Defect as absence, objectively stated: the vocabulary '
             'for evil that does not justify it',
             'Description, never theodicy; the bar on justifying '
             'actual suffering is binding'],
        ],
        [0.20, 0.44, 0.36])

    L.data_table(
        story,
        'Table 14.2. The language key: binding substitutions in '
        'doctrinal statements.',
        ['Barred formulation', 'Binding formulation'],
        [
            ['\u201cGod projects / renders / creates the universe\u201d',
             '\u201cThe universe is the appearance of God\u201d'],
            ['\u201cThe world emerges from consciousness\u201d',
             '\u201cThe world is grounded in consciousness\u201d / '
             '\u201cis a coarse description of the one reality\u201d'],
            ['\u201cBefore the dream / after creation\u201d',
             '\u201cGrounded in the Absolute\u201d (no temporal '
             'ordering)'],
            ['\u201cGod dreams / simulates / computes\u201d',
             'Dropped from doctrine; permitted only in labeled '
             'pedagogical asides'],
            ['\u201cProves / smoking gun / ultimate validation\u201d '
             '(for equivalence or mapping results)',
             'The result\u2019s status tag, stated: \u201cis neutral '
             'for the framework\u201d / \u201cis an interpretive '
             'mapping\u201d'],
            ['\u201cConsciousness is the unbroken symmetry\u201d (as '
             'a result)',
             '\u201cAn interpretive metaphor: consciousness as the '
             'invariant ground\u201d'],
        ],
        [0.46, 0.54])

    # ==================== APPENDIX A ====================
    L.h1(story, 'Appendix A. The Corpus Map and Completion Markers')

    L.data_table(
        story,
        'Table A.1. The corpus at twelve auditing parties, with the '
        'empirical source set and completion markers.',
        ['Party / source', 'What it audited or supplied',
         'Completion marker'],
        [
            ['First-edition audit (docx lineage)',
             'The 130-turn GLM dialogue, line level', 'Delivered; '
             'superseded by later editions'],
            ['Second-edition audit (PDF lineage)',
             'The dialogue plus the first external exchanges',
             'Delivered; page-13 correction applied'],
            ['The Dream That Must Be (critique and v2 trilogy '
             'editions)',
             'The Qwen trilogy, line level, arc-test corrected',
             'Delivered; arc-test codified'],
            ['The FEP-inversion critique',
             'The final-act formalization of conversation two',
             'Delivered; Bite 1 standing'],
            ['Steelman Audit and Consolidation (38 pp)',
             'The dialogue under the full steelman method',
             'Delivered'],
            ['Revised Edition (third)',
             'The corpus with the first DeepSeek exchange recovered',
             'Delivered'],
            ['Strengthened Edition (fourth)',
             'The corpus at ten parties with the decombination '
             'formalization', 'Delivered'],
            ['DeepSeek exchange one (ei9y81lsr98ujftn91, 53 turns)',
             'The universal-consciousness audit line',
             'Recovered from damaged payload; message 64 response '
             'unrecoverable server-side'],
            ['DeepSeek exchange two (d56jfcwyyw3flhzrt1, 88 turns)',
             'The eliminative program and the S1\u2013S4 '
             'specification', 'Read to verified ending'],
            ['DeepSeek exchange three (r9nkpwqs4uu5h169uf, 3 turns)',
             'The hard-problem taxonomy; the decombination.txt and '
             'elevation-cost.txt attachments',
             'Read to verified ending; both attachments read in full '
             'from the file service'],
            ['The two exported critique files (party twelve)',
             'The contingency argument\u2019s two drafts',
             'Read verbatim this round; recorded as sources '
             '(chapter 7)'],
            ['The external Claude audit (party eleven)',
             'The 130-turn dialogue, adversarial, line-referenced',
             'Read line by line; every load-bearing citation '
             'verified; adjudicated (chapter 6)'],
            ['Empirical source set',
             'Santander et al. 2025; Modesti et al. 2022; Schlumpf '
             'et al. 2013; Reinders et al. 2019; Farnes et al. 2020 '
             'with the Reynante toolkit',
             'All read in full from the supplied PDFs and archive; '
             'anchors consolidated (chapters 4\u20135)'],
        ],
        [0.30, 0.40, 0.30])

    L.body(story,
           'The map closes the round\u2019s accounting. Two dialogue '
           'lines, four external exchanges, one embedded audit, one '
           'consolidation treatise, seven editions of this audit '
           'lineage, one adversarial external audit, two exported '
           'critique files, and five empirical sources: every item is '
           'either read to a completion marker or marked with the '
           'precise reason it cannot be. The two items the corpus '
           'will never possess are recorded rather than forgotten \u2014 '
           'the unrecoverable response of the first exchange\u2019s '
           'message 64, and the closed raw data of the split-brain '
           'and DID domains \u2014 and the two items this round '
           'recovered from silence are now permanent parties: the '
           'audit that attacked the framework from outside, and the '
           'critique pair that attacked its theological culmination '
           'from within. The corpus ends the round larger, better '
           'policed, and empirically anchored \u2014 which is what '
           'the steelman-strengthen-elevate-anchor mandate required, '
           'and what the next edition inherits.')
