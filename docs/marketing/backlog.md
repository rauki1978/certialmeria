# Backlog priorizado

> Fecha: 2026-09-22
> Orden: por impacto sobre certificados vendidos, no por facilidad.
> Esfuerzo: **S** < 2 h · **M** 2-8 h · **L** 1-3 días · **XL** más de 3 días.
> Cada tarea lleva un **criterio de finalización comprobable**: si no se puede comprobar, la tarea no está hecha.

---

## Cómo está ordenado

Hay una secuencia obligada, y saltársela desperdicia trabajo:

1. **Desbloquear** (T1-T2). Sin canonical correcto, el contenido no existe para Google. Sin medición, no se puede decidir nada.
2. **Sanear riesgo** (T3-T5). Cosas que exponen legalmente o que cuestan clientes ahora.
3. **Recoger datos** (T6-T8). Cuatro a seis semanas de espera obligatoria.
4. **Decidir con datos** (T9+). Nada de esto antes de tener las cifras.

---

## Bloque 1 — Desbloquear (semana 1)

### T1 · Corregir el canonical de 102 páginas 🔴
- **Hallazgo:** H1
- **Por qué primero:** el contenido de 156 páginas está anulado. Todo lo demás que se haga en SEO es inútil mientras esto siga así.
- **Impacto:** el más alto del backlog. Devuelve la posibilidad de posicionar a todas las páginas comerciales, los 31 artículos y ~50 municipios, incluidos Almería capital, Roquetas y El Ejido.
- **Esfuerzo:** M
- **Dependencias:** ninguna. Se puede empezar ya.
- **Cómo:** script en Python que lea cada `index.html`, derive la URL desde la ruta del archivo y reescriba el canonical a su propia URL absoluta. Leer y escribir en bytes para no romper acentos (regla del `CLAUDE.md`). Excluir `pruebas index/` y `node_modules/`.
- **Criterio de finalización:**
  1. `grep -rl 'canonical href="https://www.certialmeria.es/">' --include=index.html .` no devuelve nada salvo la portada.
  2. Cada página tiene canonical igual a su propia URL, con `www`, con barra final.
  3. Comprobado en producción con `curl` en al menos 5 páginas de distinta carpeta.
  4. El sitemap y los canonical coinciden URL por URL.

### T2 · Conectar GA4 de verdad 🔴
- **Hallazgo:** H2
- **Por qué:** sin datos no se puede decidir sobre municipios, canibalización ni publicidad. Es la tarea que convierte opiniones en decisiones.
- **Impacto:** alto e indirecto — habilita todo el resto del plan.
- **Esfuerzo:** S (una vez se tenga el identificador)
- **Dependencias:** **el propietario debe crear la propiedad GA4 y facilitar el `G-…`.** Bloqueada hasta entonces.
- **Cómo:** sustituir `GA_MEASUREMENT_ID` en las 318 referencias. Mantener el condicionamiento al consentimiento de cookies. Excluir tráfico propio.
- **Criterio:** informe en tiempo real de GA4 con una visita de prueba; cero apariciones de `GA_MEASUREMENT_ID` en el repositorio.

### T3 · Verificar Search Console y enviar el sitemap 🔴
- **Hallazgo:** H2, y es el verificador de T1
- **Impacto:** alto e indirecto. Es la única forma de comprobar que T1 funciona y la única fuente para decidir sobre T9 y T10.
- **Esfuerzo:** S
- **Dependencias:** T1 hecho (para que lo que se envíe sea correcto); acceso del propietario.
- **Criterio:** dominio verificado, sitemap procesado sin errores, y captura del estado de indexación guardada como punto de partida en `docs/marketing/datos/`.

---

## Bloque 2 — Sanear riesgo (semana 1-2)

### T4 · Retirar o corregir las 1.000 reseñas declaradas 🔴
- **Hallazgo:** H3
- **Por qué:** riesgo legal (RDL 24/2021, reseñas falsas) y riesgo de sanción de Google. No es aplazable.
- **Impacto:** evita un perjuicio; no suma tráfico.
- **Esfuerzo:** S
- **Dependencias:** P3 (nº real de reseñas). **Si P3 no llega, se retira el bloque** — retirar es seguro, dejarlo no.
- **Cómo:** en las 159 páginas, sustituir `aggregateRating` por los valores reales de la ficha o eliminar el bloque. Quitar el distintivo «4.9 Google» de portada si no hay respaldo. De paso, actualizar `priceValidUntil` (H11), que está en el mismo JSON-LD.
- **Criterio:** ninguna página declara valoraciones no verificables; el validador de resultados enriquecidos de Google no da error; `priceValidUntil` con fecha futura.

