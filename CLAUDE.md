# CertiAlmería — Instrucciones del proyecto

**Negocio:** certificados de eficiencia energética. Raúl Cañadas Navarro, Arquitecto Técnico, COAAT Almería nº 1.440.
**Prioridad comercial:** Almería capital y periferia.
**Objetivo:** más certificados vendidos y rentables. No más tráfico, no más páginas.

> Última actualización: 2026-09-22 (tras la auditoría inicial)

---

## Antes de tocar nada, leer esto

La documentación de negocio y marketing vive en `docs/marketing/`:

| Archivo | Para qué |
|---|---|
| `negocio.md` | **Hechos verificados** y preguntas pendientes. Si un dato no está aquí, no se publica |
| `auditoria-inicial.md` | Los 18 hallazgos con su evidencia y severidad |
| `medicion.md` | Embudo de visita → consulta → cliente → venta |
| `backlog.md` | Tareas priorizadas con criterio de finalización |
| `plan-90-dias.md` | Fases y entregables |
| `decisiones.md` | Decisiones tomadas **y su motivo**. Añadir una entrada al decidir algo relevante |
| `integracion-app.md` | Contrato con `cee.certialmeria.es`: qué manda la web y qué falta en la aplicación |

---

## Arquitectura

- **HTML estático**, sin sistema de compilación. 156 páginas publicadas.
- **Cloudflare Pages**, despliegue automático al hacer push a `main`. Dominio: `www.certialmeria.es`.
- La configuración real de servidor está en **`_headers`** y **`_redirects`**. ⚠️ `.htaccess` existe pero **Cloudflare Pages no lo lee**: editarlo no surte ningún efecto.
- Tailwind **precompilado** en `/css/tailwind.min.css`. La `tailwind.config` en línea **no tiene efecto** sin el CDN.
- Portada: `index.html` (~4.000 líneas, CSS y JS en línea). 103 páginas de municipio en `municipios/`, 31 artículos en `blog/`.
- Archivos UTF-8 con final de línea LF.

### Formularios y datos
- Portada: formulario asistido con id **`#wizard-form`**, 4 pasos (`totalSteps = 4`). El JS busca ese id exacto.
- Las otras 155 páginas: formulario compartido inyectado por **`/js/lead-form.js`**.
- Los interesados van a **dos destinos a la vez**: la app propia (`cee.certialmeria.es/api/interesados`) **y** copia por email vía Web3Forms. Basta que una funcione. Antispam: Cloudflare Turnstile.
- **Esto funciona bien. No simplificarlo a un solo destino.**
- El asistente reserva **día y hora de visita**: sólo **martes y jueves por la tarde**, con 24 h de margen. Lo pinta `/js/reserva-visita.js`, que consulta los huecos ocupados en la app y, si no contesta, ofrece todos. Las horas están en **dos sitios que hay que cambiar juntos**: el array `HORAS` de ese JS y el `<select id="hora-visita">` de `index.html`.
- Campos obligatorios añadidos: **DNI/NIE** (con comprobación de letra, `dniValido()`) y **referencia catastral**. Hacen falta para inscribir el certificado en la Junta. Ver D12.
- Lo que falta está en la aplicación, no aquí: ver `docs/marketing/integracion-app.md`.

### Segundo dominio
`certificadoenergeticoalmeria.com` es del mismo negocio (WordPress) y **lleva la etiqueta de Google Ads**. No tocarlo: ver D8 en `decisiones.md`.

---

## Reglas que no se rompen

### Datos y honestidad
1. **No inventar cifras.** Ni reseñas, ni número de clientes, ni años de experiencia, ni precios, ni ventajas. Si el dato no está en `negocio.md` §1-5, no se publica.
2. **El precio es 75 € + IVA = 90,75 €** (ver D10). Donde se anuncie el precio, el «+ IVA» puede ir pequeño pero **el total tiene que estar a la vista**: lo exige el art. 20 del RDL 1/2007. No volver a escribir «IVA incluido» ni «todo incluido»; lo que va incluido es **la tasa y el registro en la Junta de Andalucía**.
3. **Un clic no es una consulta, y una consulta no es una venta.** Ver D3 en `decisiones.md`.

### Contenido
4. **No crear páginas de municipio** copiando una plantilla y cambiando el nombre. Ya hay pares con 100 % de texto idéntico (ver D9).
5. **No eliminar ni redirigir URLs** sin comprobar antes su función y sus datos de rendimiento (ver D4).
6. **No cambiar las URLs establecidas.**
7. Cada página debe tener **canonical propio** (su URL absoluta, con `www` y barra final). Nunca apuntando a la portada: ese fue el error que anulaba 102 páginas.
8. Un solo `<title>`, una sola meta descripción y un solo `<h1>` por página.

### Técnica
9. **No migrar de tecnología** (ver D7). El HTML estático se queda.
10. **No instalar MCP, plugins ni dependencias** sin justificar para qué sirven.
11. **No enviar formularios reales** en las pruebas.
12. Para recomendaciones técnicas, **consultar fuentes oficiales** (Google Search Central, documentación de Cloudflare), no lo que se recuerde.
13. **Preservar lo que ya funciona.** El circuito del formulario, las cabeceras de seguridad de `_headers` y el control de consentimiento de cookies están bien: no desmontarlos.

