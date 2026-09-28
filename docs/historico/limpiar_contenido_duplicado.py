#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Limpia contenido duplicado de Almería en las páginas de municipios
ELIMINA todo entre </header> y <footer> para dejar solo estructura
"""

import re
from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"

# Los 47 municipios que necesitan limpieza
MUNICIPIOS_LIMPIAR = [
    "abla", "abrucena", "alboloduy", "alcolea", "alcontar",
    "alcudia-de-monteagud", "alicun", "almocita", "alsodux",
    "armuna-de-almanzora", "bayarcal", "bayarque", "beires",
    "benitagla", "benizalon", "bentarique", "cantoria",
    "chercos", "cobdar", "enix", "felix", "fines", "huecija",
    "illar", "la-mojonera", "laroya", "lijar", "lubrin",
    "lucar", "nacimiento", "oria", "padules", "partaloa",
    "pechina", "santa-cruz-de-marchena", "senes", "sierro",
    "sonontin", "sufli", "taberno", "tahal", "terque",
    "tres-villas-las", "turrillas", "uleila-del-campo",
    "urracal", "viator"
]

def limpiar_pagina(municipio):
    """Elimina contenido entre </header> y <footer>"""
    index_path = MUNICIPIOS_DIR / municipio / "index.html"

    if not index_path.exists():
        print(f"SKIP No existe: {municipio}")
        return False

    with open(index_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Buscar patrón: desde </header> o </nav> hasta <footer
    # ELIMINAR TODO ese contenido
    patron = r'(</header>|</nav>)(.*?)(<footer)'

    def reemplazo(match):
        # Mantener el cierre de header/nav y apertura de footer
        # Eliminar todo lo del medio
        return match.group(1) + '\n\n' + match.group(3)

    html_limpio = re.sub(patron, reemplazo, html, flags=re.DOTALL)

    # Guardar
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_limpio)

    print(f"OK Limpiado: {municipio}")
    return True

def main():
    print("=" * 60)
    print("LIMPIEZA CONTENIDO DUPLICADO")
    print("=" * 60)
    print()

    exitosos = 0
    for municipio in MUNICIPIOS_LIMPIAR:
        if limpiar_pagina(municipio):
            exitosos += 1

    print()
    print("=" * 60)
    print(f"COMPLETADO: {exitosos} páginas limpiadas")
    print("=" * 60)

if __name__ == '__main__':
    main()
