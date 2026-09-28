const sharp = require('sharp');
const fs = require('fs');

async function optimizeHero() {
  console.log('🚀 Optimizando imagen hero-bg.jpg a WebP...\n');

  const input = 'images/hero-bg.jpg';
  const output = 'images/hero-bg.webp';

  try {
    // Verificar si existe el archivo
    if (!fs.existsSync(input)) {
      console.log('⚠️  Archivo no encontrado:', input);
      return;
    }

    // Obtener tamaño original
    const originalStats = fs.statSync(input);
    const originalSize = (originalStats.size / 1024).toFixed(2);

    console.log(`📁 Archivo original: ${input}`);
    console.log(`📊 Tamaño original: ${originalSize} KB`);

    // Convertir a WebP con calidad 80
    await sharp(input)
      .webp({ quality: 80, effort: 6 })
      .toFile(output);

    // Obtener tamaño optimizado
    const optimizedStats = fs.statSync(output);
    const optimizedSize = (optimizedStats.size / 1024).toFixed(2);
    const savings = ((1 - optimizedStats.size / originalStats.size) * 100).toFixed(2);

    console.log(`\n✅ ${output} creado exitosamente`);
    console.log(`📊 Tamaño optimizado: ${optimizedSize} KB`);
    console.log(`💾 Ahorro: ${savings}% (${(originalSize - optimizedSize).toFixed(2)} KB)`);
    console.log('\n✨ Optimización completada!');

  } catch (error) {
    console.error('❌ Error:', error.message);
  }
}

optimizeHero();