### Contacto (consistente en todo el sitio)
- Teléfono: **667 451 538** · WhatsApp: `wa.me/34667451538`
- COAAT Almería nº **1.440**
- Zona climática **A4** (costa) y **B4** (interior)

---

## Diseño

- **Tipografía:** Montserrat (400, 500, 600, 700). Máximo `font-bold` (700), nunca 900.
- **Colores en uso real:** verde `#43A047`, hover `#388E3C`, WhatsApp `#25d366`, texto `#1a1a1a`, fondo claro `#f6f7f8`.
  ⚠️ `tailwind.config.js` sigue declarando el verde antiguo `#8BC34A`: divergencia conocida (H18).
- **Naranja `#E65100`:** sólo para distintivos pequeños. **Nunca en botones ni llamadas a la acción.**
- **Tres estilos de botón, y sólo tres:** `.btn-primary` (verde WhatsApp), `.btn-secondary` (blanco con borde), `.btn-link`.
- **Tarjetas:** `.card-unified`. **Secciones:** alternar fondo blanco y claro, sin bloques verdes.
- **WhatsApp es la llamada a la acción principal**; el teléfono, secundaria.
- Radios: 8 / 12 / 16 px. Barra fija de contacto: `#sticky-cta`.
- Menú móvil: `#mobile-menu`, `#mobile-menu-button` (animación de hamburguesa a X con `line1`/`line2`/`line3`).
- FAQ: `toggleFAQ(this)`.

---

## Trampas conocidas (han roto la web antes)

1. **Bloques `<script>` duplicados en `index.html`** que declaran el mismo `const` de primer nivel (`mobileMenuButton`, `observer`, `style`). Los `const` de primer nivel se comparten entre scripts clásicos: el segundo bloque lanza «Identifier already declared» y **muere entero**. Ya rompió el efecto de cabecera y el service worker de la PWA. `node --check` por bloque **no lo detecta**: sólo un navegador real.
   → **Por eso el JS nuevo va en archivos externos compartidos, no en línea.**
2. El formulario de la portada **debe** llamarse `wizard-form`. Una vez se renombró a `order-form` y el envío dejó de funcionar en silencio.
3. Las subpáginas arrastran un `<!-- JavaScript optimizado --><script>` **duplicado y mal cerrado** que rompe el análisis del JS en línea. Otra razón para usar `/js/*.js`.
4. `pruebas index/` son copias de prueba de la portada: **excluir de cualquier edición masiva**.
5. Para ediciones masivas, **usar Python leyendo y escribiendo en bytes**. No usar PowerShell con contenido acentuado: destroza los acentos.
6. Conservar siempre los acentos (á, é, í, ñ…).

---

## Comandos útiles

Comprobar que ningún canonical apunta a la portada (debe devolver sólo `./index.html`):

```bash
grep -rl 'canonical href="https://www.certialmeria.es/">' --include="index.html" . | grep -v node_modules
```

Buscar identificadores de medición sin configurar (debe devolver 0):

```bash
grep -rc "GA_MEASUREMENT_ID\|TU_GOOGLE_BUSINESS_ID" --include="*.html" . | grep -v ":0$"
```

Comprobar coherencia de precio e IVA:

```bash
grep -rn "IVA incluido\|+ IVA" --include="*.html" . | grep -v "pruebas index"
```

Verificar el canonical en producción:

```bash
curl -s https://www.certialmeria.es/certificado-energetico-barato/ | grep canonical
```

Contar páginas sin `<h1>`:

```bash
for f in $(find . -name index.html -not -path "./node_modules/*" -not -path "./pruebas index/*"); do [ $(grep -c "<h1" "$f") -eq 0 ] && echo "$f"; done
```

Medir solapamiento entre páginas de municipio: ver el método de 7-gramas en `auditoria-inicial.md` (H9).

---

## Estado real (2026-09-22)

No «listo para producción». Lo publicado tiene cuatro problemas graves activos:

| | Estado |
|---|---|
| Canonical | 🔴 102 páginas se declaran duplicados de la portada |
| Analítica | 🔴 nunca ha medido nada (`GA_MEASUREMENT_ID` sin sustituir en 318 sitios) |
| Reseñas en datos estructurados | 🔴 se declaran 1.000 reseñas no verificables |
| Precio | 🔴 «+ IVA» y «IVA incluido» en la misma página |
| Formularios | ✅ funcionan bien (app + email) |
| Seguridad | ✅ cabeceras completas |

**Primera tarea de implementación: T1** en `backlog.md` (corregir el canonical).

> El historial de auditorías previas (25 archivos `.md` en la raíz, varios contradictorios entre sí) y los scripts de generación de un solo uso están pendientes de mover a `docs/historico/` (T30). Hasta entonces, **`docs/marketing/` es la única fuente vigente**; los `.md` de la raíz son material histórico y algunas de sus afirmaciones han quedado desmentidas por la auditoría.
