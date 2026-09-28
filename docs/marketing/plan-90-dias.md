# Plan de 90 días

> Fecha de inicio prevista: pendiente de las respuestas a §6 de `negocio.md`
> Redactado: 2026-09-22

## Advertencia sobre lo que este plan no promete

**No se compromete ninguna posición en Google.** Nadie puede garantizarlas, y quien lo haga está vendiendo humo. Lo que sí se compromete son **entregables comprobables** y **métricas que se medirán**, sean buenas o malas.

Un aviso adicional sobre el punto de partida: como hoy no se mide nada (H2), **el primer mes no producirá comparaciones, sino la primera línea base de la historia del sitio**. Las cifras del mes 1 no son un resultado: son el punto cero. Cualquier «mejora del X %» que se cite antes de tener esa línea base es inventada.

---

## Fase 0 · Días 1-7 — Desbloquear

**Objetivo:** que el contenido que ya existe pueda ser indexado y que empiece a haber datos.

| Entregable | Tarea | Criterio |
|---|---|---|
| Canonical corregido en 102 páginas | T1 | cero páginas apuntando a la portada; verificado en producción |
| GA4 recibiendo datos | T2 | visita de prueba visible en tiempo real |
| Search Console verificado | T3 | sitemap procesado; estado de indexación guardado |
| Reseñas no verificables retiradas | T4 | ninguna página declara 1.000 reseñas |

**Se mide:** nada todavía — se instala lo que medirá.

**Depende de:** el propietario debe crear la propiedad GA4 y dar acceso a Search Console. **Sin eso, la Fase 0 se queda a medias** y el plan entero se retrasa.

> Nota sobre expectativas: tras corregir el canonical, Google necesita semanas para volver a rastrear y reindexar 102 páginas. No habrá efecto visible en días.

---

## Fase 1 · Días 8-30 — Sanear y cerrar fugas

**Objetivo:** dejar de perder clientes que ya están llegando, y completar la medición.

| Entregable | Tarea | Criterio |
|---|---|---|
| Un solo mensaje de precio | T5 | coherente en 156 páginas *(requiere P1)* |
| `/contacto/` funcionando | T6 | responde 200 con contenido útil |
| Enlace de reseñas operativo | T7 | abre la ficha real *(requiere P3)* |
| Hero móvil aligerado y cacheado | T8 | < 150 KB, con caché larga |
| Cookies sin tapar el CTA | T9 | contacto alcanzable en 375 × 812 |
| Eventos de contacto en GA4 | T10 | los cuatro eventos verificados |
| Ficha de Google optimizada | T18 | datos, zona y fotos reales coherentes con la web |
| Circuito de reseñas en marcha | T19 | se pide reseña al entregar cada certificado |

**Se mide (primera línea base):**
- visitas totales y proporción de móvil
- clics de teléfono y de WhatsApp
- formularios enviados
- LCP móvil antes y después de T8
- páginas indexadas en Search Console

**Hito de la fase:** existe, por primera vez, un número real de visitas y de consultas.

---

## Fase 2 · Días 31-60 — Cerrar el círculo hasta la venta

**Objetivo:** poder responder «¿cuántas de las consultas se cobraron y desde qué página llegaron?».

| Entregable | Tarea | Criterio |
|---|---|---|
| Estados de cliente en la app | T11 | la consulta de consulta-a-venta devuelve resultado |
| Consultas por teléfono y WhatsApp anotadas | T12 | 30 días seguidos sin huecos |
| Etiqueta de Ads instalada | T13 | conversión de prueba registrada *(requiere P4/P5)* |
| Decisión sobre los dos dominios | T17 | registrada con su motivo *(requiere P4)* |
| Higiene técnica | T25-T32 | cada una con su criterio |

**Se mide:**
- **consulta → cliente cualificado → venta** (el embudo completo, por primera vez)
- consultas por página de origen (campo `pagina`, que ya se guarda)
- consultas por municipio
- margen real por certificado, por zona

