#!/usr/bin/env python3
"""Part 4: chapters 10-12 (Consolidated Premise, Empirical Annex,
Glossary)."""
import fhcp_pdf_lib as L


def add_content(story):
    # ══════════════ 10. THE CONSOLIDATED PREMISE ══════════════════════
    L.h1(story, '10. The Consolidated Premise')

    L.body(story,
           'This chapter delivers the consolidation: a single statement '
           'of the premise that incorporates the fourteen corrections '
           'the interlocutor issued, the ten repairs of chapter 9, and '
           'every verdict of the ledger. The statement is written in the '
           'neutral register of this report, in declarative form, using '
           'the two-language regime: ontological statements are made in '
           'the language of eternal being; process language appears only '
           'where flagged as pedagogical. What the consolidation '
           'preserves: the five axioms, the four bridges at their honest '
           'grades, the six surviving doctrines, and the concessions. '
           'What it discards: the inflation vocabulary, the three '
           'superseded Bell narrations, the "narrative weight" '
           'placeholder, the conscription of physicists, and every '
           'claim the transcript itself retired under correction.')

    L.h2(story, '10.1 The core thesis')

    L.quote(story,
            'There is one reality. It is timeless, spaceless, '
            'unchanging, without parts or composites, and conscious \u2014 '
            'not as an attribute it possesses but as what it is. It '
            'neither creates, dreams, nor simulates, for those are verbs '
            'of process, and process belongs to the perspective, not to '
            'the ground. The physical universe is not an object beside '
            'it but its extrinsic appearance: the eternal, static, '
            'necessary geometry of the unlimited as viewed from '
            'finitude. Finite perspectives \u2014 localized, bounded, '
            'irreducibly experiential \u2014 are the loci in which this '
            'appearance unfolds. This is the whole of the premise; '
            'everything else the dialogue built is either an '
            'interpretation of physics under it, a bridge yet to be '
            'argued, or a debt the premise carries openly.',
            'The consolidated core thesis, assembled from L1\u20132, '
            'L5307\u20135372, L5364\u20135368, L9673\u20139675')

    L.body(story,
           'The consolidation records its provenance honestly: the '
           'final statement of the thesis in the transcript is the '
           'interlocutor\'s own credo \u2014 "God did not create a '
           'universe. God is all there is. That is the objective, '
           'unchanging reality. What we are experiencing as the '
           'universe is a subjective perspective of the unchanging God" '
           '(L9673\u20139675) \u2014 and the consolidation restates it '
           'in the third person without altering its content, because '
           'the corrections that shaped it (C4, C6, C13, C14) were '
           'imposed precisely to protect that content from the '
           'framework\'s own tendency to smuggle process back in.')

    L.h2(story, '10.2 The doctrine of layers')

    L.body(story,
           'The premise is stratified. It distinguishes the unmanifest '
           'Absolute \u2014 beyond mathematics and description \u2014 '
           'from its eternal mathematical expression, the Logos, and '
           'from the rendered order that finite perspectives inhabit. '
           'The wavefunction of physics, the nets of local algebras in '
           'algebraic quantum field theory, and twistor geometry are '
           'read as dialects of the Logos, not as the Singularity '
           'itself; the wavefunction is the nomological structure of '
           'the manifold, discoverable but not subjective '
           '(L5827\u20135838). Between the Logos and the appearance '
           'stands the tether: the atemporal consistency constraints '
           'for which topological priority is the governing concept. '
           'Within the appearance, the rendering threshold, the '
           'consensus protocol, and the avatar\'s epistemic horizon each '
           'do their work at their own stratum. Table 9 states the '
           'layers with their physics correspondences, each held at the '
           'grade the audit assigned.')

    L.data_table(
        story,
        'Table 9. The stratified ontology, consolidated.',
        ['Layer', 'Ontological role', 'Physics correspondence', 'Grade'],
        [
            ['The Absolute (Singularity)',
             'The unmanifest, non-composite ground; pure actuality; '
             'beyond mathematics.',
             'None by definition; approached negatively.',
             'C'],
            ['The Logos',
             'The eternal, spaceless mathematical expression of the '
             'Absolute; the global structure.',
             'Universal wavefunction; global state on the C*-algebra; '
             'twistor space; configuration space.',
             'B'],
            ['The tether',
             'Atemporal consistency: the part cannot contradict the '
             'whole; topological priority.',
             'Guidance equation; GNS construction; incidence relation; '
             'transactional handshake.',
             'B'],
            ['The rendering threshold',
             'Where unbounded potential is restricted into definite, '
             'classical appearance.',
             'Objective collapse (GRW, CSL, Penrose\u2013Di\u00f3si); '
             'decoherence as interface.',
             'B'],
            ['The consensus protocol',
             'Redundant broadcasting that makes appearance shared and '
             'stable; objectivity as consensus.',
             'Quantum Darwinism; environmental redundancy.',
             'A/B'],
            ['The avatar\'s horizon',
             'The localized perspective: memory, agency, sequence; the '
             'arrow lives here.',
             'Relational QM; QBism; the perspectival reading of the '
             'partial trace.',
             'B/C'],
        ],
        [0.19, 0.33, 0.36, 0.12], font_size=8.6, center_cols=(3,))

    L.body(story,
           'The stratification\'s standing is fixed by repair R2: it is '
           'a Grade C interpretive framework whose virtue is that it '
           'converts a century of interpretation rivalry into a '
           'consistent assignment problem \u2014 Many-Worlds and '
           'pilot-wave at the Logos, the transactional reading and '
           'superdeterminism at the tether, objective collapse at the '
           'rendering threshold, Quantum Darwinism at consensus, '
           'relational QM and QBism at the horizon \u2014 and whose '
           'liability is that it cannot lose. It is therefore held as '
           'an interpretation, never as a confirmed structure.')

    L.h2(story, '10.3 The doctrine of time')

    L.body(story,
           'Time is not one thing, and the reconciliation the premise '
           'offers is the stratified one the dialogue converged on '
           '(L7050\u20137067). At the level of the Absolute there is no '
           'time: no sequence, no before, no after (L3089\u20133092). '
           'At the level of the manifold, time is a static geometric '
           'coordinate, and general relativity is the physics of its '
           'curvature (L3094\u20133099). At the level of the avatar, '
           'time is lived sequence, and the parameter of the '
           'Schr\u00f6dinger equation is the internal clock of a '
           'perspective that cannot take in the whole at once '
           '(L7017\u20137023). The Wheeler\u2013DeWitt equation, read '
           'as the signature of the timeless level, is a Grade B '
           'correspondence kept with its hedge attached. The arrow of '
           'time is the direction of actualization: the past is the '
           'settled record, the future the open potential, the present '
           'the edge where records are written (L2201\u20132207); its '
           'formula is the dialogue\'s best aphorism, kept verbatim: '
           '"The arrow of time is not in the universe. The arrow of '
           'time is in the looking" (L2743). The low-entropy boundary '
           'called the Big Bang is the local horizon of this '
           'perspective, not the beginning of anything absolute '
           '(L2331\u20132336); "beginning" and "initial" are process '
           'words, used only pedagogically. The doctrine\'s honest '
           'limit, retained: a measure for typicality \u2014 including '
           'the Boltzmann-brain question \u2014 is still owed (L1903, '
           'gap G2).')

    L.h2(story, '10.4 The doctrine of ground: topological priority')

    L.body(story,
           'The premise replaces causation at the fundamental level '
           'with topological priority (L11028\u201311086). The boundary '
           'is prior to the bulk as the canvas is prior to the '
           'painting and the axioms to the theorems; nothing happens '
           'first and nothing is pushed later. The correlations '
           'science reads as causation are entailments: the neural '
           'correlate and the conscious state are one structure viewed '
           'from two sides, and the measurement setting and the '
           'particle\'s state are parts of one global invariant '
           '(L10979\u201311015). This is the premise\'s single answer to '
           'Bell (repair R3): statistical independence fails because '
           'separateness itself is derivative \u2014 the stronger '
           'reading of superdeterminism, in which the setting and the '
           'system are co-arising aspects of one whole rather than '
           'parties to a primordial conspiracy \u2014 and entanglement '
           'is the non-spatial unity of the Logos showing through '
           '(L5154\u20135167). Physical causal closure is preserved, '
           'since nothing mental interrupts the appearance\'s order; '
           'downward causation is replaced by vertical grounding '
           '(L9228\u20139278). Emergence, correctly interpreted, is a '
           'change of perspective or layer, not a process (C12, '
           'L9154\u20139181); what physics calls the emergence of '
           'spacetime the premise calls its grounding in entanglement, '
           'with the Ryu\u2013Takayanagi relation carried as the '
           'strongest Grade B witness (L6964\u20136971). The doctrine\'s '
           'debt, retained: topological priority is named, not '
           'formalized (gap G4).')

    L.h2(story, '10.5 The doctrine of the person')

    L.body(story,
           'A person, in this premise, is a topological boundary \u2014 '
           'a Markov blanket, in the metaphor of the borrowed '
           'mathematics: a localized, self-maintaining horizon through '
           'which the unlimited appears to itself as finite '
           '(L3962\u20133963). The brain is not the person\'s '
           'generator; it is the extrinsic image of the person\'s '
           'boundary (L2794\u20132804). The individual self is a '
           'rendered construct bounded by birth and death '
           '(L9686\u20139691); its deliberation is real at its layer, '
           'and its freedom is the freedom of what it ultimately is, '
           'not of the construct \u2014 the stratified resolution the '
           'dialogue reached after three attempts (L8790\u20138817): '
           'the body determined, the deliberation real, the identity '
           'free. Other persons are not private worlds: consensus '
           'through redundant broadcasting is what objectivity means, '
           'and the moon is there when nobody looks in the sense that '
           'its pointer states are multiply recorded in the shared '
           'environment (L3597\u20133608). The arguments that such '
           'avatars are necessary features of the Absolute are kept as '
           'reasons, not demonstrations, with their counters named '
           '(repair R9): infinity and completeness suggest the '
           'inclusion of finitude; self-knowledge suggests a mirror; '
           'play suggests why the inclusion is not a defect '
           '(L9535\u20139604).')

    L.h2(story, '10.6 The status clause')

    L.body(story,
           'The premise declares its own condition (repair R10). It is '
           'a metaphysical interpretation with an empirical annex. The '
           'interpretation earns consideration by unification \u2014 '
           'one substance rather than two (L7748) \u2014 by '
           'dissolving the hard problem without magic, and by making '
           'the physics it trusts hang together with the experience it '
           'cannot doubt. It does not yet explain the data better than '
           'physicalism; it accommodates them (L3873). Its largest open '
           'problem is decombination \u2014 the law by which the one '
           'becomes many \u2014 and the Markov-blanket program is its '
           'wager on where that law will be found, stated as a wager '
           '(repair R6). Its moral remainder is the suffering of '
           'avatars, which totality and play illuminate but do not '
           'justify (repair R8). It faces rivals it must continue to '
           'answer: Russellian monism and panpsychism on one side, '
           'semantic externalism on the other (repair R7, chapter 8). '
           'It keeps a small ledger of claims the world could wound '
           '\u2014 not because the Absolute could be falsified by '
           'appearances, but because the boundary story, which is the '
           'part of the premise that lives at the interface, can be '
           '(chapter 11). Until its Newton arrives, the premise is held '
           'the way its own best sentence holds it: "a coherent bet, '
           'not a guaranteed answer" (L3893) \u2014 held firmly, '
           'transparently, and ready to be corrected again.')

    # ══════════════ 11. THE EMPIRICAL ANNEX ═══════════════════════════
    L.h1(story, '11. The Empirical Annex')

    L.body(story,
           'The annex lists everything in the premise\'s orbit that '
           'experiments can touch. Its rules are the audit\'s: each '
           'item records what a result would establish for the boundary '
           'story, what it would not establish for the Absolute, and '
           'which rival programs expect the same result. The annex also '
           'carries the criteria the dialogue itself conceded it owed: '
           'a precise ontology, a law of dissociation, a '
           'brain-to-experience mapping, novel predictions, and an '
           'account of the lawlike world (L3879\u20133883). Items on '
           'the ledger are the only empirical claims the premise is '
           'permitted to advance.')

    L.data_table(
        story,
        'Table 10. The empirical ledger.',
        ['Test', 'A positive result would establish', 'It would not establish', 'Shared with'],
        [
            ['Valentini-type quantum non-equilibrium in the cosmic '
             'microwave background or relic particles (L10091\u201310098)',
             'The Born rule is an equilibrium, not an axiom; probability '
             'is perspectival; BP4 gains Grade A support.',
             'The idealist substrate; deterministic subquantum '
             'theories suffice for the physics.',
             'De Broglie\u2013Bohm and superdeterminist programs; some '
             'quantum-gravity phenomenology.'],
            ['Objective-collapse parameter windows (GRW, CSL, '
             'Penrose\u2013Di\u00f3si) probed by optomechanics and '
             'interferometry (L6155\u20136167)',
             'A physical rendering threshold exists at the layer the '
             'stratified ontology assigns.',
             'Any interpretation of the threshold as experiential; '
             'collapse theories are physics-first.',
             'The objective-collapse research program; independent of '
             'idealism.'],
            ['A classical-AI consciousness ceiling and the '
             'quantum-computing complexity wall (L3931\u20133939; '
             'L3331\u20133336)',
             'The boundary story\'s claim that consciousness is not '
             'substrate-independent classical computation.',
             'The Absolute; even a ceiling is consistent with '
             'non-idealist biological naturalism.',
             'The Penrose\u2013Hameroff program; skeptics of strong-AI '
             'consciousness.'],
        ],
        [0.28, 0.27, 0.23, 0.22], font_size=8.4)

    L.body(story,
           'Two annex disciplines complete the ledger. First, the '
           'negative space is recorded with the same care as the '
           'positive: if quantum non-equilibrium is never found and '
           'constrained ever tighter, the equilibrium account of the '
           'Born rule weakens toward metaphor, and the premise must say '
           'so rather than absorb the null result as confirmation '
           '\u2014 the direct lesson of W1. Second, the encoding-model '
           'program for the functor R is retained as method, not as '
           'discriminator: mapping neural manifolds to experiential '
           'proxies with topological data analysis (L4110\u20134175) is '
           'good science under either ontology, and the premise claims '
           'from it only what a physicalist identity theory would also '
           'claim \u2014 structural isomorphism \u2014 leaving the '
           'direction of grounding to interpretation (the lesson of '
           'W8, and the standing debt of gap G5).')

    # ══════════════ 12. GLOSSARY ══════════════════════════════════════
    L.h1(story, '12. Glossary of the Final Vocabulary')

    L.body(story,
           'The glossary enforces the two-language regime (repair R1). '
           'Table 11 defines the ontological vocabulary \u2014 the '
           'language of eternal being in which the premise is stated. '
           'Table 12 lists the process vocabulary permitted only as '
           'pedagogy, each entry with its sanctioned use and its '
           'standing prohibition. The line references give where each '
           'term was fixed in the transcript, at its latest corrected '
           'occurrence.')

    L.data_table(
        story,
        'Table 11. The ontological vocabulary (the language of eternal being).',
        ['Term', 'Definition', 'Fixed at'],
        [
            ['The Absolute / the Singularity',
             'The one, timeless, spaceless, non-composite reality; pure '
             'actuality; all there is. Not an object among objects, and '
             'not made of parts, bits, or quanta.',
             'L5307\u20135372; L10911\u201310963'],
            ['The Logos',
             'The eternal, spaceless mathematical expression of the '
             'Absolute; the global structure physics approaches through '
             'wavefunction, algebra, and geometry. Distinct from the '
             'Singularity, which is beyond mathematics.',
             'L5827\u20135838; L5930\u20135947'],
            ['The extrinsic manifold',
             'The physical universe understood as the static, '
             'four-dimensional appearance of the Absolute to finite '
             'perspective; the rendered order.',
             'L5497; L5559\u20135597'],
            ['Topological priority',
             'The structural precedence of ground over grounded: '
             'boundary over bulk, canvas over painting. The replacement '
             'for temporal causation at the fundamental level.',
             'L11028\u201311086'],
            ['Holistic covariance',
             'The atemporal consistency of the whole: parts cannot be '
             'statistically independent because separateness is '
             'derivative. The premise\'s settled Bell response.',
             'L6048\u20136051; L8727\u20138742'],
            ['Perspectival actualization',
             'The process-by-appearance in which a finite perspective '
             'converts open potential into settled record; the home of '
             'the arrow of time.',
             'L1859\u20131873; L3152\u20133158'],
            ['The Markov blanket',
             'The localized, self-maintaining boundary of an avatar; '
             'borrowed from statistical structure as the premise\'s '
             'wager on the shape of the law of dissociation.',
             'L3962\u20133963; L8975\u20138984'],
            ['Quantum equilibrium',
             'The settled condition of a confined perspective in which '
             'the Born rule holds; its violation \u2014 '
             'non-equilibrium \u2014 is the annex\'s principal '
             'observable.',
             'L9988\u201310048'],
        ],
        [0.22, 0.56, 0.22], font_size=8.5)

    L.data_table(
        story,
        'Table 12. The pedagogical vocabulary (upaya; use and discard).',
        ['Term', 'Sanctioned pedagogical use', 'Standing prohibition'],
        [
            ['Dream / dreaming',
             'To convey that the universe is appearance within mind \u2014 '
             'the objects exist, but their substance is mental '
             '(the metaphysical, not the skeptical, dream hypothesis).',
             'Never as event or change of state; the Absolute does not '
             'begin or cease dreaming (correction C4).'],
            ['Rendering / collapse',
             'To convey the restriction of potential into definite '
             'appearance at the avatar\'s horizon.',
             'Never as a process undergone by the Absolute; collapse is '
             'perspectival, not global.'],
            ['Creation / creator',
             'To introduce the premise to theistic audiences by contrast.',
             'Never ontologically: there is no maker, no made, and no '
             'outside (L9692\u20139699).'],
            ['Before / after / beginning',
             'To order exposition for time-bound readers.',
             'Never about the Absolute or the manifold as such; the Big '
             'Bang is a boundary, not an event (C7, C8).'],
            ['Boot-up / compilation / patching',
             'To borrow intuitions from computing when explaining '
             'cosmology.',
             'Never literal; flagged as simulation-hypothesis residue '
             'and dropped immediately (C3, C9).'],
            ['Defect / glitch / error',
             'To describe how anomalies appear to avatars.',
             'Never about the Absolute, which is perfect; defects are '
             'avatar constructs (C2).'],
        ],
        [0.20, 0.40, 0.40], font_size=8.5)

    L.body(story,
           'The glossary closes the consolidation where the dialogue '
           'itself closed: with vocabulary made obedient to the position '
           'it serves. The premise\'s claims are now graded, its Bell '
           'response is single, its probability account is fixed, its '
           'ledger is honest, its rivals are named, its suffering is '
           'carried rather than explained away, and its process language '
           'is flagged at every use. What remains is exactly what the '
           'transcript\'s best sentence promised and its best moments '
           'delivered: a coherent bet, held openly, about the one '
           'unchanging truth in which all of this \u2014 including this '
           'audit \u2014 appears.')

    return story
