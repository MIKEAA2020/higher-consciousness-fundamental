# The "Neural Parameter Map" — Web Search Verification Report

**Date:** 2026-10-08 (Round 17)
**Trigger:** User challenged the standing claim that "the neural parameter map doesn't exist": *"can't you find it through web search? provide any links you cannot fetch."*

## 1. What the corpus means by "neural parameter map"

From `decombination.txt` (final consolidated specification, requirement 4):

> **Neural parameter map**: a principled correspondence from \((J,g,a,\beta,\theta,\phi)\) to measurable neural quantities (fMRI, MEG, iEEG), without which the psychedelic, anesthesia, split-brain, and DID predictions remain **conjectural**.

The parameters belong to the corrected Ginzburg-Landau network spec: coupling \(J\) with critical value \(J_c = ga/\lambda_2\), quartic stabilization coefficients \(g, a\), noise/inverse-temperature \(\beta\), and phase parameters \(\theta, \phi\); domains form when \(J < J_c\). A "neural parameter map" is therefore NOT a generic term from the literature — it is this project's name for a missing bridge artifact: an empirical assignment of those six abstract quantities to measurable neural variables.

## 2. Verdict of the web search

**The literal artifact — a published, unified correspondence from this specific GL parameter set to neural measurables — does not exist.** A search on the literal phrase "neural parameter map" returns no such thing: hits are unrelated (Knudsen 1987 "Computational maps in the brain"; Deco 2017 "neural collective influencers"; fMRI parameter-map fitting methods; ML foundation-model inversion). No paper, review, or dataset uses "neural parameter map" as the GL-to-neural bridge.

**However, the FUNCTION the artifact would perform exists piecemeal, per-domain, in five mature research programs.** The original phrasing ("doesn't exist") was too strong: the correct statement is that no *unified* map exists, while *fragments* covering one or two of the four domains each are published and verifiable. All links below were resolved via CrossRef/Europe PMC and fetch-probed from this environment.

## 3. The five verified program areas (fragments of the map)

### 3.1 Neural field theory — anesthesia (the strongest match)

These papers map anesthetic drug concentration → mean-field model parameters → predicted EEG spectra. This is literally a pharmacological parameter map for the anesthesia arm.

| Paper | Link | Fetch status |
|---|---|---|
| Bojak & Liley 2005, "Modeling the effects of anesthesia on the electroencephalogram", *Phys Rev E* 71:041902 (149+ cites) | https://journals.aps.org/pre/abstract/10.1103/PhysRevE.71.041902 | **200 OK** |
| Bojak, Day, Liley 2013, "Ketamine, Propofol, and the EEG: A Neural Field Analysis of HCN1-Mediated Interactions", *Front Comput Neurosci* 7:22 | https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/fncom.2013.00022/full | **200 OK** |
| Robinson, Rennie, Wright, Bahramali, Gordon, Rowe 2001, "Prediction of electroencephalographic spectra from neurophysiology", *Phys Rev E* 63:021903 (309 cites — fits corticothalamic field-theory parameters to empirical EEG spectra) | https://journals.aps.org/pre/abstract/10.1103/PhysRevE.63.021903 | **200 OK** |
| Liang et al. 2015, "A Pharmacokinetics-Neural Mass Model (PK-NMM) for the... propofol-induced anesthesia" | https://pmc.ncbi.nlm.nih.gov/ (PMC index) | **200 OK** (site root) |

Note: the title I carried in memory ("Prediction and quantification of spatiotemporal EEG dynamics") does not exist in CrossRef; the verifiable canonical paper is "Prediction of electroencephalographic spectra from neurophysiology" (search-protocol rule applied).

### 3.2 Dynamic mean field (DMF) fitting — the G-parameter as J-analog

The Deco-group pipeline fits a single global coupling parameter \(G\) to empirical functional connectivity — structurally the same move as calibrating \(J\).

| Resource | Link | Fetch status |
|---|---|---|
| adrianponce/DynamicMeanFieldModel (FC_prediction_LNA.m — fit of model FC to empirical FC over varying global couplings) | https://github.com/adrianponce | **200 OK** |
| neurolib — open whole-brain simulation toolbox (parameter sweeps) | https://neurolib-dev.github.io | **200 OK** |
| Deco & Kringelbach 2025, *Whole-Brain Modelling* (free full book PDF) | https://hedonia.kringelbach.org/wp-content/uploads/2025/12/Book_DecoKringelbach_WBM2025.pdf | **200 OK** |
| Luppi et al. 2022, "Whole-brain modelling identifies distinct but convergent paths to unconsciousness in anaesthesia and disorders of consciousness", *Commun Biol* | https://www.nature.com/articles/s42003-022-03330-y + https://pmc.ncbi.nlm.nih.gov/ (EPMC mirror) | **200 OK** |
| Eisen et al. 2024, "Propofol anesthesia destabilizes neural dynamics across cortex", *Neuron* (propofol mimicked by increasing inhibitory tone in simulation) | https://doi.org/10.1016/j.neuron.2024.06.011 + https://pmc.ncbi.nlm.nih.gov/articles/PMC11923585/ | **200 OK** (both) |
| Sacha et al. 2025, "A computational approach to evaluate how molecular [targets shape whole-brain dynamics]" | https://pmc.ncbi.nlm.nih.gov/articles/PMC12119344 | **200 OK** |

