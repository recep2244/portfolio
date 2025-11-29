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
});
