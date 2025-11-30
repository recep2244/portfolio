---
title: "From Static to Dynamic: The Future of Protein Modelling"
summary: "Why we need to move beyond static snapshots to capture the full range of conformational dynamics."
date: 2024-11-29
tags: ["Protein Dynamics", "AlphaFold", "Modelling"]
---

<div class="relative overflow-hidden rounded-2xl bg-gradient-to-br from-blue-50 to-indigo-50 p-8 mb-12 border border-blue-100">
  <div class="absolute top-0 right-0 w-64 h-64 bg-blue-200 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-pulse"></div>
  <div class="relative">
    <h2 class="text-3xl font-bold text-slate-900 mb-4">The Static Problem</h2>
    <p class="text-lg text-slate-700 leading-relaxed">
      AlphaFold2 revolutionized structural biology—but it shows us only <strong>one frozen moment</strong>. 
      Proteins are dynamic machines, constantly breathing and moving.
    </p>
  </div>
</div>

<div class="grid md:grid-cols-2 gap-8 mb-12">
  <div class="bg-white rounded-xl p-6 shadow-lg border border-slate-100 hover:shadow-xl transition-shadow">
    <div class="w-12 h-12 bg-red-100 rounded-lg flex items-center justify-center mb-4">
      <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
    </div>
    <h3 class="text-xl font-bold text-slate-900 mb-3">What Static Models Miss</h3>
    <ul class="space-y-2 text-slate-600">
      <li class="flex items-start gap-2">
        <span class="text-red-500 mt-1">•</span>
        <span>Conformational diversity across states</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-red-500 mt-1">•</span>
        <span>Allosteric communication pathways</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-red-500 mt-1">•</span>
        <span>Mutation-induced flexibility changes</span>
      </li>
    </ul>
  </div>

  <div class="bg-white rounded-xl p-6 shadow-lg border border-slate-100 hover:shadow-xl transition-shadow">
    <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-4">
      <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
    </div>
    <h3 class="text-xl font-bold text-slate-900 mb-3">Dynamic Modelling Captures</h3>
    <ul class="space-y-2 text-slate-600">
      <li class="flex items-start gap-2">
        <span class="text-green-500 mt-1">•</span>
        <span>Ensemble of biologically relevant states</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-green-500 mt-1">•</span>
        <span>Cryptic binding pockets</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-green-500 mt-1">•</span>
        <span>Functional motion mechanisms</span>
      </li>
    </ul>
  </div>
</div>

<div class="my-12">
  <img src="/images/research/fig3_refold4.jpg" alt="ReFOLD4 Refinement" class="w-full rounded-2xl shadow-2xl border border-slate-200 hover:scale-105 transition-transform duration-500" />
  <p class="text-center text-sm text-slate-500 mt-4 italic">Figure: ReFOLD4 protocol refining static predictions into dynamic ensembles</p>
</div>

<div class="bg-gradient-to-r from-indigo-600 to-blue-600 rounded-2xl p-8 text-white mb-12">
  <h2 class="text-3xl font-bold mb-4">The Vision</h2>
  <p class="text-lg leading-relaxed opacity-90">
    Transform protein structure prediction from <strong>static snapshots</strong> to <strong>dynamic movies</strong>. 
    By integrating AI with Molecular Dynamics, we capture the breathing motions essential for understanding 
    mutations, de novo designs, and drug resistance.
  </p>
</div>

<div class="my-12">
  <img src="/images/research/fig1_pipeline.jpg" alt="Dynamic Modelling Pipeline" class="w-full rounded-2xl shadow-2xl border border-slate-200 hover:scale-105 transition-transform duration-500" />
  <p class="text-center text-sm text-slate-500 mt-4 italic">Figure: End-to-end pipeline for dynamic protein modelling</p>
</div>

<div class="bg-slate-50 rounded-2xl p-8 border border-slate-200">
  <h3 class="text-2xl font-bold text-slate-900 mb-4">Impact</h3>
  <div class="grid md:grid-cols-3 gap-6">
    <div class="text-center">
      <div class="text-4xl font-bold text-blue-600 mb-2">10x</div>
      <p class="text-slate-600">Better mutation modeling</p>
    </div>
    <div class="text-center">
      <div class="text-4xl font-bold text-indigo-600 mb-2">100+</div>
      <p class="text-slate-600">Conformational states captured</p>
    </div>
    <div class="text-center">
      <div class="text-4xl font-bold text-purple-600 mb-2">∞</div>
      <p class="text-slate-600">Possibilities for drug discovery</p>
    </div>
  </div>
</div>
