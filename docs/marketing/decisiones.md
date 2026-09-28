# Registro de decisiones

> Una entrada por decisión. Se anota **el motivo**, no sólo el resultado, para que en seis meses se sepa por qué se hizo así y se pueda revisar si el motivo cambia.
>
> Formato: fecha · decisión · motivo · alternativas descartadas · cómo se revisará.

---

## 2026-09-22 · D1 · La auditoría no modifica nada

**Decisión.** La primera fase se limita a auditar y documentar. No se ha cambiado ni una línea de la web publicada, ni la configuración de despliegue, ni ninguna campaña.

**Motivo.** Lo pidió el encargo, y además es lo correcto: se han encontrado contradicciones de precio y de cobertura que **sólo el propietario puede resolver**. Tocar precios o retirar páginas sin ese dato produciría un daño peor que el problema.

**Estado de Git.** Se conserva íntegro. Único elemento sin seguimiento antes de empezar: el archivo `NUL` (artefacto de una redirección de PowerShell en Windows), que sigue sin tocarse. Los documentos nuevos se limitan a `docs/marketing/` y a `CLAUDE.md`.

---

## 2026-09-22 · D2 · Corregir el canonical es la primera tarea de implementación

**Decisión.** T1 —reescribir el canonical de 102 páginas a su propia URL— va antes que cualquier otra cosa.

**Motivo.** 102 páginas publicadas declaran ser duplicados de la portada, verificado en producción. Entre ellas todas las páginas comerciales, los 31 artículos del blog y unos 50 municipios, incluidos Almería capital, Roquetas de Mar y El Ejido. Mientras esté así, **todo el trabajo de contenido de este proyecto está anulado**: da igual lo bueno que sea el texto, Google consolida las señales en la portada. Es además una corrección mecánica, verificable y de riesgo bajo.

**Alternativas descartadas.**
- *Empezar por la medición (T2).* Es igual de importante, pero depende de que el propietario cree la propiedad GA4. T1 se puede hacer ya, sin esperar a nadie.
- *Empezar por rendimiento o diseño.* Mejoraría la conversión del tráfico que llega, pero el problema mayor es que no llega tráfico a 102 páginas que deberían recibirlo.

**Cómo se revisará.** En Search Console, a las 4-6 semanas: número de páginas indexadas y desaparición del aviso de «duplicada, Google eligió un canónico distinto».

---

## 2026-09-22 · D3 · Un clic en WhatsApp no se cuenta como consulta ni como venta

**Decisión.** En GA4 y en Google Ads, los clics de WhatsApp y de teléfono se registran como **conversión secundaria, sólo observación**. La conversión principal es el formulario enviado (`generate_lead`). Las consultas por teléfono y WhatsApp se cuentan **sólo si se anotan a mano** en la app.

**Motivo.** Un clic sólo demuestra que alguien pulsó un botón: abrir WhatsApp y no escribir es constantísimo. Contarlo como consulta infla los resultados y crea una falsa sensación de que todo va bien. Y hay un daño peor: si se declara como conversión principal en Google Ads, el algoritmo optimiza para conseguir **clics**, no clientes — se acaba pagando más por tráfico que no compra.

**Alternativa descartada.** *Contar los clics como consultas porque es lo fácil de medir.* Produciría cifras bonitas y decisiones equivocadas. Con un precio de 75 € y margen estrecho, un error de atribución en Ads se come la rentabilidad entera.

**Cómo se revisará.** Comparando mensualmente clics de WhatsApp con consultas reales anotadas. La proporción entre ambos dirá cuánto se habría exagerado.

---

## 2026-09-22 · D4 · No se recomienda borrar ni redirigir ninguna página todavía

**Decisión.** Aunque hay canibalización evidente (tres parejas de páginas con la misma intención) y duplicación grave entre municipios (Viator y La Mojonera son literalmente el mismo texto), **no se propone eliminar ni redirigir nada ahora**.

**Motivo.** No hay ni un dato de rendimiento: la web nunca ha medido. Sin saber qué página recibe impresiones y consultas, cualquier consolidación es una apuesta que puede tirar precisamente la que funcionaba. La secuencia correcta es: arreglar el canonical → medir 4-6 semanas → decidir con cifras.

**Alternativa descartada.** *Consolidar ya por criterio técnico.* Habría parecido diligente y habría sido imprudente. El coste de esperar seis semanas es bajo; el de borrar la página equivocada, alto y difícil de revertir.

**Cómo se revisará.** T14, T15 y T16 se ejecutan cuando haya datos de Search Console, y cada decisión se anota aquí **con la cifra que la respalda**.

---

## 2026-09-22 · D5 · Las 1.000 reseñas se retiran aunque no llegue respuesta

