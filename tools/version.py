# -*- coding: utf-8 -*-
"""
Le pone version a los assets: assets/zyntra.css?v=<hash>

Por que hace falta: GitHub Pages sirve los archivos de assets/ con unos 10
minutos de cache y no deja cambiar las cabeceras. Cuando se publica un
cambio de diseno, el que ya visito el sitio recibe el HTML NUEVO con el CSS
VIEJO todavia cacheado, y ve la pagina rota hasta que el cache expira. Con
la version en la URL el navegador esta obligado a bajar el archivo nuevo.

El numero de version es el hash del contenido, asi que cambia solo cuando el
archivo cambia de verdad: si no tocaste el CSS, la URL no se mueve y el
cache sigue sirviendo.

Lo corre build.py al final. A mano:  python tools/version.py
"""
import glob
import hashlib
import io
import os
import re

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# El favicon y el icono de app tambien: los navegadores los cachean todavia
# mas fuerte que una hoja de estilos, y al cambiar la marca hay que forzarlos.
ASSETS = ('assets/zyntra.css', 'assets/zyntra.js', 'favicon.svg', 'apple-touch-icon.png')
EXCLUIDAS = {'byheart', 'tools', 'docs', 'rediseno total de Zyntra'}


def hash_de(rel):
    with io.open(os.path.join(RAIZ, rel), 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()[:8]


def paginas():
    for patron in ('*.html', '*/index.html', '*/*/index.html'):
        for ruta in glob.glob(os.path.join(RAIZ, patron)):
            rel = os.path.relpath(ruta, RAIZ).replace('\\', '/')
            if rel.split('/')[0] in EXCLUIDAS or 'redise' in rel:
                continue
            yield rel


def main():
    versiones = {rel: hash_de(rel) for rel in ASSETS}
    tocados = 0
    for rel in paginas():
        ruta = os.path.join(RAIZ, rel)
        h = io.open(ruta, encoding='utf-8').read()
        original = h
        for asset, v in versiones.items():
            # atrapa la ruta con cualquier cantidad de ../ adelante y con o
            # sin ?v= previo, para poder correrlo las veces que haga falta.
            # El (?<=") ancla el arranque para no comerse un prefijo de mas.
            h = re.sub(r'(?<=")((?:\.\./)*' + re.escape(asset) + r')(\?v=[a-f0-9]+)?"',
                       r'\1?v=' + v + '"', h)
        if h != original:
            io.open(ruta, 'w', encoding='utf-8', newline='').write(h)
            tocados += 1
    print('  version de assets: %s  ->  %d paginas actualizadas'
          % (', '.join('%s=%s' % (k.split('/')[-1], v) for k, v in versiones.items()), tocados))


if __name__ == '__main__':
    main()
