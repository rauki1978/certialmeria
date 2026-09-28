# Medición — de la visita a la venta

> Fecha: 2026-09-22
> Principio rector: **un clic no es una consulta, y una consulta no es una venta.**
> Sólo se cuenta como venta lo que está cobrado.

---

## 1. Situación actual: no se mide nada

| Capa | Estado | Evidencia |
|---|---|---|
| Analítica web | ❌ **Inexistente** | `GA_MEASUREMENT_ID` sin sustituir en 318 referencias de 156 páginas |
| Eventos de conversión | ⚠️ Programados pero inertes | 342 llamadas `gtag('event', …)` que disparan al vacío |
| Etiqueta de Google Ads | ❌ Ninguna en este dominio | 0 apariciones de `AW-…`; la etiqueta `AW-11552890951` está en `certificadoenergeticoalmeria.com` |
| Search Console | ❓ Sin verificar | 0 metaetiquetas de verificación (podría estar por DNS) |
| Registro de consultas | ✅ **Existe y funciona** | `cee.certialmeria.es/api/interesados` + copia por email |
| Estado del cliente hasta la venta | ❓ Por confirmar | P7 en `negocio.md` |

**Consecuencia práctica.** No hay ni un dato propio sobre el que decidir. Cualquier cifra de tráfico o de rendimiento que se cite hoy sobre este sitio es una suposición. Por eso la auditoría no recomienda borrar páginas: no hay con qué justificarlo.

**El activo que sí existe.** La app propia de gestión recibe cada interesado con `nombre`, `telefono`, `email`, `municipio`, `tipo_inmueble`, `mensaje`, `pagina` (la URL de origen) y `origen`. Ese `pagina` es oro: permite atribuir cada consulta a la página que la generó **sin depender de Google Analytics**. Es la base de todo lo que sigue.

---

## 2. Las cinco etapas y qué cuenta como cada una

Definiciones estrictas, para que nadie se engañe con los números.

### Etapa 1 · Visita
**Qué es:** una sesión en el sitio.
**Cómo se medirá:** GA4, evento `page_view` automático.
**Qué NO cuenta:** vistas de robots, ni visitas propias (excluir la IP propia y el tráfico interno).

### Etapa 2 · Clic de contacto — *intención, no consulta*
**Qué es:** el visitante pulsa teléfono, WhatsApp o empieza el formulario.
**Cómo se medirá:** eventos GA4 con nombres propios:

| Evento | Se dispara cuando |
|---|---|
| `clic_telefono` | clic en un `href="tel:…"` |
| `clic_whatsapp` | clic en un `href="wa.me/…"` |
| `formulario_inicio` | primer campo del formulario recibe el foco |

**Regla explícita y no negociable:** ⚠️ **un clic de WhatsApp NO es una consulta y NO es una venta.** Mide únicamente que alguien pulsó un botón. Abre la app y no escribe, o escribe y no contesta: pasa constantemente. Contarlo como consulta infla los resultados y —lo peor— si se declara como conversión en Google Ads, el algoritmo optimiza para conseguir **clics**, no clientes: se acaba pagando más por tráfico que no compra.

En Ads estos eventos se configuran como **conversión secundaria** (observación), nunca como principal.

### Etapa 3 · Consulta real — *primera conversión de verdad*
**Qué es:** ha llegado un contacto identificable con el que se puede hablar.

Tres vías, y las tres cuentan:

| Vía | Cómo se registra | Dónde queda |
|---|---|---|
| Formulario enviado | evento `generate_lead` (ya programado en `lead-form.js:284`) | app + email |
| Mensaje de WhatsApp recibido | **registro manual** en la app | app |
| Llamada atendida con conversación real | **registro manual** en la app | app |

**Qué NO cuenta:** un clic (etapa 2). Un WhatsApp abierto sin mensaje. Una llamada perdida. Spam. Un formulario de prueba.

**Nota importante:** las consultas por WhatsApp y por teléfono **sólo pueden medirse si se anotan**. Ninguna herramienta las captura sola. Es trabajo manual de 10 segundos por consulta, y sin él el embudo queda ciego justo en su tramo más rentable — en un negocio local, la mayoría de los clientes llaman.

### Etapa 4 · Cliente cualificado
**Qué es:** la consulta es un encargo posible: inmueble en zona de servicio, el servicio es el que se presta, hay intención real y se ha podido dar precio y plazo.
**Cómo se medirá:** campo de estado en la app.
**Qué NO cuenta:** fuera de zona; sólo pedía información; comparando precios sin intención; ya tiene certificado en vigor.

### Etapa 5 · Venta
**Qué es:** certificado encargado, hecho, registrado y **cobrado**.
**Cómo se medirá:** estado final en la app, con importe y fecha.
**Qué NO cuenta:** presupuesto aceptado de palabra. Visita hecha sin cobrar. Certificado entregado y pendiente de pago.

---

## 3. Los números que interesan de verdad

No el tráfico. Estos:

