/**
 * JavaScript Optimizado para certificadoenergeticoalmeria.com
 * Archivo: main.js
 * Optimizado para Core Web Vitals y SEO
 */

// Configuración global
const CONFIG = {
    phone: '+34667451538',
    whatsapp: 'https://wa.me/34667451538',
    email: 'info@certificadoenergeticoalmeria.com',
    analytics: {
        trackCalls: true,
        trackWhatsApp: true,
        trackScrollDepth: true
    }
};

// Mobile Menu Toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navDesktop = document.querySelector('.nav-desktop');
    
    if (mobileMenuToggle && navDesktop) {
        mobileMenuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            navDesktop.classList.toggle('active');
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!mobileMenuToggle.contains(e.target) && !navDesktop.contains(e.target)) {
                mobileMenuToggle.classList.remove('active');
                navDesktop.classList.remove('active');
            }
        });
        
        // Close menu when clicking on a link
        const navLinks = navDesktop.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                mobileMenuToggle.classList.remove('active');
                navDesktop.classList.remove('active');
            });
        });
    }
});

// Utilidades de rendimiento
const Performance = {
    // Debounce function para optimizar eventos
    debounce(func, wait, immediate) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                timeout = null;
                if (!immediate) func(...args);
            };
            const callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func(...args);
        };
    },

    // Throttle function para scroll events
    throttle(func, limit) {
        let inThrottle;
        return function(...args) {
            if (!inThrottle) {
                func.apply(this, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        };
    },

    // Preload de recursos críticos
    preloadResource(href, as = 'fetch') {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.href = href;
        link.as = as;
        document.head.appendChild(link);
    },

    // Prefetch de páginas probables
    prefetchPage(href) {
        const link = document.createElement('link');
        link.rel = 'prefetch';
        link.href = href;
        document.head.appendChild(link);
    }
};

// Gestión de animaciones
const Animations = {
    // Intersection Observer para animaciones de entrada
    initScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    // Stagger animation delay
                    setTimeout(() => {
                        entry.target.classList.add('animate-in');
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, index * 100);
                    
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        // Observar elementos con clase fade-in
        document.querySelectorAll('.fade-in').forEach(el => {
            // Preparar elemento para animación
            el.style.opacity = '0';
            el.style.transform = 'translateY(30px)';
            el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
            
            observer.observe(el);
        });
    },

    // Smooth scroll para enlaces internos
    initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', (e) => {
                e.preventDefault();
                const target = document.querySelector(anchor.getAttribute('href'));
                
                if (target) {
                    const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
                    const targetPosition = target.offsetTop - headerHeight - 20;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }
};

// Optimizaciones de imágenes
const ImageOptimizer = {
    // Lazy loading con Intersection Observer
    initLazyLoading() {
        // Solo si el navegador no soporta loading="lazy" nativo
        if (!('loading' in HTMLImageElement.prototype)) {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        img.classList.add('loaded');
                        imageObserver.unobserve(img);
                    }
                });
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    },

    // Preload de imágenes críticas
    preloadCriticalImages() {
        const criticalImages = [
            '/wp-content/uploads/2025/01/9.jpg' // Imagen de Raúl Cañadas
        ];

        criticalImages.forEach(src => {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.href = src;
            link.as = 'image';
            document.head.appendChild(link);
        });
    }
};

// Analytics y tracking
const Analytics = {
    // Track de llamadas telefónicas
    trackPhoneCalls() {
        if (!CONFIG.analytics.trackCalls) return;
        
        document.querySelectorAll('a[href^="tel:"]').forEach(link => {
            link.addEventListener('click', () => {
                this.sendEvent('phone_call', {
                    phone_number: link.href.replace('tel:', ''),
                    source_page: window.location.pathname
                });
            });
        });
    },

    // Track de clicks en WhatsApp
    trackWhatsAppClicks() {
        if (!CONFIG.analytics.trackWhatsApp) return;
        
        document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp"]').forEach(link => {
            link.addEventListener('click', () => {
                this.sendEvent('whatsapp_click', {
                    source_page: window.location.pathname,
                    link_text: link.textContent.trim()
                });
            });
        });
    },

    // Track de profundidad de scroll
    trackScrollDepth() {
        if (!CONFIG.analytics.trackScrollDepth) return;
        
        const scrollThresholds = [25, 50, 75, 90];
        const trackedThresholds = new Set();
        
        const trackScrollHandler = Performance.throttle(() => {
            const scrollPercent = Math.round(
                (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100
            );
            
            scrollThresholds.forEach(threshold => {
                if (scrollPercent >= threshold && !trackedThresholds.has(threshold)) {
                    trackedThresholds.add(threshold);
                    this.sendEvent('scroll_depth', {
                        scroll_percent: threshold,
                        page: window.location.pathname
                    });
                }
            });
        }, 1000);
        
        window.addEventListener('scroll', trackScrollHandler, { passive: true });
    },

    // Enviar evento (compatible con GA4)
    sendEvent(eventName, parameters = {}) {
        // Google Analytics 4
        if (typeof gtag !== 'undefined') {
            gtag('event', eventName, parameters);
        }
        
        // Facebook Pixel
        if (typeof fbq !== 'undefined') {
            fbq('track', eventName, parameters);
        }
        
        // Console log para desarrollo
        console.log('Analytics Event:', eventName, parameters);
    }
};

