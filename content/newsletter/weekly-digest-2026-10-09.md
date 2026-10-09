---
title: "Weekly Digest: Oct 05 - Oct 09, 2026"
date: 2026-10-09
description: "A curated summary of the top protein engineering and structure prediction signals from Oct 05 - Oct 09, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Oct 05 - Oct 09, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Oct 09

### [Systematic benchmarking of AlphaFold and SWISS-MODEL kinase structures for structure-based drug discovery.](https://doi.org/10.1016/j.jmgm.2026.109571)
#### 🧬 Abstract
Accurate protein structure prediction is fundamental to structure-based drug discovery. However, the practical performance of deep learning-based models such as AlphaFold compared with traditional homology modeling approaches like SWISS-MODEL remains incompletely evaluated in realistic drug-design workflows. Here, we systematically benchmark AlphaFold2 and SWISS-MODEL using a curated dataset of 20 kinase structures with co-crystallized ligands. Predicted models were evaluated under three conditions: the raw predicted structures, structures subjected to energy minimization, and structures subjected to triplicate 100-ns unbiased molecular dynamics (MD) simulations for structural refinement. Model performance was assessed using structural accuracy metrics, multi-software docking (AutoDock Vina, AutoDock, and MOE), and post-docking MD trajectory stability analysis, together with MM/GBSA binding energy estimation. As expected, experimental structures consistently showed the best docking performance. Among predicted models, SWISS-MODEL produced slightly lower RMSD values and better interaction similarity than AlphaFold, although overall docking scores were statistically comparable. MD refinement prior to docking reduced structural suitability by increasing binding-pocket deviations and was associated with misoriented ligand poses in subsequent docking calculations, while energy minimization provided little to no improvement. Notably, the reduction in docking performance was not limited to computationally predicted structures but was also observed for experimental structures solved in complex with different ligands. Thus, rigid docking alone tended to generate a substantial number of false-positive poses. However, MD simulations applied after docking effectively identified unstable ligand poses and reduced false-positive predictions by detecting ligand dissociation. Overall true-positive rates were 30% for SWISS-MODEL and 35% for AlphaFold2. These findings highlight the importance of dynamic validation in structure-based drug discovery workflows.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Oct 09

