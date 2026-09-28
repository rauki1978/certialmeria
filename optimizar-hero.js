/**
 * optimizar-hero.js — genera el hero en formatos modernos.
 *
 * El hero es la imagen que marca el LCP (la métrica de Core Web Vitals que
 * mide cuándo aparece el contenido principal), y en móvil se estaba sirviendo
 * un PNG de 1,6 MB. Este script genera AVIF, WebP y un JPEG de respaldo a los
 * tamaños que de verdad se usan.
 *
 * Volver a ejecutarlo cada vez que cambien heromobile.png o herodesktop.png:
 *   node optimizar-hero.js
 */
const sharp = require('sharp');
const fs = require('fs');

const TRABAJOS = [
  // 828 px cubre un móvil de 414 px a densidad 2x sin pasarse.
  { src: 'heromobile.png',  destino: 'images/hero-movil',      ancho: 828 },
  { src: 'herodesktop.png', destino: 'images/hero-escritorio', ancho: 1600 },
];

(async () => {
  for (const t of TRABAJOS) {
    if (!fs.existsSync(t.src)) {
      console.log('  no está, se salta: ' + t.src);
      continue;
    }

    const antes = fs.statSync(t.src).size;
    const base = sharp(t.src).resize({ width: t.ancho, withoutEnlargement: true });

    await base.clone().avif({ quality: 52, effort: 6 }).toFile(t.destino + '.avif');
    await base.clone().webp({ quality: 74 }).toFile(t.destino + '.webp');
    await base.clone().jpeg({ quality: 78, progressive: true, mozjpeg: true }).toFile(t.destino + '.jpg');

    const kb = (f) => (fs.statSync(f).size / 1024).toFixed(0) + ' KB';
    console.log(
      t.destino.padEnd(26) +
      (antes / 1024).toFixed(0) + ' KB  ->  ' +
      'avif ' + kb(t.destino + '.avif') + ' | ' +
      'webp ' + kb(t.destino + '.webp') + ' | ' +
      'jpg ' + kb(t.destino + '.jpg')
    );
  }
})();
