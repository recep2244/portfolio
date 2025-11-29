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

## Why Local Quality Matters
Since protein motion is not uniform, local quality estimation allows us to distinguish between stable cores and flexible loops. By using these scores as dynamic restraints, we can refine structurally uncertain regions while preserving well-predicted ones.

This approach is particularly powerful for **de novo design**, where evolutionary information is absent, and **mutant modelling**, where subtle structural changes determine stability.
