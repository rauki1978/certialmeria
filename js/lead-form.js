/*
 * CertiAlmería - Formulario de captación unificado.
 * Inyecta un formulario de contacto antes del footer y envía los datos
 * por email vía FormSubmit a atltecnicosalmeria@gmail.com.
 * Único punto de mantenimiento para todas las páginas (la home usa su propio wizard).
 */
(function () {
  "use strict";

  var ACCESS_KEY = "a87c533f-7c8a-4c12-b190-6b68e0e40cec";
  var ENDPOINT = "https://api.web3forms.com/submit";

  // Evitar doble inyección.
  if (document.getElementById("cae-lead-form")) return;

  function init() {
    var anchor = document.querySelector("footer") || document.body;
    if (!anchor) return;

    var styles = document.createElement("style");
    styles.textContent = [
      ".cae-lead-section{background:#f6f7f8;padding:56px 16px;font-family:'Montserrat',sans-serif}",
      ".cae-lead-wrap{max-width:640px;margin:0 auto}",
      ".cae-lead-card{background:#fff;border:1px solid #e5e7eb;border-radius:16px;box-shadow:0 1px 3px rgba(0,0,0,.08);padding:32px 28px}",
      ".cae-lead-title{font-size:1.6rem;font-weight:700;color:#1a1a1a;margin:0 0 6px;text-align:center}",
      ".cae-lead-sub{font-size:1rem;color:#6b7280;margin:0 0 24px;text-align:center}",
      ".cae-row{display:grid;grid-template-columns:1fr 1fr;gap:14px}",
      "@media(max-width:560px){.cae-row{grid-template-columns:1fr}}",
      ".cae-field{margin-bottom:14px}",
      ".cae-field label{display:block;font-size:.85rem;font-weight:600;color:#1a1a1a;margin-bottom:6px}",
      ".cae-field input,.cae-field select,.cae-field textarea{width:100%;box-sizing:border-box;padding:12px 14px;border:1px solid #e5e7eb;border-radius:8px;font-size:1rem;font-family:inherit;color:#1a1a1a;background:#fff}",
      ".cae-field input:focus,.cae-field select:focus,.cae-field textarea:focus{outline:none;border-color:#43A047;box-shadow:0 0 0 3px rgba(67,160,71,.15)}",
      ".cae-field textarea{min-height:90px;resize:vertical}",
      ".cae-priv{display:flex;align-items:flex-start;gap:9px;font-size:.82rem;color:#6b7280;margin:4px 0 18px}",
      ".cae-priv input{margin-top:3px}",
      ".cae-priv a{color:#43A047;text-decoration:underline}",
      ".cae-submit{width:100%;background:#43A047;color:#fff;border:none;border-radius:8px;padding:15px;font-size:1.05rem;font-weight:700;font-family:inherit;cursor:pointer;transition:background .2s}",
      ".cae-submit:hover{background:#388E3C}",
      ".cae-submit:disabled{opacity:.6;cursor:not-allowed}",
      ".cae-note{text-align:center;font-size:.8rem;color:#6b7280;margin-top:14px}",
      ".cae-msg{text-align:center;padding:24px 8px}",
      ".cae-msg h3{font-size:1.3rem;font-weight:700;color:#43A047;margin:0 0 8px}",
      ".cae-msg p{color:#6b7280;margin:0 0 16px}",
      ".cae-wa{display:inline-block;background:#25d366;color:#fff;text-decoration:none;padding:12px 22px;border-radius:8px;font-weight:700}"
    ].join("");
    document.head.appendChild(styles);

    var section = document.createElement("section");
    section.className = "cae-lead-section";
    section.id = "solicitar";
    section.innerHTML =
      '<div class="cae-lead-wrap">' +
        '<div class="cae-lead-card">' +
          '<h2 class="cae-lead-title">Solicita tu presupuesto online</h2>' +
          '<p class="cae-lead-sub">Rellena el formulario y te respondemos en menos de 30 minutos. Certificado energético desde 75&euro;.</p>' +
          '<form id="cae-lead-form" novalidate>' +
            '<div class="cae-row">' +
              '<div class="cae-field"><label for="cae-nombre">Nombre y apellidos *</label><input id="cae-nombre" name="nombre" type="text" autocomplete="name" required></div>' +
              '<div class="cae-field"><label for="cae-telefono">Tel&eacute;fono *</label><input id="cae-telefono" name="telefono" type="tel" autocomplete="tel" required></div>' +
            '</div>' +
            '<div class="cae-row">' +
              '<div class="cae-field"><label for="cae-email">Email</label><input id="cae-email" name="email" type="email" autocomplete="email"></div>' +
              '<div class="cae-field"><label for="cae-municipio">Municipio</label><input id="cae-municipio" name="municipio" type="text"></div>' +
            '</div>' +
            '<div class="cae-field"><label for="cae-tipo">Tipo de inmueble</label><select id="cae-tipo" name="tipo_inmueble">' +
              '<option value="Vivienda / Piso">Vivienda / Piso</option>' +
              '<option value="Local comercial">Local comercial</option>' +
              '<option value="Oficina">Oficina</option>' +
              '<option value="Nave / Otro">Nave / Otro</option>' +
            '</select></div>' +
            '<div class="cae-field"><label for="cae-mensaje">Mensaje (opcional)</label><textarea id="cae-mensaje" name="mensaje" placeholder="Metros, direcci&oacute;n, dudas..."></textarea></div>' +
            '<label class="cae-priv"><input id="cae-priv" type="checkbox" required><span>He le&iacute;do y acepto la <a href="/politica-privacidad/" target="_blank" rel="noopener">pol&iacute;tica de privacidad</a>.</span></label>' +
            '<button type="submit" class="cae-submit" id="cae-submit">Enviar solicitud</button>' +
            '<p class="cae-note">O ll&aacute;manos directamente al <strong>667 45 15 38</strong></p>' +
          '</form>' +
        '</div>' +
      '</div>';

    anchor.parentNode.insertBefore(section, anchor);

    document.getElementById("cae-municipio").value = guessMunicipio();
    document.getElementById("cae-lead-form").addEventListener("submit", onSubmit);
  }

  function guessMunicipio() {
    var h = document.querySelector("h1, h2");
    if (h) {
      var m = h.textContent.match(/\ben\s+([A-Za-zÁÉÍÓÚáéíóúÑñ.\s-]{2,40})$/);
      if (m) return m[1].trim();
    }
    return "";
  }

  function val(id) {
    var el = document.getElementById(id);
    return el ? el.value.trim() : "";
  }

  function onSubmit(e) {
    e.preventDefault();
    var nombre = val("cae-nombre");
    var telefono = val("cae-telefono");

    if (!nombre || !telefono) {
      alert("Por favor, indica tu nombre y tu teléfono.");
      return;
    }
    if (!/^[6-9]\d{8}$/.test(telefono.replace(/\s+/g, ""))) {
      alert("Por favor, introduce un número de teléfono válido (9 dígitos).");
      return;
    }
    if (!document.getElementById("cae-priv").checked) {
      alert("Debes aceptar la política de privacidad para continuar.");
      return;
    }

    var btn = document.getElementById("cae-submit");
    btn.disabled = true;
    btn.textContent = "Enviando...";

    var payload = {
      access_key: ACCESS_KEY,
      subject: "Nueva solicitud web - " + nombre,
      from_name: "CertiAlmería Web",
      nombre: nombre,
      telefono: telefono,
      email: val("cae-email"),
      municipio: val("cae-municipio"),
      tipo_inmueble: val("cae-tipo"),
      mensaje: val("cae-mensaje"),
      pagina: location.pathname
    };

    var fd = new FormData();
    Object.keys(payload).forEach(function (k) { fd.append(k, payload[k]); });

    fetch(ENDPOINT, {
      method: "POST",
      headers: { Accept: "application/json" },
      body: fd
    })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        if (data && data.success) {
          if (typeof gtag !== "undefined") {
            gtag("event", "generate_lead", { event_category: "engagement", event_label: "lead_form_web3forms" });
          }
          showSuccess(nombre);
        } else {
          btn.disabled = false;
          btn.textContent = "Enviar solicitud";
          showError(nombre, telefono);
        }
      })
      .catch(function () {
        btn.disabled = false;
        btn.textContent = "Enviar solicitud";
        showError(nombre, telefono);
      });
  }

  function showSuccess(nombre) {
    var card = document.querySelector("#solicitar .cae-lead-card");
    if (!card) return;
    card.innerHTML =
      '<div class="cae-msg"><h3>¡Solicitud enviada, ' + escapeHtml(nombre) + '!</h3>' +
      '<p>Hemos recibido tus datos y te contactaremos en menos de 30 minutos.</p></div>';
  }

  function showError(nombre, telefono) {
    var msg = "Hola, me llamo " + nombre + " y quiero solicitar un certificado energético. Mi teléfono es " + telefono + ".";
    var wa = "https://wa.me/34667451538?text=" + encodeURIComponent(msg);
    var card = document.querySelector("#solicitar .cae-lead-card");
    if (!card) return;
    var box = document.createElement("div");
    box.className = "cae-msg";
    box.innerHTML =
      '<p>No hemos podido enviar el formulario. Escríbenos por WhatsApp o llama al <strong>667 45 15 38</strong>.</p>' +
      '<a class="cae-wa" href="' + wa + '" target="_blank" rel="noopener">Enviar por WhatsApp</a>';
    card.appendChild(box);
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
