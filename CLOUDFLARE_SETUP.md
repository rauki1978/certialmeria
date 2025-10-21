# 🚀 Guía de Configuración Cloudflare Pages

## 📋 Resumen

Esta guía te ayudará a desplegar **CertiAlmería** en Cloudflare Pages conectado con GitHub para auto-deploy. Cada push a `main` actualizará automáticamente el sitio en producción.

**Repositorio GitHub:** https://github.com/rauki1978/certialmeria

---

## 🎯 Ventajas de Cloudflare Pages

- ✅ **CDN Global** - 275+ ubicaciones en todo el mundo
- ✅ **SSL Gratis** - Certificado SSL automático
- ✅ **Auto-Deploy** - Cada push a GitHub actualiza el sitio
- ✅ **Compresión Brotli** - 20-30% mejor que GZIP
- ✅ **HTTP/3 + 0-RTT** - Máxima velocidad
- ✅ **Minificación automática** - HTML/CSS/JS
- ✅ **Ilimitado ancho de banda** - Sin cargos por tráfico
- ✅ **Protección DDoS** - Incluida automáticamente

---

## 📝 PASO 1: Conectar GitHub con Cloudflare Pages

### 1.1 Acceder a Cloudflare Dashboard

1. Ve a https://dash.cloudflare.com/
2. Inicia sesión con tu cuenta de Cloudflare
3. En el menú lateral, haz clic en **"Pages"**
4. Haz clic en **"Create a project"**

### 1.2 Conectar con GitHub

1. Haz clic en **"Connect to Git"**
2. Selecciona **"GitHub"**
3. Autoriza Cloudflare para acceder a tu GitHub
4. Selecciona el repositorio: **`rauki1978/certialmeria`**

### 1.3 Configurar el Build

**Configuración del proyecto:**

```
Project name: certialmeria
Production branch: main
```

**Build settings:**

```
Framework preset: None (sitio estático HTML)
Build command: (dejar vacío)
Build output directory: /
Root directory: /
```

**Variables de entorno:** (ninguna necesaria)

Haz clic en **"Save and Deploy"**

---

## ⚙️ PASO 2: Configuración del Dominio

### 2.1 Añadir Dominio Personalizado

1. Una vez desplegado el proyecto, ve a **"Custom domains"**
2. Haz clic en **"Set up a custom domain"**
3. Introduce tu dominio: `certificadoenergeticoalmeria.com`
4. Cloudflare detectará automáticamente tu zona DNS
5. Haz clic en **"Activate domain"**

### 2.2 Configurar DNS (si es necesario)

Si tu dominio NO está en Cloudflare, necesitarás crear un registro CNAME:

```
Type: CNAME
Name: @ (o www)
Target: certialmeria.pages.dev
Proxy: Activado (nube naranja)
```

### 2.3 Forzar HTTPS

1. Ve a **Settings → General**
2. En **"Always use HTTPS"**, actívalo
3. Guarda cambios

---

## 🔧 PASO 3: Optimizaciones de Cloudflare Dashboard

### 3.1 Speed → Optimization

Activa las siguientes opciones:

```
✅ Auto Minify
   [x] JavaScript
   [x] CSS
   [x] HTML

✅ Brotli (compresión superior a GZIP)

✅ Early Hints (mejora FCP)

✅ Rocket Loader (opcional, puede causar conflictos)
   ⚠️ Probar primero, desactivar si hay problemas con JS
```

### 3.2 Caching → Configuration

```
Browser Cache TTL: 1 month
Caching Level: Standard
```

### 3.3 Security → Settings

```
✅ Security Level: Medium
✅ Challenge Passage: 30 minutes
✅ Browser Integrity Check: ON
```

---

## 📊 PASO 4: Page Rules (Opcional pero Recomendado)

Ve a **Rules → Page Rules** y crea estas reglas:

### Rule 1: Cache Everything para recursos estáticos

