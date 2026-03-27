---
title: "Weekly Digest: Mar 23 - Mar 27, 2026"
date: 2026-03-27
description: "A curated summary of the top protein engineering and structure prediction signals from Mar 23 - Mar 27, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Mar 23 - Mar 27, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Mar 27

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://pubmed.ncbi.nlm.nih.gov/41882507/)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Mar 27

- **[Advantages and Limitations of AlphaFold in Structural Biology: Insights from Recent Studies.](https://doi.org/10.1007/s10930-025-10310-8)**: Over the past three years, AlphaFold-a deep learning-based protein structure prediction system-has transformed structural biology by providing near-experimental accuracy models directly from amino acid sequences. This narrative review synthesizes...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[A New Insight into the Study of Neural Cell Adhesion Molecule (NCAM) Polysialylation Inhibition Incorporated the Molecular Docking Models into the NMR Spectroscopy of a Crucial Peptide-Ligand Interaction.](https://doi.org/10.3390/biom16010019)**: The expression of polysialic acid (polySia) on the neuronal cell adhesion molecule (NCAM) is called NCAM-polysialylation, which is strongly related to the migration and invasion of tumor cells and aggressive clinical status. During the NCAM polysialylation...
- **[Enhancing CYP450-Ligand Binding Predictions: A Comparative Analysis of Ligand-Based and Hybrid Machine Learning Models.](https://doi.org/10.1021/acs.jcim.5c01098)**: Predicting cytochrome P450 (CYP450) ligand binding is critical in early-stage drug discovery as CYP450-mediated metabolism profoundly influences drug efficacy, safety, and adverse reaction risks. However, experimental determination of CYP450-ligand...
- **[Investigation of the potential mechanism by which methylparaben induces psoriasis: an integrated study using network toxicology, molecular docking, molecular dynamics simulation, and eight machine learning algorithms.](https://doi.org/10.1093/toxres/tfag003)**: Psoriasis is a chronic inflammatory skin disease with limited safe and effective treatments. Methylparaben, a widely used preservative in cosmetics, pharmaceuticals, and food, is an emerging environmental pollutant linked to immune-related skin disorders,...
- **[Evaluating zero-shot prediction of monomeric protein design success by AlphaFold, ESMFold, and ProteinMPNN.](https://doi.org/10.1002/pro.70453)**: De novo protein design has enabled the creation of proteins with diverse functionalities that are not found in nature. Despite recent advances, experimental success rates remain inconsistent and context-dependent, posing a bottleneck for broader...
- **[Comprehensive Molecular Docking and Molecular Dynamics Reveal Inhibitors of HER2 L755S, T798I, and T798M based on a Large Database of Curcumin Derivatives.](https://doi.org/10.31557/apjcp.2026.27.1.265)**: Objective This study presents a methodology employing virtual screening to identify curcumin derivatives with selective affinity for the HER2 mutations L755S, T798I, and T798M. Methods Curcumin derivatives were retrieved from the ChEMBL database and...
- **[Identification of Bioactive Ingredients and Mechanistic Pathways of Xuefu Zhuyu Decoction in Ventricular Remodeling: A Network Pharmacology, Molecular Docking and Molecular Dynamics Simulations.](https://doi.org/10.2174/0113816128375610250608071339)**: Background Xuefu Zhuyu Decoction (XFZYD) is clinically used in China to promote blood circulation, resolve blood stasis, and alleviate ventricular remodeling (VR). However, its molecular mechanisms remain unclear. Objective This study investigates the...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [PyMOL](https://pymol.org/) - Gold standard for molecular visualization and publication-quality imaging.
- 🛠 **Tool**: [Chai-1](https://github.com/chaidiscovery/chai-lab) - Multi-modal foundation model for molecular structure prediction.
- 💾 **Dataset**: [BioLiP](https://zhanggroup.org/BioLiP/) - Verified biologically relevant ligand-protein interactions.
- 💾 **Dataset**: [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/) - Residue-level mapping between PDB, UniProt, and other resources.

---

## 🤖 AI in Research Recap

- **[Molecular Biophysics Training Program/Center for Structural Biology seminar with Borden Lacy to be March 31 - Vanderbilt Health News](https://news.google.com/rss/articles/CBMi2AFBVV95cUxNbjRwOHdaek4wYW1UbXVsVk16ZnhJNEhQdTF3ckJZOXJrTFdTcGM4RGdyNGNSbTE0TjZBSjZaMlFwaDdOM3dXcTAwWmZadjRmZ0IyRWhnTDcxTXc2dEdra2NxY0JEOEdsWlJ4SXhrc2wzNFVtQWp5RHlWMEl5d0FaN0otVTBOTWpDVFVPeFR6TldwbURzZDRBWE9pd0QyczE0TF94cmJBcHU3S2pnLWtoOFRTeGNjTGxhTVJIZjFITG9YVHdWQWo3Q3FVdnpSWXRXUHA3U2lQcFo?oc=5&hl=en-US&gl=US&ceid=US:en)**: Molecular Biophysics Training Program/Center for Structural Biology seminar with Borden Lacy to be March 31 &nbsp;&nbsp; Vanderbilt Health News
- **[How AlphaFold is Driving India’s Life Sciences Industry - Analytics India Magazine](https://news.google.com/rss/articles/CBMinAFBVV95cUxOUlZLVml1X1U1Rmo3VnNYeFg3bE5lR3RDeW9BR3plNWlHY01RMVR3emlRd1ZOdGVfcWpibUl2UUROLUVzUGZYQ0RkcVo2bTRWNmEzc09YNUtKcm5RY0VrVXNCN3hLS3gwcUhxZGhSbGRPNzFNSnJqeGx4eEtFdHdLOU1neDZUV0lwRmhCcWpPOUNSaHBQN0F5VGRkQU0?oc=5&hl=en-US&gl=US&ceid=US:en)**: How AlphaFold is Driving India’s Life Sciences Industry &nbsp;&nbsp; Analytics India Magazine
- **[AF-pred: a prediction scheme for MHC-II binding peptides based on the prediction of the AlphaFold, along with its validation - EurekAlert!](https://news.google.com/rss/articles/CBMiWEFVX3lxTE9nanJYY0hBWHhpZF9oaEFFYlZzOWlZOVYxRjBFaVg4bHk3S19SSWRMRnlMUS1rc2FGMlhPZWtHVUNSQ1ZzdE1aVmhuVFlSMWRBRHlGbG41NUc?oc=5&hl=en-US&gl=US&ceid=US:en)**: AF-pred: a prediction scheme for MHC-II binding peptides based on the prediction of the AlphaFold, along with its validation &nbsp;&nbsp; EurekAlert!
- **[AlphaFold Can Now Predict Protein Complex Structures at Scale - the-scientist.com](https://news.google.com/rss/articles/CBMingFBVV95cUxOZURxNzdzMy1JZ0hUUkxwSkE4cEQ3X1hWX1VSb2pvVjN6eEpCVE0xLUV3aW5tXzhJRlduSlR3Q2R0ajU0M1NFZXpvWkRrM08wbWljQXZjTkMyYy14WlRaZm9lOTlJR2hrWVFiT1R4TnVTYnMyb0tJU2NmOFpkclBaWC00SUlvNW1WUGNnOWEzNE9XcEt5LXJhZW9JbkFDQQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: AlphaFold Can Now Predict Protein Complex Structures at Scale &nbsp;&nbsp; the-scientist.com
- **[Pet owner saves dog's life by using ChatGPT and AlphaFold to create cancer vaccine - The Standard (HK)](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNZlFNRVVaVzlXcDNOOFhENHVZaUx3R1VLX1g5ZkpHRE9kWFBvZ2J1MkxjVUNjaXRBMDFhRVhlUmpUY3hNem0xMnBIN1dwUXdfSmtJSVM2UVNldFJaN1dWZG44VDV2ZFVBZUdKWUZCRExSeTNpLW50VjI5bnlHZjNvR0s0RkRIdFp1V1h2dHpZdFBFeEtQUndfS1VoWi1jZlpJV2sycURWOXlscVM0YlVPMDVqTy1HMVNsZjJhVTRnNV9idkR0ZFJVZndveTJyT011TWc?oc=5&hl=en-US&gl=US&ceid=US:en)**: Pet owner saves dog's life by using ChatGPT and AlphaFold to create cancer vaccine &nbsp;&nbsp; The Standard (HK)

---

## 🏢 Industry & Real-World Applications

- **[Are Bayesian Statistics Coming to a Clinical Trial Near You? - MedPage Today](https://news.google.com/rss/articles/CBMicEFVX3lxTFBZdE54MW5ZVjFCVEpSTzBIa0x5V0ZrT0EzbnJxT3ZBUGJDNWp1eDJTajVJdVJWamlncEo1Nml2SmxfSkxCdDJrdk80V3NOalUzMjRJbzBGQ05yYnhUOVlXOTZXLVhYUUpjUjlqX09PM2o?oc=5&hl=en-US&gl=US&ceid=US:en)**: Are Bayesian Statistics Coming to a Clinical Trial Near You? &nbsp;&nbsp; MedPage Today
- **[Purple Biotech inks AI collaboration with Converge Bio - The Pharma Letter](https://news.google.com/rss/articles/CBMinwFBVV95cUxNcUczMXVlSFBmdzFXaHRvSGkwZ2VCMXVqYXg2aDlnVEs5ZGdKNFdwSURNOWRXUU1sNktMSVJjdllCZXNuRW5hQzJZallJR3BWX2VIaTZKclJNMzNqZ25DZGFGUFNUWldEaUNoTTZxRDNHZUsyQXNMTFVUMlJtdy10X2ZfcThPRXIwT0NIbld5Slk2U29HUDFtWkRmN3hHLVE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Purple Biotech inks AI collaboration with Converge Bio &nbsp;&nbsp; The Pharma Letter
- **[SK chemicals eyes MASH pipeline in new collaboration with J2H Biotech - koreabiomed.com](https://news.google.com/rss/articles/CBMibkFVX3lxTE5PNWs3SGJVUlZXOE1UbEYtTmVlaGJLNXMySS1fdURVLW1QcmMwOHB0cTdwSnBZUlVMR2NUWXY3VXlQNTQ3TERLMUxTVGRlVFRtQ2U2ZWVhRTFRSU1ZMTlLQzlQMVlzYnBQNWJHbS1n0gFyQVVfeXFMTnN6SGdtWEpfMWdXOGhTVnRocHJxR0ZZWHpqM2d0dk10LThwVXRKaTQ0dlRhbGtvNXcwendGR29YNGNHbVdNaWVJRmtVX2lLV3FpZTR1aDYtOUZwTmp6cDJIMkpTaWhadThUZmMwTU0zb2tB?oc=5&hl=en-US&gl=US&ceid=US:en)**: SK chemicals eyes MASH pipeline in new collaboration with J2H Biotech &nbsp;&nbsp; koreabiomed.com
- **[Purple Biotech Announces AI Collaboration with Converge Bio to Accelerate Development of its Next-Generation Tri-Specific Antibody Platform - Bitget](https://news.google.com/rss/articles/CBMiY0FVX3lxTE1ZY1R3WDA3SmZSZjF0eW1UOVIwWDVhNlRUTzFJOEV3ejRUdldSN0hPVW05NklRMW5kYnhmUmg4QVBPSmt4RHVxbDZaYmoyUjV2c09kcjZnZFdBVkhHd0tta2M3NNIBY0FVX3lxTE1ZY1R3WDA3SmZSZjF0eW1UOVIwWDVhNlRUTzFJOEV3ejRUdldSN0hPVW05NklRMW5kYnhmUmg4QVBPSmt4RHVxbDZaYmoyUjV2c09kcjZnZFdBVkhHd0tta2M3NA?oc=5&hl=en-US&gl=US&ceid=US:en)**: Purple Biotech Announces AI Collaboration with Converge Bio to Accelerate Development of its Next-Generation Tri-Specific Antibody Platform &nbsp;&nbsp; Bitget
- **[Purple Biotech Announces AI Collaboration with Converge Bio - GlobeNewswire](https://news.google.com/rss/articles/CBMitgJBVV95cUxOeHMwQXk4aDdBTHVoWXNSdi1KMnVuRTloMkdTRkNmX2EwUld5dEJ0LVdhTDV5dEVyeDcyRjllbFBvT25Ibko0aUpXemd1YXlSU19TZTYwRnlBNGRmYUppY0VzRlZFV2FqdVY5WUdPS0EyRGdSLVhTcVIyMU1jWE9XUDhSYkEwWVBDejNWNXdJTml5WmtjWEFESUx4SktSbGk5d21aMktvQlRsbmI0Sm5tczYxME1Jb1hjSTRGZ2RwaFBoc244RFZLdkpsbDRxZWY5NlBLZHhQZzRjbDhESmcxWXU2WGRfbENibU4yeDlDR3RlYkhlampLYmpRU2c3YWRLVlc1XzBDcmVCeTR5YjRTMmpuSndWeVBZVG9CMEhzUkk1SE5yRU1Fdk5GbjhTTmNBWDRpWWZ3?oc=5&hl=en-US&gl=US&ceid=US:en)**: Purple Biotech Announces AI Collaboration with Converge Bio &nbsp;&nbsp; GlobeNewswire
- **[Opinion: Biotechs Must Face Reality To Succeed in Today’s Funding Environment - BioSpace](https://news.google.com/rss/articles/CBMirgFBVV95cUxQZC1YMVl6OGRzWS1pd2xzVms0ZDBMY0s0cmVFSmo5czhEaTVCZ2hyQjNDS2NBSnhhRDk0cElTbEtMY3poMHFRU3BxUzhQSGRib2l6Nl85RnBCeVZzVFhPLUJQNkp4dHltVU9zUUNaaS1zeG9CLUlVUTVuWmRCeGRTNjhZbm9TeENfUEZXUjVkenNGSHVTejNTUWJTdzF3SDVkMDZvYUNkS1lyck05NEE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Opinion: Biotechs Must Face Reality To Succeed in Today’s Funding Environment &nbsp;&nbsp; BioSpace
- **[BMS, insitro add two more targets to AI-powered ALS partnership - FirstWord Pharma](https://news.google.com/rss/articles/CBMiU0FVX3lxTFB2a0hxNmhtRkpqWkJDbjRzWHVDdU1kcnRtWWxBc3FEb19SOHNJNDZpNnlsMnNCTjhwc00xWWc5alNpUXRnOTNzZmlGZHQxTGxQVWVF?oc=5&hl=en-US&gl=US&ceid=US:en)**: BMS, insitro add two more targets to AI-powered ALS partnership &nbsp;&nbsp; FirstWord Pharma

---

## 💼 Jobs & Opportunities

- **[College of computing - Postdoctoral fellow in Computational Biology - 10705 - Academic Positions (Academic Positions)](https://news.google.com/rss/articles/CBMi5gFBVV95cUxOMEFhYWhjUWh5cHYyVWNLWlBUUlF3V0RmM0xJOGlPYVlmNjhRQzA3bHotU2I5cjg1MWJrcTJkRGZmMVdaM0JSejZCNUMzRHBEWXZ6QzdyZ25QUDg3aXlaWGpKN09yYnJ6bXQ5SVYwVjRMNGxwa0FHUWVhZHRvUWdYcG9XM3duX3hBeDVJSFd6UlZIeU1acEZlR255WHRCWW9Yb1ZOTU1lTG1VRGRNRFc0MnMwcFhzOU9yZ2ZBU0ZQRTdveDNsdzZZN1VKSEI1N05YeExmbkZhV1BSSm4wM2o1VEVpMzZ5UQ?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[COLCOM - Postdoctoral Researcher: Genomic Language Models for Bacterial Genomes - Academic Positions (Academic Positions)](https://news.google.com/rss/articles/CBMi7AFBVV95cUxObUJiLW5tTU9wLWZYRzNLSWt4VTc0NXRfZjhPNkstU19VWEU5eG1vdDV5NWhJeEwwZm5JN2hJRmVoTjRtVzM2UlgzNUZKMHl6NUtsc2dLRlBKQjJLZl9jcU1MWFZrQXZ0N2FUamF5QV9vVFBwRkVObmZGMlNlUGFxTW5CV0NiYTUxdTdmQkFBRmhSdHE2TS0xdjl2SE1xX2o2MWozSll3NE5GakhyMFlvLTFPRHNkMS1fWTZjQmRHcEFWRVNSZVZWSldtU1hwbktiWlB0X1BWcm1zamVzYTlTcjhyR1VoR3BwZm02Mg?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**
- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
