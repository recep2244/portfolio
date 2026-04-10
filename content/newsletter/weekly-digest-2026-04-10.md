---
title: "Weekly Digest: Apr 06 - Apr 10, 2026"
date: 2026-04-10
description: "A curated summary of the top protein engineering and structure prediction signals from Apr 06 - Apr 10, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Apr 06 - Apr 10, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Apr 10

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Apr 10

- **[Discovery of potent ALK tyrosine kinase inhibitors for thyroid cancer via machine learning modeling, molecular docking, MD simulations, and DFT study.](https://doi.org/10.1016/j.compbiolchem.2026.108960)**: The ever-increasing need for effective therapeutic management of thyroid cancer (TC) necessitates the exploration of novel approaches for advanced drug discovery. The current study employed a robust computational pipeline integrating Machine Learning (ML)...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[A New Insight into the Study of Neural Cell Adhesion Molecule (NCAM) Polysialylation Inhibition Incorporated the Molecular Docking Models into the NMR Spectroscopy of a Crucial Peptide-Ligand Interaction.](https://doi.org/10.3390/biom16010019)**: The expression of polysialic acid (polySia) on the neuronal cell adhesion molecule (NCAM) is called NCAM-polysialylation, which is strongly related to the migration and invasion of tumor cells and aggressive clinical status. During the NCAM polysialylation...
- **[Enhancing CYP450-Ligand Binding Predictions: A Comparative Analysis of Ligand-Based and Hybrid Machine Learning Models.](https://doi.org/10.1021/acs.jcim.5c01098)**: Predicting cytochrome P450 (CYP450) ligand binding is critical in early-stage drug discovery as CYP450-mediated metabolism profoundly influences drug efficacy, safety, and adverse reaction risks. However, experimental determination of CYP450-ligand...
- **[Investigation of the potential mechanism by which methylparaben induces psoriasis: an integrated study using network toxicology, molecular docking, molecular dynamics simulation, and eight machine learning algorithms.](https://doi.org/10.1093/toxres/tfag003)**: Psoriasis is a chronic inflammatory skin disease with limited safe and effective treatments. Methylparaben, a widely used preservative in cosmetics, pharmaceuticals, and food, is an emerging environmental pollutant linked to immune-related skin disorders,...
- **[Evaluating zero-shot prediction of monomeric protein design success by AlphaFold, ESMFold, and ProteinMPNN.](https://doi.org/10.1002/pro.70453)**: De novo protein design has enabled the creation of proteins with diverse functionalities that are not found in nature. Despite recent advances, experimental success rates remain inconsistent and context-dependent, posing a bottleneck for broader...
- **[Comprehensive Molecular Docking and Molecular Dynamics Reveal Inhibitors of HER2 L755S, T798I, and T798M based on a Large Database of Curcumin Derivatives.](https://doi.org/10.31557/apjcp.2026.27.1.265)**: Objective This study presents a methodology employing virtual screening to identify curcumin derivatives with selective affinity for the HER2 mutations L755S, T798I, and T798M. Methods Curcumin derivatives were retrieved from the ChEMBL database and...
- **[Identification of Bioactive Ingredients and Mechanistic Pathways of Xuefu Zhuyu Decoction in Ventricular Remodeling: A Network Pharmacology, Molecular Docking and Molecular Dynamics Simulations.](https://doi.org/10.2174/0113816128375610250608071339)**: Background Xuefu Zhuyu Decoction (XFZYD) is clinically used in China to promote blood circulation, resolve blood stasis, and alleviate ventricular remodeling (VR). However, its molecular mechanisms remain unclear. Objective This study investigates the...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [MMseqs2](https://github.com/soedinglab/MMseqs2) - Fast and sensitive sequence search and clustering suite.
- 🛠 **Tool**: [HHSuite](https://github.com/soedinglab/hh-suite) - Remote homology detection with HMM-HMM comparison.
- 💾 **Dataset**: [BioLiP](https://zhanggroup.org/BioLiP/) - Verified biologically relevant ligand-protein interactions.
- 💾 **Dataset**: [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/) - Residue-level mapping between PDB, UniProt, and other resources.

---

## 🤖 AI in Research Recap

- **[Yi Ren to present at Molecular Biophysics Training Program/Center for Structural Biology Seminar Series, April 14 - VUMC News](https://news.google.com/rss/articles/CBMi3AFBVV95cUxNOWs2TXlxVHlfeEl3X2hYdFctZHNnS044UkZTaU1DNmVra3ItSTJMVEU1RVJWNFFfSFMyMzVGM1VITzRoQVRxX1BFSEVXSHFELU8tU3JFN25JZUJMaHFMQzdyNllfSWhGZWJmTDdiYUwxOExUQXdXRlZfZ3BZSG5SMzRvdjZkUVpyRFl6dFo2dy1jOGpBVkppUFVVTy1RN3VDTFFSdi1hcnJiWkVWSDJOazkzR0NKWWxSTVpSUjgyODc5T0M0d3BaX1lwYmJXbmNrTTF4NXBCdG1aYU8x?oc=5&hl=en-US&gl=US&ceid=US:en)**: Yi Ren to present at Molecular Biophysics Training Program/Center for Structural Biology Seminar Series, April 14 &nbsp;&nbsp; VUMC News
- **[OpenFold3 Meets AMD Instinct™ GPUs: Unlocking Scalable, High-Throughput Structural Biology - AMD](https://news.google.com/rss/articles/CBMilgFBVV95cUxPQ0s5d3prLU9wMnd4MTltZ2R1QzM1NHo0V0RxajRiSDU1U0NuVm1SMS0zeXJTY3dmQWs3UjlWWHpIUDJqcWtxOVZJOHpaaVN6MWMtNUJFSDZsNWhwREhuV3VwdWxwMkp6bU1CUktqNGdTSDJYNVkzaDZfZzB0YkVTUEpMbmppYlpLX3NSVHNXMmt1OWRMdGc?oc=5&hl=en-US&gl=US&ceid=US:en)**: OpenFold3 Meets AMD Instinct™ GPUs: Unlocking Scalable, High-Throughput Structural Biology &nbsp;&nbsp; AMD
- **[NVIDIA Scales AlphaFold-Multimer for Proteome-Wide Protein Complex Prediction - MEXC](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9HcDNoVXFaekZDQng2eGlMb0RkNk5GSzhfcjZ5cU41b1h0c2RyNVlTb042X3dXSXlzZ2RFek9tUHByNjluYjhJMg?oc=5&hl=en-US&gl=US&ceid=US:en)**: NVIDIA Scales AlphaFold-Multimer for Proteome-Wide Protein Complex Prediction &nbsp;&nbsp; MEXC
- **[How to Accelerate Protein Structure Prediction at Proteome-Scale | NVIDIA Technical Blog - NVIDIA Developer](https://news.google.com/rss/articles/CBMioAFBVV95cUxQeXNFSk8zVzRoVUF6YzVZN01GNjZDci1WOTZzcXItTEJsOV9KNm9tNG1hTXJVOUFkcXhaSEQ0ZEdjMEwyM1lxaWhHS1pMUnBPenRZQlNhR3F2VmxWREVpbVVIOTlqdkNtaGlUenNST0JqWEhDYXh0azAxSG01ckY5bVRfWlFQNUJRUkdiVzRXX3MyV1lzbEdQVEZ3VXZZZVB5?oc=5&hl=en-US&gl=US&ceid=US:en)**: How to Accelerate Protein Structure Prediction at Proteome-Scale | NVIDIA Technical Blog &nbsp;&nbsp; NVIDIA Developer
- **[Demis Hassabis: AI Competition Gap to Widen - 36 Kr](https://news.google.com/rss/articles/CBMiU0FVX3lxTE9vVXV1bWFWYmlNN014dkdCbEd4R0VGOE4zN0pjVzZteGpqYVdGeDRsWmZIdXFpVXQxRjgtSzMyRTEwaE9hZmhtR3RJWWFYWldkNGE4?oc=5&hl=en-US&gl=US&ceid=US:en)**: Demis Hassabis: AI Competition Gap to Widen &nbsp;&nbsp; 36 Kr
- **[Congratulations Dr. Mariella Quispe-Carbajal and Dr. Lingshuang Wu on their Successful Thesis Defenses! - Stony Brook University](https://news.google.com/rss/articles/CBMikwFBVV95cUxQeG5aNzJkU3Q1WmNYblRCbVdheWRlWURGWDhSaV90Tl9MUWlhUHR1QzY1WVJHcEl3MnBXVXdlVWZReFZ2VURwdFhKYUR0SVpFbE9taGoxVTBpX2I5M1NMUXpjMy11aUxyQ2owdVdoaWdmbWg5cllHeU9JaTQwSm1mUnl0UFN1UkVTNzNMSzJLZU9OOUE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Congratulations Dr. Mariella Quispe-Carbajal and Dr. Lingshuang Wu on their Successful Thesis Defenses! &nbsp;&nbsp; Stony Brook University

---

## 🏢 Industry & Real-World Applications

- **[IPO Tracker 2026: Avalyn plots IPO to push inhaled pulmonary fibrosis pipeline through clinic - BioSpace](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBOZU9ySndUUGJrdkEyMDJubkhYMENBeUI3aUtiYVFCb1FEaU9vNXFsN18ydzBPOE5DcmdGQ1ZmaFhHbEpyV0R1TWF5OUZvUXBYZjJESkpfcDlmbWlPdWg4?oc=5&hl=en-US&gl=US&ceid=US:en)**: IPO Tracker 2026: Avalyn plots IPO to push inhaled pulmonary fibrosis pipeline through clinic &nbsp;&nbsp; BioSpace
- **[Record Biotech Deals: China Out-Licensing Hits $60B as Global Capital Flows In - News and Statistics - IndexBox](https://news.google.com/rss/articles/CBMikAFBVV95cUxPWW5uc3VCX2lWRG5Nd0tmbTF0MExxTDFmX2xDR2lYb0cwM0M5SVVRMExKalY4dG9tSEdXX0hqSkg4UTdOQ0xDcHlTRWc5MVVWM3ZZODdYRm8zeXIweWcwVEo1cFVoc19ieXJTcTkxOW5HWElaWk9jWURyT1JTRUpjZ1l6REJSTUVUTVozczd5UWo?oc=5&hl=en-US&gl=US&ceid=US:en)**: Record Biotech Deals: China Out-Licensing Hits $60B as Global Capital Flows In - News and Statistics &nbsp;&nbsp; IndexBox
- **[Biologics Across the Airway: Selection, Remission Goals, and Real-World Barriers - HCPLive](https://news.google.com/rss/articles/CBMipAFBVV95cUxOY1BHMXpzRzgtdEprbWlDMk9xb0JMZGFZMXJyLVRsQzJsX0RWUkhGaG0tMVhEc00xRlJDaDF4RW9Ndm5KVkxtWWpSeFZtSTBjaUVXT0FLMUFqRFdQajBTMlhacUhZQmNTaFh3TFFNdkRTRHVGTXB0WVJoMXotN1VxYUlhRlhLREQ1dTQyNm9ZR21nekphLXowUW9EQ3VCWFRZUHBsQw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Biologics Across the Airway: Selection, Remission Goals, and Real-World Barriers &nbsp;&nbsp; HCPLive
- **[NVIDIA Scales AlphaFold-Multimer for Proteome-Wide Protein Complex Prediction - MEXC](https://news.google.com/rss/articles/CBMiSEFVX3lxTE9HcDNoVXFaekZDQng2eGlMb0RkNk5GSzhfcjZ5cU41b1h0c2RyNVlTb042X3dXSXlzZ2RFek9tUHByNjluYjhJMg?oc=5&hl=en-US&gl=US&ceid=US:en)**: NVIDIA Scales AlphaFold-Multimer for Proteome-Wide Protein Complex Prediction &nbsp;&nbsp; MEXC
- **[LangChain Unveils Human-AI Feedback Loop Framework for Trading Copilots - blockchain.news](https://news.google.com/rss/articles/CBMihgFBVV95cUxPdmJvMzZKTTRYOWJsOFhIRzBwbGtORkdiRmVwRDFQbVlMM0d3NVNyYXN6c0ZUYzlrX3R0SW4xQi1QdTE5NmUtLUo1bkFyVkVrSDR3SzBMNm5UaFhCWFBzbUd0bTZjZnJyMmFfeFdfQ3Zvc1hUb0RsZEstWDFMLWtqMUxxUTV5UQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: LangChain Unveils Human-AI Feedback Loop Framework for Trading Copilots &nbsp;&nbsp; blockchain.news
- **[Biologics in development outnumber small molecules for the first time - BioWorld News](https://news.google.com/rss/articles/CBMirwFBVV95cUxPTnc5Z0dfejloaEI5OHQzNmhxVDZZU0FlTjhGc21xTzlHMUU5TmFkci1QZ0ppNVpqVmtYU2Z2UEVkaEJGVTlSTnkxUG1jS0U4VndOX0VWeXJUem9rcHEtMEI0VFZnSE5CSHJmQWRyYUIySG45N0dxU0lqSk1SNFJXNjhSSGMyakQ0NEc0NHcyUmt6bFEyWkRXcEpSdG1mVVdWellON093SUh3N3BzNDhj?oc=5&hl=en-US&gl=US&ceid=US:en)**: Biologics in development outnumber small molecules for the first time &nbsp;&nbsp; BioWorld News
- **[Companies partner to accelerate development of sugar reduction solutions - Food Business News](https://news.google.com/rss/articles/CBMivAFBVV95cUxPWXRfOFU0U05qLUFXSVNucmNRSDBESURCbk00T25iWk51NWlYTC1xTmpyUUNycDVDNTEzSWFGMGNSZHByTkl4dldvV2g2V19nMkI1dWFhdzhoOEVvVlc3VWFfQkVfRTNjWThqTmZGLUV0Vl9CeGNxS3BmcVVBQTRhWXZFMG5vY2hKcC1GaHRaaTZnb2tkb3g4dmIzSkhfLV9sREoyY3FxM3NPc0ZDQzAwZUxOT0JmNWxiRzh3Rw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Companies partner to accelerate development of sugar reduction solutions &nbsp;&nbsp; Food Business News

---

## 💼 Jobs & Opportunities

- **[AbbVie hiring Senior Scientist I - Bioinformatics, Biotherapeutics and Genetic Medicine in Worcester, MA - LinkedIn (Bioinformatics Careers)](https://news.google.com/rss/articles/CBMiqAJBVV95cUxQakNyMFhCV2RNeVlFQ1dkek54UU9kZGUyRmtfcmZVX00yZm0xZDlDRVJYY1g2YWVFRHhFeUg5RnV5VzNtNHZvVl9kWDVDc3hJdEFNUWFHb19vZEZjZUd2ZlJTci1DVC1fM0NCaVhUZjIzOEVLY0J6eFJReGhYSmp3RWN6VFNsR3BDQlN2OGgxN0lCbXZuYjBXOGl1Z1k2TGt4YW9hM2tENW1nOEZaWEpmZkpIeDFvajdJNUxqNGdGOWhhQmR6ZHoyVU9qVFoxZzhGZkpIOVRSZXItWnJpT1psV3NwQWFoT2R2LVZCYUpUNWVscjIxQXlxd0t3UHdGekxnWXI0cmo3SUczcWNZZko3aGJyUjhhdDRJMHBuZWxRNE1tN0lBMVllUQ?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Broad Institute of MIT and Harvard hiring Computational Scientist I - Computational Biology in Cambridge, MA - LinkedIn (Bioinformatics Careers)](https://news.google.com/rss/articles/CBMiywFBVV95cUxPQ1VKUi1EOTF1bFJfdWZHQlF6WGk4bTNCMHBmb2ZoVXc5NU5nYXNQS3JjSlZXT0Q5Q2NUbmd5NEpmNTM5blBHdkFzQl81bERBS3pqa2dmWEgxVmpxaGhwOGpvLUhTeVZtczAyUC1FczNjZ2lOSGswakxUdFFmckp3UUwzU0VDREgzeHpXMTdxM3lOMVpOZDBhS2xOU2pMek9uTUdCcjNRcTN4VXYyVXJKMnAtS3lWNmd0dnU4NXVXV2VMMDdZRFh3WXFBcw?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**
- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
