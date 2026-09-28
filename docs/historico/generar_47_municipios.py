#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera contenido HTML único compacto para los 47 municipios restantes
"""

from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
OUTPUT_FILE = BASE_DIR / "CONTENIDO_47_MUNICIPIOS.md"

# Los 47 municipios sin contenido custom con datos aprox
MUNICIPIOS = {
    # Metropolitana y costa
    "pechina": {"nombre": "Pechina", "hab": "5.500", "alt": "108m", "zona": "B3"},
    "viator": {"nombre": "Viator", "hab": "6.000", "alt": "90m", "zona": "B3"},
    "enix": {"nombre": "Enix", "hab": "450", "alt": "470m", "zona": "C3"},
    "felix": {"nombre": "Felix", "hab": "650", "alt": "520m", "zona": "C3"},
    "la-mojonera": {"nombre": "La Mojonera", "hab": "9.500", "alt": "71m", "zona": "B3"},

    # Alpujarra
    "bentarique": {"nombre": "Bentarique", "hab": "550", "alt": "520m", "zona": "C3"},
    "illar": {"nombre": "Illar", "hab": "400", "alt": "570m", "zona": "C3"},
    "lijar": {"nombre": "Líjar", "hab": "400", "alt": "645m", "zona": "C3"},
    "terque": {"nombre": "Terque", "hab": "400", "alt": "490m", "zona": "C3"},
    "huecija": {"nombre": "Huécija", "hab": "600", "alt": "480m", "zona": "C3"},
    "padules": {"nombre": "Padules", "hab": "500", "alt": "570m", "zona": "C3"},
    "alsodux": {"nombre": "Alsodux", "hab": "150", "alt": "640m", "zona": "C3"},
    "alboloduy": {"nombre": "Alboloduy", "hab": "600", "alt": "630m", "zona": "C3"},
    "almocita": {"nombre": "Almócita", "hab": "200", "alt": "940m", "zona": "D3"},
    "beires": {"nombre": "Beires", "hab": "200", "alt": "880m", "zona": "D3"},

    # Filabres
    "tahal": {"nombre": "Tahal", "hab": "300", "alt": "850m", "zona": "D3"},
    "senes": {"nombre": "Senes", "hab": "250", "alt": "880m", "zona": "D3"},
    "lucar": {"nombre": "Lúcar", "hab": "500", "alt": "900m", "zona": "D3"},
    "turrillas": {"nombre": "Turrillas", "hab": "250", "alt": "950m", "zona": "D3"},
    "nacimiento": {"nombre": "Nacimiento", "hab": "400", "alt": "920m", "zona": "D3"},
    "abla": {"nombre": "Abla", "hab": "1.300", "alt": "630m", "zona": "C3"},
    "abrucena": {"nombre": "Abrucena", "hab": "1.300", "alt": "890m", "zona": "D3"},

    # Almanzora
    "oria": {"nombre": "Oria", "hab": "2.200", "alt": "450m", "zona": "C3"},
    "fines": {"nombre": "Fines", "hab": "1.800", "alt": "470m", "zona": "C3"},
    "lubrin": {"nombre": "Lubrín", "hab": "1.500", "alt": "500m", "zona": "C3"},
    "taberno": {"nombre": "Taberno", "hab": "1.100", "alt": "400m", "zona": "C3"},
    "uleila-del-campo": {"nombre": "Uleila del Campo", "hab": "800", "alt": "450m", "zona": "C3"},
    "cantoria": {"nombre": "Cantoria", "hab": "3.200", "alt": "400m", "zona": "C3"},
    "armuna-de-almanzora": {"nombre": "Armuña de Almanzora", "hab": "1.100", "alt": "440m", "zona": "C3"},
    "laroya": {"nombre": "Laroya", "hab": "150", "alt": "750m", "zona": "D3"},
    "sierro": {"nombre": "Sierro", "hab": "400", "alt": "680m", "zona": "C3"},
    "sufli": {"nombre": "Suflí", "hab": "300", "alt": "640m", "zona": "C3"},
    "sonontin": {"nombre": "Sonontín", "hab": "300", "alt": "690m", "zona": "C3"},
    "partaloa": {"nombre": "Partaloa", "hab": "700", "alt": "820m", "zona": "D3"},
    "urracal": {"nombre": "Urracal", "hab": "350", "alt": "780m", "zona": "D3"},
    "santa-cruz-de-marchena": {"nombre": "Santa Cruz de Marchena", "hab": "300", "alt": "780m", "zona": "D3"},

    # Los Vélez
    "tres-villas-las": {"nombre": "Las Tres Villas", "hab": "650", "alt": "1.080m", "zona": "D3"},
    "alcontar": {"nombre": "Alcóntar", "hab": "300", "alt": "925m", "zona": "D3"},
    "chercos": {"nombre": "Chercos", "hab": "300", "alt": "900m", "zona": "D3"},

    # Varios
    "alcolea": {"nombre": "Alcolea", "hab": "900", "alt": "485m", "zona": "C3"},
    "alcudia-de-monteagud": {"nombre": "Alcudia de Monteagud", "hab": "250", "alt": "890m", "zona": "D3"},
    "alicun": {"nombre": "Alicún", "hab": "230", "alt": "900m", "zona": "D3"},
    "bayarcal": {"nombre": "Bayárcal", "hab": "350", "alt": "1.255m", "zona": "E1"},
    "bayarque": {"nombre": "Bayarque", "hab": "350", "alt": "930m", "zona": "D3"},
    "benitagla": {"nombre": "Benitagla", "hab": "200", "alt": "900m", "zona": "D3"},
    "benizalon": {"nombre": "Benizalón", "hab": "250", "alt": "890m", "zona": "D3"},
    "cobdar": {"nombre": "Cóbdar", "hab": "200", "alt": "700m", "zona": "C3"},
}

def generar_html(carpeta, datos):
    """Genera HTML único para un municipio"""
    nombre = datos["nombre"]
    hab = datos["hab"]
    alt = datos["alt"]
    zona = datos["zona"]

    # Texto según zona climática
    if zona == "B3":
        clima_texto = "clima suave con demanda energética equilibrada"
    elif zona == "C3":
        clima_texto = "demanda de calefacción prioritaria por la altitud"
    elif zona == "D3":
        clima_texto = "demanda de calefacción muy alta por la altitud elevada"
    else:  # E1
        clima_texto = "demanda de calefacción extrema por máxima altitud"

    html = f'''### {nombre.upper()}
**Carpeta**: `{carpeta}`

```html
<section class="container-custom py-16">
    <div class="max-w-4xl mx-auto">

        <h2 class="text-3xl font-bold text-neutral-900 mb-6">Certificado Energético en {nombre}</h2>

        <p class="text-lg leading-relaxed mb-6">
            Certificado energético en {nombre} ({hab} habitantes, {alt} altitud). <strong>Zona climática {zona}</strong> según el Código Técnico de la Edificación, con {clima_texto}. Servicio profesional 75€ todo incluido con visita presencial en todo el municipio.
        </p>

        <p class="text-lg leading-relaxed mb-6">
            Como Arquitecto Técnico colegiado COAAT 1.440 con 20 años de experiencia en la provincia de Almería, realizo certificados energéticos en {nombre} con atención personalizada. Incluye visita técnica, elaboración profesional y registro oficial en la Junta de Andalucía.
        </p>

        <div class="bg-gradient-to-r from-primary/20 to-secondary/20 p-8 rounded-2xl mb-8">
            <h3 class="text-2xl font-bold text-primary mb-4">75€ Todo Incluido - {nombre}</h3>
            <ul class="space-y-3 text-lg">
                <li>✓ Visita técnica presencial en {nombre}</li>
                <li>✓ Elaboración por Arquitecto Técnico COAAT 1.440</li>
                <li>✓ Registro oficial Junta de Andalucía incluido</li>
                <li>✓ Entrega garantizada en 24-48 horas</li>
            </ul>
        </div>

        <div class="grid md:grid-cols-2 gap-6 mb-8">
            <a href="tel:+34667451538" class="flex items-center justify-center gap-3 bg-gradient-to-r from-primary to-secondary text-white px-8 py-5 rounded-full text-xl font-bold hover:from-secondary hover:to-primary transition-all duration-300">
                📞 Llamar: 667 45 15 38
            </a>
            <a href="https://wa.me/34667451538?text=Hola,%20necesito%20certificado%20energético%20en%20{nombre.replace(" ", "%20")}" class="flex items-center justify-center gap-3 bg-gradient-to-r from-whatsapp to-green-600 text-white px-8 py-5 rounded-full text-xl font-bold hover:from-green-600 hover:to-whatsapp transition-all duration-300">
                💬 WhatsApp Directo
            </a>
        </div>

    </div>
</section>
```

---

'''
    return html

def main():
    print("=" * 60)
    print("GENERANDO CONTENIDO ÚNICO 47 MUNICIPIOS")
    print("=" * 60)
    print()

    contenido_completo = '''# CONTENIDO ÚNICO - 47 MUNICIPIOS RESTANTES

**Formato**: Ultra-compacto 150-180 palabras
**Objetivo**: Evitar contenido duplicado, SEO long-tail
**Fecha**: 2025-10-05

---

'''

    for carpeta, datos in sorted(MUNICIPIOS.items()):
        contenido_completo += generar_html(carpeta, datos)
        print(f"  OK {datos['nombre']}")

    # Guardar
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(contenido_completo)

    print()
    print("=" * 60)
    print(f"Contenido generado: {OUTPUT_FILE.name}")
    print(f"Total municipios: {len(MUNICIPIOS)}")
    print("=" * 60)

if __name__ == '__main__':
    main()
