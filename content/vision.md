---
title: "Research Vision"
summary: "Transforming protein structure prediction from static snapshots to dynamic ensembles for de novo design and drug discovery."
date: 2024-11-29
layout: "vision"
---

# Transforming Protein Structure Prediction: From Static to Dynamic

## The Challenge: Beyond Static Snapshots

The 3D structure of proteins governs their molecular functionality, determining high-resolution structural determination essential for structure-guided drug discovery, mechanistic insight into pathogenic genetic mutations, and the rational design of targeted therapeutics. Determining protein structures experimentally is challenging due to the high cost, time demands, and limitations of methods like X-ray crystallography, NMR, and cryo-EM, particularly for flexible, heterogeneous, and dynamic proteins such as membrane and intrinsically disordered proteins.

In silico modelling is crucial for protein structure prediction. Machine learning (ML) advancements, particularly deep learning, have enhanced these approaches by learning complex sequence-structure relationships. Methods like **AlphaFold2 (AF2)** and **AlphaFold3 (AF3)** have revolutionised the field with near-experimental accuracy.

However, these state-of-the-art methods still face critical limitations:
1.  **Struggle with Mutants & De Novo Proteins**: They rely on evolutionary history, making them less effective for novel variants where evolutionary depth is shallow.
2.  **Static Bias**: They typically generate static models, overlooking the conformational dynamics essential for function, binding, and allostery.

## My Vision: A Dynamic Modelling Framework

My vision is to transform protein structure prediction from static to dynamic, with a strong emphasis on **mutant variants** and **de novo designed proteins**.

> "I aim to create a versatile computational pipeline that captures structural dynamics, enhances functional insights, and supports drug discovery and protein engineering applications."

### The Next-Generation Protocol

My fellowship project addresses these gaps by developing a framework that integrates:
*   **Diverse ML-based predictors** for initial structure generation.
*   **MD-driven sampling strategies** to explore conformational space.
*   **Adaptive restraints** guided by **local quality estimation**.

This approach ensures that structurally stable regions remain constrained while allowing greater flexibility in low-confidence regions, binding sites, and areas affected by mutations.

{{< research_visuals >}}

## Strategic Focus & Methodology

### 1. Local Quality Estimation as a Driver
Focusing on local structural details has been central to my protocol development. By utilising per-residue confidence scores, I can differentiate between stable backbone regions and flexible loops. This allows for **targeted refinement**, preserving stability where needed while enabling biophysical motion in uncertain areas.

### 2. Modelling Mutants & Novel Folds
Current tools struggle with point mutations because the evolutionary signal remains largely unchanged. My protocol will systematically explore mutant and designed folds, capturing their structural variations and dynamic behaviours to better understand functional consequences and stability.

### 3. Bridging Academia and Industry
I bring a unique blend of experience:
*   **Academic Leadership**: Pioneering local quality estimation methods in the McGuffin group.
*   **Industry Impact**: At **InstaDeep**, I developed AI-driven pipelines for TCR-pMHC modelling, contributing to personalized cancer vaccine design.
*   **Global Response**: Applied ReFOLD3 to provide mechanistic insights into SARS-CoV-2 proteins during the pandemic.

## Impact: Accelerating Discovery

The ability to predict rare conformational states and engineer synthetic biomolecules will have far-reaching impacts:
*   **Drug Discovery**: Rational design of next-generation therapeutics.
*   **Synthetic Biology**: Engineering novel enzymes for sustainable biotechnology.
*   **Precision Medicine**: Understanding disease mechanisms at a molecular level.

This work aligns closely with the BBSRC’s vision to advance frontier bioscience. Given that the global pharmaceutical market is projected to exceed **$1.7 trillion**, even incremental advances in dynamic modelling can lead to substantial cost reductions and faster development timelines.

---

*This vision represents a transformative step for the UK’s computational biology landscape, establishing leadership in dynamic protein modelling.*
