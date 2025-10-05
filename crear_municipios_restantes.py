#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crea páginas para los 25 municipios restantes sin index.html
"""

import os
import re
from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"
TEMPLATE_PATH = MUNICIPIOS_DIR / "almeria" / "index.html"

# 25 municipios sin index.html con datos básicos
MUNICIPIOS_RESTANTES = {
    "fines": {"nombre": "Fines", "poblacion": "1.800", "altitud": "470"},
    "huecija": {"nombre": "Huécija", "poblacion": "600", "altitud": "480"},
    "illar": {"nombre": "Illar", "poblacion": "400", "altitud": "570"},
    "laroya": {"nombre": "Laroya", "poblacion": "150", "altitud": "750"},
    "lijar": {"nombre": "Líjar", "poblacion": "400", "altitud": "645"},
    "lubrin": {"nombre": "Lubrín", "poblacion": "1.500", "altitud": "500"},
    "lucar": {"nombre": "Lúcar", "poblacion": "500", "altitud": "900"},
    "nacimiento": {"nombre": "Nacimiento", "poblacion": "400", "altitud": "920"},
    "oria": {"nombre": "Oria", "poblacion": "2.200", "altitud": "450"},
    "padules": {"nombre": "Padules", "poblacion": "500", "altitud": "570"},
    "partaloa": {"nombre": "Partaloa", "poblacion": "700", "altitud": "820"},
    "pechina": {"nombre": "Pechina", "poblacion": "5.500", "altitud": "108"},
    "santa-cruz-de-marchena": {"nombre": "Santa Cruz de Marchena", "poblacion": "300", "altitud": "780"},
    "senes": {"nombre": "Senes", "poblacion": "250", "altitud": "880"},
    "sierro": {"nombre": "Sierro", "poblacion": "400", "altitud": "680"},
    "sonontin": {"nombre": "Sonontín", "poblacion": "300", "altitud": "690"},
    "sufli": {"nombre": "Suflí", "poblacion": "300", "altitud": "640"},
    "taberno": {"nombre": "Taberno", "poblacion": "1.100", "altitud": "400"},
    "tahal": {"nombre": "Tahal", "poblacion": "300", "altitud": "850"},
    "terque": {"nombre": "Terque", "poblacion": "400", "altitud": "490"},
    "tres-villas-las": {"nombre": "Las Tres Villas", "poblacion": "650", "altitud": "1.080"},
    "turrillas": {"nombre": "Turrillas", "poblacion": "250", "altitud": "950"},
    "uleila-del-campo": {"nombre": "Uleila del Campo", "poblacion": "800", "altitud": "450"},
    "urracal": {"nombre": "Urracal", "poblacion": "350", "altitud": "780"},
    "viator": {"nombre": "Viator", "poblacion": "6.000", "altitud": "90"}
}

def leer_template():
    """Lee el archivo template de Almería"""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def adaptar_template(template_html, carpeta_municipio):
    """Adapta el template para un municipio específico"""
    datos = MUNICIPIOS_RESTANTES[carpeta_municipio]
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

def crear_pagina(carpeta_municipio):
    """Crea el archivo index.html para un municipio"""
    dir_path = MUNICIPIOS_DIR / carpeta_municipio

    if not dir_path.exists():
        print(f"ERROR Directorio no existe: {carpeta_municipio}")
        return False

    index_path = dir_path / "index.html"
    if index_path.exists():
        print(f"SKIP Ya existe: {carpeta_municipio}/index.html")
        return False

    template = leer_template()
    nuevo_html = adaptar_template(template, carpeta_municipio)

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(nuevo_html)

    print(f"OK Creado: {carpeta_municipio}/index.html")
    return True

def main():
    print("=" * 60)
    print("CREACION PAGINAS 25 MUNICIPIOS RESTANTES")
    print("=" * 60)
    print()

    if not TEMPLATE_PATH.exists():
        print(f"ERROR No se encuentra el template: {TEMPLATE_PATH}")
        return

    print(f"Template base: {TEMPLATE_PATH}")
    print(f"Municipios a crear: {len(MUNICIPIOS_RESTANTES)}")
    print()

    exitosos = 0
    fallidos = 0

    for municipio in sorted(MUNICIPIOS_RESTANTES.keys()):
        if crear_pagina(municipio):
            exitosos += 1
        else:
            fallidos += 1

    print()
    print("=" * 60)
    print(f"RESUMEN: {exitosos} creados, {fallidos} fallidos/skipped")
    print("=" * 60)

if __name__ == '__main__':
    main()
