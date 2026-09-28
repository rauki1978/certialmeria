# CertiAlmería — Hechos del negocio

> Última revisión: 2026-09-22
> Regla de este documento: sólo entra aquí lo **verificado**. Lo que no está confirmado va a "Preguntas pendientes" (§6) y **no se usa en la web, ni en anuncios, ni en fichas**.

---

## 1. Identidad profesional (verificado en código y en web pública)

| Dato | Valor | Dónde se ha comprobado |
|---|---|---|
| Marca comercial | CertiAlmería | `index.html`, logo, dominio |
| Profesional | Raúl Cañadas Navarro | `index.html` meta `author` |
| Titulación | Arquitecto Técnico | toda la web |
| Colegiación | COAAT Almería nº 1.440 | toda la web; también en el 2º dominio |
| Teléfono | 667 45 15 38 | `tel:+34667451538`, 7 enlaces sólo en portada |
| WhatsApp | +34 667 451 538 | `wa.me/34667451538` |
| Email operativo | atltecnicosalmeria@gmail.com | destino de Web3Forms |
| Dominio principal | www.certialmeria.es | canonical, sitemap |
| Segundo dominio | certificadoenergeticoalmeria.com | ver §5 |
| Código postal en schema | 04001 | JSON-LD de `index.html` |
| Dirección postal | **no publicada** | `streetAddress` ausente en todo el sitio |

---

## 2. Servicio y oferta

### Confirmado
- Servicio principal: **certificado de eficiencia energética (CEE)** de vivienda, local y oficina.
- El precio anunciado en toda la web es **75 €**.
- El alcance anunciado incluye: visita presencial con toma de datos, elaboración del certificado, etiqueta energética, firma de técnico competente y **registro en la Junta de Andalucía** (incluida la tasa).
- Plazo anunciado: **24-48 h**.
- Hay páginas de servicio para vivienda, local comercial, oficina, consultoría energética y un "pack certificado + plano".
- Existe una **aplicación propia de gestión** en `cee.certialmeria.es` / `appcertialmeria.vercel.app`, protegida con login, que recibe los interesados del formulario.

### ⚠️ Contradicción abierta y bloqueante: el IVA

La web dice las dos cosas **en la misma página**:

| Ubicación | Texto literal |
|---|---|
| `index.html:1142` (bloque de datos destacados) | «75€ — Precio fijo **+ IVA**» |
| `index.html:1714` (casilla de aceptación del formulario) | «Acepto el servicio por **75 € (IVA incluido)**» |

No es un matiz de redacción: la casilla del formulario es la que el cliente marca, así que **el compromiso que se está recogiendo es "75 € IVA incluido"**, mientras el reclamo comercial dice "+ IVA". Además, el art. 20 del RDL 1/2007 (Ley General para la Defensa de los Consumidores y Usuarios) obliga a anunciar al consumidor final el **precio total con impuestos incluidos**.

→ **Hasta que se aclare no se toca ningún precio.** Ver P1 en §6.

---

## 3. Cobertura

### Confirmado
- La web reclama **cobertura de los 103 municipios** de la provincia de Almería y hay 103 páginas de municipio publicadas.
- El mensaje dominante es «certificados energéticos **exclusivamente en la provincia de Almería**» (314 apariciones en el sitio).
- El `areaServed` del schema de portada lista Almería, Roquetas de Mar, El Ejido y Níjar.

### ⚠️ Contradicción abierta
La página `/certificado-energetico/` —una de las de mayor intención comercial— anuncia en su `<title>` y en su meta description:

> «Certificado Energético Online 75€ | **Entrega 48h Toda España**»
> «Entrega 48h garantizada **toda España**.»

Es incompatible con "exclusivamente provincia de Almería" y con un servicio que incluye **visita presencial**. Para Google Business Profile y para SEO local, un área de servicio contradictoria resta confianza. → Ver P2 en §6.

