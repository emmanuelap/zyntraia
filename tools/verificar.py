# -*- coding: utf-8 -*-
"""
Chequeo del sitio: enlaces internos, anclas y datos estructurados.

Cada pagina de servicio enlaza a anclas de la home y de preguntasfrecuentes.
Una ancla mal escrita no rompe nada visible: el link simplemente no salta a
ningun lado y nadie se entera. Este script las verifica todas.

Uso:
    python tools/verificar.py        devuelve 1 si encuentra algo
"""
import io
import os
import re
import sys
import glob
import json

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXTERNO = ('http://', 'https://', '//', 'mailto:', 'tel:', 'data:')

# byheart/ es material de referencia que dejo el dueno, no forma parte del sitio
EXCLUIDAS = {'byheart', 'tools', 'docs'}


def leer(p):
    with io.open(os.path.join(RAIZ, p), encoding='utf-8') as f:
        return f.read()


def paginas_del_sitio():
    """Todo el HTML del sitio, con la ruta relativa a la raiz."""
    fuera = []
    for patron in ('*.html', '*/index.html'):
        for p in glob.glob(os.path.join(RAIZ, patron)):
            rel = os.path.relpath(p, RAIZ).replace('\\', '/')
            if rel.split('/')[0] in EXCLUIDAS:
                continue
            fuera.append(rel)
    return sorted(set(fuera))


def resolver(desde, href):
    """Devuelve la ruta del archivo destino, relativa a la raiz."""
    base = os.path.dirname(desde)
    ruta = os.path.normpath(os.path.join(base, href)).replace('\\', '/')
    if ruta in ('.', ''):
        ruta = 'index.html'
    if os.path.isdir(os.path.join(RAIZ, ruta)):
        ruta = ruta.rstrip('/') + '/index.html'
    return ruta


def main():
    problemas = []
    ids = {}
    todas = paginas_del_sitio()

    for p in todas:
        ids[p] = set(re.findall(r'\sid="([^"]+)"', leer(p)))

    for p in todas:
        h = leer(p)

        for attr, valor in re.findall(r'\b(href|src)="([^"]*)"', h):
            if not valor or valor.startswith(EXTERNO) or valor == '#':
                continue
            ruta, _, ancla = valor.partition('#')
            destino = resolver(p, ruta) if ruta else p

            if not os.path.exists(os.path.join(RAIZ, destino)):
                problemas.append('%s: %s="%s" apunta a un archivo que no existe (%s)'
                                 % (p, attr, valor, destino))
                continue

            if ancla and destino.endswith('.html') and ancla not in ids.get(destino, set()):
                problemas.append('%s: el ancla #%s no existe en %s' % (p, ancla, destino))

        for bloque in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
            try:
                json.loads(bloque)
            except Exception as e:
                problemas.append('%s: JSON-LD invalido (%s)' % (p, e))

        vacios = re.findall(r'<img(?![^>]*\balt=)[^>]*>', h)
        if vacios:
            problemas.append('%s: %d <img> sin alt' % (p, len(vacios)))

    print('paginas revisadas: %d' % len(todas))
    for p in todas:
        print('  %s' % p)

    if problemas:
        print('\nPROBLEMAS (%d):' % len(problemas))
        for x in problemas:
            print('  - %s' % x)
        sys.exit(1)
    print('\nsin problemas: enlaces, anclas, JSON-LD y alt en orden')


if __name__ == '__main__':
    main()
