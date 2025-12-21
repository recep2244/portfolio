---
title: "Weekly Digest: Dec 14 - Dec 21, 2025"
date: 2025-12-21
description: "A curated summary of the top protein engineering and structure prediction signals from Dec 14 - Dec 21, 2025."
author: "Protein Design Digest"
tags: ["weekly", "digest", "protein-design"]
---

{{< newsletter >}}

# 🧬 Weekly Recap
**Dec 14 - Dec 21, 2025**

Missed a day? Here are the top research signals and tools from the past week, summarized for your Sunday reading.

---

## 🏆 Top Signals of the Week

## 🗓️ Sunday, Dec 21

### [Meeko: Molecule Parametrization and Software Interoperability for Docking and Beyond.](https://doi.org/10.1021/acs.jcim.5c02271)
#### 🧬 Abstract
Molecule parametrization is an essential requirement to guarantee the accuracy of docking calculations. Parametrization includes a proper perception of chemical properties such as bonds, formal charges and protonation states. This includes large biological macromolecules, such as proteins and nucleic acids, and small molecules, such as ligands and cofactors. The structures of proteins and nucleic acids are challenging due to omission of several atoms from the structural model, and from the lack of connectivity and bond order information in the PDB and mmCIF file formats. For small molecules, the very large chemical diversity poses challenges for both validating correctness and providing accurate parameters. These challenges affect various modeling approaches like molecular docking and molecular dynamics. Moreover, several specialized methods (particularly in molecular docking) leverage specific chemical properties to add custom potentials, pseudoatoms, or manipulate atomic connectivity. To address these challenges, we developed Meeko, a molecular parametrization Python package that leverages the widely used RDKit cheminformatics library for a chemically accurate description of the molecular representation. Small molecules are modeled as single RDKit molecules, and biological macromolecules as multiple RDKit molecules, one for each residue. Meeko is highly customizable and designed to be easily scriptable for high-throughput processing, replacing MGLTools for receptor and ligand preparation.

> **Why it matters:** Expands the searchable sequence space for novel folds and high-affinity binders.

---

## ⚡ Selected Quick Reads

