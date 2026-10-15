/**
 * Service Worker para certificadoenergeticoalmeria.com
 * Archivo: sw.js
 * Optimizado para velocidad y experiencia offline
 */

const CACHE_NAME = 'certificado-energetico-v1.0.0';
const STATIC_CACHE = 'static-v1.0.0';
const DYNAMIC_CACHE = 'dynamic-v1.0.0';

// Recursos críticos para cachear inmediatamente
const STATIC_ASSETS = [
    '/',
    '/styles.css',
    '/main.js',
    '/manifest.json',
    '/wp-content/uploads/2025/01/9.jpg', // Imagen de Raúl Cañadas
    // Añadir más recursos estáticos críticos
];

// Rutas de páginas principales para cachear
const PAGE_ROUTES = [
    '/',
    '/certificado-energetico-almeria/',
    '/certificado-energetico-roquetas-de-mar/',
    '/certificado-energetico-el-ejido/',
    '/certificado-energetico-nijar/',
    '/certificado-energetico-vera/'
];

// URLs que nunca deben cachearse
const NEVER_CACHE = [
    '/admin/',
    '/wp-admin/',
    '/wp-login.php',
    'chrome-extension://',
    'analytics.google.com',
    'googletagmanager.com'
];

// Instalación del Service Worker
self.addEventListener('install', (event) => {
    console.log('🔧 Service Worker: Installing...');
    
    event.waitUntil(
        caches.open(STATIC_CACHE)
            .then((cache) => {
                console.log('📦 Service Worker: Precaching static assets');
                return cache.addAll(STATIC_ASSETS);
            })
            .then(() => {
                console.log('✅ Service Worker: Installation complete');
                return self.skipWaiting(); // Activar inmediatamente
            })
            .catch((error) => {
                console.error('❌ Service Worker: Installation failed', error);
            })
    );
});