| Indicador | Fórmula | Para qué sirve |
|---|---|---|
| Visita → consulta | consultas ÷ visitas | ¿convence la web? |
| Consulta → cualificado | cualificados ÷ consultas | ¿atrae al público correcto? |
| Cualificado → venta | ventas ÷ cualificados | ¿cierra bien la oferta? |
| **Consulta → venta** | ventas ÷ consultas | **el número clave del negocio** |
| Consultas por página | agrupar por el campo `pagina` de la app | qué páginas trabajan y cuáles no |
| Consultas por municipio | agrupar por `municipio` | dónde está la demanda real |
| Coste por consulta (Ads) | gasto ÷ consultas | si la publicidad es sostenible |
| **Coste por venta (Ads)** | gasto ÷ ventas | **si la publicidad es rentable** |
| Margen por certificado | precio − (desplazamiento + tiempo + tasa) | el techo del coste por venta |

**La única comparación que decide si se sigue invirtiendo:** coste por venta frente a margen por certificado. Con un precio de 75 €, el margen es estrecho y el margen de error en Ads es pequeño: por eso la medición tiene que estar antes del primer euro de publicidad, no después.

**Por municipio, además:** la periferia y el interior no cuestan lo mismo de servir. Un certificado en Serón consume una mañana de desplazamiento; uno en el centro de Almería, una hora. El mismo precio da márgenes distintos. Agrupar las ventas por municipio es lo que permitirá decidir con datos hasta dónde conviene llegar — y refuerza la prioridad declarada de capital y periferia.

---

## 4. Qué implantar, en orden

### Paso 1 — GA4 conectado de verdad *(bloquea todo lo demás)*
1. Crear la propiedad GA4 y obtener el identificador `G-XXXXXXXXXX` real.
2. Sustituirlo en los 318 sitios donde hoy está `GA_MEASUREMENT_ID`.
3. Respetar el consentimiento de cookies que ya está implementado: la carga sigue condicionada a la aceptación de analítica. **No desactivar ese control.**
4. Excluir el tráfico propio.
5. Verificar en el informe de tiempo real que llegan datos.

**Criterio de finalización:** el informe en tiempo real de GA4 muestra una visita de prueba, y no queda ni una aparición de `GA_MEASUREMENT_ID` en el repositorio.

### Paso 2 — Search Console
Verificar el dominio, enviar el sitemap, y revisar el informe de indexación. **Este paso es el que confirmará si la corrección del canonical (H1) surte efecto**, y el que dará por fin datos para decidir sobre las páginas que se canibalizan y sobre los municipios.

**Criterio:** dominio verificado, sitemap procesado y una captura del estado de indexación guardada como punto de partida.

### Paso 3 — Eventos de contacto
Implantar `clic_telefono`, `clic_whatsapp`, `formulario_inicio` y `generate_lead` con nombres consistentes en las 156 páginas. Mejor en un único archivo JS compartido que repetidos en cada HTML, por el problema de scripts duplicados que ya ha roto la portada antes (ver `CLAUDE.md`).

**Criterio:** los cuatro eventos aparecen en la depuración de GA4 al ejecutarlos a mano. **Sin enviar formularios reales**: usar la depuración del navegador o un envío marcado como prueba, según lo acordado.

### Paso 4 — Etiqueta de Google Ads
Instalar la etiqueta (decidir antes si se reutiliza `AW-11552890951` o se crea una nueva → P4, P5) y definir:

- **Conversión principal:** `generate_lead` — el formulario enviado.
- **Conversiones secundarias (sólo observación):** `clic_telefono`, `clic_whatsapp`.

**Criterio:** la conversión registra una prueba en la interfaz de Ads, y las secundarias están marcadas explícitamente como secundarias.

### Paso 5 — Estados en la app *(el paso que cierra el círculo)*
Añadir a `cee.certialmeria.es` un campo de estado por interesado:

    nuevo → contactado → cualificado → presupuestado → ganado → cobrado
                      ↘ descartado (con motivo)

Con: importe, fecha de cobro, municipio, y el `pagina` de origen que **ya se está guardando**.

**Criterio:** se puede responder con una consulta a la base de datos: *«de las consultas de los últimos 30 días, cuántas se cobraron, por qué importe y desde qué página llegaron»*.

### Paso 6 — Ventas fuera de línea de vuelta a Ads
Cuando haya volumen suficiente, subir las ventas cobradas a Google Ads como conversiones fuera de línea. Así el algoritmo optimiza para **clientes que pagan**, no para formularios. Es la diferencia entre publicidad que se sostiene y publicidad que se abandona a los tres meses.

**Criterio:** Ads muestra ventas importadas y el coste por venta real.

---

## 5. Revisión periódica

| Cuándo | Qué se mira |
|---|---|
| Semanal (10 min) | consultas de la semana por vía y por municipio; ¿alguna se quedó sin contestar? |
| Mensual (30 min) | embudo completo; consultas por página; si hay Ads, coste por venta frente a margen |
| Trimestral | qué páginas no han traído ni una consulta en 90 días → decidir con datos |

## 6. Privacidad

- No se guardan credenciales ni identificadores de cuentas en esta documentación.
- La analítica sigue supeditada al consentimiento de cookies ya implementado.
- Los datos personales de los interesados viven en la app, no en el repositorio.
- No se envían formularios reales en las pruebas.
