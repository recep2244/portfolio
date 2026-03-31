document.addEventListener('DOMContentLoaded', () => {

    // ─── Scroll Reveal ───────────────────────────────────────────────────────
    // Only observe elements that are explicitly marked with .reveal-on-scroll
    // in the HTML templates. Do NOT auto-add the class to p/h1-h3 — that causes
    // overflow:hidden parents to clip translated children, leaving them invisible.
    const revealObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                obs.unobserve(entry.target);
            }
        });
    }, {
        root: null,
        rootMargin: '0px 0px -40px 0px',
        threshold: 0.08
    });

    document.querySelectorAll('.reveal-on-scroll').forEach(el => {
        revealObserver.observe(el);
    });

    // ─── Dynamic Mutation Scores ─────────────────────────────────────────────
    const scoreElements = {
        dockq:   document.querySelector('[data-score="dockq"]'),
        qs:      document.querySelector('[data-score="qs"]'),
        ics:     document.querySelector('[data-score="ics"]'),
        modfold: document.querySelector('[data-score="modfold"]')
    };

    const mutations = [
        { name: 'Wild Type', dockq: 0.72, qs: 0.68, ics: 0.74, modfold: 0.65 },
        { name: 'Y33W',      dockq: 0.85, qs: 0.92, ics: 0.88, modfold: 0.76 },
        { name: 'S52F',      dockq: 0.91, qs: 0.87, ics: 0.93, modfold: 0.82 },
        { name: 'T28A',      dockq: 0.68, qs: 0.71, ics: 0.65, modfold: 0.61 },
        { name: 'D31K',      dockq: 0.79, qs: 0.84, ics: 0.81, modfold: 0.73 }
    ];

    let mutationIndex = 0;

    function updateScores() {
        if (!scoreElements.dockq) return;
        const m = mutations[mutationIndex];
        if (scoreElements.dockq)   scoreElements.dockq.textContent   = m.dockq.toFixed(2);
        if (scoreElements.qs)      scoreElements.qs.textContent      = m.qs.toFixed(2);
        if (scoreElements.ics)     scoreElements.ics.textContent     = m.ics.toFixed(2);
        if (scoreElements.modfold) scoreElements.modfold.textContent = m.modfold.toFixed(2);
        mutationIndex = (mutationIndex + 1) % mutations.length;
    }

    if (scoreElements.dockq) setInterval(updateScores, 4000);

    // ─── Interactive Protein Engineering Simulation ──────────────────────────
    const mutationBtns  = document.querySelectorAll('.mutation-btn');
    const residueVisual = document.getElementById('residue-visual');
    const mutationLabel = document.getElementById('mutation-label');

    if (mutationBtns.length > 0 && residueVisual) {
        mutationBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                mutationBtns.forEach(b => {
                    b.classList.remove('active', 'bg-slate-300');
                    b.classList.add('bg-slate-100');
                });
                btn.classList.add('active', 'bg-slate-300');
                btn.classList.remove('bg-slate-100');
                if (mutationLabel) mutationLabel.textContent = btn.getAttribute('data-mutation');

                const type = btn.getAttribute('data-mutation');
                let svg = '';
                switch (type) {
                    case 'Wild Type':
                        svg = `<circle cx="100" cy="65" r="8" fill="#64748b"/>
                               <text x="100" y="50" text-anchor="middle" fill="#475569" font-size="10" font-weight="bold">WT</text>`;
                        break;
                    case 'Y33W':
                        svg = `<circle cx="100" cy="65" r="14" fill="#15803d" class="animate-pulse"/>
                               <text x="100" y="45" text-anchor="middle" fill="#15803d" font-size="12" font-weight="bold">Trp</text>
                               <path d="M90,75 L80,90" stroke="#15803d" stroke-width="2"/>
                               <path d="M110,75 L120,90" stroke="#15803d" stroke-width="2"/>`;
                        break;
                    case 'S52F':
                        svg = `<rect x="90" y="55" width="20" height="20" fill="#1d4ed8" transform="rotate(45 100 65)"/>
                               <text x="100" y="45" text-anchor="middle" fill="#1d4ed8" font-size="12" font-weight="bold">Phe</text>`;
                        break;
                    case 'T28A':
                        svg = `<circle cx="100" cy="65" r="6" fill="#b91c1c"/>
                               <text x="100" y="50" text-anchor="middle" fill="#b91c1c" font-size="10" font-weight="bold">Ala</text>`;
                        break;
                }
                residueVisual.innerHTML = svg;
            });
        });
    }

    // ─── Reading Progress Bar ─────────────────────────────────────────────────
    const progressBar = document.querySelector('.reading-progress');
    if (progressBar) {
        window.addEventListener('scroll', () => {
            const scrolled = window.scrollY;
            const total    = document.documentElement.scrollHeight - window.innerHeight;
            progressBar.style.width = total > 0 ? `${(scrolled / total) * 100}%` : '0%';
        }, { passive: true });
    }

    // ─── Scroll-to-top button ─────────────────────────────────────────────────
    const scrollTopBtn = document.querySelector('.scroll-to-top');
    if (scrollTopBtn) {
        window.addEventListener('scroll', () => {
            scrollTopBtn.classList.toggle('visible', window.scrollY > 400);
        }, { passive: true });
        scrollTopBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    }
});
