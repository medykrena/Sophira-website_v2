/**
 * SOPHIRA.CH - JavaScript Consolidé
 * Version 2.0 - Optimisé et modulaire
 */

// ============================================
// 1. COOKIE CONSENT MANAGEMENT (RGPD/LPD)
// ============================================

const CookieConsent = {
  CONSENT_KEY: 'sophira_consent_v1',
  
  /**
   * Read consent preferences from localStorage
   */
  read() {
    try {
      return JSON.parse(localStorage.getItem(this.CONSENT_KEY)) || null;
    } catch (e) {
      console.error('Error reading consent:', e);
      return null;
    }
  },
  
  /**
   * Apply consent preferences to Google Analytics
   */
  applyToGtag(prefs) {
    if (typeof gtag === 'undefined') {
      console.warn('Google Analytics (gtag) not loaded');
      return;
    }
    
    const analyticsGranted = !!(prefs && prefs.analytics);
    gtag('consent', 'update', {
      analytics_storage: analyticsGranted ? 'granted' : 'denied',
      ad_storage: 'denied',
      ad_user_data: 'denied',
      ad_personalization: 'denied'
    });
  },
  
  /**
   * Accept analytics cookies
   */
  accept() {
    const prefs = {
      necessary: true,
      analytics: true,
      marketing: false,
      date: new Date().toISOString()
    };
    localStorage.setItem(this.CONSENT_KEY, JSON.stringify(prefs));
    this.applyToGtag(prefs);
    this.hideBanner();
  },
  
  /**
   * Refuse analytics cookies
   */
  refuse() {
    const prefs = {
      necessary: true,
      analytics: false,
      marketing: false,
      date: new Date().toISOString()
    };
    localStorage.setItem(this.CONSENT_KEY, JSON.stringify(prefs));
    this.applyToGtag(prefs);
    this.hideBanner();
  },
  
  /**
   * Show cookie banner
   */
  showBanner() {
    const banner = document.getElementById('cookie-banner');
    if (banner) {
      banner.style.display = 'block';
    }
  },
  
  /**
   * Hide cookie banner
   */
  hideBanner() {
    const banner = document.getElementById('cookie-banner');
    if (banner) {
      banner.style.display = 'none';
    }
  },
  
  /**
   * Initialize consent system
   */
  init() {
    const prefs = this.read();
    
    if (prefs) {
      // User has already made a choice
      this.applyToGtag(prefs);
      this.hideBanner();
    } else {
      // First visit - show banner
      this.showBanner();
    }
    
    // Attach event listeners
    const btnAccept = document.getElementById('cookie-accept');
    const btnRefuse = document.getElementById('cookie-refuse');
    const btnLater = document.getElementById('cookie-later');
    
    if (btnAccept) {
      btnAccept.addEventListener('click', () => this.accept());
    }
    if (btnRefuse) {
      btnRefuse.addEventListener('click', () => this.refuse());
    }
    if (btnLater) {
      btnLater.addEventListener('click', () => this.hideBanner());
    }
  }
};

// ============================================
// 2. NAVIGATION MANAGEMENT
// ============================================

