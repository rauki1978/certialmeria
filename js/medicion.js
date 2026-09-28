/*
 * CertiAlmería - Medición de contactos (GA4).
 *
 * Un solo archivo para las 157 páginas. Registra la INTENCIÓN de contacto:
 *   clic_telefono      → clic en cualquier enlace tel:
 *   clic_whatsapp      → clic en cualquier enlace a wa.me / api.whatsapp.com
 *   formulario_inicio  → primer campo del formulario que recibe el foco
 * (el envío real del formulario ya lo registra lead-form.js como generate_lead).
 *
 * Un clic NO es una consulta ni una venta (ver medicion.md): en Google Ads
 * estos eventos van como conversión secundaria, nunca como principal.
 *
 * GA4 sólo se carga si el visitante acepta las cookies de analítica
 * (initializeAnalytics en cada página). Sin consentimiento no existe
 * window.gtag y aquí no se envía nada.
 *
 * El origen de la visita (ficha de Google, búsqueda, anuncio...) lo pone GA4
 * solo; para distinguir la ficha, su enlace a la web lleva utm_source=gmb.
 */
(function () {
  "use strict";

  if (window.__caeMedicion) return;
  window.__caeMedicion = true;

  function enviar(evento, datos) {
    if (typeof window.gtag !== "function") return;
    datos = datos || {};
    datos.pagina = location.pathname;
    window.gtag("event", evento, datos);
  }

  document.addEventListener("click", function (e) {
    var a = e.target && e.target.closest ? e.target.closest("a[href]") : null;
    if (!a) return;
    var href = a.getAttribute("href") || "";
    if (/^tel:/i.test(href)) {
      enviar("clic_telefono", { enlace: href.replace(/^tel:/i, "") });
    } else if (/(wa\.me|api\.whatsapp\.com)/i.test(href)) {
      enviar("clic_whatsapp");
    }
  }, true);

  var formularioIniciado = false;
  document.addEventListener("focusin", function (e) {
    if (formularioIniciado) return;
    var t = e.target;
    if (!t || !t.closest || !t.closest("form")) return;
    if (!/^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) return;
    formularioIniciado = true;
    enviar("formulario_inicio");
  });
})();