**Decisión.** Si no se facilita el número real de reseñas de la ficha de Google (P3), el bloque `aggregateRating` y el distintivo «4.9 Google» **se retiran** de las 159 páginas. No se dejan como están.

**Motivo.** Declarar 1.000 reseñas con una sola reseña anónima visible expone a dos cosas simultáneas: infracción en materia de consumo (el RDL 24/2021, que transpone la Directiva Omnibus, prohíbe expresamente declarar valoraciones falsas) e incumplimiento de la política de datos estructurados de Google, con riesgo de perder resultados enriquecidos o recibir una acción manual. **Retirar el bloque es seguro; mantenerlo no lo es.** Ante la duda, se elige la opción que no expone al negocio.

**Alternativa descartada.** *Dejarlo hasta que haya reseñas reales.* El riesgo corre mientras esté publicado, y la web lleva así al menos desde 2025.

**Cómo se revisará.** Cuando el circuito de reseñas (T7 + T19) produzca valoraciones reales, se repone el bloque con las cifras verdaderas de la ficha.

---

## 2026-09-22 · D6 · No se adopta Higgsfield ni otra herramienta creativa por ahora

**Decisión.** No se incorpora herramienta de generación creativa en los primeros 90 días.

**Motivo.** El cuello de botella no es producir imágenes. Es que 102 páginas no se indexan, que la web no mide nada y que se anuncian reseñas que no existen. Gastar en creatividad antes de resolver eso es gasto sin retorno. Y de fondo: lo que vende este servicio es **la confianza en un técnico colegiado concreto**. Un vídeo de 30 segundos grabado con el móvil, con Raúl explicando qué mide en una visita real, convence más que cualquier pieza generada — y es verdad.

**Cuándo se reconsidera.** Cuando T20 (Google Ads) esté en marcha y siendo rentable, y haga falta variar creatividades. Entonces, sólo para fondos y recursos gráficos, **nunca para simular visitas, inmuebles, clientes ni certificados que no existen**.

---

## 2026-09-22 · D7 · Se mantiene el HTML estático; no se migra de tecnología

**Decisión.** El sitio sigue siendo HTML estático desplegado en Cloudflare Pages. No se propone migración a ningún framework.

**Motivo.** Funciona, es rápido de servir, y ninguno de los problemas encontrados se debe a la tecnología: el canonical mal puesto, el identificador de analítica sin sustituir y las imágenes sin comprimir pasan exactamente igual en cualquier framework. Migrar consumiría semanas y **no arreglaría ni uno** de los hallazgos. Cambiar de tecnología por preferencia es precisamente lo que el encargo prohíbe.

**Lo que sí se propone.** Externalizar a archivos JS compartidos lo que hoy está repetido en 156 HTML —eventos de analítica, sobre todo—, porque los bloques `<script>` duplicados ya han roto la portada dos veces (documentado en `CLAUDE.md`).

**Cuándo se reconsideraría.** Si llegara a hacer falta contenido dinámico real por usuario. Hoy no hace falta.

---

## 2026-09-22 · D8 · No se toca el segundo dominio hasta decidirlo con el propietario

**Decisión.** `certificadoenergeticoalmeria.com` se deja exactamente como está.

**Motivo.** Es del mismo negocio (mismo teléfono, mismo número de colegiado) y **lleva la etiqueta de conversión de Google Ads `AW-11552890951`**, mientras este dominio no tiene ninguna. Es muy probable que el gasto publicitario y todo el histórico de medición estén asociados a ese sitio. Redirigirlo o retirarlo sin planificarlo **puede romper campañas activas y borrar el único histórico que existe**. Es una decisión de negocio, no técnica.

**Cómo se revisará.** P4 y P5. Tres salidas legítimas: unificar con 301 hacia certialmeria.es; mantener el antiguo sólo como landing de Ads con `noindex`; o mantener ambos con áreas claramente separadas. Se decidirá con el propietario y se anotará aquí.

---

## 2026-09-22 · D9 · No se crean más páginas de municipio

**Decisión.** Queda prohibido generar páginas nuevas de municipio a partir de una plantilla cambiando el nombre. Norma incorporada a `CLAUDE.md`.

**Motivo.** Ya ocurrió: 103 páginas con solapamiento medido de hasta el 100 % entre pares (Viator y La Mojonera), mediana de ~370 palabras. Es el patrón que Google trata como contenido de escaso valor, consume presupuesto de rastreo y no aporta señal local. Repetirlo agravaría el problema que hay que arreglar.

**Lo que sí se hará.** Contenido realmente específico para el grupo prioritario del negocio —Almería capital y periferia—, con datos que no podrían aparecer en otra página: zona climática aplicable, tipología constructiva de la zona, barrios, plazos y desplazamiento reales.

---

## 2026-09-28 · D10 · El precio es 75 € + IVA, con el total a la vista

