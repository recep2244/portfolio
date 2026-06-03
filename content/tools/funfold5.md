---
title: "FunFOLD5"
summary: "Template-based ligand binding site prediction using structural alignment and quality assessment."
date: 2024-01-01
tags: ["Docker", "Ligand Binding", "Structure Prediction"]
casp_rank: "2nd Place CASP16"
stat: "Surpasses AlphaFold3 Server"
color: "emerald"
publications:
  - title: "Prediction of protein structures, functions and interactions using the IntFOLD7, MultiFOLD and ModFOLDdock servers"
    journal: "Nucleic Acids Research"
    year: "2023"
    citations: "67"
    doi: "https://doi.org/10.1093/nar/gkad297"
  - title: "Highlights of model quality assessment in CASP16"
    journal: "Proteins: Structure, Function, and Bioinformatics"
    year: "2025"
    doi: "https://doi.org/10.1002/prot.70035"
---

<p class="text-lg text-slate-400 leading-relaxed">
  <strong class="text-text">FunFOLD5</strong> predicts ligand-binding residues by structurally
  superposing the target against ligand-bound templates and transferring binding-site information —
  ranked 2nd for ligand prediction at CASP16, surpassing the AlphaFold3 server.
</p>

<!-- Highlights -->
<div class="grid sm:grid-cols-3 gap-px bg-[color:var(--color-panel)] border border-[color:var(--color-panel)] rounded-xl overflow-hidden my-10">
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="text-2xl font-bold gradient-text leading-none">2nd</div>
    <div class="mono-meta mt-2">CASP16 ligand</div>
  </div>
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="text-2xl font-bold gradient-text leading-none">&gt; AF3</div>
    <div class="mono-meta mt-2">Server baseline</div>
  </div>
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="text-2xl font-bold gradient-text leading-none">Template</div>
    <div class="mono-meta mt-2">Structure-based</div>
  </div>
</div>

<!-- Install -->
<div class="border border-[color:var(--color-panel)] rounded-xl p-6 md:p-7 my-10">
  <p class="mono-meta text-accent mb-4">&gt; docker_pull</p>
  <pre class="bg-[#0a0f14] border border-[color:var(--color-panel)] rounded-lg p-4 overflow-x-auto text-sm m-0"><code><span class="text-accent">$</span> docker pull radiyaman/funfold5_template</code></pre>
  <pre class="bg-[#0a0f14] border border-[color:var(--color-panel)] rounded-lg p-4 overflow-x-auto text-sm mt-3 mb-0"><code><span class="text-accent">$</span> docker run -v $(pwd):/data radiyaman/funfold5_template \
    -i /data/target.pdb -o /data/results</code></pre>
</div>

<!-- Methodology -->
<div class="grid gap-px bg-[color:var(--color-panel)] border border-[color:var(--color-panel)] rounded-xl overflow-hidden sm:grid-cols-3 my-10">
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="mono-meta text-accent mb-3">01</div>
    <h3 class="text-base font-semibold text-text">Structural alignment</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">Superpose the target structure against a library of ligand-bound templates.</p>
  </div>
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="mono-meta text-accent mb-3">02</div>
    <h3 class="text-base font-semibold text-text">Binding-site transfer</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">Map contacting residues from aligned templates onto the target sequence.</p>
  </div>
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="mono-meta text-accent mb-3">03</div>
    <h3 class="text-base font-semibold text-text">Confidence scoring</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">Cluster and rank predicted sites by template agreement and reliability.</p>
  </div>
</div>

<div class="flex flex-wrap gap-3 my-10">
  <a href="https://hub.docker.com/r/radiyaman/funfold5_template" target="_blank" rel="noopener noreferrer" class="btn-primary">Docker Hub ↗</a>
  <a href="https://github.com/recep2244" target="_blank" rel="noopener noreferrer" class="btn-secondary">GitHub ↗</a>
</div>
