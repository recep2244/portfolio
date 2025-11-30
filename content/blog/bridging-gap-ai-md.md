---
title: "Bridging the Gap: AI, MD, and De Novo Design"
summary: "Integrating deep learning with molecular dynamics and local quality estimation to model mutants and novel folds."
date: 2024-11-29
tags: ["AI", "Molecular Dynamics", "De Novo Design"]
---

<div class="relative overflow-hidden rounded-2xl bg-gradient-to-br from-purple-50 to-pink-50 p-8 mb-12 border border-purple-100">
  <div class="absolute bottom-0 left-0 w-64 h-64 bg-purple-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-pulse"></div>
  <div class="relative">
    <h2 class="text-3xl font-bold text-slate-900 mb-4">The Hybrid Approach</h2>
    <p class="text-lg text-slate-700 leading-relaxed">
      Combining the <strong>speed of AI</strong> with the <strong>physics of MD</strong> and the 
      <strong>precision of local quality estimation</strong>.
    </p>
  </div>
</div>

<div class="grid md:grid-cols-3 gap-6 mb-12">
  <div class="group bg-white rounded-xl p-6 shadow-lg border-2 border-blue-100 hover:border-blue-500 transition-all hover:-translate-y-2">
    <div class="w-16 h-16 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
      <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
    </div>
    <h3 class="text-xl font-bold text-slate-900 mb-2">Machine Learning</h3>
    <p class="text-slate-600">Initial structure generation</p>
  </div>

  <div class="group bg-white rounded-xl p-6 shadow-lg border-2 border-purple-100 hover:border-purple-500 transition-all hover:-translate-y-2">
    <div class="w-16 h-16 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
      <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
    </div>
    <h3 class="text-xl font-bold text-slate-900 mb-2">Molecular Dynamics</h3>
    <p class="text-slate-600">Conformational sampling</p>
  </div>

  <div class="group bg-white rounded-xl p-6 shadow-lg border-2 border-pink-100 hover:border-pink-500 transition-all hover:-translate-y-2">
    <div class="w-16 h-16 bg-gradient-to-br from-pink-500 to-pink-600 rounded-xl flex items-center justify-center mb-4 group-hover:scale-110 transition-transform">
      <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
    </div>
    <h3 class="text-xl font-bold text-slate-900 mb-2">Quality Estimation</h3>
    <p class="text-slate-600">Adaptive restraints</p>
  </div>
</div>

<div class="my-12">
  <img src="/images/research/fig4_sars_cov2.jpg" alt="SARS-CoV-2 Refinement" class="w-full rounded-2xl shadow-2xl border border-slate-200 hover:scale-105 transition-transform duration-500" />
  <p class="text-center text-sm text-slate-500 mt-4 italic">Figure: ReFOLD3 refining SARS-CoV-2 viral protein structures</p>
</div>

<div class="bg-gradient-to-r from-purple-600 to-pink-600 rounded-2xl p-8 text-white mb-12">
  <h2 class="text-3xl font-bold mb-4">Why Local Quality Matters</h2>
  <p class="text-lg leading-relaxed opacity-90">
    Protein motion isn't uniform. <strong>Stable cores</strong> need tight restraints. 
    <strong>Flexible loops</strong> need freedom. Local quality scores let us distinguish between them, 
    refining uncertain regions while preserving well-predicted ones.
  </p>
</div>

<div class="my-12">
  <img src="/images/research/fig5_1_funfold.jpg" alt="FunFOLD Protocols" class="w-full rounded-2xl shadow-2xl border border-slate-200 hover:scale-105 transition-transform duration-500" />
  <p class="text-center text-sm text-slate-500 mt-4 italic">Figure: Template-based vs template-free protocols for CASP16 target</p>
</div>

<div class="grid md:grid-cols-2 gap-8">
  <div class="bg-blue-50 rounded-xl p-6 border-l-4 border-blue-600">
    <h3 class="text-xl font-bold text-slate-900 mb-3">De Novo Design</h3>
    <p class="text-slate-700">Model novel folds where evolutionary information is absent</p>
  </div>
  <div class="bg-purple-50 rounded-xl p-6 border-l-4 border-purple-600">
    <h3 class="text-xl font-bold text-slate-900 mb-3">Mutant Modelling</h3>
    <p class="text-slate-700">Capture subtle structural changes that determine stability</p>
  </div>
</div>
