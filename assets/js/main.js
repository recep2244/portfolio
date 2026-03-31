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

    // ─── Scroll-spy: highlight active nav section ─────────────────────────────
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('a[href*="#"]');
    if (sections.length && navLinks.length) {
        const spyObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.id;
                    navLinks.forEach(link => {
                        const isMatch = link.getAttribute('href').endsWith('#' + id) ||
                                        link.getAttribute('href') === '#' + id;
                        link.classList.toggle('nav-active', isMatch);
                    });
                }
            });
        }, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });
        sections.forEach(s => spyObserver.observe(s));
    }
});