const Navigation = {
  burger: null,
  mobilePanel: null,
  langBtn: null,
  langMenu: null,
  
  /**
   * Open mobile menu
   */
  openMobile() {
    if (!this.mobilePanel) return;
    
    this.mobilePanel.removeAttribute('hidden');
    this.mobilePanel.setAttribute('aria-hidden', 'false');
    
    if (this.burger) {
      this.burger.setAttribute('aria-expanded', 'true');
    }
    
    document.body.classList.add('no-scroll');
  },
  
  /**
   * Close mobile menu
   */
  closeMobile() {
    if (!this.mobilePanel) return;
    
    this.mobilePanel.setAttribute('hidden', '');
    this.mobilePanel.setAttribute('aria-hidden', 'true');
    
    if (this.burger) {
      this.burger.setAttribute('aria-expanded', 'false');
    }
    
    document.body.classList.remove('no-scroll');
  },
  
  /**
   * Toggle mobile menu
   */
  toggleMobile() {
    if (!this.mobilePanel) return;
    
    if (this.mobilePanel.hasAttribute('hidden')) {
      this.closeLang();
      this.openMobile();
    } else {
      this.closeMobile();
    }
  },
  
  /**
   * Open language menu
   */
  openLang() {
    if (!this.langMenu) return;
    
    this.langMenu.classList.add('open');
    this.langMenu.setAttribute('aria-hidden', 'false');
    
    if (this.langBtn) {
      this.langBtn.setAttribute('aria-expanded', 'true');
    }
  },
  
  /**
   * Close language menu
   */
  closeLang() {
    if (!this.langMenu) return;
    
    this.langMenu.classList.remove('open');
    this.langMenu.setAttribute('aria-hidden', 'true');
    
    if (this.langBtn) {
      this.langBtn.setAttribute('aria-expanded', 'false');
    }
  },
  
  /**
   * Toggle language menu
   */
  toggleLang(e) {
    e.stopPropagation();
    
    if (!this.langMenu) return;
    
    if (this.langMenu.classList.contains('open')) {
      this.closeLang();
    } else {
      this.closeMobile();
      this.openLang();
    }
  },
  
  /**
   * Handle click outside menus
   */
  handleOutsideClick(e) {
    // Close language menu if click outside
    if (this.langMenu && this.langMenu.classList.contains('open')) {
      const insideLang = this.langMenu.contains(e.target) || 
                        (this.langBtn && this.langBtn.contains(e.target));
      if (!insideLang) {
        this.closeLang();
      }
    }
    
    // Close mobile menu if click outside
    if (this.mobilePanel && !this.mobilePanel.hasAttribute('hidden')) {
      const insideMobile = this.mobilePanel.contains(e.target) || 
                          (this.burger && this.burger.contains(e.target));
      if (!insideMobile) {
        this.closeMobile();
      }
    }
  },
  
  /**
   * Handle escape key
   */
  handleEscape(e) {
    if (e.key === 'Escape') {
      this.closeLang();
      this.closeMobile();
    }
  },
  
  /**
   * Initialize navigation system
   */
  init() {
    // Get DOM elements
    this.burger = document.getElementById('burger');
    this.mobilePanel = document.getElementById('menu-mobile');
    this.langBtn = document.getElementById('lang-btn');
    this.langMenu = document.getElementById('lang-menu');
    
    // Attach event listeners
    if (this.burger && this.mobilePanel) {
      this.burger.addEventListener('click', () => this.toggleMobile());
    }
    
    if (this.langBtn && this.langMenu) {
      this.langBtn.addEventListener('click', (e) => this.toggleLang(e));
    }
    
    // Close menus on outside click
    document.addEventListener('click', (e) => this.handleOutsideClick(e));
    
    // Close menus on ESC key
    document.addEventListener('keydown', (e) => this.handleEscape(e));
  }
};

// ============================================
// 3. UTILITIES
// ============================================

const Utils = {
  /**
   * Check if user prefers reduced motion
   */
  prefersReducedMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  },
  
  /**
   * Smooth scroll to element
   */
  scrollTo(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
      const behavior = this.prefersReducedMotion() ? 'auto' : 'smooth';
      element.scrollIntoView({ behavior, block: 'start' });
    }
  },
  
  /**
   * Debounce function
   */
  debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
      const later = () => {
        clearTimeout(timeout);
        func(...args);
      };
      clearTimeout(timeout);
      timeout = setTimeout(later, wait);
    };
  }
};

// ============================================
// 4. INITIALIZATION
// ============================================

/**
 * Initialize all modules when DOM is ready
 */
function init() {
  // Initialize cookie consent
  CookieConsent.init();
  
  // Initialize navigation
  Navigation.init();
  
  // Log successful initialization (development only)
  if (window.location.hostname === 'localhost' || 
      window.location.hostname === '127.0.0.1') {
    console.log('✅ Sophira JS initialized');
  }
}

// Run initialization when DOM is fully loaded
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', init);
} else {
  // DOM already loaded
  init();
}

// Export for potential use in other scripts
window.Sophira = {
  CookieConsent,
  Navigation,
  Utils
};
