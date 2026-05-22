---
title: "Weekly Digest: May 18 - May 22, 2026"
date: 2026-05-22
description: "A curated summary of the top protein engineering and structure prediction signals from May 18 - May 22, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**May 18 - May 22, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, May 22

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, May 22

- **[BA-Pred and RMSD-Pred: Integrated Graph Neural Network Models for Accurate Protein-Ligand Binding Affinity and Binding Pose Prediction.](https://doi.org/10.1021/acs.jcim.5c02591)**: Accurate prediction of protein-ligand bound poses and their affinities is essential in structure-based drug discovery. Here, we present an integrated deep-learning framework that disentangles the two core tasks─affinity estimation and pose...
- **[PlantP450Dock: an Automated Molecular Docking Pipeline of Plant Cytochrome P450s](https://doi.org/10.64898/2026.05.12.724510)**: Cytochrome P450 enzymes (CYPs) are the primary drivers of chemical diversification in plant secondary metabolism; however, fewer than 10% of the superfamily members have been functionally characterized. Computational docking provides a scalable strategy to...
- **[AlphaFold and the Transformation of Structural Biology: Evolution, Applications, Limitations, and Future Directions](https://doi.org/10.22541/au.177282022.20654724/v1)**: The protein folding problem is the challenge of predicting a protein's three-dimensional structure from its amino acid sequence. This problem has been a central challenge in molecular biology for over fifty years. The advent of AlphaFold, a deep learning...
- **[Discovery of potent ALK tyrosine kinase inhibitors for thyroid cancer via machine learning modeling, molecular docking, MD simulations, and DFT study.](https://doi.org/10.1016/j.compbiolchem.2026.108960)**: The ever-increasing need for effective therapeutic management of thyroid cancer (TC) necessitates the exploration of novel approaches for advanced drug discovery. The current study employed a robust computational pipeline integrating Machine Learning (ML)...
- **[Benchmarking generative scaffold design methods for peptide engineering in TCR-MHC complexes](https://doi.org/10.64898/2026.01.22.701133)**: De novo peptide design at T cell receptor-peptide-major histocompatibility complex (TCR-pMHC) interfaces is a central challenge in computational immunology, with direct implications for vaccine development, cancer immunotherapy, and autoimmune disease....
- **[Integrating glycosylation in  <i>de novo</i>  protein design with ReGlyco Binder Design Filter](https://doi.org/10.64898/2026.04.16.718906)**: Artificial Intelligence (AI)-based methods for 3D protein structure prediction are revolutionising structural biology 1–7 , providing novel templates for experimental data refinement and an on demand 3D perspective on any molecular architecture and...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[The past, present and future of de novo protein design.](https://doi.org/10.1038/s41586-026-10328-7)**: With deep-learning-powered advances in protein design methods, there is an ongoing paradigm shift in protein engineering from random selection to intentional computational design methods. Here we describe the current state of de novo protein design. While...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) - State-of-the-art generative model for de novo protein design.
- 🛠 **Tool**: [ProteinMPNN](https://github.com/dauparas/ProteinMPNN) - High-speed sequence design optimized for fixed-backbone folding.
- 💾 **Dataset**: [BioLiP](https://zhanggroup.org/BioLiP/) - Verified biologically relevant ligand-protein interactions.
- 💾 **Dataset**: [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/) - Residue-level mapping between PDB, UniProt, and other resources.

---

## 🤖 AI in Research Recap

- **[Google I/O showed how the path for AI-driven science is shifting - MIT Technology Review](https://news.google.com/rss/articles/CBMitAFBVV95cUxOOFNwMmpOT0pBOGZyYzN0ZkVzTjQ1RHZTNmgwMVdacGN3MEszYzM2TXhQZGhvc3FLX2ZRNS16azdqaUJ0R2F3RUhnUVo0bDhJSTEzM3U2S1otUS14STBFaml4SXVGZ2g4bDR6N19RZ2FveGVHVEY1WUVoUmZHTjZWRHVtbmJoX0dJQ004ZEdUSk5yWlZfd2lEVW13anFLX0trdU5MUEtsNUhHTk9nOXR6UHF0RjPSAbQBQVVfeXFMTjhTcDJqTk9KQThmcmMzdGZFc040NUR2UzZoMDFXWnBjdzBLM2MzNk14UGRob3NxS19mUTUtems3amlCdEdhd0VIZ1FaNGw4SUkxMzN1NktaLVEteEkwRWppeEl1RmdoOGw0ejdfUWdhb3hlR1RGNVlFaFJmR042VkR1bW5iaF9HSUNNOGRHVEpOclpWX3dpRFVtd2pxS19La3VOTFBLbDVIR05PZzl0elBxdEYz?oc=5&hl=en-US&gl=US&ceid=US:en)**: Google I/O showed how the path for AI-driven science is shifting &nbsp;&nbsp; MIT Technology Review
- **[Varsity Don Explores Brain Signals In Addiction, Chronic Pain - LEADERSHIP Newspapers](https://news.google.com/rss/articles/CBMiiwFBVV95cUxOckZmRzdwMWJxc3FDelFrdWlEWlQzR00wMG1zQmUxblF3aWNDWTdmbzJTWjNYSjkwb2l5b2lWNmc5NV9UZ1BRZW1taGdjNXZBVXROVnFmaUprVEZoOXFrS19kd0RoTFIwOWxYV0xIUVg0UWVMOEJ5VExjU0xzRTd3REYwR1FXMFlrV0RV?oc=5&hl=en-US&gl=US&ceid=US:en)**: Varsity Don Explores Brain Signals In Addiction, Chronic Pain &nbsp;&nbsp; LEADERSHIP Newspapers

---

## 🏢 Industry & Real-World Applications

- **[TaiMed Biologics Completes Phase 2b Enrollment for TMB-365/380 HIV Therapy - The Clinical Trial Vanguard](https://news.google.com/rss/articles/CBMiugFBVV95cUxNbEtSV0xBN3otTkJEVXpWZkdfM1Jmc0NnRGNfZjR0QUs1VzJIc21WSjJmeUV4OWtjWU9kTUxEZ1RyZXo2NE9IWGJCVmtKdVl4ZlpLMEhjR1lEaWVHSEl5OVBFVXJ3NHJXLThSUmlleVN5eTRoWEM2eHNfRkZHZmJUV0NLb0gwVWhMUWJkZG1EZ2h2TDdDeUsxMm5WZzJjRHIwU0NibVJCLVluYzVOOTBFZTBvc3Z0Y3FDWEE?oc=5&hl=en-US&gl=US&ceid=US:en)**: TaiMed Biologics Completes Phase 2b Enrollment for TMB-365/380 HIV Therapy &nbsp;&nbsp; The Clinical Trial Vanguard
- **[TaiMed Biologics Completes Phase 2b Enrollment for TMB-365/380 in HIV Maintenance Therapy Study - GlobeNewswire](https://news.google.com/rss/articles/CBMi-wFBVV95cUxQMDM2eHJSQ2lyXzY2YjBvNVlDMWxJS2Nhd0ZLbG8yRkozWHktek1keXg1eHRsaXZqMVVGMkM0eUZkT21PZUtpSzRzRUJFR2N0ZVR5MWpQNVc4S2k4eVRZR1E4aXQ5WHRmcndhajhhSkhPdC0tVDRNOV9TVS1tV053YmYwSS1vaDVjX21mTU1ibW5Ld05lakF0dFNRRlJZTVVFakZrcTBudmFHYjNDZ0s4cVVsQmo4VG90X0tmTGdsNV9hYUlrZlJiQ3gwRU1fZXJnYm53LXY1RG0zdHV1em5xbXV4MzFmUnNyZDZIMVpjRUJ2SXdyOWZCMm8xdw?oc=5&hl=en-US&gl=US&ceid=US:en)**: TaiMed Biologics Completes Phase 2b Enrollment for TMB-365/380 in HIV Maintenance Therapy Study &nbsp;&nbsp; GlobeNewswire
- **[2026 ASCO Abstract Highlights: Innovent Biologics' IBI363 (PD-1/IL-2α-bias bispecific fusion protein) Demonstrates Robust Survival Benefits in Long-Term Follow-up of PoC Study in Advanced Immunotherapy-Resistant Non-Small Cell Lung Cancer - Yahoo Finance Singapore](https://news.google.com/rss/articles/CBMikAFBVV95cUxNV2V6RnUwZHZYaGZPOTlNTHJybWw5cEhfQU5KYy1NN2NwbWVQaVJwc2xKaUVnZU9NRnoyeTFDc3owUm9hZGdHNEhJRy1QZ3VYSmFSZGRUeEpLSnBDYU5PTkh4UkkwUXhVaG1iOUpIMWNzVklOdThwMGgzeGJQa2NBVnJLbjlPV21yNUYtSnFnSFo?oc=5&hl=en-US&gl=US&ceid=US:en)**: 2026 ASCO Abstract Highlights: Innovent Biologics' IBI363 (PD-1/IL-2α-bias bispecific fusion protein) Demonstrates Robust Survival Benefits in Long-Term Follow-up of PoC Study in Advanced Immunotherapy-Resistant Non-Small Cell Lung Cancer &nbsp;&nbsp; Yahoo Finance Singapore
- **[AI healthcare and BioToken partnership expands WORK Medical’s (WOK) digital asset ambitions - MSN](https://news.google.com/rss/articles/CBMi1wFBVV95cUxPaUNMZUNwbjVxSGg1Q056aUplMU1UcC1NcHdNYU5LT09Ta095ZHF3NWlZQjFGckVOVXd1UkszY1VoMllFdFRoM1Azall5d0pOcUhKWDdMYnQ1RTUxQjBMZkVEcjh4bHplZFN4MzdfMkwwMXpOZmoyZ0U2QXRVWnNWTFdXUkY3czhKU3FLUDM5SFFQRTZKcFJ0bG5nSHBPZ0g2YmRqMll5ME5Fa2VSdTBrb3N0RXNiR0dyQjZObS02akRMMlBfcGE1NGM0VENGZ0x3Szd2NXR6RQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: AI healthcare and BioToken partnership expands WORK Medical’s (WOK) digital asset ambitions &nbsp;&nbsp; MSN
- **[After raising $800M, Parabilis seeks an IPO to pursue ‘undruggable’ targets - BioPharma Dive](https://news.google.com/rss/articles/CBMikgFBVV95cUxQaWY4U081RV94bms1c3pwM3hVVXAyQURBUDM1eHNIOXROWjA5QV9zbWhEczhick5LVHg3bWhKS1lvLVVFRTFWQ0VKazVNdXBGTWhfZjBxSVNTWU9xVDdyMzBWNEFCRk03WWFhaEtHSG80SC02SjcwSVFuUkR5Z1BHSjd4akEwUGpfWW1UcHpJaHdTdw?oc=5&hl=en-US&gl=US&ceid=US:en)**: After raising $800M, Parabilis seeks an IPO to pursue ‘undruggable’ targets &nbsp;&nbsp; BioPharma Dive
- **[Hengrui, BMS deal watershed moment for China biotech - BioWorld News](https://news.google.com/rss/articles/CBMilwFBVV95cUxPcFVXbHp2R2toQ1A2cXdFaXNYOGR5Y1Y3QkV5WU1kQkZZcVVPWjFMc3VqVmNqVTJ5dEFONklNbGFzWFIzYmY1UWM5Z3B2akxqNi1MZGM1QVRqY1dQZVlIeVhTaTNIYjFsdk9waWJCRFM5YWdfUkhmWjVPelQzckVWaVVNaVMzdDJwa0hvYTBQNEZwd2lhU1Nz?oc=5&hl=en-US&gl=US&ceid=US:en)**: Hengrui, BMS deal watershed moment for China biotech &nbsp;&nbsp; BioWorld News
- **[PharmAla Biotech Signs Term Sheet for $100 Million U.S. Licensing Deal for ALA-002 MDMA Therapy (MDXXF) - Yahoo Finance](https://news.google.com/rss/articles/CBMipAFBVV95cUxOYXJNMjB4U2F2SElxSkhNbDNHY0llSVVybk9UYllEd0Vrc2JfUnJCbWxuOUJXSUIwUkNPVnRUREZMUHFvUFByS1NqQk9RajNDVlQzUjZjelY2OW9ldkNsYVdhTnJrbGxiNHVTek5fbG9hSEh1ZkxsV0FGRnpiRVdOXzYxbmxHTnpBd3BNODVrdWF0QzMwNWpYWGdzanlyeWd4U0F4Zg?oc=5&hl=en-US&gl=US&ceid=US:en)**: PharmAla Biotech Signs Term Sheet for $100 Million U.S. Licensing Deal for ALA-002 MDMA Therapy (MDXXF) &nbsp;&nbsp; Yahoo Finance

---

## 💼 Jobs & Opportunities

- **[Korro Bio - Senior Scientist, Computational Biology - Lever (Lever)](https://news.google.com/rss/articles/CBMifkFVX3lxTE1ldlR0X0dQZ2ludlY1T1pNcEp6d20xWWZjRWpSYmMwZDhRVW53VHR0Tld3dTBHNGlwUGRiR0Nvb1NhNzBwTTY3Vjg2bGp6eURqWXYtZDhRdVhLWm50cDFUVWRDbFA4dk9OWTJMNkYxTHNYZmRfVDVVNjlqY3YtUQ?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Simply Protein for Pets, Inc - Senior Business Intelligence Analyst - Lever (Lever)](https://news.google.com/rss/articles/CBMifkFVX3lxTFB5YV85SUVBbkowQ0dEaEhHMVhZZUxHWlB3NUJyWnFkSWNzOE40VEowd1VyWmpydFI2TXB1SW9nNEg5V2V0M3hnODFqZmxmUHUxX0xPX3QzcGlmclVsOUJvUGs1TVJOODVNc1dZMlFKMkRPMWJYUU9sV0cxcEIyZw?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**
- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
