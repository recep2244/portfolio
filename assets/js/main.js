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

    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    document.querySelectorAll('.reveal-on-scroll, .reveal-fade, .sec-head').forEach(el => {
        revealObserver.observe(el);
    });

    // ─── Animated stat count-up ───────────────────────────────────────────────
    // Numbers with data-count-to animate from 0 → target when scrolled into view.
    const fmt = (n) => n >= 1000 ? n.toLocaleString() : String(n);
    const countObserver = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            const el = entry.target;
            obs.unobserve(el);
            const to = parseFloat(el.dataset.countTo);
            const suffix = el.dataset.countSuffix || '';
            if (reduceMotion || isNaN(to)) { el.textContent = fmt(to) + suffix; return; }
            const duration = 1400;
            let startTs = null;
            const step = (ts) => {
                if (startTs === null) startTs = ts;
                const p = Math.min((ts - startTs) / duration, 1);
                const eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
                el.textContent = fmt(Math.round(to * eased)) + suffix;
                if (p < 1) requestAnimationFrame(step);
            };
            requestAnimationFrame(step);
        });
    }, { threshold: 0.4 });
    document.querySelectorAll('[data-count-to]').forEach(el => countObserver.observe(el));

    // ─── Interactive pointer effects ──────────────────────────────────────────
    // Cursor-following ambient glow, per-card spotlight, magnetic buttons.
    // Skipped on touch devices and when the user prefers reduced motion.
    const finePointer = window.matchMedia('(pointer: fine)').matches;
    if (finePointer && !reduceMotion) {
        const glow = document.querySelector('.cursor-glow');
        const spotlights = document.querySelectorAll('.glass-card, .cv-card, .glow-cell');
        const magnets = document.querySelectorAll('.btn-primary, .btn-secondary, .nav-pill');

        let gx = 0, gy = 0, raf = null;
        window.addEventListener('pointermove', (e) => {
            gx = e.clientX; gy = e.clientY;
            if (glow && raf === null) {
                raf = requestAnimationFrame(() => {
                    raf = null;
                    glow.style.opacity = '1';
                    glow.style.setProperty('--cx', gx + 'px');
                    glow.style.setProperty('--cy', gy + 'px');
                });
            }
        }, { passive: true });
        document.addEventListener('mouseleave', () => { if (glow) glow.style.opacity = '0'; });

        spotlights.forEach(card => {
            card.addEventListener('pointermove', (e) => {
                const r = card.getBoundingClientRect();
                card.style.setProperty('--mx', ((e.clientX - r.left) / r.width * 100) + '%');
                card.style.setProperty('--my', ((e.clientY - r.top) / r.height * 100) + '%');
            }, { passive: true });
        });

        magnets.forEach(btn => {
            btn.addEventListener('pointermove', (e) => {
                const r = btn.getBoundingClientRect();
                const mx = e.clientX - (r.left + r.width / 2);
                const my = e.clientY - (r.top + r.height / 2);
                btn.style.transform = `translate(${mx * 0.22}px, ${my * 0.32}px)`;
            });
            btn.addEventListener('pointerleave', () => { btn.style.transform = ''; });
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
