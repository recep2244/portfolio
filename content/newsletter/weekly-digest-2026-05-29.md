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

- **[Vertu’s Alphafold foldable phone has launched, and you’ve got to see its obnoxious price - MSN](https://news.google.com/rss/articles/CBMipgNBVV95cUxNZjhRSWdCR0ZfelhyVTlpNFZqbjNqR0dvaUt5ZW1IUHc5X2tNM0ItSjR4bHgwZ2NJX01RWlFtVWVZRjJvcFZoNkhZYURnZHBUYlVrOEpvNENfa0ZzSjM2MXdSZS1OR1RSQXpBWS1pdy1FNG54cnFfU2J6QXd5SXFXLXRRakhpUTFld0JocGFjWXl6RW9MS3VPSzhlaHU4end3Z0N5U2tDbHdNZHVjSEdLWGI5T1owd2hoZ0p3Mnh2Y1JhRkNhTEZ2SEZDekxWcDMxV3FONkhqYW9kWmV2RmFlM0hMM0MyWkdpdmpNaWZTSDRGdjEwR2tldU1WbF9KTWFWbVdsLTBJYXdBQlh2X1FQNExiZF93YTBIWUMxZlN3ZzZfV0I1WkExeE9yUmJBNkRreEY4OWtYVmxwWkU1OWhqMWZicmltYy1nOUxVOXpNNGhEQ0RJUG5wT0M3U3RBUUVRSkRTMnhOVVl2dnFUVjFhRG9mWXlfTXl0dGUwN1ZfUXNiY09WQlhBVFdqRkxvVnBEcmxFMXdSQ28tWGxYUkJFOTRuZEVxZw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu’s Alphafold foldable phone has launched, and you’ve got to see its obnoxious price &nbsp;&nbsp; MSN
- **[Vertu ALPHAFOLD is a $6,880 foldable with an AI agent and alligator belly leather - Neowin](https://news.google.com/rss/articles/CBMirAFBVV95cUxQVU1ublNsWmcxcHBhcHNaM2xmRWRMbGFNZGFVdWxERlVIbDZrenQ0d2hkelV0a0dSYXhXU3lIeVZPbjVnODhLdHdSWWpja1pqUTBPMmgyYVlid1NIMlZnNFdUanZUQUpJdHUtS25jeTZNX0hMeXlYc2hJYXNmMWRjVnp1S2JOelMtV0pUVG5yQVhJbzlsbVcxTV9pcXdOWHBFWHA5Wklpcy1MbVZ6?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu ALPHAFOLD is a $6,880 foldable with an AI agent and alligator belly leather &nbsp;&nbsp; Neowin
- **[Orbital Industries, an “AlphaFold” for materials science, raises $50M - Resilience Media](https://news.google.com/rss/articles/CBMilwFBVV95cUxQWldFeHFPSFRTd201bW9yZUpNRV81aUVYaVU0TFBlTEtxVzRTNjE4VzRpWGZFZ0ctMWJ1VU5JZnVocWo1aXIzMjl4M2drN0lETlJ5OVBuMFFiejM5dDFrSDgwQlZtczRPd0pyQ1B2czc4VVFmVXpTRjVNc2FmV2dlRlZ1NTNzeHpKR05yRnp6c21qdWk5cW5r?oc=5&hl=en-US&gl=US&ceid=US:en)**: Orbital Industries, an “AlphaFold” for materials science, raises $50M &nbsp;&nbsp; Resilience Media
- **[VERTU Launches ALPHAFOLD, the World’s First Hermes Agent Phone for CEOs - EIN News](https://news.google.com/rss/articles/CBMiswFBVV95cUxQOUd5VGVHZTYyRHJ2anB5WFM3dFlDWmRkUjdBWmlsa3dSWnBOR1ptVXUzWU9nUTFYZUpIRkQzYVd4UGh0T0Y4cVdZN1RfVWh1UkxZMTFya1RPVE9nUUs2Z0NRVldLNEkxbkpwX1FMWTdNWEszWnVqUGJBeFpFY1NxNDNfdi00V3lHbFEtYU9DdzZaMDNTbVVKODl4T2xmZGhxeHdfeWlqbG9vbUtpSHlXSUdsc9IBuAFBVV95cUxQcmswNkd1bVlrOGJ1MWZwLWNDRHo5OXBiUXVXdWF4NUJ3ZEEzSEx0MURPdU9rMHFudGJxa0FGbWdpRFJyNVIyVE9NaWhhYWxVeHBRTGZQdjlHQzJTVmktakFaaV9rM3A1ZWFnTkIxanpPbHprQ3YybE5FZ3NlbzlLbHJnZ3RZOHJrWDVYaG9objFZLTNlZDRsZG5YLV9fQXpPc2dzZmtuYnlueGJtaks2V3lNNld2RXlT?oc=5&hl=en-US&gl=US&ceid=US:en)**: VERTU Launches ALPHAFOLD, the World’s First Hermes Agent Phone for CEOs &nbsp;&nbsp; EIN News
- **[Vertu’s $6,880 AlphaFold is a luxury foldable with a budget camera problem - Android Headlines](https://news.google.com/rss/articles/CBMiuAFBVV95cUxORWRWZGczV050SlFTa2s0QmlIbnR3SDZGdmlhMmE4RmI3Rlk5WFhWU1JaWElFU0xTT0JVTmE0d0xiT0lTTlJBTjhkb0NjVEk0ZjFKdE51OE5PcHBZTmw5dGUtcWJjeXYxcjdWa2N6RG9uOUZxWXgwVm5WTjJpWnBfWDl2U2FWN1N2eVcwOFJGdEpVVVNKUkFSTmhTSUxpLTRzT0pxOHVjTVpIWmF0ZHFzM1Nvbng2QlY3?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu’s $6,880 AlphaFold is a luxury foldable with a budget camera problem &nbsp;&nbsp; Android Headlines
- **[Vertu Bets Its Comeback on a $6,880 AI Phone Only a CEO Could Love - Technology Org](https://news.google.com/rss/articles/CBMifEFVX3lxTFBYTlNxUmtNOHVUQVJsQTNtNTJtM0RsRVUtazZMSFhMVUktNkxORGZJT1VGN1JoYkQ2Q1o2VUZEUlUtaEhOd004bzBGREFMWV9GMkppcUtIQXlfMERtYVhiTmVudHlWZ1p1bUQwZ0gzYzVDSnlSaU5pNVBsY3c?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu Bets Its Comeback on a $6,880 AI Phone Only a CEO Could Love &nbsp;&nbsp; Technology Org
- **[Vertu wants CEOs to run companies from an AI foldable starting at $6,880 - TechCrunch](https://news.google.com/rss/articles/CBMiqAFBVV95cUxPNzg5a3ZXNmdRZU1RUWxpQzc4bWFhNWhLWWhITHhmNHFWUEhuR2pnN081Smh2NzNueWFjVjRTeUZuSjg1LTV3WTlJQ0h6bi0tdkNnay1lYl9NVFNMU09TUTNMZkk3aXRjQTlTWW5UdGJfckh2RF9oTDNrSUNub2tXcW5YRVFoc3JtRlY3NkJJMnZoN1RZVGplNU9FaFE2a3hLX2FfRmo5RGY?oc=5&hl=en-US&gl=US&ceid=US:en)**: Vertu wants CEOs to run companies from an AI foldable starting at $6,880 &nbsp;&nbsp; TechCrunch

---

## 🏢 Industry & Real-World Applications

- **[Pfizer and Innovent Biologics Enter Global Strategic Collaboration to Accelerate Development of Innovative Oncology Medicines - Business Wire](https://news.google.com/rss/articles/CBMijwJBVV95cUxOcUlhQWoxMkdtV0RyYXRoTUNhVGIyLVBlYi1hMnhFaE9CSUZDaTMtWE1XMFlJNE0zNGI1NFdCMVc5Y2cwUk5RZThVNVFncFRXWHVpYTlsak9qZlhHMVVqVWpLQjIyZHJHU19TUDdWdXltdllWQWFKYjZOeUptOGRidjZlOFVlSVNMVEpWU0k2NGE3VXRpNm9OR1cwdkpOSXBiRmF4MUh3bTR3aE5heENmVm1nbVF0X2NEYzlkM3FXLUItZEpXcmJkWG5KWDh3UW9nVXJHdnhUek4wNTZTUHJJcUVDVDZhWkhxX1N2aDdaOFdJN2FwQXJYb2Nha1NkOEZub3ExQlJaZEhFWUptVG9J?oc=5&hl=en-US&gl=US&ceid=US:en)**: Pfizer and Innovent Biologics Enter Global Strategic Collaboration to Accelerate Development of Innovative Oncology Medicines &nbsp;&nbsp; Business Wire
- **[J&J Mastered Cancer Biotech Deals on the Cheap. Can It Stay on the Cutting Edge? - WSJ](https://news.google.com/rss/articles/CBMivgFBVV95cUxNWUJJSUxvcHNPU0xkaXpIYkxFNXVoUTJYbWxUVXRwNVFrZ3lBbmxWS0NCSk5WRGFNZ1FzWVE2a05aa3dEY0NxZUxjZzU1RDFMUE9TWFpxd21LY3hPUnoycFdkV3pITHh6cVFoWktXbmktSEp5MzV1SnFVZ3JSbHNzNk41bzUyYk5NaHI3d2U1Qmhfdks2dFd6SU0yUi1ZbDJNQkN6ME5Ta3ltSXBhWFFyWG5IN3JPQmxTVnNHcmpR?oc=5&hl=en-US&gl=US&ceid=US:en)**: J&J Mastered Cancer Biotech Deals on the Cheap. Can It Stay on the Cutting Edge? &nbsp;&nbsp; WSJ
- **[Lilly Continues Biotech Acquisition Spree - DCAT Value Chain Insights](https://news.google.com/rss/articles/CBMigAFBVV95cUxPcFhZUU9LTWtNWGFHdF9wSnkzZkxaRFFaQ2dtYTZKU0JWekg4NG1DQnBFZ1p4T3FoOHNKLVFkM0xoYXhITkwwN0VMcG1NQ3hZVEJWckt4Z1ozekhDem04Rl9PQ3lTUFpYWHdJaFdEODNrQ2dKV0RPSXJLNkFaNjVGMg?oc=5&hl=en-US&gl=US&ceid=US:en)**: Lilly Continues Biotech Acquisition Spree &nbsp;&nbsp; DCAT Value Chain Insights
- **[​JuanHand, PalawanPay forge partnership at FinTech Festival - The Manila Times](https://news.google.com/rss/articles/CBMivgFBVV95cUxPVmpiNkp2TnJ3bHN3dzk4NDNCZklpOVMwUlFFWjRkQlZ6S25ncU8talBCZU9fSjhSaTZXVmFva2dkQVJtS2dMZlJtYnJEcEVlcUw3bHhGN1Exckkyemt2NTBMVmFmX1FrVEdYOERGWFhlZWhGSlpzVmdfbWtaOHpYbjIxWXVnNmM5NEdGWmNOZXRpVWFDZnk2dy1VdVdpR1VsNHJpMVBhcUxQMGFoWmxhMURlVW9qQUZKZThEX1VR0gG-AUFVX3lxTE9WamI2SnZOcndsc3d3OTg0M0JmSWk5UzBSUUVaNGRCVnpLbmdxTy1qUEJlT19KOFJpNldWYW9rZ2RBUm1LZ0xmUm1ickRwRWVxTDdseEY3UTFySTJ6a3Y1MExWYWZfUWtUR1g4REZYWGVlaEZKWnNWZ19ta1o4elhuMjFZdWc2Yzk0R0ZaY05ldGlVYUNmeTZ3LVV1V2lHVWw0cmkxUGFxTFAwYWhabGExRGVVb2pBRkplOERfVVE?oc=5&hl=en-US&gl=US&ceid=US:en)**: ​JuanHand, PalawanPay forge partnership at FinTech Festival &nbsp;&nbsp; The Manila Times
- **[HanchorBio to List on Taiwan Innovation Board at NT$120 per Share as HCB101 Clinical Data Support Global Partnering Discussions - Yahoo Finance Australia](https://news.google.com/rss/articles/CBMikgFBVV95cUxPRU5lVTRUOUNGLTRHMzlBM25BMmJKdHVTd1lLYVdrV1pEeldtaVpyOFVBNFhoWFh4bkhlQkhUaENVc1M5QnRGTUxOVnBpbmhGYk5XeXI3OUVLc09OSFFjaXJjTXVvQ2J3Q2xZNFVSOFkwSFQwU20xajlwcTRNV0R2SGoxZmg5aHJDRWNTTjJCOEpDUQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: HanchorBio to List on Taiwan Innovation Board at NT$120 per Share as HCB101 Clinical Data Support Global Partnering Discussions &nbsp;&nbsp; Yahoo Finance Australia
- **[XL‑protein Launches Spin-Off PASylANTA Therapeutics to Develop Long‑Acting IL‑1Ra Biobetters - markets.businessinsider.com](https://news.google.com/rss/articles/CBMi5gFBVV95cUxOTFhTcXh5QzFVUEwzM181SmNPNXVMTmtQS2tLS3pISzlNZWlfdXhNZjhJalkwTUFzRkxabGc2aWVmamFmZHg1QXJCMm9MUHNlZ1hmY0JRS3ZxdjMwYVZlc1g0NjRLcTlmbmJ6Sm4tN1FyVDAtYTlXRXZGeS05Q0lLbUU4cmdpakg2U1NqaHlnLTcxS1c2OUdtSXVoRVYtSmR5dXIyYUxlV1NIQ1ZabW1rSGQ0dkpkS21CRzZaUmthQUhRYlZBTjFzVUR1MVRUTTJneXU3bEZBSFNIN0dNZ1BaT01xakd1QQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: XL‑protein Launches Spin-Off PASylANTA Therapeutics to Develop Long‑Acting IL‑1Ra Biobetters &nbsp;&nbsp; markets.businessinsider.com
- **[Galux, AimedBio partner to develop BBB-crossing protein delivery platform - koreabiomed.com](https://news.google.com/rss/articles/CBMibkFVX3lxTE94NXY0bE41c3JvWEdvMkF2dF9QOGI0c3FEckxmVUE0bDh3YzZzenVLTzVJUWdSVFZQRmpHNTZGQ0J1aVI2YTZHMkp3aHpBYWhPbmRTdHhXNVRUVVN3WW1RbVp2ZVMwYnVOV0FlLUln0gFyQVVfeXFMT0hqOEZJNldfdVJiVUd5OGNBR2Rxa2lhMkVvdUVYd3lGTHdRaFdGNU1VcEcwTlNkXzBWWVFYaTRycEJuVGE4cWhRZTl4TFVvejNGVEFzelRlVGxTYnVIOUtrUEswaDBXUjNIRUhUbTNPMnB3?oc=5&hl=en-US&gl=US&ceid=US:en)**: Galux, AimedBio partner to develop BBB-crossing protein delivery platform &nbsp;&nbsp; koreabiomed.com

---

## 💼 Jobs & Opportunities

- **[Jack Link's Protein Snacks Plant Engineering Manager - SmartRecruiters (SmartRecruiters)](https://news.google.com/rss/articles/CBMingFBVV95cUxNa1FObERNalhnTDNEQll3c3dLWTJPWVRiV2hScXZmd1VXYzF6SDdtY3VfcFhLenM5aGNTWEU1Yk1QWlJMMWpfbHRPSGF2TFpuTDh5WXlUb2Q5c21oXzFkbTR0RU9jeXJEMWE4cDZmUlZBQ1p3N182MlZrQk11V0E4LWRSMWFoQTI1bl9pcDlWT20tYnFwMFdNMG5zcEZndw?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Jack Link's Protein Snacks Experiential Marketing Associate - SmartRecruiters (SmartRecruiters)](https://news.google.com/rss/articles/CBMipwFBVV95cUxQN0d0bmVCZm80ejZxeC1oRFd2SjBqdzZqOFVueXItMzdHcDVrV0dPcEFJRDhsNXhVa3dKTGNET2dUT0ItYU82Y0o4UUdMQkpfZlREX0hwME5WY3ppVzBCb1QyVEZudW1faWFvSFRxXzFzbFhJVDN6d1RNTFJiMElMN01JOFZXVzlaYnM5RmZCWTlvdDlFdUZpSk84MFVKNk8wcW9pNXJ2SQ?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**
- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
