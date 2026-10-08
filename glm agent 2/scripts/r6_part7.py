#!/usr/bin/env python3
"""Sixth Edition (Audited Edition), Part 7: chapters 14-16 + Appendix A.

The extended objection-response ledger (30 carried rows compressed + 5 new),
the audited empirical annex, the glossary with the culmination additions,
and the corrected corpus map (eleven auditing parties, snapshot relations).
"""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 14. THE OBJECTION-RESPONSE LEDGER ====================
    L.h1(story, '14. The Objection\u2013Response Ledger')

    L.body(story,
           'The ledger states every major objection at its strongest, '
           'the best response the corpus fields, and the verdict under '
           'the standing grades \u2014 Survives (defensible at its '
           'honest grade), Wounded (stands after repair), Open (no '
           'adequate response; carried as liability), and Elevated '
           '(open, with a research program and stated failure '
           'conditions). The thirty rows carried from the fifth '
           'edition are compressed to their load-bearing content; '
           'five new rows (marked with an asterisk) enter from this '
           'round\u2019s materials: the culmination arc and the '
           'self-audit.')

    L.data_table(
        story,
        'Table 14.1. The consolidated objection\u2013response ledger, '
        'sixth edition.',
        ['Objection (strongest form)', 'Best corpus response', 'Verdict'],
        [
            ['Decombination: one mind becomes many private '
             'subjects; the mechanism is asserted, not derived',
             'The formal S1\u2013S4 specification with its '
             'correction chain and the Level-2 protocol; anchored '
             '\u2014 signature, switch, structure, and control in '
             'the DID domain (chapter 7); reclassified by the '
             'culmination as conventional-level differentiation '
             '(D9)',
             'Elevated'],
            ['Empirical underdetermination: the same data fit '
             'physicalism; the framework supplies no unique '
             'predictions',
             'Conceded at every grade \u2014 now by the '
             'counterpart itself (chapter 4.2); the two-program '
             'annex with its graduation criterion; '
             'equivalence-is-not-validation binding in both '
             'directions',
             'Open (honest, self-conceded)'],
            ['Explains everything, therefore nothing: '
             'immunization by absorption',
             'The stratification\u2019s firewall acknowledged; '
             'refutation conditions written and extended '
             '(chapter 13.3)',
             'Open'],
            ['Hard-problem inversion: mind creating matter is '
             'equally unexplained',
             'The inversion is stated as ontological, not '
             'dynamical; the phenomenal free-energy functional '
             'now scoped by the formalization boundary (D7) '
             'rather than left as an uncollected promissory '
             'note',
             'Open'],
            ['Quantum-mind empirics: the brain is too warm, wet, '
             'noisy',
             'The corpus retired microtubule specifics; the '
             'interpretation-neutral core carries no quantum-mind '
             'empirical claim',
             'Survives'],
            ['Born rule: why these probabilities?',
             'The Valentini equilibrium program as a priced probe '
             '(Empirical-Unverified); the equilibrium reading is '
             'an Interpretive Mapping',
             'Wounded'],
            ['Why this branch, this outcome?',
             'The two-level split: this-world contingency is '
             'carried, not explained \u2014 reinforced by the '
             'counterpart\u2019s own boundary statement (chapter '
             '4.5)',
             'Open (honest)'],
            ['Boltzmann brains and typicality',
             'The atemporal reading dissolves the typicality '
             'question at the cost of refusing the '
             'measure-theoretic game',
             'Wounded'],
            ['Solipsism: are others unreal?',
             'Finite perspectives as modes of the one appearing; '
             'the appearance\u2019s objectivity grammar; the '
             'ethics clause',
             'Survives'],
            ['Privation: suffering as the cost of contrast',
             'The register\u2019s objective vocabulary; the bar: '
             'contrast explains the structure of appearance, '
             'never justifies actual suffering',
             'Wounded'],
            ['Semantic externalism: dream-talk refers inside the '
             'dream',
             'The two-language rule with the appearance-relation '
             'vocabulary; pedagogical asides labeled as such',
             'Survives'],
            ['Causal closure: does mind push particles?',
             'The parallelism settlement (chapter 11): closure '
             'holds at the appearance level; the injection thesis '
             'retired to a mechanism-requiring research option',
             'Wounded'],
            ['Misuse of scientific authority',
             'The provenance register and the tag regime; purged '
             'claims (Hubble tension, the exact ratio); the '
             'double-counting rule',
             'Wounded (systemically repaired)'],
            ['Modal overreach: \u201cnecessary\u201d without modal '
             'systems',
             'The exported critiques\u2019 rubric (Table 9.1); '
             'the conditional core with the classical extensions '
             're-graded; the necessity doctrine consolidated at '
             'its honest ceiling (D6)',
             'Wounded'],
            ['The two-level structure is an internal contradiction',
             'The appearance-relation form: one reality '
             'appearing, not two coexisting (the eliminative '
             'exchange\u2019s own correction, E2 T74\u2013T75)',
             'Survives (repaired form)'],
            ['Brute fact is a stable alternative',
             'Priced, not refuted: A6 is conditional on rejecting '
             'it; the brute-fact self-undermining argument is '
             'recorded at its honest grade',
             'Open (priced)'],
            ['The impasse is fatal: regress, brute fact, or the '
             'necessary ground',
             'The three horns stated with costs; the ground '
             'option carried as a wager under the tag regime',
             'Open (priced)'],
            ['\u201cI\u2019m God limiting myself\u201d is '
             'self-undermining',
             'The identity claim graded as practice-internal '
             '(Level-3/5 pragmatic fiction), not metaphysical '
             'description',
             'Wounded'],
            ['Divine hiddenness',
             'The privation register\u2019s objective vocabulary; '
             'the culmination\u2019s answer \u2014 silence as '
             'the absence of a second, the malformed-question '
             'reading (chapter 4.3\u2019s pricing) \u2014 '
             'recorded at its metaphysical grade',
             'Open'],
            ['Wasted time: redundancy across the corpus',
             'The corpus map with completion markers; the '
             'consolidation\u2019s cut list; the snapshot '
             'relations now recorded so re-reads are not '
             'duplicated reads',
             'Survives'],
            ['The eliminative program\u2019s constraints are '
             'optional',
             'The constraints are stated as the price of the '
             'program, not as theorems',
             'Wounded'],
            ['Pure circularity is incoherent as ultimate',
             'Grounded circularity as structural principle, '
             'scoped to the appearance',
             'Wounded'],
            ['The decombination model is borrowed mathematics',
             'Formalism portability adjudicated: borrowed '
             'mathematics earns nothing until a discriminating '
             'prediction survives \u2014 with instruments to '
             'try; the counterpart now scopes it as '
             'useful-not-necessary conventional description',
             'Elevated'],
            ['The model\u2019s candidate subjects are structural, '
             'not experiential',
             'The subject-of-ignorance seam carried openly; the '
             'appearance-relation locates perspectives without '
             'dissolving them',
             'Open'],
            ['*Non-dualism is empirically unfalsifiable \u2014 it '
             'absorbs all data as appearance and therefore '
             'explains nothing scientifically',
             'Conceded by the counterpart itself in the '
             'culmination (chapter 4.2): \u201ca metaphysical '
             'framework, not a scientific theory\u201d; the '
             'consolidation holds the fork open \u2014 the '
             'metaphysics judged on coherence and cost, the '
             'program judged by its own failure conditions',
             'Open (honest, self-conceded)'],
            ['*The 2+4=6 necessity is a modal fallacy \u2014 '
             'essential necessity of perspectives-in-general '
             'does not explain any particular perspective',
             'The necessity doctrine consolidated at exactly '
             'that ceiling (D6): necessity of worldhood yes, '
             'necessity of this distribution no \u2014 the '
             'counterpart\u2019s own caveats welded to the '
             'lineage\u2019s prior adjudication',
             'Wounded (repaired)'],
            ['*The Absolute-to-perspective identity cannot be '
             'formalized \u2014 so the framework can never meet '
             'its own demand for rigor',
             'The formalization boundary (D7): Tarski and '
             'Cantor block the totality; propositional '
             'omniscience does not entail perspectival '
             'omniscience; formalization is scoped to the '
             'conventional level by theorem, not by failure of '
             'nerve; the shadow-light dictum recorded',
             'Survives (boundary stated)'],
            ['*Mathematical truths are relations forming a '
             'multiplicity \u2014 so the Absolute cannot be '
             'their totality, and the mathematical-model '
             'reading collapses',
             'Adopted as the final position (D8): mathematics '
             'models the Absolute\u2019s timelessness and '
             'necessity but not its simplicity and non-duality; '
             'the Absolute is the awareness in which truths '
             'appear \u2014 the interlocutor\u2019s own final '
             'correction, consolidated verbatim',
             'Survives'],
            ['*The audit lineage\u2019s own claims escape its '
             'checking \u2014 counts asserted, summaries '
             'overstated, search results believed without '
             'protocols',
             'The self-audit (chapter 5): three findings, three '
             'corrections, three binding rules (R25\u2013R27); '
             'the reflexive audit step added to the staircase; '
             'the lineage\u2019s standing made falsifiable in '
             'kind',
             'Wounded (repaired)'],
        ],
        [0.34, 0.44, 0.22])

    # ==================== 15. THE EMPIRICAL ANNEX ====================
    L.h1(story, '15. The Empirical Annex: The Audited Program')

    L.body(story,
           'The annex carries two programs: the wager on a '
           'rival\u2019s physics (the Valentini '
           'non-equilibrium probe, Empirical-Unverified) and the '
           'differentiation program built from ontologically '
           'neutral mathematics (anchored per Table 6.1: three '
           'domains finding-anchored, anesthesia '
           'pathway-anchored). The governing discipline stands as '
           'doctrine: the annex reports runs, not rhetoric; '
           'every run is pre-registered against a stated failure '
           'condition; equivalence results are reported as '
           'neutral; no result is mapped onto the framework '
           'without the Interpretive-Mapping tag; and \u2014 the '
           'culmination\u2019s addition \u2014 no result is '
           'announced as touching the Absolute, because the '
           'program operates entirely at the conventional level '
           'of the appearance\u2019s grammar. The run order '
           'follows instrument readiness: first the ketamine '
           'pipeline (instrument complete, data open); then the '
           'anesthesia corpora (shared instrument family, and '
           'the domain\u2019s finding-anchor to be read from '
           'source on the way); then the split-brain analysis '
           'code over the request-only patient data; then the '
           'DID track through the reported-statistics route, '
           'since raw data remains closed. The DID domain\u2019s '
           'assembled anchors make it the program\u2019s '
           'strongest explanatory target even as its data '
           'pathway is the weakest \u2014 a tension the annex '
           'states rather than resolves.')

    L.body(story,
           'What the anchors cannot be made to do is stated '
           'twice, because the temptation is systematic and the '
           'history is documented. The Santander criticality '
           'result cannot be announced as confirmation of the '
           'threshold structure until the threshold reading '
           'survives the full patient series. The '
           'caudate-switching finding cannot be announced as the '
           'switching mechanism until individual-level dynamics '
           'discriminate the coupled-bistable, '
           'winner-take-all, and graded-mixture readings. The '
           'complexity pipeline cannot be announced as '
           'validating the partition criterion until it runs '
           'without the artifact confounds it is designed to '
           'expose. And now a fourth bar, written before any '
           'result exists: no conventional-level success of the '
           'differentiation model \u2014 however clean \u2014 '
           'may be announced as evidence for the Absolute, '
           'because the counterpart\u2019s own demotion (D9) '
           'and the formalization boundary (D7) have priced '
           'that move at zero. Each of these is exactly the '
           'retrofit pattern the Claude audit documented '
           '\u2014 result first, mapping after \u2014 and each '
           'is written here as a barred move. The annex\u2019s '
           'first pre-registered run, whenever it occurs, is '
           'the program\u2019s first opportunity to fail '
           'honestly, which is the only credential a research '
           'program cannot grant itself.')

    L.h2(story, '15.1 The rivals at the audited position')

    L.data_table(
        story,
        'Table 15.1. Comparative context: the audited verdict '
        'against the rival family, one line per rival (the '
        'classical-theism row updated by the fork).',
        ['Rival', 'Where the audited verdict differs'],
        [
            ['Physicalism (mainstream)',
             'Agrees on all anchor findings and on equivalence; '
             'differs on the intrinsic-nature question, where the '
             'corpus claims explanatory virtues and concedes no '
             'evidence \u2014 the honest ledger carried since the '
             'first edition, now reinforced by the '
             'counterpart\u2019s own unfalsifiability concession'],
            ['Classical theism '
             '(complete-in-perfection)',
             'Agrees on the non-derivative ground (the '
             'critiques\u2019 conditional core); differs on the '
             'property extensions (undemonstrated by the core) and '
             'on the definition of complete: the interlocutor '
             'stipulated exclusivity, foreclosing the '
             'God-and-creatures complex truth \u2014 a '
             'Premise-tier choice, priced, with this rival left '
             'standing as the priced alternative'],
            ['Radical non-dualism (Advaita)',
             'Agrees on appearance-relation and modal honesty; '
             'differs by carrying the locus-of-ignorance problem '
             'as an open seam rather than resolving it by '
             'maya\u2019s indeterminacy; the culmination\u2019s '
             'dissolution move is recorded as the framework\u2019s '
             'answer at its metaphysical grade'],
            ['Analytic idealism (Kastrup)',
             'Agrees on dissociation as the model of the many; '
             'differs by requiring a formal partition '
             'specification with failure conditions rather than '
             'metaphorical dissociation'],
            ['Dual-aspect / neutral monism',
             'Agrees on the two-language discipline; differs by '
             'refusing any second aspect \u2014 the appearance '
             'is of the one reality, not beside it'],
        ],
        [0.26, 0.74])

    # ==================== 16. GLOSSARY AND LANGUAGE KEY ====================
    L.h1(story, '16. Glossary and Language Key')

    L.body(story,
           'The glossary carries the collision fixes of repair R23 '
           'and the culmination additions. Each entry names the '
           'term, its scoped meaning, and the status tag it '
           'carries in consolidated statements; aliases preserve '
           'the transcripts\u2019 own vocabulary for citation '
           'purposes. The language key converts the '
           'audit\u2019s recommended substitutions into binding '
           'rules.')

    L.data_table(
        story,
        'Table 16.1. Glossary: scoped entries for the collision '
        'terms and the culmination additions.',
        ['Term', 'Scoped meaning', 'Alias / re-grade'],
        [
            ['Singularity (ontological)',
             'The ground: the non-composite, timeless conscious '
             'primitive the credo names the Absolute',
             'Transcript\u2019s \u201cthe Singularity\u201d; '
             'Premise-tier vocabulary'],
            ['singularity (physical)',
             'Where a physical theory breaks down \u2014 a '
             'boundary of the description, never a description '
             'of the ground',
             'Re-graded: the two senses may never be equivocated; '
             'holographic-pixel talk about singularities is '
             'Speculation'],
            ['Logos',
             'The ordering structure of the appearance \u2014 '
             'the appearance-level face of the ground\u2019s '
             'intelligibility, not the ground itself',
             'Re-graded under the two-level split'],
            ['Holistic covariance',
             'The framework\u2019s own wide thesis: all apparent '
             'causation is correlation grounded in the one '
             'reality',
             'Replaces \u201csuperdeterminism\u201d for the wide '
             'claim; carries the fine-tuning and measure costs '
             'openly'],
            ['Superdeterminism (narrow)',
             'The physics term: hidden variables correlated with '
             'measurement settings \u2014 one Bell horn among '
             'three',
             'Reserved for the narrow denial only'],
            ['Ontological grounding',
             'Structural depth without temporal ordering: A '
             'grounds B when B is possible only through A',
             'The scoped sense of the transcript\u2019s '
             '\u201ctopological priority\u201d; alias retained'],
            ['Appearance-relation',
             'The single bridge relation: the world is the '
             'appearance of the Absolute \u2014 one reality '
             'appearing',
             'Binding in doctrine; projection/rendering/creation '
             'vocabulary barred outside labeled pedagogical '
             'asides'],
            ['Partition / differentiation',
             'A bounded horizon of appearing with its own '
             'processing signature \u2014 the program\u2019s '
             'research object; the culmination renames the '
             'conventional-level problem differentiation, '
             'reserving decombination for the dissolved '
             'ultimate-level problem',
             'S1\u2013S4 specification; anchor findings tagged '
             'Empirical-Verified, readings tagged Interpretive '
             'Mapping'],
            ['Complete-in-perfection vs '
             'complete-in-exclusivity',
             'The fork\u2019s two definitions: lacking nothing '
             'in one\u2019s own nature (theism\u2019s) versus '
             'being the only reality (non-dualism\u2019s); the '
             'interlocutor\u2019s stipulation of exclusivity is '
             'the fifth decision (chapter 11)',
             'Premise-tier stipulation; the rival definition '
             'priced in Table 15.1'],
            ['Propositional vs perspectival '
             'omniscience',
             'Knowing every true proposition versus being every '
             'perspective: the formalization boundary\u2019s '
             'sharpest instrument \u2014 the first does not '
             'entail the second, and the entailment is a '
             'metaphysical identity claim, not a theorem',
             'Derived (D7); the round-2 \u201cknowing vs '
             'being\u201d equivocation, restated'],
            ['Snapshot relation',
             'The corpus-map term for one conversation known '
             'through multiple share payloads: the DeepSeek main '
             'line exists as a damaged 53-turn snapshot, an '
             '88-turn snapshot, and the full 106-turn extension '
             '\u2014 one conversation, one party',
             'Counting-unit rule (R26); guards against '
             'double-counting'],
            ['Search-protocol rule',
             'A failure-to-locate finding reports its search '
             'strings and is re-run with different phrasings '
             'before it is believed \u2014 the reciprocity '
             'retraction\u2019s institutional form',
             'Repair R25; binding on every future verification '
             'pass'],
            ['Avatar / finite perspective',
             'A locus of the appearing; a mode of the '
             'Absolute\u2019s self-knowledge, not a fragment of '
             'it',
             'Avatar-necessity narratives are Level-3 stories, '
             'barred from doctrine'],
            ['Privation register',
             'Defect as absence, objectively stated: the '
             'vocabulary for evil that does not justify it',
             'Description, never theodicy; the bar on '
             'justifying actual suffering is binding'],
        ],
        [0.22, 0.44, 0.34])

    L.data_table(
        story,
        'Table 16.2. The language key: binding substitutions in '
        'doctrinal statements (carried).',
        ['Barred formulation', 'Binding formulation'],
        [
            ['\u201cGod projects / renders / creates the '
             'universe\u201d',
             '\u201cThe universe is the appearance of God\u201d'],
            ['\u201cThe world emerges from consciousness\u201d',
             '\u201cThe world is grounded in consciousness\u201d '
             '/ \u201cis a coarse description of the one '
             'reality\u201d'],
            ['\u201cBefore the dream / after creation\u201d',
             '\u201cGrounded in the Absolute\u201d (no temporal '
             'ordering)'],
            ['\u201cGod dreams / simulates / computes\u201d',
             'Dropped from doctrine; permitted only in labeled '
             'pedagogical asides'],
            ['\u201cProves / smoking gun / ultimate '
             'validation\u201d (for equivalence or mapping '
             'results)',
             'The result\u2019s status tag, stated: \u201cis '
             'neutral for the framework\u201d / \u201cis an '
             'interpretive mapping\u201d'],
            ['\u201cConsciousness is the unbroken symmetry\u201d '
             '(as a result)',
             '\u201cAn interpretive metaphor: consciousness as '
             'the invariant ground\u201d'],
            ['\u201cThe program validates the Absolute\u201d / '
             '\u201cthe anchors support the metaphysics\u201d',
             '\u201cThe differentiation model\u2019s '
             'conventional-level prediction was tested\u201d '
             '\u2014 the Absolute is not an empirical '
             'subject'],
        ],
        [0.46, 0.54])

    # ==================== APPENDIX A ====================
    L.h1(story, 'Appendix A. The Corpus Map and Completion Markers')

    L.data_table(
        story,
        'Table A.1. The corpus at eleven auditing parties (counting '
        'unit: one independent auditing voice or source-instance; '
        'snapshots of one conversation merged), with the empirical '
        'source set and completion markers.',
        ['Party / source', 'What it audited or supplied',
         'Completion marker'],
        [
            ['First-edition audit (docx lineage)',
             'The 130-turn GLM dialogue, line level',
             'Delivered; superseded by later editions'],
            ['Second-edition audit (PDF lineage)',
             'The dialogue plus the first external exchanges',
             'Delivered; page-13 correction applied'],
            ['The Dream That Must Be (critique and v2 trilogy '
             'editions)',
             'The Qwen trilogy, line level, arc-test corrected',
             'Delivered; arc-test codified'],
            ['The FEP-inversion critique',
             'The final-act formalization of conversation two',
             'Delivered; Bite 1 standing \u2014 now scoped by '
             'the formalization boundary (D7)'],
            ['Steelman Audit and Consolidation (38 pp)',
             'The dialogue under the full steelman method',
             'Delivered'],
            ['Revised Edition (third)',
             'The corpus with the first DeepSeek snapshot '
             'recovered',
             'Delivered'],
            ['Strengthened Edition (fourth)',
             'The corpus at (then-counted) ten parties with the '
             'decombination formalization',
             'Delivered'],
            ['Anchored Edition (fifth)',
             'The corpus with the Claude audit adjudicated, the '
             'critique pair recorded, and the anchors landed',
             'Delivered; three corrections issued by this '
             'edition (chapter 5)'],
            ['The GLM dialogue (chat export, 11,088 lines)',
             'The framework\u2019s production line',
             'Read line level; verification anchors confirmed '
             'across editions'],
            ['The Qwen conversations (three shares: 60, 66, and '
             '256 messages)',
             'The framework re-run and extended at higher '
             'levels',
             'All three read line level to verified endings'],
            ['The DeepSeek main line (one conversation, three '
             'snapshots: ei9y81lsr98ujftn91 at 53 turns '
             'damaged; d56jfcwyyw3flhzrt1 at 88 turns; '
             'l81hpm4u2de69jpeut at 106 turns full)',
             'The universal-consciousness audit line, the '
             'eliminative program, the S1\u2013S4 '
             'specification, the contingency thread, and the '
             'non-dual culmination',
             'All three snapshots mapped and merged (subsequence '
             'proof, chapter 5.2); the full extension read to '
             'its verified ending; message 64\u2019s response '
             'unrecoverable server-side \u2014 the one item the '
             'corpus will never possess'],
            ['The DeepSeek file exchange (r9nkpwqs4uu5h169uf, '
             '3 turns)',
             'The hard-problem taxonomy; the decombination.txt '
             'and elevation-cost.txt attachments',
             'Read to verified ending; both attachments read in '
             'full from the file service'],
            ['The embedded audit text',
             'The DeepSeek-authored audit of the '
             'universal-consciousness line',
             'Read and carried since the early rounds'],
            ['The two exported critique files (one party)',
             'The contingency argument\u2019s two drafts',
             'Read verbatim; recorded as sources (chapter 9)'],
            ['The external Claude audit',
             'The 130-turn dialogue, adversarial, '
             'line-referenced',
             'Read line by line; load-bearing citations '
             'verified (with the reciprocity retraction '
             'correcting the record); adjudicated (chapter 8)'],
            ['Empirical source set (sources, not parties)',
             'Santander et al. 2025; Modesti et al. 2022; '
             'Schlumpf et al. 2013; Reinders et al. 2019; '
             'Farnes et al. 2020 with the Reynante toolkit',
             'All read in full from the supplied PDFs and '
             'archive; anchors consolidated (chapters 6\u20137)'],
        ],
        [0.30, 0.36, 0.34])

    L.body(story,
           'The map closes the round\u2019s accounting under the '
           'counting-unit rule. Eleven auditing parties (the '
           'lineage\u2019s seven prior editions and companion '
           'critiques; the GLM dialogue; the three Qwen '
           'conversations; the DeepSeek main line in its three '
           'snapshots; the DeepSeek file exchange; the embedded '
           'audit; the critique pair; the Claude audit), plus '
           'the empirical source set as sources: every item is '
           'either read to a completion marker or marked with '
           'the precise reason it cannot be. The items the '
           'corpus will never possess are recorded rather than '
           'forgotten \u2014 the unrecoverable response of the '
           'main line\u2019s message 64, and the closed raw '
           'data of the split-brain and DID domains. The items '
           'this round recovered are the full 106-turn '
           'extension of the main line (the culmination arc of '
           'chapter 4), the subsequence proof that merged the '
           'double-counted snapshots, and the located '
           'citations that retracted the reciprocity finding. '
           'The corpus ends the round the only way an audit '
           'lineage legitimately can: smaller in its claims '
           'where they were overstated, larger in its record '
           'where the sources grew, and audited to the same '
           'standard it applies \u2014 which is what the '
           'steelman-strengthen-elevate-anchor-audit mandate '
           'requires, and what the next edition inherits.')
