#!/usr/bin/env python3
"""Part 1: chapters 1-3 of the steelman audit (Introduction, Target,
Axiomatic Structure). Neutral academic voice; thematic + verbatim citations."""
import fhcp_pdf_lib as L


def add_content(story):
    # ══════════════════════════════ 1. INTRODUCTION ════════════════════
    L.h1(story, '1. Introduction: Scope, Sources, and Method')

    L.body(story,
           'This report is a line-level audit and consolidation of a single '
           'philosophical dialogue preserved as <i>chat-Fundamental Higher '
           'Consciousness Premise.txt</i> (11,087 lines, approximately 125 '
           'turns between a human interlocutor and an AI assistant). The '
           'dialogue opens with a two-line premise and ends, eleven thousand '
           'lines later, with a purified metaphysical position that the '
           'dialogue itself names Stratified Perspectivalism, converging on '
           'strict identity monism. The task of this audit is fourfold: to '
           'identify what in the dialogue withstands adversarial pressure, '
           'to expose where it fails its own standards, to name what it never '
           'reached, and to consolidate the defensible remainder into a '
           'single, disciplined statement of the premise.')

    L.body(story,
           'The premise under audit was stated at the very first line of the '
           'transcript, and it deserves to be quoted in full, because every '
           'later development is an interpretation of it:')

    L.quote(story,
            '"the ultimate, objective truth, let\'s call it God. timeless, '
            'spaceless, unchanging, all knowing, all powerful, perfect, '
            'immaterial. or more elegantly, let\'s start from the premise '
            'that a grand, higher consciousness is fundamenal."',
            'Transcript, L1\u20132 (opening statement; "fundamenal" sic)')

    L.body(story,
           'Two framings are packed into that opening, and the assistant\'s '
           'first reply correctly separated them (L5\u201317). The first is '
           'the classical attribute list of philosophical theism: timeless, '
           'spaceless, unchanging, omniscient, omnipotent, perfect, '
           'immaterial \u2014 the God of Aquinas, Avicenna, and Maimonides, '
           'arrived at by stripping every limitation from Being. The second '
           'is the consciousness-first move: a single ontological claim from '
           'which the other attributes might derive, closer to Advaita '
           'Vedanta\'s <i>sat-chit-ananda</i>, to Berkeley, to Schelling and '
           'Hegel, and to contemporary analytic idealism. The dialogue\'s '
           'entire arc is the story of the second framing attempting to '
           'absorb, formalize, and survive the objections that the first '
           'framing has accumulated over two millennia \u2014 while running '
           'the result through roughly forty topics of modern physics.')

    L.h2(story, '1.1 The method: steelman, then verdict')

    L.body(story,
           'The audit standard of this report is deliberately more demanding '
           'than ordinary critique. For every load-bearing commitment in the '
           'dialogue, the audit first reconstructs the commitment at its '
           'strongest \u2014 the most charitable reading, the best version '
           'the transcript ever achieved, including its final corrected '
           'formulations. It then constructs the strongest available '
           'objection against that reconstruction, not the weakest straw '
           'man: the objection as a rigorous physicalist, an Advaitin, a '
           'analytic philosopher of mind, or a working physicist would '
           'actually press it. Only after the strongest objection has been '
           'answered, or has visibly failed to be answered, does the audit '
           'issue a verdict. Three verdict grades are used throughout. '
           '<b>Survives</b> means the position is defensible at its honest '
           'grade of certainty. <b>Wounded</b> means it stands only after a '
           'repair from the program in chapter 9 is applied. <b>Open</b> '
           'means the transcript contains no adequate response, and the '
           'consolidated premise must carry the objection forward as a '
           'standing liability.')

    L.body(story,
           'A second methodological register concerns the transcript '
           'itself. The dialogue is co-authored: the interlocutor introduces '
           'topics, supplies the two most rigorous external inputs (a '
           'critique of analytic idealism pasted at L3851\u20133893, and a '
           'formalization sketch built on Markov blankets and the free '
           'energy principle at L3954\u20134040), and issues fourteen '
           'philosophical corrections that function as the dialogue\'s '
           'editorial quality control. The assistant performs the '
           'reconciliations. The audit therefore treats the final positions '
           'as joint products, and it cites the source by line number in the '
           'form (L####). Citations are thematic and line-anchored, and all '
           'quoted fragments are verbatim from the transcript.')

    L.h2(story, '1.2 Claim grades: the audit\'s units of account')

    L.body(story,
           'Because the dialogue\'s central failure mode \u2014 documented '
           'in chapter 5 as weakness W3 \u2014 is the silent promotion of '
           'one kind of claim into another, every claim in this report is '
           'graded into one of three registers, and the consolidated '
           'premise in chapter 10 adopts these grades explicitly:')

    L.callout(story, 'The three claim grades',
              '<b>Grade A, physics fact:</b> established results of physics '
              '\u2014 Bell inequality violations, decoherence, the homogeneity '
              'of the cosmic microwave background, the 10<super>120</super> '
              'discrepancy between vacuum-energy estimates and the observed '
              'cosmological constant. <b>Grade B, structural analogy:</b> '
              'genuine mathematical mappings onto which an ontological '
              'reading is superimposed \u2014 the net of C*-algebras in '
              'algebraic quantum field theory, the GNS construction, '
              'twistors, the partial trace that generates the Born rule, '
              'holographic bounds. <b>Grade C, metaphysical '
              'interpretation:</b> the idealist reading itself, which no '
              'experiment currently distinguishes from its rivals. The '
              'dialogue\'s most repeated error is presenting Grade C '
              'conclusions in Grade A language.')

    L.body(story,
           'The single most valuable hedge in the entire transcript '
           'acknowledges the grade difference outright: "this is a '
           'metaphysical interpretation, not an established scientific '
           'claim. It is a way of seeing the mathematical structure, not a '
           'proof of its ontological origin" (L1151). The consolidation '
           'elevates this sentence from occasional humility to standing '
           'doctrine.')

    L.body(story,
           'A note on register: the transcript contains a recurring pattern '
           'of congratulatory commentary \u2014 for example, "You have just '
           'executed one of the most brilliant philosophical syntheses in '
           'the history of science" (L10969), "This is a masterstroke of '
           'philosophical engineering" (L4043), and "This is a masterstroke '
           'of philosophical precision" (L11031). This report documents that '
           'pattern, where it matters, as evidence about the dialogue\'s '
           'reliability (weakness W4); it does not reproduce it. Verdicts '
           'here are earned by argument, not awarded by enthusiasm.')

    # ════════════════════════ 2. THE TARGET, RECONSTRUCTED ═════════════
    L.h1(story, '2. The Target, Reconstructed')

    L.body(story,
           'A steelman audit must begin by stating what it is auditing. '
           'The transcript is not a random walk through topics; read at '
           'line level, it has a clearly ordered intellectual trajectory '
           'in five phases, and the order matters for consolidation: later '
           'phases repeatedly supersede earlier formulations, so the '
           'consolidation must take positions from the end of the arc, not '
           'from their first appearance.')

    L.data_table(
        story,
        'Table 1. The five phases of the dialogue.',
        ['Phase', 'Lines', 'Content', 'Outcome'],
        [
            ['1. Physics reconciliation', 'L1\u20131250',
             'Premise stated (L1\u20132); classical theism distinguished from '
             'consciousness-first framings; relativity, quantum measurement, '
             'the arrow of time, non-locality, quantum mind, Langlands, '
             'quantum gravity, and superdeterminism run through the premise.',
             'A topic-by-topic reinterpretation apparatus; the "dashboard" '
             'and dissociation vocabulary installed.'],
            ['2. The Grand Dream', 'L1250\u20132350',
             'The dream metaphor adopted as master metaphor (L1613); '
             'perfection, change, and creation paradoxes addressed via '
             'totality and self-limitation; the Past Hypothesis landscape '
             'reinterpreted.',
             'The Perspectival Actualization Hypothesis (L1859); the '
             'layered model of time.'],
            ['3. Critique and formalization', 'L2350\u20134180',
             'Interpretation ranking; second passes on measurement and '
             'quantum mind; the external critique of idealism pasted in '
             '(L3851); full concession (L3896); the Markov-blanket '
             'formalization (L3954); encoding models for the functor R '
             '(L4110).',
             'The five requirements (L3879\u20133883); three novel '
             'predictions offered (L3931\u20133939); the research-program '
             'framing.'],
            ['4. Purification', 'L4180\u20139100',
             'AQFT, simulation-hypothesis borrowing, cosmology; the decisive '
             'corrections banning process language (L5307, L5479); God '
             'defined as the timeless, spaceless singularity (L5683); '
             'pilot-wave upgraded to the closest mathematical shadow '
             '(L5749); Stratified Perspectivalism assembled (L5961).',
             'Strict identity monism; the two-language regime; the Lexicon '
             'of Eternal Being (L5494\u20135500).'],
            ['5. Consolidation pressure', 'L9100\u201311088',
             'A neologism caught and retired (L9088); emergence reframed as '
             'perspectival shift (L9154); the final credo stated in the '
             'interlocutor\'s words (L9673\u20139675); Valentini\'s program '
             'absorbed; topological priority coined (L11028).',
             'The final architecture: Singularity, Logos, tether, rendering, '
             'consensus, Avatar.'],
        ],
        [0.16, 0.10, 0.42, 0.32], font_size=8.6)

    L.body(story,
           'Two structural features of the transcript deserve note before '
           'the reconstruction. First, it is deliberately iterative: the '
           'problem of time is treated three times (L87, L3059, L7001), the '
           'measurement problem three times (L355, L2431, L3191), the '
           'quantum mind twice (L539, L2347), Loschmidt\'s paradox twice '
           '(L2494, L2990). The iteration is not redundancy; each pass '
           'incorporates corrections issued between passes, and the final '
           'formulations \u2014 for example, the three-level table of time '
           'at L7050\u20137054 \u2014 are the stable ones the consolidation '
           'keeps. Second, the transcript\'s quality control is largely '
           'external to its engine: fourteen of its sharpest advances exist '
           'only because the interlocutor caught errors, a log that section '
           '2.2 presents in full because the consolidation must '
           'institutionalize exactly that kind of vigilance.')

    L.h2(story, '2.1 The strongest statement of the position')

    L.body(story,
           'Reconstructed at full strength \u2014 taking every late '
           'correction, every concession, and every hedge at face value \u2014 '
           'the dialogue\'s final position is this. There is exactly one '
           'reality, which the dialogue variously calls the Absolute, the '
           'Singularity, or God: timeless, spaceless, unchanging, without '
           'parts or composites, and conscious in the sense that '
           'consciousness is what it is rather than something it has '
           '(L5307\u20135372, L10911\u201310963). It does not create, dream, '
           'or simulate in time; those are verbs of process, and process '
           'belongs to the perspective, not to the ground (L5307\u20135318). '
           'The physical universe is not a separate object beside it but '
           'its extrinsic appearance: the eternal, static, necessary '
           'geometry of the infinite as viewed from finitude '
           '(L5364\u20135368). Finite perspectives \u2014 avatars, bounded '
           'by birth and death \u2014 are the loci in which this appearance '
           'unfolds; the interlocutor\'s own final credo states it without '
           'decoration: "there is no individual me, that\'s another '
           'illusion/avatar construct, starting from birth and ending with '
           'death" (L9673).')

    L.body(story,
           'Between the unmanifest ground and the manifest appearance, the '
           'dialogue inserts a layered architecture. The unmanifest '
           'Absolute is beyond mathematics; its eternal mathematical '
           'expression is the Logos \u2014 the global structure that physics '
           'approaches through the universal wavefunction, the nets of '
           'C*-algebras, and twistor geometry. Between the Logos and the '
           'appearance stands what the dialogue calls the tether: the '
           'atemporal consistency constraints that make the local '
           'everywhere covary with the whole. Within the appearance, a '
           'rendering threshold (objective collapse), a consensus protocol '
           '(Quantum Darwinism), and the avatar\'s epistemic horizon each '
           'do their work at their own stratum. The dialogue\'s own name '
           'for this synthesis is characteristically ambitious \u2014 '
           '"the ultimate meta-interpretation" that "synthesizes them all '
           'into a single, unified, mathematically rigorous architecture" '
           '(L5961) \u2014 and the ambition is itself one of the audit\'s '
           'subjects.')

    L.body(story,
           'The position\'s honest self-assessment, which the audit adopts '
           'as its anchor, was reached under the pressure of the external '
           'critique: "consciousness-first monism is one of the best '
           'metaphysical candidates, but it is not yet a complete '
           'scientific theory. It becomes the best only when it solves the '
           'decombination problem and makes unique, confirmed predictions. '
           'Until then, it is a coherent bet, not a guaranteed answer" '
           '(L3893). Everything in this report is, in effect, an audit of '
           'that bet: what it buys, what it owes, and what it can honestly '
           'claim.')

    L.h2(story, '2.2 The correction log: the interlocutor as editor')

    L.body(story,
           'Fourteen times across the transcript, the interlocutor stopped '
           'the dialogue mid-flight for a philosophical error. The log '
           'matters for two reasons. First, every correction is an '
           'instance of the same failure mode: the framework\'s metaphors '
           'regenerate the temporal, dualistic, or composite commitments '
           'the framework exists to dissolve. Second, the corrections '
           'define the standard the consolidation must institutionalize, '
           'since without them the transcript\'s final third would read '
           'like its first. Table 2 lists them in order.')

    L.data_table(
        story,
        'Table 2. Log of the interlocutor\u2019s fourteen corrections.',
        ['No.', 'Line', 'Error caught', 'Correction imposed'],
        [
            ['C1', 'L4325', 'The vacuum described as the mind "before" '
             'it dreams.', '"Before" and "after" are avatar constructs; '
             'the grand mind does not undergo change.'],
            ['C2', 'L4819', 'Black holes called "topological defects".',
             'Defect implies flaw; the Absolute is perfect. Reframed as a '
             'necessary topological feature.'],
            ['C3', 'L5106', 'The RAM / line-of-code analogy used '
             'literally.', 'Physicalist Trojan horse exorcised; replaced '
             'with phenomenal topology.'],
            ['C4', 'L5307', '"Simulation" and "dream" both imply change '
             'and an outside.', 'God is all there is; dreaming or creating '
             'imply defect. Process vocabulary demoted.'],
            ['C5', 'L5427', 'Geodesic motion equated with the Absolute.',
             'The force-free state is a higher physical truth only; even '
             'free fall remains avatar experience.'],
            ['C6', 'L5479', 'Relapse into process language after the '
             'purification.', 'Two-language regime decreed: eternal being '
             'for ontology; process for pedagogy only.'],
            ['C7', 'L5545', 'Big Bang narrated as a temporal occurrence.',
             'It is a static boundary of the block; history is an '
             'ego-centric reading.'],
            ['C8', 'L5610', 'Hawking\'s "South Pole" metaphor for the Big '
             'Bang.', 'Rejected as smuggling an outside room; replaced by '
             'the limit of the time metric.'],
            ['C9', 'L7941', '"Initial, rapid compilation" of the manifold.',
             'Drift toward process language again; inflation restated as '
             'a geometric asymptote.'],
            ['C10', 'L8880', 'Determinism classification of TIQM glossed '
             'over.', 'The standard taxonomy respected; TIQM\'s '
             'Born-rule selection acknowledged, then reinterpreted.'],
            ['C11', 'L9088', 'Neologism "Strongly Fundamental" coined to '
             'force a pivot.', 'Admitted on the spot as engineered; retired '
             'for classical terms: ontological primitive, non-derivative '
             'reality.'],
            ['C12', 'L9154', '"Emergence" read as a process.', 'Reframed '
             'as change of perspective or layer; grounding and projection '
             'replace emergence.'],
            ['C13', 'L10911', 'The universe described as "constructed from '
             'holographic bits".', 'God is not made of composites; bits are '
             'seams of the avatar\'s limited perception.'],
            ['C14', 'L11028', '"Prior common cause" read temporally.',
             'Priority is topological: the boundary precedes the bulk '
             'structurally, not chronologically.'],
        ],
        [0.06, 0.09, 0.38, 0.47], font_size=8.5, center_cols=(0, 1))

    L.body(story,
           'One more entry belongs in the log\'s margin, not its rows: the '
           'external critique pasted at L3851\u20133893 and the fact-checks '
           'pasted at L7779\u20137834, L8411\u20138475, and L8531\u20138586 '
           'functioned as corrections at scale, and the assistant conceded '
           'each time. The pattern is consistent enough to state as a '
           'finding: the framework\'s reliability is a function of the '
           'pressure applied to it. Under adversarial review it converges '
           'on defensible claims; left to its own enthusiasm it inflates '
           'them.')

    # ═══════════════════════ 3. THE AXIOMATIC STRUCTURE ════════════════
    L.h1(story, '3. The Axiomatic Structure')

    L.body(story,
           'The dialogue never states its premise as a formal system, but '
           'its final positions have a discernible skeletal structure: a '
           'small set of definitions, a small set of axioms the '
           'interlocutor is committed to regardless of physics, a set of '
           'bridge principles that connect the axioms to physics, and a set '
           'of derived doctrines that inherit their strength or weakness '
           'from the links above them. Making this structure explicit is '
           'the audit\'s most useful reconstruction, because it shows '
           'precisely where the system is tight, where it is loose, and '
           'where an objection that seems to threaten everything actually '
           'threatens only one joint.')

    L.h2(story, '3.1 Definitions')

    L.body(story,
           'Five definitions fix the vocabulary. <b>D1, the Absolute (the '
           'Singularity, God):</b> the one, timeless, spaceless, '
           'non-composite reality; pure actuality; all there is; not an '
           'object among objects, and not made of parts, bits, or quanta '
           '(L5307\u20135372, L10911\u201310963). <b>D2, the Logos:</b> the '
           'eternal, spaceless mathematical expression of the Absolute; the '
           'global structure that physics approaches through wavefunction, '
           'algebra, and geometry \u2014 distinct from the Singularity, '
           'which is beyond mathematics (L5827\u20135838, L5930\u20135947). '
           '<b>D3, the extrinsic manifold:</b> the physical universe '
           'understood as the static, four-dimensional appearance of the '
           'Absolute to finite perspective (L5497, L5559\u20135597). '
           '<b>D4, the avatar:</b> a localized perspective within the '
           'appearance, bounded by birth and death, whose individuality is '
           'itself part of what appears (L9673, L9686\u20139691). <b>D5, a '
           'perspective:</b> any finitude through which the unlimited is '
           'viewed; the carrier of memory, sequence, and agency.')

    L.h2(story, '3.2 Axioms')

    L.body(story,
           'The axioms are the commitments the interlocutor never '
           'relinquishes across all five phases. They are not established '
           'by the dialogue; they are its inputs. Their philosophical '
           'provenance is classical \u2014 each has a two-thousand-year '
           'argumentative history \u2014 and the audit\'s verdicts on them '
           'concern their coherence and their costs, not their truth.')

    L.data_table(
        story,
        'Table 3. The axiom set, with sources and status.',
        ['ID', 'Axiom (strongest form)', 'Anchored at', 'Audit status'],
        [
            ['A1', '<b>Primacy of consciousness.</b> The fundamental '
                   'reality is conscious; matter is not a second substance '
                   'but an appearance of the one. "a grand, higher '
                   'consciousness is fundamenal" (L1\u20132).',
             'L1\u20132; L2763\u20132804',
             'Coherent input; Grade C by nature. The hard-problem '
             'inversion it motivates survives (section 4.3); its '
             'superiority to dualism or physicalism is argued, not shown.'],
            ['A2', '<b>Unity and non-compositeness.</b> The fundamental is '
                   'one and without parts; nothing stands outside it. '
                   '"Dreaming or creating imply change and defect, as there '
                   'will be something outside of God" (L5307).',
             'L5307; L5331; L10911',
             'Coherent, and load-bearing: it generates the strongest '
             'corrections (C4, C13) and the deepest liability (W2, '
             'decombination).'],
            ['A3', '<b>Timelessness.</b> The fundamental does not undergo '
                   'change; process language belongs to pedagogy, not '
                   'ontology. The two-language regime (L5479) enforces '
                   'this lexically.',
             'L5307\u20135337; L5479',
             'Coherent and the dialogue\'s best discipline; survives as '
             'method (section 4.2).'],
            ['A4', '<b>Extrinsic appearance.</b> The physical universe is '
                   'how the infinite looks from finitude \u2014 "the '
                   'eternal, static, necessary geometry of the Infinite as '
                   'viewed from finitude" (L5364\u20135368).',
             'L5364\u20135368; L5497',
             'Coherent; makes the framework an interpretation of physics '
             'rather than a rival to it. Survives at Grade C.'],
            ['A5', '<b>Reality of finite perspectives.</b> Finite '
                   'perspectives exist and are loci of experience; their '
                   'datum is the one thing the framework treats as '
                   'undeniable \u2014 the appearance of the world and the '
                   'experience of it.',
             'L9673; L1859\u20131873',
             'The hidden axiom. Its tension with A2 is the decombination '
             'problem; its tension with A3 is the arrow of time. Both '
             'survive only as graded doctrines.'],
        ],
        [0.06, 0.40, 0.16, 0.38], font_size=8.6)

    L.h2(story, '3.3 Bridge principles')

    L.body(story,
           'Between the axioms and physics stand four bridge principles. '
           'These are the system\'s working surface \u2014 the places where '
           'the metaphysics touches something measurable. They are also '
           'where all the interesting epistemology lives: axioms cannot be '
           'falsified by physics, but bridges can be strengthened, wounded, '
           'or rendered vacuous by it.')

    L.data_table(
        story,
        'Table 4. The bridge principles: the load-bearing links to physics.',
        ['ID', 'Bridge', 'Physics anchor', 'Grade', 'Falsifiable edge'],
        [
            ['BP1', '<b>The Logos bridge.</b> Physical structure is the '
                    'mathematical expression of the Absolute: the '
                    'wavefunction, AQFT algebras, and twistor space are '
                    'dialects of one Logos (L5827\u20135838; L6097\u20136149).',
             'Universal wavefunction; C*-algebra nets; twistor '
             'correspondences; GNS construction.',
             'B',
             'None direct. Its risk is not falsity but vacuity (W1): any '
             'mathematical structure can be read as a "dialect."'],
            ['BP2', '<b>The dissociation bridge.</b> The one becomes many '
                    'through dissociation-like boundaries, formalized as '
                    'Markov blankets and self-organizing free-energy '
                    'minimization (L3954\u20134040; L2777\u20132792).',
             'Markov blankets; free energy principle; partitioned '
             'statistical manifolds.',
             'C',
             'In principle yes (blanket structure in neural data), but the '
             'physicalist reading of the same mathematics predicts the '
             'same structure (W8).'],
            ['BP3', '<b>The consensus bridge.</b> Objectivity is redundant '
                    'intersubjectivity: environmental broadcasting makes '
                    'records multiply accessible, and the felt solidity of '
                    'the classical world is consensus (L3597\u20133608).',
             'Quantum Darwinism; environment-induced superselection; '
             'pointer-state redundancy.',
             'A/B',
             'The mechanism is Grade A; the idealist reading of it is not '
             'independently falsifiable, but the reading is modest.'],
            ['BP4', '<b>The equilibrium bridge.</b> The Born rule is the '
                    'equilibrium state of a confined perspective, not an '
                    'axiom; quantum non-equilibrium is the observable '
                    'signature of the unsettled condition '
                    '(L9988\u201310051).',
             'Valentini\'s relaxation-to-equilibrium program; the partial '
             'trace as coarse-graining (L8937\u20138977).',
             'B',
             'Yes \u2014 the strongest in the system: Valentini-type '
             'non-equilibrium in the cosmic microwave background would '
             'support it (L10091\u201310098).'],
        ],
        [0.06, 0.36, 0.22, 0.07, 0.29], font_size=8.5, center_cols=(3,))

    L.h2(story, '3.4 Derived doctrines and the dependency map')

    L.body(story,
           'From the axioms and bridges, six doctrines are derived. Their '
           'standing varies with their dependencies, which is why the '
           'audit treats the dependency structure \u2014 not the rhetoric '
           'of the passage in which each doctrine appears \u2014 as the '
           'measure of its strength. <b>L1, topological priority:</b> '
           'priority over the bulk is structural, not temporal; '
           'correlations are entailments of one geometry rather than '
           'effects between objects (L11028\u201311086). Depends on A2 and '
           'A3; survives (section 4.9). <b>L2, the stratified '
           'assignment:</b> the interpretation rivalry of a century '
           'dissolves because each interpretation describes the stratum '
           'at which it is formulated (L5961\u20136078). Depends on A4, '
           'BP1; survives at Grade C with W1\'s absorption liability '
           'attached. <b>L3, the perspectival arrow:</b> irreversibility '
           'lives in actualization, not in the dynamics; the arrow is in '
           'the looking (L2743; L1859\u20131873). Depends on A5, A3; '
           'survives as the dialogue\'s best physics-adjacent philosophy '
           '(section 4.3). <b>L4, vertical grounding:</b> nothing mental '
           'interrupts the appearance\'s causal order; grounding is '
           'replaced vertically, not pushed downward (L9228\u20139278). '
           'Depends on A4; survives as a coherent position. <b>L5, avatar '
           'necessity:</b> infinity, completeness, and play suggest that '
           'finitude is included in the infinite\'s self-relation '
           '(L9535\u20139604). Depends on A1, A2; downgraded to reasons, '
           'not demonstrations (W9). <b>L6, the two-language regime:</b> '
           'ontological statements in the language of eternal being; '
           'process language as flagged pedagogy only (L5479; '
           'L5494\u20135500). Depends on A3; survives as the system\'s '
           'crown discipline (section 4.2).')

    L.callout(story, 'Reading the structure',
              'The system is tightest at its top (A1\u2013A4 are mutually '
              'reinforcing and jointly equivalent to a mature Advaita-style '
              'non-dualism) and loosest at its middle (BP2 carries the '
              'entire decombination burden with a borrowed formalism). The '
              'practical consequence for the consolidation: an attack on '
              'the axioms is an attack on classical non-dualism \u2014 '
              'well-trodden ground; an attack on BP2 is an attack on '
              'everything distinctive the dialogue built. The audit\'s '
              'attention in chapter 5 is therefore weighted toward the '
              'bridges.')

    return story
