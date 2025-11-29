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
});