- **[From sweetener to risk factor: Network toxicology, molecular docking and molecular dynamics reveal the mechanism of aspartame in promoting coronary heart disease.](https://doi.org/10.1016/j.cbi.2025.111876)**: Aspartame, a widely used non-nutritive sweetener, has been epidemiologically linked to coronary heart disease (CHD), although the underlying mechanisms remain unclear. This study employed an integrative computational strategy combining network toxicology, molecular docking, and molecular dynamics to decode aspartame's CHD-promoting mechanisms. Initially, the toxicity profile of aspartame was predicted using ProTox 3.0 and ADMETlab 3.0, which highlighted significant cardiotoxicity. Through multi-source target screening of aspartame (PharmMapper, SEA, etc.) and CHD (GeneCards, OMIM), 216 shared targets were identified. Protein-protein interaction network analysis revealed 10 hub targets (INS, PPARGC1A, TNF, AKT1, IL6, MMP9, IGF1, PTGS2, SIRT1, PPARG). Gene Ontology (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway analyses revealed significant enrichment in lipid metabolism, inflammatory responses, insulin resistance, and atherosclerosis-related pathways. Molecular docking and molecular dynamics simulations (MDS) demonstrated high-affinity binding of aspartame to three core targets (PTGS2, TNF, and PPARGC1A), with a binding energy ≤ -7.0 kcal/mol, and confirmed high binding stability. This study reveals that aspartame may promote the pathogenesis of CHD by disrupting cardiovascular homeostasis through multi-target interactions, including inflammatory response, metabolic dysregulation, and vascular remodeling. These findings provide molecular evidence for re-evaluating the safety profile of aspartame and establish a computational framework to guide experimental validation and preventive strategies.

---

## 🛠️ Tools & Datasets

- 🛠 **Tool**: [ReFOLD4](https://www.reading.ac.uk/bioinf/ReFOLD/) - Sophisticated protein structure refinement tool for improving model quality.
- 💾 **Dataset**: [Uniprot Knowledgebase](https://www.uniprot.org/) - The world's most comprehensive resource for protein sequence and annotation.

---

## 🤖 AI in Research Recap

- **[AlphaFold and the architecture that cracked protein structure - Interesting Engineering](https://news.google.com/rss/articles/CBMiiAFBVV95cUxQb2tCcnN4TThaSHJUN3hJVklDRk1kTHZpWTNVU0twV2ZXMEQ5eGNEZ2ZCMVJHMFdfSGtMRDRraXdaSTlEUlBqY2J3TWNsYVpNV2ZEWDR2N0wzX0ZMb1V1NGlhdWxVdkNUX2lPVzJCajB0SUtpZG5qeV9HWFNkMjJJNm9BVnMtRGsz?oc=5)**: AlphaFold and the architecture that cracked protein structure &nbsp;&nbsp; Interesting Engineering
- **[AI pinpoints new drug target for treating monkeypox virus - BioTechniques](https://news.google.com/rss/articles/CBMitgFBVV95cUxOalByWk5udkdDZVBfUTFUSTVFNDlDWWFJSmRfdGRHRzYxTkZuRzNtRkhqUUN4ZFVheEVNRUs0aTVsZWZ2OFRnSFljSWhydkdWV1lobGdtX0l6b19DbWZveEtSWElIdGhOQ0xRemYyZDJrSTI4MW5QZ2luTUVhdllnS2JNLVprMzdoUE5tS2FpZ1pCSl9lekc0eXBpbTNkdzRUWURUM0x0bk40Um1tQTBHVnNfdmd2Zw?oc=5)**: AI pinpoints new drug target for treating monkeypox virus &nbsp;&nbsp; BioTechniques
- **[Key Insights: Computational Structural Biology Workshop - Mirage News](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNbVNHc2s0Z2JOWk9FOTZKSmZrQ3RYXzdJOHlUNWNzMHM1UFNvamdQc2tLZUdBeEQtMGV3bXBkYlVFVXpOdHc4bllHLUFGdzZhZG9TZEhJTjllbzJPcUZkRWxIR3c5Skp6Vi1ZZ1pPYlA0WmExY3BsVzZCQkk3cnJmTHVBZEhaV3dU?oc=5)**: Key Insights: Computational Structural Biology Workshop &nbsp;&nbsp; Mirage News

---

## 🏢 Industry & Real-World Applications

- **[Galux, Boehringer Ingelheim to Jointly Explore AI in Precision Protein Design - Contract Pharma](https://news.google.com/rss/articles/CBMivwFBVV95cUxOLTJXbVRmV1o5ZmszaExSN3l1TWY4VEREUHIwSzRKejFXRFY5STJzYnZEZzMtTEpsVjJYVGFkR25JekRPU0U1dkRzRFI4NG9NS2xQeDM2WFFsLXJiOWtBbjF5VjczMmdXYm1VdTg1YVZPd0dvWm5ZVUpJNWZWVHNTcWdoNWlOV2owbG9rVnhlbi1lMFRSM0xEa3dVMmUwZmpLVnBDcWVNc0UxR0xiRzc3UmNwRmF1NmpNNlhMR0R6UQ?oc=5)**: Galux, Boehringer Ingelheim to Jointly Explore AI in Precision Protein Design &nbsp;&nbsp; Contract Pharma
- **[Profluent Bio Partners with Ensoma for AI-Designed Base Editors in Stem Cell Therapies - SynBioBeta](https://news.google.com/rss/articles/CBMi7AFBVV95cUxOdU5Hd2x4R2lpVWJwelRYblNVeVNZUDFtSXZoaVc4bWMtRVRKNlRidnA5cjRLcmZBaWVrV3hhY3RpOVlzcFMwR2JSSG4xVnRfN3hlbWV0NkY2WEdWQVVuQWxTa3JPWmloTU5OTDhGYkJaeWpXR3JrU1JlZUhtdGNZb09id21EaEwwUzJ4UUoyanJFQnZNajhkMWFnTm40RUh1UDg0SXRld3FiMWs5OTJsb2hMb2twUHZGMU5BZzkwRnBHMWVrVEptbmI2bnM4MzJ6ZXB0NF80em43b25vNGpjamxRTDJEenFZLVppTQ?oc=5)**: Profluent Bio Partners with Ensoma for AI-Designed Base Editors in Stem Cell Therapies &nbsp;&nbsp; SynBioBeta
- **[Lindus Health, Quotient Sciences Partner to Accelerate Drug Development to Clinical Trials - Contract Pharma](https://news.google.com/rss/articles/CBMi0AFBVV95cUxNWUdWS3NHWXd4REFRX2ZOcjVPTDFfQUQxWmtsOVVrVFBleXVpbnBFSTRmZE5wY0ljQmVzRzdXRHJuX1I0SDF3QU0xZ19YQWlqbU9GX1lvTlZFTFBsVWVCOVcwek9ZRmxZTi01UUs3NHRKQkVNUU15cG1nc0hqM2hqMmc1XzBwTG1JcTFvNEszdzdnOW8xS0hFY0pBTThxamdLak1JQk0tMnI4YWJZSW9vQU5EbVhtZjNDZ1RuUHdNQzFIWDFmTTJ2V3BnMVJrMWpF?oc=5)**: Lindus Health, Quotient Sciences Partner to Accelerate Drug Development to Clinical Trials &nbsp;&nbsp; Contract Pharma

---

_Enjoyed this digest? Subscribe above to get these dailies in your inbox every morning._
