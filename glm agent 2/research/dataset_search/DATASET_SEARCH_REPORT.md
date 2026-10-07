# Dataset Search Report — Level-2 Protocol Domains
## (psychedelics / anesthesia / split-brain / DID)

Date: 2026-10-08 · Method: z-ai web_search (4 rounds, ~15 queries) + OpenNeuro GraphQL
`advancedSearch(keywords:[...])` enumeration (20+ terms) + PhysioNet topic catalog +
Zenodo REST API + Mendeley internal API probe + link-by-link curl fetch test (31 links).

---

## 1. Psychedelics — OPEN DATASETS (all verified fetchable)

| # | Dataset | Link | Fetch |
|---|---------|------|-------|
| 1 | Psilocybin Precision Functional Mapping (Psilocybin desynchronizes the human brain) — OpenNeuro ds006072, v1.2.0 | https://openneuro.org/datasets/ds006072/versions/1.2.0 | 200 ✓ (GraphQL: public, snapshot 1.2.0) |
| 2 | PsiConnect — multimodal psilocybin study — OpenNeuro ds006110 (latest v1.2.2) | https://openneuro.org/datasets/ds006110/versions/1.2.0 | 200 ✓ |
| 3 | Neural correlates of the LSD experience (multimodal MEG/fMRI) — OpenNeuro ds003059, v1.0.0 | https://openneuro.org/datasets/ds003059/versions/1.0.0 | 200 ✓ |
| 4 | DMT-HAR-MED: DMT + harmine during meditation, fMRI — OpenNeuro ds006644, v1.0.1 | https://openneuro.org/datasets/ds006644/versions/1.0.1 | 200 ✓ |
| 5 | HaD-PET: DMT + harmine cerebral glucose metabolism, FDG-PET — OpenNeuro ds007768, v1.0.0 | https://openneuro.org/datasets/ds007768 | 200 ✓ |
| 6 | NIMH Ketamine Mechanism of Action Study — OpenNeuro ds005917, v1.1.0 | https://openneuro.org/datasets/ds005917 | 200 ✓ |
| 7 | LSD & psilocybin complexity results (fractal dimension, Lempel-Ziv) — Mendeley zxt5zsfhjr | https://data.mendeley.com/datasets/zxt5zsfhjr/1 | 200 ✓ (derived metrics, not raw) |
| 8 | PsiConnect mirror on NEMAR (EEG/MEG portal) | https://nemar.org/dataset/on006110 | 200 ✓ |

## 2. Anesthesia — OPEN DATASETS (all verified fetchable)

| # | Dataset | Link | Fetch |
|---|---------|------|-------|
| 1 | Behavioral & autonomic dynamics during propofol unconsciousness — PhysioNet | https://physionet.org/content/propofol-anesthesia-dynamics/ | 200 ✓ |
| 2 | EEG dynamics during unconsciousness mediated by GABAergic anesthetics — PhysioNet | https://physionet.org/content/eeg-gaba-anesthesia/1.0.0/ | 200 ✓ |
| 3 | Multitaper spectra during GABAergic anesthetic unconsciousness — PhysioNet | https://physionet.org/content/eeg-power-anesthesia/1.0.0/ | 200 ✓ |
| 4 | Michigan Human Anesthesia fMRI Dataset-1 (propofol) — OpenNeuro ds006623 | https://openneuro.org/datasets/ds006623 | 200 ✓ |
| 5 | Repeated awakening study; complexity measures & dreaming — OpenNeuro ds005620 | https://openneuro.org/datasets/ds005620/versions/1.0.0 | 200 ✓ |
| 6 | Anesthesia-induced LOC biomarkers of conscious awareness — OpenNeuro ds003171, v2.0.1 | https://openneuro.org/datasets/ds003171 | 200 ✓ |
| 7 | Multimodal EEG-fNIRS under general anesthesia — OpenNeuro ds004541 | https://openneuro.org/datasets/ds004541 | 200 ✓ |
| 8 | INSPIRE perioperative research dataset — PhysioNet | https://physionet.org/content/inspire/1.4.2/ | 200 ✓ |
| 9 | VitalDB intraoperative multi-parameter database — PhysioNet | https://physionet.org/content/vitaldb/1.0.0/ | 200 ✓ |
| 10 | Multimodal physiological indices during surgery — PhysioNet | https://physionet.org/content/multimodal-surgery-anesthesia/1.0/ | 200 ✓ |
| 11 | JSMF ACCESS intraoperative derived EEG — PhysioNet | https://physionet.org/content/jsmf-access/1.0.0/ | 200 ✓ |
| 12 | Cambridge repository: brain connectivity during propofol sedation (research data) | https://www.repository.cam.ac.uk/items/b7817912-50b5-423b-882e-978fb39a49df | 200 ✓ |
| 13 | EDA awake vs sedation — PhysioNet | https://physionet.org/content/eda-rest-sedation/1.0/ | 200 ✓ (note: /1.0.0/ → 404; correct version is /1.0/) |

## 3. Split-brain — NO OPEN RAW DATASET FOUND

