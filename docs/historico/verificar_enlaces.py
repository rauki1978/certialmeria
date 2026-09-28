#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificación de enlaces y accesos a municipios
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"

# Lista de todos los municipios con contenido generado (52)
MUNICIPIOS_GENERADOS = [
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

def verificar_archivo_existe(municipio):
    """Verifica si existe el archivo index.html"""
    index_path = MUNICIPIOS_DIR / municipio / "index.html"
    return index_path.exists()

def verificar_contenido_insertado(municipio):
    """Verifica si el contenido único fue insertado (busca marcador)"""
    index_path = MUNICIPIOS_DIR / municipio / "index.html"

    if not index_path.exists():
        return False

    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            contenido = f.read()

        # Buscar indicadores de contenido insertado
        # (palabras clave específicas del contenido generado)
        marcadores = [
            "Zona Climática",
            "CTE DB-HE1",
            "zona climática",
            "Tipologías Constructivas"
        ]

        return any(marcador in contenido for marcador in marcadores)
    except:
        return False

def verificar_en_pagina_indice(municipio):
    """Verifica si el municipio está enlazado en /municipios/index.html"""
    index_municipios = MUNICIPIOS_DIR / "index.html"

    if not index_municipios.exists():
        return False

    try:
        with open(index_municipios, 'r', encoding='utf-8') as f:
            contenido = f.read()

        # Buscar el enlace al municipio
        enlace = f'href="/municipios/{municipio}/"'
        return enlace in contenido
    except:
        return False

def verificar_en_homepage():
    """Verifica enlaces desde la homepage"""
    homepage = BASE_DIR / "index.html"

    if not homepage.exists():
        return []

    enlaces_encontrados = []
    try:
        with open(homepage, 'r', encoding='utf-8') as f:
            contenido = f.read()

        for municipio in MUNICIPIOS_GENERADOS:
            enlace = f'/municipios/{municipio}/'
            if enlace in contenido:
                enlaces_encontrados.append(municipio)
    except:
        pass

    return enlaces_encontrados

def main():
    print("=" * 70)
    print("VERIFICACION DE ENLACES Y ACCESOS - MUNICIPIOS")
    print("=" * 70)
    print()

    # Análisis por municipio
    resultados = []

    for municipio in MUNICIPIOS_GENERADOS:
        existe = verificar_archivo_existe(municipio)
        tiene_contenido = verificar_contenido_insertado(municipio)
        en_indice = verificar_en_pagina_indice(municipio)

        resultados.append({
            'municipio': municipio,
            'existe': existe,
            'contenido': tiene_contenido,
            'en_indice': en_indice
        })

    # Verificar homepage
    en_homepage = verificar_en_homepage()

    # REPORTE
    print(f"Total municipios con contenido generado: {len(MUNICIPIOS_GENERADOS)}")
    print()

    # Estadísticas
    total_existen = sum(1 for r in resultados if r['existe'])
    total_con_contenido = sum(1 for r in resultados if r['contenido'])
    total_en_indice = sum(1 for r in resultados if r['en_indice'])

    print("ESTADISTICAS GLOBALES:")
    print(f"  Archivos index.html existentes:  {total_existen}/{len(MUNICIPIOS_GENERADOS)}")
    print(f"  Con contenido único insertado:    {total_con_contenido}/{len(MUNICIPIOS_GENERADOS)}")
    print(f"  Enlazados en /municipios/:        {total_en_indice}/{len(MUNICIPIOS_GENERADOS)}")
    print(f"  Enlazados en homepage:            {len(en_homepage)}/{len(MUNICIPIOS_GENERADOS)}")
    print()

    # Problemas detectados
    sin_archivo = [r['municipio'] for r in resultados if not r['existe']]
    sin_contenido = [r['municipio'] for r in resultados if r['existe'] and not r['contenido']]
    sin_enlace_indice = [r['municipio'] for r in resultados if r['existe'] and not r['en_indice']]

    if sin_archivo:
        print("CRITICO - Sin archivo index.html:")
        for m in sin_archivo:
            print(f"  - {m}")
        print()

    if sin_contenido:
        print("ADVERTENCIA - Sin contenido insertado:")
        for m in sin_contenido:
            print(f"  - {m}")
        print()

    if sin_enlace_indice:
        print("ADVERTENCIA - No enlazados en /municipios/index.html:")
        for m in sin_enlace_indice:
            print(f"  - {m}")
        print()

    # Resumen estado
    print("=" * 70)
    if not sin_archivo and not sin_contenido and total_en_indice == len(MUNICIPIOS_GENERADOS):
        print("STATUS: OK COMPLETO - Todos los municipios accesibles con contenido")
    elif not sin_archivo and not sin_contenido:
        print("STATUS: OK PARCIAL - Archivos completos, pero faltan enlaces en índice")
    else:
        print("STATUS: REQUIERE ACCION - Ver advertencias arriba")
    print("=" * 70)

if __name__ == '__main__':
    main()
