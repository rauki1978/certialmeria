/*
 * CertiAlmería - Aviso de cookies y carga de Google (GA4 + Google Ads).
 *
 * Un solo archivo para las 157 páginas. Sustituye al bloque «Cookie Consent
 * System» que iba copiado (dos veces) dentro de cada HTML y que, fuera de la
 * portada, no podía enseñar el aviso: el HTML del banner solo existía allí.
 * Resultado: quien entraba por una página de municipio nunca veía el aviso y
 * nunca se le medía. Ahora el aviso lo pinta este archivo en todas.
 *
 * Dos finalidades opcionales, cada una con su casilla (decisión de Raúl,
 * 28/09/2026):
 *   analytics → Google Analytics 4 (G-BFM9L1F4CW)
 *   ads       → Google Ads (AW-11552890951): medir qué anuncios traen clientes
 *
 * Consent Mode v2 en modo BÁSICO: no se carga nada de Google hasta que el
 * visitante acepta al menos una de las dos. Al cargar, se declara el
 * consentimiento real de cada finalidad (ad_storage, ad_user_data,
 * ad_personalization, analytics_storage). No se usa el modo avanzado (enviar
 * datos sin cookies antes del consentimiento): la AEPD lo ve arriesgado.
 *
 * La elección se guarda en localStorage «certialmeria_cookies» con v:2. Quien
 * eligió con el aviso antiguo (solo analítica) sigue midiéndose en analítica,
 * pero se le vuelve a preguntar porque ahora hay una finalidad nueva.
 *
 * Funciones globales que usan los botones ya existentes (portada, /cookies/):
 * acceptAllCookies, rejectOptionalCookies, showCookieSettings,
 * closeCookieSettings, saveCookieSettings.
 */