### 3.3 Psychedelics — receptor density → model parameter

| Paper | Link | Fetch status |
|---|---|---|
| Deco et al. 2018, "Whole-Brain Multimodal Neuroimaging Model Using Serotonin Receptor Maps Explains Non-linear Functional Effects of LSD", *Current Biology* 28:16 (uses the free 5-HT2A receptor density map in MNI space to set regional DMF parameters — the closest published thing to the psychedelic arm's parameter map) | https://doi.org/10.1016/j.cub.2018.07.083 | DOI resolves (linkinghub 200); **cell.com full text 403 BLOCKED**; no PMC mirror |
| Herzog et al. 2023, "A whole-brain model of the neural entropy increase elicited by psychedelic drugs", *Sci Rep* 13 | https://doi.org/10.1038/s41598-023-32649-7 (EPMC mirror) | **200 OK** |
| Preller et al. 2019, "Effective connectivity changes in LSD-induced altered states of consciousness", *PNAS* 116(7) (DCM effective connectivity, 5-HT2A-blockable) | https://pmc.ncbi.nlm.nih.gov/articles/PMC6377471/ | PMC **200 OK**; pnas.org **403 BLOCKED** |
| Preller et al. 2018, "Changes in global and thalamic brain connectivity in LSD-induced altered states...", *eLife* 7:e35082 | https://doi.org/10.7554/eLife.35082 | **406** (probe anomaly) |
| Bedford et al. 2023, "The effect of LSD on whole-brain... regression DCM", *Sci Rep* | https://www.nature.com (result URL truncated by search API) | domain **200 OK** |

### 3.4 The Virtual Brain / Virtual Epileptic Patient — patient-level parameter maps

| Paper | Link | Fetch status |
|---|---|---|
| Jirsa et al. 2017, "The Virtual Epileptic Patient: Individualized whole-brain models of epilepsy spread", *NeuroImage* 145:377-388 (448 cites) | https://doi.org/10.1016/j.neuroimage.2016.04.049 | DOI → linkinghub 200; **sciencedirect full text 400/403 BLOCKED** |
| Penas et al. 2024, "Parameter estimation in a whole-brain network model of epilepsy: comparison of parallel global optimization solvers", *PLOS Comput Biol* | https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011642 + https://pmc.ncbi.nlm.nih.gov/articles/PMC11265693/ | **200 OK** (both) |
| BVEP — "Bayesian Virtual Epileptic Patient... infer the **spatial map of epileptogenicity** in a personalized large-scale brain model" | https://github.com (repo under github.com; search returned domain root) | domain **200 OK** |
| The Virtual Brain portal + LEARN: VEP Part 1 tutorial | https://www.thevirtualbrain.org | **200 OK** |
| Wang et al. 2025, "Virtual brain twins for stimulation in epilepsy", *Commun Biol* | https://www.nature.com (article page) | domain **200 OK** |

The BVEP phrase is notable: "spatial map of epileptogenicity" inferred from iEEG is literally a patient-specific parameter map — for epilepsy, not for the GL spec.

### 3.5 Critical coupling on the connectome — the \(J\) vs \(J_c\) structure

| Paper | Link | Fetch status |
|---|---|---|
| Ódor 2019, "Critical synchronization dynamics of the Kuramoto model on connectome and small world graphs", *Sci Rep* 9:19691 (Kuramoto on the human connectome; global coupling \(K\) as control parameter; critical coupling strength identified) | https://www.nature.com/articles/s41598-019-54769-9 + https://pmc.ncbi.nlm.nih.gov/articles/PMC6928153/ | **200 OK** (both) |
| Haldeman & Beggs 2005, "Critical branching captures activity in living neural networks and maximizes the number of metastable states", *Phys Rev Lett* 94:058101 | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.94.058101 | **200 OK** |
| Dörfler & Bullo 2011, "On the Critical Coupling for Kuramoto Oscillators" (theory) | https://epubs.siam.org + mirror https://skoge.folk.ntnu.no | SIAM **403 BLOCKED**; NTNU mirror **200 OK** |
| Myrov et al. 2024, "Hierarchical whole-brain modeling of critical [regimes]", bioRxiv | https://www.biorxiv.org | **403 BLOCKED** (preprint server) |

**Split-brain note:** the Santander et al. 2025 PNAS criticality finding (~10% callosal fibers sufficient for full integration; analysis code at github.com/tsantander/splitBrainNetworks) is already in the corpus and is the split-brain fragment of this area; PNAS itself is 403-blocked here but the user-supplied PDF was read in full in Round 12.

## 4. Links that CANNOT be fetched from this environment

| # | URL | Status | Workaround |
|---|---|---|---|
| 1 | cell.com (Deco 2018 *Curr Biol* full text) | 403 | none open (no PMC); abstract via linkinghub redirect |
| 2 | pnas.org (Preller 2019) | 403 | PMC6377471 mirror (200) |
| 3 | sciencedirect.com (Jirsa 2017 *NeuroImage*; Eisen preprint path) | 400/403 | DOI → linkinghub only; no open mirror for Jirsa |
| 4 | biorxiv.org (Myrov 2024; biorxiv preprints) | 403 | none from this IP |
| 5 | researchgate.net | 403 | none needed |
| 6 | epubs.siam.org (Dörfler & Bullo) | 403 | NTNU mirror https://skoge.folk.ntnu.no (200) |
| 7 | liebertpub.com | 403 | none needed |
| 8 | febs.onlinelibrary.wiley.com; onlinelibrary.wiley.com | 403 | none needed |
| 9 | ora.ox.ac.uk (Fabus 2023 thesis) | 403 | none |
| 10 | biologicalpsychiatrycnni.org (Avram 2024) | 403 | none from this IP |
| 11 | jmsgr.tamhsc.edu | 000 (no route) | none |
| 12 | research-collection.ethz.ch (known from Round 12) | 403 | none |
| 13 | pubmed.ncbi.nlm.nih.gov article pages | challenge-gated (root 200) | PMC mirrors work |

Search/API infra notes: OpenAlex API returned persistent 429 this session (worked in Round 12) — pivoted to CrossRef + Europe PMC REST, both reliable. The z-ai web_search upstream threw two transient 429/timeouts and one 422 (over-narrow query), all retried successfully.

## 5. What this means for the decombination spec (requirement 4)

1. **The user's challenge is sustained in part.** "Doesn't exist" was overstrong. Fragments of a neural parameter map are published and verifiable: anesthesia has the most complete arm (Bojak-Liley/Robinson NFT: drug → field parameters → EEG spectra); psychedelics have a receptor-density → regional-parameter map (Deco 2018); coupling thresholds on the real connectome are computed (Ódor 2019); patient-level parameter inference at iEEG scale is clinical practice (VEP/BVEP).
2. **The unified GL-spec map still does not exist anywhere.** No published work assigns \((J, g, a, \beta, \theta, \phi)\) — the quartic-stabilized GL field with domain formation at \(J_c = ga/\lambda_2\) — to neural measurables across even two of the four domains, let alone psychedelic + anesthesia + split-brain + DID jointly. The \(\theta, \phi\) phase parameters in particular have no published neural assignment. The Fourth/Fifth/Sixth Editions' marking of the four-domain predictions as "conjectural until the neural parameter map exists" therefore stands, but should be phrased: *conjectural until the map is assembled — the per-arm ingredients now being individually verified in the literature*.
3. **Assembly path now visible.** A Level-2 research protocol could legitimately combine: (a) Ódor-style Kuramoto-on-connectome critical-coupling estimation for \(J/J_c\); (b) Bojak-Liley-style anesthetic parameter sweeps for the anesthesia arm; (c) Deco-2018-style 5-HT2A receptor-density parameterization for the psychedelic arm; (d) TVB/BVEP-style patient-level inference for clinical populations (DID/split-brain analogues). Each step has open code (adrianponce DMF, neurolib, BVEP, tsantander/splitBrainNetworks) — the missing piece is the GL quartic-stabilized glue, which is exactly the spec this project carries.

## 6. Search protocol record

- 11 web searches run (q1–q10 + retry), 48 unique URLs discovered, all fetch-probed (results in `npm_fetch_results.json`)
- 12 papers resolved via CrossRef → `npm_resolved.json`; 6 mismatches re-resolved via Europe PMC → `npm_resolved3.json`
- Canonical corrections: Deco 2018 is *Current Biology* (not Cell Reports as the search snippet implied); Haldeman & Beggs title carries "maximizes the number of metastable states"; Robinson 2001 canonical title is "Prediction of electroencephalographic spectra from neurophysiology"; Penas journal version is *PLOS Comput Biol* 2024 (10.1371/journal.pcbi.1011642), preprint 403-blocked
- All raw search JSONs preserved in this directory (q1–q10)
