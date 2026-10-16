---
title: "Weekly Digest: Oct 12 - Oct 16, 2026"
date: 2026-10-16
description: "A curated summary of the top protein engineering and structure prediction signals from Oct 12 - Oct 16, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Oct 12 - Oct 16, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Oct 16

### [Systematic benchmarking of AlphaFold and SWISS-MODEL kinase structures for structure-based drug discovery.](https://doi.org/10.1016/j.jmgm.2026.109571)
#### 🧬 Abstract
Accurate protein structure prediction is fundamental to structure-based drug discovery. However, the practical performance of deep learning-based models such as AlphaFold compared with traditional homology modeling approaches like SWISS-MODEL remains incompletely evaluated in realistic drug-design workflows. Here, we systematically benchmark AlphaFold2 and SWISS-MODEL using a curated dataset of 20 kinase structures with co-crystallized ligands. Predicted models were evaluated under three conditions: the raw predicted structures, structures subjected to energy minimization, and structures subjected to triplicate 100-ns unbiased molecular dynamics (MD) simulations for structural refinement. Model performance was assessed using structural accuracy metrics, multi-software docking (AutoDock Vina, AutoDock, and MOE), and post-docking MD trajectory stability analysis, together with MM/GBSA binding energy estimation. As expected, experimental structures consistently showed the best docking performance. Among predicted models, SWISS-MODEL produced slightly lower RMSD values and better interaction similarity than AlphaFold, although overall docking scores were statistically comparable. MD refinement prior to docking reduced structural suitability by increasing binding-pocket deviations and was associated with misoriented ligand poses in subsequent docking calculations, while energy minimization provided little to no improvement. Notably, the reduction in docking performance was not limited to computationally predicted structures but was also observed for experimental structures solved in complex with different ligands. Thus, rigid docking alone tended to generate a substantial number of false-positive poses. However, MD simulations applied after docking effectively identified unstable ligand poses and reduced false-positive predictions by detecting ligand dissociation. Overall true-positive rates were 30% for SWISS-MODEL and 35% for AlphaFold2. These findings highlight the importance of dynamic validation in structure-based drug discovery workflows.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Oct 16

