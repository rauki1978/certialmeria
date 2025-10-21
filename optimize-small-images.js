const sharp = require('sharp');
const fs = require('fs');

async function optimizeSmallImages() {
  console.log('🚀 Optimizando imágenes para tamaños de visualización reales...\n');

  try {
    // Logo pequeño para header
    console.log('📦 Logo pequeño (1182x387px → 400x131px)...');
    const logoOriginal = fs.statSync('images/logo.webp');
    const logoOriginalSize = (logoOriginal.size / 1024).toFixed(2);

    await sharp('images/logo.webp')
      .resize(400, 131, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
      .webp({ quality: 85, effort: 6 })
      .toFile('images/logo-small.webp');

    const logoSmall = fs.statSync('images/logo-small.webp');
    const logoSmallSize = (logoSmall.size / 1024).toFixed(2);
    const logoSavings = ((1 - logoSmall.size / logoOriginal.size) * 100).toFixed(2);

    console.log(`   Original: ${logoOriginalSize} KB`);
    console.log(`   Pequeño:  ${logoSmallSize} KB`);
    console.log(`   Ahorro:   ${logoSavings}% (${(logoOriginalSize - logoSmallSize).toFixed(2)} KB)\n`);

    // Iconos pequeños
    console.log('🎯 Iconos pequeños (1024x1024px → 128x128px)...\n');
    const icons = ['precio', 'cobertura', 'rapidez', 'profesionalidad'];
    let totalOriginalIcons = 0;
    let totalSmallIcons = 0;

    for (const icon of icons) {
      const iconOriginal = fs.statSync(`images/${icon}.webp`);
      const iconOriginalSize = (iconOriginal.size / 1024).toFixed(2);
      totalOriginalIcons += iconOriginal.size;

      await sharp(`images/${icon}.webp`)
        .resize(128, 128, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
        .webp({ quality: 85, effort: 6 })
        .toFile(`images/${icon}-icon.webp`);

      const iconSmall = fs.statSync(`images/${icon}-icon.webp`);
      const iconSmallSize = (iconSmall.size / 1024).toFixed(2);
      totalSmallIcons += iconSmall.size;
      const iconSavings = ((1 - iconSmall.size / iconOriginal.size) * 100).toFixed(2);

      console.log(`   ${icon}.webp:`);
      console.log(`      Original: ${iconOriginalSize} KB`);
      console.log(`      Pequeño:  ${iconSmallSize} KB`);
      console.log(`      Ahorro:   ${iconSavings}%\n`);
    }

    // Resumen total
    const totalOriginal = logoOriginal.size + totalOriginalIcons;
    const totalSmall = logoSmall.size + totalSmallIcons;
    const totalSavings = ((1 - totalSmall / totalOriginal) * 100).toFixed(2);

    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━');
    console.log('📊 RESUMEN TOTAL:');
    console.log(`   Tamaño original:  ${(totalOriginal / 1024).toFixed(2)} KB`);
    console.log(`   Tamaño optimizado: ${(totalSmall / 1024).toFixed(2)} KB`);
    console.log(`   Ahorro total:      ${totalSavings}% (${((totalOriginal - totalSmall) / 1024).toFixed(2)} KB)`);
    console.log('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n');

    console.log('✨ Archivos generados:');
    console.log('   ✅ images/logo-small.webp');
    console.log('   ✅ images/precio-icon.webp');
    console.log('   ✅ images/cobertura-icon.webp');
    console.log('   ✅ images/rapidez-icon.webp');
    console.log('   ✅ images/profesionalidad-icon.webp\n');

    console.log('🎉 Optimización completada exitosamente!');

  } catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
  }
}

optimizeSmallImages();
