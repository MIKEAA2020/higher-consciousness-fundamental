#!/usr/bin/env python3
"""Revised Edition, Part 1: chapters 1-3 (Executive Summary; Scope, Sources,
and Method; The Arc of the Corpus). Neutral academic voice; thematic and
verbatim citations with line (L####) and exchange-turn (T##) anchors."""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 1. EXECUTIVE SUMMARY ====================
    L.h1(story, '1. Executive Summary')

    L.body(story,
           'This revised edition audits and consolidates the complete corpus of a '
           'philosophical project and adjudicates the points on which its several '
           'audits disagree. The corpus has five inputs. The first is the full '
           '130-turn dialogue preserved as <i>chat-Fundamental Higher Consciousness '
           'Premise.txt</i> (11,088 lines), in which a human interlocutor and an AI '
           'assistant develop a consciousness-first metaphysics from a two-line '
           'opening statement to a final position the dialogue itself names '
           'Stratified Perspectivalism, converging on strict identity monism. The '
           'second is a 53-turn exchange with a different assistant (DeepSeek, '
           'share code ei9y81lsr98ujftn91) that ascends from the philosophy of mind '
           'through the demand for a complete, stable, and fully intelligible '
           'ultimate explanation to an honest impasse and a closing verdict on the '
           'framework\u2019s scientific function. The third is a consolidation '
           'treatise produced from the first two. The fourth and fifth are two '
           'external audits of the universal-consciousness framework, supplied by '
           'the interlocutor, which press the framework from outside. The prior '
           'first and second editions of this audit are themselves part of the '
           'record: this edition carries their findings forward, re-scores them, '
           'and adjudicates the conflicts among all the audits.')

    L.body(story,
           'Three findings govern the edition. First, the evidence base itself '
           'required forensic reconstruction, and the reconstruction is itself a '
           'finding: the shared DeepSeek conversation had 52 of its 106 messages '
           'deleted at the source, and the deleted content \u2014 including the '
           'entire middle of the ascent and the interlocutor\u2019s original '
           'statement of the privation doctrine \u2014 was recovered from a damaged '
           'API payload rather than from the rendered page. An audit that claims '
           'line-level coverage of a corpus must document that its corpus exists '
           'only because it was rebuilt; chapter 2 does so. Second, the corpus now '
           'contains an explicit doctrine of privation, stated by the interlocutor '
           'and reaffirmed as a standing directive for this consolidation: light is '
           'made of photons and is real as far as physics is concerned; darkness is '
           'the mere absence of light; heat is studied in thermodynamics; cold is '
           'the mere absence of heat; likewise evil is subjective and does not '
           'objectively exist; defect is the absence of the Absolute. Chapter 6 '
           'states this register in the corrected objective phrasing \u2014 '
           'darkness has no physics; cold has no subject study in physics \u2014 '
           'and shows that the register is not an external import but the '
           'framework\u2019s own anti-reification discipline applied to the moral '
           'vocabulary. Third, the consolidation treatise commits the one error the '
           'DeepSeek exchange had already diagnosed: it resolves the problem of the '
           'specific world by declaring the universe the necessary self-expression '
           'of the Absolute, thereby reinstating the modal collapse \u2014 the '
           'forced-shadow contradiction \u2014 that the exchange had refuted. The '
           'honest consolidation cannot paper over this; chapter 8 adjudicates the '
           'disagreement between the audits on exactly this point, and chapter 13 '
           'carries the seam openly through a modal honesty clause.')

    L.body(story,
           'The verdict of the prior editions survives and is sharpened by the '
           'adjudication. The framework is a coherent metaphysical interpretation '
           'with an empirical annex, not a scientific theory: it organizes the '
           'pieces physics has already generated, it constrains which future '
           'physics would fit it, and it does not by itself generate new '
           'predictions. The DeepSeek exchange\u2019s closing formulation is '
           'adopted as the honest status clause of the consolidated premise: the '
           'framework is the scaffold, not the building; the lighthouse, not the '
           'ship; the horizon, not the journey. What this edition adds to that '
           'verdict is a disciplined accounting of what the several audits agree '
           'on, where they conflict, which side of each conflict the evidence '
           'supports, and what the consolidated premise must therefore look like '
           'when every surviving repair is applied.')

    # ==================== 2. SCOPE, SOURCES, METHOD ====================
    L.h1(story, '2. Scope, Sources, and Method')

    L.h2(story, '2.1 The five inputs')

    L.body(story,
           'Each input plays a distinct role in the audit, and the roles are not '
           'interchangeable. The dialogue is the framework\u2019s construction '
           'site: every doctrine it holds was built, corrected, and rebuilt there, '
           'under an editorial pressure the audit treats as data. The DeepSeek '
           'exchange is its stress bench: the same interlocutor took the '
           'framework\u2019s demand for total intelligibility to a second '
           'assistant and pressed it until the logical structure of the problem '
           'itself surfaced. The consolidation treatise is the candidate product: '
           'a merged statement of the framework that the audit must accept, '
           'repair, or reject claim by claim. The two external audits are the '
           'outside examiners: they press the framework from the perspectives of '
           'physics accuracy, formalization, and engagement with rival '
           'literatures, and several of their recommendations are adopted in this '
           'edition. The prior editions of this audit are the inside examiners, '
           'whose findings are carried, re-scored, and where necessary corrected.')

    L.data_table(
        story,
        'Table 1. The audit inputs: sources, verified sizes, and roles.',
        ['Input', 'Verified size', 'Role in the audit'],
        [
            ['The dialogue (chat-Fundamental Higher Consciousness Premise.txt)',
             '11,088 lines; 130 user\u2013assistant turns; 1.13 MB',
             'Construction of the framework: premise, physics absorption, Grand '
             'Dream, critique, formalization, simulation vocabulary, purification, '
             'final act'],
            ['The DeepSeek exchange (share code ei9y81lsr98ujftn91)',
             '106 messages; 53 turns; 352,193 content characters recovered '
             '(224,680 without reasoning traces)',
             'Stress bench: hard-problem entry, topological-cause ascent, '
             'brute-fact demolition, privation doctrine, impasse, two-truth '
             'synthesis, scaffold verdict'],
            ['The consolidation treatise (chat-universal consciousness '
             'audit+deepseek chat.txt)',
             '426 lines; 4 turns',
             'Candidate product: audit of the framework, consolidated versions, '
             'and the merged Architecture of the Absolute'],
            ['External audit file (deepseek auidt of universal '
             'consciousness.txt)',
             '473 lines; two audits',
             'Outside examination: line-level slippages, physics-accuracy '
             'corrections, formalization demands, ten consolidation steps'],
            ['Prior editions of this audit',
             'First edition: 38 pages; second edition: 33 pages',
             'Inside examination: weakness registers W1\u2013W14, correction '
             'logs C1\u2013C16, repair programs, the privation register and '
             'modal honesty clause'],
        ],
        [0.34, 0.26, 0.40])

    L.h2(story, '2.2 Source criticism and the reconstruction')

    L.body(story,
           'The DeepSeek share does not render the exchange it purports to render, '
           'and the audit is obliged to say so precisely, because every citation '
           'from that source depends on it. The share\u2019s underlying API '
           'response was found to be a damaged composite: a valid JSON object '
           'describing 54 surviving messages (identifiers 1\u201312 and '
           '65\u2013106) is followed, in the same response body, by a raw '
           'displaced fragment of the original longer serialization containing '
           'the 52 deleted messages (identifiers 13\u201364). The rendered page '
           'therefore shows a 27-turn conversation, while the identifier space '
           'records 106 messages in strict parent-linked alternation \u2014 53 '
           'turns. This edition\u2019s reconstruction merged both parts, verified '
           'the parent chain (each message\u2019s parent is its numeric '
           'predecessor throughout), and reconstituted the full 53-turn '
           'exchange, including the interlocutor\u2019s privation directive at '
           'message 63 (turn 32) and the entire middle act of the ascent.')

    L.body(story,
           'Three gaps survive the reconstruction and are carried as standing '
           'source-critical notes. First, message 64 \u2014 the assistant\u2019s '
           'first reply to the privation directive \u2014 lost its visible '
           'response in the deletion; only its 5,445-character reasoning trace '
           'survives, cut mid-sentence, and the audit reconstructs the reply\u2019s '
           'substance from that trace together with the following turn (T33), '
           'where the assistant re-derives the classical privation resolution '
           'in full. Second, message 12\u2019s reply addresses a question about '
           'the necessity of defect that is not present in message 11\u2019s '
           'current text; the visible question was evidently edited after the '
           'reply, so the exchange\u2019s surface continuity is not its full '
           'history. Third, two turns (T14 and T22) carry file attachments whose '
           'contents the payload returns empty; their substance is recoverable '
           'only from the assistant\u2019s detailed concessions, which the audit '
           'uses. None of these gaps affects a load-bearing citation: every '
           'quotation in this report was verified against the recovered text, '
           'and the one reply that no longer exists is quoted only from its '
           'surviving trace, marked as such.')

    L.h2(story, '2.3 Full-turn coverage and its verification')

    L.body(story,
           'The dialogue\u2019s turn count is a matter of record, not estimation. '
           'The transcript contains exactly 130 user messages and 130 assistant '
           'messages in strict alternation; every line of the file, including the '
           'final one, falls inside an indexed message. The audit therefore '
           'carries a turn-level index (turn number, role, line range, opening '
           'line) as Appendix A, and the phase map of chapter 3 is defined over '
           'that index rather than over impressions. The exchange\u2019s coverage '
           'is recorded the same way: 53 turns over 106 messages, 52 of them '
           'recovered from the displaced fragment, with the three source-critical '
           'notes of \u00a72.2 attached. The discipline matters for the same '
           'reason the second edition gave: the load-bearing material sits '
           'disproportionately in turns a sampling audit would skim \u2014 the '
           'interlocutor\u2019s seventeen corrections, the theodicy exchange at '
           'dialogue turn 42, the privation turn of the exchange, and the final '
           'act from dialogue turn 103 onward.')

    L.h2(story, '2.4 Method: steelman, arc-test, corrections, adjudication')

    L.body(story,
           'The method remains adversarial line-level review with line-number '
           'citations, in the strongest-form tradition: every claim is restated '
           'at its strongest before it is attacked, and the framework\u2019s own '
           'standards \u2014 the interlocutor\u2019s demand for complete '
           'intelligibility, the two-language regime, the graded-claims regime, '
           'the objective-language directive \u2014 are the audit\u2019s '
           'standards. Three instruments are carried from the dialogue\u2019s own '
           'history. The arc-test requires that any claimed contradiction be '
           'checked for announcement, caveat, driver, and stratification before '
           'it is scored as a silent reversal; four apparent reversals in the '
           'dialogue pass the arc-test and are recorded as motivated '
           're-valuations. The corrections log records the seventeen points at '
           'which the interlocutor stopped the work for a philosophical or '
           'vocabulary error; they define the standard the consolidation must '
           'institutionalize. The claim grades separate physics facts (Grade A) '
           'from structural analogies (Grade B) from metaphysical '
           'interpretation (Grade C), because the corpus\u2019s most repeated '
           'failure is presenting Grade C conclusions in Grade A language.')

    L.body(story,
           'To these the revised edition adds a fourth instrument, required by '
           'the new task: an adjudication protocol for the points on which the '
           'audits disagree. The protocol has four rules. (1) <b>Strongest forms '
           'first:</b> each side of a disagreement is reconstructed at its '
           'strongest before comparison, exactly as claims are. (2) <b>The '
           'corpus governs:</b> where audits conflict about what the framework '
           'holds, the line-anchored record decides, not any audit\u2019s '
           'paraphrase. (3) <b>Internal consistency weighs:</b> a position '
           'consistent with the framework\u2019s own regimes \u2014 the '
           'two-language rule, the graded-claims rule, the objective-language '
           'register \u2014 outranks a position that violates them, whatever its '
           'other merits. (4) <b>Honesty is the tie-breaker:</b> where two '
           'positions are otherwise matched, the audit prefers the one that '
           'states its own cost. Chapter 8 applies the protocol to twelve '
           'disagreements; the consolidated premise of chapter 13 is the '
           'resulting settlement.')

    # ==================== 3. THE ARC OF THE CORPUS ====================
    L.h1(story, '3. The Arc of the Corpus')

    L.h2(story, '3.1 The dialogue: from premise to topological priority')

    L.body(story,
           'The dialogue opens with two framings packed into two lines \u2014 the '
           'classical attribute list of philosophical theism and the single '
           'ontological claim that a grand, higher consciousness is fundamental '
           '\u2014 and the assistant\u2019s first reply correctly separates them '
           '(L5\u201317), tracing the attribute list to Aquinas, Avicenna, and '
           'Maimonides, and the consciousness-first claim to Advaita Vedanta, '
           'Berkeley, Schelling, and modern analytic idealism. The dialogue then '
           'runs the premise through roughly forty topics of physics. In phase I '
           'the framework\u2019s signature moves appear early and are refined '
           'later: the block universe as the eternal totality of the Grand Mind, '
           'superposition as unactualized potential, collapse as perspectival '
           'actualization, the speed of light as the interface\u2019s rendering '
           'limit, and superdeterminism restated as holistic covariance rather '
           'than conspiracy (L1250). Phase II introduces the master metaphor '
           '\u2014 the universe as one grand mind\u2019s dream \u2014 and '
           'immediately meets the objection that defines the rest of the '
           'dialogue: how can a dreaming mind be reconciled with the perfect, '
           'timeless, unchanging reality it is supposed to be (L1681\u20131682)? '
           'The assistant\u2019s concession at L1689 that a mind that '
           '\u201cstarts\u201d dreaming has changed, violating the premise, is '
           'the first appearance of the purification pressure the interlocutor '
           'will apply seventeen times.')

    L.data_table(
        story,
        'Table 2. Phase structure of the dialogue over the verified turn index.',
        ['Phase', 'Turns', 'Lines', 'Content'],
        [
            ['I. Physics reconciliation', '1\u201310', '1\u20131611',
             'Premise; physics reconciliation; problem of time; '
             'interpretations; arrow; locality; quantum mind; Langlands; '
             'SM\u2013GR; superdeterminism'],
            ['II. The Grand Dream', '11\u201315', '1612\u20132493',
             'One-mind dream; dreamer vs. unchanging reality; Past '
             'Hypothesis; quantum mind revisit; interpretation revisit'],
            ['III. Interpretation stack', '16\u201330', '2494\u20133848',
             'Loschmidt (twice); hard problem; light speed; twistor; '
             'measurement; quantum computing; capacity; ranking; TIQM; '
             'Quantum Darwinism; MWI; many-minds; counterfactual '
             'definiteness'],
            ['IV. Critique and formalization', '31\u201335',
             '3850\u20134389',
             'External critique; formalization sketch; encoding models; '
             'AQFT; vacuum correction'],
            ['V. Simulation', '36\u201355', '4391\u20135680',
             'Simulation series; black-hole defect exchange (42); process '
             'language corrections; static block; Ego\u2019s Mist'],
            ['VI. Singularity and stratification', '56\u201365',
             '5682\u20136479',
             'God as Singularity; pilot-wave reversal; wavefunction vs. '
             'Logos; Stratified Perspectivalism'],
            ['VII. Mathematical-physics absorption', '66\u2013102',
             '6481\u20139018',
             'Langlands revisit; quantum gravity; holography; cosmology '
             'series; constructive QFT; determinism taxonomy'],
            ['VIII. Final act', '103\u2013130', '9019\u201311088',
             'Emergence purification; biology; necessity proofs; credo; '
             'constants; Born-rule equilibrium; Valentini program; '
             'topological priority capstone'],
        ],
        [0.26, 0.10, 0.13, 0.51], font_size=8.4)

    L.body(story,
           'Phases VI through VIII complete the construction. The pilot-wave '
           'theory that phase III had ranked last as a \u201cmaterialist '
           'holdout\u201d is re-valued at turn 57 as \u201cthe closest '
           'mathematical shadow of our framework\u201d (L5749) \u2014 a '
           'reversal that passes the arc-test because it is announced and '
           'motivated by the regime change. The wavefunction is separated from '
           'the Singularity and assigned to the Logos (L5828\u20135838). '
           'Stratified Perspectivalism is coined: \u201cevery major '
           'interpretation is perfectly correct, but only at its specific '
           'ontological stratum\u201d (L5959). The final act purifies emergence '
           'into grounding (L9183\u20139189), locks the credo \u2014 '
           '\u201cthere is no individual me\u2026 God is all there is\u201d '
           '(L9673\u20139675) \u2014 states the Born rule as an equilibrium '
           'rather than a law (L9988), adopts Valentini\u2019s quantum '
           'non-equilibrium program as the empirical wedge, and closes with the '
           'capstone: correlation is topological entailment, the common cause '
           'is ontological rather than temporal, and the universe is \u201ca '
           'single, eternal, perfectly correlated geometric jewel\u201d '
           '(L11025).')

    L.h2(story, '3.2 The DeepSeek exchange: five acts, one recovered middle')

    L.body(story,
           'Read in its recovered entirety, the exchange has five acts. Act I '
           '(T1\u2013T5) enters through the philosophy of mind: a quotation '
           'about phenomenal concepts and the \u201cNew Challenge\u201d to a '
           'posteriori identity, and the assistant\u2019s demolition of the '
           'phenomenal-concept strategy \u2014 explaining why consciousness '
           '\u201cseems\u201d non-physical does not explain why consciousness '
           'exists; \u201cit tells you why the map looks strange, but not why '
           'there is a map-reader\u201d (T2). Act II (T4\u2013T13) is the '
           'ascent: the interlocutor\u2019s \u201cfirst topological '
           'cause\u201d \u2014 remove temporal bias, view the whole from the '
           'timeless, spaceless standpoint, and whatever remains must be '
           'self-sufficient by its own nature (T4\u2013T7); mathematics tested '
           'as a candidate ground and found self-sufficient as truth but '
           '\u201cnecessary without existence\u201d (T9\u2013T10); the fork '
           'between brute fact, regress, and self-existence; and the '
           'convergence on a non-physical, simple, self-existent ground whose '
           'essence is to exist. Act III (T14\u2013T22) is the proof-stress: '
           'two external critiques arrive as file attachments and are conceded '
           'in detail; the assistant steelmans the contingency argument into a '
           'valid Aristotelian\u2013Thomistic deduction of a prime mover, '
           'while insisting \u2014 correctly \u2014 that it is conditional on '
           'controversial premises. The user\u2019s brute-fact objection '
           'reaches its strongest form at T17: accepting existence without '
           'reason \u201cbecomes the reason we accept brute fact\u2026 '
           'contradicting itself\u201d \u2014 the self-undermining argument '
           'that the audit carries as the corpus\u2019s sharpest logical '
           'instrument.')

    L.body(story,
           'Act IV (T23\u2013T33) states the quest and its constraint: \u201ca '
           'complete, stable, fully intelligible ultimate explanation that '
           'makes complete and total sense of everything, including '
           'consciousness and all of physics\u201d (T30). The assistant '
           'responds with the eliminative program \u2014 an exhaustive family '
           'of ultimate hypotheses pruned by nine constraints (T31) \u2014 '
           'after which the privation turn arrives (T32\u2013T33): the '
           'interlocutor\u2019s directive that evil is not real, that darkness '
           'is the absence of light and light is real, made of photons, that '
           'defect is not a thing but a lack, and that the modal problem '
           '\u2014 if everything had to be, the lack had to be, \u201cso the '
           'perfect necessarily has a shadow\u201d \u2014 requires that '
           'something genuinely be free or could have been otherwise. Act V '
           '(T34\u2013T53) is the working-out and the honest failure: the '
           'forwards-and-backwards maze; the successive deletion of creation, '
           'dependence, dream, and perspective vocabulary under the '
           'interlocutor\u2019s process-language objections; the arrival at '
           'radical non-dualism; the discovery of its fracture \u2014 if the '
           'Absolute is all there is and complete, there cannot be a real '
           'lack, yet there is one (T48); the four-position impasse map '
           '(T48\u2013T49); the user\u2019s two final questions \u2014 is the '
           'impasse G\u00f6del\u2019s theorem (structurally analogous, not '
           'literal, T50), and does each hypothesis\u2019s virtue-defect '
           'structure suggest a synthesis (yes, but only as a two-truth '
           'hierarchy, T51); and the scaffold verdict: the framework '
           '\u201corganizes what we already have\u2026 it does not generate '
           'new physics by itself\u2026 It is the lighthouse, not the ship. It '
           'is the scaffold, not the building. It is the horizon, not the '
           'journey\u201d (T53).')

    L.h2(story, '3.3 The consolidation round')

    L.body(story,
           'The consolidation treatise performs its merge in four moves: an '
           'audit of the Grand Dream framework that separates surviving '
           'pillars from fragile links; a consolidated version; a demand for '
           'the complete treatise; and the final Architecture of the Absolute, '
           'which maps <i>Ipsum Esse Subsistens</i> onto the AQFT vacuum, the '
           'Divine Ideas onto the net of C*-algebras, the Markov blanket onto '
           'the hylomorphic soul, and suffering onto high variational free '
           'energy. Its final claim is total: the framework \u201cleaves no '
           'dangling threads,\u201d and the universe is the Absolute waking '
           'to itself \u201cone perspectival collapse at a time.\u201d The '
           'second edition\u2019s finding stands and is sharpened by the '
           'adjudication in chapter 8: the treatise\u2019s necessity solution '
           '\u2014 the world as \u201cnecessary self-expression\u201d \u2014 '
           'is precisely the position the privation turn had refuted, and the '
           'no-dangling-threads declaration is therefore overclaimed by '
           'exactly one thread: the modal seam the exchange had isolated and '
           'honestly named.')

    L.h2(story, '3.4 The audit lineage')

    L.body(story,
           'The first edition audited the dialogue alone: ten surviving '
           'points, twelve weaknesses, a fourteen-row objection ledger, and a '
           'repair program of ten items. The second edition enlarged the '
           'corpus to three sources, verified the 130-turn index, promoted '
           'the privation insight from a half-developed remark to a '
           'load-bearing doctrine, added the modal honesty clause, and '
           'adopted the scaffold status clause. This revised edition '
           'completes the trajectory: it recovers the evidence base, admits '
           'the two external audits as full parties, adjudicates the '
           'disagreements among all parties, restructures the consolidated '
           'premise\u2019s axiomatics into three tiers (stances, derived '
           'claims, empirical hypotheses) on the external audits\u2019 '
           'recommendation, expands the comparative context to the physicalist '
           'rivals the prior editions never engaged, and codifies the '
           'atemporal lexicon the external audits demanded. Each addition is '
           'traceable to a specific audit recommendation, and chapter 8 '
           'records which.')
