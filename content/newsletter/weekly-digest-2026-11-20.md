---
title: "Weekly Digest: Nov 16 - Nov 20, 2026"
date: 2026-11-20
description: "A curated summary of the top protein engineering and structure prediction signals from Nov 16 - Nov 20, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Nov 16 - Nov 20, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Nov 20

### [Multiparadigm Benchmark of Molecular Docking: From Physics to Co-Folding and Hybrid Models.](https://doi.org/10.1021/acs.jcim.6c01293)
#### 🧬 Abstract
Generalizability of molecular docking predictions across novel protein targets and distinct small-molecule chemotypes is key to the successful application of deep learning co-folding approaches in drug discovery, as highlighted by recent benchmarks, including Runs-n-Poses [Škrinjar, P.; et al.Nat. Struct. Mol. Biol.2026, 33, 782-794.]. To compare generalizability across physics-based, hybrid rescoring models, and co-folding approaches, we systematically benchmarked several molecular docking tools representing these paradigms. Our results support previous observations that co-folding approaches show superior performance on targets resembling their training datasets. However, they deteriorate sharply to unacceptably low 20-40% success rates on novel dissimilar systems, consistent with memorization. In contrast, physics-based and hybrid methods exhibit greater out-of-distribution robustness, maintaining more than 60% success rates for docking protein-ligand complexes with minimal similarity to previously known complexes. Our results highlight the complementarity of AI-based approaches and methods based on physical sampling in all-atom models, in terms of their applicability range, and argue for the benefits of tighter integration.

> **Why it matters:** Essential ground-truth data for validating next-gen foundation models like Boltz or Chai.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Nov 20