### T5 · Unificar el mensaje de IVA 🔴
- **Hallazgo:** H4
- **Por qué:** el cliente ve dos precios distintos en el momento de decidir, y el art. 20 del RDL 1/2007 exige precio final con impuestos.
- **Impacto:** medio-alto en conversión, directamente en el punto de cierre.
- **Esfuerzo:** S
- **Dependencias:** **P1. Bloqueada: no se toca ningún precio sin la respuesta.**
- **Criterio:** una sola forma de expresar el precio en las 156 páginas; la casilla del formulario y el reclamo comercial dicen lo mismo.

### T6 · Recuperar `/contacto/` o redirigir sus 157 enlaces 🟠
- **Hallazgo:** H6
- **Por qué:** «Contacto» está en el menú de todas las páginas y devuelve al visitante a la portada. Es una fuga en la intención más comercial que hay.
- **Impacto:** medio-alto en conversión.
- **Esfuerzo:** M
- **Dependencias:** decidir entre las dos opciones (recomendada: recuperar la página).
- **Cómo (opción recomendada):** quitar `/contacto/ / 301` de `_redirects`, dar a la página contenido real —teléfono, WhatsApp, formulario, zona de servicio, horario, colegiación—, añadirle `<h1>` (H14) y canonical propio.
- **Criterio:** `curl -I https://www.certialmeria.es/contacto/` devuelve 200; la página tiene un `<h1>`; sigue en el sitemap con canonical propio; los enlaces del menú llevan a contenido útil.

### T7 · Arreglar el enlace de petición de reseñas 🟠
- **Hallazgo:** H7
- **Por qué:** el circuito que genera reseñas está cortado, y las reseñas son el primer factor de decisión en servicios locales y peso fuerte en el mapa. Es también la vía honesta de sustituir el 4,9 inventado por uno real.
- **Impacto:** medio-alto a medio plazo.
- **Esfuerzo:** S
- **Dependencias:** P3 (URL real de la ficha).
- **Criterio:** el enlace abre el formulario de reseña de la ficha real; probado con un cliente real; ninguna aparición de `TU_GOOGLE_BUSINESS_ID`.

### T8 · Aligerar el hero móvil 🟠
- **Hallazgo:** H5
- **Por qué:** 1,6 MB en PNG, con prioridad de carga y **sin caché**, en el dispositivo prioritario. Define el LCP.
- **Impacto:** medio-alto en conversión móvil y en Core Web Vitals.
- **Esfuerzo:** M
- **Dependencias:** ninguna. `sharp` ya está en las dependencias del proyecto.
- **Cómo:** generar AVIF + WebP a los tamaños reales de uso; servir con `<picture>`; ajustar el `preload` al formato que se sirve; **extender `_headers` para cubrir las imágenes de la raíz**, que hoy no entran en ninguna regla. Aprovechar para recomprimir los iconos de `/images/` (29 MB, con PNG de ~1 MB para iconos pequeños) y eliminar el duplicado `ticket.png` / `precio.png`.
- **Criterio:** hero móvil por debajo de 150 KB; `curl -I` sobre el hero devuelve `Cache-Control` con `max-age` largo; LCP móvil medido en PageSpeed Insights antes y después, con la mejora anotada en `decisiones.md`.

### T9 · Sacar el aviso de cookies de encima de la llamada a la acción 🟠
- **Hallazgo:** revisión visual en 375 × 812
- **Por qué:** ocupa ~40 % de la primera pantalla móvil y tapa la zona de contacto del hero. La primera impresión es un bloque de cookies con tres botones en lugar de una vía de contacto.
- **Impacto:** medio en conversión móvil.
- **Esfuerzo:** S
- **Dependencias:** ninguna. **Debe seguir cumpliendo el consentimiento: no se trata de esconderlo, sino de que ocupe menos y no tape el CTA.**
- **Criterio:** en 375 × 812, con el aviso visible, la vía de contacto principal sigue siendo alcanzable sin desplazarse; las tres opciones de consentimiento siguen disponibles.

---

## Bloque 3 — Medición completa (semana 2-4)

