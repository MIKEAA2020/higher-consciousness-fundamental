#!/usr/bin/env python3
"""Fourth Edition, Part 6: chapters 11-14 + Appendix A (Objection-Response
Ledger; Empirical Annex: Two Programs; Comparative Context, Updated;
Glossary; The Corpus Map and Completion Markers)."""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 11. OBJECTION-RESPONSE LEDGER ====================
    L.h1(story, '11. The Objection\u2013Response Ledger')

    L.body(story,
           'The ledger states every major objection at its strongest, the '
           'best response the corpus fields, and the audit\u2019s verdict '
           'under the standing grades \u2014 Survives (defensible at its '
           'honest grade), Wounded (stands after repair), Open (no '
           'adequate response; carried as liability), and the new '
           'Elevated (open, with a research program and stated failure '
           'conditions). Rows 1\u201314 are carried from prior editions '
           'with re-scores; rows 15\u201324 enter from the new sources.')

    L.data_table(
        story,
        'Table 6. The consolidated objection\u2013response ledger.',
        ['Objection (strongest form)', 'Best corpus response', 'Verdict'],
        [
            ['Decombination: one mind becomes many private subjects; '
             'dissociation relocates the hard problem (E3 T2)',
             'The formal model with S1\u2013S4 and the Level-2 protocol; '
             'the wager is now specified and falsifiable (E2 T82\u2013T88)',
             '<b>Elevated</b> \u2014 open, instrument in hand'],
            ['Empirical underdetermination: the same data fit physicalism; '
             'every result can be absorbed',
             'Reinterpretation conceded; the two annex programs carry '
             'written criteria and named rivals (E2 T88; L1552\u20131563)',
             '<b>Wounded</b> \u2014 persists at the metaphysical level'],
            ['Explains everything, therefore nothing: a structure that '
             'cannot lose is not tracking evidence',
             'Conceded in principle; R20\u2019s elevation rule bans '
             'silent re-labeling; the wall\u2019s price stays stated',
             '<b>Wounded</b> \u2014 the immunization liability persists'],
            ['Hard-problem inversion: mind creating matter is equally '
             'hard',
             'Extrinsic-appearance doctrine, now in appearance-relation '
             'form (E2 T75, T78); the taxonomy concedes the standard '
             'problem is presupposed (E3 T2)',
             '<b>Survives</b> as interpretation at Grade C'],
            ['Quantum-mind empirics: the brain is too warm, wet, noisy',
             'Decoherence reframed as the boundary\u2019s signature; '
             'carried as conditional per W6',
             '<b>Wounded</b> \u2014 conditional standing'],
            ['Born rule: why these probabilities?',
             'Equilibrium of a confined perspective; Valentini '
             'non-equilibrium as the observable signature',
             '<b>Survives</b> at Grade B with a falsifiable edge'],
            ['Why this branch, this outcome?',
             'The equilibrium distribution carries the weight; branch '
             'selection remains open',
             '<b>Wounded</b>'],
            ['Boltzmann brains and typicality',
             'Observers ride stable gradients; the measure is owed (G2)',
             '<b>Wounded</b> \u2014 honest hedge'],
            ['Solipsism: are others unreal?',
             'Layer-4 consensus; objectivity as redundant '
             'intersubjectivity (L3597\u20133608)',
             '<b>Survives</b>'],
            ['Privation: suffering as the cost of contrast \u2014 the '
             'quantity problem',
             'The register\u2019s objective vocabulary plus the modal '
             'argument; the distribution of absences remains confessed '
             '(E2 T32\u2013T33)',
             '<b>Open</b> \u2014 the moral remainder stands'],
            ['Semantic externalism: dream-talk refers inside the dream',
             'The ontological (substance) reading of the dream '
             'hypothesis; the metaphysical, not skeptical, form',
             '<b>Survives</b> (carried repair R7)'],
            ['Causal closure: does mind push particles?',
             'Vertical grounding replaces downward causation (L9228\u20139278)',
             '<b>Survives</b> as a coherent position'],
            ['Misuse of scientific authority',
             'The no-conscription rule; sources mapped, never conscripted '
             '(R2/R5)',
             '<b>Wounded</b> \u2014 rule adopted; history stands'],
            ['Modal overreach: \u201cnecessary\u201d claims without modal '
             'epistemology',
             'Downgraded to reasons with counters named (R9); the '
             'eliminative program\u2019s conditional form enforced',
             '<b>Wounded</b>'],
            ['The two-level structure is an internal contradiction: if '
             'the Absolute alone is real, nothing else is real',
             'The appearance-relation form: one reality appearing, not '
             'two realities coexisting (E2 T74\u2013T75)',
             '<b>Survives</b> in the corrected form only \u2014 R17'],
            ['Brute fact is a stable alternative to the necessary '
             'ground',
             'The self-undermining argument: the permission principle is '
             'itself brute, grounded, or a confession (E2 T17, T25)',
             '<b>Survives</b> \u2014 the exchange\u2019s own a fortiori '
             'verdict'],
            ['The impasse is fatal: regress, brute fact, or the '
             'subject-of-ignorance \u2014 the premise cannot close',
             'The three-walls map accepted; the G\u00f6del-structural '
             'analogy explains the inevitability without proving it '
             '(E2 T46, T50)',
             '<b>Open</b> \u2014 the seam is the boundary of discursive '
             'reason'],
            ['\u201cI\u2019m God limiting myself\u201d is '
             'self-contradictory: why limit? who is limited? what is '
             'the limitation?',
             'The svatantrya reconciliation with its stated trilemma; '
             'manifestation from abundance, not need (E2 T69, T77\u2013T79)',
             '<b>Wounded</b> \u2014 the strongest available form, seam '
             'stated'],
            ['Divine hiddenness: why no direct word to an honest '
             'seeker?',
             'The non-dual dissolution: no separate God to speak; the '
             'seeker is the Absolute \u2014 dissolves the questioner '
             'with the question (E2 T67, T70)',
             '<b>Wounded</b> \u2014 cleanest dissolution, personal '
             'meaning paid'],
            ['Wasted time: after the lessons, redundancy is plain '
             'waste; the lesson theodicy fails',
             'Privation as absence of due order in finite systems; the '
             'quantity residue confessed (E2 T68)',
             '<b>Open</b> at the distributional level'],
            ['The eliminative program\u2019s constraints are optional: '
             'reject one and an elimination fails',
             'Conceded; the program is carried in conditional form '
             'wherever cited (E2 T31, T47)',
             '<b>Survives</b> as conditional structure'],
            ['Pure circularity is incoherent as ultimate: a loop is '
             'composite and brute at the level of the whole',
             'Grounded circularity: horizontal dependence within, '
             'vertical dependence on the ground (E2 T62\u2013T63)',
             '<b>Survives</b> \u2014 with the boundary fixed'],
            ['The decombination model is borrowed mathematics: '
             'physicalist statistics predicts the same domains',
             'Formalism portability conceded; discriminating force '
             'rides on joint S1\u2013S4 under nulls and intervention '
             '(adjudication 16; E2 T88)',
             '<b>Wounded</b> \u2014 neutral until its criterion is run '
             '(R18)'],
            ['The model\u2019s candidate subjects are structural, not '
             'phenomenal: nothing experiences',
             'Conceded at every level of the staircase: structural, '
             'not phenomenal (E2 T86\u2013T87); the taxonomy keeps the '
             'phenomenal step separate (E3 T3)',
             '<b>Open</b> \u2014 the phenomenal step remains owed'],
        ],
        [0.40, 0.36, 0.24], font_size=7.8)

    # ==================== 12. EMPIRICAL ANNEX ====================
    L.h1(story, '12. The Empirical Annex: Two Programs')

    L.h2(story, '12.1 Program A: the physics wagers (dialogue line)')

    L.body(story,
           'Program A is carried from the dialogue line unchanged in '
           'content, now with its odds marked per adjudication 16. '
           '<b>Item one:</b> Valentini-type quantum non-equilibrium in '
           'the cosmic microwave background or relic particles would '
           'establish that the Born rule is an equilibrium rather than '
           'an axiom \u2014 supporting the perspectival reading at Grade '
           'A \u2014 while establishing nothing about the idealist '
           'substrate, and crowning Bohmian mechanics as the physics '
           '(L10091\u201310098). The wager is on a rival\u2019s horse '
           'and is stated as such. <b>Item two:</b> objective-collapse '
           'parameter windows probed by optomechanics and '
           'interferometry would establish a physical rendering '
           'threshold at the layer the stratification assigns \u2014 '
           'with collapse theories physics-first and independent of '
           'idealism (L6155\u20136167). <b>Item three:</b> the '
           'classical-AI consciousness ceiling and the '
           'quantum-computing complexity wall \u2014 shared with '
           'biological naturalism and objective-reduction programs '
           'respectively, slow to resolve, and establishing at most the '
           'boundary story\u2019s negative claim (L3931\u20133939). The '
           'annex discipline of prior editions stands: no physicist is '
           'conscripted; every item\u2019s rival predictions are named; '
           'and the negative space is recorded \u2014 if '
           'non-equilibrium is never found and constrained ever tighter, '
           'the equilibrium account weakens toward metaphor, and the '
           'premise must say so rather than absorb the null result.')

    L.h2(story, '12.2 Program B: the decombination protocol '
                '(eliminative exchange)')

    L.body(story,
           'Program B is the Level-2 protocol, carried in full from the '
           'eliminative exchange\u2019s closing turn and stated here as '
           'the annex\u2019s operative specification. <b>The parameter '
           'map:</b> the model\u2019s coupling corresponds to effective '
           'connectivity, measurable by precision matrices on functional '
           'imaging; its stabilization term to neural gain and '
           'excitability; its baseline amplitude to resting oscillatory '
           'power; its inverse temperature to arousal and signal '
           'complexity, with psychedelic states known to raise the '
           'complexity measure; its integration threshold to '
           'integrated-information measures; its self-model quality to '
           'predictive-coding error and self-referential network '
           'activity (E2 T88). <b>The four domains, all with existing '
           'datasets:</b> psychedelics, where reduced coupling and '
           'raised noise should drive the system below the coherence '
           'threshold, merging domains and failing the integration '
           'criterion for large clusters; anesthesia, where deepening '
           'sedation should collapse the domain count toward one and '
           'fail integration at loss of consciousness; split-brain, '
           'where severed interhemispheric coupling should yield two '
           'independently satisfying domains with the callosum as their '
           'boundary; and dissociative-identity paradigms, where '
           'identity states should appear as distinct metastable '
           'domains with state-dependent boundaries and '
           'self-model scores that track the active state (E2 T88). '
           '<b>The controls:</b> phase-randomized, spatially shuffled, '
           'degree-matched, and shared-global-mode nulls, so that the '
           'criteria cannot be satisfied trivially. <b>The predictions '
           'table</b> of the source is adopted as written, and its '
           'closing condition is the program\u2019s law: joint '
           'satisfaction graduates the model to falsifiable theory; '
           'failure forces revision. What the program would not '
           'establish, stated with the same care: the Absolute; the '
           'phenomenal step; the ultimate bridge. It tests the boundary '
           'story \u2014 and only the boundary story, which is exactly '
           'why it can be real science under either ontology.')

    # ==================== 13. COMPARATIVE CONTEXT, UPDATED ====================
    L.h1(story, '13. Comparative Context, Updated')

    L.body(story,
           'The comparative map is updated with the trade-off structure '
           'the eliminative exchange made explicit \u2014 the first '
           'document in the corpus to rank the ultimate frameworks '
           'against each other on named criteria rather than arguing '
           'them one by one. Its central result is adopted as the '
           'map\u2019s organizing fact: no framework maximizes purity, '
           'closure, dissolution, empirical fertility, and personal '
           'meaning simultaneously, because the criteria trade off '
           'structurally \u2014 \u201cthe rankings are in tension by '
           'structure, not by accident\u201d (E2 T73). Classical theism '
           'ranks first for empirical fertility and personal meaning '
           'and pays with relation, distinction, and an unresolved '
           'hidden ledger. Radical non-dualism ranks first for logical '
           'purity and existential dissolution and pays with the '
           'reality of physics and the individual. The synthesized '
           'non-dual family \u2014 the audited premise\u2019s family '
           '\u2014 ranks second everywhere, which the exchange reads '
           'not as failure but as the price of refusing to choose, '
           'provided it is stated in the appearance-relation form '
           '(adjudications 14 and 17).')

    L.data_table(
        story,
        'Table 7. The premise among its rivals, under the trade-off '
        'criteria of the eliminative exchange.',
        ['Framework', 'World\u2019s status', 'Live hard problem', 'Relation '
         'to the audited premise'],
        [
            ['Classical theism',
             'Real, contingent, created \u2014 distinct but dependent',
             'Hiddenness; the quantity of permitted privation',
             'Strongest rival for empirical fertility and personal '
             'meaning; the premise refuses its relation and pays the '
             'ranked price'],
            ['Radical non-dualism (Advaita)',
             'Beginningless appearance; ignorance a lack, not a thing',
             'The subject of ignorance \u2014 dissolved, not solved',
             'The premise\u2019s identity at the ultimate level; the '
             'seam is shared'],
            ['Kashmiri Shaivism (svatantrya)',
             'Free self-manifestation; the world as self-display',
             'Why manifestation at all \u2014 answered from abundance, '
             'not necessity',
             'Source of the premise\u2019s strongest reconciliation '
             '(E2 T77\u2013T79)'],
            ['Analytic idealism (Kastrup)',
             'Extrinsic appearance of one transpersonal mind',
             'Decombination: dissociation without a law',
             'Same family; the premise adds stratification, topological '
             'priority, and now the S1\u2013S4 protocol'],
            ['Cosmopsychism',
             'Derivative local subjects from a cosmic subject',
             'Subject-collapse (decombination, mirrored)',
             'Closest cousin; the unity-of-experience argument favors '
             'this family over the micro family'],
            ['Russellian monism / panpsychism',
             'Matter with experiential intrinsic natures',
             'The combination problem',
             'Shares the intrinsic-nature diagnosis at lower '
             'ontological cost; micro-route instead of cosmic subject'],
            ['Brute fact / infinite regress / pure circularity',
             'Unexplained, deferred, or looped',
             'None \u2014 explanation stopped, deferred, or circular',
             'The eliminated family: unstable, self-undermining, or '
             'collapsing under the exchange\u2019s arguments'],
        ],
        [0.20, 0.26, 0.24, 0.30], font_size=8.2)

    L.body(story,
           'The premise\u2019s position in this map is now statable in '
           'one sentence that the corpus earned across two lines and '
           'four exchanges: an Advaita-style non-dualism argued through '
           'an eliminative program rather than scripture, disciplined '
           'by the via negativa\u2019s process ban, extended by '
           'stratification and topological priority, reconciled by '
           'svatantrya-and-perspective, voiced in the privation '
           'register\u2019s objective language, and holding a '
           'two-program empirical annex in which its oldest open '
           'problem runs on neutral mathematics with a written '
           'failure condition. Every clause of that sentence is '
           'defensible at its stated grade; none of it is a discovery '
           'about physics; and the sentence\u2019s honest name for '
           'itself is the one the ascent gave it \u2014 a scaffold '
           'beside a laboratory, not a temple on either.')

    # ==================== 14. GLOSSARY ====================
    L.h1(story, '14. Glossary of the Final Vocabulary')

    L.data_table(
        story,
        'Table 8. The ontological vocabulary (the language of eternal '
        'being), extended.',
        ['Term', 'Definition', 'Fixed at'],
        [
            ['The Absolute / the Singularity',
             'The one, timeless, spaceless, non-composite reality; pure '
             'actuality; all there is; not made of parts, bits, or '
             'quanta',
             'L5307\u20135372; v3L10421'],
            ['Appearance-relation',
             'The corrected form of the two-level structure: one '
             'reality appearing; the conventional is not a second '
             'reality and not nothing \u2014 rope and snake, water '
             'and wave, screen and movie',
             'E2 T74\u2013T75; adjudication 14'],
            ['The mode of objectivity',
             'The aspect under which the Absolute appears as the '
             'physical world; physics is its grammar \u2014 \u201cthe '
             'study of the ordered way the Absolute appears to itself '
             'under the mode of objectivity\u201d',
             'E2 T78'],
            ['The eliminative program',
             'The premise\u2019s argument-form: an exhaustive family of '
             'ultimate hypotheses eliminated under nine stated '
             'constraints; conditional throughout',
             'E2 T31, T47'],
            ['Grounded circularity',
             'Circular causality as a local, structural principle: '
             'horizontally closed loops, vertically dependent on the '
             'ground; never ultimate',
             'E2 T61\u2013T63'],
            ['Svatantrya / self-manifestation',
             'The Absolute\u2019s free self-display from abundance, not '
             'need; perspectives as modes of its self-knowledge',
             'E2 T77\u2013T79'],
            ['The candidate subject',
             'What the decombination model formally specifies: coherent '
             'metastable domains plus exact screening plus an '
             'intervention-validated self-model plus stable closure',
             'E2 T82'],
            ['S1\u2013S4',
             'The four operational criteria: dissociation (screening), '
             'integration (internal mutual information), self-modeling '
             '(predictive gain over a null), stable closure '
             '(contraction under intervention)',
             'E2 T82, T88'],
            ['The ultimate bridge',
             'The third problem of the taxonomy: why the Absolute gives '
             'rise to the experiential field at all \u2014 possibly '
             'impossible; the boundary of the program',
             'E3 T3; E2 T87 (Level 6)'],
            ['Topological priority',
             'The structural precedence of boundary over bulk, canvas '
             'over painting; the replacement for temporal causation at '
             'the fundamental level',
             'L11028\u201311086'],
            ['Quantum equilibrium',
             'The settled condition of a confined perspective in which '
             'the Born rule holds; non-equilibrium is the annex\u2019s '
             'principal observable',
             'L9988\u201310048'],
            ['The privation register',
             'The objective language for defect: darkness is absence of '
             'light; cold has no subject study in physics; evil is '
             'subjective, not a positive entity; defect is absence of '
             'due function \u2014 real as a hole, never a substance',
             'E2 T32\u2013T33; ch. 8'],
            ['The seam',
             'The boundary of discursive reason at the subject of '
             'ignorance: renamed across traditions (maya, '
             'anirvacaniya, the ultimate bridge), never closed',
             'E1 impasse; E2 T85; E3 T3'],
            ['Elevation (vs. immunization)',
             'A weakness is elevated when the corpus supplies a repair '
             'with failure conditions; immunization is the forbidden '
             're-labeling that makes the framework unable to lose',
             'The elevation protocol; R20'],
        ],
        [0.22, 0.56, 0.22], font_size=8.0)

    L.data_table(
        story,
        'Table 9. The pedagogical vocabulary (upaya; use and discard).',
        ['Term', 'Sanctioned use', 'Standing prohibition'],
        [
            ['Dream / dreaming',
             'To convey that the universe is appearance within mind \u2014 '
             'the metaphysical, not the skeptical, hypothesis',
             'Never as event or change of state; the Absolute does not '
             'begin or cease dreaming'],
            ['Creation / creator',
             'To introduce the premise to theistic audiences by contrast',
             'Never ontologically: no maker, no made, no outside'],
            ['Before / after / beginning',
             'To order exposition for time-bound readers',
             'Never about the Absolute or the manifold as such; the Big '
             'Bang is a boundary, not an event'],
            ['Limiting / self-limitation',
             'To gesture at the svatantrya reconciliation for audiences '
             'who know the lila literature',
             'Never as though the Absolute lacks, needs, or undergoes '
             'the limitation (E2 T69 trilemma)'],
            ['Defect / glitch / error',
             'To describe how anomalies appear to avatars',
             'Never about the Absolute; defects are avatar constructs, '
             'absences in the register\u2019s objective sense'],
            ['Level talk (\u201creal at its level\u201d)',
             'Shorthand, only when immediately paraphrased into the '
             'appearance-relation form',
             'Never as a metaphysical claim \u2014 the both-real '
             'reading is the banned contradiction (R17)'],
        ],
        [0.20, 0.40, 0.40], font_size=8.0)

    # ==================== APPENDIX A ====================
    L.h1(story, 'Appendix A. The Corpus Map and Completion Markers')

    L.body(story,
           'The appendix records every audited source, its verified '
           'size, and the completion marker by which line-level coverage '
           'was verified \u2014 the discipline the interlocutor\u2019s '
           'directives fixed and this edition extends to the two new '
           'exchanges. For the two dialogue lines and the recovered '
           'ascent, completion was verified in prior rounds and carried '
           'by their line-level reading documents; for the eliminative '
           'and taxonomy exchanges, the markers below were verified '
           'character-for-character in the recovered payloads this '
           'round.')

    L.data_table(
        story,
        'Table 10. The complete corpus: sources, sizes, and completion '
        'markers.',
        ['Source', 'Verified size', 'Completion marker / coverage'],
        [
            ['Qwen conversation one (share f30d7216)',
             '60 messages; 3,167 lines',
             'Read in full; canonical transcript and line-level reading '
             'on record'],
            ['Qwen conversation two (share 68292366)',
             '66 messages; 3,487 lines',
             'Read in full; line-level reading on record'],
            ['Qwen conversation three (share a6629bde)',
             '256 messages; 10,457 lines',
             'Read in full; line-level reading on record with its '
             'visible correction section'],
            ['The GLM dialogue (chat-Fundamental Higher Consciousness '
             'Premise.txt)',
             '130 turns; 11,088 lines',
             'Read in full across editions; the turn index of the third '
             'edition carries the map'],
            ['E1, the ascent (share ei9y81lsr98ujftn91)',
             '106 messages, 53 turns; 352,193 recovered content '
             'characters',
             'Ends \u201cIt is the scaffold, not the building\u2026 That '
             'is the most honest and useful answer I can give.\u201d '
             'Recovered from the damaged payload; verified'],
            ['E2, the eliminative exchange (share d56jfcwyyw3flhzrt1)',
             '176 messages, 88 turns; 1,294,295 payload characters',
             'Ends \u201cIf they are not, the model must be revised. '
             'That is the honest state of the art.\u201d Recovered '
             'whole; verified'],
            ['E3, the taxonomy exchange (share r9nkpwqs4uu5h169uf)',
             '6 messages, 3 turns',
             'Ends \u201cBut given the framework\u2019s starting '
             'assumption, the structural problem is the remaining hard '
             'problem.\u201d Verified'],
            ['The consolidation treatise (chat-universal consciousness '
             'audit+deepseek chat.txt)',
             '426 lines; 4 turns',
             'Ends with the Architecture of the Absolute\u2019s closing '
             'declaration; verified in the third edition'],
            ['The external audit file (deepseek auidt of universal '
             'consciousness.txt)',
             '473 lines',
             'Read in full in the third edition; carried'],
            ['The Steelman Audit (PDF)',
             '38 pages',
             'Extracted and read page-by-page this round'],
            ['The Trilogy Edition (PDF)',
             '28 pages',
             'Extracted and read page-by-page this round; its scope '
             'note corrected by this edition'],
            ['The second edition (PDF)',
             '33 pages',
             'Read in prior rounds; page-13 correction applied and '
             'verified'],
            ['The revised edition (PDF)',
             '45 pages',
             'Read in prior rounds; its five-party count corrected by '
             'Table 1'],
        ],
        [0.30, 0.24, 0.46], font_size=8.0)

    L.body(story,
           'One entry in the map closes the edition where the corpus '
           'itself closes. The eliminative exchange\u2019s final turn '
           'hands the framework a sentence it had never owned before '
           '\u2014 a written condition under which its oldest open '
           'problem\u2019s instrument stands or falls \u2014 and does '
           'so in the register every audit has demanded: neutral, '
           'graded, and falsifiable. The consolidated premise carries '
           'that sentence forward as its own standing obligation, '
           'together with everything this edition has strengthened and '
           'everything it has refused to pretend was strengthened. The '
           'audit\u2019s work ends where the corpus\u2019s honest work '
           'has always ended: with the bet stated, the prices named, '
           'the instruments specified, and the seam carried openly '
           '\u2014 a coherent bet, held openly, about the one unchanging '
           'reality in which all of this, including this audit and its '
           'corrections, appears.')
