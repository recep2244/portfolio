---
title: "ModFOLDdock2Q"
summary: "Quality assessment of protein-protein complex models using deep learning and structural features."
date: 2024-01-01
tags: ["Docker", "Protein-Protein Docking", "Quality Assessment"]
---

# ModFOLDdock2Q

ModFOLDdock2Q is a comprehensive tool for assessing the quality of protein-protein complex models. It leverages deep learning and structural features to predict the accuracy of docking poses.

![Figure 1: Quality Assessment Pipeline](/images/research/fig1_pipeline.jpg "QA Pipeline Overview")

## 🐳 Docker Installation

The easiest way to run ModFOLDdock2Q is via Docker. This ensures all dependencies are correctly configured.

```bash
docker pull radiyaman/modfolddock2q
```

## Usage Guide

Run ModFOLDdock2Q on your protein complex:

```bash
docker run -v $(pwd):/data radiyaman/modfolddock2q \
  -i /data/complex.pdb \
  -o /data/output
```

## Key Features
- **Deep Learning QA**: Uses neural networks trained on CASP data
- **Multi-metric Scoring**: Combines structural and energetic features
- **Fast Processing**: Analyzes complexes in seconds
- **Docker Deployment**: Easy installation and reproducibility

## Resources

<div class="not-prose my-8 flex flex-wrap gap-4">
  <a href="https://hub.docker.com/r/radiyaman/modfolddock2q" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-bold rounded-lg transition-all shadow-md hover:shadow-lg">
    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M13.983 11.078h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185m-2.954-5.43h2.119a.186.186 0 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.186.185.186m-2.93 0h2.12a.186.186 0 00.184-.186V3.574a.185.185 0 00-.184-.185h-2.12a.185.185 0 00-.184.185v1.888c0 .102.083.186.185.186m-2.964 0h2.119a.186.186 0 00.185-.186V3.574a.185.185 0 00-.185-.185H2.136a.185.185 0 00-.186.185v1.888c0 .102.083.186.186.186m-2.93 5.43h2.12a.186.186 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185v1.888c0 .102.083.185.185.185m-2.964 0h2.119a.186.186 0 00.185-.185V9.006a.185.185 0 00-.185-.186H2.136a.186.186 0 00-.186.185v1.888c0 .102.083.185.186.185m-2.929 0h2.12a.186.186 0 00.185-.185V9.006a.185.185 0 00-.185-.186h-2.12a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185M8.018 3.575h2.119a.186.186 0 00.186-.185V1.502a.186.186 0 00-.186-.186H8.018a.185.185 0 00-.185.186v1.888c0 .102.083.185.185.185m-2.969 0h2.12a.186.186 0 00.184-.185V1.502a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.186v1.888c0 .102.083.185.184.185m6.905 5.636L11.32 9.212a.26.26 0 00-.097.133.262.262 0 00-.013.213l.258.847a.26.26 0 00.315.178l.835-.25a.266.266 0 00.17-.348l-.257-.843a.26.26 0 00-.58-.068zM24 11.078c0-2.843-2.292-5.152-5.115-5.152h-.825v-1.25c0-.102-.083-.185-.185-.185h-2.119a.185.185 0 00-.186.185v1.25h-2.924v-1.25a.186.186 0 00-.186-.185h-2.119a.185.185 0 00-.185.185v1.25H7.332v-1.25a.185.185 0 00-.185-.185H5.028a.185.185 0 00-.185.185v1.25H2.108v-1.25a.185.185 0 00-.185-.185H.804a.185.185 0 00-.186.185v1.25H.185A.185.185 0 000 6.11v12.923c0 .102.083.185.185.185h23.63c.102 0 .185-.083.185-.185V11.078z"/></svg>
    Docker Hub
  </a>
  
  <a href="https://github.com/recep2244" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-6 py-3 bg-slate-900 hover:bg-slate-800 text-white font-bold rounded-lg transition-all shadow-md hover:shadow-lg">
    <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
    GitHub
  </a>
</div>

## Methodology
ModFOLDdock2Q uses a combination of:
- **Residue-level contact predictions**
- **Interface quality scores**
- **Global model assessment metrics**
