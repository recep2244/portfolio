---
title: "Bridging the Gap: AI, MD, and De Novo Design"
date: 2024-11-28
summary: "Integrating deep learning with molecular dynamics and local quality estimation to model mutants and novel folds."
tags: ["AI", "Molecular Dynamics", "De Novo Design"]
layout: "blog"
---

# Bridging the Gap: AI, MD, and De Novo Design

My fellowship project targets a pivotal gap: the lack of effective tools for modelling mutants and de novo-designed proteins.

## The Hybrid Approach
I am developing a next-generation framework that integrates:
1.  **Machine Learning**: For initial structure generation.
2.  **Molecular Dynamics (MD)**: For sampling conformational space.
3.  **Local Quality Estimation**: For guiding adaptive restraints.

![Figure 4: Refinement of the SARS-CoV-2 CASP-Commons initiative target C1908 (ORF7) using ReFOLD3 with gradual restraint strategies.](/images/research/fig4_sars_cov2.jpg "Figure 4: SARS-CoV-2 Target Refinement")

## Why Local Quality Matters
Since protein motion is not uniform, local quality estimation allows us to distinguish between stable cores and flexible loops. By using these scores as dynamic restraints, we can refine structurally uncertain regions while preserving well-predicted ones.

![Figure 5.1/5.2: Output from the template-based and template-free protocols for the CASP16 target L2000.](/images/research/fig5_1_funfold.jpg "Figure 5.1/5.2: Template-based vs Template-free Protocols")

This approach is particularly powerful for **de novo design**, where evolutionary information is absent, and **mutant modelling**, where subtle structural changes determine stability.
