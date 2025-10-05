#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Encuentra los 4 municipios que faltan de los 103 oficiales
"""

from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"

# Lista oficial de 103 municipios de Almería (fuente: Wikipedia)
MUNICIPIOS_OFICIALES = {
    "abla", "abrucena", "adra", "albanchez", "alboloduy", "albox", "alcolea",
    "alcontar", "alcudia-de-monteagud", "alhabia", "alhama-de-almeria", "alicun",
    "almeria", "almocita", "alsodux", "antas", "arboleas", "armuna-de-almanzora",
    "bacares", "balanegra", "bayarcal", "bayarque", "bedar", "beires", "benahadux",
    "benitagla", "benizalon", "bentarique", "berja", "canjayar", "cantoria",
    "carboneras", "castro-de-filabres", "chercos", "chirivel", "cobdar",
    "cuevas-del-almanzora", "dalias", "el-ejido", "enix", "felix", "fines", "finana",
    "fondon", "gador", "gallardos-los", "garrucha", "gergal", "huecija",
    "huercal-de-almeria", "huercal-overa", "illar", "instincion", "laroya",
    "laujar-de-andarax", "lijar", "lubrin", "lucainena-de-las-torres", "lucar",
    "macael", "maria", "mojacar", "la-mojonera", "nacimiento", "nijar", "ohanes",
    "olula-de-castro", "olula-del-rio", "oria", "padules", "partaloa",
    "paterna-del-rio", "pechina", "pulpi", "purchena", "ragol", "rioja",
    "roquetas-de-mar", "santa-cruz-de-marchena", "santa-fe-de-mondujar", "senes",
    "seron", "sierro", "sonontin", "sorbas", "sufli", "tabernas", "taberno",
    "tahal", "terque", "tijola", "tres-villas-las", "turre", "turrillas",
    "uleila-del-campo", "urracal", "velefique", "velez-blanco", "velez-rubio",
    "vera", "viator"
}

# Municipios que tenemos en directorios
municipios_existentes = set()
for dir_path in MUNICIPIOS_DIR.iterdir():
    if dir_path.is_dir():
        municipios_existentes.add(dir_path.name)

# Encontrar faltantes
faltantes = MUNICIPIOS_OFICIALES - municipios_existentes

print("=" * 60)
print("MUNICIPIOS FALTANTES DE LOS 103 OFICIALES")
print("=" * 60)
print()
print(f"Municipios oficiales: {len(MUNICIPIOS_OFICIALES)}")
print(f"Municipios en carpetas: {len(municipios_existentes)}")
print(f"FALTAN: {len(faltantes)}")
print()

if faltantes:
    print("MUNICIPIOS FALTANTES:")
    for m in sorted(faltantes):
        print(f"  - {m}")
else:
    print("✓ TODOS LOS MUNICIPIOS ESTÁN PRESENTES")

print()
print("=" * 60)
