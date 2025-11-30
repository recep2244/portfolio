---
title: "ReFOLD3 Server"
summary: "Refinement of 3D protein models using molecular dynamics simulations and quality assessment."
date: 2024-01-01
tags: ["Protein Refinement", "MD Simulations", "Web Server"]
---

<div class="grid md:grid-cols-2 gap-8 mb-12">
  <div>
    <h1 class="text-4xl font-bold text-slate-900 mb-4">ReFOLD3</h1>
    <p class="text-xl text-slate-600 leading-relaxed mb-6">
      State-of-the-art <strong>MD-based refinement</strong> for 3D protein models. 
      Combines molecular dynamics with quality assessment to improve prediction accuracy.
    </p>
    <div class="flex flex-wrap gap-3">
      <span class="px-4 py-2 bg-blue-100 text-blue-700 rounded-full text-sm font-bold">Web Server</span>
      <span class="px-4 py-2 bg-green-100 text-green-700 rounded-full text-sm font-bold">MD Simulations</span>
      <span class="px-4 py-2 bg-purple-100 text-purple-700 rounded-full text-sm font-bold">Quality Assessment</span>
    </div>
  </div>
  <div class="bg-gradient-to-br from-blue-500 to-indigo-600 rounded-2xl p-8 text-white flex items-center justify-center">
    <div class="text-center">
      <div class="text-6xl font-bold mb-2">Top 10</div>
      <p class="text-lg opacity-90">CASP13 Refinement Method</p>
    </div>
  </div>
</div>

<div class="my-12">
  <img src="/images/research/fig3_refold4.jpg" alt="ReFOLD4 Refinement Protocol" class="w-full rounded-2xl shadow-2xl border border-slate-200 hover:scale-105 transition-transform duration-500" />
  <p class="text-center text-sm text-slate-500 mt-4 italic">ReFOLD4 protocol: Fine-grained restraint strategies guided by local quality estimation</p>
</div>

<div class="grid md:grid-cols-3 gap-6 mb-12">
  <div class="bg-white rounded-xl p-6 shadow-lg border-t-4 border-blue-500">
    <div class="text-4xl mb-3">⚡</div>
    <h3 class="text-lg font-bold text-slate-900 mb-2">MD-based Refinement</h3>
    <p class="text-slate-600 text-sm">Interactive Molecular Dynamics protocols to relax and optimize structures</p>
  </div>
  
  <div class="bg-white rounded-xl p-6 shadow-lg border-t-4 border-purple-500">
    <div class="text-4xl mb-3">🎯</div>
    <h3 class="text-lg font-bold text-slate-900 mb-2">Quality Assessment</h3>
    <p class="text-slate-600 text-sm">Integrates ModFOLD QA scores to select the best refined models</p>
  </div>
  
  <div class="bg-white rounded-xl p-6 shadow-lg border-t-4 border-green-500">
    <div class="text-4xl mb-3">🤖</div>
    <h3 class="text-lg font-bold text-slate-900 mb-2">Automated Pipeline</h3>
    <p class="text-slate-600 text-sm">Simply upload your PDB file and let the server handle the rest</p>
  </div>
</div>

<div class="bg-gradient-to-r from-slate-900 to-slate-800 rounded-2xl p-8 text-white mb-12">
  <h2 class="text-2xl font-bold mb-6">How to Use</h2>
  <div class="grid md:grid-cols-4 gap-4">
    <div class="text-center">
      <div class="w-12 h-12 bg-blue-500 rounded-full flex items-center justify-center mx-auto mb-3 text-xl font-bold">1</div>
      <p class="text-sm">Upload PDB model</p>
    </div>
    <div class="text-center">
      <div class="w-12 h-12 bg-purple-500 rounded-full flex items-center justify-center mx-auto mb-3 text-xl font-bold">2</div>
      <p class="text-sm">Configure intensity</p>
    </div>
    <div class="text-center">
      <div class="w-12 h-12 bg-pink-500 rounded-full flex items-center justify-center mx-auto mb-3 text-xl font-bold">3</div>
      <p class="text-sm">Run refinement</p>
    </div>
    <div class="text-center">
      <div class="w-12 h-12 bg-green-500 rounded-full flex items-center justify-center mx-auto mb-3 text-xl font-bold">4</div>
      <p class="text-sm">Download results</p>
    </div>
  </div>
</div>

<div class="text-center">
  <a href="https://www.reading.ac.uk/bioinf/ReFOLD/ReFOLD3_form.html" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-3 px-10 py-5 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-white font-bold rounded-xl transition-all shadow-xl hover:shadow-2xl text-xl hover:scale-105 transform">
    <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
    Launch ReFOLD3 Server
  </a>
</div>
