#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementa contenido de los 47 municipios restantes en sus páginas HTML
"""

import os
import re
from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"
CONTENIDO_FILE = BASE_DIR / "CONTENIDO_47_MUNICIPIOS.md"

# Diccionario para almacenar contenido extraído
CONTENIDO = {}

def extraer_contenido():
    """Extrae contenido HTML del archivo markdown"""
    with open(CONTENIDO_FILE, 'r', encoding='utf-8') as f:
        contenido_md = f.read()

    # Patrón: **Carpeta**: `{nombre}` ... ```html ... ```
    patron = r'\*\*Carpeta\*\*: `([a-z0-9\-]+)`.*?```html\n(.*?)\n```'
    matches = re.findall(patron, contenido_md, re.DOTALL)

    for carpeta, html in matches:
        CONTENIDO[carpeta] = html.strip()

    print(f"OK Extraido contenido para {len(CONTENIDO)} municipios")

def insertar_contenido(municipio_carpeta):
    """Inserta contenido en la página HTML del municipio"""
    index_path = MUNICIPIOS_DIR / municipio_carpeta / "index.html"

    if not index_path.exists():
        print(f"ERROR No existe: {index_path}")
        return False

    # Leer HTML actual
    with open(index_path, 'r', encoding='utf-8') as f:
        html_actual = f.read()

    contenido_html = CONTENIDO[municipio_carpeta]

    # Buscar <main> o insertar antes de <footer>
    if '<main' in html_actual:
        # Reemplazar contenido de <main>
        patron_main = r'(<main[^>]*>)(.*?)(</main>)'
        if re.search(patron_main, html_actual, re.DOTALL):
            html_nuevo = re.sub(patron_main, rf'\1\n{contenido_html}\n\3', html_actual, flags=re.DOTALL)
        else:
            print(f"ERROR No se encontro cierre </main> en {municipio_carpeta}")
            return False
    else:
        # Insertar antes de <footer>
        if '<footer' in html_actual:
            html_nuevo = html_actual.replace('<footer', f'{contenido_html}\n\n<footer')
        else:
            print(f"ERROR No se encontro <footer> en {municipio_carpeta}")
            return False

    # Guardar
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_nuevo)

    print(f"OK Implementado: {municipio_carpeta}")
    return True

def main():
    print("=" * 60)
    print("IMPLEMENTACION 47 MUNICIPIOS RESTANTES")
    print("=" * 60)
    print()

    # Extraer contenido
    extraer_contenido()
    print()

    # Implementar en cada página
    exitosos = 0
    fallidos = 0

    for carpeta in sorted(CONTENIDO.keys()):
        if insertar_contenido(carpeta):
            exitosos += 1
        else:
            fallidos += 1

    print()
    print("=" * 60)
    print(f"RESUMEN: {exitosos} exitosos, {fallidos} fallidos de {len(CONTENIDO)} total")
    print("=" * 60)

if __name__ == '__main__':
    main()
