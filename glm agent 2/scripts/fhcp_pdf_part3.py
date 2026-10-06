#!/usr/bin/env python3
"""Part 3: chapters 7-9 (Objection-Response Ledger, Comparative Context,
Repair Program)."""
import fhcp_pdf_lib as L


def add_content(story):
    # ══════════════ 7. THE OBJECTION-RESPONSE LEDGER ═══════════════════
    L.h1(story, '7. The Objection\u2013Response Ledger')

    L.body(story,
           'This chapter is the audit\'s central deliverable: every major '
           'objection raised against the premise, inside or outside the '
           'dialogue, stated at its strongest (the steelman of the '
           'critic), together with the best response the transcript '
           'actually fields and the audit\'s verdict. The verdict grades '
           'are those of section 1.1: <b>Survives</b> (defensible at its '
           'honest grade), <b>Wounded</b> (stands only after a repair '
           'from chapter 9), <b>Open</b> (no adequate response exists in '
           'the transcript; the consolidation carries the objection as a '
           'standing liability).')

    L.data_table(
        story,
        'Table 7. Objections, strongest forms, responses, and verdicts.',
        ['Objection', 'Strongest form (steelman)', 'Best response in the transcript', 'Lines', 'Verdict'],
        [
            ['Decombination: how does one mind become many private subjects?',
             'Dissociation modeled on clinical DID is a scale-up with no '
             'independent warrant; without a composition/decomposition '
             'law the move relocates the hard problem rather than solving '
             'it \u2014 a cost the framework itself concedes (L3867).',
             'Markov blankets plus free-energy self-organization as the '
             'promised law (L3975\u20133985); the law is named as an '
             'explicit debt in the five requirements (L3879\u20133883).',
             'L2777\u20132792; L3861\u20133867',
             '<b>Open</b> (W2, G1; repair R6 states the wager honestly).'],
            ['Empirical underdetermination: the same data fit physicalism.',
             'A framework that reinterprets every result as confirmation '
             'is insulated, not supported; its three novel predictions '
             'are shared with rival programs or conditional on contested '
             'empirics.',
             'Reinterpretation strategy acknowledged; three novel '
             'predictions offered (classical-AI ceiling, '
             'quantum-computing wall, anesthesia/psychedelic signatures) '
             '(L3869\u20133883; L3931\u20133939).',
             'L3869\u20133883',
             '<b>Wounded</b> (W1, W5, W8; needs R2 + R5 honest ledger).'],
            ['Explains everything, therefore explains nothing.',
             'A structure that cannot lose is not tracking evidence; the '
             'absorption pattern documented at W1 is structural, not '
             'incidental.',
             'Conceded in principle: the framework "does not supply those '
             'equations"; stratification offered as structure, not '
             'mechanism (L1550\u20131563).',
             'L1550\u20131563',
             '<b>Wounded</b> (concession honest; absorption behavior '
             'persists; R1/R2).'],
            ['Hard-problem inversion: mind creating matter is equally '
             'hard.',
             'Inverting the explanatory arrow moves the mystery, it does '
             'not shrink it; both directions face a brute terminus.',
             'Extrinsic-appearance doctrine: matter is what mental '
             'process looks like across a boundary; the brain is the '
             'image of the boundary (L2763\u20132804).',
             'L2763\u20132804',
             '<b>Survives</b> as interpretation at Grade C; rests on the '
             'open law of dissociation (W2).'],
            ['Quantum-mind empirics: the brain is too warm, wet, noisy.',
             'Decoherence-time calculations (Tegmark) rule out sustained '
             'microscopic quantum coherence in neuronal conditions at '
             'known scales; "protected just long enough" is an unfalsifiable '
             'patch unless a mechanism is given.',
             'Decoherence reframed as the reducing valve \u2014 the '
             'signature of the boundary rather than an obstacle to it '
             '(L555\u2013562; L2360\u20132367).',
             'L555\u2013562; L2360\u20132367',
             '<b>Wounded</b> (reframing is circular absent the empirics; '
             'carried as conditional per W6).'],
            ['Born rule: why these probabilities?',
             'Either the probabilities are brute axioms \u2014 no '
             'explanation \u2014 or any explanatory story must be '
             'compatible with every observed frequency, which is '
             'difficult to achieve non-trivially.',
             'Final account: equilibrium of the confined perspective, '
             'with quantum non-equilibrium as the observable signature '
             '(L8937\u20138977; L9988\u201310051).',
             'L8937\u20138977; L9988\u201310051',
             '<b>Survives</b> as Grade B analogy with a falsifiable '
             'edge (chapter 11).'],
            ['Why this branch, this outcome, and not another?',
             'Without a selection story, the one-world appearance is a '
             'stubborn residue of unexplained de facto choice.',
             'Avatar attention narrows the rendered; the equilibrium '
             'distribution carries the weight (L3670\u20133686).',
             'L3670\u20133686',
             '<b>Wounded</b> ("narrative weight" retired; '
             'branch-selection remains open under the equilibrium '
             'story).'],
            ['Boltzmann brains and typicality.',
             'If the arrow is perspectival, ordered observers need a '
             'measure privileging them; otherwise fluctuation-born '
             'observers dominate the space of perspectives.',
             'Perspectival Actualization: observers ride stable '
             'gradients, not fluctuations; the measure is admitted '
             'owed (L1903).',
             'L2669\u20132679; L1903',
             '<b>Wounded</b> (honest hedge; the measure is owed \u2014 '
             'gap G2).'],
            ['Solipsism: if all is one mind, are others unreal?',
             'Monism threatens to collapse other minds into appearance '
             'without independent reality \u2014 an unlivable and '
             'self-undermining consequence.',
             'Layer-4 consensus via Quantum Darwinism: objectivity is '
             'redundant intersubjectivity (L3602\u20133608); "one '
             'ocean, many whirlpools" (L6519\u20136524).',
             'L3602\u20133608; L6519\u20136524',
             '<b>Survives</b> (redundancy mechanism is Grade A; the '
             'reading is modest).'],
            ['Theodicy: suffering as the cost of contrast.',
             'The quantitative and distributional problem of suffering '
             '\u2014 the child\'s terminal illness versus the aesthetic '
             'requirement of contrast \u2014 is not touched by '
             'totality-and-play language; the price is paid by those '
             'who did not negotiate.',
             'Totality requires the nightmare; divine play (Lila) '
             '(L1714\u20131718; L1670\u20131675).',
             'L1714\u20131718',
             '<b>Open</b> (gap G3; R8 strengthens but cannot close).'],
            ['Semantic externalism: dream-talk refers inside the dream.',
             'If the world were a dream, the word "dream" would refer '
             'to things inside it; the skeptic\'s contrast between dream '
             'and reality is undermined from within (Putnam, Chalmers).',
             'Never engaged; the Zhuangzi parable is treated '
             'aesthetically (L7687\u20137777).',
             'L7687\u20137777',
             '<b>Open</b> (W11, R7 adds the engagement; see section '
             '8.6).'],
            ['Causal closure: does mind push particles?',
             'If consciousness is fundamental, either it intervenes in '
             'physical dynamics \u2014 conflicting with closure \u2014 '
             'or it does nothing, and its fundamentality is idle.',
             'Vertical grounding replaces downward causation; physics '
             'stays closed (L9228\u20139278).',
             'L9228\u20139278',
             '<b>Survives</b> as a coherent position; the isomorphism '
             'pipeline cannot test it (W8).'],
            ['Misuse of scientific authority.',
             'Penrose, Hawking, and Valentini are conscripted as '
             'vindications while their own commitments are reversed '
             '(W5) \u2014 misattribution that misleads lay readers.',
             'None in the transcript; each borrowing is presented '
             'unflagged (L2980; L4903; L10664\u201310673).',
             'L2980; L4903; L10664',
             '<b>Wounded</b> (R2 grade labels + no-conscription rule '
             'required).'],
            ['If all is the Absolute\'s appearance, what does the '
             'Absolute explain?',
             'An unmanifest ground beyond mathematics explains nothing '
             'that a brute universe would not, at one more ontological '
             'level.',
             'Topological priority: the boundary entails the bulk; '
             'correlations are entailments, not effects '
             '(L11028\u201311086); parsimony of one substance rather '
             'than two (L7748).',
             'L11028\u201311086; L7748',
             '<b>Survives</b> as the best available answer; honestly '
             'metaphysical (Grade C).'],
            ['Modal overreach: "necessary" claims about God and avatars.',
             'The infinity, mirror, and keystone arguments for the '
             'necessity of avatars carry textbook counters and no '
             'stated modal epistemology (W9, G6).',
             'None; the arguments are announced as proofs at '
             'L9535\u20139604.',
             'L9535\u20139604',
             '<b>Wounded</b> (R9 downgrades them to reasons with '
             'counters named).'],
        ],
        [0.16, 0.28, 0.26, 0.12, 0.18], font_size=8.0, header_font=8.4)

    L.body(story,
           'Read as a whole, the ledger\'s pattern is informative. The '
           'framework survives exactly where its claims are modest '
           '(objectivity-as-consensus, the equilibrium Born rule, the '
           'extrinsic-appearance doctrine) and bleeds exactly where it '
           'overclaims (authority conscription, modal arguments, '
           'absorbed empirics). The two Open rows \u2014 decombination '
           'and theodicy \u2014 are not incidental failures but the two '
           'places where the premise\'s grandeur most outruns its '
           'apparatus. A reader who accepts the consolidated premise '
           'should accept it while looking directly at those two rows.')

    # ══════════════ 8. COMPARATIVE CONTEXT ═════════════════════════════
    L.h1(story, '8. Comparative Context: The Premise among Its Rivals')

    L.body(story,
           'The assistant\'s first reply in the transcript (L5\u201317) '
           'already placed the premise in its lineage: Advaita Vedanta, '
           'Berkeley, Schelling and Hegel, and contemporary analytic '
           'idealism, against the backdrop of classical theism. The '
           'dialogue then ran eleven thousand lines without returning to '
           'that lineage \u2014 a deficiency logged as W11. This chapter '
           'supplies the missing engagement, because a consolidated '
           'premise that cannot locate itself among its rivals does not '
           'yet know what it is arguing for. The comparison below is '
           'thematic: what each tradition takes as fundamental, how it '
           'relates mind to matter, how it answers the hard problem, and '
           'where the audited premise agrees, borrows, or genuinely '
           'innovates.')

    L.h2(story, '8.1 Advaita Vedanta')

    L.body(story,
           'The affinity is the deepest in the set. Advaita\'s Brahman '
           '\u2014 <i>sat-chit-ananda</i>, being-consciousness-bliss, '
           'one without a second, beyond time and space \u2014 is '
           'structurally identical to the dialogue\'s Absolute: '
           'non-dual, non-composite, timeless, with the manifest world '
           'as appearance (<i>maya</i>) rather than creation. The '
           'dialogue\'s final credo ("God did not create a universe. God '
           'is all there is," L9673\u20139675) is Advaita\'s doctrine in '
           'modern idiom, and its corrections C4 and C13 \u2014 banning '
           'creation and composite language \u2014 re-derive '
           'Shankara\'s discipline of speaking of the unqualified '
           'absolute only via negation. Where the dialogue genuinely '
           'departs from classical Advaita is method: it refuses to '
           'rest on scripture or liberatory experience, and instead '
           'runs the doctrine through forty topics of physics \u2014 '
           'decoherence, the Born rule, holographic bounds \u2014 '
           'treating modern physics as the contemporary form of the '
           'question the Upanishads asked. That project is legitimate '
           'but must be stated for what it is: an interpretation of '
           'physics under an Advaita-style premise, not a discovery '
           'that physics implies Advaita. Advaita also owns a mature '
           'theory of levels (<i>vyavahara</i> vs. <i>paramarthika</i>, '
           'conventional vs. absolute truth) that the dialogue\'s '
           'two-language regime reinvents without acknowledging the '
           'precedent \u2014 the consolidation does acknowledge it.')

    L.h2(story, '8.2 Analytic idealism (Kastrup)')

    L.body(story,
           'The nearest contemporary relative. Kastrup\'s analytic '
           'idealism holds that there is one transpersonal mind, that '
           'living beings are dissociated complexes of it, and that the '
           'physical world is the extrinsic appearance of mental '
           'processes \u2014 the same three commitments as the '
           'dialogue\'s premise, argued in the idiom of analytic '
           'philosophy. The dialogue\'s dissociation vocabulary and its '
           'Markov-blanket formalization are recognizably this program '
           '\u2014 indeed the blanket formalization is stronger in '
           'Kastrup\'s own presentations, where dissociation is modeled '
           'on the boundary structure of self-organizing systems rather '
           'than only on clinical analogy. The audit\'s verdict on '
           'decombination (W2, Open) applies to Kastrup\'s program '
           'equally: the law by which the one becomes many is the '
           'shared open problem of the family. The dialogue\'s '
           'distinctive contributions relative to analytic idealism are '
           'two: the stratified ontology, which assigns the quantum '
           'interpretations to different strata instead of choosing '
           'one; and topological priority, which replaces causal talk '
           'at the fundamental level with structural entailment \u2014 '
           'a move analytic idealism has not made.')

    L.h2(story, '8.3 Classical theism (Aquinas, Avicenna, Maimonides)')

    L.body(story,
           'The attribute list in the transcript\'s first line \u2014 '
           'timeless, spaceless, unchanging, omniscient, omnipotent, '
           'perfect, immaterial \u2014 is the God of the philosophers, '
           'arrived at by <i>via negativa</i> and grounded in pure act. '
           'The dialogue keeps the metaphysics and drops the two things '
           'that make classical theism a religion: creation, and '
           'personal relation. Its correction C4 (nothing outside God; '
           'dreaming or creating imply defect) is precisely the point '
           'where it leaves Aquinas: for the Thomist, God\'s act of '
           'creation is not a change in God but a real relation in the '
           'creature, and the world\'s contingency is the datum '
           'creation explains; for the dialogue, creation language is '
           'a defect to be purified away, and the world\'s contingency '
           'is an appearance within the necessary. The dialogue also '
           'inherits classical theism\'s hardest debts without '
           'inheriting its answers: divine simplicity maps onto '
           'non-compositeness (and decombination), and the problem of '
           'evil maps onto W10 \u2014 where the tradition has two '
           'millennia of theodicy and the transcript has an aesthetic '
           'of contrast. The consolidation\'s confession of a moral '
           'remainder (R8) is, in effect, an admission that leaving '
           'classical theism\'s answers behind is a cost, not only a '
           'simplification.')

    L.h2(story, '8.4 Absolute idealism (Schelling, Hegel)')

    L.body(story,
           'The German Idealists supply the dialogue\'s deepest '
           'structural idea without being named for it after the first '
           'reply: the Absolute\'s self-relation requires self-othering '
           '\u2014 finitude is not a fall from the infinite but the '
           'infinite\'s own condition of self-knowledge. The dialogue\'s '
           'mirror argument for avatars (W9) is Schelling\'s intuition '
           'that the absolute cannot know itself without a counterposed '
           'image; its "Grand Dream" phase, in which the world is the '
           'Dreamer\'s necessary self-limitation, is Hegel\'s '
           'self-externalization rehearsed in physics vocabulary. The '
           'cost the Idealists paid \u2014 and the dialogue inherits the '
           'bill \u2014 is the difficulty of saying why self-othering '
           'is necessary rather than merely elegant, and why the '
           'specific shape of this world is entailed rather than '
           'brutely selected. The dialogue\'s answer (topological '
           'priority: the bulk is entailed by the boundary) is more '
           'precise than Hegel\'s dialectical narration, but it pays '
           'for the precision by remaining a name for the relation '
           'rather than a derivation of it (gap G4).')

    L.h2(story, '8.5 Russellian monism, panpsychism, cosmopsychism')

    L.body(story,
           'The nearest cheap rivals \u2014 cheap in the currency of '
           'ontological commitment. They share the framework\'s '
           'diagnosis (physics is silent on intrinsic nature) while '
           'distributing micro-experience to matter\'s intrinsic '
           'properties (Russellian monism, panpsychism) or grounding '
           'experience in a cosmic subject (cosmopsychism), without '
           'asserting that the fundamental is a mind in the full sense. '
           'Russellian monism avoids the decombination problem by '
           'keeping experience at the micro-level \u2014 and instead '
           'inherits the combination problem, its exact mirror '
           '(gap G7): how do micro-experiences sum to a unified '
           'subject? Cosmopsychism is the closest cousin of all \u2014 '
           'a cosmic subject with derivative local subjects \u2014 '
           'and owns the same decombination problem under the name '
           '"decombination" or "subject-collapse." The honest '
           'comparative verdict: the dialogue\'s unity-of-experience '
           'argument (one experiential field is never observed to '
           'aggregate from parts; L7748\'s one-substance parsimony) is '
           'a real reason to prefer the cosmic-subject family over the '
           'micro-experience family, but it is a reason, not a proof, '
           'and the two families\' open problems are symmetric enough '
           'that a rational physicalist may hold neither \u2014 which '
           'is the point of the ledger\'s underdetermination row.')

    L.h2(story, '8.6 The simulation hypothesis and the dream argument')

    L.body(story,
           'The dialogue\'s fifth phase explicitly retires the '
           'simulation framing: "simulation implies computer '
           'involvement, whereas dream points to conscious thought. '
           'however, both terms share a fault, as they both imply '
           'change" (L5307). Its implicit position nevertheless '
           'descends from the Zhuangzi parable it quotes '
           '(L7687\u20137777) and from Descartes\'s dream worry, and '
           'it faces the modern sharpening of both: Chalmers\'s '
           'distinction between the skeptical and the metaphysical '
           'dream hypothesis. The metaphysical form holds that the '
           'objects of experience exist but their substance is mental '
           '\u2014 trees are dream-trees in the sense that their '
           'underlying nature is experiential. The consolidated '
           'premise adopts exactly this form (as the previous audit\'s '
           'repair R7 already recognized): its claim is ontological, '
           'not skeptical \u2014 it does not doubt the world\'s '
           'reality; it reinterprets its substance. This adoption '
           'answers the semantic-externalist objection in its strongest '
           'form: if dream-talk refers inside the dream, then the '
           'metaphysical dream hypothesis is not refuted by that fact '
           '\u2014 it is a claim about what the referring terms are '
           'made of, not about whether there is anything they refer '
           'to. The price of the move is the loss of all epistemic '
           'frisson: the premise can no longer be sold as '
           '"waking from the dream," only as re-describing what '
           'waking already discloses.')

    L.data_table(
        story,
        'Table 8. The premise among its traditions.',
        ['Tradition', 'Fundamental reality', 'Mind\u2013matter relation', 'Central open problem', 'Relation to the audited premise'],
        [
            ['Advaita Vedanta',
             'Brahman: being-consciousness-bliss; one without a second',
             'World is maya \u2014 appearance, not creation',
             'Status of the individual self; liberatory knowledge',
             'Structural identity of the Absolute; the premise adds the '
             'physics-interpretation project'],
            ['Analytic idealism (Kastrup)',
             'One transpersonal mind',
             'Matter is the extrinsic appearance of mental process',
             'Decombination: dissociation without a law',
             'Same family; premise adds stratification and topological '
             'priority'],
            ['Classical theism (Aquinas)',
             'God as pure act, simple, timeless',
             'Creation: real relation in the creature, none in God',
             'Evil; the modal status of creation',
             'Shared attributes; premise drops creation and personhood, '
             'keeping the metaphysics'],
            ['Absolute idealism (Hegel, Schelling)',
             'Absolute Spirit self-othering',
             'Nature is Spirit\'s self-externalization',
             'Necessity of the specific world-shape',
             'The avatar-mirror argument and Grand Dream phase descend '
             'from it'],
            ['Russellian monism / panpsychism',
             'Matter with experiential intrinsic natures',
             'Mind is the intrinsic face of physical structure',
             'Combination problem',
             'Shares the intrinsic-nature diagnosis at lower cost; '
             'micro-route instead of cosmic subject'],
            ['Cosmopsychism',
             'One cosmic subject',
             'Local subjects derive from the cosmic subject',
             'Subject-collapse (decombination, mirrored)',
             'Closest cousin; the unity-of-experience argument favors '
             'this family over the micro family'],
            ['Simulation hypothesis / metaphysical dream',
             'A base reality with computational or experiential '
             'substance',
             'Perceived world rendered by the base',
             'Skeptical vs. metaphysical reading; reference inside the '
             'simulation',
             'Premise adopts the metaphysical (substance) form and '
             'retires the skeptical frisson'],
        ],
        [0.16, 0.20, 0.21, 0.19, 0.24], font_size=8.0, header_font=8.4)

    L.body(story,
           'The comparative table closes the gap the transcript left '
           'open (W11) and yields the consolidation\'s positioning '
           'sentence: the audited premise is an Advaita-style '
           'non-dualism, argued with the apparatus of analytic '
           'idealism, disciplined by the method of classical theology\'s '
           '<i>via negativa</i>, and extended by two genuinely original '
           'moves \u2014 the stratified assignment of the quantum '
           'interpretations, and topological priority as the replacement '
           'for causation. Each element of that sentence is defensible; '
           'none of it is a discovery about physics.')

    # ══════════════ 9. THE REPAIR PROGRAM ══════════════════════════════
    L.h1(story, '9. Improvements: The Repair Program')

    L.body(story,
           'The repairs convert the audit\'s findings into standing '
           'rules for the consolidated premise. They are organized in '
           'five families \u2014 epistemic discipline, doctrinal '
           'commitment, empirical hygiene, dialectical completeness, '
           'and register declaration \u2014 because the same failure '
           'tends to recur when a rule is stated as an aspiration '
           'rather than as a procedure. Each repair names the '
           'weaknesses it addresses and the cost of adopting it; the '
           'consolidated premise in chapter 10 carries all ten.')

    L.h2(story, '9.1 Epistemic discipline')

    L.body(story,
           '<b>R1. Institutionalize the two-language regime.</b> The '
           'Lexicon of Eternal Being becomes binding for all '
           'ontological statements, and every use of process vocabulary '
           '\u2014 dreaming, rendering, collapse, before, after, '
           'creation, beginning \u2014 is marked as pedagogical <i>upaya</i>, '
           'explicitly discarded once the point is made. The transcript '
           'needed the rule stated once (L5479) and then still required '
           'three further corrections (C9, C12, C13); the rule works '
           'only if enforcement is lexical, not aspirational. Cost: a '
           'permanent editorial burden, and prose that is colder than '
           'the dream language it replaces. Addresses W3, W4, and the '
           'entire correction log.')

    L.body(story,
           '<b>R2. Grade every claim and ban inflation.</b> Three '
           'grades, marked in the text itself where ambiguity would '
           'otherwise creep: physics fact (A), structural analogy (B), '
           'metaphysical interpretation (C). The words "proof", '
           '"smoking gun", "vindication", "necessity", and "must" are '
           'reserved for Grade A uses or deleted. The default posture '
           'is the dialogue\'s own best hedge: "a metaphysical '
           'interpretation, not an established scientific claim" '
           '(L1151). Cost: rhetorical deflation that will disappoint '
           'readers seduced by the original\'s certainty language. '
           'Addresses W1, W3, W5, W7.')

    L.h2(story, '9.2 Doctrinal commitment')

    L.body(story,
           '<b>R3. Commit to one Bell response.</b> The premise answers '
           'Bell with topological priority and holistic covariance: '
           'setting and particle are not independent because they are '
           'topologically posterior expressions of one structure, and '
           'entanglement is the non-spatial unity of that structure. '
           'The earlier narrations \u2014 sacrificing locality '
           '(L395), preserving operational locality via ontological '
           'non-locality (L488\u2013504), temporal superdeterminism '
           '(L1249\u20131606) \u2014 are retired and recorded as '
           'superseded. Cost: the loss of three colorful narrations and '
           'the admission that the framework once held three answers '
           'to one question. Addresses W1 and the contradictions of '
           'the transcript\'s early free-will and Bell sections.')

    L.body(story,
           '<b>R4. Fix the account of probability.</b> The Born rule is '
           'stated once, in the final form: the equilibrium '
           'distribution of a confined perspective, with quantum '
           'non-equilibrium as the observable signature of the unsettled '
           'condition. "Narrative weight" and the raw axiom are '
           'retired. The account is carried at Grade B and tied to the '
           'empirical annex, since it is the only part of the '
           'probability story with a falsifiable edge. Cost: if '
           'non-equilibrium is never found, the account weakens toward '
           'metaphor \u2014 and the premise must say so rather than '
           'absorb the null result (W1\'s lesson).')

    L.h2(story, '9.3 Empirical hygiene')

    L.body(story,
           '<b>R5. Maintain an honest empirical ledger.</b> Exactly '
           'three items belong on it: Valentini-type non-equilibrium '
           'signatures in the cosmic microwave background; '
           'objective-collapse parameter windows; and the '
           'classical-AI consciousness ceiling with the associated '
           'quantum-computing complexity wall. Each is listed with what '
           'it would establish, what it would not, and which rival '
           'programs predict the same outcomes. The ledger also records '
           'the framework\'s own owed criteria (L1554\u20131562): the '
           'hidden variables, the probability measure, the quantitative '
           'reproduction, the no-signaling guarantee, and the predicted '
           'deviations. No other empirical claim is permitted to carry '
           'weight, and no physicist is conscripted whose own '
           'commitments oppose the conclusion. Cost: the framework '
           'loses the rhetorical support of Penrose, Hawking, and '
           'Valentini readings. Addresses W1, W5, W6, W8.')

    L.body(story,
           '<b>R6. State the free-energy inversion as a wager.</b> The '
           'Markov-blanket formalization is stated as the premise\'s '
           'central wager about where the law of dissociation will come '
           'from, not as a feasibility transfer from physicalist '
           'neuroscience. The physicalist reading of the same '
           'mathematics remains available, and the premise says so. '
           'Decombination is carried as the premise\'s largest open '
           'problem, exactly as the external critique demanded '
           '(L3879\u20133891). Cost: the formalization stops counting '
           'as progress toward the law and starts counting as a bet '
           '\u2014 which is what it is. Addresses W2, W12.')

    L.h2(story, '9.4 Dialectical completeness')

    L.body(story,
           '<b>R7. Engage the rivals.</b> The consolidated premise '
           'names its nearest alternatives \u2014 Russellian monism '
           'and panpsychism, which share the intrinsic-nature diagnosis '
           'at lower ontological cost, and cosmopsychism, its closest '
           'cousin \u2014 and the semantic-externalist tradition, which '
           'blunts dream arguments by observing that dream-talk refers '
           'inside the dream. The premise\'s answers: the '
           'unity-of-experience and one-substance parsimony arguments '
           '(L7748), offered as reasons rather than proofs, and the '
           'ontological (substance) rather than skeptical reading of '
           'the dream hypothesis. Chapter 8 supplies the full '
           'engagement. Addresses W11.')

    L.body(story,
           '<b>R8. Strengthen the theodicy, honestly.</b> The premise '
           'keeps totality and play as its account of suffering and '
           'adds the admission the transcript omitted: the account\'s '
           'cost is borne by the avatars, and the premise has no '
           'argument that forces acceptance \u2014 only the testimony '
           'that contrast is the condition of experience. It is stated '
           'as the premise\'s moral remainder, not resolved. Cost: the '
           'premise confesses an unpaid moral debt in perpetuity. '
           'Addresses W10, gap G3.')

    L.body(story,
           '<b>R9. Downgrade the demonstrations.</b> The infinity, '
           'mirror, and completeness arguments for the necessity of '
           'avatars are retained as reasons internal to the premise\'s '
           'own commitments, with their counters named: infinity need '
           'not instantiate every perspective experientially; '
           'consciousness may not require subject\u2013object '
           'structure; the keystone claim of structural dependence is '
           'asserted, not derived. Nothing in the premise\'s core '
           'depends on their validity. Cost: the premise loses its '
           'would-be proofs of its own necessity. Addresses W9, gap '
           'G6.')

    L.h2(story, '9.5 Register declaration')

    L.body(story,
           '<b>R10. Declare the register.</b> The consolidated premise '
           'is a metaphysical interpretation that maintains an '
           'empirical annex. The interpretation earns its keep by '
           'unification and parsimony; the annex tests the boundary '
           'story and keeps the premise honest; neither masquerades as '
           'the other. This single declaration dissolves the '
           'transcript\'s ending, in which a laboratory program and a '
           'timeless Singularity coexist without a stated relation '
           '(W12), and it honors the dialogue\'s own best '
           'self-description \u2014 "a coherent bet" \u2014 now made '
           'structural. Cost: the premise cannot be marketed as '
           'science, ever, until its Newton arrives and the annex '
           'graduates.')

    L.callout(story, 'The repairs in one sentence',
              'Say what the framework is (an interpretation), grade '
              'what it claims (A/B/C), fix what it answers (one Bell '
              'response, one probability account), owe what it borrowed '
              '(the law of dissociation, the measure, the formalization '
              'of priority), engage whom it fears (Russellian monism, '
              'semantic externalism, the distributional problem of '
              'evil), and declare what it is doing (interpretation plus '
              'annex, never conflated).')

    return story
