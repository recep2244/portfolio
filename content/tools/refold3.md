---
title: "ReFOLD3 Server"
summary: "Refinement of 3D protein models using molecular dynamics simulations and quality assessment."
date: 2024-01-01
tags: ["Protein Refinement", "MD Simulations", "Web Server"]
casp_rank: "Best Server CASP14"
stat: "Top-5 CASP13 Refinement"
color: "blue"
publications:
  - title: "ReFOLD3: Refinement of 3D protein models with gradual restraints based on predicted local quality and residue contacts"
    journal: "Nucleic Acids Research"
    year: "2021"
    citations: "22"
    doi: "https://doi.org/10.1093/nar/gkab300"
  - title: "Improvement of protein tertiary and quaternary structure predictions using the ReFOLD refinement method and the AlphaFold2 recycling process"
    journal: "Bioinformatics Advances"
    year: "2023"
    citations: "19"
    doi: "https://doi.org/10.1093/bioadv/vbad078"
  - title: "Methods for the Refinement of Protein Structure 3D Models"
    journal: "International Journal of Molecular Sciences"
    year: "2019"
    citations: "80"
    doi: "https://doi.org/10.3390/ijms20092301"
---

<p class="text-lg text-slate-400 leading-relaxed">
  <strong class="text-text">ReFOLD3</strong> refines 3D protein models with molecular dynamics under
  <strong class="text-text">gradual restraints</strong> derived from predicted per-residue quality and
  residue–residue contacts — improving accuracy beyond the starting model while guarding against
  over-refinement.
</p>

<!-- Benchmark strip -->
<div class="grid sm:grid-cols-3 gap-px bg-[color:var(--color-panel)] border border-[color:var(--color-panel)] rounded-xl overflow-hidden my-10">
  <div class="bg-[color:var(--color-surface)] p-6">
    <div class="text-2xl font-bold gradient-text leading-none">Top&nbsp;5</div>
    <div class="mono-meta mt-2">CASP13 refinement</div>
  </div>
  <div class="bg-[color:var(--color-surface)] p-6">
    <div class="text-2xl font-bold gradient-text leading-none">Best</div>
    <div class="mono-meta mt-2">Server · CASP14</div>
  </div>
  <div class="bg-[color:var(--color-surface)] p-6">
    <div class="text-2xl font-bold gradient-text leading-none">+AF2</div>
    <div class="mono-meta mt-2">Recycling protocol</div>
  </div>
</div>

<figure class="my-10">
  <img src="{{< relURL "images/research/fig3_refold4.jpg" >}}" alt="ReFOLD4 refinement protocol"
       class="w-full rounded-xl border border-[color:var(--color-panel)]" />
  <figcaption class="mono-meta mt-3 text-center">ReFOLD4 protocol — fine-grained restraint strategies guided by local quality estimation</figcaption>
</figure>

<!-- Capabilities -->
<div class="grid gap-px bg-[color:var(--color-panel)] border border-[color:var(--color-panel)] rounded-xl overflow-hidden sm:grid-cols-3 my-10">
  <div class="bg-[color:var(--color-surface)] p-6">
    <div class="mono-meta text-accent mb-3">01</div>
    <h3 class="text-base font-semibold text-text">MD-based refinement</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">Restrained molecular dynamics relaxes and optimises the model toward the native state.</p>
  </div>
  <div class="bg-[color:var(--color-surface)] p-6">
    <div class="mono-meta text-accent mb-3">02</div>
    <h3 class="text-base font-semibold text-text">Quality-guided restraints</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">ModFOLD per-residue scores decide where to restrain tightly and where to let regions move.</p>
  </div>
  <div class="bg-[color:var(--color-surface)] p-6">
    <div class="mono-meta text-accent mb-3">03</div>
    <h3 class="text-base font-semibold text-text">Automated selection</h3>
    <p class="text-sm text-slate-400 mt-2 leading-relaxed">Upload a PDB model; the server runs the protocol and returns the best-scoring refined structure.</p>
  </div>
</div>

<!-- Workflow -->
<div class="border border-[color:var(--color-panel)] rounded-xl p-6 md:p-7 my-10">
  <p class="mono-meta text-accent mb-5">&gt; how_to_run</p>
  <ol class="grid sm:grid-cols-4 gap-4 list-none p-0 m-0">
    <li class="flex sm:flex-col gap-3 items-baseline"><span class="mono-meta text-accent">01</span><span class="text-sm text-slate-300">Upload PDB model</span></li>
    <li class="flex sm:flex-col gap-3 items-baseline"><span class="mono-meta text-accent">02</span><span class="text-sm text-slate-300">Configure intensity</span></li>
    <li class="flex sm:flex-col gap-3 items-baseline"><span class="mono-meta text-accent">03</span><span class="text-sm text-slate-300">Run refinement</span></li>
    <li class="flex sm:flex-col gap-3 items-baseline"><span class="mono-meta text-accent">04</span><span class="text-sm text-slate-300">Download results</span></li>
  </ol>
</div>

<div class="my-10">
  <a href="https://www.reading.ac.uk/bioinf/ReFOLD/ReFOLD3_form.html" target="_blank" rel="noopener noreferrer" class="btn-primary">
    Launch ReFOLD3 Server
    <svg style="width:1rem;height:1rem" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
  </a>
</div>
