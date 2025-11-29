// Scroll Reveal Animation
document.addEventListener('DOMContentLoaded', () => {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    // Elements to animate
    const elements = document.querySelectorAll('.glass-card, .section-heading, .eyebrow, .pill, p, h1, h2, h3');
    elements.forEach(el => {
        el.classList.add('reveal-on-scroll');
        observer.observe(el);
    });

    // Dynamic Antibody Scores - Cycling through different mutations
    const scoreElements = {
        dockq: document.querySelector('[data-score="dockq"]'),
        qs: document.querySelector('[data-score="qs"]'),
        ics: document.querySelector('[data-score="ics"]'),
        modfold: document.querySelector('[data-score="modfold"]')
    };

    // Different mutation scenarios with their scores
    const mutations = [
        { name: 'Wild Type', dockq: 0.72, qs: 0.68, ics: 0.74, modfold: 0.65 },
        { name: 'Y33W', dockq: 0.85, qs: 0.92, ics: 0.88, modfold: 0.76 },
        { name: 'S52F', dockq: 0.91, qs: 0.87, ics: 0.93, modfold: 0.82 },
        { name: 'T28A', dockq: 0.68, qs: 0.71, ics: 0.65, modfold: 0.61 },
        { name: 'D31K', dockq: 0.79, qs: 0.84, ics: 0.81, modfold: 0.73 }
    ];

    let currentMutationIndex = 0;

    function updateScores() {
        if (!scoreElements.dockq) return; // Exit if elements don't exist

        const mutation = mutations[currentMutationIndex];

        // Update each score with animation
        if (scoreElements.dockq) scoreElements.dockq.textContent = mutation.dockq.toFixed(2);
        if (scoreElements.qs) scoreElements.qs.textContent = mutation.qs.toFixed(2);
        if (scoreElements.ics) scoreElements.ics.textContent = mutation.ics.toFixed(2);
        if (scoreElements.modfold) scoreElements.modfold.textContent = mutation.modfold.toFixed(2);

        // Move to next mutation
        currentMutationIndex = (currentMutationIndex + 1) % mutations.length;
    }

    // Update scores every 4 seconds
    if (scoreElements.dockq) {
        setInterval(updateScores, 4000);
    }

    // Interactive Protein Engineering Simulation
    const mutationBtns = document.querySelectorAll('.mutation-btn');
    const residueVisual = document.getElementById('residue-visual');
    const mutationLabel = document.getElementById('mutation-label');

    if (mutationBtns.length > 0 && residueVisual) {
        mutationBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from all
                mutationBtns.forEach(b => b.classList.remove('active', 'bg-slate-300'));
                mutationBtns.forEach(b => b.classList.add('bg-slate-100'));

                // Add active class to clicked
                btn.classList.add('active', 'bg-slate-300');
                btn.classList.remove('bg-slate-100');

                const mutationType = btn.getAttribute('data-mutation');
                mutationLabel.textContent = mutationType;

                // Update Visual based on mutation
                let visualContent = '';
                switch (mutationType) {
                    case 'Wild Type':
                        visualContent = `
                            <circle cx="100" cy="65" r="8" fill="#64748b" class="transition-all duration-500" />
                            <text x="100" y="50" text-anchor="middle" fill="#475569" font-size="10" font-weight="bold">WT</text>
                        `;
                        break;
                    case 'Y33W': // Tryptophan (Bulky, Green)
                        visualContent = `
                            <circle cx="100" cy="65" r="14" fill="#15803d" class="transition-all duration-500 animate-pulse" />
                            <text x="100" y="45" text-anchor="middle" fill="#15803d" font-size="12" font-weight="bold">Trp</text>
                            <path d="M90,75 L80,90" stroke="#15803d" stroke-width="2" />
                            <path d="M110,75 L120,90" stroke="#15803d" stroke-width="2" />
                        `;
                        break;
                    case 'S52F': // Phenylalanine (Aromatic, Blue)
                        visualContent = `
                            <rect x="90" y="55" width="20" height="20" fill="#1d4ed8" class="transition-all duration-500" transform="rotate(45 100 65)" />
                            <text x="100" y="45" text-anchor="middle" fill="#1d4ed8" font-size="12" font-weight="bold">Phe</text>
                        `;
                        break;
                    case 'T28A': // Alanine (Small, Red)
                        visualContent = `
                            <circle cx="100" cy="65" r="6" fill="#b91c1c" class="transition-all duration-500" />
                            <text x="100" y="50" text-anchor="middle" fill="#b91c1c" font-size="10" font-weight="bold">Ala</text>
                        `;
                        break;
                }
                residueVisual.innerHTML = visualContent;
            });
        });
    }
});