- OpenNeuro keyword enumeration: `split-brain`, `callosotomy`, `commissurotomy` → **zero hits**.
- PhysioNet, Zenodo, Mendeley, NITRC: no split-brain patient data.
- Reality: the callosotomy patient pool is tiny (famous cases: RV, NG, VP, JW, etc.);
  data are case-study level, shared only within lab collaborations; privacy constraints.
- Closest OPEN adjacent corpora (verified fetchable):
  - IDEAS — Imaging Database for Epilepsy and Surgery: https://openneuro.org/datasets/ds005602 (200 ✓)
  - IDEAS II (diffusion MRI + connectivity): https://openneuro.org/datasets/ds007401 (200 ✓)
  - (Epilepsy presurgical cohorts occasionally include callosotomy candidates; not guaranteed.)
- Key literature (fetchable where URL resolved): PMC3607036 (EEG signatures of loss/recovery
  of consciousness) ✓; PNAS "Full interhemispheric integration sustained by a fraction of
  callosal fibers" — full URL NOT resolvable via the search backend (returns domain-only
  "https://www.pnas.org"); reachable via PubMed/EuropePMC search from a normal browser.

## 4. DID — NO OPEN RAW NEUROIMAGING DATASET FOUND (papers + false positives only)

- OpenNeuro: no DID dataset (keyword matches were all associative-learning noise).
- NFED-fmri (Zenodo 13759829): **VERIFIED FALSE POSITIVE** — it is a facial-expression
  fMRI dataset ("Naturalistic Facial Expressions Dataset"), unrelated to DID. Fetchable
  (200 ✓) but must be excluded from the DID domain.
- Fetchable DID literature:
  - Schlumpf et al. 2014, PLOS ONE — Dissociative Part-Dependent Resting-State Activity
    in DID: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0098795 (200 ✓)
  - Functional Neuroimaging in Dissociative Disorders (review):
    https://pmc.ncbi.nlm.nih.gov/articles/PMC9502311/ — **BLOCKED** (see §5).
- KCL "computers can spot the difference" (machine-learning DID classification) —
  news page URL not resolvable via search backend (domain-truncated).

## 5. LINKS THAT CANNOT BE FETCHED (from this environment)

| Link | Symptom | Notes |
|------|---------|-------|
| https://pmc.ncbi.nlm.nih.gov/articles/PMC9502311/ | HTTP 200 but reCAPTCHA bot-wall ("Checking your browser"); headless browser also blocked | PerimeterX-style protection; Europe PMC mirror https://europepmc.org/article/PMC/PMC9502311 → 403 Cloudflare "Just a moment…" |
| https://physionet.org/content/eda-rest-sedation/1.0.0/ | 404 | Wrong version path — corrected URL https://physionet.org/content/eda-rest-sedation/1.0/ works (200) |
| (unresolved) "EEG correlates of psychoactive ketamine" (Mendeley) | Search backend returns domain-only URL; Mendeley internal API ignores query params | Dataset exists per search snippet but full URL not resolvable from here |
| (unresolved) PNAS "Full interhemispheric integration sustained by a fraction of callosal fibers" | Search backend returns domain-only URL | Resolve via PubMed from a normal browser |
| (unresolved) ETH research-collection DID fMRI study; KCL DID news item | Search backend returns domain-only URLs | Same limitation |

Search-tool limitation recorded: the z-ai web_search backend persistently truncates many
result URLs to bare domains (e.g., `https://github.com`, `https://www.pnas.org`), which is
why some paper/dataset links above could not be pinned to full URLs. All links that WERE
pinned were fetch-tested: 31/31 returned HTTP 200 with correct content after the one
version-path correction; the only content-level block is the PMC bot-wall.

## 6. Cross-domain aggregators (all fetchable)

- FieldTrip open MEG/EEG data list: https://www.fieldtriptoolbox.org/faq/other/open_data/ ✓
- openlists/ElectrophysiologyData (GitHub): https://github.com/openlists/ElectrophysiologyData ✓
- Harvard Brain Data Science Platform (BIND): https://bdsp.io ✓
- NITRC-IR: https://www.nitrc.org ✓

## 7. Implication for the Level-2 protocol (decombination.txt, final spec)

The four empirical domains map to data availability as follows:
- Psychedelics: strong open coverage (psilocybin ×2, LSD, DMT ×2, ketamine) — the μ/J
  integration-parameter predictions are testable against open data today.
- Anesthesia: strongest open coverage (GABAergic EEG ×2, propofol fMRI/EEG/behavior,
  multi-agent intraoperative corpora) — the "alters dissolve" prediction is testable now.
- Split-brain: NO open raw data — predictions remain confined to published case-study
  summaries; would require new data-sharing agreements with the few remaining labs.
- DID: NO open raw neuroimaging data — same situation; only summary-level literature.
This asymmetry is itself evidence for the file's own caveat: the psychedelic/anesthesia/
split-brain/DID predictions are marked **conjectural** until a principled
(J, g, a, β, θ, φ) → neural-observable parameter map is supplied (requirement #4).