- **[Human and zebrafish cross-species comparison on ligand affinity towards the aryl hydrocarbon receptor and Keap1 oxidative stress sensor: a molecular docking dataset.](https://doi.org/10.1016/j.dib.2026.113037)**: Bioanalytical methods targeting adverse cellular outcomes are increasingly used in environmental toxicology, including receptor-mediated toxicity pathways relevant to high-throughput monitoring of drinking water, wastewater, and other environmental...
- **[PreFold-dG: estimating binding affinity of protein-protein interaction from intermediate representations of protein folding model.](https://doi.org/10.1093/bioinformatics/btag489)**: Motivation Binding affinity governs how proteins interact and underlies essential biological processes. Computational approaches have been developed to simulate and predict protein binding, but the scarcity of high-quality data has imposed significant...
- **[Molecular Docking of Natural Products: Critical Appraisal of Current Methodology and Practical Guidelines.](https://doi.org/10.3390/molecules31183228)**: Molecular docking is among the most widely used techniques in structure-based drug discovery and has become integral to natural-product research. Despite substantial advances in computational algorithms and artificial intelligence, the methodological...
- **[Adversarial Sequence Mutations in AlphaFold and ESMFold Reveal Nonphysical Structural Invariance, Confidence Failures, and Concerns for Protein Design.](https://doi.org/10.34133/csbj.0142)**: AlphaFold has transformed structural biology and spawned an ecosystem of derivative tools for protein design, binding prediction, and drug discovery. However, whether AlphaFold has learned generalizable biophysical principles as opposed to template-based...
- **[Identification of Potential SARS-CoV-2 Main Protease (MPro) Inhibitors Through Pharmacophore Modeling, Molecular Docking, and Molecular Dynamics Simulation Approaches.](https://doi.org/10.3390/ijms27177684)**: The main protease (MPro) of coronaviruses (CoVs) is an essential enzyme involved in viral replication and represents an attractive target for antiviral drug discovery. Based on the similar binding pocket residues within the MPro of different CoVs, this...
- **[Advancing In Silico Drug Design with Bayesian Refinement of AlphaFold Models.](https://doi.org/10.1021/acs.jctc.6c00868)**: Virtual screening has become an indispensable tool in modern structure-based drug discovery, enabling the identification of candidate molecules by computationally evaluating their potential to bind target proteins. The accuracy of such screenings...
- **[Protein Language Model Decoys for Target Decoy Competition in Proteomics: Quality Assessment and Benchmarks](https://doi.org/10.64898/2026.03.27.714819)**: Large-scale proteomics relies heavily on target-decoy competition for false discovery rate estimation in peptide identification, and the performance of this strategy depends strongly on the design of the decoy database. Classical generators such as...
- **[Incorporating Surfaced-Induced Dissociation Mass Spectrometry Data into an AlphaFold-derived deep learning network improves protein structure prediction](https://doi.org/10.64898/2026.06.26.734850)**: Surface-Induced Dissociation native Mass Spectrometry (SID-nMS) is a tandem MS activation method that yields information on the connectivity and stoichiometry of protein complexes. While insufficient for direct structure elucidation, the data derived from...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [OpenMM](http://openmm.org/) - GPU-accelerated molecular simulation toolkit.
- 🛠 **Tool**: [AlphaFill](https://alphafill.eu/) - Ligand and cofactor transfer into AlphaFold models.
- 💾 **Dataset**: [SCOPe](https://scop.berkeley.edu/) - Curated structural classification of proteins for fold analysis.
- 💾 **Dataset**: [Pfam](https://pfam.xfam.org/) - Protein families database with curated multiple sequence alignments.

---

## 🤖 AI in Research Recap

- **[Computational Biology Internship at Meril | Apply Online Now - BioTecNika](https://news.google.com/rss/articles/CBMihwFBVV95cUxNYTFHemF3Z0EzZTBmWU12STVnS0lYRktVS2VGUlhsTE9EVUI0R2pDRVVseGljVnJMRXlEUTBKR096eG5wODBtRmkxd1hmclJMOGtpazNiZ3V1ODVvbEpWc0k0bWx2NFBYLUFoM0NIM3ZzYlEwRzhuTFNoTW5aUzV5alg2emRlb2PSAYwBQVVfeXFMTVBVV1FjZm5SWFNNOGJZVE9JS1JUOEZXemwwMUtIc0U5MnNGODZkUHlsSEFhbG9ESTBNU2staV9tdk9FT3RSVk1GcUFCdzdZYkFVci0tWEVXZEw1QU54QmZjRTQxV3JKWkIyY3BRbE5vWnk0eDNobkQ0VE9iQXQ0S3l6SWRZNDNZR3BINC0?oc=5&hl=en-US&gl=US&ceid=US:en)**: Computational Biology Internship at Meril | Apply Online Now &nbsp;&nbsp; BioTecNika
- **[Google Opens Advanced AI Models to 200 European Researchers, Providing $3 Million in Compute Resources - BigGo Finance](https://news.google.com/rss/articles/CBMidkFVX3lxTE10MFlEekFsZDh4ckZFVUZYQ0RFQW1lTkhzMnptaURvNko0Sk04T1lCTFBiM1RmTXlzSVBieU9OWko2ejJxamg4ams0UjhQZk1HUWdtd0hqdkpJVnRETm5kMlczVkZ5eEI4YWFUbV9saVJfTi1DRHc?oc=5&hl=en-US&gl=US&ceid=US:en)**: Google Opens Advanced AI Models to 200 European Researchers, Providing $3 Million in Compute Resources &nbsp;&nbsp; BigGo Finance

---

## 🏢 Industry & Real-World Applications

- **[Clinical Forum Insights: When to Escalate to Biologics in Asthma and COPD? - HCPLive](https://news.google.com/rss/articles/CBMilgFBVV95cUxQaFhrVGE0ZFlBV3BfSFI4ZjdrZVBmNUpwUV9QRnlJYWw2NzNLOVo0emFpRGRDWFFtOGVMVG4wSHJyNlZPSzQtVERaVm1uZzFqcE1OZ2JWVlk1VFR4T3JjNzdWN25xdmRpZDYyODNTdWVpZXhfVVozbFhhQ3habHpiVUwyZlJkZV9TZXZoOUluSF9mRGFJTUE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Clinical Forum Insights: When to Escalate to Biologics in Asthma and COPD? &nbsp;&nbsp; HCPLive
- **[AI Biotech Iambic Gets $150M in IPO Cash for ‘Molecular Superintelligence’ Drug R&D - MedCity News](https://news.google.com/rss/articles/CBMipAFBVV95cUxPQ2N2YkpERlRWVzFORko3dlVQZ2tVVjZqZk9Gck51S1JjYlc4NGV3ZEZpdGpoT0l6X3g1UVVHeTdhQjBoQXl3TUQ2UUxFNjBFUVpfSk5VMU1NdXFEUmh5OGVNZ1BIUHUyYWtkRlJQZ1ZyX3RBaUZYbGMwaXh0dHpGR1YzTkNUUEhtWm9yR0toXzN4M1E0cG9KUTdXdldJU1hyeEVrVw?oc=5&hl=en-US&gl=US&ceid=US:en)**: AI Biotech Iambic Gets $150M in IPO Cash for ‘Molecular Superintelligence’ Drug R&D &nbsp;&nbsp; MedCity News
- **[Vir Biotechnology signs Gilead cancer deal with US$90M upfront - Mugglehead Investment Magazine](https://news.google.com/rss/articles/CBMigwFBVV95cUxPOVdaZ0EtenF1RzNJbERfTU9kR3RObFZpSkVPS2tzWXBKQ0FJUjdhekFsRHRUY05EMF81UVYtS0wzYUpPbDBwQVEySWhLbXZINUJ1YzNrbTk5eFhJb3FIdHQwMEZBNWFHYVNoczdoazFUOTl2WDZNcW9SNC1LVjBRSUx4WQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vir Biotechnology signs Gilead cancer deal with US$90M upfront &nbsp;&nbsp; Mugglehead Investment Magazine
- **[Generate, Zealand Sign $1.2B AI Drug Deal - Voice of Healthcare](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNMTdVSmJVT0loeHZnRlotcjlOTU1hWTJRN2JQTl9mWE92SmlrVDZoMjZwSTRBRVczb3BjRjhXdGF4aHlacWNaQTdBRDMtOFpRdlNOUjhrNUcwWUNPcDlIdlJiX2JQdVY0WjloTjJVTzZkN2p5TldGN2FSSzkxbXRxZVpreFRPa1ZvSlkyWjlkZkgtaDhSSWtYRTZBdmxTNlF4enFydTJSOXZyRFBVcndVbXZ2T0NKckpnVW4tVGhwN0loVFhfYzhzNnE4akp6d2RaNG9BMUl4S0U?oc=5&hl=en-US&gl=US&ceid=US:en)**: Generate, Zealand Sign $1.2B AI Drug Deal &nbsp;&nbsp; Voice of Healthcare
- **[Generate Biomedicines and Zealand Pharma Team Up in AI-Driven Obesity Drug Pact Worth Up to $1.2 Billion - finance.biggo.com](https://news.google.com/rss/articles/CBMidkFVX3lxTE1rSnFRN3FvcE1Dc2hNVFNhdTRONmVKbEgxU1VucVNjNVRmYWtGSll5VmxLN21WWjNXQm1wUHdfRzhYRUdZbG91Z1k4NjdIMHZtLTA5Vk9zR2lJdDdqenBDV1ZYWFFEdDdocEZ4QmhNRF92SjN2ZkE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Generate Biomedicines and Zealand Pharma Team Up in AI-Driven Obesity Drug Pact Worth Up to $1.2 Billion &nbsp;&nbsp; finance.biggo.com
- **[IQVIA, Veeva expand on existing partnership for speedier clinical trials - Fierce Biotech](https://news.google.com/rss/articles/CBMikAFBVV95cUxQTEh2dzBwR1EyMk92N0xtRXNyM3FOcGIzUVFaYnhNLWthZnE0dUMwLWtlam9GRmxyWUxMVlM4ekNtZTRtVWxtc1VUR0ltdEdEb2JQMmJrWEY1cDZNRmQza3J4dHdxb0t2am9jWG9wWDBEWm05OGtCeGs1NTFFZFZwc1NVTDV6ZC1yQ24wZFU2OVc?oc=5&hl=en-US&gl=US&ceid=US:en)**: IQVIA, Veeva expand on existing partnership for speedier clinical trials &nbsp;&nbsp; Fierce Biotech
- **[Generate Biomedicines Lands Major AI Drug Partnership to Target Booming Obesity Market - AOL.ca](https://news.google.com/rss/articles/CBMihgFBVV95cUxQaGFlV0xJYVFMdVlmdTlEalA5SjloZ3BzUVU2YmViaWR6ZVFpVnR4YzJ3Q1RoalRCMzI4bFMzaGwwU1pzbEtzX3JXVXZWQXpsaWNiYzhlcWJBbkZRNWV3b1V4eXQ0YnpOM1B5NTNjWms3RnNqZHRDZUpRTFY5dk1aSl9fOGVSUQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Generate Biomedicines Lands Major AI Drug Partnership to Target Booming Obesity Market &nbsp;&nbsp; AOL.ca

---

## 💼 Jobs & Opportunities

- **[Head, AI for Medicines Safety at The Medicines And Healthcare Products Regulatory Agency - Jobs.ac.uk (Jobs.ac.uk)](https://news.google.com/rss/articles/CBMib0FVX3lxTE1ma0ltbzY0eVE3RXBpaEs0eThnNmwzaGlSQUFobFQ4bFF3WXNMWHVQOVpYbEdiNGIxZWtobHNUT1RiM1FkTU9teHJoRUstb1Y5OFZidnF2al9vbTFyNVFjdU5CcTJsN1F3WWl3NXgxUQ?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Faculty of Health Sciences - Precision Medicine and Health Tech at VinUniversity - Jobs.ac.uk (Jobs.ac.uk)](https://news.google.com/rss/articles/CBMimwFBVV95cUxPMndJcjJaNVBtd09BYkdDZGxXTmlBcUM0bFhIODVZRVpsY1V6RHpHV3RNUGNTWnp6NFB2U252RGNjQXBmaC1YakR6MVFxLWdFNHdCNHh3cmZlRHI5bThkWEQzQWhwdjQtMmY0VjQ3TG5PM1BRTXRTNi1ydzBuVzZtM01fWFNWZmhQcHhBSll1WlROQ2VWWE00VWVWQQ?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**
- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
