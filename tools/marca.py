# -*- coding: utf-8 -*-
"""
Genera los archivos de marca que no se pueden hacer con HTML/CSS:

    favicon.svg           el isotipo, vectorial
    apple-touch-icon.png  180x180, el mismo isotipo rasterizado
    og-zyntra.jpg         1200x630, la imagen que se ve al compartir el link

El isotipo es el cuadrado blando (radio 34%) en tinta, con la Z en crema y
el punto naranja abajo a la derecha. En la web la Z es texto en Bricolage,
pero un favicon se dibuja sin webfonts, asi que aca va como poligono: diez
puntos que reproducen la Z pesada de Bricolage 800.

La imagen OG sigue la plantilla "OG - home" del kit, a 3x.

Las fuentes se bajan de Google Fonts a una carpeta temporal. No se guardan
en el repo: pesan mas que todo lo demas junto y solo hacen falta aca.

Uso:  python tools/marca.py
"""
import io
import os
import re
import sys
import tempfile
import urllib.request

from PIL import Image, ImageDraw, ImageFont

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(tempfile.gettempdir(), 'zyntra-fuentes')

TINTA = (23, 19, 16)
CREMA = (245, 240, 230)
ACENTO = (228, 87, 46)
MONO_TINTA = (142, 131, 119)

# La Z de Bricolage 800 en una caja de 100x100, como poligono cerrado.
Z = [(20, 22), (80, 22), (80, 34), (38, 66), (80, 66),
     (80, 78), (20, 78), (20, 66), (62, 34), (20, 34)]

SUPER = 4   # se dibuja a 4x y se reduce: PIL no antialiasa poligonos


def fuente(familia, ejes, archivo):
    """Baja una cara de Google Fonts y la deja cacheada."""
    os.makedirs(CACHE, exist_ok=True)
    destino = os.path.join(CACHE, archivo)
    if not os.path.exists(destino):
        url = 'https://fonts.googleapis.com/css2?family=%s:%s&display=swap' % (familia, ejes)
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        css = urllib.request.urlopen(req, timeout=30).read().decode()
        m = re.search(r'url\((https://[^)]+\.ttf)\)', css)
        if not m:
            sys.exit('marca: Google Fonts no devolvio un .ttf para %s' % familia)
        urllib.request.urlretrieve(m.group(1), destino)
    return destino


def cargar(ruta, tam, peso=None):
    f = ImageFont.truetype(ruta, tam)
    if peso is not None:
        try:
            ejes = [a[2] for a in f.get_variation_axes()]   # el default de cada eje
            nombres = [a[0] for a in f.get_variation_axes()]
            for i, n in enumerate(nombres):
                if b'wght' in n or b'Weight' in n or n == b'Weight':
                    ejes[i] = peso
            f.set_variation_by_axes(ejes)
        except Exception:
            pass    # sin soporte de variables: queda el peso por defecto
    return f


def texto_ajustado(d, xy, txt, f, fill, tracking=0):
    """
    Dibuja con letter-spacing. PIL no lo soporta, asi que va letra por letra.
    tracking en pixeles; negativo aprieta, que es lo que pide el sistema.
    """
    x, y = xy
    for ch in txt:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + tracking
    return x


def ancho_ajustado(d, txt, f, tracking=0):
    return sum(d.textlength(c, font=f) + tracking for c in txt) - tracking


# ------------------------------------------------------------------ isotipo

def isotipo(lienzo, x, y, lado, fondo=TINTA, con_punto=True):
    """Dibuja el isotipo sobre un ImageDraw ya escalado."""
    s = lado
    lienzo.rounded_rectangle([x, y, x + s, y + s], radius=int(s * .34), fill=fondo)
    lienzo.polygon([(x + px * s / 100, y + py * s / 100) for px, py in Z], fill=CREMA)
    if con_punto:
        cx, cy = x + s * .84, y + s * .84
        lienzo.ellipse([cx - s * .145, cy - s * .145, cx + s * .145, cy + s * .145], fill=fondo)
        lienzo.ellipse([cx - s * .11, cy - s * .11, cx + s * .11, cy + s * .11], fill=ACENTO)


def escribir_favicon():
    d = ' '.join('%g %g' % (x, y) for x, y in Z)
    puntos = 'M' + ('L'.join('%g,%g' % (x, y) for x, y in Z)) + 'Z'
    svg = '''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" role="img" aria-label="Zyntra">
  <rect width="100" height="100" rx="34" fill="#171310"/>
  <path fill="#F5F0E6" d="%s"/>
  <circle cx="84" cy="84" r="14.5" fill="#171310"/>
  <circle cx="84" cy="84" r="11" fill="#E4572E"/>
</svg>
''' % puntos
    ruta = os.path.join(RAIZ, 'favicon.svg')
    io.open(ruta, 'w', encoding='utf-8', newline='\n').write(svg)
    return ruta


