document.addEventListener('DOMContentLoaded', () => {

  // --- Loader Hide ---
  const loader = document.getElementById('loader');
  if (loader) {
    // Add small delay to let Ken Burns initialized before show
    setTimeout(() => {
      loader.classList.add('hide-loader');
    }, 600);
  }

  // --- Mobile Nav Toggle ---
  const mobileBtn = document.querySelector('.mobile-menu-btn');
  const nav = document.querySelector('nav');

  if (mobileBtn && nav) {
    mobileBtn.addEventListener('click', () => {
      nav.classList.toggle('active');
      const icon = mobileBtn.querySelector('i');
      if (icon) {
        if (nav.classList.contains('active')) {
          icon.classList.remove('fa-bars');
          icon.classList.add('fa-times');
        } else {
          icon.classList.remove('fa-times');
          icon.classList.add('fa-bars');
        }
      }
    });
  }

  // --- Bilingual Toggle ---
  const langToggleBtn = document.getElementById('langToggle');
  let currentLang = localStorage.getItem('site_lang') || 'el';
  
  const applyLanguage = (lang) => {
    const translatableElements = document.querySelectorAll('[data-el]');
    translatableElements.forEach(el => {
      if (lang === 'en' && el.hasAttribute('data-en') && el.getAttribute('data-en') !== "") {
        el.innerHTML = el.getAttribute('data-en');
      } else {
        el.innerHTML = el.getAttribute('data-el');
      }
    });
    if (langToggleBtn) {
      langToggleBtn.textContent = lang === 'el' ? 'EN' : 'ΕΛ';
    }
    document.documentElement.lang = lang;
  };

  if (langToggleBtn) {
    langToggleBtn.addEventListener('click', () => {
      currentLang = currentLang === 'el' ? 'en' : 'el';
      localStorage.setItem('site_lang', currentLang);
      applyLanguage(currentLang);
    });
  }
  applyLanguage(currentLang);

  // --- Intersection Observer for Fade-In-Up ---
  const fadeElements = document.querySelectorAll('.fade-in-up');
  const observerOptions = { threshold: 0.1, rootMargin: "0px 0px -50px 0px" };
  const fadeObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  fadeElements.forEach(el => fadeObserver.observe(el));


  // --- Counter Animations ---
  const counters = document.querySelectorAll('.counter-value');
  const counterObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const target = +entry.target.getAttribute('data-target');
        const duration = 2000;
        const inc = target / (duration / 16); // 60 fps
        
        let current = 0;
        const updateCounter = () => {
          current += inc;
          if (current < target) {
            entry.target.innerText = Math.ceil(current);
            requestAnimationFrame(updateCounter);
          } else {
            entry.target.innerText = target;
          }
        };
        updateCounter();
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(counter => counterObserver.observe(counter));


  // --- Hero Slider with Ken Burns ---
  const slides = document.querySelectorAll('.hero-slide');
  if (slides.length > 0) {
    let currentSlide = 0;
    slides[currentSlide].classList.add('active');
    
    // Switch completely roughly 1s before the 10s Ken Burns ends, so visually fluid
    setInterval(() => {
      slides[currentSlide].classList.remove('active');
      currentSlide = (currentSlide + 1) % slides.length;
      
      // small delay to retrigger animation if classes were the same
      setTimeout(() => {
        slides[currentSlide].classList.add('active');
      }, 50);
    }, 8000); 
  }

  // --- Gallery Masonry Setup ---
  const galleryGrid = document.querySelector('.masonry-grid');
  const loadMoreBtn = document.getElementById('loadMoreGallery');
  
  if (galleryGrid && window.photoData) {
    let itemsLoaded = 0;
    const batchSize = 30; // Load 30 photos at a time
    const allImages = window.photoData.images; // Array of filenames

    const loadImages = () => {
      let limit = Math.min(itemsLoaded + batchSize, allImages.length);
      for (let i = itemsLoaded; i < limit; i++) {
        const itemDiv = document.createElement('div');
        itemDiv.className = 'masonry-item fade-in-up';
        
        const img = document.createElement('img');
        img.src = `Photos/${allImages[i]}`;
        img.loading = "lazy";
        img.alt = `Gallery Photo ${i}`;
        
        // Open lightbox event
        img.addEventListener('click', () => {
          openLightbox(`Photos/${allImages[i]}`);
        });

        itemDiv.appendChild(img);
        galleryGrid.appendChild(itemDiv);
        
        // Let intersection observer catch new content
        fadeObserver.observe(itemDiv);
      }
      itemsLoaded = limit;
      
      if (itemsLoaded >= allImages.length && loadMoreBtn) {
        loadMoreBtn.style.display = 'none';
      }
    };
    
    // Initial Load
    loadImages();
    
    if (loadMoreBtn) {
      loadMoreBtn.addEventListener('click', loadImages);
    }
  }

  // --- Lightbox Logic ---
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = document.getElementById('lightbox-img');
  const lightboxClose = document.getElementById('lightbox-close');

  const openLightbox = (src) => {
    if(!lightbox || !lightboxImg) return;
    lightboxImg.src = src;
    lightbox.classList.add('active');
  };

  if(lightboxClose) {
    lightboxClose.addEventListener('click', () => {
      lightbox.classList.remove('active');
      lightboxImg.src = '';
    });
  }
  
  if(lightbox) {
    lightbox.addEventListener('click', (e) => {
      if(e.target === lightbox) {
        lightbox.classList.remove('active');
        lightboxImg.src = '';
      }
    });
  }

});