(function () {
  "use strict";

  if (window.__caeConsentimiento) return;
  window.__caeConsentimiento = true;

  var GA_ID = "G-BFM9L1F4CW";
  var ADS_ID = "AW-11552890951";
  var CLAVE = "certialmeria_cookies";
  var VERSION = 2;

  var estado = { necessary: true, analytics: false, ads: false, v: VERSION };
  var decidido = false;
  var cargado = false;

  try {
    var guardado = JSON.parse(localStorage.getItem(CLAVE) || "null");
    if (guardado) {
      estado.analytics = !!guardado.analytics;
      estado.ads = !!guardado.ads;
      decidido = guardado.v === VERSION;
    }
  } catch (e) { /* sin almacenamiento: se pregunta en cada visita */ }

  function guardar() {
    estado.v = VERSION;
    try {
      localStorage.setItem(CLAVE, JSON.stringify(estado));
      localStorage.setItem("cookies_accepted", "true");
    } catch (e) { /* modo privado */ }
    decidido = true;
  }

  function senales() {
    var ads = estado.ads ? "granted" : "denied";
    return {
      ad_storage: ads,
      ad_user_data: ads,
      ad_personalization: ads,
      analytics_storage: estado.analytics ? "granted" : "denied"
    };
  }

  // Carga gtag.js una sola vez y configura lo consentido. Si el visitante
  // cambia de opinión en la misma página, se actualiza el consentimiento.
  function aplicar() {
    if (!estado.analytics && !estado.ads) {
      if (cargado) window.gtag("consent", "update", senales());
      return;
    }
    if (!cargado) {
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("consent", "default", senales());
      window.gtag("js", new Date());
      var s = document.createElement("script");
      s.async = true;
      s.src = "https://www.googletagmanager.com/gtag/js?id=" + (estado.analytics ? GA_ID : ADS_ID);
      document.head.appendChild(s);
      cargado = { ga: false, ads: false };
    } else {
      window.gtag("consent", "update", senales());
    }
    if (estado.analytics && !cargado.ga) {
      window.gtag("config", GA_ID);
      cargado.ga = true;
    }
    if (estado.ads && !cargado.ads) {
      window.gtag("config", ADS_ID);
      cargado.ads = true;
    }
  }

  // ---------- Interfaz ----------
  var AZUL = "#1e40af";

  function css() {
    if (document.getElementById("cae-cookies-css")) return;
    var st = document.createElement("style");
    st.id = "cae-cookies-css";
    st.textContent =
      "#cae-cookies{position:fixed;left:0;right:0;bottom:0;z-index:2147483000;background:#111827;color:#fff;" +
      "padding:16px;box-shadow:0 -4px 20px rgba(0,0,0,.25);border-top:4px solid " + AZUL + ";font:14px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}" +
      "#cae-cookies .cae-in{max-width:1100px;margin:0 auto;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}" +
      "#cae-cookies p{margin:0;flex:1 1 420px;color:#d1d5db}" +
      "#cae-cookies strong{color:#fff}" +
      "#cae-cookies a{color:#93c5fd;text-decoration:underline}" +
      ".cae-bts{display:flex;flex-wrap:wrap;gap:8px}" +
      ".cae-b{border:0;border-radius:8px;padding:9px 16px;font:600 14px system-ui,sans-serif;cursor:pointer}" +
      ".cae-b1{background:" + AZUL + ";color:#fff}.cae-b2{background:#4b5563;color:#fff}.cae-b3{background:transparent;color:#d1d5db;border:1px solid #6b7280}" +
      "#cae-cookies-modal{position:fixed;inset:0;z-index:2147483001;background:rgba(0,0,0,.55);display:flex;align-items:center;justify-content:center;padding:16px;font:14px/1.5 system-ui,-apple-system,Segoe UI,Roboto,sans-serif}" +
      "#cae-cookies-modal .cae-box{background:#fff;color:#111827;border-radius:12px;max-width:560px;width:100%;max-height:90vh;overflow:auto;padding:22px}" +
      "#cae-cookies-modal h2{margin:0 0 6px;font-size:19px}" +
      ".cae-fila{display:flex;gap:14px;align-items:flex-start;justify-content:space-between;padding:14px 0;border-top:1px solid #e5e7eb}" +
      ".cae-fila h3{margin:0 0 2px;font-size:15px}.cae-fila p{margin:0;color:#4b5563;font-size:13px}" +
      ".cae-fila input{width:22px;height:22px;accent-color:" + AZUL + ";flex:0 0 auto;margin-top:2px}" +
      ".cae-pie{display:flex;justify-content:flex-end;gap:8px;padding-top:14px;border-top:1px solid #e5e7eb}";
    document.head.appendChild(st);
  }

  function quitar(id) {
    var el = document.getElementById(id);
    if (el) el.parentNode.removeChild(el);
  }

  function banner() {
    if (document.getElementById("cae-cookies")) return;
    css();
    var d = document.createElement("div");
    d.id = "cae-cookies";
    d.setAttribute("role", "dialog");
    d.setAttribute("aria-label", "Aviso de cookies");
    d.innerHTML =
      '<div class="cae-in"><p><strong>Cookies en CertiAlmería.</strong> Usamos cookies técnicas necesarias y, si lo aceptas, ' +
      "cookies de <strong>análisis</strong> (Google Analytics) para mejorar la web y de <strong>publicidad</strong> (Google Ads) " +
      'para saber qué anuncios nos traen clientes. <a href="/cookies/">Política de cookies</a></p>' +
      '<div class="cae-bts"><button type="button" class="cae-b cae-b3" data-cae="config">Configurar</button>' +
      '<button type="button" class="cae-b cae-b2" data-cae="rechazar">Rechazar</button>' +
      '<button type="button" class="cae-b cae-b1" data-cae="aceptar">Aceptar todas</button></div></div>';
    d.addEventListener("click", function (e) {
      var a = e.target.getAttribute && e.target.getAttribute("data-cae");
      if (a === "aceptar") window.acceptAllCookies();
      else if (a === "rechazar") window.rejectOptionalCookies();
      else if (a === "config") window.showCookieSettings();
    });
    document.body.appendChild(d);
  }

  function modal() {
    quitar("cae-cookies-modal");
    css();
    var m = document.createElement("div");
    m.id = "cae-cookies-modal";
    m.setAttribute("role", "dialog");
    m.setAttribute("aria-modal", "true");
    m.setAttribute("aria-label", "Configuración de cookies");
    m.innerHTML =
      '<div class="cae-box"><h2>Configuración de cookies</h2>' +
      '<p style="margin:0 0 8px;color:#4b5563">Elige qué cookies opcionales aceptas. Puedes cambiarlo cuando quieras desde la <a href="/cookies/">política de cookies</a>.</p>' +
      '<div class="cae-fila"><div><h3>Técnicas</h3><p>Necesarias para que la web funcione. No se pueden desactivar.</p></div><input type="checkbox" checked disabled aria-label="Cookies técnicas (siempre activas)"></div>' +
      '<div class="cae-fila"><div><h3>Análisis</h3><p>Google Analytics: cuántas personas visitan la web y qué páginas usan, para mejorarla.</p></div><input type="checkbox" id="cae-c-analytics" aria-label="Cookies de análisis"' + (estado.analytics ? " checked" : "") + "></div>" +
      '<div class="cae-fila"><div><h3>Publicidad</h3><p>Google Ads: saber si un contacto llegó desde uno de nuestros anuncios, para no gastar en anuncios que no funcionan.</p></div><input type="checkbox" id="cae-c-ads" aria-label="Cookies de publicidad"' + (estado.ads ? " checked" : "") + "></div>" +
      '<div class="cae-pie"><button type="button" class="cae-b cae-b3" style="color:#374151" data-cae="cerrar">Cancelar</button>' +
      '<button type="button" class="cae-b cae-b1" data-cae="guardar">Guardar preferencias</button></div></div>';
    m.addEventListener("click", function (e) {
      if (e.target === m) return window.closeCookieSettings();
      var a = e.target.getAttribute && e.target.getAttribute("data-cae");
      if (a === "cerrar") window.closeCookieSettings();
      else if (a === "guardar") window.saveCookieSettings();
    });
    document.body.appendChild(m);
  }

  function registrar(evento) {
    if (typeof window.gtag === "function") {
      window.gtag("event", "cookie_consent", {
        analytics_enabled: estado.analytics,
        ads_enabled: estado.ads,
        eleccion: evento
      });
    }
  }

  // ---------- API global (la usan los botones de la portada y de /cookies/) ----------
  window.acceptAllCookies = function () {
    estado.analytics = true;
    estado.ads = true;
    guardar();
    quitar("cae-cookies");
    quitar("cae-cookies-modal");
    aplicar();
    registrar("aceptar_todas");
  };

  window.rejectOptionalCookies = function () {
    estado.analytics = false;
    estado.ads = false;
    guardar();
    quitar("cae-cookies");
    quitar("cae-cookies-modal");
    aplicar();
  };

  window.showCookieSettings = function () {
    quitar("cae-cookies");
    modal();
  };

  window.closeCookieSettings = function () {
    quitar("cae-cookies-modal");
    if (!decidido) banner();
  };

  window.saveCookieSettings = function () {
    var a = document.getElementById("cae-c-analytics");
    var p = document.getElementById("cae-c-ads");
    estado.analytics = !!(a && a.checked);
    estado.ads = !!(p && p.checked);
    guardar();
    quitar("cae-cookies-modal");
    aplicar();
    registrar("configurar");
  };

  // ---------- Arranque ----------
  aplicar();
  function inicio() { if (!decidido) banner(); }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", inicio);
  } else {
    inicio();
  }
})();