**Decisión.** Respondida P1: el precio es **75 € + IVA**, o sea **90,75 €**. Se unifica en las 156 páginas. El «+ IVA» va en letra pequeña, como pidió el propietario, pero **siempre acompañado del total** (90,75 €) donde se anuncia el precio. En la caja del formulario que dice «Total», el importe grande es 90,75 € y debajo, pequeño, «75 € + IVA». Se retira toda referencia a «IVA incluido» y «todo incluido», y en su lugar se dice lo que de verdad va incluido: **la tasa y el registro en la Junta de Andalucía**.

**Motivo.** «75 € IVA incluido» convivía con «75 € + IVA» en la misma página, y la frase que el cliente aceptaba al enviar el formulario era la equivocada. Sobre el tamaño: el art. 20 del RDL 1/2007 exige que al consumidor se le anuncie el precio total con impuestos. «75 €» grande con «+ IVA» diminuto y sin total es el patrón que la norma persigue. Añadir el total al lado mantiene el gancho comercial del 75 y deja el anuncio defendible. Se le advirtió al propietario y aceptó esta forma.

Además, «todo incluido» era ambiguo justo en lo que importaba: la gente lo leía como «IVA incluido». Decir «tasa y registro en la Junta incluidos» es más concreto, es verdad, y es precisamente la ventaja frente a quien cobra el registro aparte.

**Alternativa descartada.** *Poner 90,75 € como precio principal.* Es la opción más conservadora legalmente, pero pierde el reclamo del 75 €, que es el eje de toda la web y de las páginas de «barato» y «75 euros». La solución mixta cumple sin tirar el posicionamiento.

**Cómo se revisará.** Si algún cliente reclama por el precio, revisar si el total estaba visible en el punto donde decidió.

---

## 2026-09-28 · D11 · El formulario vende la reserva del hueco, no un descuento

**Decisión.** El asistente pasa a funcionar como reserva: el cliente elige **día y hora concretos** de visita (martes y jueves por la tarde) y el hueco queda a su nombre. Se anuncian cuatro ventajas de reservar por el formulario: eliges día y hora, precio cerrado por escrito, confirmación por WhatsApp y email, y no pagas nada ahora.

**Motivo.** El propietario pidió «que dé la impresión de que si se rellena por formulario te sale mejor». Las cuatro ventajas anunciadas son **reales y estructurales**: por teléfono hay que cuadrar agenda, por formulario el hueco se coge en el momento. No hace falta inventar un descuento para que el formulario sea la mejor opción, y por tanto no se inventa.

**Alternativa descartada.** *Anunciar un precio mejor por formulario.* Habría dado el mismo empujón, pero o es real —y entonces hay dos precios que mantener y facturar— o es falso, y anunciar una ventaja inexistente es práctica comercial desleal además de romper la regla 1 del `CLAUDE.md`. Si el propietario quiere un descuento real por formulario, se implementa, pero tiene que ser real y respetarse al facturar.

**Cómo se revisará.** Comparando en GA4 las consultas que entran por formulario frente a las de teléfono y WhatsApp, una vez haya volumen.

---

## 2026-09-28 · D12 · Se pide DNI y referencia catastral, y el DNI se valida

**Decisión.** El formulario pide **DNI/NIE** (con comprobación de la letra en el navegador) y la **referencia catastral** pasa de opcional a obligatoria, con enlace a la Sede del Catastro para encontrarla. Ambos van en el paso que corresponde: el DNI con los datos personales, la referencia con los del inmueble.

**Motivo.** Los dos son imprescindibles para inscribir el certificado en el registro de la Junta a nombre del cliente, así que pedirlos tarde obliga a volver a llamar. Un DNI con la letra mal bloquea el registro, y detectarlo en el momento cuesta diez líneas de código.

**Contrapartida asumida, y avisada:** cada campo obligatorio de más baja la conversión, y el DNI es de los que más fricción generan. Por eso queda **al final del embudo**, después de que la persona haya elegido día y hora, cuando ya ha invertido algo. Si al ver los datos se detecta mucho abandono en el paso 1, la salida es mover el DNI al último paso o pedirlo después por WhatsApp.

**Aviso de protección de datos.** El DNI es dato personal. Hay que comprobar que la política de privacidad recoge su tratamiento y su finalidad (inscripción registral), y **validarlo también en el servidor**: lo del navegador se salta cualquiera.

---

## 2026-09-28 · D13 · El aviso automático por WhatsApp se separa en dos cosas

**Decisión.** Registrar la fecha de la cita se hace **ya** (la web manda `fecha_visita` y `hora_visita` a la aplicación). El **aviso automático por WhatsApp** se aparca como decisión aparte, y se recomienda empezar por aviso por email más un enlace `wa.me` de un clic dentro de la aplicación.

