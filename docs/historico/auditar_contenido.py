#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditoría de Contenido - CertiAlmería
Analiza páginas de municipios y blog para detectar contenido faltante o insuficiente
"""

import os
import re
import json
from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime
from difflib import SequenceMatcher

# Configuración
BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")

# Umbrales de palabras
MUNICIPIO_MIN = 100
MUNICIPIO_IDEAL = 300
BLOG_MIN = 300
BLOG_IDEAL = 800

# Similitud para detectar duplicados (0.0 a 1.0)
SIMILITUD_DUPLICADO = 0.70


def limpiar_html(html_content):
    """Extrae texto limpio del HTML excluyendo header, footer, nav"""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Eliminar elementos que no son contenido
    for tag in soup(['header', 'footer', 'nav', 'script', 'style', 'noscript']):
        tag.decompose()

    # Obtener texto limpio
    texto = soup.get_text(separator=' ', strip=True)

    # Limpiar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)

    return texto.strip()


def contar_palabras(texto):
    """Cuenta palabras reales excluyendo números y símbolos solos"""
    palabras = re.findall(r'\b[a-záéíóúñüA-ZÁÉÍÓÚÑÜ]{3,}\b', texto)
    return len(palabras)


def extraer_headings(html_content):
    """Extrae H1, H2, H3 del contenido"""
    soup = BeautifulSoup(html_content, 'html.parser')

    headings = {
        'h1': [h.get_text(strip=True) for h in soup.find_all('h1')],
        'h2': [h.get_text(strip=True) for h in soup.find_all('h2')],
        'h3': [h.get_text(strip=True) for h in soup.find_all('h3')]
    }

    return headings


def extraer_meta(html_content):
    """Extrae meta title y description"""
    soup = BeautifulSoup(html_content, 'html.parser')

    title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else None

    meta_desc = soup.find('meta', attrs={'name': 'description'})
    description = meta_desc.get('content', '').strip() if meta_desc else None

    return {
        'title': title,
        'description': description
    }


def tiene_cta(html_content):
    """Detecta si tiene CTAs (teléfono o WhatsApp)"""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Buscar enlaces de teléfono o WhatsApp
    tel_links = soup.find_all('a', href=re.compile(r'tel:|wa\.me|whatsapp'))

    return len(tel_links) > 0


def calcular_similitud(texto1, texto2):
    """Calcula similitud entre dos textos (0.0 a 1.0)"""
    return SequenceMatcher(None, texto1, texto2).ratio()


def detectar_placeholders(texto):
    """Detecta si el texto contiene placeholders sin rellenar"""
    placeholders = [
        r'\{[A-Z_]+\}',
        r'Lorem ipsum',
        r'TODO:',
        r'placeholder',
        r'PLACEHOLDER',
        r'NOMBRE_MUNICIPIO',
        r'PROVINCIA'
    ]

    for pattern in placeholders:
        if re.search(pattern, texto, re.IGNORECASE):
            return True

    return False


def analizar_pagina(ruta_archivo, tipo='municipio'):
    """Analiza una página HTML y retorna sus métricas"""

    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        return {
            'error': f"No se pudo leer: {str(e)}",
            'estado': 'error'
        }

    # Extraer datos
    texto_limpio = limpiar_html(html_content)
    num_palabras = contar_palabras(texto_limpio)
    headings = extraer_headings(html_content)
    meta = extraer_meta(html_content)
    cta_presente = tiene_cta(html_content)
    tiene_placeholders = detectar_placeholders(html_content)

    # Determinar estado
    if tipo == 'municipio':
        min_palabras = MUNICIPIO_MIN
        ideal_palabras = MUNICIPIO_IDEAL
    else:  # blog
        min_palabras = BLOG_MIN
        ideal_palabras = BLOG_IDEAL

    if num_palabras < min_palabras or tiene_placeholders:
        estado = 'vacia' if num_palabras < 100 else 'insuficiente'
    elif num_palabras < ideal_palabras:
        estado = 'insuficiente'
    else:
        estado = 'completa'

    # Verificar estructura
    estructura_ok = (
        len(headings['h1']) > 0 and
        len(headings['h2']) >= 2 and
        meta['title'] is not None and
        meta['description'] is not None
    )

    if not estructura_ok and estado == 'completa':
        estado = 'insuficiente'

    return {
        'palabras': num_palabras,
        'headings': {
            'h1': len(headings['h1']),
            'h2': len(headings['h2']),
            'h3': len(headings['h3'])
        },
        'meta_title': meta['title'],
        'meta_description': meta['description'],
        'tiene_cta': cta_presente,
        'tiene_placeholders': tiene_placeholders,
        'estructura_ok': estructura_ok,
        'estado': estado,
        'texto_muestra': texto_limpio[:200]  # Para detección de duplicados
    }


def detectar_duplicados(resultados):
    """Detecta páginas duplicadas comparando contenido"""
    duplicados = []
    paginas = list(resultados.items())

    for i in range(len(paginas)):
        for j in range(i + 1, len(paginas)):
            url1, data1 = paginas[i]
            url2, data2 = paginas[j]

            if data1.get('estado') == 'error' or data2.get('estado') == 'error':
                continue

            texto1 = data1.get('texto_muestra', '')
            texto2 = data2.get('texto_muestra', '')

            if len(texto1) > 50 and len(texto2) > 50:
                similitud = calcular_similitud(texto1, texto2)

                if similitud >= SIMILITUD_DUPLICADO:
                    duplicados.append({
                        'pagina1': url1,
                        'pagina2': url2,
                        'similitud': round(similitud * 100, 1)
                    })

    return duplicados


def auditar_municipios():
    """Audita todas las páginas de municipios"""
    municipios_dir = BASE_DIR / 'municipios'
    resultados = {}

    # Listar todos los subdirectorios de municipios
    if not municipios_dir.exists():
        return resultados

    for municipio_dir in sorted(municipios_dir.iterdir()):
        if municipio_dir.is_dir() and municipio_dir.name != 'index.html':
            index_file = municipio_dir / 'index.html'

            if index_file.exists():
                url = f"/municipios/{municipio_dir.name}/"
                resultados[url] = analizar_pagina(index_file, tipo='municipio')
                resultados[url]['nombre'] = municipio_dir.name.replace('-', ' ').title()

    return resultados


def auditar_blog():
    """Audita todos los artículos del blog"""
    blog_dir = BASE_DIR / 'blog'
    resultados = {}

    if not blog_dir.exists():
        return resultados

    for articulo_dir in sorted(blog_dir.iterdir()):
        if articulo_dir.is_dir():
            index_file = articulo_dir / 'index.html'

            if index_file.exists():
                url = f"/blog/{articulo_dir.name}/"
                resultados[url] = analizar_pagina(index_file, tipo='blog')
                resultados[url]['nombre'] = articulo_dir.name.replace('-', ' ').title()

    return resultados


def generar_resumen(municipios, blog):
    """Genera resumen ejecutivo de la auditoría"""

    def contar_estados(resultados):
        estados = {'completa': 0, 'insuficiente': 0, 'vacia': 0, 'error': 0}
        for data in resultados.values():
            estado = data.get('estado', 'error')
            estados[estado] = estados.get(estado, 0) + 1
        return estados

    estados_municipios = contar_estados(municipios)
    estados_blog = contar_estados(blog)

    # Listas de URLs por estado
    def filtrar_por_estado(resultados, estado):
        return [url for url, data in resultados.items() if data.get('estado') == estado]

    return {
        'total_paginas': len(municipios) + len(blog),
        'municipios': {
            'total': len(municipios),
            'completas': estados_municipios['completa'],
            'insuficientes': estados_municipios['insuficiente'],
            'vacias': estados_municipios['vacia'],
            'errores': estados_municipios['error']
        },
        'blog': {
            'total': len(blog),
            'completos': estados_blog['completa'],
            'insuficientes': estados_blog['insuficiente'],
            'vacios': estados_blog['vacia'],
            'errores': estados_blog['error']
        },
        'urls_completas': filtrar_por_estado({**municipios, **blog}, 'completa'),
        'urls_insuficientes': filtrar_por_estado({**municipios, **blog}, 'insuficiente'),
        'urls_vacias': filtrar_por_estado({**municipios, **blog}, 'vacia'),
        'urls_error': filtrar_por_estado({**municipios, **blog}, 'error')
    }


def main():
    """Función principal"""
    print("INICIANDO AUDITORIA DE CONTENIDO...")
    print(f"Base: {BASE_DIR}\n")

    # Auditar municipios
    print("Auditando municipios...")
    municipios = auditar_municipios()
    print(f"   OK {len(municipios)} municipios analizados\n")

    # Auditar blog
    print("Auditando blog...")
    blog = auditar_blog()
    print(f"   OK {len(blog)} articulos analizados\n")

    # Detectar duplicados
    print("Detectando duplicados...")
    duplicados_municipios = detectar_duplicados(municipios)
    duplicados_blog = detectar_duplicados(blog)
    print(f"   WARN {len(duplicados_municipios)} duplicados en municipios")
    print(f"   WARN {len(duplicados_blog)} duplicados en blog\n")

    # Generar resumen
    resumen = generar_resumen(municipios, blog)

    # Crear reporte JSON
    reporte = {
        'auditoria_fecha': datetime.now().strftime('%Y-%m-%d'),
        'resumen': resumen,
        'municipios': municipios,
        'blog': blog,
        'duplicados': {
            'municipios': duplicados_municipios,
            'blog': duplicados_blog
        }
    }

    # Guardar JSON
    output_json = BASE_DIR / f"auditoria-contenido-{datetime.now().strftime('%Y-%m-%d')}.json"
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(reporte, f, ensure_ascii=False, indent=2)

    print(f"OK Reporte JSON guardado: {output_json.name}\n")

    # Mostrar resumen
    print("=" * 60)
    print("RESUMEN EJECUTIVO")
    print("=" * 60)
    print(f"Total paginas auditadas: {resumen['total_paginas']}")
    print()
    print("MUNICIPIOS:")
    print(f"  [OK]   Completas:      {resumen['municipios']['completas']}/{resumen['municipios']['total']}")
    print(f"  [WARN] Insuficientes:  {resumen['municipios']['insuficientes']}/{resumen['municipios']['total']}")
    print(f"  [ERR]  Vacias:         {resumen['municipios']['vacias']}/{resumen['municipios']['total']}")
    print()
    print("BLOG:")
    print(f"  [OK]   Completos:      {resumen['blog']['completos']}/{resumen['blog']['total']}")
    print(f"  [WARN] Insuficientes:  {resumen['blog']['insuficientes']}/{resumen['blog']['total']}")
    print(f"  [ERR]  Vacios:         {resumen['blog']['vacios']}/{resumen['blog']['total']}")
    print()
    print(f"Duplicados detectados: {len(duplicados_municipios) + len(duplicados_blog)}")
    print("=" * 60)

    return reporte


if __name__ == '__main__':
    reporte = main()
