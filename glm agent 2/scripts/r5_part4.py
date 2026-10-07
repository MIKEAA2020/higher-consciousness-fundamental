#!/usr/bin/env python3
"""Fifth Edition (Anchored Edition), Part 4: chapters 7-9.

Chapter 7 records the two exported critiques as first-class sources.
Chapter 8 re-scores the weaknesses under anchoring. Chapter 9 settles the
four decisions the Claude audit placed before the interlocutor.
"""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 7. THE TWO EXPORTED CRITIQUES ====================
    L.h1(story, '7. The Two Exported Critiques, Recorded')

    L.h2(story, '7.1 What the files are, and what they were')

    L.body(story,
           'The two files whose provenance chapter 2.2 establishes are '
           'the contingency argument\u2019s own audit trail. The first '
           'critiques the argument\u2019s first draft; the second '
           'critiques the revision the first critique produced; and the '
           'DeepSeek exchange in which they were re-attached then '
           'conceded their force and issued the corrected steelman the '
           'fourth edition consolidated. Until this round the corpus '
           'possessed only the concession and the corrected steelman; '
           'the critiques themselves were unread as sources. Recording '
           'them closes the last provenance gap in the contingency '
           'thread, and it does so at the moment the thread matters '
           'most, because the Claude audit\u2019s gap findings (the '
           'avatar-necessity proof, the undefined bridge relation) and '
           'the critiques\u2019 findings (the over-reaching conclusion, '
           'the contestable premises) are two attacks on the same '
           'theological culmination from two different directions.')

    L.h2(story, '7.2 The first critique: \u201cNot conclusively\u201d')

    L.body(story,
           'The first file\u2019s seven vulnerabilities decompose into '
           'three that the consolidated editions had already absorbed '
           'and four that sharpen the grading. Already absorbed: the '
           'strong Principle of Sufficient Reason is a substantive '
           'premise, not a theorem (the corpus\u2019s A-tier now carries '
           'it as a stated premise with its rejection priced); the '
           'rejection of brute fact and infinite regress requires '
           'argument, not dissatisfaction (the rivals table prices both '
           'as standing alternatives); and the conclusion\u2019s '
           'property list outruns its premises (the conditional core). '
           'Sharpening: the dichotomy of premise two is false \u2014 an '
           'external ground need not be dependent, and the real '
           'trichotomy is dependent explanation, brute totality, or '
           'necessary termination; \u201cself-existent\u201d does not '
           'immediately mean essence-entails-existence without further '
           'modal premises; the move from physics\u2019 failure to '
           'entail existence to physical reality\u2019s contingency is '
           'a category shift (a theory\u2019s not entailing its '
           'subject\u2019s necessity is an epistemic fact about '
           'theories); and the category correction \u2014 physicalism '
           'is a doctrine, not an entity, so the conclusion must read '
           '\u201cfundamental physical reality cannot be the ultimate '
           'self-existent ground\u201d \u2014 is adopted verbatim into '
           'the axiom statement. The file\u2019s own stronger '
           'formulation, six steps ending at a ground that is not '
           'physical \u201cin the same dependent sense,\u201d is '
           'adopted as the thesis\u2019s official reading.')

    L.h2(story, '7.3 The second critique: \u201cSubstantially '
                'stronger, but it still overstates\u201d')

    L.body(story,
           'The second file\u2019s six issues are the argument\u2019s '
           'full bill of undemonstrated steps, and the edition adopts '
           'them as the grading rubric for the necessary-ground thesis. '
           'One: individual contingency does not aggregate to total '
           'contingency \u2014 the clean premise is \u201cat least one '
           'contingent concrete being exists.\u201d Two: the restricted '
           'PSR is legitimate but substantive; defining contingency as '
           'not-self-explanatory does not itself prove external '
           'explanation, because lacking an internal explanation is '
           'compatible with having no sufficient explanation at all '
           '\u2014 the PSR rules that out, the definition does not. '
           'Three: the anti-regress argument must be stated as the '
           'stronger principle the file formulates \u2014 no collection '
           'composed entirely of derivative grounds can provide a '
           'non-derivative ground \u2014 rather than as the '
           'lender/borrower analogy, and the essentially-ordered-series '
           'argument and the whole-series argument must be kept '
           'distinct, the second risking a composition fallacy unless '
           'the totality\u2019s own contingency is established. Four: '
           'the immediate conclusion is a non-derivative ground, not a '
           'being whose essence is existence \u2014 that requires the '
           'essence/existence distinction and a modal bridge. Five: '
           'necessity does not entail pure actuality, composition does '
           'not entail contingency without further premises, limitation '
           'is not equivalent to contingency, immateriality needs the '
           'argument that matter involves composition and potency, and '
           '\u201ceternal\u201d must disambiguate timeless from '
           'everlasting. Six: uniqueness requires a separate '
           'individuation argument. The file\u2019s eight-step '
           'defensible core, and its closing verdict \u2014 valid '
           'conditionally; essence-as-existence, pure actuality, '
           'simplicity, immateriality, eternity, and uniqueness not yet '
           'demonstrated; intellect, will, omniscience, omnipotence, '
           'and perfect goodness not established by the core \u2014 is '
           'now the thesis\u2019s standing grade.')

    L.h2(story, '7.4 Convergence with the consolidated core')

    L.data_table(
        story,
        'Table 7.1. The contingency thesis, graded against the two '
        'files\u2019 rubric.',
        ['Thesis component', 'Grade under the files\u2019 rubric',
         'Status tag'],
        [
            ['At least one contingent concrete being exists',
             'Granted (the files\u2019 corrected first premise)',
             'Premise'],
            ['Every contingent concrete being has a sufficient '
             'ontological ground (restricted PSR)',
             'Substantive, contestable; its rejection is priced '
             '(brute-fact alternative)',
             'Premise'],
            ['No collection of entirely derivative grounds can '
             'constitute a complete ground',
             'The corrected anti-regress principle; stronger than the '
             'analogy; still disputed',
             'Premise'],
            ['Therefore a non-derivative ground of contingent reality '
             'exists',
             'Valid conditionally on the three premises \u2014 the '
             'files\u2019 and the exchanges\u2019 joint verdict',
             'Derived'],
            ['The ground is not physical in the same dependent sense',
             'Follows if physical reality belongs to the contingent '
             'totality; the category-corrected reading',
             'Derived'],
            ['Its essence is existence; it is pure actuality, simple, '
             'immaterial, timeless, unique',
             'Requires the classical essence/existence and act/potency '
             'frameworks plus an individuation argument \u2014 each '
             'undemonstrated by the core',
             'Interpretive Mapping'],
            ['It is intellect, will, omniscient, omnipotent, perfectly '
             'good \u2014 the God of classical theism',
             'Requires still further premises; the files grade it '
             'beyond the argument',
             'Speculation'],
        ],
        [0.34, 0.42, 0.24])

    L.body(story,
           'The convergence finding is that the consolidated editions '
           'had already arrived where the files point: the conditional '
           'core, the priced brute-fact alternative, the two-level '
           'split\u2019s separation of worldhood entailment from '
           'this-world necessity, and the demotion of the divine-'
           'property extensions. What the verbatim files add is the '
           'discipline of the rubric itself \u2014 a checklist that '
           'any future restatement of the contingency thesis must clear '
           'line by line. The rubric is therefore recorded as doctrine '
           'in Table 7.1, and the two files enter the corpus map as '
           'auditing party twelve.')

    # ==================== 8. WEAKNESSES, RE-SCORED ====================
    L.h1(story, '8. Weaknesses, Re-scored Under Anchoring')

    L.h2(story, '8.1 What the anchors change')

    L.body(story,
           'The weakness register of the fourth edition carried the '
           'decombination gap as its largest entry, scored as elevated '
           'but conjectural. The anchors change that score in one '
           'direction only: the four domains now have verified '
           'findings, instruments, and failure conditions, so the '
           'program\u2019s standing is no longer promissory. They do '
           'not touch the register\u2019s other entries, and the '
           'edition is careful not to let anchoring launder them: the '
           'subject of ignorance, the simplicity-versus-compositionality '
           'tension, the quantity of privation, and the immunization '
           'pressure of stratification all remain open, each with its '
           'carrier forward from the prior editions. The one score that '
           'moves in the other direction is the anesthesia fork, below '
           '\u2014 a contradiction the Claude audit surfaced and the '
           'corpus had never stated.')

    L.h2(story, '8.2 The anesthesia fork, stated')

    L.body(story,
           'The interlocutor\u2019s formalization turn predicted that '
           'under anesthesia the idealist reading is \u201closs of the '
           'boundary, so experience ceases even if some local '
           'processing continues\u201d (L4006); the assistant\u2019s '
           'reply held that \u201cthe boundary becomes too rigid or '
           'fragmented, so the alter\u2019s access to the environment '
           'is severed (loss of reportability), but the fundamental '
           'field remains\u201d (L4081). These are different empirical '
           'claims: cessation of experience versus severance of access '
           'with persistence of the field. The fork is genuine, and the '
           'consolidation\u2019s duty is to state it rather than '
           'harmonize it. Under the status regime both readings are '
           'Speculation; what distinguishes them is their priced '
           'relationship to evidence. The cessation reading is aligned '
           'with the floor protocol\u2019s anesthesia test (graded '
           'sedation depth with reports at recovery) and is the weaker '
           'metaphysical commitment; the access-severance reading '
           'preserves the field\u2019s continuity but takes on the '
           'burden of saying what an unreported, access-severed '
           'experience is, which is the locus-of-ignorance problem in '
           'empirical dress. The program\u2019s anesthesia track \u2014 '
           'now anchored by the open sedation corpora and the shared '
           'complexity instrument \u2014 can in principle adjudicate '
           'between them: graded-depth designs with pre-registered '
           'recovery reports distinguish cessation from access loss '
           'only at the phenomenological margin, so the fork is written '
           'into the track\u2019s failure conditions (Table 4.1): if '
           'the graded-depth design cannot separate the readings, the '
           'access-severance reading is unfalsifiable in this domain '
           'and must be re-graded from Speculation to an explicitly '
           'metaphysical commitment.')

    L.h2(story, '8.3 The standing seams')

    L.body(story,
           'Three seams remain untouched by every instrument this '
           'edition possesses, and they are carried forward unchanged. '
           'The subject of ignorance: the appearance-relation form '
           'relocates but does not dissolve the Advaita-style question '
           'of to whom the appearance appears and what carries the '
           'ignorance; the Claude audit\u2019s \u201cwho is '
           'deluded\u201d finding and the critiques\u2019 modal gaps '
           'both pass through it. The simplicity-versus-compositionality '
           'tension: the ground is non-composite by the corpus\u2019s '
           'own enforced Divine Simplicity turn, while every formalism '
           'that models the appearance \u2014 the partition '
           'spectra, the blanket graph, the deformation momenta of the '
           'DID classifier \u2014 is compositional; the two-level '
           'split holds the tension by scoping the formalisms to '
           'appearance, at the price that the ground itself is now '
           'modeled by nothing. The quantity of privation: the world '
           'contains the suffering the theodicy passage tried to '
           'price, and the consolidation\u2019s bar on justifying '
           'actual suffering leaves the register as description, not '
           'theodicy. These are the honest limits of the anchored '
           'position, and no anchoring claim in this edition is '
           'permitted to obscure them.')

    # ==================== 9. THE FOUR DECISIONS ====================
    L.h1(story, '9. The Four Decisions, Settled')

    L.body(story,
           'The Claude audit closed by naming four decisions \u201conly '
           'you can make,\u201d correctly noting that the transcript '
           'had left each of them ambiguous. The corpus\u2019s own '
           'materials, read to their endings, determine a position on '
           'all four; this chapter states each decision, the corpus\u2019s '
           'warrant for it, and its price. The decisions are settled '
           'in the sense the audit lineage has always used: not proven, '
           'but adopted with costs stated and alternatives priced.')

    L.data_table(
        story,
        'Table 9.1. The four decisions, their warrants, and their '
        'prices.',
        ['Decision', 'Settled position', 'Warrant in the corpus',
         'Price'],
        [
            ['Why the appearance: entailment, Advaita-style '
             'indeterminate status, or brute fact',
             'Entailment at the level of worldhood only \u2014 the '
             'appearance of a world is entailed by complete truth; '
             'this world\u2019s details are not',
             'The interlocutor\u2019s own no-creation turn (L5680); '
             'the two-level split adjudicated in the third edition '
             'after the treatise\u2019s forced-shadow contradiction '
             'was rejected; the avatar-necessity narratives demoted '
             '(chapter 6)',
             'The Spinozist reading\u2019s explanatory closure is '
             'refused: why this world remains honestly unanswered, '
             'and the three teleological arguments stay barred from '
             'doctrine'],
            ['The Bell horn: neutral, holistic superdeterminism, or '
             'extra preferred-foliation structure',
             'Horn-agnostic core: holistic covariance as the '
             'ontological reading; empirical interpretation-neutrality; '
             'pilot-wave as Interpretive Mapping; Valentini as priced '
             'probe',
             'The stratification\u2019s own layer assignments; the '
             'audit\u2019s horn-conflict finding (sustained); the '
             'intervention dilemma\u2019s standing survival',
             'The fine-tuning and measure costs of the wide '
             'correlation thesis are carried openly; the '
             'interventionist programs the corpus endorses are '
             'endorsed only as probes, so their failure costs the '
             'corpus nothing it claimed'],
            ['Agency: parallelism with agency at Level 3 only, or '
             'real top-down causation with a mechanism',
             'Psychophysical parallelism at the base; agency as a '
             'Level-3/Level-5 pragmatic fiction; the injection thesis '
             'retired to a research option requiring a mechanism',
             'The causal-closure settlement (L9248) against the '
             'injection passages (L585, L2406) \u2014 the '
             'contradiction the audits have tracked since the first '
             'critique; the audit\u2019s naming proposal adopted',
             'The framework\u2019s soteriological register loses its '
             'literal steering-wheel reading; genuine agency survives '
             'only if a mechanism is specified and survives its own '
             'tests'],
            ['Ambition: metaphysics only, or a research program with '
             'at least one discriminating prediction',
             'Both, explicitly separated: the metaphysics as scaffold; '
             'the boundary program as laboratory, able to graduate by '
             'its written criterion without the metaphysics graduating '
             'with it',
             'The graduation condition the second exchange wrote '
             '(E2 T88); the scaffold-versus-laboratory adjudication of '
             'the fourth edition; the anchors of chapter 4',
             'The graduation criterion now has instruments and failure '
             'conditions, so the program can actually fail \u2014 '
             'which is the price of being taken seriously'],
        ],
        [0.20, 0.28, 0.28, 0.24])
