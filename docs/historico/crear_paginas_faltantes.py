#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para crear páginas HTML faltantes de municipios
Usa almeria/index.html como template base
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"
TEMPLATE_PATH = MUNICIPIOS_DIR / "almeria" / "index.html"

# Municipios faltantes (los que tienen directorio pero no index.html)
MUNICIPIOS_FALTANTES = [
    "turre", "gallardos-los", "huercal-de-almeria", "fondon",
    "laujar-de-andarax", "sorbas", "lucainena-de-las-torres",
    "instincion", "santa-fe-de-mondujar", "gador", "ohanes",
    "zurgena", "paterna-del-rio", "ragol", "gergal", "velefique",
    "velez-blanco", "velez-rubio", "maria", "rioja", "tijola", "seron"
]

# Datos básicos de cada municipio (nombre display)
DATOS_MUNICIPIOS = {
    "turre": {"nombre": "Turre", "poblacion": "3.200", "altitud": "200"},
    "gallardos-los": {"nombre": "Los Gallardos", "poblacion": "3.500", "altitud": "90"},
    "huercal-de-almeria": {"nombre": "Huércal de Almería", "poblacion": "16.000", "altitud": "76"},
    "fondon": {"nombre": "Fondón", "poblacion": "1.000", "altitud": "900"},
    "laujar-de-andarax": {"nombre": "Laujar de Andarax", "poblacion": "1.700", "altitud": "920"},
    "sorbas": {"nombre": "Sorbas", "poblacion": "2.400", "altitud": "408"},
    "lucainena-de-las-torres": {"nombre": "Lucainena de las Torres", "poblacion": "600", "altitud": "520"},
    "instincion": {"nombre": "Instinción", "poblacion": "500", "altitud": "650"},
    "santa-fe-de-mondujar": {"nombre": "Santa Fe de Mondújar", "poblacion": "500", "altitud": "430"},
    "gador": {"nombre": "Gádor", "poblacion": "3.000", "altitud": "250"},
    "ohanes": {"nombre": "Ohanes", "poblacion": "600", "altitud": "700"},
    "zurgena": {"nombre": "Zurgena", "poblacion": "3.200", "altitud": "250"},
    "paterna-del-rio": {"nombre": "Paterna del Río", "poblacion": "450", "altitud": "885"},
    "ragol": {"nombre": "Rágol", "poblacion": "300", "altitud": "642"},
    "gergal": {"nombre": "Gérgal", "poblacion": "1.100", "altitud": "910"},
    "velefique": {"nombre": "Velefique", "poblacion": "300", "altitud": "1.100"},
    "velez-blanco": {"nombre": "Vélez-Blanco", "poblacion": "1.900", "altitud": "1.070"},
    "velez-rubio": {"nombre": "Vélez-Rubio", "poblacion": "6.500", "altitud": "890"},
    "maria": {"nombre": "María", "poblacion": "500", "altitud": "1.225"},
    "rioja": {"nombre": "Rioja", "poblacion": "1.500", "altitud": "950"},
    "tijola": {"nombre": "Tíjola", "poblacion": "3.500", "altitud": "595"},
    "seron": {"nombre": "Serón", "poblacion": "2.300", "altitud": "1.020"}
}


def leer_template():
    """Lee el archivo template de Almería"""
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()


def adaptar_template(template_html, carpeta_municipio):
    """Adapta el template para un municipio específico"""

    datos = DATOS_MUNICIPIOS[carpeta_municipio]
    nombre = datos["nombre"]
    nombre_lower = nombre.lower()

    # Reemplazos principales
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
        f'<meta name="keywords" content="certificado energético {nombre_lower}, eficiencia energética {nombre_lower}, arquitecto técnico {nombre_lower}, certificado energético precio {nombre_lower}">',
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

    # WhatsApp links (actualizar mensaje)
    nuevo_html = re.sub(
        r'necesito%20certificado%20energético%20en%20Almería%20capital',
        f'necesito%20certificado%20energético%20en%20{nombre.replace(" ", "%20")}',
        nuevo_html
    )

    return nuevo_html


def crear_pagina(carpeta_municipio):
    """Crea el archivo index.html para un municipio"""

    # Verificar que el directorio existe
    dir_path = MUNICIPIOS_DIR / carpeta_municipio
    if not dir_path.exists():
        print(f"ERROR Directorio no existe: {carpeta_municipio}")
        return False

    # Verificar que no existe ya el archivo
    index_path = dir_path / "index.html"
    if index_path.exists():
        print(f"SKIP Ya existe: {carpeta_municipio}/index.html")
        return False

    # Leer template
    template = leer_template()

    # Adaptar para este municipio
    nuevo_html = adaptar_template(template, carpeta_municipio)

    # Guardar archivo
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(nuevo_html)

    print(f"OK Creado: {carpeta_municipio}/index.html")
    return True


def main():
    print("=" * 60)
    print("CREACION DE PAGINAS HTML FALTANTES")
    print("=" * 60)
    print()

    # Verificar que existe el template
    if not TEMPLATE_PATH.exists():
        print(f"ERROR No se encuentra el template: {TEMPLATE_PATH}")
        return

    print(f"Template base: {TEMPLATE_PATH}")
    print(f"Municipios a crear: {len(MUNICIPIOS_FALTANTES)}")
    print()

    # Crear cada página
    exitosos = 0
    fallidos = 0

    for municipio in MUNICIPIOS_FALTANTES:
        if crear_pagina(municipio):
            exitosos += 1
        else:
            fallidos += 1

    print()
    print("=" * 60)
    print(f"RESUMEN: {exitosos} creados, {fallidos} fallidos/skipped de {len(MUNICIPIOS_FALTANTES)} total")
    print("=" * 60)


if __name__ == '__main__':
    main()