// Activación del Service Worker
self.addEventListener('activate', (event) => {
    console.log('🚀 Service Worker: Activating...');
    
    event.waitUntil(
        // Limpiar caches antiguos
        caches.keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames.map((cacheName) => {
                        if (cacheName !== STATIC_CACHE && 
                            cacheName !== DYNAMIC_CACHE && 
                            cacheName !== CACHE_NAME) {
                            console.log('🗑️ Service Worker: Deleting old cache', cacheName);
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
            .then(() => {
                console.log('✅ Service Worker: Activation complete');
                return self.clients.claim(); // Tomar control inmediatamente
            })
    );
});

// Interceptar requests
self.addEventListener('fetch', (event) => {
    const { request } = event;
    const url = new URL(request.url);

    // Solo se gestionan las peticiones GET de la propia web. Las de otros
    // dominios (Google Ads, Meta, fuentes de Google...) van directas al
    // navegador: si pasaban por aquí, el service worker las repetía bajo su
    // propia CSP, fallaban y devolvía «503 sin conexión». Así se perdían el
    // píxel de Meta, las conversiones de Ads y la fuente Montserrat en todas
    // las páginas visitadas después de la portada (15/10/2026).
    if (url.origin !== self.location.origin || request.method !== 'GET') {
        return;
    }

    // Ignorar requests que no deben cachearse
    if (shouldNeverCache(url)) {
        return;
    }
    
    // Estrategia diferente según el tipo de recurso
    if (isStaticAsset(url)) {
        event.respondWith(cacheFirstStrategy(request));
    } else if (isPageRequest(request)) {
        event.respondWith(staleWhileRevalidateStrategy(request));
    } else if (isAPIRequest(url)) {
        event.respondWith(networkFirstStrategy(request));
    } else {
        event.respondWith(networkFirstStrategy(request));
    }
});

// Estrategias de caching

/**
 * Cache First: Para recursos estáticos que no cambian
 */
async function cacheFirstStrategy(request) {
    try {
        const cachedResponse = await caches.match(request);
        if (cachedResponse) {
            return cachedResponse;
        }
        
        const networkResponse = await fetch(request);
        if (networkResponse.ok) {
            const cache = await caches.open(STATIC_CACHE);
            cache.put(request, networkResponse.clone());
        }
        
        return networkResponse;
    } catch (error) {
        console.error('Cache First Strategy failed:', error);
        return new Response('Offline', { status: 503 });
    }
}

/**
 * Stale While Revalidate: Para páginas HTML
 */
async function staleWhileRevalidateStrategy(request) {
    const cache = await caches.open(DYNAMIC_CACHE);
    const cachedResponse = await cache.match(request);
    
    const fetchPromise = fetch(request)
        .then((networkResponse) => {
            if (networkResponse.ok) {
                cache.put(request, networkResponse.clone());
            }
            return networkResponse;
        })
        .catch(() => cachedResponse || createOfflinePage());
    
    return cachedResponse || await fetchPromise;
}

/**
 * Network First: Para APIs y contenido dinámico
 */
async function networkFirstStrategy(request) {
    try {
        const networkResponse = await fetch(request);
        
        if (networkResponse.ok && request.method === 'GET') {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, networkResponse.clone());
        }
        
        return networkResponse;
    } catch (error) {
        const cachedResponse = await caches.match(request);
        return cachedResponse || createOfflineResponse();
    }
}

// Funciones de utilidad

function shouldNeverCache(url) {
    return NEVER_CACHE.some(pattern => url.href.includes(pattern)) ||
           url.protocol === 'chrome-extension:' ||
           url.protocol === 'moz-extension:';
}

function isStaticAsset(url) {
    const staticExtensions = ['.css', '.js', '.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.woff', '.woff2'];
    return staticExtensions.some(ext => url.pathname.endsWith(ext));
}

function isPageRequest(request) {
    return request.method === 'GET' && 
           request.headers.get('accept')?.includes('text/html');
}

function isAPIRequest(url) {
    return url.pathname.includes('/api/') || 
           url.pathname.includes('/wp-json/');
}

function createOfflinePage() {
    return new Response(`
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Sin conexión - Certificado Energético Almería</title>
            <style>
                body {
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    text-align: center;
                    padding: 2rem;
                    background: #f8f9fa;
                }
                .offline-container {
                    max-width: 500px;
                    margin: 0 auto;
                    background: white;
                    padding: 3rem;
                    border-radius: 15px;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
                }
                .offline-icon {
                    font-size: 4rem;
                    margin-bottom: 2rem;
                }
                h1 {
                    color: #2c5aa0;
                    margin-bottom: 1rem;
                }
                p {
                    color: #666;
                    margin-bottom: 2rem;
                    line-height: 1.6;
                }
                .contact-info {
                    background: #f8f9fa;
                    padding: 1.5rem;
                    border-radius: 8px;
                    margin-top: 2rem;
                }
                .phone {
                    font-size: 1.2rem;
                    font-weight: bold;
                    color: #2c5aa0;
                }
            </style>
        </head>
        <body>
            <div class="offline-container">
                <div class="offline-icon">📱</div>
                <h1>Sin conexión a Internet</h1>
                <p>No se puede conectar con nuestro sitio web en este momento. Pero puede contactarnos directamente:</p>
                
                <div class="contact-info">
                    <div class="phone">📞 667 45 15 38</div>
                    <p>Raúl Cañadas Navarro<br>Arquitecto Técnico Colegiado</p>
                </div>
                
                <button onclick="window.location.reload()" style="
                    background: #ff6b35;
                    color: white;
                    border: none;
                    padding: 1rem 2rem;
                    border-radius: 25px;
                    font-size: 1rem;
                    cursor: pointer;
                    margin-top: 2rem;
                ">
                    Reintentar conexión
                </button>
            </div>
        </body>
        </html>
    `, {
        headers: {
            'Content-Type': 'text/html; charset=utf-8'
        }
    });
}

function createOfflineResponse() {
    return new Response(JSON.stringify({
        error: 'Sin conexión',
        message: 'No hay conexión a Internet disponible',
        contact: {
            phone: '667451538',
            whatsapp: 'https://wa.me/34667451538'
        }
    }), {
        headers: {
            'Content-Type': 'application/json; charset=utf-8'
        },
        status: 503
    });
}

// Background Sync para formularios (si se implementan)
self.addEventListener('sync', (event) => {
    if (event.tag === 'contact-form') {
        event.waitUntil(syncContactForm());
    }
});

async function syncContactForm() {
    try {
        // Recuperar datos guardados del IndexedDB
        const formData = await getStoredFormData();
        
        if (formData.length > 0) {
            for (const data of formData) {
                await submitFormData(data);
                await removeStoredFormData(data.id);
            }
        }
    } catch (error) {
        console.error('Error syncing form data:', error);
    }
}

// Push notifications (opcional, para futuro)
self.addEventListener('push', (event) => {
    if (!event.data) return;
    
    const data = event.data.json();
    const options = {
        body: data.body,
        icon: '/icon-192x192.png',
        badge: '/icon-badge-72x72.png',
        tag: 'certificado-notification',
        requireInteraction: true,
        actions: [
            {
                action: 'call',
                title: 'Llamar ahora',
                icon: '/icon-call.png'
            },
            {
                action: 'whatsapp',
                title: 'WhatsApp',
                icon: '/icon-whatsapp.png'
            }
        ]
    };
    
    event.waitUntil(
        self.registration.showNotification(data.title, options)
    );
});

// Manejar clicks en notificaciones
self.addEventListener('notificationclick', (event) => {
    event.notification.close();
    
    let url = '/';
    
    switch (event.action) {
        case 'call':
            url = 'tel:+34667451538';
            break;
        case 'whatsapp':
            url = 'https://wa.me/34667451538';
            break;
        default:
            url = '/';
    }
    
    event.waitUntil(
        clients.openWindow(url)
    );
});

// Cleanup de cache periódico
self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'CLEAN_CACHE') {
        event.waitUntil(cleanOldCaches());
    }
});

async function cleanOldCaches() {
    const cacheNames = await caches.keys();
    const cachesToDelete = cacheNames.filter(name => 
        !name.includes(CACHE_NAME.split('-v')[0])
    );
    
    await Promise.all(
        cachesToDelete.map(name => caches.delete(name))
    );
    
    console.log('🧹 Old caches cleaned');
}

// Funciones para IndexedDB (para background sync)
async function getStoredFormData() {
    // Implementar según necesidades
    return [];
}

async function submitFormData(data) {
    // Implementar envío de formulario
    return fetch('/api/contact', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    });
}

async function removeStoredFormData(id) {
    // Implementar eliminación de IndexedDB
    return true;
}

// Log de eventos importantes
console.log('📋 Service Worker loaded for certificadoenergeticoalmeria.com');