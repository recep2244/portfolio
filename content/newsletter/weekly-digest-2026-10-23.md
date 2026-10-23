---
title: "Weekly Digest: Oct 19 - Oct 23, 2026"
date: 2026-10-23
description: "A curated summary of the top protein engineering and structure prediction signals from Oct 19 - Oct 23, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Oct 19 - Oct 23, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Oct 23

### [Systematic benchmarking of AlphaFold and SWISS-MODEL kinase structures for structure-based drug discovery.](https://doi.org/10.1016/j.jmgm.2026.109571)
#### 🧬 Abstract
Accurate protein structure prediction is fundamental to structure-based drug discovery. However, the practical performance of deep learning-based models such as AlphaFold compared with traditional homology modeling approaches like SWISS-MODEL remains incompletely evaluated in realistic drug-design workflows. Here, we systematically benchmark AlphaFold2 and SWISS-MODEL using a curated dataset of 20 kinase structures with co-crystallized ligands. Predicted models were evaluated under three conditions: the raw predicted structures, structures subjected to energy minimization, and structures subjected to triplicate 100-ns unbiased molecular dynamics (MD) simulations for structural refinement. Model performance was assessed using structural accuracy metrics, multi-software docking (AutoDock Vina, AutoDock, and MOE), and post-docking MD trajectory stability analysis, together with MM/GBSA binding energy estimation. As expected, experimental structures consistently showed the best docking performance. Among predicted models, SWISS-MODEL produced slightly lower RMSD values and better interaction similarity than AlphaFold, although overall docking scores were statistically comparable. MD refinement prior to docking reduced structural suitability by increasing binding-pocket deviations and was associated with misoriented ligand poses in subsequent docking calculations, while energy minimization provided little to no improvement. Notably, the reduction in docking performance was not limited to computationally predicted structures but was also observed for experimental structures solved in complex with different ligands. Thus, rigid docking alone tended to generate a substantial number of false-positive poses. However, MD simulations applied after docking effectively identified unstable ligand poses and reduced false-positive predictions by detecting ligand dissociation. Overall true-positive rates were 30% for SWISS-MODEL and 35% for AlphaFold2. These findings highlight the importance of dynamic validation in structure-based drug discovery workflows.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Oct 23

