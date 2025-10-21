const sharp = require('sharp');
const fs = require('fs');
const path = require('path');

// Imágenes que necesitan conversión a WebP
const imagesToOptimize = [
  { input: 'images/logo.png', output: 'images/logo.webp', quality: 85 },
  { input: 'images/raul-canadas.jpg', output: 'images/raul-canadas.webp', quality: 80 }
];

async function optimizeImages() {
  console.log('🚀 Iniciando optimización de imágenes...\n');

  for (const img of imagesToOptimize) {
    try {
      // Verificar si el archivo de entrada existe
      if (!fs.existsSync(img.input)) {
        console.log(`⚠️  ${img.input} no encontrado, saltando...`);
        continue;
      }

      // Obtener tamaño original
      const originalStats = fs.statSync(img.input);
      const originalSize = (originalStats.size / 1024).toFixed(2);

      // Convertir a WebP
      await sharp(img.input)
        .webp({ quality: img.quality, effort: 6 })
        .toFile(img.output);

      // Obtener tamaño optimizado
      const optimizedStats = fs.statSync(img.output);
      const optimizedSize = (optimizedStats.size / 1024).toFixed(2);
      const savings = ((1 - optimizedStats.size / originalStats.size) * 100).toFixed(2);

      console.log(`✅ ${path.basename(img.input)} → ${path.basename(img.output)}`);
      console.log(`   📊 ${originalSize} KB → ${optimizedSize} KB (${savings}% reducción)\n`);

    } catch (error) {
      console.error(`❌ Error procesando ${img.input}:`, error.message);
    }
  }

  console.log('✨ Optimización completada!');
}

optimizeImages();
