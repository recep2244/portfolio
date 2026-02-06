---
title: "Weekly Digest: Feb 02 - Feb 06, 2026"
date: 2026-02-06
description: "A curated summary of the top protein engineering and structure prediction signals from Feb 02 - Feb 06, 2026."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Feb 02 - Feb 06, 2026**

Missed a day? Here are the top research signals and tools from Monday to Friday, summarized in one place.

---

## 🏆 Top Signals of the Week

## 🗓️ Friday, Feb 06

### [DynaBench: Dynamic data for the docking benchmark.](https://doi.org/10.1016/j.jmb.2026.169650)
#### 🧬 Abstract
Protein-protein interactions are central to numerous cellular processes, including transport, signaling, and immune response. Structural modeling of protein assemblies typically relies on AlphaFold or docking methods, which produce structural models evaluated against a single experimental reference. While AlphaFold2 and its extension, AlphaFold-Multimer, have advanced complex prediction, they, and conventional docking tools, offer only static representations. However, flexibility at protein-protein interfaces is increasingly recognized as critical for function. To address this limitation, DynaBench provides a benchmark of interface dynamics in biologically relevant protein assemblies. We performed MD simulations for over 200 protein-protein complexes listed in the Docking Benchmark 5.5 ( https://zlab.umassmed.edu/benchmark/), generating three 100 ns long replicas per complex. All trajectories are now publicly available online ( http://www-lbt.ibpc.fr/DynaBench) via the MDposit platform (INRIA node), which is part of the EU-funded Molecular Dynamics Data Bank (MDDB). These simulations offer a unique resource for exploring interfacial flexibility, training machine learning models, redefining accuracy metrics for model evaluation, and informing the design of protein interfaces.

> **Why it matters:** Expands the searchable sequence space for novel folds and high-affinity binders.

---

## 📚 All Papers & Quick Reads

### 🗓️ Friday, Feb 06

- **[Enhancing CYP450-Ligand Binding Predictions: A Comparative Analysis of Ligand-Based and Hybrid Machine Learning Models.](https://doi.org/10.1021/acs.jcim.5c01098)**: Predicting cytochrome P450 (CYP450) ligand binding is critical in early-stage drug discovery as CYP450-mediated metabolism profoundly influences drug efficacy, safety, and adverse reaction risks. However, experimental determination of CYP450-ligand...
- **[Highly accurate protein structure prediction-based virtual docking pipeline accelerating the identification of anti-schistosomal compounds.](https://doi.org/10.1371/journal.ppat.1013274)**: Schistosomiasis is a major neglected tropical disease that lacks an effective vaccine and faces increasing challenges from praziquantel resistance, underscoring the urgent need for novel therapeutics. Target-based drug discovery (TBDD) is a powerful...
- **[Benchmarking co-folding methods to predict the structures of covalent protein-ligand complexes.](https://doi.org/10.1038/s41401-025-01721-5)**: Targeted covalent inhibitors (TCIs) are emerging as a new modality in drug discovery because of their strong binding affinity and prolonged target engagement. However, the rational design of TCIs remains a significant challenge and is hindered by the lack...
- **[Protein Structural Model Selection Informed by Comparison of Predicted Ligand Binding Poses.](https://doi.org/10.1021/acs.jcim.5c01925)**: Recent advances in protein structure prediction have highlighted the importance of a longstanding problem: given multiple structural models of a protein, how does one select the best model to use when predicting interactions between that protein and...
- **[Evaluating zero-shot prediction of monomeric protein design success by AlphaFold, ESMFold, and ProteinMPNN.](https://doi.org/10.1002/pro.70453)**: De novo protein design has enabled the creation of proteins with diverse functionalities that are not found in nature. Despite recent advances, experimental success rates remain inconsistent and context-dependent, posing a bottleneck for broader...
- **[Comprehensive Molecular Docking and Molecular Dynamics Reveal Inhibitors of HER2 L755S, T798I, and T798M based on a Large Database of Curcumin Derivatives.](https://doi.org/10.31557/apjcp.2026.27.1.265)**: Objective This study presents a methodology employing virtual screening to identify curcumin derivatives with selective affinity for the HER2 mutations L755S, T798I, and T798M. Methods Curcumin derivatives were retrieved from the ChEMBL database and...
- **[Boosting AlphaFold protein tertiary structure prediction through MSA engineering and extensive model sampling and ranking in CASP16.](https://doi.org/10.1038/s42003-025-08960-6)**: AlphaFold2 and AlphaFold3 have revolutionized protein structure prediction by enabling high-accuracy structure predictions for most single-chain proteins. However, obtaining high-quality predictions for difficult targets with shallow or noisy multiple...
- **[Innovative Approaches in Molecular Docking for the Discovery of Novel Inhibitors Against Alzheimer's Disease.](https://doi.org/10.2174/0115672050386924250930184405)**: Introduction Alzheimer's disease (AD) is a debilitating neurodegenerative condition marked by progressive cognitive decline and memory impairment, affecting millions worldwide. Despite extensive research, no definitive cure exists, underscoring the need...

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [ProteinSolver](https://github.com/manulera/ProteinSolver) - Graph-based neural network for protein sequence design.
- 🛠 **Tool**: [RFdiffusion](https://github.com/RosettaCommons/RFdiffusion) - State-of-the-art generative model for de novo protein design.
- 💾 **Dataset**: [SCOPe](https://scop.berkeley.edu/) - Curated structural classification of proteins for fold analysis.
- 💾 **Dataset**: [Pfam](https://pfam.xfam.org/) - Protein families database with curated multiple sequence alignments.

---

## 🤖 AI in Research Recap

- **[AlphaGenome Decodes 98% Genome, Identifies Disease Causes - 조선일보](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQb3FSSGlpZjlJNHotY2JFUDB2NVhObEYzSFI2Z3BETTNvTUxPY0xvcFVVV3ZNSlBVRldreFg2RmpEN2FFX3lfd2ZmTFpJRGZ1NmdST2tuazNmdjJNYVdRT1VOald5MmtmaFBMdUJVeVBUMnRiYWVTc0M0Qjh0aUdtWjJUUHE4WHAw?oc=5&hl=en-US&gl=US&ceid=US:en)**: AlphaGenome Decodes 98% Genome, Identifies Disease Causes &nbsp;&nbsp; 조선일보
- **[Transcriptomic profiling of chlorogenic acid and taurine treatment in human skin cells provides insights into cellular senescence mechanisms - Frontiers](https://news.google.com/rss/articles/CBMioAFBVV95cUxNOFd1ZGNwZ1JrOWR4QTN0MHR4NUxPcFpieFNjVWdQOUVhdG15ZUNPTWF4VF9Rc2NGTE9QX3YyZkJJVGMtS0xPYkFfQXVfTlBGQmp2ZjN3V3o4SzMtRmgtNnZFRWsyMFBQdVk1M1FLV1JoRklnbjlGMGZpYmRfc2pFdWwzLVJFc0JKTVlVVEh5OXlkNzBWcGk0UDJmYndSWUNP?oc=5&hl=en-US&gl=US&ceid=US:en)**: Transcriptomic profiling of chlorogenic acid and taurine treatment in human skin cells provides insights into cellular senescence mechanisms &nbsp;&nbsp; Frontiers
- **[Mental knots—studies offer insights into a protein's role in schizophrenia - MSN](https://news.google.com/rss/articles/CBMi1wJBVV95cUxQd3BINTNaMkxEaUJqN3R4ajYyWk92NGxuc1VuUjJNbTZsZy1UUVg4SE9nZzA5eVVFXzMya0pDbXhyaGdsdHJKbWF4Q2ZhYmFwTVhLZzFUU2J0WGZYTVNnMk5pWWVLeDdDUW1HcnRkempLSDYtdmhHRy0ycVB2a1Q4Nl9adXFoZGtJX3p4MUVFdlJjYWxpaW5tVlVSb0otRkdRSy1OVVB2dTZyQTlQSkgyYkRwenhJS2JLaTNuQkdHLUJQTzdUTUI1TnRWMk9uTHkyQTFXd3QwaWpmLVNETDBhZ3pKMXkxZU1uTmVYeXFiVlp2OGJLLWJsZEVqQTRhSFlsZlpHZWJXSkhTRDNTbzVKaGd1NHduM2JrRjJUTVotZ1Q1QkJ0OFdlYko5SVJVdmVqMTdWQ0ZkcVRlbDh5aUtndDNxekVKRmRXdDF6T1I3ajhKRlBLdlk0?oc=5&hl=en-US&gl=US&ceid=US:en)**: Mental knots—studies offer insights into a protein's role in schizophrenia &nbsp;&nbsp; MSN
- **[AlphaGenome Deciphers Non-Coding DNA for Gene Regulation - IEEE Spectrum](https://news.google.com/rss/articles/CBMie0FVX3lxTE1KNkNXcGhDbTM2YUhJOHZsd0c3cUk3X1YzdFJUY05EVlpxLW1vUnBrWlYwdWNDb0xTX1ZlN2ROWHRXVDRlaWF1WDJPbWJEOVlmTHRvdV9INVEwbWVuVEFQRkNnRFRtQnFaeEFnbHMzbU03WndCeGxMLUlVSdIBe0FVX3lxTE1KNkNXcGhDbTM2YUhJOHZsd0c3cUk3X1YzdFJUY05EVlpxLW1vUnBrWlYwdWNDb0xTX1ZlN2ROWHRXVDRlaWF1WDJPbWJEOVlmTHRvdV9INVEwbWVuVEFQRkNnRFRtQnFaeEFnbHMzbU03WndCeGxMLUlVSQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: AlphaGenome Deciphers Non-Coding DNA for Gene Regulation &nbsp;&nbsp; IEEE Spectrum
- **[A UVA Health team enlists bacteria to build better, faster virus-fighting vaccines - C-VILLE Weekly](https://news.google.com/rss/articles/CBMipAFBVV95cUxOZXlrNTJoeDdNakNHSWZrekFDQkxQTDh4ZnZETmVkRUpXNF8ycklVaDMwSDNoT3hYM0g3M2pPQzZuUU9SdW92Nk5yVE93X3JOeHcydnBIa1FoM3U3R1VFTUZUXzFSNkEzNFRpMWg2eTYzZS12RXIzNTVFZkg0SVJLUm5ib3lPYXpZWHE2MHJWbzY5NUJnSjIybm9DaHdPRENfandVRQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: A UVA Health team enlists bacteria to build better, faster virus-fighting vaccines &nbsp;&nbsp; C-VILLE Weekly
- **[February is Heart Month: What does new data mean for you, your health - Newport Daily News](https://news.google.com/rss/articles/CBMi1gFBVV95cUxNWEtJV3ZMb2dfVUgyRGNBYTl2cVRiQk1HOU9QelhkbDgxMlBqWGZpMFJDUnQxYXVGRXlwZEJ1WEhpWkR5a3IycTBLRldlMjN2NHBZVGY1LV93X2t4ZTJJamMxSmFRRUdLSjRqZ1dVRHpFazVsdTU4dFQ4ZS1SYTI5Vk9UYm9JUVNpZWVrR01NNEdVS3pOU21MakhqSGJGRnhyc04zSkNfZzlhUjBPaDcxUUxYOGdaRlRrcF9LQjZVRFlvQjZwRFFEbWt4aUt5MDF4b3dUZlln?oc=5&hl=en-US&gl=US&ceid=US:en)**: February is Heart Month: What does new data mean for you, your health &nbsp;&nbsp; Newport Daily News
- **[HepS protein in Salmonella - dr Grzegorz Grabe published in ‘Nature’ - | Uniwersytet Gdański](https://news.google.com/rss/articles/CBMikwFBVV95cUxOTEI4MnB0ZkxEcVJNVnlkTFNmREZjeS1OVXdycTliTDM1WWJ2TmpyWXN4UkItdk50bi1jcTJpS1l2RFBqU2NYbzlyRU5jX0dHc3FnSTdXYXVUYm9RTnNXeVFYYnA5aGMtdDI3LXZMM3BpaXV5SnAyS1hSWTljeUlDaHBHdWszTnVlRjl4OGFJbGh1cEE?oc=5&hl=en-US&gl=US&ceid=US:en)**: HepS protein in Salmonella - dr Grzegorz Grabe published in ‘Nature’ &nbsp;&nbsp; | Uniwersytet Gdański

---

## 🏢 Industry & Real-World Applications

- **[Eisai strikes Japan licensing deal with Shanghai Henlius Biotech - whbl.com](https://news.google.com/rss/articles/CBMimAFBVV95cUxOVUM4cXVDcl9rQmFkeUtGbTdHRFNxY0RDaXJKNG5YeU0xQWRFdWRfdnNaTWFQZkJ6RnVjM1daT3hiSUEwZC1SLTNlNGs0X3Q1UEhXbzNJU2Fid1dXdExnS2liQnVUUVNudHdaRVZvMGxBcWlqRWI4TVdNRDE3QTM3b2t3WUstc3htV0F1X01oRmRrZHZ6OENkVg?oc=5&hl=en-US&gl=US&ceid=US:en)**: Eisai strikes Japan licensing deal with Shanghai Henlius Biotech &nbsp;&nbsp; whbl.com
- **[Indian Gov’t To Invest $1.1 Bn To Support Biologics & Biosimilars Hub - DCAT Value Chain Insights](https://news.google.com/rss/articles/CBMirAFBVV95cUxNS1pWX1JWZGhIYmtEclVhYXIzR3VPVDhrNTl4UTRlbDJEbjBFcTY2WmZWWk1nWkVJcXlieGVkRUhkTUxCZVVlTWYzVk1CekZLMEItRGtfUjRmdF9MdXhGWFJtekxCZFBBWVF3c1pZcmtYMlhIcDg5VnNFd192M0gxX0Q2Q2pmb3lPNFppUndMYjVJYmk4VjcwemttbE9fN0Z0eThseWYzdGJKMm1Y?oc=5&hl=en-US&gl=US&ceid=US:en)**: Indian Gov’t To Invest $1.1 Bn To Support Biologics & Biosimilars Hub &nbsp;&nbsp; DCAT Value Chain Insights
- **[A cut above: Veradermics locks in $256M IPO and shares spike - Fierce Pharma](https://news.google.com/rss/articles/CBMirgFBVV95cUxOejdxLVlRdURidk9OZlo4Ui13WUJWeGpwY3pzLU9CVzBtS0xkT1QteFNONDVZUTVmY1VRNFplbGlieUJ1RDhBMG5Fa3ZscWR6c09aSTZvbXdudHY5bHUxMFFPNWZwUkN5X3JYMXlGUUtMNEZPRENSdE93VnpVbHp2Z1E3UzV0WW1aTW1WU3lPaGlWN2hJemV5VU9kTW5fXzRqYll5enJ2clZBdWs4dVE?oc=5&hl=en-US&gl=US&ceid=US:en)**: A cut above: Veradermics locks in $256M IPO and shares spike &nbsp;&nbsp; Fierce Pharma
- **[Eisai strikes Japan licensing deal with Shanghai Henlius Biotech - Reuters](https://news.google.com/rss/articles/CBMi0gFBVV95cUxNTjMxVFhfOU56V1pzOFFxWWd2eWIzMTNTS1BUd1A3NFJjVGpqR0dFX2JEdTJpX1BwcnNicXdlLWVPM1BRbmVRcU5TSzN5Uy1QNDRqbUw0QXRGXzIyMU9qSmFjNU5CNzB4ZzNhRHdFb3RkS2RmRDlpanM3VzFsUDRQeW52NVJwWlVQcWhELXV1OV9hdjNsX1VqbVEydmNwVjJ5N0w4MTNpNS1pUlZvNVpEU0V5blZsbkZraFFpWVpYQURXZHFXNnZ4dGU3QVZuS2dqRWc?oc=5&hl=en-US&gl=US&ceid=US:en)**: Eisai strikes Japan licensing deal with Shanghai Henlius Biotech &nbsp;&nbsp; Reuters
- **[From Biologics to Bio-Machines: Top Takeaways From Maui Derm 2026 - American Journal of Managed Care](https://news.google.com/rss/articles/CBMilAFBVV95cUxOZ1ctS0ZBZmdMbmpHZVVBWWhVOFFxbXBsRENGODh6TGduTnBjdm05aGxxUm5TOTZQVFVIeHNzLTd1Y1VFdzJuSHlQR0pJbWg5RVFWQTVDYS04MzkxZ2lMVzFSaFdFYVNMMU9FZ3FyZDk1X2VrOUVxRzNJME1FV19Sa0pnZ2czUW8tV1B0MDhNSGg0Wm9z?oc=5&hl=en-US&gl=US&ceid=US:en)**: From Biologics to Bio-Machines: Top Takeaways From Maui Derm 2026 &nbsp;&nbsp; American Journal of Managed Care
- **[Trial tests VCN-01 before eye removal in hard-to-treat retinoblastoma - stocktitan.net](https://news.google.com/rss/articles/CBMivAFBVV95cUxQcHhtOXVNSkJQR2pId2liYkY1Z3ZEU0tNVjlIWE9PQ2NZMktLQkpZZW1MUkRySE5ITVlxbGpmVmhMZVBxZ2p3Um8wYjV2YVY5UnBxRXdoZU4yZV9BM2xMemZXOVhOQ0NCa2YweS1OMlI4cGFUSFpTR2JJVWxnQ0JFMXhaNVhQeEs0OV9Ga1AxVDdjbVhNcjRrbmhSTUVubTNaTElJcl92WVI0NmJGTjJLUmxLRWpydkNlQzlLSw?oc=5&hl=en-US&gl=US&ceid=US:en)**: Trial tests VCN-01 before eye removal in hard-to-treat retinoblastoma &nbsp;&nbsp; stocktitan.net
- **[Zonsen PepLib Biotech Enters Global R&D Collaboration and License Agreement with Lilly - Business Wire](https://news.google.com/rss/articles/CBMi2gFBVV95cUxPcFNYNmE1RDhITHlwZy0yREl2WmdWalZmcFc4Z2syY2Zja3VncUxkRTYwRzlwOWN1M0xwUkFsX2VrUlIxV3R6dDRZSmJJdHkxamxfVDdRUlpWMWhEMFJONlJLOUF3NlRNMm02NjE2SjNXQXRJZDFQcEwyNWJ6R05ZSVBhQ2pwcjZ1cEJ1RFZFZG5NY0p4UXowRzZWMVc1ZW81Q0Jhc2ZPaGZLMzB3LUZCOXo2bjJzbUVXZnZhRFVMNmxSQmJ2Yi10Tkx0b2NsMzVDVWFna1dHZzR1UQ?oc=5&hl=en-US&gl=US&ceid=US:en)**: Zonsen PepLib Biotech Enters Global R&D Collaboration and License Agreement with Lilly &nbsp;&nbsp; Business Wire

---

## 💼 Jobs & Opportunities

- **[Allegiant - Data Scientist I - Lever (Lever)](https://news.google.com/rss/articles/CBMie0FVX3lxTE11SXJ5Vk4zS2owLUN5Rm1uWDJ4cjZNMTJpT2VITk1iT04zVDItN1liQUswYmVlUzRxOFY5ajRGNVVlU2NqcmRvYTJTQ1NPOU95N0FfQ256ZnRNRVVOLTVNSlY2YkN1enA4UmQtX0xod01RSXFVUV9PS0xGTQ?oc=5&hl=en-US&gl=US&ceid=US:en)**
- **[Brighte - Expression of Interest - Lever (Lever)](https://news.google.com/rss/articles/CBMidEFVX3lxTFBvS2lBUjZ0MTZuYUtCMVlqR1dPNGtudldvMmVkRkJWUUxONUJjTjNvN2dBWHJ4VVE1amR0U0JRb1o4V2YzblVObGhpWGxITkx5cS1jWUFQZ2ZONmxsOWt2OFVGN09OQWJaS2dVVU8zdTVMc0hp?oc=5&hl=en-US&gl=US&ceid=US:en)**

---

## 📅 Events

- **[Structural Biology Events](https://www.nature.com/natureconferences/index.html)**
- **[Protein Design Hub (LinkedIn Group)](https://www.linkedin.com/groups/16324018/)**

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
