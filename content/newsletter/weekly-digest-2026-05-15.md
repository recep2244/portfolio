---
title: "Weekly Digest: May 11 - May 15, 2026"
date: 2026-05-15
description: "A curated summary of the top protein engineering and structure prediction signals from May 11 - May 15, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**May 11 - May 15, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, May 15

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, May 15

- **[Classical Docking to Machine Learning Based Docking: Molecular Docking in Drug Discovery.](https://pubmed.ncbi.nlm.nih.gov/42136460/)**: Molecular docking has emerged as a cornerstone methodology in computational drug discovery, enabling the prediction of ligand-receptor interactions with considerable accuracy and efficiency. This article provides a comprehensive overview of docking...
- **[BA-Pred and RMSD-Pred: Integrated Graph Neural Network Models for Accurate Protein-Ligand Binding Affinity and Binding Pose Prediction.](https://doi.org/10.1021/acs.jcim.5c02591)**: Accurate prediction of protein-ligand bound poses and their affinities is essential in structure-based drug discovery. Here, we present an integrated deep-learning framework that disentangles the two core tasks─affinity estimation and pose...
- **[AlphaFold and the Transformation of Structural Biology: Evolution, Applications, Limitations, and Future Directions](https://doi.org/10.22541/au.177282022.20654724/v1)**: The protein folding problem is the challenge of predicting a protein's three-dimensional structure from its amino acid sequence. This problem has been a central challenge in molecular biology for over fifty years. The advent of AlphaFold, a deep learning...
- **[Discovery of potent ALK tyrosine kinase inhibitors for thyroid cancer via machine learning modeling, molecular docking, MD simulations, and DFT study.](https://doi.org/10.1016/j.compbiolchem.2026.108960)**: The ever-increasing need for effective therapeutic management of thyroid cancer (TC) necessitates the exploration of novel approaches for advanced drug discovery. The current study employed a robust computational pipeline integrating Machine Learning (ML)...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[The past, present and future of de novo protein design.](https://doi.org/10.1038/s41586-026-10328-7)**: With deep-learning-powered advances in protein design methods, there is an ongoing paradigm shift in protein engineering from random selection to intentional computational design methods. Here we describe the current state of de novo protein design. While...
- **[PathDiffusion: modeling protein folding pathway using evolution-guided diffusion](https://doi.org/10.64898/2026.01.16.699856)**: Despite remarkable advances in protein structure prediction, a fundamental question remains unresolved: how do proteins fold from unfolded conformations into their native states? Here, we introduce PathDiffusion, a novel generative framework that simulates...
- **[3D-QSAR, Molecular Docking, Molecular Dynamics Simulation, and Pharmacokinetic Prediction of 1H-Pyrazolo[3,4-d]pyrimidine Derivatives as PI3Kδ Inhibitors.](https://pubmed.ncbi.nlm.nih.gov/42136309/)**: The inhibition of cellular inflammatory factor secretion by phosphatidylinositol- 3-kinase δ (PI3Kδ) makes it a novel target for acute lung injury therapy. This study aimed to elucidate the structure-activity relationship of 1H pyrazolo [3, 4-d] pyrimidine...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [ReFOLD4](https://www.reading.ac.uk/bioinf/ReFOLD/) - Sophisticated protein structure refinement tool for improving model quality.
- 🛠 **Tool**: [FunFOLD5](https://www.reading.ac.uk/bioinf/FunFOLD/) - Automated system for protein ligand-binding site prediction and function annotation.
- 💾 **Dataset**: [SCOPe](https://scop.berkeley.edu/) - Curated structural classification of proteins for fold analysis.
- 💾 **Dataset**: [Pfam](https://pfam.xfam.org/) - Protein families database with curated multiple sequence alignments.

---

## 🤖 AI in Research Recap

- **[IBM’s MAMMAL model puts open AI drug discovery in sharper focus - Startup Fortune](https://news.google.com/rss/articles/CBMilAFBVV95cUxOakROYnBlY3JkOXZmVjhOTzFYWDFZUjNfX3lJR2ZwWFhzSmZaSTFnVkhuYjFyZlA1ZTBrOGZYU1o1QjRyUlFnTURrb0FsQ3dCQmk2WUlMaEhhSmlhd1U0RlNpaENVaDhpdUF4OFpjSHlxM0ZzM01adkRIQzNFU2RIdnQ2VEttUm5Tdm9iR3luYk5SN0Ey?oc=5&hl=en-US&gl=US&ceid=US:en)**: IBM’s MAMMAL model puts open AI drug discovery in sharper focus &nbsp;&nbsp; Startup Fortune
- **[Demis Hassabis Raises $2.1 Billion to Use AI to Cure Diseases - Greek City Times](https://news.google.com/rss/articles/CBMiiwFBVV95cUxQVFdSV0pkUXFWVTRQcndNS0lyclFTa0xjZE5od0RRZEQ5TkNYVC1jZDVLbkgxYkcwLUp6WlNaU2toUW5kcGd5S251NUgtcXZhX25WQzVfVm5yMHhVeWhpM3FJNnRvdERvb1ZDTXFNSEtzdnpRNWVkT1p4X3dVMTNtZ1NnQkppa3pGUEFv?oc=5&hl=en-US&gl=US&ceid=US:en)**: Demis Hassabis Raises $2.1 Billion to Use AI to Cure Diseases &nbsp;&nbsp; Greek City Times
- **[Jade McDaniel presents May 19 at Molecular Biophysics Training Program/Center for Structural Biology Seminar Series - Vanderbilt Health News](https://news.google.com/rss/articles/CBMi4wFBVV95cUxNNHB5a2cxU1hObVY5ckJYTmxuUXBGRGp0cjNCTDZxaURkUEtpQkhiRUtEbk52OEtBX3ZId2F2Z2xJaEZWWFd5YmdUeVhLbzVyQjA5OEtTNkNEWEFua093RGhDcmJ2eVpONFM4TE1Kd0lPeTd1a3U3NWswQVQxUXJWOXg1YmxLZTBxUm9yaVA3bS0wbU4yWmFoNjZ4NEExMWlyQlFpdklTUWxKRFgtbzRXWnBTM1REUEN1QVIxUUVYZ2dsUkQ0LS1uazhCN3AxNUNrOGlyUEFkUWRGMWhlbXFHXzB5TQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Jade McDaniel presents May 19 at Molecular Biophysics Training Program/Center for Structural Biology Seminar Series &nbsp;&nbsp; Vanderbilt Health News

---

## 🏢 Industry & Real-World Applications

- **[Envudeucitinib Shows 68% PASI 90 Response in Phase 3 Psoriasis Trials - The Clinical Trial Vanguard](https://news.google.com/rss/articles/CBMisgFBVV95cUxPWElWd0trU2FwMEdtWE9NYzFDa1UtVW5LdGUxNDhISHVSUlVoczYySWUwUHNDRFhpamFrdGsway1KSUkxT3VKMkVvbko5X09HcmJXTFd2c3pLNmtIQk1nMzVIRm1HaWVNeEVreGk3RjdJMVZ4TGhIX3JJTUNkaEx5ZUJQR2kwS25FMENKOEExVjRMS1NxZVpZTmpCMEt3VFRVR0RuV1Q4ZHk2Q3hJUEtDdUh3?oc=5&hl=en-US&gl=US&ceid=US:en)**: Envudeucitinib Shows 68% PASI 90 Response in Phase 3 Psoriasis Trials &nbsp;&nbsp; The Clinical Trial Vanguard
- **[World Pharmaceutical Glass Container - Market Analysis, Forecast, Size, Trends and Insights - IndexBox](https://news.google.com/rss/articles/CBMi3gFBVV95cUxQaURIbkZKUi1PWFZzLWNjTzh6SWExNEE1ckVMa0I4cXdHalRxXzV3ajJKb1p2d0ZxSXRaSnRoelVEY2JsWEttckUtTHFCd3J5eVZWSVRHQW5zb0p2SG1IV2RpUkpISmFLbGVpdU12WTNBVWxiQmttbWpDNW5ia3N2X0ZyVGN3NllUWHAzOVZaSVlSRGZ5V252aVhuRkVaQWNaY0JELWZrUHFGMkpWOFlGcThJUDlCTkRuOHJhM2tUSkNWWEpmbXJEZVJRenBPQjAza3haMnA4TmdEdlBQWnc?oc=5&hl=en-US&gl=US&ceid=US:en)**: World Pharmaceutical Glass Container - Market Analysis, Forecast, Size, Trends and Insights &nbsp;&nbsp; IndexBox
- **[What Were HCW Biologics' Key Developments in Q1 2026 - Kavout](https://news.google.com/rss/articles/CBMijwFBVV95cUxPMlhzRUdDclRJMmVOWFZWazV5OW00S1I5MUsxRERNYTZSYUFMdE1IeGcyZ1IyRTdMWmRacVdZWDR0Y3FfdE9nc0tvbERCa2tPb1JsdTBMdl81RFc2R0hISzVuaFNwU0VxWUVrZllrVnVvOUszY0pfcmpXOEdWeGdUc3VkQ01RQVR5ZmJkcGxWdw?oc=5&hl=en-US&gl=US&ceid=US:en)**: What Were HCW Biologics' Key Developments in Q1 2026 &nbsp;&nbsp; Kavout
- **[BioHub Maryland partners with NIBRT to train biotech workers - BioProcess International](https://news.google.com/rss/articles/CBMiwwFBVV95cUxOcGlPeWg1Q1VRaGh6cm0zYkhYcWZSTEFoTWJkMmpUaExKVTJESlhKMFFwQzA5Qy1XZUtsei1IVFZ0c0pCcHphX09TbllnMmlxMHlsMF84RWdQWFdiaUdHMEc5dVJPZ1YxQk5pQUZtd0R6UDJBVFVwU3NPam5UcTlBcUlXenRvY3RDUGYyNXd6aGNnaEo5LXdrYXJyWG9Kb251XzNpZFl3M2I1U3N5NWx0QmhMVXFjRE51NVREZ3ZyZVU0bG8?oc=5&hl=en-US&gl=US&ceid=US:en)**: BioHub Maryland partners with NIBRT to train biotech workers &nbsp;&nbsp; BioProcess International
- **[Xencor stock (US98401F1057): Biotech focus on immunotherapy and protein engineering - AD HOC NEWS](https://news.google.com/rss/articles/CBMixgFBVV95cUxNV0VZWXF3OUxPVEd3RDhzeVRaVjZhaXotVUxwYWJQOWxCSklZbnNGN3YydDd1RW10M3h5cVVqZXVrNVp2Nks3UkxYQ2YwUXZ3dXBmeWYxOEZmdXVUWUdBMnROOWMxODJnNUdIczZ2VS0tbVpvenNiaUtaQWQtM1FCZmhHU2RVUXdwc3dsd3JaR29fMlFfVWZhdEZIcEdVN1puTjdPOUVTQXNXb0NFaVhSclZGSXh3OXEwM0pZaW5mR2NBa2lQRkE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Xencor stock (US98401F1057): Biotech focus on immunotherapy and protein engineering &nbsp;&nbsp; AD HOC NEWS
- **[Inhibrx Inc stock (US45720L1070): Biotech firm in Virtus ETF holdings - AD HOC NEWS](https://news.google.com/rss/articles/CBMiwwFBVV95cUxQYWFFNmdsWlJHZmpwX1JFTjhQVFZCOFJaa2NaMi1pb1h0bGl6RkRScVNqNjU3Vmx2U1FiaEdwY2lYYUhjeVRHMm84V3k5TUV1MjQ5V2t4Wm1Qd0wtUlNjWXdrUkxacGlzV0RHN29VTE9jQjEtc19BRHVQUnJ5cnlnUGxBdDRQdjdPNkZnSVllaUZJRGJEdDFxS0VHajA2NER4MzJ5MFRiQnFYS0dVOHdlWFZGclFKX3JDeVlIeGZpaC1DM0E?oc=5&hl=en-US&gl=US&ceid=US:en)**: Inhibrx Inc stock (US45720L1070): Biotech firm in Virtus ETF holdings &nbsp;&nbsp; AD HOC NEWS
- **[What investors now expect from AI biotech companies - Labiotech.eu](https://news.google.com/rss/articles/CBMiZkFVX3lxTE1aamwwT3YzcWl4c29yVFp6bHc2M1RHQnVFb1otMTNTbFlNS3VDYllXdk9RUXF5YWdPbURMbEpYUkg1dExmV2d2V0F2WmZJUG5hNjhudHYxaWliSGJhbUxBdzh3aFhDUQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: What investors now expect from AI biotech companies &nbsp;&nbsp; Labiotech.eu

---

## 💼 Jobs & Opportunities

- **[Research Associate in Bioinformatics and Genetics at Imperial College London - Jobs.ac.uk (Jobs.ac.uk)](https://news.google.com/rss/articles/CBMiiwFBVV95cUxPS0dhcVBBaGd1OXNadm5GRU9Ec1kzVG54YzNXWDAzT3ZJSzREY2FHQTE1d0dTTnFWd3VJZndwZ0EwTmttUXR3ell6V2MzRVhVN1RLUmZpX3RDNFhkLWMzdDdCQzVDbU8zOTJQUmtYcUZJcTZuZmVyUklxUjlVbm1xSTVuanAzbXhOeDhZ?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Search - Jobs.ac.uk (Jobs.ac.uk)](https://news.google.com/rss/articles/CBMikwFBVV95cUxPWVZKVG5Sa0c4NDc0T3VZZzRuVTVaNzRBVWN1TUNJYkxNemZCLUZqNjVWUXN6M25oMC13RXZTbXIwcV9KaU9RemI3X3VUZDFMeFRYZlZ6Ry16UXJkck1jdTV2YTJZTTZUNHAycGVnV3IxWjBrY3dfQ2ZyemE0QUJ0eUFmQzZDdnIwU1RLbll5TVFubms?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**
- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
