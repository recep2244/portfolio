---
title: "FunFOLD5"
summary: "Template-based ligand binding site prediction using structural alignment and quality assessment."
date: 2024-01-01
tags: ["Docker", "Ligand Binding", "Structure Prediction"]
---

# FunFOLD5

FunFOLD5 is a powerful tool for predicting ligand binding sites in protein structures. It uses a template-based approach, aligning your target structure against a library of known protein-ligand complexes to identify potential binding pockets.

![Figure 5.1/5.2: Template-based vs Template-free Protocols](/images/research/fig5_1_funfold.jpg "FunFOLD5 Protocols")

## 🐳 Docker Installation

Get the latest version from Docker Hub:

```bash
docker pull radiyaman/funfold5_template
```

## 🚀 Usage Guide

### Running a Prediction
Mount your data directory and specify the target structure:

```bash
docker run -v $(pwd):/data radiyaman/funfold5_template \
    -i /data/target.pdb \
    -o /data/results \
    --ligands /data/ligand_library
```

### Input Requirements
- **Target PDB**: A clean PDB file of your protein structure.
- **Ligand Library**: Optional path to a custom ligand library (default library included).

## How It Works
1. **Structural Alignment**: Aligns target against PDB templates.
2. **Cluster Analysis**: Groups ligands from similar templates.
3. **Quality Assessment**: Scores clusters based on conservation and geometry.
4. **Output**: Generates PDB files of predicted ligands superimposed on your target.

## Resources
- [Docker Hub Profile](https://hub.docker.com/r/radiyaman/funfold5_template)
- [Method Paper](https://doi.org/your-paper-doi)