- **[Comparative benchmarking of template-based, evolutionary-diffusion, and generative language models for IsPETase structure prediction.](https://doi.org/10.1142/s0219720026510029)**: Accurate protein structure prediction is critical for rational enzyme engineering, which requires high-fidelity models. This study benchmarks three distinct structure prediction paradigms against the experimental crystal structure of IsPETase, serving as a...
- **[PreFold-dG: estimating binding affinity of protein-protein interaction from intermediate representations of protein folding model.](https://doi.org/10.1093/bioinformatics/btag489)**: Motivation Binding affinity governs how proteins interact and underlies essential biological processes. Computational approaches have been developed to simulate and predict protein binding, but the scarcity of high-quality data has imposed significant...
- **[Molecular Docking of Natural Products: Critical Appraisal of Current Methodology and Practical Guidelines.](https://doi.org/10.3390/molecules31183228)**: Molecular docking is among the most widely used techniques in structure-based drug discovery and has become integral to natural-product research. Despite substantial advances in computational algorithms and artificial intelligence, the methodological...
- **[Adversarial Sequence Mutations in AlphaFold and ESMFold Reveal Nonphysical Structural Invariance, Confidence Failures, and Concerns for Protein Design.](https://doi.org/10.34133/csbj.0142)**: AlphaFold has transformed structural biology and spawned an ecosystem of derivative tools for protein design, binding prediction, and drug discovery. However, whether AlphaFold has learned generalizable biophysical principles as opposed to template-based...
- **[Identification of Potential SARS-CoV-2 Main Protease (MPro) Inhibitors Through Pharmacophore Modeling, Molecular Docking, and Molecular Dynamics Simulation Approaches.](https://doi.org/10.3390/ijms27177684)**: The main protease (MPro) of coronaviruses (CoVs) is an essential enzyme involved in viral replication and represents an attractive target for antiviral drug discovery. Based on the similar binding pocket residues within the MPro of different CoVs, this...
- **[Advancing In Silico Drug Design with Bayesian Refinement of AlphaFold Models.](https://doi.org/10.1021/acs.jctc.6c00868)**: Virtual screening has become an indispensable tool in modern structure-based drug discovery, enabling the identification of candidate molecules by computationally evaluating their potential to bind target proteins. The accuracy of such screenings...
- **[Incorporating Surfaced-Induced Dissociation Mass Spectrometry Data into an AlphaFold-derived deep learning network improves protein structure prediction](https://doi.org/10.64898/2026.06.26.734850)**: Surface-Induced Dissociation native Mass Spectrometry (SID-nMS) is a tandem MS activation method that yields information on the connectivity and stoichiometry of protein complexes. While insufficient for direct structure elucidation, the data derived from...
- **[Role of Artificial Intelligence in bioinformatics: Revolutionizing molecular docking and DNA tokenization.](https://doi.org/10.1016/j.compbiolchem.2026.109217)**: Bioinformatics has become a crucial discipline that connects biology and computational analysis, extracting meaningful insights from complex biological datasets. Traditional bioinformatics approaches, which rely on statistical models and manual analysis,...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [MMseqs2](https://github.com/soedinglab/MMseqs2) - Fast and sensitive sequence search and clustering suite.
- 🛠 **Tool**: [HHSuite](https://github.com/soedinglab/hh-suite) - Remote homology detection with HMM-HMM comparison.
- 💾 **Dataset**: [BioLiP](https://zhanggroup.org/BioLiP/) - Verified biologically relevant ligand-protein interactions.
- 💾 **Dataset**: [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/) - Residue-level mapping between PDB, UniProt, and other resources.

---

## 🤖 AI in Research Recap

- **[Sponsored: We’ve Always Copied Nature. Now We Can Search It. - SingularityHub](https://news.google.com/rss/articles/CBMijgFBVV95cUxQUmhSUGRNSS1ydjlBa3lQZlRqcXRzbS1Kb2JsdnBvZ0dKdHRoSEw5Uk1vME12R25rcmJfMjhqUDhWZGZUOWNJTzFucUZYUzZMVlZweFhvRE56a2RCN3hpS1NjcTJvMHAzM19sVk4xOUdRVGhHMmhyTnY2X1RZZTFDZGZRZVhJU3NGREtmUnJn?oc=5&hl=en-US&gl=US&ceid=US:en)**: Sponsored: We’ve Always Copied Nature. Now We Can Search It. &nbsp;&nbsp; SingularityHub
- **[ELRIG and The Protein Society announce keynote speakers for protein sciences in Drug Discovery 2026 - Cambridge Network](https://news.google.com/rss/articles/CBMixwFBVV95cUxNNVFyR3R2R1R4UWwzblFLemZZZHdQd24wb2JEV2g4QnFEUWtMWHdqU2ItU2lBOW5iYVBQbC0xZkliYXg5MzlMWDU0N2dNLWtoX24taWlaXzItcnBxTEFzV01xN0gySklPUWpEVWR5dlJMaVk5TW90ZXktdXVGSUhjeWxaUjFfU0JmamMxVU1FaWJnN1NZb1UwcW5za29Vb01GUkJlaG9XaUR2OGJYYlNVS3oweGt2bERfUV9saFFSMjIta2FJT0Iw?oc=5&hl=en-US&gl=US&ceid=US:en)**: ELRIG and The Protein Society announce keynote speakers for protein sciences in Drug Discovery 2026 &nbsp;&nbsp; Cambridge Network
- **[Nobel-winning AI scientist John Jumper said he was leaving Google DeepMind for Anthropic, drawing praise from Google AI chief Demis Hassabis | Hindustan Times - Hindustan Times](https://news.google.com/rss/articles/CBMiuAJBVV95cUxNc3FwNm9aOTJ6d3VaT2xYYlBkR3phNW53Q19uVVo4TUZtOGRaNUVqQk5najBZalN2MTRRV3MzSHMzcGNzUlVubzVzSDhGQmhVVHRnR3lrYm5GX1J5Si1kWXBQZ01fYmlUT3RNaW0tTTJIOG1CVlZNcEl3c1E1Z09hSE9Ibk5NRjgtT2E3aUctLWRFWGZ1bjg4ZTh6anp2aDB4YVRrckJ1QndpRkIwOVo0blRFWjB4bGJydEZ3QzJ4T1JDbG90MGVLM3BqbS1yRlVUcmE2Zm1DT2U4Qk1uajR4aGhocENSeHZaN3czOHBvZ3NzY2k5ekVmYlo5U3o5bE1rVzZrZjVsZm5adEplb2RNcm9MVkw0cWhWOWJOd3VidmU1dTBpWFVrbkhvSF9jUEJqLS1KRDJCSnXSAbgCQVVfeXFMTXNxcDZvWjkyend1Wk9sWGJQZEd6YTVud0NfblVaOE1GbThkWjVFakJOZ2owWWpTdjE0UVdzM0hzM3Bjc1JVbm81c0g4RkJoVVR0Z0d5a2JuRl9SeUotZFlwUGdNX2JpVE90TWltLU0ySDhtQlZWTXBJd3NRNWdPYUhPSG5OTUY4LU9hN2lHLS1kRVhmdW44OGU4emp6dmgweGFUa3JCdUJ3aUZCMDlaNG5URVoweGxicnRGd0MyeE9SQ2xvdDBlSzNwam0tckZVVHJhNmZtQ09lOEJNbmo0eGhoaHBDUnh2Wjd3Mzhwb2dzc2NpOXpFZmJaOVN6OWxNa1c2a2Y1bGZuWnRKZW9kTXJvTFZMNHFoVjliTnd1YnZlNXUwaVhVa25Ib0hfY1BCai0tSkQyQkp1?oc=5&hl=en-US&gl=US&ceid=US:en)**: Nobel-winning AI scientist John Jumper said he was leaving Google DeepMind for Anthropic, drawing praise from Google AI chief Demis Hassabis | Hindustan Times &nbsp;&nbsp; Hindustan Times
- **[CAS academician gives talk at UM on development of structural biology - University of Macau](https://news.google.com/rss/articles/CBMifkFVX3lxTFAzSnRPVkt6RmROQmI5MDFIU25rWnpLWTZhWDZpV1B1SHdlWmVacFJSd0lwS0V0VDFENURSNlp6bWN6d2hOeDNrTWRadWh2eUcxdnRJQkZzRURBaXN2cUV0MnpXSVNJUmJ4RTRJOWRISUZjRTFzTXNSUUtnWkJ1dw?oc=5&hl=en-US&gl=US&ceid=US:en)**: CAS academician gives talk at UM on development of structural biology &nbsp;&nbsp; University of Macau
- **[Isomorphic Labs seeks funding at a valuation of at least $40 billion - Startup Fortune](https://news.google.com/rss/articles/CBMimwFBVV95cUxNNENWWFllV1hqNFhrSEppLXNvQ2NheVlhWmhaUFJpc29LS0s4MnE0N29ldU1XSXlOSks5T0owVHpHLVJQYklLNk1HeFJIeGVfWWxKci1sWEFpS2FxV2lxTGxldDQzakZETUdRQk51M0gwR2owTkVkSHF4Wll2dElBV2wweUVpLXU2M1JtUGV6X3g1eVB0TjlzbE9pOA?oc=5&hl=en-US&gl=US&ceid=US:en)**: Isomorphic Labs seeks funding at a valuation of at least $40 billion &nbsp;&nbsp; Startup Fortune
- **[Alphabet's AI Drug Discovery Unit Isomorphic Labs Reportedly Seeking Funding at $40 Billion Valuation - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE12MHBXbTA1Ry1Lb05pUkgtNzlkWVJ4WjVnRXl2MGdzaV9HN1ZkOC1WaWVlM3dkQ1N3WERPcGZkLWRTUkgxcmlqczBjOHlQdWRWVVdUOFlFZXkzRFAxN015and0Z2ZfTENtVkNadXFGVXotSUR1dHc?oc=5&hl=en-US&gl=US&ceid=US:en)**: Alphabet's AI Drug Discovery Unit Isomorphic Labs Reportedly Seeking Funding at $40 Billion Valuation &nbsp;&nbsp; BigGo Finance

---

## 🏢 Industry & Real-World Applications

- **[TRex Bio prices $117M IPO to support immune drug work - BioPharma Dive](https://news.google.com/rss/articles/CBMihwFBVV95cUxPNzJTR0dGZnpMZTltNHBBcGlYYWRSV2w2aGxDYWhwRjFkWklYVjNBRWNMOHFOUl9Ed2RhRGZUZ2hKRDJ6MmVzRnFBeHg4cENiWExLT3NzcVlhUkw4TTdXQWdNOGI2SVBGa2VRUDljX0FxY0tocGhDT1RHX1BNTzVhQkxndkxYQmc?oc=5&hl=en-US&gl=US&ceid=US:en)**: TRex Bio prices $117M IPO to support immune drug work &nbsp;&nbsp; BioPharma Dive
- **[ELRIG and The Protein Society announce keynote speakers for protein sciences in Drug Discovery 2026 - Cambridge Network](https://news.google.com/rss/articles/CBMixwFBVV95cUxNNVFyR3R2R1R4UWwzblFLemZZZHdQd24wb2JEV2g4QnFEUWtMWHdqU2ItU2lBOW5iYVBQbC0xZkliYXg5MzlMWDU0N2dNLWtoX24taWlaXzItcnBxTEFzV01xN0gySklPUWpEVWR5dlJMaVk5TW90ZXktdXVGSUhjeWxaUjFfU0JmamMxVU1FaWJnN1NZb1UwcW5za29Vb01GUkJlaG9XaUR2OGJYYlNVS3oweGt2bERfUV9saFFSMjIta2FJT0Iw?oc=5&hl=en-US&gl=US&ceid=US:en)**: ELRIG and The Protein Society announce keynote speakers for protein sciences in Drug Discovery 2026 &nbsp;&nbsp; Cambridge Network
- **[Institute for Protein Design receives AI computing power - UW Medicine | Newsroom](https://news.google.com/rss/articles/CBMimgFBVV95cUxPZW9UeTh0SmhJbEdlRllnNWtfeUFidm9SYnFGV1hfNDM4UHhaLVFkSWFFcFJqN1YzM21WLWJraklPMHQtZ2FqNHRYcUg4bjRxaTNoWTVLd1FhelMxVXBfU2FNLUZJREI5X1hCaXJfQVdCOThkR01SSm15SHBwR1RqMVVkekRTYlcwTXFFSnItQTQtcWlkVWRnX3d3?oc=5&hl=en-US&gl=US&ceid=US:en)**: Institute for Protein Design receives AI computing power &nbsp;&nbsp; UW Medicine | Newsroom
- **[Roche taps Chinese biotech Defand in reported $1B deal - European Biotechnology Magazine](https://news.google.com/rss/articles/CBMiowFBVV95cUxOMGZScFZHbVVHYTBHVzZxSFAzendYZVhtNE9aSVdXQkFHNlBHbXR1ZnRoaUNNWXpBNGZOWmxDWEZ2WFJfUy15TkZzNnF1WXRjeGJlLTgyOFU0WFBEZGtIbE9yZ0hMTExWVGxvbVdmdFkyb0l4ZklMYTJ1czJkX1hza3ZzcFQza0k2c3d5WFFBd19hLVZKLTNRN1JSeGpnQTAwOTFj?oc=5&hl=en-US&gl=US&ceid=US:en)**: Roche taps Chinese biotech Defand in reported $1B deal &nbsp;&nbsp; European Biotechnology Magazine
- **[Roche goes beyond licensing in deal with Chinese biotech - STAT](https://news.google.com/rss/articles/CBMiqgFBVV95cUxQUkhyXzM0RVBsbEc5ZGJGZ05FeXJGOUJkREhKeWVEb1JOVVBfVmFUM0Zxdks0TUphdDFtWHJsMFpQM1NIcURNa1R1SFFMalItQXhUWjlWZE1qaUZWcmhDV3MzMFRpU3pmSEJRMmd6dGs2RTlBSVBOMU1KZkYxVk93UC1mX2hETjdWSlRDWlJmMkw3cXkxM3E4ZFk0Y2lSQk1oT0tMemVuYURsUQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Roche goes beyond licensing in deal with Chinese biotech &nbsp;&nbsp; STAT
- **[Forging a Transatlantic Biotechnology Partnership to Confront the China Challenge - Center for European Policy Analysis (CEPA)](https://news.google.com/rss/articles/CBMivAFBVV95cUxOMW1GMGJidGx0QlE0bG9nZmFabVNRTmdtdlJ5cE10UUFvUjRBamhtOHdhWnBhb1RBakNMSkFPZTRHUm55LWhHdlE5eDhrc0dJZmhpbHk3eTJjX0tldlRNLUt3T1AtNHpzX3V0VUlwQ0VBWHIzLVQ1ZVBocDluU08xTzdnTmdQdnZwSUoyekZoYnJEdjRhR2dib1BYYS1LdmVfS3pVZGFndmIzMmtLTUh6cDB3cGYtYno1LTQycA?oc=5&hl=en-US&gl=US&ceid=US:en)**: Forging a Transatlantic Biotechnology Partnership to Confront the China Challenge &nbsp;&nbsp; Center for European Policy Analysis (CEPA)
- **[Protein sciences in drug discovery 2026 - News-Medical](https://news.google.com/rss/articles/CBMikAFBVV95cUxOR2p2THN4REdjX1FMdldpTXlwREM4ZWMxZlFOMDlHVkc4c0twS0FuSUROcFhEbVJCQ2MtSndoX0FZaEIyY2VnOGNkX2JqQ1lsTU5HbWVJZlpfeW1kSlRGN3dFTFZMaS1SUzVYSlVGaFUwN25uOWhVV2dpQWo0YzI5MU1iWWV6ci1LSHV5NVZ6S00?oc=5&hl=en-US&gl=US&ceid=US:en)**: Protein sciences in drug discovery 2026 &nbsp;&nbsp; News-Medical

---

## 💼 Jobs & Opportunities

- **[Benchmarking cell segmentation in two Spatialomics platforms with open-source software - Nature (Nature Careers)](https://news.google.com/rss/articles/CBMiX0FVX3lxTE0zQzBoWVNTSUE5djAtYTA2RVRCWllSTmZBTnJxOVZBbEtRUFlTMTNEQUQ2VlEtQURpeHlIcGEyWjVEQno5ZUNiVGZ0Slo4MzB0YnQtVDVkSWdzc1RpMFBB?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Transmembrane PhoxID: photoproximity labelling across the plasma membrane in vivo - Nature (Nature Careers)](https://news.google.com/rss/articles/CBMiX0FVX3lxTE83b1hkQmZVc3huUVZWX19Xa3pnXzJmNVFzWlNwbGp6bi1obWc4OWNSVGJ1enRaeXU1ZzZzdTMyRmdOalFUbUpZM0RsUWxaSnRjZGZPYzg4cmU1U3RoWmRF?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**
- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