### Prioridad de negocio declarada por el propietario
**Almería capital y periferia.** Es relevante porque hoy el esfuerzo está repartido entre 103 municipios, muchos de interior y con volumen de búsqueda residual.

---

## 4. Señales de confianza: estado real

Ninguna de las cifras de prestigio es consistente. Recuento sobre los 156 HTML publicados:

| Afirmación | Variantes encontradas | Apariciones |
|---|---|---|
| Años de experiencia | «20 años» / «22 años» / «más de 10 años» | 611 / 12 / 5 |
| Inicio de actividad | «desde 2013» / «desde 2003» | 411 / 7 |
| Certificados emitidos | **2.800** (confirmado por el propietario el 2026-09-28) | unificado en 98 sitios |

«desde 2013» (13 años a fecha de hoy) es aritméticamente incompatible con «20 años» y con «22 años». Puede tener explicación legítima —carrera profesional de 20+ años, certificación energética desde 2013— pero **la web no lo explica**, así que el visitante ve cifras que se contradicen entre sí.

### ✅ Ficha de Google Business Profile (verificada el 2026-09-28)

P3 resuelta. La ficha existe y está en buen estado:

| Dato | Valor |
|---|---|
| Nombre en la ficha | **Certificado energético Almería** (pendiente de cambiar a CertiAlmería) |
| Valoración real | **5,0 con 35 opiniones** |
| Place ID | `ChIJKbf-rq93cA0Rx6lNLrjZdDo` |
| Dirección | C/ Álvarez de Castro, 34, 04002 Almería |
| Teléfono | 667 45 15 38 (coincide con la web) |
| Web enlazada | certialmeria.es (correcto) |
| Fotos | 9 |
| Categoría principal | Servicio de asesoría energética |

**La coherencia nombre-dirección-teléfono está bien**: el schema de la web declara la misma dirección y el mismo teléfono que la ficha. (Una versión anterior de esta auditoría dijo que faltaba la dirección; era un error de lectura del JSON-LD.)

**Se mantiene activa**: hay publicaciones recientes (el cambio a CE3X 3.1) y se contesta a las reseñas una por una. Eso es lo que más cuesta sostener y está hecho.

**Palabras que más repiten los clientes en las reseñas**, según la propia agrupación de Google: *eficiente, rapidez, precio, económico, eficaz, gestión*. Es el lenguaje real del cliente y sirve para redactar la web y para elegir términos en Ads.

El 5,0 con 35 opiniones se muestra ya en la portada, enlazado a la ficha, y **no** como `aggregateRating`: Google no admite que un negocio marque en su propia web las reseñas sobre sí mismo.

### ⚠️ Riesgo grave: valoraciones no verificables (RESUELTO)

> Resuelto el 2026-09-28: se retiró el bloque de 159 páginas y se sustituyó por la valoración real. Se deja el texto por si hace falta justificar por qué se quitó.

En **159 páginas** figura este bloque de datos estructurados:

    "aggregateRating": {
      "ratingValue": "4.9",
      "reviewCount": "1000"
    }

Con una sola reseña visible en la página, firmada por «Cliente Satisfecho» (sin nombre real). Y en portada se muestra un distintivo «4.9 Google».

Problemas, por orden de gravedad:

1. **Riesgo legal.** La Directiva (UE) 2019/2161 (Omnibus), transpuesta por el RDL 24/2021, prohíbe expresamente declarar valoraciones falsas o afirmar que las reseñas están verificadas sin serlo. Es infracción en materia de consumo.
2. **Política de datos estructurados de Google.** `aggregateRating` debe corresponder a valoraciones realmente recogidas y visibles en la página. Declarar 1.000 reseñas expone a la pérdida de resultados enriquecidos o a una acción manual.
3. **Incoherencia interna.** 1.000 reseñas frente a 2.300 certificados implicaría una tasa de reseña del 43 %, muy por encima de lo habitual en el sector.

