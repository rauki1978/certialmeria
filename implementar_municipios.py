#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Implementación Masiva - Contenido Municipios
Inserta el contenido generado en las páginas de municipios
"""

import os
import re
from pathlib import Path

# Base directory
BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"

# Mapeo de municipios del archivo de contenido a carpetas reales
MUNICIPIO_MAPPING = {
    # Tier 1
    "almeria-capital": "almeria",
    "almeria": "almeria",
    "roquetas-de-mar": "roquetas-de-mar",
    "el-ejido": "el-ejido",
    "nijar": "nijar",
    "vera": "vera",
    # Tier 2
    "adra": "adra",
    "berja": "berja",
    "mojacar": "mojacar",
    "garrucha": "garrucha",
    "huercal-overa": "huercal-overa",
    "vicar": "vicar",
    # Tier 3
    "cuevas-del-almanzora": "cuevas-del-almanzora",
    "pulpi": "pulpi",
    "carboneras": "carboneras",
    "tabernas": "tabernas",
    "canjayar": "canjayar",
    "antas": "antas",
    "turre": "turre",
    "bedar": "bedar",
    "los-gallardos": "gallardos-los",
    "dalias": "dalias",
    "huercal-de-almeria": "huercal-de-almeria",
    "benahadux": "benahadux",
    "alhama-de-almeria": "alhama-de-almeria",
    "fondon": "fondon",
    "laujar-de-andarax": "laujar-de-andarax",
    "sorbas": "sorbas",
    "lucainena-de-las-torres": "lucainena-de-las-torres",
    "instincion": "instincion",
    "santa-fe-de-mondujar": "santa-fe-de-mondujar",
    "gador": "gador",
    # Tier 4 (complete list)
    "arboleas": "arboleas",
    "albox": "albox",
    "zurgena": "zurgena",
    "olula-del-rio": "olula-del-rio",
    "purchena": "purchena",
    "ohanes": "ohanes",
    "paterna-del-rio": "paterna-del-rio",
    "ragol": "ragol",
    "gergal": "gergal",
    "alhabia": "alhabia",
    "castro-de-filabres": "castro-de-filabres",
    "velefique": "velefique",
    "velez-blanco": "velez-blanco",
    "velez-rubio": "velez-rubio",
    "maria": "maria",
    "rioja": "rioja",
    "tijola": "tijola",
    "seron": "seron",
    "macael": "macael",
    "bacares": "bacares",
    "chirivel": "chirivel"
}

# Contenido por municipio (extraído del archivo CONTENIDO_MUNICIPIOS_TIER1.md)
# Este diccionario se llenará con el contenido real
CONTENIDO = {}

def extraer_contenido_de_archivo():
    """Extrae el contenido HTML del archivo de contenido generado"""
    archivo_contenido = BASE_DIR / "CONTENIDO_MUNICIPIOS_TIER1.md"

    with open(archivo_contenido, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # PATRON 1: Formato largo con bloques ```html
    # titulo → cualquier contenido → ```html → contenido → ```
    patron1 = r'###? \d+\. ([A-ZÑÁÉÍÓÚ\s\-]+).*?```html\n(.*?)\n```'
    matches1 = re.findall(patron1, contenido, re.DOTALL)

    # PATRON 2: Formato corto con HTML inline
    # ### 37. NOMBRE\n**Datos**: ...\n**HTML**: `<html...>`
    patron2 = r'###? \d+\. ([A-ZÑÁÉÍÓÚ\s\-]+)\n\*\*Datos\*\*:.*?\n\*\*HTML\*\*: `(.*?)`'
    matches2 = re.findall(patron2, contenido, re.DOTALL)

    # Combinar ambos
    all_matches = matches1 + matches2

    for nombre, html in all_matches:
        nombre_lower = nombre.lower().strip()
        nombre_normalizado = nombre_lower.replace(' ', '-').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n')

        if nombre_normalizado in MUNICIPIO_MAPPING:
            CONTENIDO[MUNICIPIO_MAPPING[nombre_normalizado]] = html.strip()

    print(f"OK Extraido contenido para {len(CONTENIDO)} municipios")

def insertar_contenido(municipio_carpeta, contenido_html):
    """Inserta el contenido en el archivo index.html del municipio"""
    index_path = MUNICIPIOS_DIR / municipio_carpeta / "index.html"

    if not index_path.exists():
        print(f"ERROR No existe: {index_path}")
        return False

    # Leer archivo actual
    with open(index_path, 'r', encoding='utf-8') as f:
        html_actual = f.read()

    # Buscar donde insertar (después del header/nav, antes del footer)
    # Patrón: después de </header> o </nav>, antes de <footer>

    # Encontrar posición de inserción
    if '<main' in html_actual:
        # Si ya tiene <main>, reemplazar su contenido
        patron_main = r'(<main[^>]*>)(.*?)(</main>)'
        if re.search(patron_main, html_actual, re.DOTALL):
            html_nuevo = re.sub(patron_main, rf'\1\n{contenido_html}\n\3', html_actual, flags=re.DOTALL)
        else:
            print(f"ERROR No se encontro cierre </main> en {municipio_carpeta}")
            return False
    else:
        # Si no tiene <main>, insertar antes de <footer>
        if '<footer' in html_actual:
            html_nuevo = html_actual.replace('<footer', f'{contenido_html}\n\n<footer')
        else:
            print(f"ERROR No se encontro <footer> en {municipio_carpeta}")
            return False

    # Guardar archivo modificado
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_nuevo)

    print(f"OK Implementado: {municipio_carpeta}")
    return True

def main():
    print("=" * 60)
    print("IMPLEMENTACIÓN MASIVA - CONTENIDO MUNICIPIOS")
    print("=" * 60)
    print()

    # Extraer contenido del archivo
    extraer_contenido_de_archivo()
    print()

    # Implementar en cada municipio
    exitosos = 0
    fallidos = 0

    for carpeta in CONTENIDO.keys():
        if insertar_contenido(carpeta, CONTENIDO[carpeta]):
            exitosos += 1
        else:
            fallidos += 1

    print()
    print("=" * 60)
    print(f"RESUMEN: {exitosos} exitosos, {fallidos} fallidos de {len(CONTENIDO)} total")
    print("=" * 60)

if __name__ == '__main__':
    main()
