#!/usr/bin/env python3
"""Eighth Edition (Computed Edition), Part 5: chapters 6-8 \u2014
epistemic status, edition delta with repairs R32-R34, and the appendix."""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 6. EPISTEMIC STATUS ====================
    L.h1(story, '6. Epistemic Status: What Execution Changes and Cannot')

    L.body(story,
           'The seventh edition moved the four domains from '
           '\u201cconjectural, pending a map that does not exist\u201d '
           'to \u201cconjectural, with the assembly specified as an '
           'executable protocol.\u201d The eighth edition moves two '
           'rows of that standing again, and only those rows: the '
           'anesthesia arm\u2019s \u03b2 row is no longer conjectural '
           'at the level of its validation condition \u2014 the '
           'condition has been run, and it passed in its clean form '
           '\u2014 and the psychedelic arm\u2019s complexity '
           'observable is no longer a citation but a replication '
           'performed inside this corpus\u2019s instrument. The '
           'corresponding domain labels shift from finding-anchored '
           'toward finding-anchored-plus-executed-fragment. Everything '
           'upstream is untouched: the metaphysical premises\u2019 '
           'tiers, the non-dual culmination, the formalization '
           'boundary, the superdeterminism tension\u2019s grade, the '
           'adjudication counts, and above all the equivalence '
           'doctrine, under which even a fully successful protocol '
           'licenses only \u201cthe differentiation program\u2019s '
           'predictions are tested and surviving,\u201d never '
           '\u201cthe Absolute is thereby evidenced.\u201d')

    L.body(story,
           'What execution changes, at the deepest level, is the '
           'corpus\u2019s relationship to its own least-necessary '
           'component. The culmination arc ruled the differentiation '
           'program \u201cuseful, not necessary\u201d; the audit '
           'tradition responded by making that component maximally '
           'falsifiable. A protocol with failure conditions is a '
           'promise; a protocol with exercised failure conditions is '
           'a practice. Two conditions have now been faced without '
           'the program\u2019s destruction \u2014 the scatter '
           'condition absorbed by the weak-form support, the '
           'ordering condition passed \u2014 and two honest '
           'negatives have been recorded without reinterpretation: '
           'the operating-point structure-function coupling that '
           'is not topology-specific, and the mean-field \u03b1-'
           'trajectory that does not reproduce from the printed '
           'parameters. The program\u2019s integrity does not depend '
           'on its successes; it depends on its willingness to '
           'publish its failures at the same grade as its successes, '
           'and that willingness is now demonstrated four times '
           'over. This is the corpus\u2019s own standard, applied to '
           'itself, with numbers.')

    # ==================== 7. EDITION DELTA ====================
    L.h1(story, '7. Edition Delta and Repairs R32\u2013R34')

    L.body(story,
           'This edition is an increment on the seventh, not a '
           're-typeset of it. The seventh edition\u2019s eight '
           'chapters \u2014 the parameter-map verdict correction, '
           'the five sources read from PDF, the fragments-and-'
           'assembly statement, the seven-phase protocol, the '
           'epistemic status, the repairs R28\u2013R31, and the '
           'unfetchable appendix \u2014 remain standing and are not '
           'duplicated here. The reader of the two volumes together '
           'holds the full corpus state; the reader of this one '
           'alone holds the execution turn: the two phases run, the '
           'Farnes corpus resolved and both its contrasts completed, '
           'the map re-graded with computed values, and the protocol '
           'amended four times. The series convention \u2014 every '
           'edition self-contained in its front matter and '
           'appendices \u2014 is preserved by chapters 1, 2, and 8.')

    L.body(story,
           'Three repairs are logged, continuing the series '
           'numbering. R32 \u2014 the evoked-file reshape error: the '
           'round-twenty single-condition reference (waveform LZ '
           '0.855, envelope LZ 0.881) was computed on a row-major '
           'mis-mapping of the column-major MATLAB stream; the '
           'diagnosis is exact (the wrong mapping reproduces the '
           'reported values to the third decimal), the corrected '
           'values are 0.626 and 0.618, and the corrected mapping '
           'restores the TMS-evoked structure (flat 0.006 \u03bcV '
           'pre-pulse baseline; GFP peak 64\u201383 ms post-pulse) '
           'that the scrambled mapping could not show. R33 \u2014 '
           'the recovery-denominator arithmetic: the round-twenty '
           'report stated 4,414,380 declared doubles for the 293-'
           'trial array; the correct product of the dims (60 \u00d7 '
           '251 \u00d7 293) is 4,412,580, and the Raw_data_2 copy '
           'of the file is complete at exactly that count \u2014 '
           'which both corrects the record and validates the '
           'truncated-copy recovery (the 285-trial recovered prefix '
           'yields statistics identical to the complete file\u2019s '
           'to the third decimal). R34 \u2014 the appendix data row: '
           'the Farnes Dryad raw-EEG item, listed as unfetchable '
           'through the seventh edition, is resolved by supply '
           '(Raw_data_2, 101 sha256-verified assets) and closed; the '
           'one .set header corrupted at source is handled by the '
           'documented sidecar, not by silent substitution.')

    L.data_table(
        story,
        'Table 7.1 \u2014 The four domains: grade at the seventh '
        'edition versus grade at this edition.',
        ['Domain', 'Seventh-edition grade', 'Eighth-edition grade',
         'Basis of change'],
        [
            ['Psychedelics',
             'Finding-anchored + complete map fragment '
             '(receptor\u2192gain, intervention-validated)',
             'Finding-anchored + replicated observable (LZc under '
             'ketamine, this corpus\u2019s instrument)',
             'The Farnes corpus resolved; both contrasts run; the '
             'evoked dissociation reproduced at the corrected level'],
            ['Anesthesia',
             'Pathway-anchored + published parameter-sweep method',
             'Pathway-anchored + \u03b2 row TESTED (ordering '
             'condition passed 6/6 clean; LZ-tracking supported at '
             'exit granularity)',
             'Phase 2 executed on three corpora plus the theory leg; '
             'honest grades recorded per leg'],
            ['Split-brain',
             'Unchanged + simulation-ready threshold test',
             'Unchanged + the test\u2019s estimator now executed on '
             'open data (Phase 1)',
             'The J-row pipeline that would run the disconnection '
             'test has a computed operating point and recorded '
             'conventions'],
            ['DID',
             'Unchanged + metastable-switch simulation target '
             '(literature-anchored only)',
             'Unchanged',
             'No open raw data \u2014 the honest limit stands, '
             'unmodified by anything in this round'],
        ],
        [0.13, 0.28, 0.33, 0.26], font_size=8.0, header_font=8.4)

    L.body(story,
           'Consistency checks against the standing ledger: the '
           'objection ledger\u2019s rows on empirical testability '
           'are unaffected \u2014 the executions are the '
           'differentiation program answering them, and the '
           'stratification defense remains unavailable to it by its '
           'own honest theorem. The glossary additions this edition: '
           'operating point, critical ridge, noise-to-coupling ratio, '
           'DFA exponent, LZW dictionary count, shuffle normalization, '
           'background-corrected contrast, perturbational complexity '
           'index, global field power, and biphasic activation \u2014 '
           'each defined in situ at first use, per the series '
           'convention.')

    # ==================== 8. APPENDIX ====================
    L.h1(story, '8. Appendix A \u2014 The Resolution Record')

    L.body(story,
           'The seventh edition\u2019s appendix listed eight '
           'unfetchable sources. The interlocutor\u2019s supply '
           'channel has since closed them all but one: Bedford et '
           'al. 2023, Avram et al. 2024, Liang et al. 2015, Butler '
           'et al. 2025, Piccinini et al. 2025, and Fabus et al. '
           '2023 were supplied and read in Rounds 19\u201320; the '
           'Farnes raw EEG \u2014 the last data asset, and the one '
           'this edition\u2019s primary computation required \u2014 '
           'is supplied complete in the Raw_data_2 release. The '
           'remaining item is the ETH research-collection '
           'provenance record (research-collection.ethz.ch, 403 to '
           'this environment\u2019s IP range): a metadata item '
           'only, non-blocking, whose paper (Schlumpf 2013) is '
           'already read from user supply. No protocol-critical '
           'source or dataset remains unfetched, unread, or '
           'unverified; the supply channel itself \u2014 the '
           'repository\u2019s release system with sha256 digests '
           '\u2014 proved robust enough that this round\u2019s '
           'entire primary computation ran on user-supplied, '
           'checksum-verified data. The appendix\u2019s standing '
           'methodological note is unchanged: a blocked link is a '
           'fact about this environment\u2019s egress, not about a '
           'source\u2019s existence, and the resolution route that '
           'emptied this table is the interlocutor\u2019s own.')