### T10 · Eventos de contacto en GA4 🟠
- **Hallazgo:** `medicion.md` §4 paso 3
- **Impacto:** medio e indirecto. Es lo que permitirá saber qué páginas generan intención.
- **Esfuerzo:** M
- **Dependencias:** T2.
- **Cómo:** `clic_telefono`, `clic_whatsapp`, `formulario_inicio`, `generate_lead`, en **un archivo JS compartido** — no repetidos en cada HTML, por el problema conocido de scripts duplicados que ya rompió la portada.
- **Criterio:** los cuatro eventos aparecen en la depuración de GA4. **Sin enviar formularios reales.**

### T11 · Estados de cliente en la app 🟠
- **Hallazgo:** `medicion.md` §4 paso 5
- **Por qué:** es lo que cierra el círculo de consulta a venta. Sin esto sólo se sabrá cuántos formularios llegan, no cuántos se cobran, y no se podrá calcular si la publicidad es rentable.
- **Impacto:** alto para las decisiones de inversión.
- **Esfuerzo:** L
- **Dependencias:** P7; desarrollo en la app, fuera de este repositorio.
- **Criterio:** se puede responder con una consulta: *«consultas de los últimos 30 días, cuántas cobradas, por qué importe y desde qué página»*.

### T12 · Registro manual de consultas por WhatsApp y teléfono 🟠
- **Hallazgo:** `medicion.md` §2 etapa 3
- **Por qué:** en un negocio local la mayoría de los clientes llaman. Ninguna herramienta lo captura sola. Sin este hábito el embudo queda ciego en su tramo más rentable.
- **Impacto:** alto. Es el dato que más cuesta conseguir y el que más vale.
- **Esfuerzo:** S para habilitarlo; requiere constancia diaria.
- **Dependencias:** T11.
- **Criterio:** durante 30 días seguidos, toda consulta telefónica o por WhatsApp queda anotada el mismo día.

### T13 · Etiqueta de conversión de Google Ads 🟡
- **Hallazgo:** H2, H10
- **Esfuerzo:** S
- **Dependencias:** T2, T10, y **P4/P5 resueltas** (si se reutiliza `AW-11552890951` o se crea cuenta nueva).
- **Cómo:** principal = `generate_lead`. Secundarias, sólo observación = `clic_telefono`, `clic_whatsapp`. **Nunca un clic como conversión principal**, porque el algoritmo optimizaría para clics en lugar de clientes.
- **Criterio:** conversión de prueba registrada; las secundarias marcadas explícitamente como secundarias.

---

## Bloque 4 — Decisiones que exigen datos (semana 6 en adelante)

> ⛔ **Nada de este bloque antes de tener 4-6 semanas de Search Console posteriores a T1.** Actuar antes sería borrar a ciegas.

### T14 · Resolver la canibalización de las tres parejas 🟡
- **Hallazgo:** H8
- **Esfuerzo:** M
- **Dependencias:** T1 + T3 + 4-6 semanas de datos.
- **Cómo:** por cada pareja (`barato`/`75-euros`, `rapido`/`24-horas`, portada/`municipios/almeria`), conservar la que reciba impresiones y clics, y fusionar la otra con 301 hacia ella, trasladando antes el contenido que aporte.
- **Criterio:** una sola URL por intención; las retiradas responden 301; documentado en `decisiones.md` **con las cifras que respaldan cada decisión**.

### T15 · Reescribir las páginas de municipio prioritarias 🟡
- **Hallazgo:** H9
- **Por qué:** hay pares con 100 % de solapamiento (Viator y La Mojonera son el mismo texto con otro nombre). La prioridad del negocio es capital y periferia, y hoy el esfuerzo está repartido entre 103 municipios.
- **Impacto:** medio-alto sobre la prioridad declarada.
- **Esfuerzo:** XL
- **Dependencias:** T1, T3, datos.
- **Cómo:** contenido realmente específico para el grupo prioritario (Almería, Roquetas, El Ejido, Vícar, Huércal de Almería, Níjar, Viator, Benahadux, Pechina, Gádor): zona climática aplicable, tipología constructiva de la zona, barrios, plazos y desplazamiento reales, casos propios. **No crear ni una página más cambiando sólo el nombre.**
- **Criterio:** solapamiento entre páginas prioritarias por debajo del 30 % con la misma medición de 7-gramas que usó la auditoría; cada una con un dato local que no podría estar en otra.

### T16 · Decidir qué hacer con el resto de municipios 🟡
- **Hallazgo:** H9
- **Esfuerzo:** L
- **Dependencias:** T15 y datos de Search Console.
- **Cómo:** para los que no reciban impresiones, elegir entre reescribir, fusionar en páginas comarcales (Almanzora, Alpujarra, Los Vélez, Levante) o dejar con `noindex`. **Con cifras delante, no por intuición.**
- **Criterio:** decisión por municipio documentada con su dato de impresiones.

