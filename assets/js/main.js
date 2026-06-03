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

        // Custom trailing ring cursor
        const ring = document.querySelector('.cursor-ring');
        if (ring) {
            let rx = -100, ry = -100, tx = -100, ty = -100;
            window.addEventListener('pointermove', (e) => {
                tx = e.clientX; ty = e.clientY; ring.style.opacity = '1';
            }, { passive: true });
            const tickRing = () => {
                rx += (tx - rx) * 0.18; ry += (ty - ry) * 0.18;
                ring.style.setProperty('--rx', rx + 'px');
                ring.style.setProperty('--ry', ry + 'px');
                requestAnimationFrame(tickRing);
            };
            tickRing();
            document.querySelectorAll('a, button, .glass-card, .glow-cell, input, textarea, select, [role="button"]').forEach(el => {
                el.addEventListener('pointerenter', () => ring.classList.add('active'));
                el.addEventListener('pointerleave', () => ring.classList.remove('active'));
            });
        }

        // 3D tilt on the big glass panels
        document.querySelectorAll('.glass-card').forEach(card => {
            card.addEventListener('pointermove', (e) => {
                const r = card.getBoundingClientRect();
                const px = (e.clientX - r.left) / r.width - 0.5;
                const py = (e.clientY - r.top) / r.height - 0.5;
                card.style.transform = `perspective(900px) rotateX(${-py * 4.5}deg) rotateY(${px * 4.5}deg)`;
            });
            card.addEventListener('pointerleave', () => { card.style.transform = ''; });
        });
    }

    // ─── Text scramble / decode (matrix-style) ────────────────────────────────
    if (!reduceMotion) {
        const SC = '01<>-_/[]{}=+*^?#abcdef';
        const scramble = (el) => {
            const final = el.dataset.scrambleText || el.textContent;
            el.dataset.scrambleText = final;
            let iter = 0;
            clearInterval(el._sc);
            el._sc = setInterval(() => {
                el.textContent = final.split('').map((ch, i) =>
                    ch === ' ' ? ' ' : (i < iter ? final[i] : SC[Math.floor(Math.random() * SC.length)])
                ).join('');
                iter += final.length / 18;
                if (iter >= final.length) { clearInterval(el._sc); el.textContent = final; }
            }, 35);
        };
        document.querySelectorAll('[data-scramble]').forEach(el => {
            scramble(el);
            el.addEventListener('pointerenter', () => scramble(el));
        });
    }

    // ─── Hero protein/particle network (canvas) ───────────────────────────────
    const heroCanvas = document.getElementById('hero-net');
    if (heroCanvas) {
        const ctx = heroCanvas.getContext('2d');
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        const COUNT = window.innerWidth < 768 ? 26 : 52;
        const LINK = 140;
        const mouse = { x: -999, y: -999 };
        let w = 0, h = 0, nodes = [], animId = null;

        const resize = () => {
            const r = heroCanvas.getBoundingClientRect();
            w = r.width; h = r.height;
            heroCanvas.width = w * dpr; heroCanvas.height = h * dpr;
            ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        };
        const seed = () => {
            nodes = Array.from({ length: COUNT }, () => ({
                x: Math.random() * w, y: Math.random() * h,
                vx: (Math.random() - 0.5) * 0.32, vy: (Math.random() - 0.5) * 0.32,
            }));
        };
        const draw = () => {
            ctx.clearRect(0, 0, w, h);
            for (const n of nodes) {
                n.x += n.vx; n.y += n.vy;
                if (n.x < 0 || n.x > w) n.vx *= -1;
                if (n.y < 0 || n.y > h) n.vy *= -1;
                const dx = mouse.x - n.x, dy = mouse.y - n.y;
                if (dx * dx + dy * dy < 40000) { n.x += dx * 0.0009; n.y += dy * 0.0009; }
            }
            for (let i = 0; i < nodes.length; i++) {
                for (let j = i + 1; j < nodes.length; j++) {
                    const a = nodes[i], b = nodes[j];
                    const d = Math.hypot(a.x - b.x, a.y - b.y);
                    if (d < LINK) {
                        ctx.strokeStyle = `rgba(167,139,250,${(1 - d / LINK) * 0.45})`;
                        ctx.lineWidth = 1;
                        ctx.beginPath(); ctx.moveTo(a.x, a.y); ctx.lineTo(b.x, b.y); ctx.stroke();
                    }
                }
            }
            ctx.fillStyle = 'rgba(216,180,254,0.9)';
            for (const n of nodes) { ctx.beginPath(); ctx.arc(n.x, n.y, 1.7, 0, 6.2832); ctx.fill(); }
            animId = requestAnimationFrame(draw);
        };

        window.addEventListener('pointermove', (e) => {
            const r = heroCanvas.getBoundingClientRect();
            mouse.x = e.clientX - r.left; mouse.y = e.clientY - r.top;
        }, { passive: true });
        window.addEventListener('resize', () => { resize(); seed(); }, { passive: true });

        resize(); seed();
        if (reduceMotion) {
            draw(); cancelAnimationFrame(animId); animId = null;
        } else {
            const heroSection = heroCanvas.closest('section') || heroCanvas;
            new IntersectionObserver((entries) => {
                entries.forEach(en => {
                    if (en.isIntersecting && animId === null) draw();
                    else if (!en.isIntersecting && animId !== null) { cancelAnimationFrame(animId); animId = null; }
                });
            }, { threshold: 0 }).observe(heroSection);
        }
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