def escribir_apple():
    n = 180
    img = Image.new('RGB', (n * SUPER, n * SUPER), TINTA)
    isotipo(ImageDraw.Draw(img), 0, 0, n * SUPER)
    img = img.resize((n, n), Image.LANCZOS)
    ruta = os.path.join(RAIZ, 'apple-touch-icon.png')
    img.save(ruta, 'PNG', optimize=True)
    return ruta


# ------------------------------------------------------------------ imagen OG

TITULO_OG = 'Sistemas a medida, turnos y chatbots para tu negocio'
PIE_IZQ = 'DIAGNÓSTICO GRATIS · CABA'
PIE_DER = 'EMMANUELAP.GITHUB.IO'


def ojito_og(img, x, y, s):
    """
    El Ojito de la barra de marca. Sobre tinta va invertido, como en el kit:
    cuerpo tinta con aro crema, iris naranja y parpado crema.
    (x, y) es la esquina superior izquierda, para que alinee con el titular.

    Se arma en una capa aparte y se recorta con una mascara circular. Dibujar
    el parpado directo sobre la imagen no sirve: es un chord cuyos extremos
    caen en el punto mas alto del circulo, donde el circulo no tiene ancho,
    asi que le salian dos alas planas a los costados.
    """
    n = int(s) * SUPER
    capa = Image.new('RGB', (n, n), TINTA)
    c = ImageDraw.Draw(capa)

    ir = n * .23
    cx = n / 2 + n * .09
    c.ellipse([cx - ir, n / 2 - ir, cx + ir, n / 2 + ir], fill=ACENTO)
    lid = n * .18
    c.chord([0, -lid, n, lid], 0, 180, fill=CREMA)

    mascara = Image.new('L', (n, n), 0)
    ImageDraw.Draw(mascara).ellipse([0, 0, n - 1, n - 1], fill=255)

    capa = capa.resize((int(s), int(s)), Image.LANCZOS)
    mascara = mascara.resize((int(s), int(s)), Image.LANCZOS)
    img.paste(capa, (int(x), int(y)), mascara)

    d = ImageDraw.Draw(img)
    cxx, cyy, r = x + s / 2, y + s / 2, s / 2
    d.ellipse([cxx - r, cyy - r, cxx + r, cyy + r], outline=CREMA, width=max(2, int(s * .075)))


def escribir_og():
    A, H = 1200, 630
    pad = 90
    img = Image.new('RGB', (A, H), TINTA)
    d = ImageDraw.Draw(img)

    bricolage = fuente('Bricolage+Grotesque', 'opsz,wght@12..96,800', 'bricolage-800.ttf')
    jet = fuente('JetBrains+Mono', 'wght@600', 'jetbrains-600.ttf')

    f_marca = cargar(bricolage, 63, 800)
    f_tit = cargar(bricolage, 92, 800)
    f_pie = cargar(jet, 23, 600)

    # ---- barra de marca. El Ojito arranca en el margen, igual que el titular.
    ojito_og(img, pad, pad, 58)
    texto_ajustado(d, (pad + 78, pad - 10), 'zyntra', f_marca, CREMA, tracking=-2.8)

    # ---- titular, partido a mano para que no toque el borde
    palabras = TITULO_OG.split()
    lineas, actual = [], ''
    for w in palabras:
        prueba = (actual + ' ' + w).strip()
        if ancho_ajustado(d, prueba, f_tit, -3.7) > 900 and actual:
            lineas.append(actual)
            actual = w
        else:
            actual = prueba
    lineas.append(actual)

    alto_linea = 94
    y = H - pad - 62 - alto_linea * len(lineas)
    for ln in lineas:
        texto_ajustado(d, (pad, y), ln, f_tit, CREMA, tracking=-3.7)
        y += alto_linea

    # ---- pie. Las dos leyendas se pisaban: si no entran con aire, se recorta
    # el tracking antes que dejarlas encimadas.
    yp = H - pad - 6
    tr = 4
    izq = ancho_ajustado(d, PIE_IZQ, f_pie, tr)
    der = ancho_ajustado(d, PIE_DER, f_pie, tr)
    while izq + der + 60 > A - pad * 2 and tr > 0:
        tr -= .5
        izq = ancho_ajustado(d, PIE_IZQ, f_pie, tr)
        der = ancho_ajustado(d, PIE_DER, f_pie, tr)
    texto_ajustado(d, (pad, yp), PIE_IZQ, f_pie, MONO_TINTA, tracking=tr)
    texto_ajustado(d, (A - pad - der, yp), PIE_DER, f_pie, ACENTO, tracking=tr)

    ruta = os.path.join(RAIZ, 'og-zyntra.jpg')
    img.save(ruta, 'JPEG', quality=88, optimize=True, progressive=True)
    return ruta


if __name__ == '__main__':
    for r in (escribir_favicon(), escribir_apple(), escribir_og()):
        print('  %-24s %6.1f KB' % (os.path.relpath(r, RAIZ), os.path.getsize(r) / 1024))