### T17 · Decidir la estrategia de los dos dominios 🟡
- **Hallazgo:** H10
- **Esfuerzo:** M la decisión; L la ejecución.
- **Dependencias:** **P4 y P5. Bloqueada.**
- **Cuidado:** redirigir un dominio con historial de Google Ads puede romper campañas activas. No tocar hasta decidir y planificar.
- **Criterio:** decisión registrada en `decisiones.md` con su motivo; si se unifica, redirecciones comprobadas una a una y campañas reapuntadas antes del cambio.

---

## Bloque 5 — Captación, cuando la base esté sana

> Estas tareas dependen de que T1-T13 estén hechas. Poner dinero en publicidad sobre una web que no mide y con el canonical roto es tirarlo.

| # | Tarea | Impacto | Esfuerzo | Depende de |
|---|---|---|---|---|
| T18 | Google Business Profile: reclamar/optimizar la ficha, fotos reales, zona de servicio coherente, publicaciones | **Alto** — en servicios locales el mapa suele traer más clientes que la web | M | P2, P3 |
| T19 | Circuito de reseñas en marcha: pedirla al entregar el certificado, con el enlace ya arreglado | **Alto** | S + constancia | T7, T18 |
| T20 | Google Ads de búsqueda, ámbito Almería capital y periferia, con presupuesto contenido y términos de marca y de servicio | Medio-alto | M | T13, P2, P9 |
| T21 | Términos negativos y revisión de búsquedas: filtrar «gratis», «curso», «modelo», fuera de zona | Medio — protege el presupuesto | S + semanal | T20 |
| T22 | GEO/AEO: respuestas claras y citables, datos estructurados correctos, `FAQPage` sólo donde hay preguntas reales | Medio, creciente | M | T1, T4 |
| T23 | Vídeo corto real: una visita, qué se mide, el certificado entregado | Medio | L | — |
| T24 | Redes sociales con la cadencia que se pueda sostener | Bajo-medio | L | T23 |

### Sobre Higgsfield y las herramientas creativas

**Recomendación: no adoptar ahora.** El cuello de botella del negocio no es la producción de imágenes: es que la web no se indexa, no mide y anuncia reseñas que no existen. Herramienta creativa antes de eso es gasto sin retorno.

Y hay un motivo de fondo más importante: lo que vende este servicio es **confianza en un técnico colegiado concreto**. Un vídeo de 30 segundos grabado con el móvil, con Raúl explicando qué mide en una visita real, convence más que cualquier pieza generada — y es honesto. Los activos generados se plantean cuando haya que escalar creatividades de Ads (T20 en marcha y rentable), y siempre para fondos o recursos gráficos, **nunca para simular visitas, inmuebles, clientes ni certificados que no existen**.

---

## Tareas de higiene (sin prisa, sin dependencias)

| # | Tarea | Esfuerzo | Criterio |
|---|---|---|---|
| T25 | Quitar la etiqueta `viewport` duplicada (H13) | S | una sola por página |
| T26 | Sacar del menú público el enlace a la app de gestión (H15) | S | no aparece en la navegación; sigue accesible para el técnico |
| T27 | Revisar `robots.txt`: `Disallow: /*.json` y `Crawl-delay` (H16) | S | no bloquea recursos legítimos |
| T28 | Borrar `.htaccess` o documentar que Cloudflare Pages no lo lee (H17) | S | nadie puede editarlo creyendo que surte efecto |
| T29 | Alinear `tailwind.config.js` con el color real en uso (H18) | S | config y diseño coinciden, o la divergencia está documentada |
| T30 | Mover a `docs/historico/` las 25 auditorías previas y los ~30 scripts de un solo uso; borrar `NUL` | M | raíz legible; nada publicado se rompe |
| T31 | Limpiar de `package.json` las dependencias de Next.js que no se usan | S | sólo queda lo que el sitio usa |
| T32 | Añadir `<h1>` a `/blog/` (H14) | S | un `<h1>` por página en todo el sitio |

---

## Bloqueadas por falta de respuesta

| Tarea | Espera |
|---|---|
| T5 (IVA) | **P1** |
| T4, T7, T18 | **P3** (ficha de Google) |
| T13, T17 | **P4, P5** (dominios y accesos) |
| T20 | **P2, P9** (cobertura y presupuesto) |
| T11 | **P7** (app) |
| Unificar experiencia y certificados en 611 textos | **P6** |
