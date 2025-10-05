#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crea páginas completas para los 4 municipios faltantes
"""

import re
from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"
TEMPLATE_PATH = MUNICIPIOS_DIR / "almeria" / "index.html"

# Datos de los 4 municipios faltantes
MUNICIPIOS_FALTANTES = {
    "albanchez": {
        "nombre": "Albánchez",
        "hab": "850",
        "alt": "780m",
        "zona": "D3",
        "comarca": "Alto Almanzora"
    },
    "balanegra": {
        "nombre": "Balanegra",
        "hab": "3.200",
        "alt": "42m",
        "zona": "A4",
        "comarca": "Poniente Almeriense"
    },
    "finana": {
        "nombre": "Fiñana",
        "hab": "2.300",
        "alt": "970m",
        "zona": "D3",
        "comarca": "Los Filabres-Tabernas"
    },
    "olula-de-castro": {
        "nombre": "Olula de Castro",
        "hab": "150",
        "alt": "860m",
        "zona": "D3",
        "comarca": "Alto Almanzora"
    }
}

def leer_template():
    """Lee el template de Almería"""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def adaptar_template(template_html, carpeta_municipio):
    """Adapta el template para un municipio específico"""
    datos = MUNICIPIOS_FALTANTES[carpeta_municipio]
    nombre = datos["nombre"]
    nombre_lower = nombre.lower()

    nuevo_html = template_html

    # Title tag
    nuevo_html = re.sub(
        r'<title>.*?</title>',
        f'<title>Certificado Energético {nombre} 75€ | Arquitecto Técnico COAAT 1.440 | 24-48h</title>',
        nuevo_html
    )

    # Meta description
    nuevo_html = re.sub(
        r'<meta name="description" content=".*?">',
        f'<meta name="description" content="Certificado energético {nombre} 75€ todo incluido. Raúl Cañadas, Arquitecto Técnico COAAT 1.440. Entrega 24-48h garantizada.">',
        nuevo_html
    )

    # Meta keywords
    nuevo_html = re.sub(
        r'<meta name="keywords" content=".*?">',
        f'<meta name="keywords" content="certificado energético {nombre_lower}, eficiencia energética {nombre_lower}, arquitecto técnico {nombre_lower}">',
        nuevo_html
    )

    # Open Graph title
    nuevo_html = re.sub(
        r'<meta property="og:title" content=".*?">',
        f'<meta property="og:title" content="Certificado Energético {nombre} 75€ | Arquitecto Técnico COAAT 1.440">',
        nuevo_html
    )

    # Open Graph description
    nuevo_html = re.sub(
        r'<meta property="og:description" content=".*?">',
        f'<meta property="og:description" content="Certificado energético {nombre} 75€ todo incluido. Arquitecto técnico colegiado COAAT 1.440.">',
        nuevo_html
    )

    # Canonical URL
    nuevo_html = re.sub(
        r'<link rel="canonical" href=".*?">',
        f'<link rel="canonical" href="https://www.certialmeria.es/municipios/{carpeta_municipio}/">',
        nuevo_html
    )

    # WhatsApp links
    nuevo_html = re.sub(
        r'necesito%20certificado%20energético%20en%20Almería%20capital',
        f'necesito%20certificado%20energético%20en%20{nombre.replace(" ", "%20")}',
        nuevo_html
    )

    return nuevo_html

def generar_contenido_unico(carpeta_municipio):
    """Genera contenido HTML único para el municipio"""
    datos = MUNICIPIOS_FALTANTES[carpeta_municipio]
    nombre = datos["nombre"]
    hab = datos["hab"]
    alt = datos["alt"]
    zona = datos["zona"]
    comarca = datos["comarca"]

    # Texto según zona climática
    if zona == "A4":
        clima_texto = "clima suave costero con demanda energética equilibrada entre calefacción y refrigeración"
    elif zona == "C3":
        clima_texto = "demanda de calefacción prioritaria por la altitud"
    elif zona == "D3":
        clima_texto = "demanda de calefacción muy alta por la altitud elevada"
    else:  # E1
        clima_texto = "demanda de calefacción extrema por máxima altitud"

    html = f'''<section class="container-custom py-16">
    <div class="max-w-4xl mx-auto">

        <h2 class="text-3xl font-bold text-neutral-900 mb-6">Certificado Energético en {nombre}</h2>

        <p class="text-lg leading-relaxed mb-6">
            Certificado energético en {nombre} ({hab} habitantes, {alt} altitud) en {comarca}. <strong>Zona climática {zona}</strong> según el Código Técnico de la Edificación, con {clima_texto}. Servicio profesional 75€ todo incluido con visita presencial en todo el municipio.
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
</section>'''

    return html

def limpiar_contenido_almeria(html):
    """Elimina el contenido de Almería entre </header> y <footer>"""
    patron = r'(</header>|</nav>)(.*?)(<footer)'

    def reemplazo(match):
        return match.group(1) + '\n\n' + match.group(3)

    return re.sub(patron, reemplazo, html, flags=re.DOTALL)

def insertar_contenido(html_base, contenido_unico):
    """Inserta contenido único antes del footer"""
    return html_base.replace('<footer', f'{contenido_unico}\n\n<footer')

def crear_pagina(carpeta_municipio):
    """Crea la página completa para un municipio"""

    # Leer template
    template = leer_template()

    # Adaptar meta tags
    html_adaptado = adaptar_template(template, carpeta_municipio)

    # Limpiar contenido de Almería
    html_limpio = limpiar_contenido_almeria(html_adaptado)

    # Generar contenido único
    contenido_unico = generar_contenido_unico(carpeta_municipio)

    # Insertar contenido único
    html_final = insertar_contenido(html_limpio, contenido_unico)

    # Guardar
    index_path = MUNICIPIOS_DIR / carpeta_municipio / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_final)

    print(f"OK Creado: {carpeta_municipio}/index.html")
    return True

def main():
    print("=" * 60)
    print("CREACION 4 MUNICIPIOS FALTANTES")
    print("=" * 60)
    print()

    if not TEMPLATE_PATH.exists():
        print(f"ERROR No se encuentra template: {TEMPLATE_PATH}")
        return

    print(f"Template: {TEMPLATE_PATH}")
    print(f"Municipios a crear: {len(MUNICIPIOS_FALTANTES)}")
    print()

    exitosos = 0
    for municipio in sorted(MUNICIPIOS_FALTANTES.keys()):
        if crear_pagina(municipio):
            exitosos += 1

    print()
    print("=" * 60)
    print(f"COMPLETADO: {exitosos} páginas creadas")
    print("=" * 60)

if __name__ == '__main__':
    main()
