---
title: "Weekly Digest: Jun 01 - Jun 05, 2026"
date: 2026-06-05
description: "A curated summary of the top protein engineering and structure prediction signals from Jun 01 - Jun 05, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Jun 01 - Jun 05, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Jun 05

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Jun 05

- **[Classical Docking to Machine Learning Based Docking: Molecular Docking in Drug Discovery.](https://doi.org/10.2174/0115680266424314251204071847)**: Molecular docking has emerged as a cornerstone methodology in computational drug discovery, enabling the prediction of ligand-receptor interactions with considerable accuracy and efficiency. This article provides a comprehensive overview of docking...
- **[BA-Pred and RMSD-Pred: Integrated Graph Neural Network Models for Accurate Protein-Ligand Binding Affinity and Binding Pose Prediction.](https://doi.org/10.1021/acs.jcim.5c02591)**: Accurate prediction of protein-ligand bound poses and their affinities is essential in structure-based drug discovery. Here, we present an integrated deep-learning framework that disentangles the two core tasks─affinity estimation and pose...
- **[PlantP450Dock: an Automated Molecular Docking Pipeline of Plant Cytochrome P450s](https://doi.org/10.64898/2026.05.12.724510)**: Cytochrome P450 enzymes (CYPs) are the primary drivers of chemical diversification in plant secondary metabolism; however, fewer than 10% of the superfamily members have been functionally characterized. Computational docking provides a scalable strategy to...
- **[AlphaFold and the Transformation of Structural Biology: Evolution, Applications, Limitations, and Future Directions](https://doi.org/10.22541/au.177282022.20654724/v1)**: The protein folding problem is the challenge of predicting a protein's three-dimensional structure from its amino acid sequence. This problem has been a central challenge in molecular biology for over fifty years. The advent of AlphaFold, a deep learning...
- **[Integrating glycosylation in  <i>de novo</i>  protein design with ReGlyco Binder Design Filter](https://doi.org/10.64898/2026.04.16.718906)**: Artificial Intelligence (AI)-based methods for 3D protein structure prediction are revolutionising structural biology 1–7 , providing novel templates for experimental data refinement and an on demand 3D perspective on any molecular architecture and...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[The past, present and future of de novo protein design.](https://doi.org/10.1038/s41586-026-10328-7)**: With deep-learning-powered advances in protein design methods, there is an ongoing paradigm shift in protein engineering from random selection to intentional computational design methods. Here we describe the current state of de novo protein design. While...
- **[Adversarial Sequence Mutations in AlphaFold and ESMFold Reveal Nonphysical Structural Invariance, Confidence Failures, and Concerns for Protein Design](https://doi.org/10.64898/2026.02.25.708002)**: AlphaFold has transformed structural biology and spawned an ecosystem of derivative tools for protein design, binding prediction, and drug discovery. However, whether AlphaFold has learned generalizable biophysical principles versus template-based pattern...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [Rosetta](https://www.rosettacommons.org/) - Protein modeling, docking, and design suite.
- 🛠 **Tool**: [AutoDock Vina](http://vina.scripps.edu/) - Molecular docking for ligand screening and scoring.
- 💾 **Dataset**: [BioLiP](https://zhanggroup.org/BioLiP/) - Verified biologically relevant ligand-protein interactions.
- 💾 **Dataset**: [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/) - Residue-level mapping between PDB, UniProt, and other resources.

---

## 🤖 AI in Research Recap

- **[Vertu’s Alphafold foldable phone has launched, and you’ve got to see its obnoxious price - MSN](https://news.google.com/rss/articles/CBMinwNBVV95cUxQR2padWNxUTQzMWZ2d0ZSdlRYQndZSGpnd0N3bndCdXRGOTIwckgyWTdOY1cwU2RtQkxHazdqdDdvWlFfS2l1MWc2NDY4Zmh4NDBzOHktZHhMWjlRRGdiMjY0bEFyVk1yLWU2anNzZzEza1V5bmxobkp3SURoSXZwMC1sNk1MZk9rUGNfRmMyaGRFRXd5ckRfMm91V2hJeFU0QnlBTlJOeUJWS1RwaC1rWkVTVld1cjdIQXFlaXZGSnoteTJleUdlUDBieFpQb0hoa3lYOVlnZEtIZFlrWTNQR2xOcXhKd0Z0NXhQSENQZXp3OVlyQmNDT3hmYlNlTG1GTWpjZjFkam5CTWRoZ3UtU05uWU9GR2NlZ3hOdFRObGhNYVQ5MGVZMVF0Y3Jqa0dQX2c4elgwZVdKV0VuV0I1bUZrTGhVMUx6TTdVbi1XTFZGNlNRQ1BTc3RQbDdUUFNnMTZfS0tzX0dVc0dEVm1WVklPTHdEZDFSdFRxYzBsdnloY0Y0ZGY3Q2h1Y05acHoyTTI3TlJFYUgydDhiTE9B?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu’s Alphafold foldable phone has launched, and you’ve got to see its obnoxious price &nbsp;&nbsp; MSN
- **[Can AI Cure Cancer? - Slow Boring](https://news.google.com/rss/articles/CBMiW0FVX3lxTE1RVGt1dVNqVEc2TVp1V3JQeTBhdEhIWWc4aU9wbGV6aV9fYUhNNDdkNERDNHdXVzBMb0ZVQnJienB5WmUxYkRqb0h1WjZiYTl6cmRHODBQTHBiRjg?oc=5&hl=en-US&gl=US&ceid=US:en)**: Can AI Cure Cancer? &nbsp;&nbsp; Slow Boring

---

## 🏢 Industry & Real-World Applications

- **[China: The Innovation Factor Coming Into Play - DCAT Value Chain Insights](https://news.google.com/rss/articles/CBMibkFVX3lxTE5fMVFRVndwNHU2Vy05Mk1QbGtXaVU0M254ZHJMVkVDMTJIcFNoQS1PUXFTVUktZGRNdV9XUGVIMXltOTh2akY0VkNGT053Q3pBYmxhV0JfUVRLYklyang5ZWJSS0x2dnhWMnA1bnVn?oc=5&hl=en-US&gl=US&ceid=US:en)**: China: The Innovation Factor Coming Into Play &nbsp;&nbsp; DCAT Value Chain Insights
- **[/C O R R E C T I O N -- Oberland Biotech GmbH/ - PR Newswire](https://news.google.com/rss/articles/CBMilwJBVV95cUxOWFlLVFFLQ3BCVlY5NzczdGR1MV9DTG9VeEUwS1JGVE9NeDB2bjhrVUcyeXdtV1JXWGgxemdvYk9KdW8yWkZpREl5bXRtcVRKZFpCR09SOUMtMnVpamZmb0VLcXBxdXBHWngxZTFDQzJCRHd4cTRuSER3WlRvbXpqbnh5NTFfMzhLOWRZMnlBN1RnYW1WQklpS1BweXZ3R2pXT2lSdmhxM196UG8zSHNFeFZOR0NhZEppajlNX1hjcDJIVFE3YnVfR3daY2NZbElqZU5Fd3JrUTBiWmstTlJWbzRQMi1maUdhZlh3SThnbmxkSzV3ZXhtMTE3MFM4WWFhUm1nX0RwekRlN0RzU2l2ZExvM3dpYlU?oc=5&hl=en-US&gl=US&ceid=US:en)**: /C O R R E C T I O N -- Oberland Biotech GmbH/ &nbsp;&nbsp; PR Newswire
- **[No VCs allowed: This biotech startup is funded solely by retail investors - Morning Brew](https://news.google.com/rss/articles/CBMihwFBVV95cUxNVTl1WEcxRW1UWDB4S0dkOS1nYWFFSUFPbFV1emJ1amFLUXBvQm4tY3ZCNnp0c1IzWE91akt3d1RNZnFNWEh0cEZLTGRNTGlUb0RyeVRMVXVOWTktc0x4YnF4NUp4bjZoeFBzVUxGN2pfWGhMdTJSMlY2eHVhWU1LcnYyRXE3QlE?oc=5&hl=en-US&gl=US&ceid=US:en)**: No VCs allowed: This biotech startup is funded solely by retail investors &nbsp;&nbsp; Morning Brew
- **[Towards mRNA therapeutics 2.0 - Nature](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBmMVVKQ3h6X3V2S3g2eWFYSmV0MmMzSGd6NTdYSjJXdlJ4NFJIUFc0Wjc4MW10VmlzdEpnQ2hzX0lOSlV2MlJoT0FTQlotRFRtNWx5S0Vpa3FOYmFCY0xv?oc=5&hl=en-US&gl=US&ceid=US:en)**: Towards mRNA therapeutics 2.0 &nbsp;&nbsp; Nature
- **[House bill aims to crack down on China biotech deals - BioPharma Dive](https://news.google.com/rss/articles/CBMilwFBVV95cUxNM0dvMHBFTGV1Q2wxTmtPdXBoaUF4a1JyRHk5V1RhdXo4STJiVmJ1UUYwOGZ1Nl96TUZKMnFWTUg1SGN5RS1yd1pPSTJVeE50VVpINDRGbklPbW9mREFMRHNQOVFKellVTE5VaUxXWGVLRS11WDBIWjR1SkZIbU1HaTI5S0syU09kd0VBRkZIaFV1OU5HQVJz?oc=5&hl=en-US&gl=US&ceid=US:en)**: House bill aims to crack down on China biotech deals &nbsp;&nbsp; BioPharma Dive
- **[US lawmakers reveal policy to curb collaboration with Chinese biotech - Yahoo Finance](https://news.google.com/rss/articles/CBMinAFBVV95cUxQZld2bTlNLTVWMGtvdXZvdVlfeDdBTmRQbXM4QTJQQ0FjQ29nSUc1U2oxUmc2dHhtdEJPd2tVcjBJcHRpSEY4bk9HWlZXX2xGVV9RZGJXUlplLW9YM3cxbnZ0YTVqTnViajJJVXlBd0tFQ2RVS1laVzMzNm8tOHBONXVONGNXdVR2QWZiamdiM2M0d2VlTTlCNGdPSzA?oc=5&hl=en-US&gl=US&ceid=US:en)**: US lawmakers reveal policy to curb collaboration with Chinese biotech &nbsp;&nbsp; Yahoo Finance
- **[Lundbeck partners with Cradle for AI-based protein design - medwatch.com](https://news.google.com/rss/articles/CBMib0FVX3lxTFBRSnV3WkRBZmxlYVJvdHFJUnJmOWh2LVNsaDdsaUgwazNlSUN6UmdDUzRiZnpOc0ZKTkhGU2kzZ2tQb3hJeEJMeGtxbnNfZmVLa21ySzFobVdQLWZmSU5KS0dpYlE1c2VzVk1XcUdNaw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Lundbeck partners with Cradle for AI-based protein design &nbsp;&nbsp; medwatch.com

---

## 💼 Jobs & Opportunities

- **[Job Application for Associate Director, Biomarker Development at Apogee Therapeutics - Greenhouse (Greenhouse Boards)](https://news.google.com/rss/articles/CBMicEFVX3lxTE9hc0xMT1VJQThRYWJlTVVicEVjeTNxUVV2MTBJV1JNYnc2aE1ORzdhZlRlZE1rdlkyT3VKOHBUSjJQOXVacjhBZjFremx1ek5VVm05MjByMVRoaDl6WHRWYU85NGplcS02VXQ5bVpzemI?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Job Application for Display Manager (gn) at The Quality Group - Greenhouse (Greenhouse Boards)](https://news.google.com/rss/articles/CBMic0FVX3lxTE00MWVHdUZkOTRXSy1UQmRMOG5yczhaVVNwM2xReFFubzNOeU9ZYmNCUWdyaFU2UEduRnhkOGFlYlFNSjlYM19sTWVwc2ltaDZ4NUp4akxMVnh3cXhiTGttWjlucXI2QmZ4NEU2OE01S1QzMzQ?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**
- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
