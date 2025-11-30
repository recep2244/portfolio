---
title: "FunFOLD5"
summary: "Template-based ligand binding site prediction using structural alignment and quality assessment."
date: 2024-01-01
tags: ["Docker", "Ligand Binding", "Structure Prediction"]
---

<div class="grid md:grid-cols-2 gap-8 mb-12">
  <div>
    <h1 class="text-4xl font-bold text-slate-900 mb-4">FunFOLD5</h1>
    <p class="text-xl text-slate-600 leading-relaxed mb-6">
      Powerful <strong>ligand binding site prediction</strong> using template-based structural alignment. 
      Identify potential binding pockets with confidence.
    </p>
    <div class="flex flex-wrap gap-3">
      <span class="px-4 py-2 bg-emerald-100 text-emerald-700 rounded-full text-sm font-bold">Docker</span>
      <span class="px-4 py-2 bg-teal-100 text-teal-700 rounded-full text-sm font-bold">Template-based</span>
      <span class="px-4 py-2 bg-cyan-100 text-cyan-700 rounded-full text-sm font-bold">GitHub</span>
    </div>
  </div>
  <div class="bg-gradient-to-br from-emerald-500 to-teal-600 rounded-2xl p-8 text-white flex items-center justify-center">
    <div class="text-center">
      <div class="text-6xl font-bold mb-2">🎯</div>
      <p class="text-lg opacity-90">Precision Binding Sites</p>
    </div>
  </div>
</div>

<div class="my-12">
  <img src="{{< relURL "images/research/fig5_1_funfold.jpg" >}}" alt="FunFOLD5 Protocols" class="w-full rounded-2xl shadow-2xl border border-slate-200 hover:scale-105 transition-transform duration-500" />
  <p class="text-center text-sm text-slate-500 mt-4 italic">Template-based vs template-free protocols for CASP16 target L2000</p>
</div>

<div class="bg-slate-900 rounded-2xl p-8 text-white mb-12">
  <h2 class="text-2xl font-bold mb-6">🐳 Docker Installation</h2>
  <div class="bg-slate-800 rounded-lg p-4 font-mono text-sm overflow-x-auto">
    <span class="text-green-400">$</span> docker pull radiyaman/funfold5_template
  </div>
</div>

<div class="grid md:grid-cols-3 gap-6 mb-12">
  <div class="group bg-gradient-to-br from-emerald-50 to-white rounded-xl p-6 shadow-lg hover:shadow-2xl transition-all hover:-translate-y-2">
    <div class="text-4xl mb-3">🔬</div>
    <h3 class="text-lg font-bold text-slate-900 mb-2">Template-based</h3>
    <p class="text-slate-600 text-sm">Leverages known protein-ligand structures</p>
  </div>
  
  <div class="group bg-gradient-to-br from-teal-50 to-white rounded-xl p-6 shadow-lg hover:shadow-2xl transition-all hover:-translate-y-2">
    <div class="text-4xl mb-3">📍</div>
    <h3 class="text-lg font-bold text-slate-900 mb-2">Binding Sites</h3>
    <p class="text-slate-600 text-sm">Accurately predicts ligand binding pockets</p>
  </div>
  
  <div class="group bg-gradient-to-br from-cyan-50 to-white rounded-xl p-6 shadow-lg hover:shadow-2xl transition-all hover:-translate-y-2">
    <div class="text-4xl mb-3">⭐</div>
    <h3 class="text-lg font-bold text-slate-900 mb-2">Quality Scoring</h3>
    <p class="text-slate-600 text-sm">Ranks predictions by confidence</p>
  </div>
</div>

<div class="bg-gradient-to-r from-emerald-600 to-teal-600 rounded-2xl p-8 text-white mb-12">
  <h2 class="text-2xl font-bold mb-4">Usage Example</h2>
  <div class="bg-black/20 backdrop-blur-sm rounded-lg p-4 font-mono text-sm overflow-x-auto">
    <div class="text-green-300"># Run FunFOLD5 on your protein</div>
    <div class="mt-2">docker run -v $(pwd):/data radiyaman/funfold5_template \</div>
    <div class="ml-4">-i /data/target.pdb \</div>
    <div class="ml-4">-o /data/results</div>
  </div>
</div>

