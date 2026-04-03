---
title: "Weekly Digest: Mar 30 - Apr 03, 2026"
date: 2026-04-03
description: "A curated summary of the top protein engineering and structure prediction signals from Mar 30 - Apr 03, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Mar 30 - Apr 03, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Apr 03

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Apr 03

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

- 🛠 **Tool**: [ChimeraX](https://www.rbvi.ucsf.edu/chimerax/) - Next-gen molecular visualization for large data sets.
- 🛠 **Tool**: [AlphaFold2](https://github.com/deepmind/alphafold) - Deep learning system for high-accuracy protein structure prediction.
- 💾 **Dataset**: [SCOPe](https://scop.berkeley.edu/) - Curated structural classification of proteins for fold analysis.
- 💾 **Dataset**: [Pfam](https://pfam.xfam.org/) - Protein families database with curated multiple sequence alignments.

---

## 🤖 AI in Research Recap

- **[Identifying The Limits Of Protein Evolution - astrobiology.com](https://news.google.com/rss/articles/CBMiiAFBVV95cUxOQ3IxZFpLN0llZjRuazBCVW1wUEM2Y2FrS3NFX0lhTjhwclRuN1NseFpVbllfU1I5LWpXWGlFbVVCejFBcnRZV2NWTkVZUFRiUnpfdnVxczhtNVA0R20tUkhBNHAzdnF3c2VSZU9aY3RKSmNOV2NlWVFtU0VfVjdFbTQxZU5RUnFC?oc=5&hl=en-US&gl=US&ceid=US:en)**: Identifying The Limits Of Protein Evolution &nbsp;&nbsp; astrobiology.com

---

## 🏢 Industry & Real-World Applications

- **[Novartis agrees to acquire Excellergy, Inc., building on allergy leadership with next-generation anti-IgE innovation - Novartis](https://news.google.com/rss/articles/CBMi4AFBVV95cUxQYm1xVHpTS1Boekp5RjFFQVROLW05cUpYQWNyMXNJR1JocWlWaE9xRVNwY29ZSTM0TE1IRzdYclNzenBncjlQVE5ubnpCOUJGZzNJTEhEd2ZCZzFxd21sYjZiUDJtUHZXWFlKelRKZTU0NEJBaWdKRkthM0hJUk9ic3RjZnpOZmtkckV6RHNTdjRyTEQ3V21sdk9EUzdUYkJxMEdXMGpuZHdEeHNnMTBnRkNKbHR3elVoMERveF9mMkhGVDVpVk1QMGY5YkdYTHloNGwtQy1FaGtHVkV5QklMSw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Novartis agrees to acquire Excellergy, Inc., building on allergy leadership with next-generation anti-IgE innovation &nbsp;&nbsp; Novartis
- **[Tamarind Bio Partners with A-Alpha Bio to Streamline Experimental Validation for AI-Enabled Antibody Discovery - GlobeNewswire](https://news.google.com/rss/articles/CBMijwJBVV95cUxNbnFhM0lDQVNGaTgtTFZOaUNWcWhNd004Z1NmaXNqYVZ3NlY4cldzMUdxbWo3SUJjZHoyOTRBaUZCZ3JHNnllUnNGRFFCZmdrQWRQX05ERkh6ZEZYZ1ZYRFZxZFZRZVo1TEdnVTBJVE84c0VKbjdzX1JGdTl2Vk52X3lSSVdSMTdpaExZYVpSWVliTDZjUmNBd2ZLLTk4Y241eHZHQUNKQm5ETGlWMWtQTkVnckNEa0ZpQU9OR25oRmJjRE53Wll5N2IwZkN0OFVnTjZDSlJpdWRiX2w0OTAxMFhaTWtDVE5OYjBIWWRKeXNhN0JnRmR0SVBpaWJSZTQybUd2VnZXbXhKQmxNcEYw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Tamarind Bio Partners with A-Alpha Bio to Streamline Experimental Validation for AI-Enabled Antibody Discovery &nbsp;&nbsp; GlobeNewswire
- **[Unlocking the Potential of Biologics with Advanced Drug Product Manufacturing and Development Technologies - Contract Pharma](https://news.google.com/rss/articles/CBMi1AFBVV95cUxQOVl5TWY4U09YMkE4cXRPTThrVDA4cUZfWFFoRjhfelE2Y2gzNklINkozcjkwT0t5Y01ndVpnMjBvbTZsVWZrUDc4SjRLUlVTeUpWQ2llRlpnVzhueGhkN21KSm5CemJMZmxLZExrY2hJRmxHTER2ZXcybmloRlZaYjVZUTdTdHdmaUtXMVFEZ0N0WW9TVmRQZTVpdTllT1ZMeHYya3ctejJYbWw1SzFtVFh1Z0MxSURsSXBaX09ZeUROSW55YVNvVkJ2cDdkdU1YSXFoVA?oc=5&hl=en-US&gl=US&ceid=US:en)**: Unlocking the Potential of Biologics with Advanced Drug Product Manufacturing and Development Technologies &nbsp;&nbsp; Contract Pharma
- **[Orionis Biosciences Appoints Dr. Giulio Draetta as Chief Strategy Officer - BioSpace](https://news.google.com/rss/articles/CBMisgFBVV95cUxNLTV6aFcycEJWMWdXZEdsSmg5RmhkaWp0NXJ6N216WWFyRWJ4cEZ1am1yNWpScGNDbEFxU2FQblp0SWUxQkQ1S090ZTFFWnhIb1lKVnBYWFRDd29MWWNKUHd1VExjdm90Zm9ZV1ZJOWQydXFxVXhFNjYtNG9HQTNzOXVWM3Bac2Q1RWxaMTJzMTBZVkI1WFhuenVwS2JTaTQ0LUVvdC02aTljR2ZaTHZ1aTZ3?oc=5&hl=en-US&gl=US&ceid=US:en)**: Orionis Biosciences Appoints Dr. Giulio Draetta as Chief Strategy Officer &nbsp;&nbsp; BioSpace
- **[Pure Biologics S.A. Stock: Polish Biotech Innovator in Protein Engineering Eyes Global Expansion Ami - AD HOC NEWS](https://news.google.com/rss/articles/CBMiywFBVV95cUxQQUZhcm0tdnpOSkUzX0p0cjlNV1pTUTBUajlpSl92X1RNSU1CcU1pQXpfZlgyWjFJME1vbVc1WjllUVQxN09XLUFUT1dYVmdDSEhxWUYycXF6QnVrYXRRSjdqWDROTEVmdnFDdV9vUlFkNTVRR3RJbFpXOVBIVXJHZ2Q1VG13VEg5a0JqTlpiWmhWQmdIMHkySHV1SGZIWlBhVEpCZXFNMjVjb3BMOHZ1T3BGeHd1Z1NIUkVTakRVM0h3MUlJNVQtVzdudw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Pure Biologics S.A. Stock: Polish Biotech Innovator in Protein Engineering Eyes Global Expansion Ami &nbsp;&nbsp; AD HOC NEWS
- **[Boehringer doubles down on OpenProtein.AI antibody discovery pact - FirstWord Pharma](https://news.google.com/rss/articles/CBMiU0FVX3lxTE5wVHcteEI4a0lUOWg5MVZ3eTFlNUFma1hNdUJpVTM1M3IzbVVNa1JpN3Y0b3FaYURzcVM3SkhJWXREZnFrTHlMbUk4bGFwb0dGTHRN?oc=5&hl=en-US&gl=US&ceid=US:en)**: Boehringer doubles down on OpenProtein.AI antibody discovery pact &nbsp;&nbsp; FirstWord Pharma
- **[First batch of foot-ulcer therapy made for planned human trial - Stock Titan](https://news.google.com/rss/articles/CBMivgFBVV95cUxPaFBSS0tfR045N3lUMkJscm9VanR6ZlVQNk04SWVRWmV5UWNBRWtmZ0VkcWhmYlVidzJZU0RYUXZCeTFsUVg1QzBRQUhWQ2Z6Y3VIZGU5LUN1dmN0NnU4UGNMTDBvTVE5ME1RdUY0djFQNGUwSy15bmt5a1hnSjhnME9fUG9hdmtsSnllRklsME44ZHllNTMtYl85QWRUUGxSZ0tfLURsa3J0d0I4bWxzaVVJZVg0WUdGRTNsLUhB?oc=5&hl=en-US&gl=US&ceid=US:en)**: First batch of foot-ulcer therapy made for planned human trial &nbsp;&nbsp; Stock Titan

---

## 💼 Jobs & Opportunities

- **[Job Application for Sr. Project Operations Manager at fairlife - Greenhouse (Greenhouse Boards)](https://news.google.com/rss/articles/CBMiY0FVX3lxTE5JeVotdTVkVUNRV2RRTmJRZVVteUR1RHR1akoxTHBra3ZEXzgtQmZTUU1TSFN5WWN3U2hwbGY5bFpVMlJpXzQ1bzBFY050NTBZY2FxWi1yWGI4QV94UTNQcFNFQQ?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Job Application for Associate Director, Regulatory CMC at Dianthus Therapeutics - Greenhouse (Greenhouse Boards)](https://news.google.com/rss/articles/CBMic0FVX3lxTFBwblg1QzVYc1dNYTZHLTB1cm5aenZWenBQY09uVTE2Z3JpdGozSUFSdWhNNWRJUjVobktBbjktZEFHV0h4N2xCaE1ZdHhWMTRESVBnXzlZOWc2SWtBb184UF84WkpTWF9fUTRlNmNPdFg2UWM?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**
- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