**Hito:** se sabe qué páginas traen clientes que pagan. A partir de aquí las decisiones dejan de ser opiniones.

> Si el registro manual de T12 no se sostiene, este hito no se alcanza. Es el punto más frágil del plan y depende de un hábito diario, no de tecnología.

---

## Fase 3 · Días 61-90 — Decidir con datos y empezar a captar

**Objetivo:** consolidar lo que funciona, retirar lo que no, y abrir publicidad sólo si la base está sana.

| Entregable | Tarea | Criterio |
|---|---|---|
| Canibalización resuelta | T14 | una URL por intención, con cifras que lo respalden |
| Municipios prioritarios reescritos | T15 | solapamiento < 30 %; un dato local propio por página |
| Decisión sobre el resto de municipios | T16 | por municipio, con su dato de impresiones |
| Google Ads en marcha *(condicionado)* | T20, T21 | campaña activa con conversiones registrando |
| Contenidos citables (GEO/AEO) | T22 | datos estructurados válidos |

**Condición para abrir Google Ads — las cuatro, sin excepción:**
1. GA4 y la etiqueta de Ads midiendo correctamente.
2. El embudo hasta la venta operativo (T11 + T12).
3. Cobertura y precio sin contradicciones (P1, P2 resueltas).
4. Margen por certificado conocido, para saber cuánto se puede pagar por venta.

**Si alguna falla, no se abre Ads.** Con un precio de 75 €, el margen es estrecho: publicidad sin medición se convierte en pérdida antes de que nadie lo note.

**Se mide:**
- coste por consulta y **coste por venta**
- coste por venta frente a margen por certificado *(la comparación que decide si se sigue)*
- consultas por municipio frente a coste de servirlos
- evolución de la indexación tras T1

---

## Lo que se revisa cada semana

| Cuándo | Qué | Tiempo |
|---|---|---|
| Lunes | consultas de la semana por vía y municipio; ¿alguna sin contestar? | 10 min |
| Día 1 de mes | embudo completo; consultas por página; coste por venta si hay Ads | 30 min |
| Fin de fase | ¿se cumplieron los criterios? ¿qué se cambia? → a `decisiones.md` | 1 h |

---

## Qué puede descarrilar el plan

| Riesgo | Efecto | Cómo se contiene |
|---|---|---|
| No llegan los accesos (GA4, Search Console, Ads, ficha) | **Bloquea las Fases 0 y 2 por completo** | Es el riesgo principal. Depende sólo del propietario |
| P1 (IVA) sin respuesta | T5 bloqueada; sigue habiendo dos precios en la web | Escalado: es también un asunto de cumplimiento |
| El registro manual de consultas no se mantiene | Embudo ciego; no se puede calcular rentabilidad | Hacerlo trivial: un campo, un clic, en el móvil |
| Se abre Ads antes de medir | Gasto sin saber qué funciona | Las cuatro condiciones de la Fase 3 no se negocian |
| Tentación de crear más páginas de municipio | Más contenido duplicado, mismo problema | Norma escrita en `CLAUDE.md` |
| Google tarda en reindexar tras T1 | Parece que la corrección no sirvió | Contar en semanas, no en días. Vigilar en Search Console |

---

## Después de los 90 días

Con datos reales sobre la mesa, las decisiones que tocará tomar:

- ¿Compensa servir todos los municipios, o conviene acotar a la zona rentable?
- ¿Sostiene Google Ads el coste por venta frente al margen?
- ¿Es 75 € el precio adecuado, visto el margen real por zona?
- ¿Merece la pena el contenido de blog, o rinde más la ficha de Google y las reseñas?
- ¿Qué servicio tiene mejor margen: certificado suelto, pack con plano, consultoría?

Ninguna se puede responder hoy. En 90 días, con este plan cumplido, todas tendrán respuesta con cifras.
