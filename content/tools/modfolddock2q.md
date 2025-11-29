---
title: "ModFOLDdock2Q"
summary: "Quality assessment of protein-protein complex models using deep learning and structural features."
date: 2024-01-01
tags: ["Docker", "Protein-Protein Docking", "Quality Assessment"]
layout: "tool"
---

# ModFOLDdock2Q

ModFOLDdock2Q is a comprehensive tool for assessing the quality of protein-protein complex models. It leverages deep learning and structural features to predict the accuracy of docking poses.

## 🐳 Docker Installation

The easiest way to run ModFOLDdock2Q is via Docker. This ensures all dependencies are correctly configured.

```bash
docker pull radiyaman/modfolddock2q
```

## 🚀 Usage Guide

### Basic Command
To run the tool on a single PDB file:

```bash
docker run -v $(pwd):/data radiyaman/modfolddock2q \
    -i /data/input_complex.pdb \
    -o /data/output_results
```

### Parameters
- `-i`: Input PDB file (must be a complex with multiple chains).
- `-o`: Output directory for results.
- `-v`: Mounts your current directory to `/data` inside the container.

## Output Interpretation
The tool generates a report containing:
- **Global Score**: Overall quality of the complex (0-1).
- **Interface Score**: Quality of the protein-protein interface.
- **Per-Residue Scores**: Local quality estimates for each residue.

## Resources
- [Docker Hub Profile](https://hub.docker.com/r/radiyaman/modfolddock2q)
- [GitHub Repository](https://github.com/recep2244/modfolddock2q)
