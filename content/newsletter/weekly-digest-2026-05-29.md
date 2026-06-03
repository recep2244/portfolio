---
title: "Weekly Digest: May 25 - May 29, 2026"
date: 2026-05-29
description: "A curated summary of the top protein engineering and structure prediction signals from May 25 - May 29, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**May 25 - May 29, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, May 29

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, May 29

- **[Classical Docking to Machine Learning Based Docking: Molecular Docking in Drug Discovery.](https://doi.org/10.2174/0115680266424314251204071847)**: Molecular docking has emerged as a cornerstone methodology in computational drug discovery, enabling the prediction of ligand-receptor interactions with considerable accuracy and efficiency. This article provides a comprehensive overview of docking...
- **[BA-Pred and RMSD-Pred: Integrated Graph Neural Network Models for Accurate Protein-Ligand Binding Affinity and Binding Pose Prediction.](https://doi.org/10.1021/acs.jcim.5c02591)**: Accurate prediction of protein-ligand bound poses and their affinities is essential in structure-based drug discovery. Here, we present an integrated deep-learning framework that disentangles the two core tasks─affinity estimation and pose...
- **[PlantP450Dock: an Automated Molecular Docking Pipeline of Plant Cytochrome P450s](https://doi.org/10.64898/2026.05.12.724510)**: Cytochrome P450 enzymes (CYPs) are the primary drivers of chemical diversification in plant secondary metabolism; however, fewer than 10% of the superfamily members have been functionally characterized. Computational docking provides a scalable strategy to...
- **[AlphaFold and the Transformation of Structural Biology: Evolution, Applications, Limitations, and Future Directions](https://doi.org/10.22541/au.177282022.20654724/v1)**: The protein folding problem is the challenge of predicting a protein's three-dimensional structure from its amino acid sequence. This problem has been a central challenge in molecular biology for over fifty years. The advent of AlphaFold, a deep learning...
- **[Discovery of potent ALK tyrosine kinase inhibitors for thyroid cancer via machine learning modeling, molecular docking, MD simulations, and DFT study.](https://doi.org/10.1016/j.compbiolchem.2026.108960)**: The ever-increasing need for effective therapeutic management of thyroid cancer (TC) necessitates the exploration of novel approaches for advanced drug discovery. The current study employed a robust computational pipeline integrating Machine Learning (ML)...
- **[Integrating glycosylation in  <i>de novo</i>  protein design with ReGlyco Binder Design Filter](https://doi.org/10.64898/2026.04.16.718906)**: Artificial Intelligence (AI)-based methods for 3D protein structure prediction are revolutionising structural biology 1–7 , providing novel templates for experimental data refinement and an on demand 3D perspective on any molecular architecture and...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[The past, present and future of de novo protein design.](https://doi.org/10.1038/s41586-026-10328-7)**: With deep-learning-powered advances in protein design methods, there is an ongoing paradigm shift in protein engineering from random selection to intentional computational design methods. Here we describe the current state of de novo protein design. While...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [ESMFold](https://github.com/facebookresearch/esm) - Language-model-based protein structure prediction from sequences.
- 🛠 **Tool**: [OmegaFold](https://github.com/HeliXonProtein/OmegaFold) - Structure prediction from single sequences with rapid inference.
- 💾 **Dataset**: [SCOPe](https://scop.berkeley.edu/) - Curated structural classification of proteins for fold analysis.
- 💾 **Dataset**: [Pfam](https://pfam.xfam.org/) - Protein families database with curated multiple sequence alignments.

---

## 🤖 AI in Research Recap

- **[Vertu’s Alphafold foldable phone has launched, and you’ve got to see its obnoxious price - MSN](https://news.google.com/rss/articles/CBMiwANBVV95cUxOaDhWY01jbDdBWDdDMFBjYWExWmZhdWw5ckpvaF9vUUhrNE5fYXJ5dFU5NndIMGxlZjJVOUMxRTF6M2dIeGYtdDhJWmFWM2w5c3NKQnpnYm00UlhROHZ2OFdmc0tSVUpZNUptZ1MyM3hKc0JLUmdQV2hmaTUySDc3WEZLNHBiZkE0MXBTNVBzNjMtUHBSQ3ZwaHcyUmtmUGN0VExoWXFYbHpkU1RaVGExY3BNc2NiRS1makJiZHppeXVsOXBvV0RJN0V0QjA2Ym1FN1c5akNzR2RYLUx2anVFdWpwT3QwX3BTR3R0Y2JwLVJkU0NGX29OWXVzaEdROUk0WEZ0bFBnQ2xiN0w5NENsRzNhVnNpRGZ5emx2dnFHR0RSM09zcEpLUlg3R2c1dXNJV1p6bS1UQl9Uc2pjLUNTMnJ4LTV3czVoNnpJclVMaVJQRnp3a3VIcEcydE1aNXU4cHdCd1RMS3JUb1RsUkhtSXBCa3ZHNUEzQ2dsbFctbWN6QU9aUldnM1JRYVBwdVAtWEx0MGVzUnIyeVZKLU5IbHAwQlVsZERfNEdTeDV2aFBudG1yTFNuXzFtNFJqeF9q?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu’s Alphafold foldable phone has launched, and you’ve got to see its obnoxious price &nbsp;&nbsp; MSN
- **[Vertu ALPHAFOLD is a $6,880 foldable with an AI agent and alligator belly leather - Neowin](https://news.google.com/rss/articles/CBMirAFBVV95cUxQVU1ublNsWmcxcHBhcHNaM2xmRWRMbGFNZGFVdWxERlVIbDZrenQ0d2hkelV0a0dSYXhXU3lIeVZPbjVnODhLdHdSWWpja1pqUTBPMmgyYVlid1NIMlZnNFdUanZUQUpJdHUtS25jeTZNX0hMeXlYc2hJYXNmMWRjVnp1S2JOelMtV0pUVG5yQVhJbzlsbVcxTV9pcXdOWHBFWHA5Wklpcy1MbVZ6?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu ALPHAFOLD is a $6,880 foldable with an AI agent and alligator belly leather &nbsp;&nbsp; Neowin
- **[Orbital Industries, an “AlphaFold” for materials science, raises $50M - Resilience Media](https://news.google.com/rss/articles/CBMilwFBVV95cUxQWldFeHFPSFRTd201bW9yZUpNRV81aUVYaVU0TFBlTEtxVzRTNjE4VzRpWGZFZ0ctMWJ1VU5JZnVocWo1aXIzMjl4M2drN0lETlJ5OVBuMFFiejM5dDFrSDgwQlZtczRPd0pyQ1B2czc4VVFmVXpTRjVNc2FmV2dlRlZ1NTNzeHpKR05yRnp6c21qdWk5cW5r?oc=5&hl=en-US&gl=US&ceid=US:en)**: Orbital Industries, an “AlphaFold” for materials science, raises $50M &nbsp;&nbsp; Resilience Media
- **[VERTU Launches ALPHAFOLD, the World’s First Hermes Agent Phone for CEOs - EIN News](https://news.google.com/rss/articles/CBMiswFBVV95cUxQOUd5VGVHZTYyRHJ2anB5WFM3dFlDWmRkUjdBWmlsa3dSWnBOR1ptVXUzWU9nUTFYZUpIRkQzYVd4UGh0T0Y4cVdZN1RfVWh1UkxZMTFya1RPVE9nUUs2Z0NRVldLNEkxbkpwX1FMWTdNWEszWnVqUGJBeFpFY1NxNDNfdi00V3lHbFEtYU9DdzZaMDNTbVVKODl4T2xmZGhxeHdfeWlqbG9vbUtpSHlXSUdsc9IBuAFBVV95cUxQcmswNkd1bVlrOGJ1MWZwLWNDRHo5OXBiUXVXdWF4NUJ3ZEEzSEx0MURPdU9rMHFudGJxa0FGbWdpRFJyNVIyVE9NaWhhYWxVeHBRTGZQdjlHQzJTVmktakFaaV9rM3A1ZWFnTkIxanpPbHprQ3YybE5FZ3NlbzlLbHJnZ3RZOHJrWDVYaG9objFZLTNlZDRsZG5YLV9fQXpPc2dzZmtuYnlueGJtaks2V3lNNld2RXlT?oc=5&hl=en-US&gl=US&ceid=US:en)**: VERTU Launches ALPHAFOLD, the World’s First Hermes Agent Phone for CEOs &nbsp;&nbsp; EIN News
- **[Vertu Bets Its Comeback on a $6,880 AI Phone Only a CEO Could Love - Technology Org](https://news.google.com/rss/articles/CBMifEFVX3lxTFBYTlNxUmtNOHVUQVJsQTNtNTJtM0RsRVUtazZMSFhMVUktNkxORGZJT1VGN1JoYkQ2Q1o2VUZEUlUtaEhOd004bzBGREFMWV9GMkppcUtIQXlfMERtYVhiTmVudHlWZ1p1bUQwZ0gzYzVDSnlSaU5pNVBsY3c?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu Bets Its Comeback on a $6,880 AI Phone Only a CEO Could Love &nbsp;&nbsp; Technology Org
- **[Vertu’s new luxury foldable phone is an AI ‘command center.’ - The Verge](https://news.google.com/rss/articles/CBMimAFBVV95cUxNdTJnZ2V2dVFKR0pVRS15cmtOLU43OHVfbm5iSmIxR0NVaHFyMTNDQlR3Q3NGazMzdmdseWNUZlJWTmZocms2U1daVnltT05QamdJQ195ZWZnbGxCcVlhNHl3WWdwU1lyMnFPbDd2QWZzMG9FWjVHd0ZjN1dqMUR0dWU1aDRtSmxhVjR3ZDdsUmI2b09GeVFQSg?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu’s new luxury foldable phone is an AI ‘command center.’ &nbsp;&nbsp; The Verge

---

## 🏢 Industry & Real-World Applications

- **[China’s Innovent Biologics signs US$10.5b Pfizer deal for 12 cancer drug trials - South China Morning Post](https://news.google.com/rss/articles/CBMi1wFBVV95cUxQejNUNFJqUzVuZUdvNWhVMjYzRzRrM3hlX1ZpeWtocjN6SWZaem45djhnX2ZhTm1ZVnpHRFA5alZtWlotUmRyeTR6ak1HbmZvNF9jMjdFTkVEa1dNVmdacmlDOXBOMUs3U2lKODFnbkdVTUYzOXBSc3pILWNKbEZJemhhT2p2UDlfZ0dqZThfMEh1M3M1Y2xYeDF6d2ZUUjVYczJ3UmVhOUR4Smc5NEZwbFl1NWFUOElnVmFYVE5FX2N1SlI3QTk0b09mWHQ3TGo4ZDNjZXB0c9IB1wFBVV95cUxQcVhhVGVKd3k0REF3T2Rham44ZzRfUmo0M2FBcGxfOU9hYlBtMVk3RnRWMGpMbGlzdXR3OEdBOWtjbGJsMVQ4LVdTXzMwOXp2X01WVXc4bTJhSUZtSHgzMWRuN1JhdVRHNW5OajFScS1kMmlQQ09QWDN1b1p1WDBWS2c3QmZrMC13RVNITjVtbFJ6WjRRMEcyaDhGdThrcVBiUUFPaUhJSDRDdW1xVmpmUmNjbDhWZzF2REJFc3czRXhIU3RsWTR4aV82RUNqcXVHVU1Ldk9qWQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: China’s Innovent Biologics signs US$10.5b Pfizer deal for 12 cancer drug trials &nbsp;&nbsp; South China Morning Post
- **[Innovent Biologics, Pfizer strike $10.5 billion cancer drug deal amid China biotech boom - WTVB](https://news.google.com/rss/articles/CBMiqgFBVV95cUxPbnI1UWlFYzY5QVFDZTN5Yi1tTW1PM196TnJKQnBtWWVJM1NrZzc2YkNVeVBhRklFRENfWXM0U3VKZDdxQ0lNVU9Vcjd3ek1hOWVyNHAtbjlIUFBmZlpqbkJMWXF6ZDBZNjI0V2ZfLVlnTlBXSW5KZFJWMGdSMHlFTk5ObzdjYm0tc1hJOS1Qd1d0STFqWWhYVlVJdF9kWklmTE9WUDJVbnBzQQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Innovent Biologics, Pfizer strike $10.5 billion cancer drug deal amid China biotech boom &nbsp;&nbsp; WTVB
- **[Innovent Biologics, Pfizer strike $10.5 bln cancer drug deal amid China biotech boom - Reuters](https://news.google.com/rss/articles/CBMiwgFBVV95cUxNampzaWZlRmdCSXlMZGlrR2VmMTJ3X0JxOVJzSHVsbFhvdENBNDY2Rm5ld05LSzBlSFFacmVKNXJqOXZtdUh6dmpYblgzSmtHal9uQ1FTN2tONXlHd0pHQkFrRFFDQ0JrWjFpSmhYaUNxMWEzb3JnTDVZQXM0RnpoVUdCYXlEaTA5NHJYVWplTC0tUldjS3BsUFJVNmlsd0lkLWhob0ttX09JY2NMbElVRWo5SVVNODg1M3Ixc2JpMEFqdw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Innovent Biologics, Pfizer strike $10.5 bln cancer drug deal amid China biotech boom &nbsp;&nbsp; Reuters
- **[Pfizer and Innovent Biologics Enter Global Strategic Collaboration to Accelerate Development of Innovative Oncology Medicines - Business Wire](https://news.google.com/rss/articles/CBMijwJBVV95cUxOcUlhQWoxMkdtV0RyYXRoTUNhVGIyLVBlYi1hMnhFaE9CSUZDaTMtWE1XMFlJNE0zNGI1NFdCMVc5Y2cwUk5RZThVNVFncFRXWHVpYTlsak9qZlhHMVVqVWpLQjIyZHJHU19TUDdWdXltdllWQWFKYjZOeUptOGRidjZlOFVlSVNMVEpWU0k2NGE3VXRpNm9OR1cwdkpOSXBiRmF4MUh3bTR3aE5heENmVm1nbVF0X2NEYzlkM3FXLUItZEpXcmJkWG5KWDh3UW9nVXJHdnhUek4wNTZTUHJJcUVDVDZhWkhxX1N2aDdaOFdJN2FwQXJYb2Nha1NkOEZub3ExQlJaZEhFWUptVG9J?oc=5&hl=en-US&gl=US&ceid=US:en)**: Pfizer and Innovent Biologics Enter Global Strategic Collaboration to Accelerate Development of Innovative Oncology Medicines &nbsp;&nbsp; Business Wire
- **[J&J Mastered Cancer Biotech Deals on the Cheap. Can It Stay on the Cutting Edge? - WSJ](https://news.google.com/rss/articles/CBMivgFBVV95cUxNWUJJSUxvcHNPU0xkaXpIYkxFNXVoUTJYbWxUVXRwNVFrZ3lBbmxWS0NCSk5WRGFNZ1FzWVE2a05aa3dEY0NxZUxjZzU1RDFMUE9TWFpxd21LY3hPUnoycFdkV3pITHh6cVFoWktXbmktSEp5MzV1SnFVZ3JSbHNzNk41bzUyYk5NaHI3d2U1Qmhfdks2dFd6SU0yUi1ZbDJNQkN6ME5Ta3ltSXBhWFFyWG5IN3JPQmxTVnNHcmpR?oc=5&hl=en-US&gl=US&ceid=US:en)**: J&J Mastered Cancer Biotech Deals on the Cheap. Can It Stay on the Cutting Edge? &nbsp;&nbsp; WSJ
- **[Lilly Continues Biotech Acquisition Spree - DCAT Value Chain Insights](https://news.google.com/rss/articles/CBMigAFBVV95cUxPcFhZUU9LTWtNWGFHdF9wSnkzZkxaRFFaQ2dtYTZKU0JWekg4NG1DQnBFZ1p4T3FoOHNKLVFkM0xoYXhITkwwN0VMcG1NQ3hZVEJWckt4Z1ozekhDem04Rl9PQ3lTUFpYWHdJaFdEODNrQ2dKV0RPSXJLNkFaNjVGMg?oc=5&hl=en-US&gl=US&ceid=US:en)**: Lilly Continues Biotech Acquisition Spree &nbsp;&nbsp; DCAT Value Chain Insights
- **[​JuanHand, PalawanPay forge partnership at FinTech Festival - The Manila Times](https://news.google.com/rss/articles/CBMivgFBVV95cUxPVmpiNkp2TnJ3bHN3dzk4NDNCZklpOVMwUlFFWjRkQlZ6S25ncU8talBCZU9fSjhSaTZXVmFva2dkQVJtS2dMZlJtYnJEcEVlcUw3bHhGN1Exckkyemt2NTBMVmFmX1FrVEdYOERGWFhlZWhGSlpzVmdfbWtaOHpYbjIxWXVnNmM5NEdGWmNOZXRpVWFDZnk2dy1VdVdpR1VsNHJpMVBhcUxQMGFoWmxhMURlVW9qQUZKZThEX1VR0gG-AUFVX3lxTE9WamI2SnZOcndsc3d3OTg0M0JmSWk5UzBSUUVaNGRCVnpLbmdxTy1qUEJlT19KOFJpNldWYW9rZ2RBUm1LZ0xmUm1ickRwRWVxTDdseEY3UTFySTJ6a3Y1MExWYWZfUWtUR1g4REZYWGVlaEZKWnNWZ19ta1o4elhuMjFZdWc2Yzk0R0ZaY05ldGlVYUNmeTZ3LVV1V2lHVWw0cmkxUGFxTFAwYWhabGExRGVVb2pBRkplOERfVVE?oc=5&hl=en-US&gl=US&ceid=US:en)**: ​JuanHand, PalawanPay forge partnership at FinTech Festival &nbsp;&nbsp; The Manila Times

---

## 💼 Jobs & Opportunities

- **[VRS Recruitment hiring Bioinformatics Research Scientist in Slough, England, United Kingdom - LinkedIn (Bioinformatics Careers)](https://news.google.com/rss/articles/CBMingFBVV95cUxQTF9DZ2VGLXNVSW8wNGhxNzRPVUpRU0d3RU01MGVtdFZ5dEplQ29DbmZ5blZoNmk4ZG91dzlDUVFjRHl5cEJLaU84N0hMTnpIQUs1dmk2cUYwbjVxMjN3NWpPanBIbGNJSXEzQ1JKNXZzSmtpWGVZYTRadU1IWWtsVVE3aE16NXFFZjlEWUppeHVKV0pmT21kazlkakRUZw?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Planet Pharma hiring Senior Associate Scientist – Physical Biochemistry & Structural Biology (NO PhD APPLICANTS WILL BE CONSIDERED) in Cambridge, MA - LinkedIn (Bioinformatics Careers)](https://news.google.com/rss/articles/CBMiiAJBVV95cUxNazNtWC1hbUhONW5wUnI0ZUJ6aFA2RlpIeVdhNlh3V0E1MFNZOUxTVGdhaG1SYVFiMlFkUjNqT2VycmZ5cG9ZMTJJeFBfM1dXbGNESWMxZ0V5UW81VkZSeUhsTkd3M0JUUkFpMklTTHJFbGg2ODAtelJuUUlQTjZVbXJWOEpkVTQwWDR2Mmp4aEp3UHJ1SDBNMjRzdEM3RHdfZXRYX2VsQklFdGlJZ2xRNTlGVXliX09icm1Hc3JZYzdpamZhWVdMMkEybmU0U3ZNM0VWZkZlTlFCMXBFSEFISlprMWNSU0tDZ2duaHZfdzJ0SXhYUkFES211TnFoTDdYajVKTEhndE0?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**
- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
