document.addEventListener('DOMContentLoaded', () => {

    // ══════════════════════════════════════════════════════════
    // BILINGUAL SYSTEM (EL / EN)
    // ══════════════════════════════════════════════════════════
    const langToggleTrigger = document.getElementById('lang-toggle');
    let currentLang = localStorage.getItem('kdif_lang') || 'el';

    const translations = {
        'header-support': { el: 'ΣΤΗΡΙΞΤΕ ΜΑΣ',   en: 'SUPPORT US' },
        'menu-btn':       { el: 'ΜΕΝΟΥ',            en: 'MENU' },
        'nav-home':       { el: 'ΑΡΧΙΚΗ',           en: 'HOME' },
        'nav-programs':   { el: 'ΤΙ ΚΑΝΟΥΜΕ',       en: 'WHAT WE DO' },
        'nav-about':      { el: 'ΠΟΙΟΙ ΕΙΜΑΣΤΕ',    en: 'ABOUT US' },
        'nav-news':       { el: 'ΤΑ ΝΕΑ ΜΑΣ',       en: 'OUR NEWS' },
        'nav-contact':    { el: 'ΕΠΙΚΟΙΝΩΝΙΑ',      en: 'CONTACT' },
        'nav-support':    { el: 'ΣΤΗΡΙΞΤΕ ΜΑΣ',    en: 'SUPPORT US' }
    };

    const updateLanguage = (lang) => {
        // data-el / data-en elements
        document.querySelectorAll('[data-el]').forEach(el => {
            el.textContent = (lang === 'el')
                ? el.getAttribute('data-el')
                : el.getAttribute('data-en');
        });

        // data-i18n elements
        document.querySelectorAll('[data-i18n]').forEach(el => {
            const key = el.getAttribute('data-i18n');
            if (translations[key]) {
                el.textContent = translations[key][lang];
            }
        });

        // data-placeholder-el / data-placeholder-en inputs
        document.querySelectorAll('[data-placeholder-el]').forEach(el => {
            el.placeholder = (lang === 'el')
                ? el.getAttribute('data-placeholder-el')
                : el.getAttribute('data-placeholder-en');
        });

        // Update indicators
        const overlayLangStatus = document.getElementById('overlay-lang-status');
        if (overlayLangStatus) {
            overlayLangStatus.textContent = (lang === 'el') ? 'GR' : 'EN';
        }
        if (langToggleTrigger) {
            langToggleTrigger.textContent = (lang === 'el') ? 'EN' : 'EL';
        }
        document.documentElement.lang = lang;
        localStorage.setItem('kdif_lang', lang);
    };

    if (langToggleTrigger) {
        langToggleTrigger.addEventListener('click', () => {
            currentLang = (currentLang === 'el') ? 'en' : 'el';
            updateLanguage(currentLang);
        });
    }
    updateLanguage(currentLang);

    // Newsletter email validation — bilingual custom message
    document.querySelectorAll('.newsletter-form input[type="email"]').forEach(input => {
        input.addEventListener('invalid', () => {
            const lang = localStorage.getItem('kdif_lang') || 'el';
            input.setCustomValidity(
                lang === 'el' ? 'Παρακαλώ εισάγετε το email σας' : 'Please enter your email address'
            );
        });
        input.addEventListener('input', () => input.setCustomValidity(''));
    });


    // ══════════════════════════════════════════════════════════
    // HEADER — Scroll shrink + transparent mode for home hero
    // ══════════════════════════════════════════════════════════
    const header = document.getElementById('site-header');
    const homeHero = document.querySelector('.home-hero');

    if (header) {
        const updateHeader = () => {
            header.classList.toggle('scrolled', window.scrollY > 60);
        };

        window.addEventListener('scroll', updateHeader, { passive: true });
        updateHeader();
    }


    // ══════════════════════════════════════════════════════════
    // NAV OVERLAY — open / close
    // ══════════════════════════════════════════════════════════
    const menuOpen  = document.getElementById('menu-open');
    const menuClose = document.getElementById('nav-close');
    const navOverlay = document.getElementById('nav-overlay');

    const openNav = () => {
        if (!navOverlay) return;
        navOverlay.classList.add('open');
        document.body.style.overflow = 'hidden';
    };
    const closeNav = () => {
        if (!navOverlay) return;
        navOverlay.classList.remove('open');
        document.body.style.overflow = '';
    };

    menuOpen  && menuOpen.addEventListener('click', openNav);
    menuClose && menuClose.addEventListener('click', closeNav);

    // Close on any nav link click
    document.querySelectorAll('.overlay-nav a').forEach(link =>
        link.addEventListener('click', closeNav)
    );

    // Close on Escape key
    document.addEventListener('keydown', e => {
        if (e.key === 'Escape' && navOverlay?.classList.contains('open')) closeNav();
    });


    // ══════════════════════════════════════════════════════════
    // ACCORDION
    // ══════════════════════════════════════════════════════════
    document.querySelectorAll('.accordion-item').forEach(item => {
        const accHeader = item.querySelector('.accordion-header');
        if (!accHeader) return;

        accHeader.addEventListener('click', () => {
            const isActive = item.classList.contains('active');

            // Close all
            document.querySelectorAll('.accordion-item').forEach(acc =>
                acc.classList.remove('active')
            );

            // Toggle clicked (open if was closed)
            if (!isActive) item.classList.add('active');
        });
    });


    // ══════════════════════════════════════════════════════════
    // SCROLL REVEAL — IntersectionObserver
    // ══════════════════════════════════════════════════════════
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;

            const el     = entry.target;
            const delay  = [...el.classList].find(c => c.startsWith('reveal-delay-'));
            const ms     = delay ? parseInt(delay.split('-')[2]) * 130 : 0;

            setTimeout(() => el.classList.add('visible'), ms);

            // Trigger counters that are direct descendants
            el.querySelectorAll('.counter').forEach(counter => {
                if (!counter.dataset.started) {
                    setTimeout(() => startCounter(counter), ms + 200);
                }
            });

            // If the element itself is a counter
            if (el.classList.contains('counter') && !el.dataset.started) {
                setTimeout(() => startCounter(el), ms + 200);
            }

            revealObserver.unobserve(el);
        });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));


    // ══════════════════════════════════════════════════════════
    // COUNTER ANIMATION
    // ══════════════════════════════════════════════════════════
    function startCounter(el) {
        el.dataset.started = 'true';
        const target   = parseInt(el.getAttribute('data-target'));
        if (isNaN(target)) return;

        const duration = 2400;
        const step     = target / (duration / 16);
        let current    = 0;

        const update = () => {
            current += step;
            if (current < target) {
                el.textContent = Math.floor(current);
                requestAnimationFrame(update);
            } else {
                el.textContent = target;
            }
        };
        update();
    }


    // ══════════════════════════════════════════════════════════
    // BACK TO TOP
    // ══════════════════════════════════════════════════════════
    const backToTop = document.getElementById('back-to-top');
    if (backToTop) {
        window.addEventListener('scroll', () => {
            backToTop.classList.toggle('visible', window.scrollY > 500);
        }, { passive: true });

        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }


    // ══════════════════════════════════════════════════════════
    // LOADER (if present)
    // ══════════════════════════════════════════════════════════
    const loader    = document.getElementById('loader');
    const loaderBar = document.querySelector('.loader-bar');

    if (loader) {
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 35;
            if (progress >= 100) {
                progress = 100;
                clearInterval(interval);
                setTimeout(() => loader.classList.add('hidden'), 400);
            }
            if (loaderBar) loaderBar.style.width = progress + '%';
        }, 80);
    }


    // ══════════════════════════════════════════════════════════
    // HERO SLIDER (legacy, if slides exist)
    // ══════════════════════════════════════════════════════════
    const slides = document.querySelectorAll('.hero-slide');
    if (slides.length > 0) {
        let current = 0;
        slides[current].classList.add('active');
        setInterval(() => {
            slides[current].classList.remove('active');
            current = (current + 1) % slides.length;
            slides[current].classList.add('active');
        }, 5500);
    }

});
