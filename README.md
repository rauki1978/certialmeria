# CertiAlmería - Certificados Energéticos Almería

[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)](https://html.spec.whatwg.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

Sitio web profesional optimizado para SEO de **CertiAlmería**, servicio de certificación energética en la provincia de Almería, España.

## 📋 Descripción del Proyecto

CertiAlmería es un sitio web estático multi-página diseñado para posicionar como líder en certificación energética en Almería. Ofrece información detallada sobre certificados energéticos, precios, servicios por municipio y contenido educativo SEO-optimizado.

**Profesional:** Raúl Cañadas Navarro
**Credencial:** Arquitecto Técnico COAAT Almería 1.440
**Experiencia:** 20 años - 1.800+ certificados realizados

## 🎯 Características Principales

### ✅ Optimización SEO Agresiva
- **112+ páginas indexables** con contenido único
- **104 páginas municipales** geo-localizadas (pueblos de Almería)
- **30 artículos de blog** long-tail optimizados (400-600 palabras c/u)
- Schema.org markup completo (LocalBusiness, Article, FAQPage)
- Meta tags optimizados para cada página
- Sitemap.xml estructurado con prioridades estratégicas

### 🎨 Diseño Moderno y Responsive
- Mobile-first design
- TailwindCSS para estilos consistentes
- Efectos visuales (parallax, gradientes, animaciones)
- Navegación adaptativa con menú hamburguesa
- Hero sections con CTAs optimizados

### 🚀 Performance Optimizado
- HTML/CSS/JS vanilla (sin frameworks pesados)
- Lazy loading de imágenes
- WebP detection automática
- Preload de recursos críticos
- Core Web Vitals optimizados

### 📊 Herramientas Interactivas
- Calculadora de precio certificado energético (superficie + tipo inmueble)
- Calculadora de caducidad (con variable de calificación energética)
- Formularios de contacto con validación
- CTAs WhatsApp directos

## 📁 Estructura del Proyecto

```
CERTIALMERIA/
├── index.html                          # Homepage principal
├── sitemap.xml                         # Mapa del sitio
├── robots.txt                          # Instrucciones crawlers
├── .gitignore                          # Exclusiones Git
├── README.md                           # Este archivo
│
├── css/
│   └── tailwind.min.css                # TailwindCSS compilado
│
├── images/                             # Imágenes y recursos visuales
│   ├── hero-bg.jpg                     # Background principal
│   ├── logo.png                        # Logo CertiAlmería
│   └── ...
│
├── blog/                               # 30 artículos SEO
│   ├── arquitecto-tecnico-vs-ingeniero-certificado/
│   ├── certificado-energetico-24-horas-posible/
│   ├── certificado-energetico-alquiler-turistico/
│   ├── multas-certificado-energetico-2025/
│   ├── precio-certificado-energetico-2025/
│   └── ... (26 artículos más)
│
├── municipios/                         # 104 páginas municipales
│   ├── almeria/
│   ├── roquetas-de-mar/
│   ├── el-ejido/
│   ├── nijar/
│   └── ... (100 municipios más)
│
├── pages/                              # Páginas estratégicas SEO
│   ├── certificado-energetico/         # Keyword principal (74K búsquedas/mes)
│   ├── certificado-energetico-barato/  # 18K búsquedas/mes
│   ├── vs-certicalia/                  # Intercepción competencia
│   ├── vs-tinsa/
│   ├── certificado-energetico-rapido/
│   └── calculadora-precio-certificado-energetico/
│
├── aviso-legal/                        # Páginas legales
├── politica-privacidad/
├── politica-cookies/
└── arquitecto-tecnico-coaat-1440/      # Página credenciales
```

## 🛠️ Stack Tecnológico

| Tecnología | Versión | Uso |
|------------|---------|-----|
| **HTML5** | - | Estructura semántica |
| **TailwindCSS** | 3.x | Sistema de diseño y estilos |
| **JavaScript** | ES6+ | Interactividad (calculadoras, menús, validación) |
| **Schema.org** | JSON-LD | Markup estructurado para SEO |
| **Google Fonts** | - | Tipografía Montserrat |

### Sin dependencias de build:
- ✅ No requiere Node.js para deployment
- ✅ No requiere compilación
- ✅ Archivos estáticos listos para servir
- ✅ Compatible con cualquier hosting estático

## 🎯 Keywords Objetivo

### Alto Volumen
- `certificado energético` → 74,000 búsquedas/mes
- `certificado energético barato` → 18,000 búsquedas/mes
- `precio certificado energético` → 12,000 búsquedas/mes
- `certificado energético rápido` → 6,800 búsquedas/mes

### Geo-targeting
- `certificado energético almería`
- `certificado energético roquetas de mar`
- `certificado energético el ejido`
- + 101 municipios más

### Long-tail
- `certificado energético 75 euros`
- `certificado energético 24 horas`
- `arquitecto técnico certificado energético`
- `multas certificado energético 2025`

**Total volumen objetivo:** ~120,000 búsquedas/mes combinadas

## 📈 Estrategia SEO Implementada

1. **Dual Targeting:** Geo-local (Almería) + Nacional (no-geo keywords)
2. **Intercepción competencia:** Páginas vs-certicalia, vs-tinsa
3. **Long-tail masivo:** 30 artículos respondiendo queries específicas
4. **Enlazado interno:** Red de enlaces cruzados entre páginas
5. **Schema markup:** LocalBusiness + Article + FAQPage
6. **Core Web Vitals:** Performance optimizado

## 🚀 Instrucciones de Deployment

### Opción 1: Hosting Estático (Recomendado)

**Netlify / Vercel / GitHub Pages:**

```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/certialmeria.git

# 2. Configurar dominio personalizado en el panel del hosting
# Apuntar DNS: www.certialmeria.es

# 3. Deploy automático (push to main)
git push origin main
```

**Configuración DNS:**
```
A Record: @ → IP del hosting
CNAME: www → dominio-hosting.netlify.app
```

### Opción 2: Servidor tradicional (Apache/Nginx)

**Apache (.htaccess):**
```apache
# Redirect www a non-www
RewriteEngine On
RewriteCond %{HTTP_HOST} ^www\.certialmeria\.es [NC]
RewriteRule ^(.*)$ https://certialmeria.es/$1 [L,R=301]

# Comprimir archivos
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/css application/javascript
</IfModule>

# Cache control
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpg "access plus 1 year"
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
</IfModule>
```

**Nginx:**
```nginx
server {
    listen 80;
    server_name certialmeria.es www.certialmeria.es;
    root /var/www/certialmeria;
    index index.html;

    # Comprimir
    gzip on;
    gzip_types text/css application/javascript image/svg+xml;

    # Cache
    location ~* \.(jpg|jpeg|png|gif|ico|css|js)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### Opción 3: Local (desarrollo)

```bash
# Servidor Python simple
cd CERTIALMERIA
python -m http.server 8000

# Abrir en navegador
# http://localhost:8000
```

## 📊 Métricas del Proyecto

- **Total páginas:** 159 HTML
- **Artículos blog:** 30
- **Páginas municipales:** 104
- **Páginas estratégicas:** 10+
- **Tamaño total:** ~25 MB (con imágenes)
- **Tiempo carga:** <2s (homepage)
- **Lighthouse Score:** 90+ (Performance, SEO, Accessibility)

## 🔧 Mantenimiento

### Añadir nuevo municipio:
```bash
# 1. Crear carpeta
mkdir municipios/nuevo-municipio

# 2. Copiar template
cp municipios/_template/index.html municipios/nuevo-municipio/

# 3. Personalizar contenido (título, H1, meta description)

# 4. Actualizar sitemap.xml
```

### Añadir nuevo artículo blog:
```bash
# 1. Crear carpeta
mkdir blog/nuevo-articulo

# 2. Copiar template blog
cp blog/_template/index.html blog/nuevo-articulo/

# 3. Escribir contenido SEO-optimizado (400-600 palabras)

# 4. Actualizar enlaces internos en otros artículos
```

## 📞 Contacto

**Raúl Cañadas Navarro**
Arquitecto Técnico COAAT Almería 1.440

- 📱 Teléfono: 667 451 538
- 📧 Email: info@certialmeria.es
- 🌐 Web: [www.certialmeria.es](https://www.certialmeria.es)
- 📍 Almería, Andalucía, España

## 📄 Licencia

Proyecto propietario de CertiAlmería © 2025. Todos los derechos reservados.

---

**Desarrollado con ❤️ para el sector de la certificación energética en Almería**