**No se ha localizado un perfil público de Google Business Profile con reseñas que respalde el 4,9.** Ver P3 en §6. Esta cifra debe sustituirse por el dato real de la ficha o retirarse: no puede quedarse como está.

### ⚠️ El circuito de captación de reseñas está roto

`solicitud-resena/index.html` enlaza a:

    https://g.page/r/TU_GOOGLE_BUSINESS_ID/review

El identificador sigue siendo el texto de ejemplo. Cualquier cliente que haya usado ese enlace para dejar una reseña ha llegado a un error. Esto explicaría por sí solo una ficha con pocas reseñas.

---

## 5. Los dos dominios: hallazgo relevante

Hay un segundo sitio del mismo negocio (mismo teléfono y mismo número de colegiado):

| | www.certialmeria.es | certificadoenergeticoalmeria.com |
|---|---|---|
| Tecnología | HTML estático (Cloudflare Pages) | WordPress + tema Divi |
| Páginas | 156 | landing extensa (una página larga) |
| Teléfono | 667 45 15 38 | **667 45 15 38** (el mismo) |
| COAAT | nº 1.440 | **nº 1.440** (el mismo) |
| Marca en texto | CertiAlmería | «En Certialmería…» |
| Google Analytics | ❌ **placeholder sin configurar** | ✅ `GT-P82NSW7T` |
| Google Ads | ❌ ninguna etiqueta | ✅ **`AW-11552890951`** |
| Canonical | ⚠️ 102 páginas apuntan a la portada | ✅ correcto (auto-canonical) |

**Lectura de negocio:** la medición y la etiqueta de conversión de Google Ads viven en el sitio **antiguo**, mientras el sitio nuevo —mucho más extenso y el que se está trabajando— no mide nada. Además, dos dominios propios compitiendo por las mismas búsquedas reparten autoridad y complican la coherencia nombre-dirección-teléfono en la que se apoya el SEO local.

→ Ver P4 y P5 en §6.

---

## 6. Preguntas pendientes (bloquean decisiones)

| # | Pregunta | Qué bloquea |
|---|---|---|
| **P1** | ¿75 € son **IVA incluido** o **+ IVA** (90,75 €)? | Corregir precios; cumplimiento RDL 1/2007 |
| **P2** | ¿Se presta servicio fuera de Almería? ¿Con visita o sin ella? | Título de `/certificado-energetico/`, GBP, Ads |
| **P3** | ¿Existe ficha de Google Business Profile? URL, nº real de reseñas y nota | Corregir `aggregateRating`; SEO local; reseñas |
| **P4** | ¿`certificadoenergeticoalmeria.com` es propio? ¿Se mantiene, se redirige o se conserva sólo para Ads? | Estrategia de dominio y reparto de autoridad |
| **P5** | ¿Hay acceso a Google Ads `AW-11552890951` y a Search Console? | Todo lo que dependa de datos |
| **P6** | Años de experiencia y certificados emitidos: cifra real y única | Unificar 611 apariciones de texto |
| **P7** | ¿La app `cee.certialmeria.es` registra el estado del cliente hasta la venta? | Diseño de la medición de ventas |
| **P8** | Precio del "pack certificado + plano" y del resto de servicios | Coherencia de la oferta |
| **P9** | Presupuesto mensual disponible para Google Ads | Plan de campañas |
| **P10** | ¿Cuántos certificados al mes se quieren y se pueden atender? | Dimensionar la captación |

---

## 7. Lo que NO se ha verificado y por tanto no se afirma

- Tráfico actual del sitio. **Sin analítica es imposible saberlo.**
- Qué páginas reciben visitas o generan consultas.
- Posiciones en Google de cualquier término.
- Número actual de consultas, clientes y ventas.
- Rentabilidad por certificado y coste de adquisición.
- Los volúmenes de búsqueda que figuraban en el `CLAUDE.md` anterior (74.000/mes, 119.500/mes…): no consta fuente ni fecha.
