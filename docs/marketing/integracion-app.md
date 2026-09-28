# Integración web ↔ aplicación (cee.certialmeria.es)

> Fecha: 2026-09-28
> **Esto no se puede terminar en este repositorio.** La web es HTML estático: no tiene servidor donde guardar un token. Todo lo que aquí figura como pendiente vive en el código de la aplicación, no aquí.

---

## Lo que la web ya manda

El asistente de la portada (`#wizard-form`) envía a `POST /api/reservas` este objeto. Los campos nuevos van marcados:

    {
      "nombre": "Nombre Apellidos",
      "dni": "12345678Z",                  // NUEVO
      "telefono": "600000000",
      "email": "cliente@ejemplo.es",
      "direccion": "Calle Ejemplo 1",
      "cp": "04001",
      "municipio": "Almería",
      "ref_catastral": "1234567AB1234C",   // ahora OBLIGATORIO
      "tipo_inmueble": "piso",
      "metros": "80",
      "anio": "1998",
      "observaciones": "...",
      "fecha_visita": "2026-10-01",        // NUEVO  (AAAA-MM-DD)
      "hora_visita": "17:00",              // NUEVO  (martes o jueves, tarde)
      "empresa": "",                       // campo trampa antispam: si viene con algo, es un robot
      "turnstile_token": "...",
      "interesado_id": "...",
      "acepta_servicio": true,
      "acepta_privacidad": true
    }

El DNI se valida en el navegador (letra de control de DNI y NIE), pero **hay que validarlo también en el servidor**: lo del navegador se salta cualquiera.

⚠️ **Si la aplicación descarta los campos que no conoce, se pierden el DNI y la cita.** Es lo primero que hay que comprobar.

---

## Pendiente 1 · Disponibilidad real de citas

**Lo que pidió el propietario:** que las citas se coordinen con las que ya están reservadas en la aplicación.

`js/reserva-visita.js` ya lo consulta. Falta el endpoint:

    GET /api/huecos?desde=2026-09-29&hasta=2026-11-05

    200 OK
    {
      "ok": true,
      "ocupados": [
        { "fecha": "2026-10-01", "hora": "17:00" },
        { "fecha": "2026-10-06", "hora": "18:00" }
      ]
    }

Basta con devolver las citas ya reservadas en ese rango. El script se encarga del resto: quita esas horas del desplegable y, si un día se queda sin horas libres, lo oculta entero.

**Mientras no exista**, la web ofrece todos los huecos de martes y jueves y la aplicación confirma después. No se rompe nada: es el mismo criterio que ya sigue `lead-form.js` — vale más una reserva que haya que recolocar que un formulario que no se deja enviar.

**Detalles que hay que resolver en el servidor:**
- Debe permitir peticiones desde `https://www.certialmeria.es` (CORS). En `_headers` el `connect-src` ya autoriza `cee.certialmeria.es`.
- No debe devolver datos personales, sólo fecha y hora. Son huecos ocupados, no clientes.
- **La comprobación definitiva va en `POST /api/reservas`**: entre que alguien ve el desplegable y envía el formulario pueden pasar minutos. Si el hueco se ha ocupado, que la reserva se acepte igual y se marque para recolocar — así lo anuncia la web: «Si ese hueco ya estuviera cogido te avisamos y buscamos el siguiente. No pierdes la reserva.»
- Horas disponibles hoy: `16:00`, `17:00`, `18:00`, `19:00`, sólo martes y jueves. Si esto cambia, hay que cambiarlo en dos sitios: el array `HORAS` de `js/reserva-visita.js` y el `<select id="hora-visita">` de `index.html`.

---

## Pendiente 2 · Aviso automático por WhatsApp

**Lo que pidió el propietario:** que al dar de alta el certificado se mande automáticamente el aviso por WhatsApp, y que quede registrada la fecha.

**Esto no se puede hacer desde la web, y conviene saber lo que implica antes de decidir.**

Un enlace `wa.me` —lo que usa hoy la web— **no manda nada**: abre WhatsApp con un texto escrito para que la persona le dé a enviar. Para que salga un mensaje solo, sin que nadie toque nada, hace falta la **WhatsApp Business Platform (Cloud API)** de Meta, y eso trae condiciones:

| | |
|---|---|
| Cuenta | Meta Business verificada |
| Número | Un número **dedicado**. Al darlo de alta en la API, **deja de funcionar en la app normal de WhatsApp** |
| Mensajes | Fuera de las 24 h siguientes al último mensaje del cliente, sólo se pueden mandar **plantillas aprobadas previamente** por Meta |
| Coste | Se paga por mensaje de plantilla. No es gratis |
| Dónde vive | En el servidor de la aplicación. El token **nunca** puede estar en la web: sería público |

⚠️ **El aviso importa:** el 667 45 15 38 es el número que aparece en las 156 páginas y el que usan los clientes. Si se mete ese número en la Cloud API, se pierde el WhatsApp normal en el móvil. Lo sensato es **dar de alta un segundo número** para los avisos automáticos y dejar el 667 para hablar con la gente.

**Alternativa más barata para empezar:** que la aplicación mande el aviso **por email** (ya tiene correo montado con Web3Forms) y que el WhatsApp lo siga enviando Raúl a mano desde un enlace `wa.me` con el texto ya escrito, desde la propia aplicación. Un clic, coste cero, y cubre el 90 % del valor. La Cloud API se plantea cuando el volumen lo justifique.

**Sobre «que la fecha quede registrada»:** con `fecha_visita` y `hora_visita` ya llegando a la aplicación, eso es un campo en su base de datos. No necesita WhatsApp para nada. Merece la pena separarlo: registrar la cita es hoy; el aviso automático es una decisión con coste.

---

## Pendiente 3 · Estados del cliente hasta el cobro

Sigue pendiente lo de `medicion.md` §4 paso 5: sin el estado de cada interesado hasta el cobro no se puede saber si la captación es rentable. Ahora hay un motivo más para hacerlo: con la cita reservada, los estados naturales serían

    nuevo → visita reservada → visitada → certificado emitido → registrado → cobrado
                            ↘ recolocar (el hueco estaba cogido)
                            ↘ descartado (con motivo)

---

## Resumen de lo que toca a quién

| Tarea | Dónde | Estado |
|---|---|---|
| Campos DNI, referencia catastral y cita en el formulario | esta web | ✅ hecho |
| Calendario de martes y jueves por la tarde | esta web | ✅ hecho |
| Consulta de disponibilidad (cliente) | esta web | ✅ hecho, esperando el endpoint |
| Aceptación del encargo sin pago previo, bien visible | esta web | ✅ hecho |
| Alternativa «llámame o manda un WhatsApp» | esta web | ✅ hecho |
| Aceptar los campos nuevos sin descartarlos | **aplicación** | ⏳ comprobar |
| Validar el DNI en servidor | **aplicación** | ⏳ |
| `GET /api/huecos` | **aplicación** | ⏳ |
| Comprobar el hueco al reservar | **aplicación** | ⏳ |
| Aviso de alta del certificado | **aplicación** | ⏳ decidir email o Cloud API |
| Estados hasta el cobro | **aplicación** | ⏳ |