```
URL: *certificadoenergeticoalmeria.com/images/*

Settings:
- Cache Level: Cache Everything
- Edge Cache TTL: 1 month
- Browser Cache TTL: 1 month
```

### Rule 2: Cache Everything para CSS/JS

```
URL: *certificadoenergeticoalmeria.com/css/*

Settings:
- Cache Level: Cache Everything
- Edge Cache TTL: 1 month
- Browser Cache TTL: 1 month
```

### Rule 3: Forzar HTTPS

```
URL: http://*certificadoenergeticoalmeria.com/*

Settings:
- Always Use HTTPS: ON
```

---

## 🔐 PASO 5: Headers de Seguridad (Ya Configurados)

Los headers de seguridad están configurados en el archivo `_headers` del proyecto:

```
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
Referrer-Policy: strict-origin-when-cross-origin
```

Cloudflare los aplicará automáticamente. ✅

---

## 🌐 PASO 6: Configuración DNS Completa

Si gestionas DNS en Cloudflare, configura:

### Registros DNS Recomendados:

```
Type: CNAME
Name: @
Target: certialmeria.pages.dev
Proxy: ✅ Proxied (nube naranja)

Type: CNAME
Name: www
Target: certialmeria.pages.dev
Proxy: ✅ Proxied (nube naranja)
```

### Redirección WWW → No-WWW (o viceversa)

En **Rules → Redirect Rules**, crea:

```
Si: Hostname equals www.certificadoenergeticoalmeria.com
Entonces: Redirect to https://certificadoenergeticoalmeria.com$1
Status code: 301 (Permanent)
```

---

## 🚀 PASO 7: Deploy y Verificación

### 7.1 Verificar Deploy Exitoso

1. Ve a **Pages → certialmeria → Deployments**
2. Verifica que el último deploy tiene estado **"Success"** ✅
3. Haz clic en el deploy para ver detalles
4. Copia la URL: `https://certialmeria.pages.dev`
5. Ábrela en el navegador para verificar

### 7.2 Testing Checklist

Visita el sitio y verifica:

- [x] El sitio carga correctamente
- [x] Las imágenes WebP se muestran (inspecciona con DevTools)
- [x] HTTPS funciona (candado verde)
- [x] Redirección HTTP → HTTPS funciona
- [x] Headers de seguridad presentes (inspecciona con DevTools → Network)
- [x] Compresión Brotli activa (Network → Headers → `content-encoding: br`)

### 7.3 PageSpeed Test

1. Ve a https://pagespeed.web.dev/
2. Introduce: `https://certificadoenergeticoalmeria.com`
3. Verifica las puntuaciones:
   - **Mobile:** 90+ ✅
   - **Desktop:** 95+ ✅
   - **Core Web Vitals:** Todo verde ✅

---

## 🔄 PASO 8: Workflow de Desarrollo

### Flujo de trabajo automático:

```bash
# 1. Hacer cambios locales
# Editar archivos en local...

# 2. Commit de cambios
git add .
git commit -m "Descripción de cambios"

# 3. Push a GitHub
git push origin main

# 4. Cloudflare Pages auto-despliega ✅
# En 30-60 segundos el sitio estará actualizado
```

### Ver logs de deploy:

1. Dashboard → Pages → certialmeria
2. Haz clic en el último deployment
3. Ve la pestaña **"Build log"** para ver detalles

---

## 📈 PASO 9: Monitoreo y Analytics

### 9.1 Web Analytics (Gratis)

1. Ve a **Analytics & Logs → Web Analytics**
2. Haz clic en **"Enable Web Analytics"**
3. Copia el script y añádelo a `index.html` antes de `</head>`:

```html
<script defer src='https://static.cloudflareinsights.com/beacon.min.js'
        data-cf-beacon='{"token": "TU_TOKEN_AQUI"}'></script>
```

### 9.2 Métricas Disponibles

Cloudflare te mostrará:
- Page views
- Unique visitors
- Core Web Vitals (LCP, FID, CLS)
- Bandwidth usage
- Requests per day
- Top pages

---

