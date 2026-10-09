#!/usr/bin/env python3
"""Seventh Edition (Parameter-Map Edition), Part 4: chapter 5 \u2014 the
concrete Level-2 decombination protocol. Seven phases, each with objective,
data, method (named to a published source), estimator, null model, and
failure condition."""
import fhcp_pdf_lib as L


def add_content(story):
    # ==================== 5. LEVEL-2 PROTOCOL ====================
    L.h1(story, '5. The Level-2 Protocol: A Concrete Specification')

    L.h2(story, '5.1 Objective, Scope, and Design Logic')

    L.body(story,
           'The protocol\u2019s objective is to discharge the four '
           'requirements of the decombination specification\u2019s final '
           'form: the simulation protocol (requirement 1: specify G, '
           '\u03b2, J, g, a, d, K, and the estimator for conditional '
           'mutual information; demonstrate S1\u2013S4 jointly on the '
           'same candidate subject), the null models (requirement 2: '
           'matched controls sharing global modes so that integration '
           'and self-modeling are not trivially satisfied), the '
           'finite-size scaling (requirement 3: how domain size, '
           'coherence length, and metastability scale with N, \u03b2, '
           'J, and whether the bifurcation survives the thermodynamic '
           'limit), and the neural parameter map (requirement 4: the '
           'correspondence from (J, g, a, \u03b2, \u03b8, \u03c6) to '
           'measurable neural quantities). Its scope is fixed by the '
           'culmination arc: conventional level only. The protocol '
           'tests the differentiation program\u2019s claims about the '
           'appearance\u2019s grammar; it does not, cannot, and does '
           'not attempt to bridge to the Absolute. Success at every '
           'phase would make the four-domain predictions tested, not '
           'true; failure at any phase would be informative about the '
           'specification\u2019s neural adequacy, not about the '
           'metaphysics. This is the doctrine the sixth edition welded '
           '\u2014 equivalence-is-not-validation, conceded by the '
           'counterpart itself \u2014 and the protocol is built '
           'inside it.')

    L.body(story,
           'The design logic follows the assembly result. Each '
           'specification parameter has at least one published '
           'estimation route (chapter 4); the protocol therefore '
           'proceeds by estimating the parameters arm by arm on open '
           'data, then simulating the specification with the estimated '
           'parameters, then testing S1\u2013S4 against both the '
           'simulation and the empirical data, and finally subjecting '
           'the whole to the null-model, scaling, and preregistration '
           'discipline. The phases are ordered so that each '
           'parameter\u2019s best-supported estimator is exercised '
           'first: criticality (the J row, with the Myrov ridge), '
           'anesthesia (\u03b2 and the J-modulation row, with the '
           'neural-field sweeps), psychedelics (the receptor row, with '
           'the Deco parameterization), patient-level inversion (the '
           'spatial rows, with the Jirsa machinery), joint '
           'demonstration (requirements 1\u20133 together), and '
           'preregistered adjudication. Phases 1 through 4 are '
           'independent of each other and can run in parallel; phase '
           '5 consumes their outputs; phase 6 governs everything '
           'retroactively by fixing the analysis plan before the data '
           'are touched.')

    L.data_table(
        story,
        'Table 5.1 \u2014 Protocol overview: phases, map rows discharged, '
        'named methods, and primary open data.',
        ['Phase', 'Discharges', 'Named method (source)', 'Primary open data'],
        [
            ['0. Infrastructure and preregistration',
             'Governance (all phases)',
             'OSF-style frozen analysis plan; adversarial-collaboration '
             'charter (corpus doctrine, sixth edition)',
             'Protocol document itself, versioned'],
            ['1. Coupling and criticality',
             'J vs J<sub>e</sub> estimation; \u03b2 as noise-to-coupling ratio',
             'Hierarchical Kuramoto on individual connectomes; '
             'DFA-defined critical ridge (Myrov, P2); connectome Kuramoto '
             'sweeps (\u00d3dor 2019)',
             'Open connectome sets (HCP-style dMRI); MEG: ds003059 (LSD '
             'MEG/fMRI), open resting MEG'],
            ['2. Anesthesia arm',
             '\u03b2\u2194depth mapping; anesthetic J-modulation',
             'Neural-field parameter sweeps vs spectra (Bojak\u2013Liley '
             '2005/2013; Robinson 2001); DMF inhibitory-tone mimicking '
             '(Eisen 2024)',
             'ds006623 (propofol fMRI), ds005620 (awakening), ds003171 '
             '(LOC biomarkers), ds004541 (EEG\u2013fNIRS)'],
            ['3. Psychedelic arm',
             'Receptor\u2192gain row; s<sub>e</sub> scalar; J-crossing test',
             'DMF + 5-HT2A receptor-density gain scaling (Deco, P3); '
             'FCD fitting by KS distance; blockade validation '
             '(Preller, P4)',
             'ds006072, ds006110 (psilocybin), ds003059 (LSD), ds006644, '
             'ds007768 (DMT), ds005917 (ketamine)'],
            ['4. Patient-level inversion',
             'Spatial (J, g, a, \u03b2) maps; direction prior',
             'Bayesian inversion of network models against iEEG/SEEG '
             '(Jirsa, P1); MCM directional prior (Riedl, P5)',
             'Open iEEG (epilepsy corpora incl. IDEAS ds005602); '
             'simultaneous PET\u2013MRI where available'],
            ['5. Joint demonstration',
             'Requirements 1\u20133: S1\u2013S4 jointly; nulls; '
             'finite-size scaling',
             'Projected Langevin simulation of the specification; CMI '
             'estimators (k-NN / Gaussian); shuffled and matched-mode '
             'nulls',
             'Simulated; anchored to phases 1\u20134 outputs'],
            ['6. Adjudication and reporting',
             'Status-tagged verdicts per domain',
             'Preregistered failure conditions; corpus tagging scheme '
             '(Premise / Derived / Interpretive / Speculation / '
             'Empirical-Verified / Unverified)',
             'This corpus\u2019s standing ledger'],
        ],
        [0.20, 0.20, 0.34, 0.26], font_size=8.0, header_font=8.4)

    L.h2(story, '5.2 Phase 1 \u2014 Coupling and Criticality Estimation')

    L.body(story,
           'Phase 1 estimates, per subject and per frequency band, the '
           'distance of the brain\u2019s operating point from the '
           'critical coupling regime \u2014 the specification\u2019s '
           'J-versus-J<sub>c</sub> row instantiated on real topology. '
           'The method is the Myrov pipeline: reconstruct the '
           'individual structural connectome from diffusion MRI; build '
           'the hierarchical Kuramoto model with local coupling K and '
           'global coupling L; sweep the (K, L) plane; compute node '
           'order, DFA exponents, phase-locking values, and amplitude '
           'cross-correlations on six minutes of simulated activity per '
           'parameter combination (one minute discarded as warm-up); '
           'define the critical regime as the region where more than '
           'ten percent of nodes exceed DFA 0.65; and locate the '
           'subject\u2019s operating point by maximizing the '
           'parcel-level and edge-level correlation between model '
           'observables and the subject\u2019s MEG observables, with '
           'oscillator frequencies sampled from the measured PSD with '
           'the aperiodic component removed. The output per subject is '
           'a signed distance to the critical ridge along the coupling '
           'axis \u2014 the quantity the specification calls '
           '(J<sub>c</sub> \u2212 J)/J<sub>c</sub>, estimated '
           'empirically. The null discipline is the study\u2019s own: '
           'shuffled-connectome and random-uniform models must destroy '
           'the model\u2013MEG correspondence (they did in the source), '
           'and spin-permutation tests protect the spatial '
           'correlations. The failure condition is preregistered: if '
           'the operating point does not concentrate near the ridge '
           'across subjects \u2014 if healthy resting brains scatter '
           'across the plane \u2014 then the specification\u2019s '
           'central empirical presupposition, that brains operate in '
           'the extended critical neighborhood, fails for this '
           'estimator, and the J row\u2019s neural adequacy is '
           'falsified at Level 2.')

    L.body(story,
           'Phase 1 also fixes \u03b2 operationally. The specification '
           'distinguishes a bifurcation threshold (J against '
           'J<sub>c</sub> = ga/\u03bb<sub>2</sub>) from a coherence '
           'threshold (J\u03b2 against domain-wall cost); \u03b2 is '
           'therefore not a free arousal metaphor but the '
           'noise-to-coupling ratio at the fitted operating point. In '
           'the hierarchical model this is estimated as the ratio of '
           'the fitted noise amplitude to the fitted local coupling at '
           'the MEG-matched (K, L); in the anesthetic datasets of '
           'Phase 2 it acquires its drug-explicit anchor. The '
           'elevation-cost proposal \u2014 \u03b2 to arousal \u2014 '
           'is thereby replaced by a derived estimator with a '
           'preregistered validation: \u03b2 estimates must order '
           'correctly across sedation levels within subject, or the '
           'mapping is marked Unvalidated and the anesthesia arm\u2019s '
           '\u03b2 row returns to proposal status.')

    L.h2(story, '5.3 Phase 2 \u2014 The Anesthesia Arm')

    L.body(story,
           'Phase 2 runs the specification\u2019s anesthesia '
           'prediction \u2014 domains dissolve as coupling and '
           'coherence fall below threshold with deepening sedation, '
           'with the alteration structure preserved (the '
           'specification\u2019s revision of the original '
           '\u201calters dissolve\u201d claim) \u2014 against the '
           'four open corpora. The method is the '
           'Bojak\u2013Liley sweep: parameterize the anesthetic '
           'modulation of inhibitory synaptic gain (propofol\u2019s '
           'GABAergic potentiation) and of the HCN1-mediated '
           'interaction (ketamine), sweep the modulation depth, and '
           'compare predicted against measured spectra \u2014 the '
           '\u03b1-peak frequency trajectory being the discriminating '
           'observable, since propofol and ketamine move it in '
           'opposite directions, which the neural-field analysis '
           'reproduces. In parallel, the dynamic-mean-field route '
           'mimics propofol by increasing inhibitory tone (the Eisen '
           '2024 demonstration) and tracks the destabilization of '
           'simulated networks across behavioral states. The '
           'specification-level test: translate each sedation level '
           'into the (\u03b2, J) plane via the Phase-1 estimator '
           '(noise-to-coupling ratio) and the fitted inhibitory '
           'modulation, and test whether the measured '
           'complexity-based consciousness indicators (LZ complexity, '
           'the shared instrument of the Farnes\u2013Reynante toolkit '
           'already in the corpus) fall as the operating point exits '
           'the critical neighborhood \u2014 the specification\u2019s '
           'coherence-threshold prediction. Failure condition: if the '
           'LZ trajectory across sedation levels does not track the '
           'estimated exit from the critical neighborhood within '
           'preregistered tolerance bands, the \u03b2 row and the '
           'coherence-threshold structure are falsified for the '
           'anesthesia arm; if it tracks, the arm\u2019s prediction '
           'upgrades from conjectural to tested, with the equivalence '
           'doctrine governing interpretation.')

    L.h2(story, '5.4 Phase 3 \u2014 The Psychedelic Arm')

    L.body(story,
           'Phase 3 executes the Deco parameterization on the open '
           'psychedelic corpora and tests the specification\u2019s '
           'psychedelic prediction: receptor-dense regions gain '
           'amplitude first (the entropic destabilization), pushing '
           'the operating point through or toward the critical ridge '
           'from the subcritical side \u2014 the J-crossing test. The '
           'procedure is published end to end: fit G to the placebo '
           'condition by Kolmogorov\u2013Smirnov distance against the '
           'functional-connectivity-dynamics distribution; freeze G; '
           'modulate regional gains by s<sub>E</sub> weighted by the '
           '5-HT2A receptor atlas; sweep s<sub>E</sub> and locate the '
           'optimum for the drug condition; then \u2014 the '
           'protocol\u2019s extension beyond the source \u2014 map '
           'each (G, s<sub>E</sub>) pair into the specification\u2019s '
           'plane by running the projected '
           'Ginzburg\u2013Landau dynamics with J set from the '
           'Phase-1 estimator and regional a weighted by the receptor '
           'map, and test whether the fitted drug states cluster on '
           'the near-critical side of the ridge, crossing it for the '
           'high-entropy subjects only. The controls are the '
           'source\u2019s own, plus the corpus\u2019s: two hundred '
           'shuffled receptor maps, the uniform map, the '
           'wrong-receptor maps (5-HT1A, 1B, 4, T), and \u2014 the '
           'intervention anchor \u2014 the ketanserin-blockade '
           'condition of the Preller design, where the model must '
           'return to placebo parameters when the receptor is '
           'blocked. The 5-HT2A gene-expression spatial match '
           '(Preller\u2019s Allen-Atlas result) supplies the '
           'independent anatomical cross-check. Failure condition: if '
           'the drug-condition fits require receptor maps '
           'indistinguishable from shuffled controls \u2014 that is, '
           'if the psychedelic state\u2019s dynamics are explained '
           'without the receptor\u2019s spatial structure \u2014 the '
           'receptor row fails; if the fitted states do not approach '
           'the ridge, the J-crossing prediction is falsified at '
           'Level 2.')

    L.h2(story, '5.5 Phase 4 \u2014 Patient-Level Inversion')

    L.body(story,
           'Phase 4 adapts the Virtual Epileptic Patient\u2019s '
           'inference machinery to the specification\u2019s '
           'parameters, on open intracranial corpora and, where '
           'simultaneous acquisitions exist, with the metabolic '
           'connectivity prior. The node model is replaced by the '
           'projected Langevin dynamics of the specification with its '
           'quartic onsite potential; the fitting target, following '
           'the source\u2019s observables, is the log power of '
           'high-frequency activity per channel, baseline-corrected '
           'and detrended, with a Gaussian observation model and the '
           'SEEG forward solution; the inferred spatial map is '
           '(g, a, J<sub>local</sub>, \u03b2) per region rather than '
           'x<sub>0</sub> alone, with the zero-mean projection '
           'handled exactly as the specification requires (the '
           'Lagrange-multiplier formulation). Inference is Bayesian '
           '\u2014 Hamiltonian Monte Carlo with variational '
           'initialization, as in the source \u2014 and returns '
           'posterior densities per region, so that '
           'epileptogenic-vs-healthy grading becomes '
           'domain-vs-vacuum grading: regions whose posterior '
           'J-against-threshold mass lies below J<sub>c</sub> are '
           'candidate domains. The Riedl prior enters where the data '
           'support it: on simultaneous PET\u2013MRI acquisitions, '
           'the MCM direction field asymmetrizes the otherwise '
           'symmetric coupling, and the FDG map supplies an '
           'independent energetic reading of the a parameter '
           '(attractor depth as metabolic cost). The validation '
           'ladder is the source\u2019s: first reproduce a known '
           'result (the seizure-propagation reconstruction on open '
           'epilepsy data), then invert the specification on the same '
           ' recordings and test whether the recovered domain '
           'structure matches the clinically established zones '
           '\u2014 an epileptogenic zone is, after all, a '
           'pathological domain, and the specification predicts its '
           'boundary geometry (domain walls at connectome seams). '
           'Failure condition: if the specification\u2019s '
           'inversion cannot recover known zones at rates above the '
           'shuffled-connectome null, the spatial rows are '
           'inadequate at iEEG grade.')

    L.h2(story, '5.6 Phase 5 \u2014 Joint Demonstration, Null Models, and Scaling')

    L.body(story,
           'Phase 5 discharges requirements 1\u20133 together, in '
           'simulation, with the parameters anchored by phases '
           '1\u20134. The simulation protocol is fixed as follows. '
           'Graph G: the individual connectome, thresholded at '
           'connection density 0.2 with weights normalized so that '
           'the Laplacian spectrum is comparable across subjects; N '
           'is the parcellation size (90 AAL for cross-study '
           'comparability, 200-region Lausanne for robustness). '
           'Field dimension d = 2 with the anisotropic potential '
           'V(x, y) = g/4\u00b7(x<super>2</super> + y<super>2</super> \u2212 a)<super>2</super> + '
           '\u03ba\u00b7x<super>2</super>y<super>2</super>, phase count K set by the '
           'number of macroscopic networks the empirical '
           'phase-clustering resolves; J set from Phase 1\u2019s '
           'operating point; \u03b2 from the Phase-1 ratio; (g, a) '
           'from Phase 4\u2019s posterior medians with the '
           'sensitivity analysis below. Integration: '
           'Euler\u2013Maruyama with the projection P = '
           'I \u2212 11\u1d40/N applied at every step, step size '
           '0.05, 256 steps per simulated second (the source '
           'convention). The conditional mutual information '
           'estimator: k-nearest-neighbor (Kraskov-style) CMI for '
           'scalar conditionals, Gaussian-process CMI for '
           'field-valued conditionals, both with preregistered '
           'bias-correction and surrogate calibration \u2014 the '
           'specification\u2019s requirement 1 explicitly demands '
           'the estimator be named, and the corpus adopts the '
           'k-NN family as primary with the GP family as '
           'confirmation.')

    L.body(story,
           'The joint demonstration then evaluates D, I, S, and P on '
           'the same candidate subject (A, B, R) \u2014 the honest '
           'theorem\u2019s antecedents \u2014 under the '
           'specification\u2019s exact definitions: dissociation '
           'I(\u03a8<sub>A</sub>; \u03a8<sub>R</sub> | '
           '\u03a8<sub>B</sub>) \u2264 \u03b5 with the graph blanket '
           'B; integration I(\u03a8<sub>A1</sub>; \u03a8<sub>A2</sub> '
           '| \u03a8<sub>B12</sub>) \u2265 \u03b8 with \u03b8 '
           'preregistered against nulls; intervention-validated '
           'self-modeling \u0394<sub>self</sub> with the effect '
           'required to vanish under M<sub>t</sub>-lesioning; and '
           'stable closure \u03c1(D\u212b<sub>A</sub>) < 1 together '
           'with vanishing innovation from the exterior under '
           'interventions on R. The null models of requirement 2 '
           'are: (i) shuffled-connectome (topology destroyed, degree '
           'preserved); (ii) matched-global-mode surrogates '
           '(phase-shuffled signals sharing the dominant modes, '
           'which inflate naive integration); (iii) '
           'random-graph-matched (same degree distribution, rewired); '
           'and (iv) the strongest control the corpus adds \u2014 a '
           'homogeneous-field null in which the same dynamics run '
           'with a and J uniform, so that any domain structure is '
           'purely connectome-borne. The finite-size scaling of '
           'requirement 3 runs N across 90, 200, 500, and 1000 with '
           'two graph families (connectome-derived and '
           'stochastic-block replicas), measuring domain size, '
           'coherence length, metastability lifetime, and the '
           'bifurcation gap; the specification\u2019s honest claim '
           '\u2014 metastable domain states with Gibbs mixing rather '
           'than literal spontaneous symmetry breaking at finite N '
           '\u2014 must reproduce, and the thermodynamic-limit '
           'question answered by extrapolation. Failure conditions: '
           'any null passing D+I+S+P; the homogeneous-field null '
           'passing I; scaling exponents inconsistent with the '
           'specification\u2019s c \u221d \u221a(J<sub>c</sub> '
           '\u2212 J) prediction; or S1\u2013S4 failing to co-locate '
           'on a single (A, B, R) at the anchored parameters.')

    L.h2(story, '5.7 Phase 6 \u2014 Preregistration, Adversarial Collaboration, and Reporting')

    L.body(story,
           'Phase 6 fixes the governance. The analysis plan \u2014 '
           'every estimator, threshold, tolerance band, null, and '
           'failure condition named above \u2014 is frozen and '
           'timestamped before any empirical data are touched, in '
           'the open-science registry style, with the corpus\u2019s '
           'own pre-registration discipline (adopted at the fifth '
           'edition after the refutation-conditions chapter) as the '
           'template. Deviations are permitted only as logged '
           'amendments with justification, never silently \u2014 the '
           'lesson of the search-protocol rule, generalized. '
           'Adversarial collaboration is the standing posture: the '
           'corpus\u2019s entire method is the adversarial audit, '
           'and the protocol invites the same treatment, with the '
           'physicalist rival hypotheses (global-mode artifacts, '
           'hemodynamic confounds, parcellation sensitivity, '
           'selection effects in the open corpora) assigned to '
           'named devil\u2019s-advocate analyses rather than left '
           'for reviewers to discover. Reporting follows the '
           'status-tag scheme: every claim leaves the protocol '
           'tagged Premise, Derived, Interpretive, Speculative, '
           'Empirical-Verified, or Unverified, with the tagging '
           'auditable from the frozen plan. The equivalence doctrine '
           'is printed on every results table: a confirmed '
           'prediction of the differentiation program is evidence '
           'about the appearance\u2019s grammar, not validation of '
           'the metaphysics, and no protocol output may be cited '
           'otherwise.')

    L.h2(story, '5.8 The Predictions and Their Failure Conditions')

    L.data_table(
        story,
        'Table 5.2 \u2014 The four domains at Level 2: predictions, '
        'instruments, and preregistered failure conditions.',
        ['Domain', 'Prediction (specification)', 'Instrument / data', 'Failure condition'],
        [
            ['Psychedelics',
             'Receptor-weighted gain pushes the operating point toward '
             'and for high-entropy subjects across the critical ridge; '
             'entropy and sensory\u2013associative redistribution track '
             'the crossing',
             'Deco parameterization on ds006072 / ds006110 / ds003059; '
             'Phase-1 ridge estimator; 5D-ASC covariates',
             'Drug fits indistinguishable from shuffled-receptor '
             'controls; or fitted states not near the ridge'],
            ['Anesthesia',
             'Sedation lowers the noise-to-coupling ratio out of the '
             'coherence neighborhood; domain structure dissolves '
             'before the bifurcation; complexity indicators track the '
             'exit',
             'Bojak\u2013Liley sweeps + Phase-1 \u03b2 estimator on '
             'ds006623 / ds005620 / ds003171 / ds004541; LZ complexity '
             '(Farnes\u2013Reynante instrument)',
             'LZ trajectory does not track the estimated critical-'
             'neighborhood exit within tolerance bands'],
            ['Split-brain',
             'Disconnection raises \u03bb<sub>2</sub> of the residual graph, '
             'moving J<sub>e</sub>; a small residual posterior coupling '
             'suffices near the ridge (the Santander fraction)',
             'Simulation on individual and synthetic callosotomy '
             'graphs; Santander analysis code; IDEAS surgical '
             'candidates (ds005602 / ds007401) as connectome sources',
             'Simulated disconnection does not reproduce the '
             'observed critical-coupling tolerance (~10% fibers '
             'sufficing) under the estimated parameters'],
            ['DID',
             'Part-dependent state switching corresponds to '
             'metastable domain selection: transitions occur between '
             'attractor basins rather than by continuous drift; '
             'switch-related caudate and prefrontal findings mark the '
             'domain-wall dynamics',
             'Simulation with bistable regional parameters against '
             'the published signature findings (Schlumpf 2013; '
             'Reinders 2019; Modesti 2022) as qualitative targets; '
             'no open raw data \u2014 literature-anchored only',
             'Simulated switching statistics incompatible with the '
             'documented transition phenomenology (amnesia '
             'boundaries, switch latency, part-dependent activation) '
             'under any parameter set in the preregistered family'],
        ],
        [0.13, 0.34, 0.29, 0.24], font_size=7.9, header_font=8.3)

    L.h2(story, '5.9 Compute, Data Logistics, and Honest Limits')

    L.body(story,
           'The compute plan is modest by simulation-science '
           'standards and is dominated by the (K, L) sweeps and the '
           'Bayesian inversions. The Myrov pipeline\u2019s scale '
           '\u2014 twenty-four models, two-dimensional sweeps, six '
           'minutes per combination \u2014 ran on laboratory '
           'workstations; the specification\u2019s projected '
           'Langevin system at 90\u20131000 nodes with '
           'two-dimensional fields is comparable to the '
           'epilepsy-simulation loads the Virtual Brain community '
           'handles routinely, and the parameter-space exploration '
           'of the source (a four-dimensional chart over seizure '
           'counts) is the pattern for the protocol\u2019s '
           '(J, \u03b2, a, K) charts. The open tooling covers every '
           'phase: neurolib for mean-field simulation, the decolab '
           'repository for the receptor parameterization, the '
           'Virtual Brain and the BVEP for patient-level machinery, '
           'the tsantander repository for the split-brain '
           'criticality analysis, and the Reynante toolkit for the '
           'complexity instrument. Data logistics are the '
           'asymmetry already documented: psychedelics and '
           'anesthesia have strong open coverage; split-brain and '
           'DID have none, and their Level-2 tests are therefore '
           'simulation-anchored with literature targets \u2014 '
           'an honest degradation the protocol does not disguise.')

    L.body(story,
           'The honest limits, stated once more in the '
           'protocol\u2019s own voice. First, the map assembled here '
           'is conventional-level throughout; nothing in any phase '
           'bears on the Absolute, and the culmination arc\u2019s '
           'ceiling \u2014 no bridge, because no two banks \u2014 '
           'is not moved by any result. Second, the stabilization '
           'pair (g, a) and the phase parameters (\u03b8, \u03c6, '
           '\u03ba, K) begin as derived and structural assignments; '
           'they acquire empirical standing only through Phase 5\u2019s '
           'discriminating tests, and until then the map that '
           'includes them is an assembly under test, not a '
           'delivered artifact. Third, the open corpora are '
           'convenience samples of volunteers and patients; '
           'selection effects, parcellation sensitivity, and '
           'hemodynamic confounds are named devil\u2019s advocates '
           'with their own analyses, and a protocol that passes '
           'only by silencing them has not passed. Fourth, the '
           'non-bijectivity the VEP paper concedes applies here '
           'too: an estimated (J, \u03b2) pair is a '
           'model-level quantity whose physiological realization '
           'is many-to-one, and the protocol\u2019s claims are '
           'therefore claims about the specification\u2019s '
           'dynamics matching neural dynamics \u2014 the '
           'equivalence the doctrine governs \u2014 not about '
           'having found the brain\u2019s own parameters. Within '
           'those limits, the program the elevation-cost analysis '
           'called \u201cthe highest realistic target\u201d is now '
           'specified to the phase level, with named methods, '
           'named data, named nulls, and named failure conditions '
           '\u2014 which is what it takes to stop being a sketch '
           'and start being a protocol.')
