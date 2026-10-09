#!/usr/bin/env python3
"""Seventh Edition (Parameter-Map Edition), Part 3: chapter 4 \u2014 the
parameter map verdict correction, the five program areas, the theta/phi
gap, and the fetch-infrastructure record."""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 4. THE PARAMETER MAP ====================
    L.h1(story, '4. The Parameter Map: Fragments and Assembly Path')

    L.h2(story, '4.1 What the Specification Demands')

    L.body(story,
           'Requirement 4 of the decombination specification, verbatim '
           'from the consolidated final form: a neural parameter map is '
           '\u201ca principled correspondence from (J, g, a, \u03b2, '
           '\u03b8, \u03c6) to measurable neural quantities (fMRI, MEG, '
           'iEEG), without which the psychedelic, anesthesia, '
           'split-brain, and DID predictions remain conjectural.\u201d '
           'The six parameters belong to the corrected '
           'Ginzburg\u2013Landau network specification: the coupling '
           'J against its critical value J<sub>c</sub> = ga/\u03bb'
           '<sub>2</sub>, where \u03bb<sub>2</sub> is the algebraic '
           'connectivity of the graph; the quartic-stabilization pair '
           'g and a, which set the onsite amplitude \u2248 \u221aa and '
           'together with the spectrum set the threshold; the noise '
           'scale \u03b2, which competes with J\u03b2 against domain-wall '
           'cost in a coherence threshold distinct from the bifurcation '
           'threshold; and the phase-field parameters \u03b8 and \u03c6 '
           'of the anisotropic potential that discretizes the continuous '
           'Mexican-hat vacuum into K phases. The elevation-cost '
           'analysis, written a level down from the formalism, had '
           'proposed correspondences \u2014 \u03b2 to arousal, J to '
           'effective connectivity, a to attractor depth \u2014 but '
           'flagged them as proposals requiring biophysical derivation, '
           'not assignments. The specification\u2019s own marking was '
           'blunter: until the map exists, the four domains\u2019 '
           'predictions are conjectural.')

    L.body(story,
           'The phrase \u201cdoes not exist,\u201d as the corpus had '
           'been carrying it, made a claim about the literature without '
           'having searched the literature systematically. The '
           'interlocutor\u2019s challenge \u2014 find it through web '
           'search; provide any links you cannot fetch \u2014 converted '
           'that unexamined negative into a research task, and the task '
           'was executed. The section that follows records the corrected '
           'verdict and the evidence base: the search protocol, the five '
           'program areas where fragments of the map are published, the '
           'per-arm tables of verified sources, the gap analysis showing '
           'what still has no published assignment, and the '
           'fetch-infrastructure record with every blocked link listed '
           'for the interlocutor\u2019s use. Four of the blocked '
           'load-bearing sources were then supplied and read (chapter '
           '3); the record below reflects the state after that supply.')

    L.h2(story, '4.2 The Corrected Verdict')

    L.body(story,
           'The literal artifact does not exist. No paper, review, or '
           'dataset uses \u201cneural parameter map\u201d to mean the '
           'bridge requirement 4 demands; a literal search on the phrase '
           'returns unrelated hits \u2014 computational maps in the '
           'brain (Knudsen 1987), maps of neural collective influencers, '
           'fMRI parameter-map fitting methods, foundation-model '
           'inversion \u2014 none of which assigns the six parameters of '
           'the specification to neural measurables. No published work '
           'assigns (J, g, a, \u03b2, \u03b8, \u03c6) \u2014 the '
           'quartic-stabilized Ginzburg\u2013Landau field with domain '
           'formation below J<sub>c</sub> \u2014 across even two of the '
           'four domains, let across psychedelic, anesthesia, '
           'split-brain, and DID jointly. The phase parameters \u03b8 '
           'and \u03c6 in particular have no published neural assignment '
           'anywhere; nothing in the literature fixes the anisotropy '
           'coefficient \u03ba or the phase count K to a measurable '
           'neural quantity. In this precise sense the requirement '
           'remains unsatisfied and the four-domain predictions remain '
           'conjectural \u2014 the marking stands.')

    L.body(story,
           'But the function the artifact would perform exists '
           'piecemeal, per domain, in five mature research programs, '
           'each contributing one or two rows of the correspondence '
           'table with published methods, quantitative results, and in '
           'most cases open code. The honest verdict is therefore not '
           '\u201cdoes not exist\u201d but \u201cno unified map exists; '
           'the per-arm ingredients are individually published and '
           'verified.\u201d This correction matters practically as well '
           'as verbally: a program that believes its prerequisite is '
           'absent waits; a program that finds its prerequisite '
           'distributed across five literatures assembles. The '
           'assembly path is the subject of sections 4.3 through 4.6, '
           'and the protocol of chapter 5 is its execution plan.')

    L.h2(story, '4.3 The Five Program Areas')

    L.body(story,
           'Anesthesia has the most complete arm, because the '
           'neural-field tradition has mapped drug concentration '
           'through field parameters to predicted EEG spectra for two '
           'decades. The Bojak\u2013Liley program solves '
           'mean-field equations of cortical populations with '
           'physiologically plausible parameters and reproduces the '
           'anesthetic changes of the EEG \u2014 including the '
           'differential \u03b1-peak-frequency behavior that '
           'distinguishes propofol from ketamine, whose HCN1-mediated '
           'interactions the 2013 analysis treats explicitly. The '
           'Robinson corticothalamic tradition fits '
           'neurophysiologically grounded field parameters to empirical '
           'spectra (the 2001 paper, cited over three hundred times, is '
           'the canonical demonstration). Pharmacokinetic\u2013neural-'
           'mass hybrids relate actual drug levels to EEG dynamics and '
           'behavioral state across the sedation continuum. In map '
           'terms: the anesthesia arm possesses a published, '
           'drug-explicit route from pharmacology to field parameters '
           'to a measurable (the power spectrum), which is exactly the '
           'shape requirement 4 wants for \u03b2 and the anesthetic '
           'modulation of J.')

    L.body(story,
           'The dynamic-mean-field fitting tradition supplies the '
           'J-analog. Whole-brain mean-field models are fit to '
           'empirical functional connectivity by sweeping a single '
           'global coupling parameter G \u2014 the scalar that '
           'multiplies the connectome \u2014 and the fit\u2019s optimum '
           'locates the brain\u2019s working point on the model\u2019s '
           'bifurcation diagram. This is structurally the same move as '
           'calibrating J against J<sub>c</sub>, with G playing J '
           'one level down in model complexity. The tradition\u2019s '
           'recent applications are directly relevant: a '
           'Communications Biology study of anesthesia and disorders of '
           'consciousness fits the model across loss of consciousness; '
           'a 2024 Neuron study mimics propofol\u2019s effect in '
           'simulated networks by increasing inhibitory tone and '
           'observes the resulting destabilization across behavioral '
           'states; and the open tooling \u2014 the dynamic-mean-field '
           'reference code and the neurolib simulation library \u2014 '
           'makes the sweeps reproducible. The Deco\u2013Kringelbach '
           'whole-brain modeling monograph, freely available, is the '
           'arm\u2019s standard reference.')

    L.body(story,
           'The psychedelic arm, after this round\u2019s reads, is the '
           'only arm whose fragment is complete end to end \u2014 '
           'molecular target through regional parameter to whole-brain '
           'dynamics \u2014 because the Deco 2018 study (P3) '
           'parameterizes regional gains by the empirical 5-HT2A '
           'receptor density map, and the Preller 2018 study (P4) '
           'validates the target by full pharmacological blockade. '
           'Supporting results extend the fragment: a 2023 Scientific '
           'Reports study gives a whole-brain model of the '
           'entropy increase psychedelics elicit; the 2019 PNAS '
           'dynamic-causal-modeling study of LSD\u2019s effective '
           'connectivity (read in round-seventeen search records; full '
           'PMC mirror verified) attributes thalamocortical changes to '
           '5-HT2A; and regression-DCM studies of LSD and psilocybin '
           'map effective-connectivity changes at scale. The critical-'
           'coupling tradition supplies the arm\u2019s threshold '
           'structure: Kuramoto synchronization on the actual human '
           'connectome, with the global coupling as control parameter '
           'and critical coupling strengths identified (\u00d3dor 2019, '
           'with open PMC mirror), and branching criticality as the '
           'avalanche-level signature (Haldeman and Beggs 2005). The '
           'Myrov study (P2) unifies the two: hierarchical Kuramoto on '
           'individual connectomes, critical ridge defined by DFA, '
           'matched per subject against MEG.')

    L.body(story,
           'The patient-level inference tradition supplies what no '
           'group-level fit can: parameter maps at intracranical '
           'resolution for individual brains. The Virtual Epileptic '
           'Patient (P1) is the demonstration \u2014 a Bayesian '
           'excitability map fit to stereo-EEG, with the epileptogenic '
           'zone recovered non-invasively and validated against '
           'clinical reading across patients; the parameter-estimation '
           'literature of the Virtual Brain (Penas 2024, PLOS '
           'Computational Biology, with open code) optimizes the '
           'estimation itself; and the Bayesian Virtual Epileptic '
           'Patient\u2019s stated purpose is to infer \u201cthe spatial '
           'map of epileptogenicity\u201d \u2014 a patient-specific '
           'parameter map in the clinical sense, for epilepsy rather '
           'than for the specification. Metabolic connectivity '
           'mapping (P5) completes the set with its directional and '
           'energetic observables. The five program areas are '
           'summarized in the table below, with the arm each serves '
           'and the map row it fills.')

    L.data_table(
        story,
        'Table 4.1 \u2014 The five program areas: published fragments of the '
        'neural parameter map (all links fetch-verified or user-supplied; '
        'PMC mirrors noted where the publisher blocks this environment).',
        ['Program area', 'Load-bearing sources (verified)', 'Map row it fills'],
        [
            ['Neural field theory of anesthesia',
             'Bojak & Liley 2005, Phys Rev E 71:041902 (149+ citations); '
             'Bojak et al. 2013, Front Comput Neurosci 7:22 (ketamine vs '
             'propofol \u03b1-peak, HCN1); Robinson et al. 2001, Phys Rev E '
             '63:021903 (309 citations); PK\u2013NMM hybrids',
             'Anesthesia arm: drug \u2192 field parameters \u2192 EEG '
             'spectra; the \u03b2 and J-modulation route'],
            ['Dynamic mean-field G-fitting',
             'Deco-group fitting pipeline (open reference code); neurolib '
             'toolbox; Luppi et al. 2022, Commun Biol (PMC mirror); Eisen '
             'et al. 2024, Neuron (PMC11923585); Deco\u2013Kringelbach '
             '2025 monograph (free PDF)',
             'The J-analog: G swept against empirical FC/FCD; working '
             'point on the bifurcation diagram'],
            ['Receptor-density parameterization',
             'Deco et al. 2018, Curr Biol (P3, read in full; open code; '
             'open PET atlas); Preller et al. 2018, eLife (P4, read in '
             'full); Herzog et al. 2023, Sci Rep; Preller et al. 2019, '
             'PNAS (PMC6377471)',
             'Psychedelic arm: receptor map \u2192 regional gains; drug '
             'state \u2192 scalar s<sub>e</sub>; intervention-validated target'],
            ['Patient-level Bayesian inference',
             'Jirsa et al. 2017, NeuroImage (P1, read in full); Penas et '
             'al. 2024, PLOS Comput Biol (open code); BVEP (spatial map '
             'of epileptogenicity); Proix et al. N=15 validation',
             'Per-subject spatial parameter maps at iEEG grade; the '
             'inference engine for (J, g, a, \u03b2) regionally'],
            ['Critical coupling on the connectome',
             '\u00d3dor 2019, Sci Rep (PMC6928153); Haldeman & Beggs '
             '2005, PRL 94:058101; Myrov et al. bioRxiv (P2, read in '
             'full); D\u00f6rfler & Bullo 2011 (NTNU mirror)',
             'The J vs J<sub>e</sub> structure on real topology; '
             'distance-to-criticality per subject (DFA-defined ridge)'],
        ],
        [0.22, 0.48, 0.30], font_size=8.2, header_font=8.6)

    L.h2(story, '4.4 The Theta\u2013Phi Gap')

    L.body(story,
           'Assembling the fragments still leaves the specification\u2019s '
           'distinctive variables unmapped, and the honest assembly '
           'statement names them. The coupling J inherits the richest '
           'support: the G-sweeping tradition, the Kuramoto critical '
           'coupling literature, and the VEP\u2019s global coupling all '
           'estimate a single coupling scalar against dynamics, and the '
           'Myrov ridge gives its critical value a per-subject, '
           'per-frequency estimator. The noise scale \u03b2 has the '
           'anesthesia arm\u2019s pharmacology and the arousal mapping '
           'proposals; the protocol operationalizes it as the '
           'noise-to-coupling ratio at fixed G, following the '
           'coherence-threshold structure of the specification itself. '
           'The stabilization pair (g, a) is the weakest dynamical '
           'assignment: no published program fits an onsite-amplitude '
           'quartic to neural data, and the protocol must derive its '
           'estimator anew \u2014 from the amplitude of the observed '
           'order parameter at fixed coupling \u2014 and mark it '
           'derived-unvalidated until the null-model discipline of '
           'chapter 5 passes. The phase parameters are worse: \u03b8 and '
           '\u03c6, with the anisotropy \u03ba and the phase count K, '
           'have no published neural assignment at all. The protocol '
           'assigns them structurally \u2014 K to the number of '
           'macroscopic functional networks the data resolves, the '
           'anisotropy to the sharpness of the observed phase-cluster '
           'histograms \u2014 and tags the entire row Speculative '
           'until the simulation phases produce a discriminating '
           'signature. This is the gap the unified map must close '
           'before it exists, and no literature closes it today.')

    L.h2(story, '4.5 Fetch-Infrastructure Record')

    L.body(story,
           'The round-seventeen search probed forty-eight unique URLs '
           'with browser-like headers and recorded every failure; this '
           'round\u2019s supply resolved four of the five '
           'load-bearing blocks. What remains blocked from this '
           'environment is catalogued in Appendix A with full titles '
           'and links, so that any item the interlocutor wants read can '
           'be supplied the same way. The API layer also failed '
           'instructively: the OpenAlex service, which round twelve '
           'had used freely, rate-limited every query this round '
           '(HTTP 429, persistent across retries with backoff), and '
           'the resolution pivoted to CrossRef and Europe PMC, both of '
           'which served reliably; the web-search upstream itself threw '
           'two transient timeouts and one over-narrow-query rejection, '
           'all retried. The methodological rule the sixth edition '
           'adopted after the reciprocity retraction \u2014 a failure '
           'to locate is evidence about the search, not the target, '
           'until the search protocol is documented \u2014 is '
           'therefore applied to fetch failures too: a 403 from a '
           'publisher is a fact about the environment, not about the '
           'paper\u2019s existence, and the record below treats it '
           'that way, with every blocked load-bearing item now either '
           'resolved through a mirror, resolved through user supply, '
           'or explicitly listed as pending.')

    L.callout(story,
              'The assembly statement (status-tagged)',
              'The neural parameter map of requirement 4 does not '
              'exist as a published artifact [Empirical-Verified, by '
              'systematic search]. Its function exists piecemeal: J '
              'estimation [Published method, multiple traditions], '
              '\u03b2 through anesthetic pharmacology [Published '
              'method], receptor-to-gain regional parameterization '
              '[Published method with controls], patient-level '
              'Bayesian parameter maps [Published method, clinically '
              'validated], directional and energetic observables '
              '[Published method, simultaneous PET\u2013MRI]. The '
              'stabilization pair (g, a) has a derived but unvalidated '
              'estimator [Speculative until protocol Phase 5]. The '
              'phase parameters \u03b8, \u03c6, \u03ba, K have no '
              'published neural assignment [Gap \u2014 the map\u2019s '
              'open row]. The four-domain predictions remain '
              'conjectural until the assembly is executed; the '
              'assembly is now executable, which it was not when the '
              'requirement was written.')
