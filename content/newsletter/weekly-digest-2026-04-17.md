---
title: "Weekly Digest: Apr 13 - Apr 17, 2026"
date: 2026-04-17
description: "A curated summary of the top protein engineering and structure prediction signals from Apr 13 - Apr 17, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Apr 13 - Apr 17, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Apr 17

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Apr 17

- **[Discovery of potent ALK tyrosine kinase inhibitors for thyroid cancer via machine learning modeling, molecular docking, MD simulations, and DFT study.](https://doi.org/10.1016/j.compbiolchem.2026.108960)**: The ever-increasing need for effective therapeutic management of thyroid cancer (TC) necessitates the exploration of novel approaches for advanced drug discovery. The current study employed a robust computational pipeline integrating Machine Learning (ML)...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[A New Insight into the Study of Neural Cell Adhesion Molecule (NCAM) Polysialylation Inhibition Incorporated the Molecular Docking Models into the NMR Spectroscopy of a Crucial Peptide-Ligand Interaction.](https://doi.org/10.3390/biom16010019)**: The expression of polysialic acid (polySia) on the neuronal cell adhesion molecule (NCAM) is called NCAM-polysialylation, which is strongly related to the migration and invasion of tumor cells and aggressive clinical status. During the NCAM polysialylation...
- **[Enhancing CYP450-Ligand Binding Predictions: A Comparative Analysis of Ligand-Based and Hybrid Machine Learning Models.](https://doi.org/10.1021/acs.jcim.5c01098)**: Predicting cytochrome P450 (CYP450) ligand binding is critical in early-stage drug discovery as CYP450-mediated metabolism profoundly influences drug efficacy, safety, and adverse reaction risks. However, experimental determination of CYP450-ligand...
- **[Investigation of the potential mechanism by which methylparaben induces psoriasis: an integrated study using network toxicology, molecular docking, molecular dynamics simulation, and eight machine learning algorithms.](https://doi.org/10.1093/toxres/tfag003)**: Psoriasis is a chronic inflammatory skin disease with limited safe and effective treatments. Methylparaben, a widely used preservative in cosmetics, pharmaceuticals, and food, is an emerging environmental pollutant linked to immune-related skin disorders,...
- **[Evaluating zero-shot prediction of monomeric protein design success by AlphaFold, ESMFold, and ProteinMPNN.](https://doi.org/10.1002/pro.70453)**: De novo protein design has enabled the creation of proteins with diverse functionalities that are not found in nature. Despite recent advances, experimental success rates remain inconsistent and context-dependent, posing a bottleneck for broader...
- **[Comprehensive Molecular Docking and Molecular Dynamics Reveal Inhibitors of HER2 L755S, T798I, and T798M based on a Large Database of Curcumin Derivatives.](https://doi.org/10.31557/apjcp.2026.27.1.265)**: Objective This study presents a methodology employing virtual screening to identify curcumin derivatives with selective affinity for the HER2 mutations L755S, T798I, and T798M. Methods Curcumin derivatives were retrieved from the ChEMBL database and...
- **[Predicting the Mechanism of Action of Bawei Chufan Soup in Treating Teen Depression through Network Pharmacology, Molecular Docking and Molecular Dynamics Simulation.](https://doi.org/10.2174/0115734099381670251024040419)**: Introduction The Bawei Chufan Soup (BWCFS) in Traditional Chinese Medicine (TCM) offers unique advantages in treating Teen Depression (TD). This study utilizes network pharmacology, molecular docking, and molecular dynamics simulations to predict the...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [OpenMM](http://openmm.org/) - GPU-accelerated molecular simulation toolkit.
- 🛠 **Tool**: [AlphaFill](https://alphafill.eu/) - Ligand and cofactor transfer into AlphaFold models.
- 💾 **Dataset**: [SCOPe](https://scop.berkeley.edu/) - Curated structural classification of proteins for fold analysis.
- 💾 **Dataset**: [Pfam](https://pfam.xfam.org/) - Protein families database with curated multiple sequence alignments.

---

## 🤖 AI in Research Recap

- **[As OpenAI releases GPT-Rosalind for life sciences research, we test out the new AlphaFold and PubMed plugins - R&D World](https://news.google.com/rss/articles/CBMi4AFBVV95cUxQR2RRZm5nc1pVdlZ1UElRbDJjOWRrUlhiRjZSaTFnMUU4aFdUYUZtMjFRTlBtMk1pdFRwMlRiZDRzZmdDZmgwaVAwdzdJQi1GSFBrX3dVdjlLZkJiSVc1bkd6dEFfUFpCcnZyT0xkdDhvM1RXUFdCLTlOU3MzUFhSWnNscEhKczZVV05WYzhlUDJ2Yy1GTHFuNDc0R0lqMkdiNU51QWdMdFpRU1pHdHF4Mi1ubzF3MVM2ZzhONmRDS3Vfd1BxWFhoOFI3cDVseEhpZWJ1aHo2NnctSWhiU2lBdw?oc=5&hl=en-US&gl=US&ceid=US:en)**: As OpenAI releases GPT-Rosalind for life sciences research, we test out the new AlphaFold and PubMed plugins &nbsp;&nbsp; R&D World
- **[OpenAI to rival Google’s AlphaFold with new AI model for life sciences research - Silicon Republic](https://news.google.com/rss/articles/CBMipAFBVV95cUxQckhJWktycy12S3ZKX0cyVDBVcVZmMm10b0tnU1lBNDZxTGhUOTNwUF9HeEJmdS1UNHdoRE5XNkNDaVF2SHp3c3JJdXYwWkVOS2V3YVRwV3JPeGxmYmtYdHMzRFhWTzB0a3YybGtFYzRDeXlNVV9DMEw1VW8teUtxTWt6WDEtbFIwa0JMSFNsd09KWWRzY3ZfXzVRbmRYa19pX1NyNQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: OpenAI to rival Google’s AlphaFold with new AI model for life sciences research &nbsp;&nbsp; Silicon Republic
- **[What is OpenAI’s GPT-Rosalind and how it differs from Google DeepMind AlphaFold - The Financial Express](https://news.google.com/rss/articles/CBMi0gFBVV95cUxPYXNFOG5uWnBKN1FVWC1qYUJ4VUJiT1Zuc1RvQXl6a1ZFbDhHQU4zdmxJN0k0UVhPZ1dBYlFZdEZyYWRHUDlFSktPSklGaFNLTUVtS29leXdtNFNoNFVNNXppMG5ZSVh3MFprWnhucW42LVF1SlN4Nk9LWmdlcldCOFFBUmV3VzBCQU8wVXU2eWxyWm1nZFl6NzdidmtDRmw1MC1Lb3kzVC1ZTDdLeVc1X1BnbV8zczFHaFhKb21DbzNhZ2xWZ21lbC1ab3E4LW9ucWfSAdgBQVVfeXFMTTByZ1JGS2lBLUNvckoyZksyS1dIR3VjNVhMekhsMG9sTmZBZUt2WnBDbmR4dXEzTFJaeG5xNEVtNDFGUS1aRlZvSUxrNmFRWEVWSlVxbXZ2c2hwWDhEcmRYclVRM2Uycm1GeHRyeEZ1WU1ra21tNm9OaTQyVWRPeE56LVlpeUNBNDBZVXg5ekdDTmJ5bldlX1JTLWtoY1JGc0ZrRUFmdmRtUFRKa1dsQmc2NUxRemNNeV80dXhFdy1vVFpfbThqR0tkLU5LUVFZR0sxM3NtdnJt?oc=5&hl=en-US&gl=US&ceid=US:en)**: What is OpenAI’s GPT-Rosalind and how it differs from Google DeepMind AlphaFold &nbsp;&nbsp; The Financial Express
- **[Pill bugs don't just use the minerals they eat—they rebuild them inside their bodies - MSN](https://news.google.com/rss/articles/CBMi6wJBVV95cUxOcUx0OTZBNTNuS1ZiUV9zWHhqS1paQ2lCWVBVTTdUQ2Q2eU4xOU1CVXdfdGROdDNYQXQyY3p3NkE2ZUdQNHUwUWpObHZIeU5hYzJwSlpwN2kwS2pnZzN4eTd0NU9PSEJDN3VXQy1qQWxXYWhaOXEzNkgwb3lzdTFLTDVHc1hlZU5EY0IxSGRONlQzTVBDMGE5NFpab2xoYkdzQUZBSmdUeXpBQlJzOW93dTlCUXo4RWdWLTgyWm1MTVZzV3BHQ1N0VEFNSXZvSm9XX0w1N1RldllFQkx5Ukkxd1BoZDhxV2hSMUtBZTg0NjNYWldac1BPVFZKUlJxQjQ0RThaVllhZmw3bGlSNjNOSEhUX0MzQmcteUlEeWdudU15LWFEMnpfSTdZRld1d2JFeThURjRiQnlDTW84cGRxUHQzYnVOZTZHbjZxYVZOa0hLRFdMNU1nMHlwcklZUWN0MzVYVTYtTy1vNDA?oc=5&hl=en-US&gl=US&ceid=US:en)**: Pill bugs don't just use the minerals they eat—they rebuild them inside their bodies &nbsp;&nbsp; MSN
- **[OpenAI goes after Google DeepMind's turf with a new biology-focused AI model: GPT-Rosalind - Neowin](https://news.google.com/rss/articles/CBMitwFBVV95cUxNTkNoc1BCMUhORG1MU2ZKM3U2c05YQ21LR3pvQWR3WUhEVzgxeE9ZRmVRVmN1MHhvUUNsZ3BPOUdWN2JIelg1b3IzVGcwaV9aUVlTNDlNbHVMMm8tZ2F0S3NCVlpuWHM1aUw5QUdUdlJKdjBlV1daVy1MZm1wdzF2WVctaFpHZjVyWkVaNkJHbVE4dG40MEJaTkYxX1VBaC1RNlhKbVhFcmNFUmxkLVVGdGxLVm9hTWfSAbcBQVVfeXFMTU5DaHNQQjFITkRtTFNmSjN1NnNOWENtS0d6b0Fkd1lIRFc4MXhPWUZlUVZjdTB4b1FDbGdwTzlHVjdiSHpYNW9yM1RnMGlfWlFZUzQ5TWx1TDJvLWdhdEtzQlZablhzNWlMOUFHVHZSSnYwZVdXWlctTGZtcHcxdllXLWhaR2Y1clpFWjZCR21ROHRuNDBCWk5GMV9VQWgtUTZYSm1YRXJjRVJsZC1VRnRsS1ZvYU1n?oc=5&hl=en-US&gl=US&ceid=US:en)**: OpenAI goes after Google DeepMind's turf with a new biology-focused AI model: GPT-Rosalind &nbsp;&nbsp; Neowin

---

## 🏢 Industry & Real-World Applications

- **[Kailera nets $625M in one of biotech’s biggest-ever IPOs - BioPharma Dive](https://news.google.com/rss/articles/CBMimAFBVV95cUxORTZwdFF0bkVNbjdPN1VpSVVKeGNvMkVYVnlCa2NveWtmRUUzLTktNWxwTnFrYnZEb3NEZUxmQXY2M1RHR1NIeS1WUXNFTDBRXzROd3RSazFxeFpDQmFxMjE1cW9NWWJNUDU1Q2MxTXY4Y3djZmZWdDBReDB5MFd0a1ZCWDVwSkVvMmMwWHVVWEJBRmloQlRETw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Kailera nets $625M in one of biotech’s biggest-ever IPOs &nbsp;&nbsp; BioPharma Dive
- **[Vir Biotechnology (VIR) Valuation After Astellas Partnership And New VIR 5500 Trial Milestone - simplywall.st](https://news.google.com/rss/articles/CBMi5AFBVV95cUxQaFN5LThmSm5LZVdNX0lqOFNuY0VWa1B2M19sU1lBcFlCeFlhNnRnbFV0RXhHMTdVOU9HT1JhUnRBMGZ0MUEzaGR5ZmpWN3FWT0o4dHRrLURmWkRIcHE3Wkx5aVAxN1JsaEtBb1lCYXNrdXltQy01R0pteG8xSVkzRGNaY3VlNjFHQmlKczNCZW5ocW14WGRhUko3bmU2Q2ZCWmxKMnV4cE1hR25uRDVCMXNxakZVYkhqbUcxamd5TTFKeTFwR0NtQkRsZXAzbzJGMTZRQ2ZWUGV3d3ZvY0xVZ2liUW7SAeoBQVVfeXFMUHdwUlFOOHFEdTk5akF2WHlJeG9fbFFEU2VTeVdPRTZKcTFZZ29mM190Zm94c24yZzRPcDBmbHpDVnlwUThJT0RCYlJBc0x6SFR6UlE4R25WOWZ4NWkwcnN4cTVXQVhtQlN5a1BaVHBpYjZqMVg5TnNPMzlWLUZjWWp0bGMwNndTUWl3eEFCODFSSTQ2bmo1TmxlOGVPRnc1SU01ZXk4dk0yMS01N1Zvbnhkb1l0MGV6NUN4dEhxUGtVb2dtRlRMdlo3b1d2NW03bmNGeTM2Vmp1MTJkZmJqMnVKWEc5dTdSeV9B?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vir Biotechnology (VIR) Valuation After Astellas Partnership And New VIR 5500 Trial Milestone &nbsp;&nbsp; simplywall.st
- **[ATUM Names Genentech and Eli Lilly Veteran Gavin Barnard as Chief Scientific Officer - citybiz](https://news.google.com/rss/articles/CBMiwAFBVV95cUxNQWdMSWdMb0FoS0d3bTI0WW5sTl8xZFpHZlBGTzhlcDlBbFk1WjFVaWpkRnU0aS1nTTRMS2tqVl9CeUpSbF90TW5OWDlCRldiZkFCY1dTVl9nRW5wdGg3QXpXYVMxNW1uWVgxVWNDdFVrelZWLWV2ZHFURjA3aEtSWVlWbzl1M1FSQUlJRkV4Ri1LTXhYR3BrMTk0NVhvTVBnY2h4ajMxb191TmlWMnZ4RVNfVHdiLUZMMlZvWUNsdng?oc=5&hl=en-US&gl=US&ceid=US:en)**: ATUM Names Genentech and Eli Lilly Veteran Gavin Barnard as Chief Scientific Officer &nbsp;&nbsp; citybiz
- **[BIO campaign reiterates what’s at stake if biotech funding slips - Medical Marketing and Media](https://news.google.com/rss/articles/CBMibkFVX3lxTFBWZUNCSzQxSlNJOHJ6NFFkakV1bllTcE43VlIxRG10eEFJNDlmeS0xc21WTkpBd0R6N1Y4T3UxSExFYUp4R1paU1g1R04zMjVOZWVQZVNrdnh5dzNWOWd2QXp2Q0lidFRMTFROWGV3?oc=5&hl=en-US&gl=US&ceid=US:en)**: BIO campaign reiterates what’s at stake if biotech funding slips &nbsp;&nbsp; Medical Marketing and Media
- **[Investigational New Drug CDMO Market Forecast Points Higher Toward 2035, Driven by Biologics Complexity - IndexBox](https://news.google.com/rss/articles/CBMizAFBVV95cUxOTmlZalMyTGVheXlaMEYyWVJPaUVBYkhrWXRreTE3S1lUaTdVcG5jWm51RTdwUl9IczdLLU9fNlQyTXJNNmVocEZlLVNIRk5ZWVFhZXVxRjFGYVV3bEprdm55aEtUR1FOT09tMHlqRjFJcGYxUS03T25QdnFLMnpDSEtiT1VaMkhHd0NzNS1GbHJTdnVxWGgtWlRicVh0ejRtUWJfcHRLbWkzQW5xRVNqY19vQW04WWFLRlRya3Q5MF9yTmRuZUlMN0szRFE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Investigational New Drug CDMO Market Forecast Points Higher Toward 2035, Driven by Biologics Complexity &nbsp;&nbsp; IndexBox
- **[Spain sets up Boston-focused VC fund with goal of raising $200M for biotechs - Fierce Biotech](https://news.google.com/rss/articles/CBMivAFBVV95cUxOdkJDT2hCTWt3RFpwR0RDZS1IbDI2QlB5RHVia3o3bDBRTUtIYkczS0hMOGIwQmJrSFNIUFA1Nko1VWN1UnJNZERWNzFMZFI1VTBmYS0wV1pLYjA0NlVuQVBkdmtSNURXa2RXUjVzbkFYTXl3dzBvcEE5TmF6NVVTNGxaWHM4Wmx4dVJHNkE0M3FTZ0FLcl9lc2tEcm51R0RneWFpUi1TYzY5b3dYR0VnQ2lNQ014NlViWTcyNQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Spain sets up Boston-focused VC fund with goal of raising $200M for biotechs &nbsp;&nbsp; Fierce Biotech
- **[Biologics for Psoriasis: Are Dual Inhibitors More Effective? - Everyday Health](https://news.google.com/rss/articles/CBMiqgFBVV95cUxOWEpXTFhoeEozbFhGY3dtSUYzTzM0SGJHQjJxRHUtWlZnZVgwS1VUUWhhNk5KdEVlTkplMG5MVUdyTlVBU0JIdWFnNXVhMlVpUmRvTVB0d2RyN1hFTk1KbzRTSE12Qlk4VEt4ZGlvX2hLNnRmNlZCQXlPN0xucFhvNGtSN0NLdW15SVB5a08yT2U3VExpNE5meGtKU1VEdmZOZjJ4bFUwUnBTZw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Biologics for Psoriasis: Are Dual Inhibitors More Effective? &nbsp;&nbsp; Everyday Health

---

## 💼 Jobs & Opportunities

- **[Genentech hiring Postdoctoral Fellow, Computational Biology & Medicine/Neuroscience in South San Francisco, CA - LinkedIn (Bioinformatics Careers)](https://news.google.com/rss/articles/CBMivwFBVV95cUxQdWZEV0Y2N3h4cENyOXhHQmlrWkpRSVNEcC1IaWFXTXpWaGRWeVItTkRZVzZxMmNPaG0zalJrcXlXR0NBMU53X0RZTDllLU9tTzNFUmMwV3JCcWg5ZnBUbEJneUZ3aUN1cDhDS3VLNUVjQTltekxRcFVZQ1NmM2IySjZUblR1TXRJdEhJVVpQbV9mN2lMU21XQVFhTEx0MkxvU2VOUDBoZXBDYVhLQ3pMZGhZb3BxVS1JNnhZRTNpSQ?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Mercor hiring Senior Bioinformatics Scientist | Upto $110/hr in United Kingdom - LinkedIn (Bioinformatics Careers)](https://news.google.com/rss/articles/CBMiowFBVV95cUxQRXdzelAzeWNjd2xKblBoN19zRGxjclpLZU90QlJEcnF5QjJEdDA4NF9fMzBhNXFCRktDVzZyUnNPZWFuNk9PSE5CZVE4MDF1Vm1KQU5NRE5Ma0lNZU1OcTB3NDI1R2JGOTRtRUd3Q1k4OExIU0R1OXdXdmZmT0psVjJkVlRWOGpqTjRGY3ZBV1psallwODJwbGhidnA4cnlMRTFr?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**
- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