// SEO y Core Web Vitals
const SEOOptimizer = {
    // Optimizar Core Web Vitals
    optimizeCoreWebVitals() {
        // Preload de recursos críticos
        const criticalResources = [
            { href: '/styles.css', as: 'style' },
            { href: CONFIG.whatsapp, as: 'fetch', crossorigin: 'anonymous' }
        ];
        
        criticalResources.forEach(resource => {
            Performance.preloadResource(resource.href, resource.as);
        });
        
        // Prefetch de páginas probables
        const likelyPages = [
            '/certificado-energetico-almeria/',
            '/certificado-energetico-roquetas-de-mar/',
            '/certificado-energetico-el-ejido/'
        ];
        
        likelyPages.forEach(page => {
            Performance.prefetchPage(page);
        });
    },

    // Mejorar LCP (Largest Contentful Paint)
    optimizeLCP() {
        // Preload de hero image si existe
        const heroImage = document.querySelector('.hero img, .professional-image img');
        if (heroImage && heroImage.src) {
            Performance.preloadResource(heroImage.src, 'image');
        }
        
        // Preload de fonts críticas
        const fontLink = document.createElement('link');
        fontLink.rel = 'preload';
        fontLink.href = 'https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap';
        fontLink.as = 'style';
        fontLink.onload = function() {
            this.onload = null;
            this.rel = 'stylesheet';
        };
        document.head.appendChild(fontLink);
    },

    // Optimizar CLS (Cumulative Layout Shift)
    optimizeCLS() {
        // Reservar espacio para imágenes
        const images = document.querySelectorAll('img:not([width]):not([height])');
        images.forEach(img => {
            // Establecer aspect ratio por defecto si no está definido
            if (!img.style.aspectRatio) {
                img.style.aspectRatio = '16 / 9';
            }
        });
        
        // Reservar espacio para contenido dinámico
        const dynamicElements = document.querySelectorAll('.testimonial, .card');
        dynamicElements.forEach(el => {
            if (!el.style.minHeight) {
                el.style.minHeight = '200px';
            }
        });
    }
};

// Funcionalidades de UX
const UXEnhancements = {
    // Inicializar tooltips y mejoras visuales
    initTooltips() {
        const tooltipElements = document.querySelectorAll('[data-tooltip]');
        tooltipElements.forEach(el => {
            el.addEventListener('mouseenter', this.showTooltip.bind(this));
            el.addEventListener('mouseleave', this.hideTooltip.bind(this));
        });
    },

    showTooltip(e) {
        const tooltip = document.createElement('div');
        tooltip.className = 'tooltip';
        tooltip.textContent = e.target.dataset.tooltip;
        tooltip.style.cssText = `
            position: absolute;
            background: #333;
            color: white;
            padding: 8px 12px;
            border-radius: 4px;
            font-size: 14px;
            z-index: 1000;
            pointer-events: none;
            opacity: 0;
            transition: opacity 0.3s ease;
        `;
        
        document.body.appendChild(tooltip);
        
        const rect = e.target.getBoundingClientRect();
        tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
        tooltip.style.top = rect.top - tooltip.offsetHeight - 8 + 'px';
        
        requestAnimationFrame(() => {
            tooltip.style.opacity = '1';
        });
        
        this.currentTooltip = tooltip;
    },

    hideTooltip() {
        if (this.currentTooltip) {
            this.currentTooltip.remove();
            this.currentTooltip = null;
        }
    },

    // Mejorar accesibilidad
    improveAccessibility() {
        // Añadir skip link
        const skipLink = document.createElement('a');
        skipLink.href = '#main-content';
        skipLink.textContent = 'Saltar al contenido principal';
        skipLink.className = 'skip-link';
        document.body.insertBefore(skipLink, document.body.firstChild);
        
        // Mejorar navegación por teclado
        this.improveKeyboardNavigation();
        
        // Añadir ARIA labels donde falten
        this.addAriaLabels();
    },

    improveKeyboardNavigation() {
        // Gestión de focus visible
        let hadKeyboardEvent = true;
        
        const keyboardEventHandler = () => hadKeyboardEvent = true;
        const mouseEventHandler = () => hadKeyboardEvent = false;
        
        document.addEventListener('keydown', keyboardEventHandler);
        document.addEventListener('mousedown', mouseEventHandler);
        
        document.addEventListener('focusin', (e) => {
            if (hadKeyboardEvent) {
                e.target.classList.add('focus-visible');
            }
        });
        
        document.addEventListener('focusout', (e) => {
            e.target.classList.remove('focus-visible');
        });
    },

    addAriaLabels() {
        // Añadir labels a botones de teléfono y WhatsApp
        document.querySelectorAll('a[href^="tel:"]').forEach(link => {
            if (!link.getAttribute('aria-label')) {
                link.setAttribute('aria-label', `Llamar al teléfono ${link.textContent.trim()}`);
            }
        });
        
        document.querySelectorAll('a[href*="wa.me"]').forEach(link => {
            if (!link.getAttribute('aria-label')) {
                link.setAttribute('aria-label', 'Contactar por WhatsApp');
            }
        });
    }
};

