#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Genera contenido HTML único compacto para 51 municipios restantes
"""

from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
OUTPUT_FILE = BASE_DIR / "CONTENIDO_51_MUNICIPIOS.md"

# Datos de los 51 municipios restantes (sin contenido custom)
MUNICIPIOS = {
    # Costa y Metropolitana
    "pechina": {"nombre": "Pechina", "hab": "5.500", "alt": "108m", "zona": "B3", "comarca": "Metropolitana"},
    "viator": {"nombre": "Viator", "hab": "6.000", "alt": "90m", "zona": "B3", "comarca": "Metropolitana"},

    # Valle Almanzora
    "oria": {"nombre": "Oria", "hab": "2.200", "alt": "450m", "zona": "C3", "comarca": "Valle Almanzora"},
    "fines": {"nombre": "Fines", "hab": "1.800", "alt": "470m", "zona": "C3", "comarca": "Valle Almanzora"},
    "lubrin": {"nombre": "Lubrín", "hab": "1.500", "alt": "500m", "zona": "C3", "comarca": "Sierra Cabrera"},
    "taberno": {"nombre": "Taberno", "hab": "1.100", "alt": "400m", "zona": "C3", "comarca": "Valle Almanzora"},
    "uleila-del-campo": {"nombre": "Uleila del Campo", "hab": "800", "alt": "450m", "zona": "C3", "comarca": "Valle Almanzora"},

    # Alpujarra y Andarax
    "huecija": {"nombre": "Huécija", "hab": "600", "alt": "480m", "zona": "C3", "comarca": "Valle Andarax"},
    "terque": {"nombre": "Terque", "hab": "400", "alt": "490m", "zona": "C3", "comarca": "Valle Andarax"},
    "padules": {"nombre": "Padules", "hab": "500", "alt": "570m", "zona": "C3", "comarca": "Valle Andarax"},
    "illar": {"nombre": "Illar", "hab": "400", "alt": "570m", "zona": "C3", "comarca": "Valle Andarax"},
    "lijar": {"nombre": "Líjar", "hab": "400", "alt": "645m", "zona": "C3", "comarca": "Alpujarra"},
    "bentarique": {"nombre": "Bentarique", "hab": "550", "alt": "520m", "zona": "C3", "comarca": "Alpujarra"},

    # Sierra Filabres
    "tahal": {"nombre": "Tahal", "hab": "300", "alt": "850m", "zona": "D3", "comarca": "Sierra Filabres"},
    "senes": {"nombre": "Senes", "hab": "250", "alt": "880m", "zona": "D3", "comarca": "Sierra Filabres"},
    "lucar": {"nombre": "Lúcar", "hab": "500", "alt": "900m", "zona": "D3", "comarca": "Sierra Filabres"},
    "turrillas": {"nombre": "Turrillas", "hab": "250", "alt": "950m", "zona": "D3", "comarca": "Sierra Filabres"},
    "nacimiento": {"nombre": "Nacimiento", "hab": "400", "alt": "920m", "zona": "D3", "comarca": "Sierra Filabres"},

    # Alto Almanzora
    "laroya": {"nombre": "Laroya", "hab": "150", "alt": "750m", "zona": "D3", "comarca": "Alto Almanzora"},
    "sierro": {"nombre": "Sierro", "hab": "400", "alt": "680m", "zona": "C3", "comarca": "Alto Almanzora"},
    "sufli": {"nombre": "Suflí", "hab": "300", "alt": "640m", "zona": "C3", "comarca": "Alto Almanzora"},
    "sonontin": {"nombre": "Sonontín", "hab": "300", "alt": "690m", "zona": "C3", "comarca": "Alto Almanzora"},
    "partaloa": {"nombre": "Partaloa", "hab": "700", "alt": "820m", "zona": "D3", "comarca": "Alto Almanzora"},
    "urracal": {"nombre": "Urracal", "hab": "350", "alt": "780m", "zona": "D3", "comarca": "Alto Almanzora"},
    "santa-cruz-de-marchena": {"nombre": "Santa Cruz de Marchena", "hab": "300", "alt": "780m", "zona": "D3", "comarca": "Alto Almanzora"},
    "tres-villas-las": {"nombre": "Las Tres Villas", "hab": "650", "alt": "1.080m", "zona": "D3", "comarca": "Los Vélez"},
}

def generar_html(carpeta, datos):
    """Genera HTML único para un municipio"""

    nombre = datos["nombre"]
    hab = datos["hab"]
    alt = datos["alt"]
    zona = datos["zona"]
    comarca = datos["comarca"]

    # Texto específico según zona climática
    if zona == "B3":
        demanda_texto = "demanda energética equilibrada entre calefacción y refrigeración"
    elif zona == "C3":
        demanda_texto = "demanda de calefacción prioritaria por la altitud"
    else:  # D3, E1
        demanda_texto = "demanda de calefacción muy alta debido a la altitud"

    html = f'''### {nombre.upper()}
**Carpeta**: {carpeta}
**Datos**: {hab} hab | {alt} | {zona} | {comarca}

```html
<section class="container-custom py-16">
    <div class="max-w-4xl mx-auto">

        <h2 class="text-3xl font-bold text-neutral-900 mb-6">Certificado Energético en {nombre}</h2>

        <p class="text-lg leading-relaxed mb-6">
            {nombre} ({hab} habitantes, {alt} altitud) en {comarca}. <strong>Zona climática {zona}</strong> según el CTE con {demanda_texto}. Certificado energético profesional 75€ todo incluido.
        </p>

        <p class="text-lg leading-relaxed mb-6">
            Como Arquitecto Técnico COAAT 1.440 especializado en la provincia de Almería, conozco las características constructivas de {nombre} y realizo certificados energéticos con visita presencial, elaboración profesional y registro oficial incluido.
        </p>

        <div class="bg-gradient-to-r from-primary/20 to-secondary/20 p-8 rounded-2xl mb-8">
            <h3 class="text-2xl font-bold text-primary mb-4">75€ Todo Incluido en {nombre}</h3>
            <ul class="space-y-3 text-lg">
                <li>✓ Visita técnica presencial</li>
                <li>✓ Arquitecto Técnico COAAT 1.440</li>
                <li>✓ Registro Junta de Andalucía</li>
                <li>✓ Entrega 24-48 horas</li>
            </ul>
        </div>

        <div class="grid md:grid-cols-2 gap-6 mb-8">
            <a href="tel:+34667451538" class="flex items-center justify-center gap-3 bg-gradient-to-r from-primary to-secondary text-white px-8 py-5 rounded-full text-xl font-bold hover:from-secondary hover:to-primary transition-all duration-300">
                📞 667 45 15 38
            </a>
            <a href="https://wa.me/34667451538?text=Hola,%20necesito%20certificado%20energético%20en%20{nombre.replace(" ", "%20")}" class="flex items-center justify-center gap-3 bg-gradient-to-r from-whatsapp to-green-600 text-white px-8 py-5 rounded-full text-xl font-bold hover:from-green-600 hover:to-whatsapp transition-all duration-300">
                💬 WhatsApp
            </a>
        </div>

    </div>
</section>
```

---

'''
    return html

def main():
    print("Generando contenido para 51 municipios restantes...")

    contenido_completo = '''# CONTENIDO ÚNICO - 51 MUNICIPIOS RESTANTES

**Formato**: Ultra-compacto 150-200 palabras
**Objetivo**: Evitar contenido duplicado, capturar long-tail keywords
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
    print(f"Contenido generado: {OUTPUT_FILE}")
    print(f"Total municipios: {len(MUNICIPIOS)}")

if __name__ == '__main__':
    main()
