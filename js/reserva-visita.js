/**
 * reserva-visita.js — huecos de visita técnica, coordinados con la aplicación.
 *
 * Las visitas son SOLO martes (día 2) y jueves (día 4), por la tarde.
 *
 * Antes de ofrecer un hueco se le pregunta a la aplicación qué citas tiene ya
 * reservadas, para no dar dos veces la misma hora. Si la aplicación no
 * responde (o el endpoint todavía no existe) se ofrecen todos los huecos y la
 * aplicación confirma después: vale más una reserva que haya que recolocar
 * que un formulario que no se deja enviar. Es el mismo criterio que sigue
 * lead-form.js.
 *
 * CONTRATO CON LA APLICACIÓN (pendiente de implementar en cee.certialmeria.es)
 *   GET /api/huecos?desde=AAAA-MM-DD&hasta=AAAA-MM-DD
 *   200 { "ok": true, "ocupados": [ { "fecha": "2026-10-01", "hora": "17:00" } ] }
 *   Basta con devolver las citas ya reservadas en ese rango. Si un día tiene
 *   todas sus horas ocupadas, este script lo oculta entero.
 *
 * Va en archivo externo a propósito: los <script> en línea de index.html ya
 * rompieron la página dos veces al repetir un const de primer nivel.
 */
(function () {
  "use strict";

  var API_HUECOS = "https://cee.certialmeria.es/api/huecos";

  var MARTES = 2;
  var JUEVES = 4;
  var CUANTOS = 8;          // ~4 semanas de huecos
  var MARGEN_HORAS = 24;    // no se reserva para hoy ni para dentro de un rato

  // Tienen que coincidir con las opciones del <select> de horas del formulario.
  var HORAS = ["16:00", "17:00", "18:00", "19:00"];

  var DIAS = ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"];
  var MESES = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
               "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"];

  var ocupados = {};        // { "2026-10-01": { "17:00": true } }
  var huecos = [];          // fechas candidatas (objetos Date)

  function dosDigitos(n) {
    return (n < 10 ? "0" : "") + n;
  }

  /** Valor que viaja al servidor: AAAA-MM-DD, sin depender de la zona horaria. */
  function valor(f) {
    return f.getFullYear() + "-" + dosDigitos(f.getMonth() + 1) + "-" + dosDigitos(f.getDate());
  }

  /** Texto que ve la persona: "jueves 8 de octubre". */
  function etiqueta(f) {
    return DIAS[f.getDay()] + " " + f.getDate() + " de " + MESES[f.getMonth()];
  }

  /** Próximas fechas en martes o jueves, con 24 h de margen. */
  function calcularHuecos() {
    var out = [];
    var hoy = new Date();
    hoy.setHours(0, 0, 0, 0);
    var limite = new Date(Date.now() + MARGEN_HORAS * 3600 * 1000);
    limite.setHours(0, 0, 0, 0);

    // Como mucho 60 días por delante: corta el bucle pase lo que pase.
    for (var i = 0; i < 60 && out.length < CUANTOS; i++) {
      var f = new Date(hoy.getTime() + i * 86400000);
      var dia = f.getDay();
      if ((dia === MARTES || dia === JUEVES) && f >= limite) {
        out.push(f);
      }
    }
    return out;
  }

  function horasLibres(clave) {
    var cogidas = ocupados[clave] || {};
    var libres = [];
    for (var i = 0; i < HORAS.length; i++) {
      if (!cogidas[HORAS[i]]) libres.push(HORAS[i]);
    }
    return libres;
  }

  function pintarFechas(select) {
    select.innerHTML = "";

    var disponibles = [];
    for (var i = 0; i < huecos.length; i++) {
      if (horasLibres(valor(huecos[i])).length) disponibles.push(huecos[i]);
    }

    var vacio = document.createElement("option");
    vacio.value = "";
    vacio.textContent = disponibles.length ? "Elige el día" : "Sin huecos: llámanos y lo cuadramos";
    select.appendChild(vacio);

    for (var j = 0; j < disponibles.length; j++) {
      var o = document.createElement("option");
      o.value = valor(disponibles[j]);
      o.textContent = etiqueta(disponibles[j]);
      select.appendChild(o);
    }
  }

  /** Deja en el select de horas solo las que quedan libres ese día. */
  function pintarHoras(selectHora, clave) {
    if (!selectHora) return;
    var previa = selectHora.value;
    var libres = clave ? horasLibres(clave) : HORAS;

    selectHora.innerHTML = "";
    var vacio = document.createElement("option");
    vacio.value = "";
    vacio.textContent = "Elige la hora";
    selectHora.appendChild(vacio);

    for (var i = 0; i < libres.length; i++) {
      var h = libres[i];
      var fin = parseInt(h.slice(0, 2), 10) + 1;
      var o = document.createElement("option");
      o.value = h;
      o.textContent = h + " - " + dosDigitos(fin) + ":00";
      if (h === previa) o.selected = true;
      selectHora.appendChild(o);
    }
  }

  function consultarApp() {
    if (!huecos.length) return Promise.resolve();
    var desde = valor(huecos[0]);
    var hasta = valor(huecos[huecos.length - 1]);

    return fetch(API_HUECOS + "?desde=" + desde + "&hasta=" + hasta, {
      headers: { Accept: "application/json" }
    })
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (j) {
        if (!j || !j.ok || !j.ocupados || !j.ocupados.length) return;
        for (var i = 0; i < j.ocupados.length; i++) {
          var c = j.ocupados[i];
          if (!c || !c.fecha || !c.hora) continue;
          if (!ocupados[c.fecha]) ocupados[c.fecha] = {};
          ocupados[c.fecha][c.hora] = true;
        }
      })
      .catch(function () {
        // La aplicación no contesta: se ofrecen todos los huecos y ella
        // confirma. No se bloquea la reserva por esto.
      });
  }

  function init() {
    var selectFecha = document.querySelector("[data-reserva-fechas]");
    if (!selectFecha) return;
    var selectHora = document.getElementById("hora-visita");

    huecos = calcularHuecos();

    // Se pinta ya con todo disponible, y se refina cuando conteste la app:
    // así el formulario es usable desde el primer segundo.
    pintarFechas(selectFecha);
    pintarHoras(selectHora, "");

    selectFecha.addEventListener("change", function () {
      pintarHoras(selectHora, selectFecha.value);
    });

    consultarApp().then(function () {
      var elegida = selectFecha.value;
      pintarFechas(selectFecha);
      if (elegida) selectFecha.value = elegida;
      pintarHoras(selectHora, selectFecha.value);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
