#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Limpia contenido duplicado de los 22 municipios y re-implementa contenido único
"""

import re
from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"
CONTENIDO_FILE = BASE_DIR / "CONTENIDO_MUNICIPIOS_TIER1.md"

# Los 22 municipios con contenido duplicado
MUNICIPIOS_22 = [
    "turre", "gallardos-los", "huercal-de-almeria", "fondon",
    "laujar-de-andarax", "sorbas", "lucainena-de-las-torres",
    "instincion", "santa-fe-de-mondujar", "gador", "zurgena",
    "ohanes", "paterna-del-rio", "ragol", "gergal", "velefique",
    "velez-blanco", "velez-rubio", "maria", "rioja", "tijola", "seron"
]

# Contenido extraído
CONTENIDO = {}

def extraer_contenido():
    """Extrae contenido del archivo TIER1"""
    with open(CONTENIDO_FILE, 'r', encoding='utf-8') as f:
        contenido_md = f.read()

    # Patrón 1: Formato largo
    patron1 = r'###? \d+\. ([A-ZÑÁÉÍÓÚ\s\-]+).*?```html\n(.*?)\n```'
    matches1 = re.findall(patron1, contenido_md, re.DOTALL)

    # Patrón 2: Formato corto inline
    patron2 = r'###? \d+\. ([A-ZÑÁÉÍÓÚ\s\-]+)\n\*\*Datos\*\*:.*?\n\*\*HTML\*\*: `(.*?)`'
    matches2 = re.findall(patron2, contenido_md, re.DOTALL)

    all_matches = matches1 + matches2

    for nombre, html in all_matches:
        nombre_lower = nombre.lower().strip()
        nombre_normalizado = nombre_lower.replace(' ', '-').replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ', 'n')

        # Mapeo especial
        if nombre_normalizado == "los-gallardos":
            nombre_normalizado = "gallardos-los"

        CONTENIDO[nombre_normalizado] = html.strip()

    print(f"OK Extraido contenido para {len(CONTENIDO)} municipios del archivo TIER1")

def limpiar_y_reimplementar(municipio):
    """Limpia contenido duplicado y reimplementa el correcto"""
    index_path = MUNICIPIOS_DIR / municipio / "index.html"

    if not index_path.exists():
        print(f"ERROR No existe: {municipio}")
        return False

    if municipio not in CONTENIDO:
        print(f"SKIP No hay contenido custom para: {municipio}")
        return False

    # Leer HTML
    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # PASO 1: Limpiar contenido entre </header> y <footer>
    patron_limpiar = r'(</header>|</nav>)(.*?)(<footer)'

    def reemplazo_limpiar(match):
        return match.group(1) + '\n\n' + match.group(3)

    html_limpio = re.sub(patron_limpiar, reemplazo_limpiar, html, flags=re.DOTALL)

    # PASO 2: Insertar contenido único antes de <footer>
    contenido_unico = CONTENIDO[municipio]
    html_final = html_limpio.replace('<footer', f'{contenido_unico}\n\n<footer')

    # Guardar
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_final)

    print(f"OK Limpiado y reimplementado: {municipio}")
    return True

def main():
    print("=" * 60)
    print("LIMPIEZA Y REIMPLEMENTACION 22 MUNICIPIOS")
    print("=" * 60)
    print()

    # Extraer contenido
    extraer_contenido()
    print()

    # Procesar cada municipio
    exitosos = 0
    fallidos = 0

    for municipio in MUNICIPIOS_22:
        if limpiar_y_reimplementar(municipio):
            exitosos += 1
        else:
            fallidos += 1

    print()
    print("=" * 60)
    print(f"RESUMEN: {exitosos} exitosos, {fallidos} fallidos de {len(MUNICIPIOS_22)} total")
    print("=" * 60)

if __name__ == '__main__':
    main()
