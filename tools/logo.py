# -*- coding: utf-8 -*-
"""
Genera las versiones del logo que usa el sitio, a partir del vector original.

El original (`assets/Zyntra-logo-vector.svg`) esta hecho para fondo CLARO: la
palabra ZYNTRA y el lema son #0B1014, que contra el fondo del sitio (#100f0d)
da contraste 1.0. Invisible. Aca se recolorea y se separa en tres piezas.

El vector es un solo path compuesto por color, asi que las piezas se arman
partiendo los subtrazos por su altura:

    y 156-514   la Z grande        -> isotipo
    y 262-456   la palabra ZYNTRA
    y 570-600   el lema

Salidas:
    assets/logo-zyntra.svg           completo, con lema     -> el hero
    assets/logo-zyntra-compacto.svg  sin lema               -> el header
    assets/logo-zyntra-simbolo.svg   solo la Z              -> favicon

Uso:  python tools/logo.py
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = os.path.join(RAIZ, 'assets', 'Zyntra-logo-vector.svg')

# Variante elegida: palabra en blanco, diagonal en el cian de marca.
PALABRA = '#ffffff'
ACENTO = '#81ecff'


def subtrazos(d):
    return ['M' + s for s in d.split('M') if s.strip()]


def alto(sub):
    ys = [float(x) for x in re.findall(r'-?\d+\.?\d*', sub)][1::2]
    return min(ys), max(ys)


def armar(nombre, viewbox, d_palabra, d_acento, titulo):
    partes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<svg xmlns="http://www.w3.org/2000/svg" viewBox="%s" role="img" aria-label="%s">'
              % (viewbox, titulo),
              '  <g fill-rule="evenodd" clip-rule="evenodd">']
    if d_palabra:
        partes.append('    <path fill="%s" d="%s"/>' % (PALABRA, d_palabra))
    if d_acento:
        partes.append('    <path fill="%s" d="%s"/>' % (ACENTO, d_acento))
    partes += ['  </g>', '</svg>', '']
    ruta = os.path.join(RAIZ, 'assets', nombre)
    io.open(ruta, 'w', encoding='utf-8', newline='\n').write('\n'.join(partes))
    return ruta


def main():
    svg = io.open(ORIGEN, encoding='utf-8').read()
    d_oscuro = re.search(r'fill="#0B1014" d="([^"]*)"', svg).group(1)
    d_claro = re.search(r'fill="#94897C" d="([^"]*)"', svg).group(1)

    oscuros = subtrazos(d_oscuro)
    claros = subtrazos(d_claro)
    if len(claros) != 2:
        sys.exit('logo: esperaba 2 subtrazos claros, hay %d' % len(claros))

    # el color claro son la diagonal de la Z y una barrita bajo la palabra
    diagonal = min(claros, key=lambda s: alto(s)[0])
    barra = max(claros, key=lambda s: alto(s)[0])

    zeta = [s for s in oscuros if alto(s)[1] <= 520]          # la Z: cruza toda la altura
    palabra = [s for s in oscuros if 250 < alto(s)[0] and alto(s)[1] <= 500]
    lema = [s for s in oscuros if alto(s)[0] > 500]

    zeta = [s for s in zeta if s not in palabra]

    generados = [
        armar('logo-zyntra.svg', '35 135 1960 495',
              ' '.join(zeta + palabra + lema), ' '.join([diagonal, barra]),
              'Zyntra - Automatizamos el futuro'),
        # el contenido sin lema llega hasta y=529 por la barrita bajo la palabra;
        # con 380 de alto quedaba cortada
        armar('logo-zyntra-compacto.svg', '35 135 1958 415',
              ' '.join(zeta + palabra), ' '.join([diagonal, barra]),
              'Zyntra'),
        # cuadrado y centrado: es el que termina de favicon
        armar('logo-zyntra-simbolo.svg', '27 52 567 567',
              ' '.join(zeta), diagonal,
              'Zyntra'),
    ]

    print('subtrazos: Z=%d  palabra=%d  lema=%d' % (len(zeta), len(palabra), len(lema)))
    for r in generados:
        print('  %-34s %4.1f KB' % (os.path.relpath(r, RAIZ).replace('\\', '/'),
                                    os.path.getsize(r) / 1024))


if __name__ == '__main__':
    main()
