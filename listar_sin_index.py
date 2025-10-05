#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lista municipios sin index.html
"""

from pathlib import Path

BASE_DIR = Path("C:/Users/rcn14/Google Drive/APPS WEB/CERTIALMERIA")
MUNICIPIOS_DIR = BASE_DIR / "municipios"

sin_index = []

for dir_path in MUNICIPIOS_DIR.iterdir():
    if dir_path.is_dir() and dir_path.name != 'index.html':
        index_file = dir_path / "index.html"
        if not index_file.exists():
            sin_index.append(dir_path.name)

sin_index.sort()

print(f"Total municipios SIN index.html: {len(sin_index)}")
print()
for m in sin_index:
    print(f"  - {m}")