## 🛠️ PASO 10: Troubleshooting

### Problema: El sitio no actualiza después de push

**Solución:**
1. Ve a Pages → Deployments
2. Verifica que hay un nuevo deployment en proceso
3. Si no hay deployment, haz clic en **"Retry deployment"**
4. Limpia cache de Cloudflare: **Caching → Configuration → Purge Everything**

### Problema: Imágenes WebP no se cargan

**Solución:**
1. Verifica que los archivos `.webp` están en GitHub
2. Chequea la consola del navegador (F12) para errores
3. Verifica que el path es correcto: `/images/nombre.webp`

### Problema: Headers personalizados no se aplican

**Solución:**
1. Verifica que el archivo `_headers` está en la raíz del proyecto
2. Revisa la sintaxis del archivo (sin errores)
3. Haz un nuevo deploy para aplicar cambios

### Problema: Redirecciones no funcionan

**Solución:**
1. Verifica el archivo `_redirects` en la raíz
2. Formato correcto: `origen destino código`
3. Espera propagación (1-2 minutos)

---

## 📊 Archivos de Configuración Incluidos

El proyecto incluye estos archivos para Cloudflare:

### `_headers`
- Headers de seguridad HTTP
- Configuración de cache por tipo de archivo
- CSP (Content Security Policy)
- CORS para fuentes

### `_redirects`
- Redirecciones 301 permanentes
- Compatible con formato Netlify/Cloudflare

### `.htaccess`
- Configuración Apache (solo si usas origen Apache)
- Cloudflare Pages NO usa .htaccess (usa `_headers` y `_redirects`)

---

## ✅ Checklist Final

Antes de considerar completada la configuración:

- [ ] Proyecto desplegado en Cloudflare Pages
- [ ] Dominio personalizado configurado y activo
- [ ] HTTPS forzado (HTTP redirige a HTTPS)
- [ ] Page Rules configuradas
- [ ] Auto Minify activado (HTML/CSS/JS)
- [ ] Brotli compression activado
- [ ] Headers de seguridad verificados
- [ ] DNS configurado correctamente
- [ ] PageSpeed score 90+ mobile y desktop
- [ ] Web Analytics habilitado
- [ ] Auto-deploy desde GitHub funcionando

---

## 🎯 Resultados Esperados

### Performance:

| Métrica | Antes | Con Cloudflare | Mejora |
|---------|-------|----------------|--------|
| **TTFB** | ~800ms | **< 200ms** | 75% ⚡ |
| **LCP** | ~3.5s | **< 1.8s** | 49% ⚡ |
| **FCP** | ~2.0s | **< 1.2s** | 40% ⚡ |
| **PageSpeed Mobile** | ~70 | **90+** | +20 pts |
| **PageSpeed Desktop** | ~85 | **95+** | +10 pts |

### Seguridad:
- ✅ SSL/TLS automático (Let's Encrypt)
- ✅ Protección DDoS
- ✅ WAF (Web Application Firewall)
- ✅ Headers de seguridad HTTP

### Disponibilidad:
- ✅ Uptime 99.99%
- ✅ CDN global (275+ PoPs)
- ✅ Failover automático

---

## 📞 Soporte

**Cloudflare Docs:** https://developers.cloudflare.com/pages/
**Cloudflare Community:** https://community.cloudflare.com/
**GitHub Repo:** https://github.com/rauki1978/certialmeria

---

## 🎉 ¡Listo para Producción!

Una vez completados todos los pasos, tu sitio estará:
- ⚡ **Ultra-rápido** (CDN global + Brotli + HTTP/3)
- 🔒 **Seguro** (SSL + Headers + DDoS protection)
- 🚀 **Auto-actualizable** (push to deploy)
- 📊 **Monitoreado** (Analytics integrado)

**¡CertiAlmería está listo para conquistar Google con puntuaciones perfectas en PageSpeed!** 🏆

---

*Última actualización: 2025-01-22*
*Proyecto: CertiAlmería → Cloudflare Pages Migration*
