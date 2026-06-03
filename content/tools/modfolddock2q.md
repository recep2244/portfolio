---
title: "ModFOLDdock2Q"
summary: "Quality assessment of protein-protein complex models using deep learning and structural features."
date: 2024-01-01
tags: ["Docker", "Protein-Protein Docking", "Quality Assessment"]
casp_rank: "CASP Validated"
stat: "16,000+ engineered features"
color: "purple"
publications:
  - title: "Prediction and quality assessment of protein quaternary structure models using the MultiFOLD2 and ModFOLDdock2 servers"
    journal: "Nucleic Acids Research"
    year: "2025"
    doi: "https://doi.org/10.1093/nar/gkaf336"
  - title: "Estimation of model accuracy in CASP15 using the ModFOLDdock server"
    journal: "Proteins: Structure, Function, and Bioinformatics"
    year: "2023"
    citations: "20"
    doi: "https://doi.org/10.1002/prot.26532"
  - title: "Highlights of model quality assessment in CASP16"
    journal: "Proteins: Structure, Function, and Bioinformatics"
    year: "2025"
    doi: "https://doi.org/10.1002/prot.70035"
---

<p class="text-lg text-slate-400 leading-relaxed">
  <strong class="text-text">ModFOLDdock2Q</strong> scores the quality of protein–protein and quaternary
  complex models, combining single-model and consensus signals through deep learning over a large
  engineered feature set — benchmarked at the CASP15 and CASP16 assessments.
</p>

<!-- Highlights -->
<div class="grid sm:grid-cols-3 gap-px bg-[color:var(--color-panel)] border border-[color:var(--color-panel)] rounded-xl overflow-hidden my-10">
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="text-2xl font-bold gradient-text leading-none">16K+</div>
    <div class="mono-meta mt-2">Engineered features</div>
  </div>
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="text-2xl font-bold gradient-text leading-none">Quaternary</div>
    <div class="mono-meta mt-2">Complex QA</div>
  </div>
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="text-2xl font-bold gradient-text leading-none">CASP15/16</div>
    <div class="mono-meta mt-2">EMA benchmarked</div>
  </div>
</div>

<!-- Install -->
<div class="border border-[color:var(--color-panel)] rounded-xl p-6 md:p-7 my-10">
  <p class="mono-meta text-accent mb-4">&gt; docker_pull</p>
  <pre class="bg-[#0a0f14] border border-[color:var(--color-panel)] rounded-lg p-4 overflow-x-auto text-sm m-0"><code><span class="text-accent">$</span> docker pull radiyaman/modfolddock2q</code></pre>
  <pre class="bg-[#0a0f14] border border-[color:var(--color-panel)] rounded-lg p-4 overflow-x-auto text-sm mt-3 mb-0"><code><span class="text-accent">$</span> docker run -v $(pwd):/data radiyaman/modfolddock2q \
    -i /data/complex.pdb -o /data/output</code></pre>
</div>

<!-- Capabilities -->
<div class="grid gap-px bg-[color:var(--color-panel)] border border-[color:var(--color-panel)] rounded-xl overflow-hidden sm:grid-cols-3 my-10">
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="mono-meta text-accent mb-3">01</div>
    <h3 class="text-base font-semibold text-text">Deep-learning QA</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">Networks trained on CASP complex targets predict per-interface and global accuracy.</p>
  </div>
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="mono-meta text-accent mb-3">02</div>
    <h3 class="text-base font-semibold text-text">Multi-signal scoring</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">Combines structural, statistical and energetic features (DockQ, QS, iLDDT, …).</p>
  </div>
  <div class="bg-[color:var(--color-surface)] glow-cell p-6">
    <div class="mono-meta text-accent mb-3">03</div>
    <h3 class="text-base font-semibold text-text">Reproducible</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">Containerised so results are identical across machines and pipelines.</p>
  </div>
</div>

<div class="flex flex-wrap gap-3 my-10">
  <a href="https://hub.docker.com/r/radiyaman/modfolddock2q" target="_blank" rel="noopener noreferrer" class="btn-primary">Docker Hub ↗</a>
  <a href="https://github.com/recep2244" target="_blank" rel="noopener noreferrer" class="btn-secondary">GitHub ↗</a>
</div>
