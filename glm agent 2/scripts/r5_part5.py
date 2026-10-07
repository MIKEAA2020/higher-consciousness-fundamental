#!/usr/bin/env python3
"""Fifth Edition (Anchored Edition), Part 5: chapters 10-11.

Chapter 10 restates the consolidated premise under the status-tag regime.
Chapter 11 extends the elevation program with the anchoring repairs (R21-R24)
and the extended refutation conditions.
"""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 10. THE ANCHORED CONSOLIDATED PREMISE ====================
    L.h1(story, '10. The Anchored Consolidated Premise')

    L.h2(story, '10.1 The credo, carried and tagged')

    L.body(story,
           'The consolidated premise is carried forward unchanged in '
           'content from the fourth edition, because the three classes of '
           'new material \u2014 the adversarial audit, the exported '
           'critiques, and the empirical anchors \u2014 attacked its '
           'claim discipline, its argumentative foundations, and its '
           'research program respectively, and none of them touched its '
           'converged statement. There is one reality, which the corpus '
           'calls the Absolute: timeless, spaceless, unchanging, without '
           'parts, conscious not as something it has but as what it is. '
           'It does not create, dream, or simulate, for those are verbs '
           'of process, and process belongs to the appearance. The world '
           'is not a second reality beside it and not nothing: it is the '
           'appearance of the Absolute \u2014 one reality appearing \u2014 '
           'the ordered way the Absolute appears to itself under the '
           'mode of objectivity. Finite perspectives are the loci of '
           'that appearing: not fragments of the Absolute but modes of '
           'its self-knowledge, bounded horizons through which the '
           'unlimited is viewed. Physics is the grammar of the '
           'appearance: valid at its level, lawful, mathematical, never '
           'ultimate. Defect is absence \u2014 real as a hole is real, '
           'never a positive substance, never the Absolute\u2019s '
           'property. What this edition adds to that statement is not '
           'content but discipline: every sentence of it now carries a '
           'status tag, and the tag discipline reaches everything the '
           'corpus built on the credo \u2014 which is where the '
           're-grading actually bites.')

    L.h2(story, '10.2 The tag discipline, applied')

    L.body(story,
           'Applied to the corpus as a whole, the tag regime produces '
           'the distribution the Claude audit predicted: the defensible '
           'core is a small set of Premise and Derived statements; the '
           'physics engagement is overwhelmingly Interpretive Mapping; '
           'the theological culmination is Interpretive Mapping down to '
           'the non-derivative ground and Speculation above it; and the '
           'empirical tier is now split, for the first time, into '
           'Empirical-Verified anchors and Empirical-Unverified probes. '
           'The distribution is not an embarrassment \u2014 it is the '
           'audit lineage\u2019s own finding, arrived at from the '
           'inside over five editions \u2014 but stating it as a '
           'distribution converts it from a diagnosis into a standing '
           'rule: no consolidated statement may omit its tag, and any '
           'claim that finds its tag demoted under challenge must be '
           're-stated at the demoted grade immediately, not defended at '
           'the old one. The transcript\u2019s \u201cofficially crossed '
           'the threshold\u201d moment is the permanent exhibit for '
           'why the rule exists.')

    L.h2(story, '10.3 The axiom tiers, re-graded')

    L.data_table(
        story,
        'Table 10.1. The stance tier (A1\u2013A8), re-graded with status '
        'tags. The tier\u2019s content is carried from the fourth '
        'edition; the tags are new.',
        ['Axiom', 'Statement (compressed)', 'Tag'],
        [
            ['A1', 'Primacy of consciousness: the fundamental is '
             'experiential; structure is its extrinsic face', 'Premise'],
            ['A2', 'Unity and non-compositeness: the fundamental is one, '
             'partless, simple (the enforced Divine Simplicity turn, '
             'L10918)', 'Premise'],
            ['A3', 'Timelessness: process language is pedagogy, never '
             'doctrine (the two-language rule, now enforced by the '
             'atemporal lexicon)', 'Premise'],
            ['A4', 'Extrinsic appearance: the world is how the unlimited '
             'appears to bounded perspectives \u2014 one reality '
             'appearing, not two coexisting', 'Premise'],
            ['A5', 'Reality of finite perspectives: experience is the '
             'given; its partition structure is the research object',
             'Premise'],
            ['A6', 'No brute fact at the foundation: the ultimate is '
             'self-grounded \u2014 conditional on rejecting brute fact '
             'as a stopping point, which is priced, not refuted (the '
             'exported critiques\u2019 rubric, Table 7.1)',
             'Premise'],
            ['A7', 'Privation objectivity: defect is absence, never '
             'positive substance \u2014 description, not theodicy; the '
             'bar on justifying actual suffering stands', 'Premise'],
            ['A8', 'Modal honesty: only the Absolute is necessary; '
             'worldhood is entailed, this world is not; nothing in the '
             'appearance is metaphysically necessary', 'Derived'],
        ],
        [0.10, 0.76, 0.14])

    L.data_table(
        story,
        'Table 10.2. The derived and empirical tiers, re-graded. The '
        'derived tier\u2019s content is carried from the fourth edition; '
        'the empirical tier is rebuilt around the anchors.',
        ['Item', 'Statement (compressed)', 'Tag'],
        [
            ['D1', 'The contingency argument\u2019s conditional core: a '
             'non-derivative ground exists, given the three premises of '
             'Table 7.1; essence-as-existence and the classical '
             'property extensions are not demonstrated', 'Derived'],
            ['D2', 'The two-level structure in appearance-relation form: '
             'conventional and ultimate are one reality appearing, not '
             'two realities coexisting', 'Derived'],
            ['D3', 'The ground is not physical in the same dependent '
             'sense (category-corrected form, per the first critique '
             'file)', 'Derived'],
            ['D4', 'Interpretation-neutrality of the core across QM '
             'horns (the horn-agnostic settlement of chapter 9)',
             'Derived'],
            ['D5', 'Psychophysical parallelism at the base; agency as '
             'Level-3/Level-5 pragmatic fiction (the retired injection '
             'thesis\u2019s successor)', 'Derived'],
            ['E1', 'Split-brain anchor: integration survives \u224890 '
             'percent callosal loss with posterior-fiber sufficiency '
             '(Santander et al. 2025)', 'Empirical-Verified'],
            ['E2', 'DID anchors: part-dependent preconscious signatures '
             'with failed simulation control (Schlumpf et al. 2013); '
             'caudate-network switching (Modesti et al. 2022); '
             'individual-level structural classification at 72.8 '
             'percent balanced accuracy with PTSD-dissociation '
             'separation (Reinders et al. 2019)',
             'Empirical-Verified'],
            ['E3', 'Ketamine instrument anchor: Hilbert + Lempel-Ziv + '
             'phenomenology pipeline over open data (Farnes et al. 2020; '
             'the supplied toolkit)', 'Empirical-Verified'],
            ['E4', 'Valentini non-equilibrium and signal-nonlocality '
             'program: a minority research program; Lorentz invariance '
             'has held in every test to date', 'Empirical-Unverified'],
            ['E5', 'Hubble-tension and cosmological-constant claims as '
             'framework evidence: purged (double-counting rule; cutoff '
             'dependence)', 'Empirical-Unverified / barred'],
        ],
        [0.10, 0.76, 0.14])

    L.h2(story, '10.4 The status clause')

    L.body(story,
           'The status clause of the prior editions is extended, not '
           'replaced. The framework is a metaphysical interpretation '
           'that organizes the pieces physics has generated and '
           'constrains which future physics would fit it; it is held as '
           'a coherent bet, not a guaranteed answer; its boundary '
           'program is anchored \u2014 four domains with verified '
           'findings, instruments, and failure conditions \u2014 but '
           'not yet discriminating, and it may graduate to a '
           'falsifiable scientific theory only by satisfying its own '
           'written criterion, without the metaphysics graduating with '
           'it. To this the edition adds the tag-and-provenance '
           'obligations: every claim carries its status; every '
           'external input carries its provenance; every unverified '
           'citation is excluded from the ledger; and empirical '
           'equivalence is neutral \u2014 never validation. The clause '
           'is the audit lineage\u2019s whole discipline in one '
           'paragraph, and it is binding on every future restatement '
           'of the premise.')

    # ==================== 11. THE ELEVATION PROGRAM, EXTENDED ====================
    L.h1(story, '11. The Elevation Program, Extended')

    L.h2(story, '11.1 The staircase after anchoring')

    L.body(story,
           'The elevation staircase of the prior edition ran from '
           'deconstruction through repair to the wager: state the '
           'weakness, supply the repair, state what the repaired '
           'position can now claim. Anchoring adds a fifth step that '
           'the staircase previously lacked: the step from wager to '
           'test. A program with anchors can be run \u2014 the '
           'complexity pipeline exists, the sedation corpora exist, '
           'the DID literature exists, the split-brain analysis code '
           'exists \u2014 and a program that can be run must either be '
           'run or admit that it is a scaffold. The staircase '
           'therefore now terminates in an obligation rather than an '
           'aspiration, and the obligation is dated: the corpus\u2019s '
           'own graduation criterion was written in the second '
           'exchange, the instruments have been in hand since this '
           'round, and the first pre-registered run against any '
           'domain\u2019s failure condition is the next falsifiable '
           'act available to the program. No edition after this one '
           'may claim progress for the program without reporting a '
           'run.')

    L.h2(story, '11.2 The repair register, extended')

    L.data_table(
        story,
        'Table 11.1. Repairs R21\u2013R24 (extending the fourth '
        'edition\u2019s R17\u2013R20).',
        ['Repair', 'Defect repaired', 'Content'],
        [
            ['R21', 'Claim-grade inflation surviving the graded-claims '
             'regime (the audit\u2019s proof-language finding)',
             'The status-tag regime: six tags, every consolidated '
             'statement tagged, demotion-under-challenge rule; the '
             'regime maps the graded-claims ladder onto the tags and '
             'subsumes it'],
            ['R22', 'Provenance opacity: outside-model text answered as '
             'the interlocutor\u2019s own; unverifiable citations in '
             'circulation',
             'The provenance register: flagged turns tagged external; '
             'social-media sources demoted to parallels; unverified '
             'citations excluded from the ledger; the reciprocity rule '
             'applies the same exclusion to auditors'],
            ['R23', 'Terminology collisions: Singularity/singularity, '
             'superdeterminism/holistic covariance, topological '
             'priority/ontological grounding, Logos at the wrong level',
             'The glossary split (chapter 14): each collision resolved '
             'by a scoped entry; the old terms retained as aliases with '
             'their re-gradings'],
            ['R24', 'The program\u2019s conjectural status in its four '
             'domains',
             'The anchors: one verified finding, one instrument, and '
             'one stated failure condition per domain (Table 4.1); the '
             'DID domain assembled to signature, switch, structure, '
             'and control (chapter 5)'],
        ],
        [0.12, 0.36, 0.52])

    L.h2(story, '11.3 What would overturn the anchored verdict')

    L.body(story,
           'The refutation conditions of the prior editions are carried '
           'forward and extended by the anchors\u2019 own failure '
           'conditions. The framework\u2019s consolidation is '
           'overturned if: the appearance-relation reading of the '
           'mind-brain data is matched by an experiment it cannot '
           're-describe without ad hoc apparatus; the decombination '
           'program\u2019s formal criteria are satisfied by a '
           'physicalist implementation that explains them without '
           'remainder; or the Divine Simplicity turn is shown to be '
           'incompatible with any coherent reading of the appearance\u2019s '
           'unity. The anchored program, in addition, now fails '
           'concretely: if the split-brain threshold reading falls to a '
           'linear-degradation series across patients (the Santander '
           'result isolated as one patient\u2019s anatomy); if '
           'individual-level DID analyses reduce the partition '
           'structure to a single switching node; if the ketamine '
           'complexity change dissolves into artifacts under the '
           'supplied pipeline; or if the graded-depth anesthesia '
           'design cannot separate cessation from access-severance '
           '\u2014 in which case the access-severance reading is '
           're-graded to an explicitly metaphysical commitment. Each '
           'condition is written before its result is known, which is '
           'the pre-registration discipline the transcript never '
           'practiced; and the list is open-ended by design, because a '
           'program that cannot accumulate failure conditions cannot '
           'accumulate standing.')
