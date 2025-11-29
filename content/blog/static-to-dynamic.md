---
title: "From Static to Dynamic: The Future of Protein Modelling"
date: 2024-11-29
summary: "Why we need to move beyond static snapshots to capture the full range of conformational dynamics in protein structure prediction."
tags: ["Protein Dynamics", "AlphaFold", "Modelling"]
---

# From Static to Dynamic: The Future of Protein Modelling

The 3D structure of proteins governs their molecular functionality. While methods like AlphaFold2 have revolutionised prediction, they typically generate static models.

## The Limitation of Static Models
Proteins are not rigid statues; they are breathing, moving machines. Static models overlook:
- **Conformational Diversity**: Proteins often exist in ensembles of states.
- **Allostery**: How binding at one site affects another.
- **Mutation Effects**: How a single amino acid change alters flexibility.

![Figure 3: Refinement of the CASP14 regular TBM target T1095 using the ReFOLD4 protocol guided by fine-grained restraint strategies based on local quality estimation (pLDDT).](/images/research/fig3_refold4.jpg "Figure 3: ReFOLD4 Refinement Protocol")

## My Vision
My vision is to transform protein structure prediction from static to dynamic. By developing an iterative protocol that generates and evaluates alternative conformations, we can capture the natural dynamics of proteins, including those with mutations or entirely novel sequences.

![Figure 1: Overview of the pipeline for dynamic modeling of protein and protein-ligand complexes (example target: T1300, CASP16 target).](/images/research/fig1_pipeline.jpg "Figure 1: Dynamic Modelling Pipeline Overview")

This dynamic modelling capability is essential for understanding function, flexibility, and interactions in biologically relevant contexts.
