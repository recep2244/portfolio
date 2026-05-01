---
title: "Weekly Digest: Apr 27 - May 01, 2026"
date: 2026-05-01
description: "A curated summary of the top protein engineering and structure prediction signals from Apr 27 - May 01, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Apr 27 - May 01, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, May 01

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, May 01

- **[Discovery of potent ALK tyrosine kinase inhibitors for thyroid cancer via machine learning modeling, molecular docking, MD simulations, and DFT study.](https://doi.org/10.1016/j.compbiolchem.2026.108960)**: The ever-increasing need for effective therapeutic management of thyroid cancer (TC) necessitates the exploration of novel approaches for advanced drug discovery. The current study employed a robust computational pipeline integrating Machine Learning (ML)...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[The past, present and future of de novo protein design.](https://doi.org/10.1038/s41586-026-10328-7)**: With deep-learning-powered advances in protein design methods, there is an ongoing paradigm shift in protein engineering from random selection to intentional computational design methods. Here we describe the current state of de novo protein design. While...
- **[Enhancing CYP450-Ligand Binding Predictions: A Comparative Analysis of Ligand-Based and Hybrid Machine Learning Models.](https://doi.org/10.1021/acs.jcim.5c01098)**: Predicting cytochrome P450 (CYP450) ligand binding is critical in early-stage drug discovery as CYP450-mediated metabolism profoundly influences drug efficacy, safety, and adverse reaction risks. However, experimental determination of CYP450-ligand...
- **[The transformative impact of AI-enabled AlphaFold 3: evolution, current status, and future prospects in structural biology.](https://doi.org/10.3389/frai.2026.1739303)**: The AlphaFold (AF) initiative profoundly impacted structural biology, evidenced by its 2024 Nobel Prize. AlphaFold progressed from AF1 to AF2, which achieved near-experimental accuracy in single-chain protein folding, and then to AF3, expanding predictions...
- **[NNDock2: A neural network-based scoring function for ranking protein-protein docking models.](https://doi.org/10.1142/s0219720026500058)**: Protein-protein interactions (PPIs) play crucial roles in diverse cellular functions and biological processes, and structural knowledge of the protein complexes is valuable for the elucidation of those functions and designing new drugs. Due to the...
- **[Investigation of the potential mechanism by which methylparaben induces psoriasis: an integrated study using network toxicology, molecular docking, molecular dynamics simulation, and eight machine learning algorithms.](https://doi.org/10.1093/toxres/tfag003)**: Psoriasis is a chronic inflammatory skin disease with limited safe and effective treatments. Methylparaben, a widely used preservative in cosmetics, pharmaceuticals, and food, is an emerging environmental pollutant linked to immune-related skin disorders,...
- **[Evaluating zero-shot prediction of monomeric protein design success by AlphaFold, ESMFold, and ProteinMPNN.](https://doi.org/10.1002/pro.70453)**: De novo protein design has enabled the creation of proteins with diverse functionalities that are not found in nature. Despite recent advances, experimental success rates remain inconsistent and context-dependent, posing a bottleneck for broader...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [ColabFold](https://github.com/sokrypton/ColabFold) - Fast AlphaFold2/MMseqs2 pipeline for large-scale predictions.
- 🛠 **Tool**: [RoseTTAFold](https://github.com/RosettaCommons/RoseTTAFold) - End-to-end neural network for protein structure prediction.
- 💾 **Dataset**: [SCOPe](https://scop.berkeley.edu/) - Curated structural classification of proteins for fold analysis.
- 💾 **Dataset**: [Pfam](https://pfam.xfam.org/) - Protein families database with curated multiple sequence alignments.

---

## 🤖 AI in Research Recap

- **[What Happens When AI Transforms a Specialized Field Overnight? - Kellogg Insight](https://news.google.com/rss/articles/CBMirwFBVV95cUxOSWVnZE40RGtqa0hsOWpaRUNtTHQ2OUVuX2hCTWVSLVBoSlByQ1ptQUJvYV9BcGszSWxtRjR5d0ZsbGZKakh0MGRyNG5QTzJhWDFpcF9hRW1hVk1lY254eV9jVXJmUHBZbWdiamthU3FRQkRCLVgxdS1vVlhjeWVMWGUyQ3hvTUhuV0FfcDBCNXV4REZfTEtfeU5aQmVOcE16SGZ3d3l6bHpVc2lxbmxF?oc=5&hl=en-US&gl=US&ceid=US:en)**: What Happens When AI Transforms a Specialized Field Overnight? &nbsp;&nbsp; Kellogg Insight
- **[An integrated strategy for mapping intrinsically disordered proteins - AIP.ORG](https://news.google.com/rss/articles/CBMinwFBVV95cUxNelFNS2hMYTNGQmZZb1ZCVTVyNXJISThtMGFZQkIxYWhRRkw5ejBiaFNMZ3djbm5ZeFA2dzNjM1JoWndlUTU1WEc2SVNiVTdiMVJqWVRBN1M4OEVkTklhRU5qeG5RM3FRbXktVG1saGVmZkZsaWptanBRcDF3SEgyYjlFWk83b0RVNVA2Tnk3ekxMdFVzbkNTcFNiT2JoYU0?oc=5&hl=en-US&gl=US&ceid=US:en)**: An integrated strategy for mapping intrinsically disordered proteins &nbsp;&nbsp; AIP.ORG
- **[Sun Peck presents at Molecular Biophysics Training Program/Center for Structural Biology Seminar Series, today - Vanderbilt Health News](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOUVNGMnl5TV9JMmhUaWYzaG5QbEVpOUZWODdHYlBZb09xdG55cWV2WEdsS3o3aXlCUk9XUTI2Z3RhdUt6dXAyN2xuYWhjMmQ5eE5DU3BlNGd2Tk1KNnh1MW9qN1hCUERlTURBekVTR2RtWXJxWUQ4YlRkVDdBeE0xaFRua29aUFAySUF5dTZvMFFTYTA2dG8xY0pGWC16U1lFcDVPTUNfUm05eS1NUVFxbFpfYjlMMHAtRV9DdjVtUkVhWTA?oc=5&hl=en-US&gl=US&ceid=US:en)**: Sun Peck presents at Molecular Biophysics Training Program/Center for Structural Biology Seminar Series, today &nbsp;&nbsp; Vanderbilt Health News
- **[Brenig Therapeutics to Present Hybrid AI Drug Discovery Platform at Keystone Symposia Computational Advances in Drug Discovery - BioSpace](https://news.google.com/rss/articles/CBMi-gFBVV95cUxNVVprOHVNX19jWlNhWlJTZExIVTc5WTVNOERDWjNOaWh5aldYQnRQb2I0dEJGejNydFdFQmZ1N1Z4SFFjZm5mVVoyYXkwN0dYSjZhNmgxcFkyVXdnQmNvRmpneGZGS2xBd1ZLNm9Hb194dVR0eXNiTk1wc1dCcm1LNFVIc2dNcEM1YW5acHVWbnBqVXJwTmtNMHlyWmNuN0NsN1RQbFZ3NHVfVC1IRkVFSXJIaFViX3RLWHNvZGU1bldqTTFpRUUyQWFYUmw5NkdDN2NFQW0ycVE3ODk2dDl6YkNWc2tkbTYyTFNXMS1jRGdsOVlwSDFWR0Z3?oc=5&hl=en-US&gl=US&ceid=US:en)**: Brenig Therapeutics to Present Hybrid AI Drug Discovery Platform at Keystone Symposia Computational Advances in Drug Discovery &nbsp;&nbsp; BioSpace
- **[AI-designed drugs near human trials as AlphaFold enters clinical phase - Mugglehead Investment Magazine](https://news.google.com/rss/articles/CBMimgFBVV95cUxQeWl2RGpRRlFiVFVZQmtSeDZWZXo4T2xOYUY4aHA1RGIyTFVrckVrVk1CLWdzaUhBSkR2ZmV3U0x0a3g1WkdNRTgxU0dDTTJ6S2tQWFVxbDVmcnQzNEp1ODhIdlh1Z3NuUnU3WDBnbU5sN1Y1UXFlQnV0aHVKYkNCNkNobGZaaWI0cndVQkh6enEtOTNyTzZVZFl3?oc=5&hl=en-US&gl=US&ceid=US:en)**: AI-designed drugs near human trials as AlphaFold enters clinical phase &nbsp;&nbsp; Mugglehead Investment Magazine

---

## 🏢 Industry & Real-World Applications

- **[European Union Mammalian Transient Protein Expression - Market Analysis, Forecast, Size, Trends and Insights - IndexBox](https://news.google.com/rss/articles/CBMizwFBVV95cUxPWklNV1QxZFdaaG5yZzVGYk41NWRYc0pfdGRzcXpGQ3hNaHdoLU5kTWpTbU9vWS1lRWxXbnpIRVNqYjVMRmV6Y3VBUFExbWNDLXVMQ2RMeDhGV0NjUExlR2lMMzRXb29DUUN0ZXNhdFgyWG5ROTNib2lDR0tYSTk1aWpMdFVZWnFWcTN3NFQ3T3BWRWxXZHNZWnRiZlk2ZkpfYnhkbFFyT1RhOVhfMWRwQnh6UklBanRqZ2FicWkybk42SzlWR0tyZmw0X24yYnc?oc=5&hl=en-US&gl=US&ceid=US:en)**: European Union Mammalian Transient Protein Expression - Market Analysis, Forecast, Size, Trends and Insights &nbsp;&nbsp; IndexBox
- **[IPO Tracker 2026: Avalyn beats expectations with $300M debut - BioSpace](https://news.google.com/rss/articles/CBMiX0FVX3lxTFBOZU9ySndUUGJrdkEyMDJubkhYMENBeUI3aUtiYVFCb1FEaU9vNXFsN18ydzBPOE5DcmdGQ1ZmaFhHbEpyV0R1TWF5OUZvUXBYZjJESkpfcDlmbWlPdWg4?oc=5&hl=en-US&gl=US&ceid=US:en)**: IPO Tracker 2026: Avalyn beats expectations with $300M debut &nbsp;&nbsp; BioSpace
- **[National grant to fund new biomanufacturing training program in South Dakota - SiouxFalls.Business](https://news.google.com/rss/articles/CBMiqAFBVV95cUxNVzB5OS1WaDFEYVI2dHlKdFk3VEIwYmFWZVV6UFExZlFuV3k5OGF4ZVZhUHJsTmppbjNMN2dkS2NwWnZxZjg0NGxLLWQ1QlprMjNoeUJwYTBGd2swM2tIWEtkRXlNVFhqU3Z1LWpWNXBkM2RQUmdjb2tkbXI1U3BiU09zOWVLT0drM2NJeUFLaHJ3bzJnZEV4X2FRNkN4U09JUHJwYmFicnY?oc=5&hl=en-US&gl=US&ceid=US:en)**: National grant to fund new biomanufacturing training program in South Dakota &nbsp;&nbsp; SiouxFalls.Business
- **[BMS calls time on Zymeworks collab, ending work on bispecific - Fierce Biotech](https://news.google.com/rss/articles/CBMiswFBVV95cUxNdTlTUG9yMTVoSFpnc2t4ZzlxTHVtZ3F3ZkQyTWlvNTFlZEh6VkNOUmU0RExxbVIySlVWbTJjU1V2S19TTnQyS1lqc3g2bVVNTnhvdTUxQ0F1RFFGTmVka28xRzg3TnVjalJleHA1Y200bWE2Zy1hWHNRYkFoZWlPVGExZGZ5SjhpOHRqYTJjWWlnS1o2UTAzNjhBN1dtVHQxVFRwaEw1OU9Fanh6dG0wZ1RJcw?oc=5&hl=en-US&gl=US&ceid=US:en)**: BMS calls time on Zymeworks collab, ending work on bispecific &nbsp;&nbsp; Fierce Biotech
- **[Vir Biotechnology Rebuild Centers On AI-Driven Drug Discovery Platform - AIM Media House](https://news.google.com/rss/articles/CBMisgFBVV95cUxNLWxYQTNZbWc0Ukg2OXNjdVVhUzRoRGtzblAxNjhXTWZmdkdhTzdsNHB0b0dRaE1fQlQwcDRrTV9sU0JFbTNCU3Z0TEI4TElVQ0pyM09DVUdFdldhWjh6RC1rVFc2ai1nRWZLU3czNlV1TW9PeWN1dzJNc3lHeUFaUUlzM1ZlOVlWamlzdGlhMmhqamRwbG12eHpsZUkxbTlXUXB5RlVtVDNabHRrRHVvQkFB?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vir Biotechnology Rebuild Centers On AI-Driven Drug Discovery Platform &nbsp;&nbsp; AIM Media House
- **[Advancing Sterile Liquid Development: Enabling Integrated Solutions for Small Molecules and Biologics - Contract Pharma](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQMEtIX2JrTlFSZHRnV1ZucmhEbFVGWUJobzUxclZ1NVlFYkxGeFdybDJNUjd3cllGTUQ2U09Udl80aXAxeG16LUJnR0ZrV1VNU1NQV2cyd0xPSnJsVFJPUnFOZjNMeFMzdGpjVmFublVyUEpHYjdVWjZTVlFHZ1VNSC1RUjQwVVJJR0d6dGJtY3d6VTZEM1lWYU5YRVU1Uk5MRlVIcEVfTFJpMzFYd1RqcDVFMTR3ODByVVk3b3FpRm1VS3pLaGVuaXU4N2M0ZEREaXdHSzFrZw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Advancing Sterile Liquid Development: Enabling Integrated Solutions for Small Molecules and Biologics &nbsp;&nbsp; Contract Pharma
- **[AAX Biotech and evitria partner on antibody development - Drug Target Review](https://news.google.com/rss/articles/CBMipwFBVV95cUxON0NIVE1SLXhGczExY0RQd2xNWEtZYldXNjhWX2NfLTJuYk5hTWJFdkFYMUVlYTlYbnlBMG43NmdORDF2N2xoZ0RIUU1COGxOUDVZMVV6V1BGRU16NFB4MEswNU1yRHN3OXJ4X1dYTHpWT2VCdGRLeFI3UWJfcDlGN2hIUmFjbkFZRlJmc3FScXZEa1VuU2VnV1hNUEx3aHl0NFEzeUVMYw?oc=5&hl=en-US&gl=US&ceid=US:en)**: AAX Biotech and evitria partner on antibody development &nbsp;&nbsp; Drug Target Review

---

## 💼 Jobs & Opportunities

- **[Job Application for Head of Translational Sciences, Drug Design, Cambridge, MA at Isomorphic Labs - Greenhouse (Greenhouse)](https://news.google.com/rss/articles/CBMib0FVX3lxTE0wVHBNemQxNTNWazVKeFZYM2JZMEdSS09udnZDblA1RTVCWXpPQ2VCYVE5Y1E1X3RwVk4zWDgteGtDNjVEMXQtaUNWbUdSOHdTUk1Jb2ZaUEx5bnp6SzlQMS1DNHpPMG0wck9FSFI3NA?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[ML Scientist I / II, Foundation Models for Life Sciences - Greenhouse (Greenhouse)](https://news.google.com/rss/articles/CBMibEFVX3lxTE8yMGJMSk1jVUpWQmVKRkRBUjl4TmFMLXk5aUtXd1lNWHhGZnBSRW41clpyZElmbDNETV96MlNsZDFtbXcwaFhJRXFwem91LTRQeUp3bnBfYlVWZUlOWVdwTFhvNThPa0FjbnJaeQ?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**
- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