// Error handling y logging
const ErrorHandler = {
    init() {
        window.addEventListener('error', this.handleError.bind(this));
        window.addEventListener('unhandledrejection', this.handlePromiseRejection.bind(this));
    },

    handleError(event) {
        console.error('JavaScript Error:', {
            message: event.message,
            filename: event.filename,
            lineno: event.lineno,
            colno: event.colno,
            error: event.error
        });
        
        // Enviar error a servicio de logging si está configurado
        this.logError('javascript_error', {
            message: event.message,
            filename: event.filename,
            line: event.lineno
        });
    },

    handlePromiseRejection(event) {
        console.error('Unhandled Promise Rejection:', event.reason);
        
        this.logError('promise_rejection', {
            reason: event.reason?.toString()
        });
    },

    logError(type, details) {
        // Aquí se puede enviar a un servicio de logging como Sentry
        if (typeof gtag !== 'undefined') {
            gtag('event', 'exception', {
                description: `${type}: ${details.message || details.reason}`,
                fatal: false
            });
        }
    }
};

// Service Worker para caching
const ServiceWorkerManager = {
    init() {
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', () => {
                navigator.serviceWorker.register('/sw.js')
                    .then(registration => {
                        console.log('SW registered: ', registration);
                    })
                    .catch(registrationError => {
                        console.log('SW registration failed: ', registrationError);
                    });
            });
        }
    }
};

// Inicialización principal
class App {
    constructor() {
        this.init();
    }

    init() {
        // Esperar a que el DOM esté listo
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.initializeApp());
        } else {
            this.initializeApp();
        }
    }

    initializeApp() {
        console.log('🚀 Inicializando certificadoenergeticoalmeria.com');
        
        try {
            // Optimizaciones de rendimiento (críticas)
            SEOOptimizer.optimizeCoreWebVitals();
            SEOOptimizer.optimizeLCP();
            SEOOptimizer.optimizeCLS();
            
            // Funcionalidades de UX
            Animations.initScrollAnimations();
            Animations.initSmoothScroll();
            ImageOptimizer.initLazyLoading();
            ImageOptimizer.preloadCriticalImages();
            
            // Analytics y tracking
            Analytics.trackPhoneCalls();
            Analytics.trackWhatsAppClicks();
            Analytics.trackScrollDepth();
            
            // Mejoras de accesibilidad
            UXEnhancements.improveAccessibility();
            UXEnhancements.initTooltips();
            
            // Error handling
            ErrorHandler.init();
            
            // Service Worker (opcional)
            ServiceWorkerManager.init();
            
            console.log('✅ App inicializada correctamente');
            
        } catch (error) {
            console.error('❌ Error inicializando app:', error);
            ErrorHandler.handleError({ message: error.message, filename: 'main.js' });
        }
    }

    // Método público para tracking manual
    trackEvent(eventName, parameters) {
        Analytics.sendEvent(eventName, parameters);
    }
}

// Inicializar aplicación
const certificadoApp = new App();

// Exportar para uso global si es necesario
window.CertificadoApp = certificadoApp;

// Funciones de utilidad global
window.CertificadoUtils = {
    // Formatear teléfono para display
    formatPhone(phone) {
        return phone.replace(/(\d{3})(\d{2})(\d{2})(\d{2})/, '$1 $2 $3 $4');
    },
    
    // Generar mensaje de WhatsApp personalizado
    generateWhatsAppURL(municipio = '') {
        const message = municipio 
            ? `Hola, necesito un certificado energético en ${municipio}`
            : 'Hola, necesito un certificado energético';
        
        return `${CONFIG.whatsapp}?text=${encodeURIComponent(message)}`;
    },
    
    // Scroll suave a elemento
    scrollToElement(selector, offset = 0) {
        const element = document.querySelector(selector);
        if (element) {
            const headerHeight = document.querySelector('.header')?.offsetHeight || 0;
            const targetPosition = element.offsetTop - headerHeight - offset;
            
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    }
};

// Debug mode para desarrollo
if (window.location.hostname === 'localhost' || window.location.hostname.includes('dev')) {
    window.DEBUG_MODE = true;
    console.log('🔧 Modo debug activado');
    
    // Añadir estilos de debug
    const debugStyles = document.createElement('style');
    debugStyles.textContent = `
        .debug-grid { 
            background: repeating-linear-gradient(
                90deg,
                transparent,
                transparent 7px,
                rgba(255,0,0,0.1) 7px,
                rgba(255,0,0,0.1) 8px
            );
        }
    `;
    document.head.appendChild(debugStyles);
}