<div class="bg-gradient-to-br from-slate-50 to-emerald-50 rounded-2xl p-8 mb-12 border border-emerald-100">
  <h2 class="text-2xl font-bold text-slate-900 mb-6">Methodology</h2>
  <div class="space-y-4">
    <div class="flex items-start gap-4">
      <div class="w-10 h-10 bg-emerald-500 rounded-lg flex items-center justify-center flex-shrink-0 text-white font-bold">1</div>
      <div>
        <h4 class="font-bold text-slate-900 mb-1">Structural Alignment</h4>
        <p class="text-slate-600 text-sm">Align target against template libraries</p>
      </div>
    </div>
    <div class="flex items-start gap-4">
      <div class="w-10 h-10 bg-teal-500 rounded-lg flex items-center justify-center flex-shrink-0 text-white font-bold">2</div>
      <div>
        <h4 class="font-bold text-slate-900 mb-1">Binding Site Transfer</h4>
        <p class="text-slate-600 text-sm">Transfer ligand binding information from templates</p>
      </div>
    </div>
    <div class="flex items-start gap-4">
      <div class="w-10 h-10 bg-cyan-500 rounded-lg flex items-center justify-center flex-shrink-0 text-white font-bold">3</div>
      <div>
        <h4 class="font-bold text-slate-900 mb-1">Confidence Scoring</h4>
        <p class="text-slate-600 text-sm">Rank predicted sites by reliability</p>
      </div>
    </div>
  </div>
</div>

<div class="flex flex-wrap justify-center gap-4">
  <a href="https://hub.docker.com/r/radiyaman/funfold5_template" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-8 py-4 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700 text-white font-bold rounded-xl transition-all shadow-lg hover:shadow-xl hover:scale-105 transform">
    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M13.983 11.078h2.119a.186.186 0 00.186-.185V9.006a.186.186 0 00-.186-.186h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185m-2.954-5.43h2.119a.186.186 0 00.186-.186V3.574a.186.186 0 00-.186-.185h-2.119a.185.185 0 00-.185.185v1.888c0 .102.083.186.185.186m-2.93 0h2.12a.186.186 0 00.184-.186V3.574a.185.185 0 00-.184-.185h-2.12a.185.185 0 00-.184.185v1.888c0 .102.083.186.185.186m-2.964 0h2.119a.186.186 0 00.185-.186V3.574a.185.185 0 00-.185-.185H2.136a.185.185 0 00-.186.185v1.888c0 .102.083.186.186.186m-2.93 5.43h2.12a.186.186 0 00.184-.185V9.006a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.185v1.888c0 .102.083.185.185.185m-2.964 0h2.119a.186.186 0 00.185-.185V9.006a.185.185 0 00-.185-.186H2.136a.186.186 0 00-.186.185v1.888c0 .102.083.185.186.185m-2.929 0h2.12a.186.186 0 00.185-.185V9.006a.185.185 0 00-.185-.186h-2.12a.185.185 0 00-.185.185v1.888c0 .102.083.185.185.185M8.018 3.575h2.119a.186.186 0 00.186-.185V1.502a.186.186 0 00-.186-.186H8.018a.185.185 0 00-.185.186v1.888c0 .102.083.185.185.185m-2.969 0h2.12a.186.186 0 00.184-.185V1.502a.185.185 0 00-.184-.186h-2.12a.185.185 0 00-.184.186v1.888c0 .102.083.185.184.185m6.905 5.636L11.32 9.212a.26.26 0 00-.097.133.262.262 0 00-.013.213l.258.847a.26.26 0 00.315.178l.835-.25a.266.266 0 00.17-.348l-.257-.843a.26.26 0 00-.58-.068zM24 11.078c0-2.843-2.292-5.152-5.115-5.152h-.825v-1.25c0-.102-.083-.185-.185-.185h-2.119a.185.185 0 00-.186.185v1.25h-2.924v-1.25a.186.186 0 00-.186-.185h-2.119a.185.185 0 00-.185.185v1.25H7.332v-1.25a.185.185 0 00-.185-.185H5.028a.185.185 0 00-.185.185v1.25H2.108v-1.25a.185.185 0 00-.185-.185H.804a.185.185 0 00-.186.185v1.25H.185A.185.185 0 000 6.11v12.923c0 .102.083.185.185.185h23.63c.102 0 .185-.083.185-.185V11.078z"/></svg>
    Docker Hub
  </a>
  
  <a href="https://github.com/recep2244" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-8 py-4 bg-gradient-to-r from-slate-900 to-slate-800 hover:from-slate-800 hover:to-slate-700 text-white font-bold rounded-xl transition-all shadow-lg hover:shadow-xl hover:scale-105 transform">
    <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
    GitHub
  </a>
</div>
