# -*- coding: utf-8 -*-
"""
Genera los PDF descargables de docs/ con el sistema de marca.

  tools/pdf_marca.py   el sistema de diseno (paleta, tipografias, Ojito)
  tools/pdfs/*.py      un archivo por documento, cada uno con construir()
  ->  docs/<archivo>.pdf

Despues de generar hay que actualizar a mano el PESO que figura en el HTML
de las pastillas de descarga: esta escrito en el texto y no lo calcula nadie.
El script te dice cuales cambiaron.

Uso:  python tools/build_pdf.py
      python tools/build_pdf.py pentesting     solo ese
"""
import glob
import importlib.util
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import pdf_marca  # noqa: E402


def cargar(ruta):
    spec = importlib.util.spec_from_file_location('doc_' + os.path.basename(ruta)[:-3], ruta)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def actualizar_pesos(generados):
    """
    Corrige el peso escrito al lado de cada pastilla de descarga.

    Antes esto se hacia a mano y quedaba viejo a la primera regeneracion. El
    separador esta escrito como entidad (&#183;), no como caracter: por eso
    el patron acepta las dos formas.
    """
    pesos = {n: round(kb) for n, _, kb in generados}
    cambios = []
    for patron in ('*.html', '*/index.html', '*/*/index.html'):
        for ruta in glob.glob(os.path.join(RAIZ, patron)):
            rel = os.path.relpath(ruta, RAIZ).replace(os.sep, '/')
            if rel.split('/')[0] in ('byheart', 'kit') or 'redise' in rel:
                continue
            h = io.open(ruta, encoding='utf-8').read()
            original = h
            for nombre, kb in pesos.items():
                def reemplazo(m, kb=kb):
                    if int(m.group(2)) == kb:
                        return m.group(0)
                    cambios.append('%s: %s KB -> %d KB  (%s)'
                                   % (nombre, m.group(2), kb, rel))
                    return '%s%d KB' % (m.group(1), kb)
                h = re.sub(
                    r'(' + re.escape(nombre) + r'.{0,600}?doc-download-size">\s*'
                    r'(?:&#183;|·)?\s*)([0-9]+)\s*KB',
                    reemplazo, h, flags=re.S)
            if h != original:
                io.open(ruta, 'w', encoding='utf-8', newline='').write(h)
    return cambios


def main():
    filtro = sys.argv[1] if len(sys.argv) > 1 else None
    rutas = sorted(glob.glob(os.path.join(AQUI, 'pdfs', '*.py')))
    rutas = [r for r in rutas if not os.path.basename(r).startswith('_')]
    if filtro:
        rutas = [r for r in rutas if filtro in os.path.basename(r)]
    if not rutas:
        sys.exit('build_pdf: no hay nada que generar')

    generados = []
    for ruta in rutas:
        mod = cargar(ruta)
        nombre, paginas, kb = mod.construir(pdf_marca.Documento, pdf_marca)
        generados.append((nombre, paginas, kb))
        print('  %-38s %2d paginas  %6.1f KB' % (nombre, paginas, kb))

    cambios = actualizar_pesos(generados)
    if cambios:
        print('\nPesos corregidos en el HTML:')
        for c in cambios:
            print('  %s' % c)
        print('\nOJO: si el HTML cambio, correr tambien  python tools/version.py')
    else:
        print('\n%d PDF generados. Los pesos del HTML ya estaban bien.'
              % len(generados))


if __name__ == '__main__':
    main()