- **[Benchmarking and behavioral characterization of LLM agents for protein design](https://doi.org/10.64898/2026.05.06.723381)**: Large language models (LLMs) are increasingly deployed as agents for scientific discovery, but standardized frameworks for evaluating their performance and behavior in scientific workflows are lacking. Protein design provides a demanding test case because...
- **[Human and zebrafish cross-species comparison on ligand affinity towards the aryl hydrocarbon receptor and Keap1 oxidative stress sensor: a molecular docking dataset.](https://doi.org/10.1016/j.dib.2026.113037)**: Bioanalytical methods targeting adverse cellular outcomes are increasingly used in environmental toxicology, including receptor-mediated toxicity pathways relevant to high-throughput monitoring of drinking water, wastewater, and other environmental...
- **[PreFold-dG: estimating binding affinity of protein-protein interaction from intermediate representations of protein folding model.](https://doi.org/10.1093/bioinformatics/btag489)**: Motivation Binding affinity governs how proteins interact and underlies essential biological processes. Computational approaches have been developed to simulate and predict protein binding, but the scarcity of high-quality data has imposed significant...
- **[Molecular Docking of Natural Products: Critical Appraisal of Current Methodology and Practical Guidelines.](https://doi.org/10.3390/molecules31183228)**: Molecular docking is among the most widely used techniques in structure-based drug discovery and has become integral to natural-product research. Despite substantial advances in computational algorithms and artificial intelligence, the methodological...
- **[Adversarial Sequence Mutations in AlphaFold and ESMFold Reveal Nonphysical Structural Invariance, Confidence Failures, and Concerns for Protein Design.](https://doi.org/10.34133/csbj.0142)**: AlphaFold has transformed structural biology and spawned an ecosystem of derivative tools for protein design, binding prediction, and drug discovery. However, whether AlphaFold has learned generalizable biophysical principles as opposed to template-based...
- **[Identification of Potential SARS-CoV-2 Main Protease (MPro) Inhibitors Through Pharmacophore Modeling, Molecular Docking, and Molecular Dynamics Simulation Approaches.](https://doi.org/10.3390/ijms27177684)**: The main protease (MPro) of coronaviruses (CoVs) is an essential enzyme involved in viral replication and represents an attractive target for antiviral drug discovery. Based on the similar binding pocket residues within the MPro of different CoVs, this...
- **[Advancing In Silico Drug Design with Bayesian Refinement of AlphaFold Models.](https://doi.org/10.1021/acs.jctc.6c00868)**: Virtual screening has become an indispensable tool in modern structure-based drug discovery, enabling the identification of candidate molecules by computationally evaluating their potential to bind target proteins. The accuracy of such screenings...
- **[An inverse-protein-folding pre-trained model for predicting the mutational effects in protein-protein interactions.](https://doi.org/10.1016/j.isci.2026.117693)**: Protein-protein interactions (PPIs) are fundamental to vast biological processes. Accurate prediction of mutation-induced changes in PPIs is crucial for protein engineering and drug discovery. Most existing PPI prediction approaches rely on refined...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [Boltz-1](https://github.com/jwohlwend/boltz) - Open-source biomolecular structure prediction model.
- 🛠 **Tool**: [ProteinSolver](https://github.com/manulera/ProteinSolver) - Graph-based neural network for protein sequence design.
- 💾 **Dataset**: [BioLiP](https://zhanggroup.org/BioLiP/) - Verified biologically relevant ligand-protein interactions.
- 💾 **Dataset**: [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/) - Residue-level mapping between PDB, UniProt, and other resources.

---

## 🤖 AI in Research Recap

- **[Google DeepMind uses Antigravity AI to identify potential new antimicrobial peptide - EdTech Innovation Hub](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNdXdiM1NEa21hWnFCZ0ZrNDRFU0Y2MDBoS0xKX0FiMzFsZUVQUjdWZC1JVWtESHdnT1BDZG5MSUpkemllMjNiZUpiWF9MMWQtX21jeW8wSEs0R1NGaEE4TnM5ZXJ4alBkS0QySFZ1c2xxci1KZ0g1ZktNNHRTc2FlcXM3Q2hGOTM0NXVlRW9YalRocWRGYWFjSUFUbVN4QnJSTUFJek1vdUtSQ3BKb0VEeVdfYjFHUENaWFZSSjhfZnY4dw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Google DeepMind uses Antigravity AI to identify potential new antimicrobial peptide &nbsp;&nbsp; EdTech Innovation Hub
- **[Nobel laureate expects human-level artificial intelligence to emerge in two to three years. What will smart t - Наша Ніва](https://news.google.com/rss/articles/CBMiS0FVX3lxTFBabWRXUFlUN2xWSlVPbWFNN1pXeGRvLVllWHhWclJhdUNfcHdwVUVfQ0t3aTdhNl91ZHlQXzJ3OVQxRENEaUo3bktNTdIBS0FVX3lxTFBabWRXUFlUN2xWSlVPbWFNN1pXeGRvLVllWHhWclJhdUNfcHdwVUVfQ0t3aTdhNl91ZHlQXzJ3OVQxRENEaUo3bktNTQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Nobel laureate expects human-level artificial intelligence to emerge in two to three years. What will smart t &nbsp;&nbsp; Наша Ніва
- **[CAR-T’s $12bn Future Hinges On More Than New Approvals - In Vivo](https://news.google.com/rss/articles/CBMi4gFBVV95cUxNa0NmZmNWMzhyVU5ocEZCQ3plcnY0V3lvVlZTOENZdkp4VkhvSG9oY2FYUi1Ya1Z3LXMtRW1TMWZZRWt1YnZVemhEU3NMa1g0OXNCcGhtTGJaTDhzVUFhOVlxb3NUX0FxZmxwU2FLbVRVQTFtczMwRS05dEl6VVh3MkZkYTRyOXl4czRudXNKOUhHZDZQZWNXN0JDcUZ2NGZ2V0ZpbXM2cHJVYTlOeWQyTkMxU2x2akE5UFJ4eXgzU0xobmdKZlFiWEdoMnNtMFdBbEhjNHB6a0c1anhvUGs5LXZB?oc=5&hl=en-US&gl=US&ceid=US:en)**: CAR-T’s $12bn Future Hinges On More Than New Approvals &nbsp;&nbsp; In Vivo
- **[Apheris, T-Systems Enable Secure Clinical Data Research on Sovereign Infrastructure - The Fast Mode](https://news.google.com/rss/articles/CBMi0wFBVV95cUxQU0dpWm5fQ3VxMlYtRUM3UlV1UHRHbmkyRm9zcE0zT2NTbjhXWF9NTm8xWk1DOWY0X1FlRHBEX1dBTXNmQXc2cjFWOExtcmZMb0hkT1EzdVZFN3ZRZnp1Rl82YTU4bC1nbG5OX0RFVlIyRHRQZEI5TFFHRHJyb3FiOVlDSHhaUjl1NWJfb3JtQ2hHYkdKM1kwLW1YSEVOYkZlaXZ5emxicEVWOUk5SjhqRnppTmE1OWcxczBReTZmYV9maHAtMkYxRGNIVUN6bFNWVjZN?oc=5&hl=en-US&gl=US&ceid=US:en)**: Apheris, T-Systems Enable Secure Clinical Data Research on Sovereign Infrastructure &nbsp;&nbsp; The Fast Mode

---

## 🏢 Industry & Real-World Applications

- **[Treasury sweeps biotech into proposed COINS Act restrictions, but spares Big Pharma’s China licensing deals - Fierce Biotech](https://news.google.com/rss/articles/CBMixgFBVV95cUxOZk9hMXREUkpYNkViVWs5R2JKZEQ0Q1hucE1HdHBiUDlqUTFPd01nQy1JUl8yaXRoOUVON3Q5QVlhNHpYZWZRbVNUMUQ1OURCQUZqWGRmVloyS09kSDJPd2IwX0hneUxPaFhNWUk1Q3cwY1NfcWdmbFBwUEhnZDlTbm92MmkzanlHQVJuNXdBYUVEa2hWdzFHNFZPTG5kNUJrZGphaUxhNlV4TWF5YUpnYy1OVnZhSkx4LVdxd0RtejNnaWZxMXc?oc=5&hl=en-US&gl=US&ceid=US:en)**: Treasury sweeps biotech into proposed COINS Act restrictions, but spares Big Pharma’s China licensing deals &nbsp;&nbsp; Fierce Biotech
- **[Biotech investment is the new front in the U.S.-China trade fight - Politico](https://news.google.com/rss/articles/CBMitAFBVV95cUxNeGctSS03QXZwRTdFZEpoZUNGczljZ1pwUnZTMjg5MGlILURUWmZqcHJPUWZuaHJVTkRaYWxxV29VRVl3clV5NTItV1dJWXFPeUlmQkJRTjE5VUVyQ1lpZmpOWm1WdWM3N01MdEpUSnNrcTZUd3dOV2tzUEdhQjNWelJ6elp1Vk5WZjZoMjd4YUFNc2tEWnI0S3ZjUkJpckpsZ3E3VGxPVi1ycmpUMVcxSEtQeEk?oc=5&hl=en-US&gl=US&ceid=US:en)**: Biotech investment is the new front in the U.S.-China trade fight &nbsp;&nbsp; Politico
- **[Nvidia, UW Institute for Protein Design Unveil Open-Source Protein Design AI Model - Genetic Engineering and Biotechnology News](https://news.google.com/rss/articles/CBMi1wFBVV95cUxPcXJuT25OLTFUZmxiZ0VYZlBRZjVVekpVNWltWFpYV2FDRlkzSk5ud3JxVWRuVFRfMlpDMHlzQ0tUWWdoemszczBwYW1LQkRJYm1ZVmJUZktWWmNWSU1zeXZyblhvb3dkcm55V2NmTUdKYkJTamdVZFRmMWV6NHVkb0p3bjRhSHFQdlcxc0hRUnBpeXFFcHJJdjFQUGk3NkVkY3h2eFJuaVR3UjdQTVh3RThLMHFGZTN0aTNpWUtUbmc3M2g4VkpDTHhlZ3pqbTZZZGZfbjJFZw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Nvidia, UW Institute for Protein Design Unveil Open-Source Protein Design AI Model &nbsp;&nbsp; Genetic Engineering and Biotechnology News
- **[Translation of in vivo CAR-T in China - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTE1vYkQweWRoeVR6U1VoeW9NdlBkYWZFSlpsa0pYY3l1bmt6cE1mS001cC1lOTBGdnRHM3UwdUdSTk1qUzlTNm42MXNNVmVzWFZJT1Y4Y1NwTC1uN3J5WlNB?oc=5&hl=en-US&gl=US&ceid=US:en)**: Translation of in vivo CAR-T in China &nbsp;&nbsp; Nature
- **[Astellas signs potential USD 400m-plus deal with AI Proteins for de novo miniprotein discovery - AllSci](https://news.google.com/rss/articles/CBMiowFBVV95cUxPMmx3Z1NZSjBhX0VUc292aE1Vd2NPejZaeHI1bzBfc1E1a2QwS0RkamxXT3J5N1ZMVVVFWUdCTXJSNWJ2b1N2RWIzR3lpSTRtMU9xeGxNYkFmbUh4SkJsOTZqN0UyQ2ZianN5VXlQcHNrVmJDcllpaXFueEl4S2ZDeXFZMmVEMUVjRXpQYzNFbE8zWVBfMEpzS2R2bkd0WmlxOWU0?oc=5&hl=en-US&gl=US&ceid=US:en)**: Astellas signs potential USD 400m-plus deal with AI Proteins for de novo miniprotein discovery &nbsp;&nbsp; AllSci
- **[EMA - Biologics Working Party training on biological investigational medicinal products - European Commission](https://news.google.com/rss/articles/CBMic0FVX3lxTFBFRHN0cDkzTENSalFJeWxqRGE2VnN3eG8yQi1NTHh5a3RFM1RTczNINVJnZHZsdlJEeXRCbk0wOFhTRXFueVhxMVBuN2ZyTTZDR3cyOUZQNmhHS3d6WEVJLWNlcXgzLWZQY1lIa1p5OUlpbGs?oc=5&hl=en-US&gl=US&ceid=US:en)**: EMA - Biologics Working Party training on biological investigational medicinal products &nbsp;&nbsp; European Commission
- **[Astellas links up with AI Proteins in $400M computational drug discovery deal - Fierce Biotech](https://news.google.com/rss/articles/CBMinwFBVV95cUxPRjVna3BYMnAwUHR1Y1luZW1jWFJ6RDhCV2NsUVBXREIzNk9CMlMyNjJhZ2xMemQxZ2syY18wem4wYmNXbXM5MHByVDR4ZW1WLTZ5OGE5djE3RW1rZG80RmFrZ2M0QU9HNDg0b3Z3emxMUktJSHRmQnhpVzNDYWd0Z0NlcDdieXpmaGpHalVvTXpPZDZhT09NbV9aWi01T0k?oc=5&hl=en-US&gl=US&ceid=US:en)**: Astellas links up with AI Proteins in $400M computational drug discovery deal &nbsp;&nbsp; Fierce Biotech

---

## 💼 Jobs & Opportunities

- **[4 Molecular Biology jobs in The Netherlands - Academic Positions (Academic Positions)](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQZ2dZWHdtdmVPa0N4M04wTlNaWWctbXp6MndGRS1iWkhURGVSRWgzMVJVNlBUTzRfS29yc0VNV0dhSHVlTHB3RExUQWlpVWEyakxtZWx5VEtnenpoeXpQRTFxcTV4eHZMRUlLekdsRDNTNHFpOU4xU3UtQnV6ZHpxdlh1djVHM1RI?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[19 Bioinformatik Jobs in Deutschland - Academic Positions (Academic Positions)](https://news.google.com/rss/articles/CBMif0FVX3lxTE53ZDVkbUNTZE5uSGEyWEJxQVFYemg0RUJEbjBxOXhnMHZldU1ZcHpXMVpYdHpFLXFHczVHOExFMlk4UjVDaVI5U0draV96T3VYRzBpVWh5dWlIVUxuekhMdzkxUTcwZzlyY0lYRW9sR0pWNThyWTRuXzdwSU9lUHM?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**
- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
