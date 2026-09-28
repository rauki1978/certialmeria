#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lista municipios que NO tienen contenido custom generado
"""

from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"

# Los 52 con contenido custom YA generado
CON_CONTENIDO = {
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
}

sin_contenido = []

for dir_path in sorted(MUNICIPIOS_DIR.iterdir()):
    if dir_path.is_dir() and dir_path.name not in CON_CONTENIDO:
        sin_contenido.append(dir_path.name)

print(f"Total municipios SIN contenido custom: {len(sin_contenido)}\n")
for m in sin_contenido:
    print(f"  \"{m}\",")