**Motivo.** Un enlace `wa.me` no manda nada: abre WhatsApp para que alguien pulse enviar. Para que salga solo hace falta la WhatsApp Business Platform (Cloud API), que exige cuenta de Meta verificada, plantillas aprobadas, pago por mensaje y —lo importante— **un número dedicado: al darlo de alta en la API deja de funcionar en la app normal**. El 667 45 15 38 aparece en las 156 páginas y es el que usan los clientes: meterlo en la API sería perder el WhatsApp del móvil.

Además, nada de esto puede vivir en esta web: es HTML estático, el token quedaría público. Va en la aplicación.

**Alternativa recomendada.** Email automático (la aplicación ya manda correo) + botón en la aplicación que abra WhatsApp con el texto escrito. Un clic, coste cero, cubre casi todo el valor. La Cloud API cuando el volumen lo justifique.

**Cómo se revisará.** Si el envío manual se convierte en un estorbo diario, se pasa a la Cloud API con un número nuevo. Detalles en `integracion-app.md`.

---

## 2026-09-28 · D14 · La documentación interna deja de ser pública

**Decisión.** `_redirects` manda `/docs/*`, `/CLAUDE.md`, `/AGENTS.md` y `/README.md` a la portada. El material histórico (32 `.md` y ~30 scripts de un solo uso que estaban en la raíz) se mueve a `docs/historico/`.

**Motivo.** Cloudflare Pages sirve **todo** lo que hay en el repositorio. Comprobado: `https://www.certialmeria.es/docs/marketing/negocio.md` devolvía 200 y se leía entera — la auditoría del negocio, el precio por confirmar, las preguntas pendientes y la estrategia de los dos dominios. También `CLAUDE.md`, `ANALISIS_POSICIONAMIENTO_SEO.md` y hasta los `.py`. **No había ninguna credencial** (lo único que parecía un token era un `TU_TOKEN_AQUI` de ejemplo), así que no es un incidente de seguridad, pero no tiene por qué leerlo la competencia.

**Alternativa descartada.** *Bloquearlo solo en robots.txt.* No sirve: robots pide que no se indexe, no impide entrar. Quien tenga la URL la lee igual.

**Lo que sería más robusto.** Configurar en el panel de Cloudflare Pages un directorio de salida que excluya `docs/`. Es un ajuste del panel, no del repositorio, así que queda para el propietario. Mientras, la redirección cumple.

**Cómo se revisará.** Tras el despliegue, comprobar que `/docs/marketing/negocio.md` devuelve 301. Y **al añadir documentación nueva fuera de `docs/`, añadirle su regla**.

---

## 2026-09-28 · D15 · El hero se sirve en WebP, no en AVIF

**Decisión.** El hero pasa de PNG de 1,6 MB a **WebP de 25 KB** (98,5 % menos). Se genera también AVIF (16 KB) y un JPEG de respaldo con `node optimizar-hero.js`, pero **lo que se sirve es el WebP**.

**Motivo.** El hero es lo que marca el LCP en móvil, que es el dispositivo prioritario, y encima llegaba **sin caché** porque las reglas de `_headers` solo cubrían `/images/*` y las imágenes estaban en la raíz. Moviéndolas a `/images/` heredan la caché de un año ya configurada.

Sobre el formato: el AVIF ahorra 9 KB más, pero al ser un fondo CSS haría falta `image-set()` con negociación de tipo, y un `preload` que acierte con el formato sin descargar los dos. Nueve kilobytes no pagan esa complejidad ni el riesgo de doble descarga. El WebP lo entiende todo lo que importa.

**Cómo se revisará.** Medir el LCP móvil en PageSpeed Insights después del despliegue y anotar el antes y el después.

---

## 2026-09-28 · D16 · `/contacto/` vuelve a existir

**Decisión.** Se quita `/contacto/ / 301` de `_redirects`. La página se queda, con un `<h1>` propio.

**Motivo.** La página ya tenía contenido útil —teléfono, WhatsApp, email, garantía profesional, información práctica, el formulario compartido y los enlaces por municipio— y canonical correcto. Las 157 páginas la enlazan desde el menú y el pie, y estaba en el sitemap. Mandar al visitante de vuelta a la portada justo cuando busca cómo contactar es una fuga en el momento de más intención de compra, y parece una web rota.

**Alternativa descartada.** *Apuntar los 157 enlaces al ancla de la portada.* Más trabajo y peor resultado: una página de contacto propia capta búsquedas de marca y sirve de destino en Ads y en la ficha de Google.

---

## Plantilla para las próximas entradas

    ## AAAA-MM-DD · Dn · Título breve

    **Decisión.** Qué se hace.
    **Motivo.** Por qué, con el dato que lo respalda.
    **Alternativas descartadas.** Qué más se consideró y por qué no.
    **Cómo se revisará.** Qué métrica o fecha dirá si fue acertada.