- **[Beyond AlphaFold 3: a standardised benchmark of open-source co-folding models for antibody-antigen complexes, from docking accuracy to interaction specificity.](https://doi.org/10.1080/19420862.2026.2760737)**: Co-folding models are increasingly used to predict antibody-antigen complexes for epitope mapping, candidate triage and structure-guided de novo design or engineering, yet the latest generation of these models has not been compared under standardized...
- **[Virology-aware artificial intelligence for respiratory antiviral discovery: from molecular docking biases to RdRp-centered benchmarking.](https://doi.org/10.3389/fphar.2026.1940098)**: Respiratory RNA viruses remain a persistent threat because they combine high transmissibility, rapid evolution, immune escape, zoonotic spillover, and incomplete therapeutic coverage. RNA-dependent RNA polymerases (RdRps) and polymerase complexes are among...
- **[Beyond the flat screen: evaluating virtual reality as a complementary tool for molecular docking in drug discovery.](https://doi.org/10.1007/s10822-026-00915-1)**: Molecular docking is a key computational approach in drug discovery and structural biology. Traditional docking tools, while effective for high-throughput screening, often rely on rigid or semiflexible receptor models and purely algorithmic sampling,...
- **[PreFold-dG: estimating binding affinity of protein-protein interaction from intermediate representations of protein folding model.](https://doi.org/10.1093/bioinformatics/btag489)**: Motivation Binding affinity governs how proteins interact and underlies essential biological processes. Computational approaches have been developed to simulate and predict protein binding, but the scarcity of high-quality data has imposed significant...
- **[Molecular Docking of Natural Products: Critical Appraisal of Current Methodology and Practical Guidelines.](https://doi.org/10.3390/molecules31183228)**: Molecular docking is among the most widely used techniques in structure-based drug discovery and has become integral to natural-product research. Despite substantial advances in computational algorithms and artificial intelligence, the methodological...
- **[Structure-based virtual screening with AlphaFold identifies CLIP1-LTK inhibitors.](https://doi.org/10.1038/s41401-026-01957-9)**: Artificial intelligence-based protein structure prediction provides new opportunities for structure-based drug discovery, especially for targets lacking experimental structures. Determining whether AlphaFold2- and AlphaFold3-derived models can reliably...
- **[Identification of Potential SARS-CoV-2 Main Protease (MPro) Inhibitors Through Pharmacophore Modeling, Molecular Docking, and Molecular Dynamics Simulation Approaches.](https://doi.org/10.3390/ijms27177684)**: The main protease (MPro) of coronaviruses (CoVs) is an essential enzyme involved in viral replication and represents an attractive target for antiviral drug discovery. Based on the similar binding pocket residues within the MPro of different CoVs, this...
- **[An inverse-protein-folding pre-trained model for predicting the mutational effects in protein-protein interactions.](https://doi.org/10.1016/j.isci.2026.117693)**: Protein-protein interactions (PPIs) are fundamental to vast biological processes. Accurate prediction of mutation-induced changes in PPIs is crucial for protein engineering and drug discovery. Most existing PPI prediction approaches rely on refined...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) - State-of-the-art generative model for de novo protein design.
- 🛠 **Tool**: [ProteinMPNN](https://github.com/dauparas/ProteinMPNN) - High-speed sequence design optimized for fixed-backbone folding.
- 💾 **Dataset**: [BioLiP](https://zhanggroup.org/BioLiP/) - Verified biologically relevant ligand-protein interactions.
- 💾 **Dataset**: [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/) - Residue-level mapping between PDB, UniProt, and other resources.

---

## 🤖 AI in Research Recap

- **[AlphaFold 3 Models Reveal How Chemical Enhancers Alter Cas12a Biosensor Structures - Bioengineer.org](https://news.google.com/rss/articles/CBMiqwFBVV95cUxNMUJmaFNTNjdsbmlpX0dOWGR0Rk5va3I1Sm55dVlqNGxMemhCWFJfYkQ4ZXVxNkZwX2NZSHlsTUVzSWFNNkpVa1F0QlNCLVNLWEpIbDdjbHBLY2NBcjNtOXZRVm45X2J1REJKWGllNG5jUVptcmtaeVJkREVTUWlLQ1BHQnlmNWRfclZ5RjJzZ3BTX1BxRHp6bmx4MVZQOW5QZ3lzNzZHNEVKTW8?oc=5&hl=en-US&gl=US&ceid=US:en)**: AlphaFold 3 Models Reveal How Chemical Enhancers Alter Cas12a Biosensor Structures &nbsp;&nbsp; Bioengineer.org
- **[Mechanistic Interpretability Shows How AlphaFold 3 Extracts Protein Structural Hypotheses - Bioengineer.org](https://news.google.com/rss/articles/CBMitAFBVV95cUxOUjlDSlBsemdzMjJnSEpCSF9ITTZxUklfMGFiSFhZX3JtVU4yWHozZ0picHhpdVNjRWZ4UkFxU1IwcE8wYV9VanpPRHQ0SXZnVWVPeWtBZm9RdmZKbU1jbmhzek9OSzVFY0pNRnNTc3ZoNXI1c2VNUjlIVllNVkhpbzV6anlvbzhzN1hVcEVyT1hrWm5ldFNQZVpmRUFGSl9uVTNCczlRakp5MGdiSUNZMTJMTFk?oc=5&hl=en-US&gl=US&ceid=US:en)**: Mechanistic Interpretability Shows How AlphaFold 3 Extracts Protein Structural Hypotheses &nbsp;&nbsp; Bioengineer.org
- **[Isomorphic Labs adds Merck as an oncology partner after $5 billion raise - Drug Discovery & Development](https://news.google.com/rss/articles/CBMirAFBVV95cUxPVWhSNDVVekNfcTNCQ09rY1JiYUdIRHNGdTlpWHRkTUI1ejBjWUFIQVJJeDJOZ251UlREYmJ6bmhYYVNDS3FDdmhIRG1JMjJqRkt2QmNkaDhfTEpSWnpvcFFfa0dHZ1A1eHdva2dOOUtNRlFTUU1XX1BJbV9LN19vZkc3NU9qbFNJUkFGZWRIZThxY2dDcWlqYzNmeUZpNWwzNTBsaUlUajk5QlJi?oc=5&hl=en-US&gl=US&ceid=US:en)**: Isomorphic Labs adds Merck as an oncology partner after $5 billion raise &nbsp;&nbsp; Drug Discovery & Development

---

## 🏢 Industry & Real-World Applications

- **[PFE Inks $2.6B Licensing Deal With Chinese Biotech for CAR-T Therapies - Yahoo Finance](https://news.google.com/rss/articles/CBMijAFBVV95cUxOaEd4TjdNeTgtaXB3RmlTdHNXTktjcWJlYjRHdzR3QTE4RV9VMDRLZ1FhV3RPSThsajdGcGhoY0twbi1wLW5VZFNvZ0o0MmhyTkIxNUQ4cnFxVE1CUHoxQ0tDa3d2SG9wZldlbnc3R2NUOGlvZzlVWlpzQ1FmVTlWdTlNbU5YVU1vM1dFdA?oc=5&hl=en-US&gl=US&ceid=US:en)**: PFE Inks $2.6B Licensing Deal With Chinese Biotech for CAR-T Therapies &nbsp;&nbsp; Yahoo Finance
- **[The role of biologics in the management of hidradenitis suppurativa - Managed Healthcare Executive](https://news.google.com/rss/articles/CBMitgFBVV95cUxOSkRQbkJzS0IySGEzb19pWkRXdXF4SzJkODZ2VVRKTE13Z2dBMFItaEh3dUlicmsyVG9OU2Y2ZlN1aTB4NXdqbHRsTmdXcmQ3NjM1ZGl4ckJ2dnFKWjBWWXJpTjRKT0hPWFhDcHRsYWhBTTRyR3U1UThiWjFaVHMwSGZwZXRDazl4dEcwLTR2ZExNckotRmZoU3E4bXI0dnRDTE03YmNLbkFXMkhJaFExNGd3ZFR2QQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: The role of biologics in the management of hidradenitis suppurativa &nbsp;&nbsp; Managed Healthcare Executive
- **[From decoding DNA to designing drugs: How AI is rewriting life sciences careers - The Times of India - Education Times](https://news.google.com/rss/articles/CBMi1wFBVV95cUxNd2NmUFZOa0g5VHI3Q041anl3Rl81N0VKUElRYTU3S1FLNjQtN213UFN5bmI2Y0drTEMzWVZiOTJ2OXlXZmpyU1lvSWVvX0VWa2hLWmJ4Umg1bVZfQS1JdVRZMC1YWF9xVHNmalY2OG5UZnk0cmNpbDYzZGlfSGlvekM0WW9SWGM1NzQtaE9jYlRZTHB4R1ZyRWxVc1FmbTh1Z0xkczVvUEdPblBqWnNKSkUwSzY2UG5pRlpfQ19ucXVrRzJWaEo5Vl80VHJDbUhhWk55ZW1Faw?oc=5&hl=en-US&gl=US&ceid=US:en)**: From decoding DNA to designing drugs: How AI is rewriting life sciences careers - The Times of India &nbsp;&nbsp; Education Times
- **[Evotec secures second FDA clearance under BMS partnership - grafa.com](https://news.google.com/rss/articles/CBMitwFBVV95cUxNdnZ6a3RFZWpXTXY5Mnh5NXl6eDZWU2NJaEhQVjlvWG1qN3hNUUhyUWxJRHp5aUpGNllWNVpqWjRib0t6ZnNWNXJpX2puNXg0cUxrYmcwWGRrelNnN1RsYTM4TnpLYmxxaXRuY3dUaE5CcWZLSzN4bXdkOTZxdG1TcW03YWlyMi04RXZpZnB3UXFuLWs4RWVVS09fb0lkc1BVdXVNSDN6YUpKTGZhWXFMUVpIUHRtbEE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Evotec secures second FDA clearance under BMS partnership &nbsp;&nbsp; grafa.com
- **[Boltz: building towards programmable molecular design - Bessemer Venture Partners](https://news.google.com/rss/articles/CBMigwFBVV95cUxOSU9Bd1RwTVhldm1vSE8wQ0J4OXVxUURDX1FqNUZOSmxkVUJSVlJydDdhMU5FU0lLLUpuREFKS1I2bGQ1TFdCOFM5OTJmbjkydFBKSVJhSXdKY05ib05JNWFyUzRPVmpWSGhWTG9kSmRHa204cHFsTTl4RE5RVWpNVzlvOA?oc=5&hl=en-US&gl=US&ceid=US:en)**: Boltz: building towards programmable molecular design &nbsp;&nbsp; Bessemer Venture Partners
- **[Pfizer enters in vivo CAR-T space via 3-program, $2.6B deal with China’s Starna - Fierce Biotech](https://news.google.com/rss/articles/CBMiowFBVV95cUxPdXVaZzZFMUZyVFdmY0JzM3FrZXNuZndFV0FGZW1zcGxOdFhYTlVmOTNhelZ4UjZ2SGVmcVNQaWFuYWVkQUxfNzhXRjRiQ3NHSi1wTWtMaFhrUWNmdmIxZno1S1ZiNTdiYjJEcjNXU1BZMU1RWFlVNHE2QlpMZFBlY1AyeGZ0TTVsMVFfSFpSd1Z3NkhubEtHY2Rzc0NqQ3RSVWRz?oc=5&hl=en-US&gl=US&ceid=US:en)**: Pfizer enters in vivo CAR-T space via 3-program, $2.6B deal with China’s Starna &nbsp;&nbsp; Fierce Biotech
- **[Updated: Pfizer gets into in vivo CAR-T with up to $2.6B Chinese biotech licensing deal - Endpoints News](https://news.google.com/rss/articles/CBMipAFBVV95cUxPVDVnR0dUcE10RzBBd2hkcUZSdk5DQ0tEdko2WUlnb2Y5X2FCVEpCeEJ6c0hQMWdzZjFlcmtDZFZoWk1CYzRySlFYT2pFVFpOWWs2cGFRdEh1ZUgzdHhtWmVIOEE2UmVkUzNob3h0MFZwbjdVNlBhU0wwVEY5ZGZuVldJdjlZUVV4cEtsdzVSOUtxNThHWUdEbGl0bTdSUzNCc1VDZQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Updated: Pfizer gets into in vivo CAR-T with up to $2.6B Chinese biotech licensing deal &nbsp;&nbsp; Endpoints News

---

## 💼 Jobs & Opportunities

- **[Job Application for Clinical Trial Manager, Oncology, Asia at Eikon Therapeutics - Greenhouse (Greenhouse Boards)](https://news.google.com/rss/articles/CBMib0FVX3lxTE8wVkJMVU1mUXdNa1V6TGZsYVg1WGZqQVptcEx1dTBNNEYyNi00NzdQbEhtS3RKVGdTSjZhelFUc3NYUjhIbk9PRnd6dEFVT0p3ZlVtUlYwdFk5WGpFVk5OY3lyaU1FRGxEeDNibFR2NA?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Job Application for Senior Scientist, Product Development at Natera - Greenhouse (Greenhouse Boards)](https://news.google.com/rss/articles/CBMiYEFVX3lxTE1KbklDQ1BuV3RzUFlvR0VQX2pHdER6T0VtclBHT0lLR1FJbVpvb2NQNWZTdkd6Q19lUUVHaEFrMXVrd01CZkc3Yms5cnlLQm5MLTRGUXJFaG5nTGpOclBGaA?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**
- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
