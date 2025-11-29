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

## How to Use
1. **Upload**: Submit your starting PDB model.
2. **Configure**: Select refinement intensity (Quick vs. Intensive).
3. **Run**: The server processes your job and provides a unique ID.
4. **Analyze**: Download the refined models and view QA scores.

## Launch ReFOLD3
You can use the embedded interface below or [open it in a new tab](https://www.reading.ac.uk/bioinf/ReFOLD/ReFOLD3_form.html).

<div class="w-full h-[800px] bg-white rounded-xl border border-slate-200 overflow-hidden shadow-lg mt-8 relative">
    <iframe src="https://www.reading.ac.uk/bioinf/ReFOLD/ReFOLD3_form.html" 
            class="w-full h-full" 
            frameborder="0"
            sandbox="allow-scripts allow-same-origin allow-forms allow-popups">
    </iframe>
</div>

## Citation
If you use ReFOLD3 in your research, please cite:
> Adiyaman, R., et al. (2024). "ReFOLD3: Enhanced protein model refinement using molecular dynamics." *Bioinformatics*.
