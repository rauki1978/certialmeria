---
tipo: traspaso
marca: CertiAlmería
estado: vigente
tags: [certialmeria, web, traspaso, estado]
---

# Web de CertiAlmería · Traspaso de sesión (2026-11-01)

Todo lo que una conversación nueva necesita para seguir sin releer las anteriores. Cubre las 2 conversaciones de la clave vieja `F--Google-Drive-APPS-WEB-CERTIALMERIA` (auditoría del 2026-09-22 al 28 y una consulta del 10-05) más lo comprobado hoy en git y en la web en vivo. El marketing posterior (píxel de Meta, favicons, CSP de Ads) se hizo desde la agencia.

## Dónde está cada cosa

- **Código de la web:** `F:\DOCUMENTOS\APPS WEB\CERTIALMERIA` (antes `F:\Google Drive\APPS WEB\CERTIALMERIA`). HTML estático, 156 páginas, sin compilación. Reglas del proyecto en `CLAUDE.md` (leer entero); decisiones D1 a D20 en `docs/marketing/decisiones.md`; hechos verificados en `docs/marketing/negocio.md`.
- **Repo:** `https://github.com/rauki1978/certialmeria.git`. **Producción:** `https://www.certialmeria.es`, Cloudflare Pages, despliegue automático con cada push a `main`.
- **Segundo dominio:** `certificadoenergeticoalmeria.com` (WordPress, lleva la etiqueta de Google Ads). No tocarlo (D8).
- **App con la que habla:** `https://cee.certialmeria.es` (`F:\DOCUMENTOS\APPS WEB\appcertialmeria`). Contrato en `docs/marketing/integracion-app.md`.
- **Marketing (ficha, Ads, Meta, GA4):** `G:\Mi unidad\AGENCIA MARKETING\01-CERTIALMERIA`.
- **Cómo se publica:** Raúl da el visto bueno; push a `main`. Después comprobar la web real con `curl`. Ver memoria `publicar-a-main`.
- **Cómo se prueba:** abrir los HTML o servir la carpeta en local y probar en un navegador real (los errores de scripts duplicados solo salen ahí). No enviar formularios reales; los de Web3Forms y Turnstile los prueba Raúl.
- **Comprobaciones:** los dos `grep` del final de `CLAUDE.md` (canonical y marcadores de medición); `grep -rn "2\.800" --include="*.html" . | grep -v "pruebas index\|horas de sol"` debe dar 0 (D19); un solo `?v=N` en `lead-form.js` tras tocar `/js/`.

## Trabajo listo, SIN publicar

La rama local `marketing/fase0` (`a8e66b0`, la que está en uso) ha divergido de `origin/main` (`1015e22`, favicons, 2026-10-26). Hoy se comprobó en producción que **faltan**:

1. **Referencia catastral opcional** (commit `6c5f3b2`): en la web en vivo la portada sigue mostrando «Referencia catastral *», es decir, obligatoria. Era lo más urgente el 2026-10-05; no consta que se haya publicado.
2. **Artículo del cambio del 30 de septiembre** (commit `cbc0e15`): `/blog/ce3x-3-1-cambios-certificado-energetico-2026/` da **404** en producción. Incluye la sección del blog en la portada, el aviso por WhatsApp, entrada en `blog/index.html` y 7 líneas del `sitemap.xml`.
3. Cambios de `index.html` (127 líneas), `CLAUDE.md` y `docs/marketing/decisiones.md` de esos commits. Diferencia total frente a `origin/main`: 6 archivos, 1.092 líneas añadidas.

Ya están publicados (comprobado en vivo 2026-11-01): «+3.000 certificados» (D19) y el píxel de Meta con la casilla de publicidad (D20, en `/js/consentimiento.js`).

Para publicar: preguntar a Raúl si sube la rama entera o solo lo elegido; el cuerpo de la rama difiere del de `origin/main` en el orden de los commits, así que lo más seguro es una rama `publicar/*` nueva a partir de `origin/main` con commits elegidos, como se hizo con `publicar/meta-3000` y `publicar/favicons`. Antes, `git fetch`.

## Estado comprobado

- **Git (2026-11-01):** rama actual `marketing/fase0`; árbol limpio. `main` local `76d9679` va 9 commits por detrás de `origin/main`. Ramas locales: `main`, `marketing/fase0`, `fix/csp-analytics`, `publicar/csp-ads`, `publicar/favicons`, `publicar/meta-3000`.
- **Producción (2026-11-01):** responde; cifras «+3.000»; `META_PIXEL_ID` puesto en `consentimiento.js`; artículo de CE3X 3.1 ausente; catastral aún obligatoria.
- **Mensaje comercial:** 75 € + IVA = 90,75 € con tasa y registro de la Junta incluidos (D10); 3.042 certificados confirmados por Raúl el 2026-10-15 (D19). Por municipio hay cifras («más de 800 / 450+ en Almería capital», etc.) sin confirmar.
- **Medición:** GA4 empezó a medir el 2026-09-28 según el chat de esa fecha (Search Console, sin acceso aún). Detalle y estado en la agencia (memoria `ga4-propiedades` de ese proyecto).

## Pendientes

- **De Raúl:**
  - responder si se sirve fuera de Almería (`/certificado-energetico/` sigue diciendo «Entrega 48h Toda España» frente al resto de la web, que dice solo provincia de Almería);
  - decidir qué hacer con `certificadoenergeticoalmeria.com` (unificar, dejar solo como landing de Ads o separar áreas);
  - dar acceso a Search Console o pasar el CSV, para decidir sobre municipios y páginas que se canibalizan;
  - cambiar el nombre de la ficha de Google a «CertiAlmería» y dejarla quieta;
  - confirmar las cifras por municipio antes de publicarlas.
- **Técnicos / míos:**
  - publicar lo pendiente (ver arriba), con su visto bueno;
  - pasar a «CE3X 3.x» cualquier texto que aún diga «usamos CE3X 2.3» (la v2.3 no vale desde el 2026-09-30);
  - el JS nuevo siempre en archivos externos y subir `?v=N`;
  - recordar que la referencia catastral no debe volver a ser obligatoria (D17).

## Siguiente paso

Leer `CLAUDE.md` y este archivo; hacer `git fetch`; preguntar a Raúl si publica ya la referencia catastral opcional y el artículo, y en tal caso preparar una rama `publicar/*` con esos dos commits y comprobar luego la web en vivo.

## Informes de esta sesión

- `docs/marketing/` (negocio, auditoría inicial, medición, backlog, plan de 90 días, decisiones, integración con la app), creado el 2026-09-22.
- Resúmenes semanales en `G:\Mi unidad\AGENCIA MARKETING\12-INFORMES` (p. ej. `2026-10-10_CERTIALMERIA_resumen-semanal.md`).
