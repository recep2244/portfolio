---
title: "Weekly Digest: Apr 20 - Apr 24, 2026"
date: 2026-04-24
description: "A curated summary of the top protein engineering and structure prediction signals from Apr 20 - Apr 24, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Apr 20 - Apr 24, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Apr 24

### [Evaluation of protein-RNA Docking Web Servers for Template-Free Docking and Comparison with the AlphaFold Server.](https://doi.org/10.1021/acs.jctc.5c01990)
#### 🧬 Abstract
Protein-RNA docking is a valuable tool for predicting the structures of protein-RNA complexes, which allow us to understand the structural basis for gene expression and regulation, thus facilitating drug development. Despite the development of several protein-RNA docking programs, the field remains relatively underdeveloped compared to protein-protein docking, and a systematic comparison of these programs in terms of accuracy and efficiency is still lacking. Recent advances in deep learning-based structure prediction, such as AlphaFold 3, offer a promising alternative for modeling protein-RNA complexes. Here, we have compiled a consolidated benchmark data set of 235 protein-RNA complexes (freely available at https://github.com/tanys-group/protein-rna-docking-benchmark), which were curated from PDB structures deposited up to July 2024, to assess the performance of five template-free docking web servers and the AlphaFold Server. Among the docking web servers, HDOCK performed the best, achieving success rates of 31.1% and 44.7% within the top 1 and top 5 predictions, respectively, as assessed by CAPRI (Critical Assessment of PRedicted Interactions) metrics. Although AlphaFold 3 outperformed all the docking web servers with an overall success rate of 87.0% in its top 5 predictions, it failed in nine cases where docking approaches succeeded and showed a markedly lower success rate of 40% for protein-RNA complexes outside its training set, comparable to that of HDOCK (35%). Our study provides valuable insights into the strengths and limitations of current protein-RNA docking servers and AlphaFold 3, offering practical guidance for selecting the appropriate tool for protein-RNA complex structure prediction. These results also suggest that hybrid approaches combining physics-based and machine learning methods hold significant promise for achieving higher prediction accuracy.

> **Why it matters:** Critical for improving fold accuracy and reducing structural uncertainty in de novo design.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Apr 24

- **[Discovery of potent ALK tyrosine kinase inhibitors for thyroid cancer via machine learning modeling, molecular docking, MD simulations, and DFT study.](https://doi.org/10.1016/j.compbiolchem.2026.108960)**: The ever-increasing need for effective therapeutic management of thyroid cancer (TC) necessitates the exploration of novel approaches for advanced drug discovery. The current study employed a robust computational pipeline integrating Machine Learning (ML)...
- **[Integrative structural and physicochemical characterization of chalcone synthase enzymes from medicinal plants using AlphaFold, molecular docking, and molecular dynamics.](https://doi.org/10.1038/s41598-026-45190-0)**: Chalcone synthase (CHS) is the entry-point enzyme of the flavonoid biosynthetic pathway, catalyzing the first committed step toward the production of diverse bioactive metabolites with antioxidant, anti-inflammatory, and anticancer properties. Here, we...
- **[Enhancing CYP450-Ligand Binding Predictions: A Comparative Analysis of Ligand-Based and Hybrid Machine Learning Models.](https://doi.org/10.1021/acs.jcim.5c01098)**: Predicting cytochrome P450 (CYP450) ligand binding is critical in early-stage drug discovery as CYP450-mediated metabolism profoundly influences drug efficacy, safety, and adverse reaction risks. However, experimental determination of CYP450-ligand...
- **[NNDock2: A neural network-based scoring function for ranking protein-protein docking models.](https://doi.org/10.1142/s0219720026500058)**: Protein-protein interactions (PPIs) play crucial roles in diverse cellular functions and biological processes, and structural knowledge of the protein complexes is valuable for the elucidation of those functions and designing new drugs. Due to the...
- **[Investigation of the potential mechanism by which methylparaben induces psoriasis: an integrated study using network toxicology, molecular docking, molecular dynamics simulation, and eight machine learning algorithms.](https://doi.org/10.1093/toxres/tfag003)**: Psoriasis is a chronic inflammatory skin disease with limited safe and effective treatments. Methylparaben, a widely used preservative in cosmetics, pharmaceuticals, and food, is an emerging environmental pollutant linked to immune-related skin disorders,...
- **[Evaluating zero-shot prediction of monomeric protein design success by AlphaFold, ESMFold, and ProteinMPNN.](https://doi.org/10.1002/pro.70453)**: De novo protein design has enabled the creation of proteins with diverse functionalities that are not found in nature. Despite recent advances, experimental success rates remain inconsistent and context-dependent, posing a bottleneck for broader...
- **[Comprehensive Molecular Docking and Molecular Dynamics Reveal Inhibitors of HER2 L755S, T798I, and T798M based on a Large Database of Curcumin Derivatives.](https://doi.org/10.31557/apjcp.2026.27.1.265)**: Objective This study presents a methodology employing virtual screening to identify curcumin derivatives with selective affinity for the HER2 mutations L755S, T798I, and T798M. Methods Curcumin derivatives were retrieved from the ChEMBL database and...
- **[Exploring quantum frontiers in protein structure prediction: techniques, challenges, and opportunities.](https://doi.org/10.1016/j.ymeth.2026.04.006)**: Protein folding is governed by the principle of free energy minimization, where a protein's native tertiary structure corresponds to the global minimum on an energy landscape shaped by quantum mechanical interactions such as hydrogen bonding, van der Waals...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [Boltz-1](https://github.com/jwohlwend/boltz) - Open-source biomolecular structure prediction model.
- 🛠 **Tool**: [ProteinSolver](https://github.com/manulera/ProteinSolver) - Graph-based neural network for protein sequence design.
- 💾 **Dataset**: [BioLiP](https://zhanggroup.org/BioLiP/) - Verified biologically relevant ligand-protein interactions.
- 💾 **Dataset**: [SIFTS](https://www.ebi.ac.uk/pdbe/docs/sifts/) - Residue-level mapping between PDB, UniProt, and other resources.

---

## 🤖 AI in Research Recap

- **[OpenAI Launches GPT-Rosalind: A Specialized AI Model Aimed at Accelerating Drug Discovery - QUASA Connect](https://news.google.com/rss/articles/CBMisAFBVV95cUxQc3YyX3NkWjIxcjFMVDNNb3ZmTDIxYnpqQmhpNWZrZl9xeTVkNnZHNlRVRFBXSVlLYzQyY3ljTS0zNVFBVk1sVFZXakNVMXJpLU4yU0VkWm55YVBEWkFpTW9pdnUxQkpwOUZLWDE2QkRTMFVJUmxjaTJyUHJtUV9KQlM5WFhteWR1eEJsb0RRaTBmRWVGbUNCTDFHaE5JcS1lTFBMcEJHUm42S2dkUjhHUA?oc=5&hl=en-US&gl=US&ceid=US:en)**: OpenAI Launches GPT-Rosalind: A Specialized AI Model Aimed at Accelerating Drug Discovery &nbsp;&nbsp; QUASA Connect
- **[Demis Hassabis, co-founder and CEO of Google DeepMind, "AlphaGo's Father," will meet with President - 매일경제](https://news.google.com/rss/articles/CBMiU0FVX3lxTE1fUXlrcmFrTkc0R2FkSFJTajBuN25SNGtNblhLOTFNNjltY0s0YlNWeDYtdHhPZkZBZHhwa09EVTE5WU9sNU9kRG1PYkd0UWhHZXc0?oc=5&hl=en-US&gl=US&ceid=US:en)**: Demis Hassabis, co-founder and CEO of Google DeepMind, "AlphaGo's Father," will meet with President &nbsp;&nbsp; 매일경제
- **[Doug Kojetin to present at Molecular Biophysics Training Program/Center for Structural Biology Seminar Series, April 28 - VUMC News](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNb29CZ3ZZNllXazZQMWZleERTMWhHOGVRQzNkVGdUVXdNMXpiUkJxMVZtWUF2el9ILUhNM2IxUzRFc0VDS3E5UU9mOUZQMG1JQlhkMDhMaG8zaWdJR3Y3MkpzbURNZzVOWUlqT0k0Z3FjNTYtWkJoTTBYRlRyVnVralFUbm5kMUtRVVA5Y3l5U01aZWVzMUpvazd3NlpCS0tqenFiWWtpOGh5LTczbElqX0Rxbkw0SzVXMW00aFRTalJoN1VqamlOakEzd01MSW1CZmZrVEczRGhPQS1KSFUxUXpoTFZPWnc?oc=5&hl=en-US&gl=US&ceid=US:en)**: Doug Kojetin to present at Molecular Biophysics Training Program/Center for Structural Biology Seminar Series, April 28 &nbsp;&nbsp; VUMC News
- **[Structural insights into S1P receptor ligand binding: implications for targeted drug design - EurekAlert!](https://news.google.com/rss/articles/CBMiXEFVX3lxTFBHOWZUdkRVbjVFRHpwYVhVZUN6WndwZUtfLUUwcmlUS3hMdkVQWXU2MGZIalNnMTJ4SWpUQkFRclp5MTlkSHNzaUk1RUN4TnlVX1lsM0p3LVgyakFS?oc=5&hl=en-US&gl=US&ceid=US:en)**: Structural insights into S1P receptor ligand binding: implications for targeted drug design &nbsp;&nbsp; EurekAlert!
- **[Glacios 3 cryo-TEM boosts cryo-EM access - Select Science](https://news.google.com/rss/articles/CBMirAFBVV95cUxNbEMwMDh0VElvRzJhbXluX0xPY1RZTGRvZ0R4SlhoeVRNSTFvc3NYQjgzYUxhTWpldERGTkI3NDlFVS1BbjBKUnVZZlZ2eFdoZVJOQ1hYT3pkWjJvZjVabVdvTnpFYTEweV9EeDRadS1JVEh1ajl6dUhncVRCSVhRalRsbXZ4azRQR0dDRGYwbUZGdW5feFdqMENTNDhQVVhyRjRtMWgzVUNsbnAt?oc=5&hl=en-US&gl=US&ceid=US:en)**: Glacios 3 cryo-TEM boosts cryo-EM access &nbsp;&nbsp; Select Science

---

## 🏢 Industry & Real-World Applications

- **[Lessons Learned in the Current Biotech Funding Environment - Pharmaceutical Executive](https://news.google.com/rss/articles/CBMiigFBVV95cUxQVzVCWVZtVmNyOTdkeXowLWNSN1ZoMmdCaUVsaVM3UlptOEYwc1lZZFBkTkxpSmFEa1pjYW5UTGtEN29yel93SEotZ0VLcXpWY01zQkhfMGoxTnFPUFdJbUhva0o3b1F0ekNVT3l5bWxFNWxsclh3TkU3Mm5SQmMtMzgteUN4eGQyeVE?oc=5&hl=en-US&gl=US&ceid=US:en)**: Lessons Learned in the Current Biotech Funding Environment &nbsp;&nbsp; Pharmaceutical Executive
- **[AbbVie Provides Update on TrenibotulinumtoxinE Biologics License Application in the U.S. - Investing News Network](https://news.google.com/rss/articles/CBMitAFBVV95cUxNZG1hNzROQTE4aDJPaEVGU3dOTG16SUFXeEtiRUh1Qzl3bmJPQXRoSUg5blBHMWJLN3pjRHdwWW4xb0RNM0c3TnhidzgwbC11dzUyT2Ewb2x6T0VpMUVTeTNBZXdWR1JoX1FHZ0praXN3MDZIX1BsbHZmcWtjb2dDMUc2Qkd0NmV6WkF3SU5NQ1VNZTRlc2NrMXRMazNoQWU1bzRjeHVhQ1prZllSb2ZfdTJyeG4?oc=5&hl=en-US&gl=US&ceid=US:en)**: AbbVie Provides Update on TrenibotulinumtoxinE Biologics License Application in the U.S. &nbsp;&nbsp; Investing News Network
- **[FDA Accepts Supplemental Biologics Application for Gazyva® in Systemic Lupus Erythematosus - Lupus Foundation of America](https://news.google.com/rss/articles/CBMitwFBVV95cUxObkZ2MktBOV9qS1oySm5SX05RcGpxbTREcXNLMGpMMlFvd3JiUC1TaGtMeG5tUy12aWhBSl9ubTJzSmY5WTA0dEZfdUtBMGlnOFNrTTFwV01hT00tb2pwRUMtdkpySktmVWdvR1hjOXNObS1QT1Rhb3hBUFIzSkZVVDNKcFZtM1FCaWV6MU5GV1pES0cwUU04ZWVJaGRkc0dadnRVZUNDeEdvbDMtTzdmQTRhRGgyY2c?oc=5&hl=en-US&gl=US&ceid=US:en)**: FDA Accepts Supplemental Biologics Application for Gazyva® in Systemic Lupus Erythematosus &nbsp;&nbsp; Lupus Foundation of America
- **[Inhibrx Provides Clinical Update on Ozekibart (INBRX-109) in Late Line Colorectal Cancer - Newswise](https://news.google.com/rss/articles/CBMivAFBVV95cUxOcXh0VzhvMjh5a1h0X3lVU0J1cEdrQzgweDBETU5KZjRxdEJaZ0V5dHkzN2tuRWlJTVJiUkZkY3R3VGxQRGh1Rzh3MjBqc0FCaS00YWR3RmxlRlkwM1hGcHIybXdlWjRjTVhEQkFIdXZUNGxBbXhZVksyWmdaczZlWEIzeTQtTUJSLVNRaTA1YV9YOWY3ZDMxNjZaUjBtamNSN1pnMjg3WTRyU0VSS1BNUmRRWGk4cS1EUjNscQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Inhibrx Provides Clinical Update on Ozekibart (INBRX-109) in Late Line Colorectal Cancer &nbsp;&nbsp; Newswise
- **[Sana Biotechnology (SANA) Valuation Check After Mayo Clinic SC451 Collaboration And Recent Share Price Swing - simplywall.st](https://news.google.com/rss/articles/CBMi5wFBVV95cUxNTGNIZDZGOWUwZUtwZ2NGX21JY1NnSXVkYzdNbDBqT3pZSGhJWlIxdFV5cmFxZ0ZIZGV3MUx4UzExdWc4X2l1ZVpEajJNc19STEVuTFE3V1dWRlpTS1JUS2FUZmREUFBfdXdQbUhWQlozbnJwNTB2NFJZTUVXeDY1V290UXdkTTZjNE4wZGh0QTlJNGVvWjNGeEF6YnZnUUZOQWo3bHNmS05WLVVLbE5PajJveVRvbl9JUFdNZlFCQmE0cjZWT0J0NHhSbFN2VDBrNHQxQmhBQmJId3dySUZiYlRkbkNmWDTSAewBQVVfeXFMUDlIa0hfMFNxeEhTYTZTdUdsN3JLYng2SzFreUdYZUczTW83bmdibkpBNVV5VW1ZNTl0cDA0Y0I1Qk96R1hQc2o1dVByT2ktMUszbUk1cU9JVFd6NnUzN0JUZ1NDMU9fSnFXczR0S25CTk1LRF91aldHdVZrYnVuNWk5ZzNMbGNQbWpmTDBORVF3Wi1LdUNkRzVDV1JyMFhVX3YxSFl3ejVmUnRKVXc0Tk5iUnR0cC0taHBRZGtYNFM4aHEtWTZGdDhyMmdDVm1YQzdoMXFzYk9aTU5vSjFjS1k5RmNjMnhSVUVkd3Q?oc=5&hl=en-US&gl=US&ceid=US:en)**: Sana Biotechnology (SANA) Valuation Check After Mayo Clinic SC451 Collaboration And Recent Share Price Swing &nbsp;&nbsp; simplywall.st
- **[Fierce Biotech Fundraising Tracker '26: Tortugas' $106M beachhead; Ray shines with $125M - Fierce Biotech](https://news.google.com/rss/articles/CBMigAFBVV95cUxPWnNIYUVmZkJnUzFkM3dqNFpZaFZRRUdTUWNxb2lMeDY4NklMMGJobEM0NDU3LUQ2ZmRhYjNNaTlRM3N4MzZHOExoV3BGQXk1a1dKNDFHaHlrT0RZX3pYd0g0OVhlNnZobEtEdzBtLTh3ZnRsSWFpbGNjRVVpU1VIMA?oc=5&hl=en-US&gl=US&ceid=US:en)**: Fierce Biotech Fundraising Tracker '26: Tortugas' $106M beachhead; Ray shines with $125M &nbsp;&nbsp; Fierce Biotech
- **[AbbVie and BioLabs Team Up to Support Life Sciences Innovation in Canada - BioSpace](https://news.google.com/rss/articles/CBMisgFBVV95cUxPUnkxWGJqcldoaWZKS2tHcHJocFN4RG9CdFQ1VmNjcDJCTDlhSTNSc0oxRWRFTGpweEZTVThsSDlleUdKYXNQWHNtVGs1T2pBbVJ5bEQ2MU1GLXIxVnVGanJXekI5VUhuSkNjZHBJck1ac2F3VEsyN0I2ZHYtVUFWVHExOW1SZnBqWi1xTmJRajlZV1FoTVlfMEw1TkhrQjF0dFk2ZVNHcnZuX3JJc1RWT25B?oc=5&hl=en-US&gl=US&ceid=US:en)**: AbbVie and BioLabs Team Up to Support Life Sciences Innovation in Canada &nbsp;&nbsp; BioSpace

---

## 💼 Jobs & Opportunities

- **[CHEManager International hiring Assistant Scientist / Assistant Professor - Computational Biology in Detroit, MI - LinkedIn (Bioinformatics Careers)](https://news.google.com/rss/articles/CBMi0AFBVV95cUxOZ2dPZEpPS21mV0RnYUt1NF9NbnFvcTRyQXY5LWZGV2gzYkZYNUwxLW8yZ0UwTUprVE9XQXBoTkVaZlR0MVY5N0JJbmgxRmQzc21vX043RTZGVUhKdG5ZRy1SM1RERGNGeU5WMTVTa0otUXFWVmpUTDhZZUI2SHNPOWZSdTVINVFqUU9HZDhhY3pmSUlnSzlSS2Y0UUw2UHI5ZlFuM3JKNmc5NUs1SHZNVFZIcm5WaVJ5WGhEY1V6ZEpCR0hmWkJqWFVoWHpUSVVx?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Mercor hiring Senior Bioinformatics Scientist | Upto $95/hr Part-time in United Kingdom - LinkedIn (Bioinformatics Careers)](https://news.google.com/rss/articles/CBMirwFBVV95cUxPUHkwckdVZnc1VDVnMWtRa01xY3FLX3RCbWJpNWJwM2RSZXRQbEJub3Q0YWRrWk5PUmlneXFIUjYwLVJSd3lLSWlOeGxzR1JxdTYwUGszOUhEd3RjRGlvYW9LZEFVSDJzb2RZUFFuUy1pZFlBMlNVcnphekJQeFRFcnVDb3h2R2dGUmxWSkVyZkZRQXF4Q0tZMnFvVk9tMEwwRU5CYjhNa0VpLUVBNk9B?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**
- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
