---
title: "ReFOLD3 Server"
summary: "Refinement of 3D protein models using molecular dynamics simulations and quality assessment."
date: 2024-01-01
tags: ["Protein Refinement", "MD Simulations", "Web Server"]
---

# ReFOLD3: Refinement of 3D Protein Models

ReFOLD3 is a state-of-the-art web server for the refinement of 3D protein models. It combines molecular dynamics (MD) simulations with quality assessment (QA) to improve the accuracy of predicted structures.

## Key Features
- **MD-based Refinement**: Uses iMD (interactive Molecular Dynamics) protocols to relax and optimize structures.
- **Quality Assessment**: Integrates ModFOLD QA scores to select the best refined models.
- **Automated Pipeline**: Simply upload your PDB file and let the server handle the rest.

![Figure 3: ReFOLD4 Refinement Protocol](/images/research/fig3_refold4.jpg "ReFOLD Refinement Process")

## How to Use
1. **Upload**: Submit your starting PDB model.
2. **Configure**: Select refinement intensity (Quick vs. Intensive).
3. **Run**: The server processes your job and provides a unique ID.
4. **Analyze**: Download the refined models and view QA scores.

## Access ReFOLD3 Web Server

<div class="not-prose my-8">
  <a href="https://www.reading.ac.uk/bioinf/ReFOLD/ReFOLD3_form.html" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-3 px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-xl transition-all shadow-lg hover:shadow-xl text-lg">
    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
    Launch ReFOLD3 Server
  </a>
</div>

## Citation
If you use ReFOLD3 in your research, please cite:
> Adiyaman, R., et al. (2024). "ReFOLD3: Enhanced protein model refinement using molecular dynamics." *Bioinformatics*.
