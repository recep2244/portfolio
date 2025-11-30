---
title: "The Future is Dynamic"
summary: "Transforming protein structure prediction from static snapshots to dynamic ensembles for de novo design and drug discovery."
date: 2024-11-29
layout: "vision"
---

# The Future is Dynamic

**Proteins are not statues.** They are breathing, moving molecular machines. Yet, the tools we rely on—even state-of-the-art AI like AlphaFold2—treat them as static sculptures.

My work shatters this limitation.

{{< figure src="/images/research/fig1_pipeline.jpg" title="Figure 1: Dynamic modelling pipeline from AI prediction → MD sampling → QA-guided refinement." class="rounded-2xl shadow-2xl border border-slate-200 my-8" >}}

## The Problem: Static Blindness
Current methods fail where it matters most:
*   **Mutations**: A single atom change can alter motion without changing the static fold.
*   **De Novo Design**: Novel proteins lack the evolutionary history AI relies on.
*   **Drug Resistance**: Often driven by subtle dynamic shifts, not just steric clashes.

## The Solution: AI + Physics
I am building the **next-generation dynamic modelling framework**. By fusing Deep Learning with Molecular Dynamics (MD) and local quality estimation, we can predict not just *structure*, but *behavior*.

### 1. Beyond Evolution
Standard AI leans on evolutionary history (MSA). My protocol integrates **MD-driven sampling** to explore conformational space for targets where evolution is silent—like **de novo designed proteins** and **orphan targets**.

### 2. Precision Refinement
Using **Local Quality Estimation** as a guide, we apply "smart restraints." We lock down the stable core while letting the flexible loops and binding sites breathe. This captures the **true ensemble** of the protein.

### 3. Real-World Impact
This isn't just theory. It's about engineering better enzymes and designing smarter drugs.
*   **SARS-CoV-2**: We revealed hidden states in viral proteins.
*   **Drug Discovery**: We uncover cryptic pockets invisible to static methods.

**We are moving from predicting a single snapshot to simulating the movie of life.**
