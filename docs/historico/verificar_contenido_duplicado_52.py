#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verifica qué municipios de los 52 con contenido custom TODAVÍA tienen contenido duplicado
"""

from pathlib import Path
import re

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"

# Los 52 municipios que deberían tener contenido CUSTOM (no el de Almería)
MUNICIPIOS_52 = [
    "almeria", "roquetas-de-mar", "el-ejido", "nijar", "vera",
    "adra", "berja", "mojacar", "garrucha", "huercal-overa", "vicar",
    "cuevas-del-almanzora", "pulpi", "carboneras", "tabernas", "canjayar",
    "antas", "turre", "bedar", "gallardos-los", "dalias",
    "huercal-de-almeria", "benahadux", "alhama-de-almeria",
    "fondon", "laujar-de-andarax", "sorbas", "lucainena-de-las-torres",
    "instincion", "santa-fe-de-mondujar", "gador",
    "arboleas", "albox", "zurgena", "olula-del-rio", "purchena",
    "ohanes", "paterna-del-rio", "ragol", "gergal", "alhabia",
    "castro-de-filabres", "velefique", "velez-blanco", "velez-rubio",
    "maria", "rioja", "tijola", "seron", "macael", "bacares", "chirivel"
]

# Marcador de contenido duplicado de Almería
MARCADOR_ALMERIA = "Base Principal en Almería"

print("=" * 60)
print("VERIFICACION CONTENIDO DUPLICADO - 52 MUNICIPIOS")
print("=" * 60)
print()

con_duplicado = []

for municipio in MUNICIPIOS_52:
    index_path = MUNICIPIOS_DIR / municipio / "index.html"

    if not index_path.exists():
        print(f"SKIP No existe: {municipio}")
        continue

    with open(index_path, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # Contar apariciones (almeria debe tener 1, los demás 0)
    count = contenido.count(MARCADOR_ALMERIA)

    if municipio == "almeria":
        if count == 0:
            print(f"ERROR Almería NO tiene su propio contenido!")
        # Almería es correcto que tenga este texto
    else:
        if count > 0:
            con_duplicado.append(municipio)
            print(f"DUPLICADO: {municipio} ({count} veces)")

print()
print("=" * 60)
if con_duplicado:
    print(f"PROBLEMA: {len(con_duplicado)} municipios con contenido duplicado:")
    for m in con_duplicado:
        print(f"  - {m}")
else:
    print("OK: Todos los municipios tienen contenido único")
print("=" * 60)
