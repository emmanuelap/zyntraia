# -*- coding: utf-8 -*-
"""
Generador de las paginas de servicio de Zyntra.

Por que existe: hasta ahora todo el sitio comercial vivia en index.html, asi
que Google recibia una sola pagina hablando de doce cosas distintas. Para
competir por "chatbot whatsapp" o "sistema de turnos" hace falta una URL
dedicada a cada tema. Doce paginas escritas a mano serian doce copias del
header y del footer que se desincronizan a la primera semana, asi que las
generamos.

Como funciona:

  index.html  ->  de aca salen el header, el footer, los botones flotantes,
                  la config de Tailwind y los <link> de las fuentes.
                  index.html es la unica fuente de verdad del "chrome".

  tools/paginas/*.py  ->  un archivo por pagina, cada uno define PAGINA.

  ->  <slug>/index.html   (y de paso se reescribe sitemap.xml)

Uso:
    python tools/build.py            genera todo
    python tools/build.py --listar   muestra que paginas hay, sin escribir

No tiene dependencias: solo la libreria estandar de Python 3.
"""
import io
import os
import re
import sys
import json
import glob
import html as html_mod
import importlib.util
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import iconos  # noqa: E402
import ojito as mascota  # noqa: E402

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(RAIZ, 'index.html')
DIR_PAGINAS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paginas')
SITIO = 'https://emmanuelap.github.io/zyntraia/'

WA = ('https://wa.me/5491166439309?text=')


# ---------------------------------------------------------------- utilidades

def leer(ruta):
    with io.open(ruta, encoding='utf-8') as f:
        return f.read()


def escribir(ruta, contenido):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with io.open(ruta, 'w', encoding='utf-8', newline='') as f:
        f.write(contenido)


def entre(texto, desde, hasta, incluir=True):
    """Devuelve el bloque entre dos marcas. Falla fuerte si no aparece."""
    i = texto.find(desde)
    if i < 0:
        sys.exit('build: no encuentro %r en index.html' % desde)
    j = texto.find(hasta, i)
    if j < 0:
        sys.exit('build: no encuentro el cierre %r' % hasta)
    return texto[i:j + len(hasta)] if incluir else texto[i + len(desde):j]


EXTERNOS = ('http://', 'https://', '//', 'mailto:', 'tel:', 'data:', '../', '/')


def subir(fragmento, niveles=1):
    """
    Las paginas generadas viven mas abajo que index.html: /slug/index.html es
    un nivel, /casos-de-exito/algo/index.html son dos. Hay que corregir cada
    ruta relativa y cada ancla que apunte a la home.
    """
    prefijo = '../' * niveles

    def arreglar(m):
        attr, valor = m.group(1), m.group(2)
        if valor.startswith(EXTERNOS) or valor == '#':
            return m.group(0)
        # OJO: los iconos son <use href="#i-algo"> y apuntan al sprite que esta
        # en ESTA pagina, no a la home. Si se les agrega ../ quedan todos rotos
        # y no se ve ni un icono. Las otras anclas (#contact-form) SI van a la
        # home y por eso se reescriben.
        if valor.startswith('#i-'):
            return m.group(0)
        if valor in ('./', '.'):          # el "./" de la home ya ES el prefijo
            return '%s="%s"' % (attr, prefijo)
        return '%s="%s%s"' % (attr, prefijo, valor)

    return re.sub(r'\b(href|src)="([^"]*)"', arreglar, fragmento)


def slug_de(texto):
    import unicodedata
    t = unicodedata.normalize('NFKD', texto).encode('ascii', 'ignore').decode()
    t = re.sub(r'[^A-Za-z0-9\s-]', '', t).strip().lower()
    return re.sub(r'\s+', '-', t)


def esc(t):
    return html_mod.escape(t, quote=True)


# ------------------------------------------------------- chrome de index.html

def leer_chrome():
    h = leer(INDEX)
    chrome = {
        'header': entre(h, '<header class="site-header">', '</header>'),
        'footer': entre(h, '<footer class="site-footer">', '</footer>'),
    }
    # Los botones flotantes son un solo <div> sin divs adentro, asi que el
    # cierre no goloso alcanza. Se ancla al <script> final para no agarrar
    # otro div si algun dia se agrega uno.
    m = re.search(r'(<div class="flotantes">.*?</div>)\s*<script\b', h, re.S)
    if not m:
        sys.exit('build: no encuentro los botones flotantes en index.html')
    chrome['flotantes'] = m.group(1)

    fuentes = re.findall(r'<link href="https://fonts\.googleapis\.com[^"]*" rel="stylesheet"/>', h)
    if len(fuentes) != 1:
        sys.exit('build: esperaba 1 <link> de fuentes en index.html, hay %d' % len(fuentes))
    chrome['fuentes'] = fuentes[0]
    # los preconnect tambien salen de index.html: unica fuente de verdad
    chrome['preconnect'] = '\n'.join(re.findall(r'<link[^>]*rel="preconnect"[^>]*/>', h))
    # el sprite de iconos no se lee de index.html: lo genera tools/iconos.py,
    # que es la unica fuente de verdad del set
    chrome['sprite'] = iconos.sprite()
    return chrome


# ------------------------------------------------------------- render de HTML

def ico(nombre, clase='ico'):
    return iconos.ico(iconos.equivalente(nombre), clase)


def bloque_texto(s):
    p = '\n'.join('<p class="cuerpo" style="margin-top:16px">%s</p>' % x for x in s['parrafos'])
    return ('<div class="encabezado-seccion" style="margin-bottom:0">\n'
            '<h2 class="h-seccion">%s</h2>\n%s\n</div>' % (s['h2'], p))


def bloque_lista(s):
    tarjetas = []
    for it in s['items']:
        tarjetas.append(
            '<div class="tarjeta reveal">\n'
            '<div class="caja-ico">%s</div>\n'
            '<div><h3>%s</h3><p>%s</p></div>\n</div>'
            % (ico(it.get('icono', 'check_circle')), it['titulo'], it['texto']))
    intro = ('<p class="cuerpo" style="margin-top:14px">%s</p>' % s['intro']) if s.get('intro') else ''
    return ('<div class="encabezado-seccion">\n<h2 class="h-seccion">%s</h2>\n%s\n</div>\n'
            '<div class="rejilla">\n%s\n</div>' % (s['h2'], intro, '\n'.join(tarjetas)))


def bloque_pasos(s):
    filas = []
    for i, p in enumerate(s['pasos'], 1):
        filas.append(
            '<div class="tarjeta reveal">\n'
            '<div class="paso-num" style="color:var(--acento-texto)">%02d</div>\n'
            '<div><h3>%s</h3><p>%s</p></div>\n</div>' % (i, p['titulo'], p['texto']))
    return ('<div class="encabezado-seccion">\n<h2 class="h-seccion">%s</h2>\n</div>\n'
            '<div class="rejilla" style="--min:220px">\n%s\n</div>'
            % (s['h2'], '\n'.join(filas)))


def bloque_faq(s):
    items = []
    for q in s['preguntas']:
        items.append(
            '<details class="faq" id="%s">\n'
            '<summary>%s<span class="faq-flecha"></span></summary>\n'
            '<div class="respuesta"><p>%s</p></div>\n</details>'
            % (slug_de(q['q']), q['q'], q['a']))
    extra = ''
    if s.get('mas'):
        enlaces = '\n'.join(
            '<li><span class="punto"></span><a class="enlace" href="@@SUBIR@@preguntasfrecuentes/#%s">%s</a></li>'
            % (a, t) for a, t in s['mas'])
        extra = ('\n<div class="tarjeta" style="margin-top:22px">\n'
                 '<p class="etiqueta">M&#225;s preguntas sobre esto</p>\n'
                 '<ul class="lista-puntos" style="margin-top:16px">\n%s\n</ul>\n</div>' % enlaces)
    return ('<div class="encabezado-seccion">\n<h2 class="h-seccion">%s</h2>\n</div>\n'
            '<div style="max-width:820px">\n%s\n</div>%s' % (s['h2'], '\n'.join(items), extra))


def bloque_cifras(s):
    """Numeros de un caso real. Solo se usan cifras que el dueno pueda defender."""
    celdas = []
    for c in s['numeros']:
        celdas.append(
            '<div class="tarjeta tarjeta--tinta reveal">\n'
            '<div class="dato" style="font-size:clamp(30px,4vw,46px)">%s</div>\n'
            '<div><h3 style="color:var(--crema);font-size:18px">%s</h3><p>%s</p></div>\n</div>'
            % (c['cifra'], c['titulo'], c.get('detalle', '')))
    intro = ('<p class="cuerpo" style="margin-top:14px">%s</p>' % s['intro']) if s.get('intro') else ''
    return ('<div class="encabezado-seccion">\n<h2 class="h-seccion">%s</h2>\n%s\n</div>\n'
            '<div class="rejilla" style="--min:230px">\n%s\n</div>'
            % (s['h2'], intro, '\n'.join(celdas)))


def bloque_casos(s):
    """Grilla de casos que enlaza a cada ficha."""
    fichas = []
    for c in s['casos']:
        fichas.append(
            '<a class="tarjeta tarjeta--enlace reveal" href="@@SUBIR@@%s/">\n'
            '<div class="caja-ico">%s</div>\n'
            '<div><h3>%s</h3><p>%s</p></div>\n'
            '<span class="puerta-cta">%s %s</span>\n</a>'
            % (c['slug'], ico(c.get('icono', 'work')), c['titulo'], c['texto'],
               c.get('cta', 'Ver el caso'), ico('arrow_forward', 'ico ico--chico')))
    return ('<div class="encabezado-seccion">\n<h2 class="h-seccion">%s</h2>\n</div>\n'
            '<div class="rejilla">\n%s\n</div>' % (s['h2'], '\n'.join(fichas)))


MESES = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')


def fecha_larga(iso):
    a, m, d = iso.split('-')
    return '%d de %s de %s' % (int(d), MESES[int(m) - 1], a)


def bloque_articulos(s):
    """Listado del blog. Cada nota enlaza a su pagina."""
    filas = []
    for a in s['articulos']:
        filas.append(
            '<a class="tarjeta tarjeta--enlace reveal" href="@@SUBIR@@%s/">\n'
            '<time class="etiqueta etiqueta--chica" datetime="%s">%s</time>\n'
            '<div><h3>%s</h3><p>%s</p></div>\n'
            '<span class="puerta-cta">Leer %s</span>\n</a>'
            % (a['slug'], a['fecha'], fecha_larga(a['fecha']), a['titulo'], a['resumen'],
               ico('arrow_forward', 'ico ico--chico')))
    return ('<div class="encabezado-seccion">\n<h2 class="h-seccion">%s</h2>\n</div>\n'
            '<div class="rejilla">\n%s\n</div>' % (s['h2'], '\n'.join(filas)))


RENDER = {'texto': bloque_texto, 'lista': bloque_lista, 'pasos': bloque_pasos,
          'faq': bloque_faq, 'cifras': bloque_cifras, 'casos': bloque_casos,
          'articulos': bloque_articulos}


def render_secciones(secciones):
    """Cada seccion es un panel de la pila. 'fondo' la pinta en tinta."""
    fuera = []
    for s in secciones:
        f = RENDER.get(s['tipo'])
        if not f:
            sys.exit('build: tipo de seccion desconocido: %r' % s['tipo'])
        clases = 'panel panel--tinta sobre-tinta' if s.get('fondo') else 'panel'
        fuera.append('<section class="%s">\n%s\n</section>' % (clases, f(s)))
    return '\n'.join(fuera)


# ------------------------------------------------------------ datos marcados

def datos_estructurados(p):
    url = SITIO + p['slug'] + '/'
    if p.get('articulo'):
        cabeza = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": p['h1'],
            "description": p['descripcion'],
            "url": url,
            "datePublished": p['articulo']['fecha'],
            "dateModified": p['articulo'].get('modificado', p['articulo']['fecha']),
            "inLanguage": "es-AR",
            "author": {"@type": "Organization", "name": "Zyntra", "url": SITIO},
            "publisher": {"@type": "Organization", "name": "Zyntra", "url": SITIO,
                          "logo": {"@type": "ImageObject",
                                   "url": SITIO + "apple-touch-icon.png"}},
            "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        }
    else:
        cabeza = None
    bloques = [cabeza or {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": p['servicio']['nombre'],
        "serviceType": p['servicio'].get('tipo', p['servicio']['nombre']),
        "description": p['descripcion'],
        "url": url,
        "provider": {
            "@type": "ProfessionalService",
            "name": "Zyntra",
            "url": SITIO,
            "telephone": "+5491166439309",
            "email": "zyntraconsultoraia@gmail.com",
            "address": {"@type": "PostalAddress",
                        "addressLocality": "Ciudad Autónoma de Buenos Aires",
                        "addressRegion": "Buenos Aires", "addressCountry": "AR"},
        },
        "areaServed": {"@type": "Country", "name": "Argentina"},
        "availableChannel": {"@type": "ServiceChannel", "serviceUrl": url},
    }, {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITIO},
            {"@type": "ListItem", "position": 2, "name": p['migas'], "item": url},
        ],
    }]
    if p.get('padre'):
        bloques[1]['itemListElement'] = [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITIO},
            {"@type": "ListItem", "position": 2, "name": p['padre']['nombre'],
             "item": SITIO + p['padre']['slug'] + '/'},
            {"@type": "ListItem", "position": 3, "name": p['migas'], "item": url},
        ]
    faqs = [s for s in p['secciones'] if s['tipo'] == 'faq']
    if faqs:
        preguntas = [q for s in faqs for q in s['preguntas']]
        bloques.append({
            "@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q['q'],
                            "acceptedAnswer": {"@type": "Answer", "text": q['a']}}
                           for q in preguntas],
        })
    return '\n'.join('<script type="application/ld+json">\n%s\n</script>'
                     % json.dumps(b, ensure_ascii=False, indent=2) for b in bloques)


# ------------------------------------------------------------------ plantilla

PLANTILLA = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>@@TITULO@@</title>
<meta content="@@DESC@@" name="description"/>
<meta content="Zyntra" name="author"/>
<meta content="#E3D8C4" name="theme-color"/>
@@PRECONNECT@@
<meta content="index, follow, max-image-preview:large, max-snippet:-1" name="robots"/>
<link href="@@URL@@" rel="canonical"/>
<link href="@@SUBIR@@favicon.svg" rel="icon" type="image/svg+xml"/>
<link href="@@SUBIR@@apple-touch-icon.png" rel="apple-touch-icon"/>
<meta content="website" property="og:type"/>
<meta content="es_AR" property="og:locale"/>
<meta content="Zyntra" property="og:site_name"/>
<meta content="@@TITULO@@" property="og:title"/>
<meta content="@@DESC@@" property="og:description"/>
<meta content="@@URL@@" property="og:url"/>
<meta content="@@SITIO@@og-zyntra.jpg" property="og:image"/>
<meta content="summary_large_image" name="twitter:card"/>
<meta content="@@TITULO@@" name="twitter:title"/>
<meta content="@@DESC@@" name="twitter:description"/>
<meta content="@@SITIO@@og-zyntra.jpg" name="twitter:image"/>
@@FUENTES@@
<link href="@@SUBIR@@assets/zyntra.css" rel="stylesheet"/>
@@SCHEMA@@
</head>
<body>
@@SPRITE@@
<div class="scroll-progress" id="scroll-progress"></div>
@@HEADER@@
<main>
<div class="envoltorio">

<section class="panel panel--tinta sobre-tinta panel--primero">
<nav aria-label="Ruta de navegaci&#243;n" class="migas">
<a href="@@SUBIR@@">Inicio</a>@@PADRE@@
<span aria-current="page">@@MIGAS@@</span>
</nav>
<div class="portada">
<div>
<div class="caja-ico caja-ico--naranja" style="margin-bottom:22px">@@ICONO@@</div>
<h1 class="display" style="color:var(--crema)">@@H1@@</h1>
@@FECHA@@
<p class="cuerpo" style="margin-top:20px;max-width:56ch">@@BAJADA@@</p>
<div class="fila-botones" style="margin-top:28px">
<a class="btn btn--primario" href="@@WA@@" rel="noopener noreferrer" target="_blank">@@CTA_BOTON@@</a>
<a class="btn btn--contorno" href="@@SUBIR@@#contact-form">Pedir diagn&#243;stico gratis</a>
</div>
</div>
</div>
</section>

@@SECCIONES@@

<section class="panel bloque-cta">
<div class="fila">
<h2>@@CTA_TITULO@@</h2>
@@OJITO@@
</div>
<div>
<p class="cuerpo" style="color:var(--sobre-naranja);max-width:56ch;margin-bottom:22px">@@CTA_TEXTO@@</p>
<div class="fila-botones">
<a class="btn btn--secundario" href="@@WA@@" rel="noopener noreferrer" target="_blank">@@CTA_BOTON@@</a>
<a class="btn btn--contorno" href="@@SUBIR@@preguntasfrecuentes/">Ver las preguntas frecuentes</a>
</div>
</div>
</section>

</div>
</main>
<div class="envoltorio">
@@FOOTER@@
</div>
@@FLOTANTES@@
<script defer src="@@SUBIR@@assets/zyntra.js"></script>
</body>
</html>
'''


def ojito_de(p):
    """
    El Ojito del bloque CTA, con la cara que le corresponde a esa pagina.
    Se elige con la clave 'ojito' de PAGINA; por defecto va 'normal'.

    Pentesting es la excepcion del brandboard: ahi NO va la mascota. Una
    auditoria de seguridad no se vende con un personaje simpatico.
    """
    if p.get('sin_ojito') or p['slug'].startswith('pentesting'):
        return ''
    return mascota.ojito(p.get('ojito', 'normal'), 'clamp(56px,8vw,78px)')


def render(p, chrome):
    url = SITIO + p['slug'] + '/'
    wa = WA + p['wa']
    niveles = p['slug'].count('/') + 1
    reemplazos = {
        '@@TITULO@@': esc(p['titulo']),
        '@@DESC@@': esc(p['descripcion']),
        '@@URL@@': url,
        '@@SITIO@@': SITIO,
        '@@PRECONNECT@@': chrome['preconnect'],
        '@@MIGAS@@': p['migas'],
        '@@PADRE@@': ('\n<a href="%s%s/">%s</a>' % ('../' * niveles, p['padre']['slug'],
                                                    p['padre']['nombre'])) if p.get('padre') else '',
        '@@ICONO@@': ico(p['icono']),
        '@@H1@@': p['h1'],
        '@@BAJADA@@': p['bajada'],
        '@@FECHA@@': ('<time class="etiqueta etiqueta--chica" style="display:block;margin-top:16px" '
                      'datetime="%s">Publicado el %s</time>'
                      % (p['articulo']['fecha'], fecha_larga(p['articulo']['fecha']))
                      ) if p.get('articulo') else '',
        '@@WA@@': wa,
        '@@CTA_BOTON@@': p['cta']['boton'],
        '@@CTA_TITULO@@': p['cta']['titulo'],
        '@@CTA_TEXTO@@': p['cta']['texto'],
        '@@FUENTES@@': chrome['fuentes'],
        '@@SPRITE@@': chrome['sprite'],
        '@@HEADER@@': subir(chrome['header'], niveles),
        '@@FOOTER@@': subir(chrome['footer'], niveles),
        '@@FLOTANTES@@': subir(chrome['flotantes'], niveles),
        '@@OJITO@@': ojito_de(p),
        '@@SCHEMA@@': datos_estructurados(p),
        '@@SECCIONES@@': render_secciones(p['secciones']),
    }
    salida = PLANTILLA
    for k, v in reemplazos.items():
        salida = salida.replace(k, v)
    salida = salida.replace('@@SUBIR@@', '../' * niveles)
    sobrantes = re.findall(r'@@[A-Z_]+@@', salida)
    if sobrantes:
        sys.exit('build: quedaron marcas sin reemplazar: %s' % set(sobrantes))
    return salida


# ------------------------------------------------------------------- sitemap

FIJAS = [('', 'weekly', '1.0'),
         ('preguntasfrecuentes/', 'monthly', '0.8'),
         ('privacidad.html', 'yearly', '0.3'),
         ('terminos.html', 'yearly', '0.3')]


def escribir_sitemap(slugs):
    hoy = date.today().isoformat()
    urls = [(SITIO + r, f, p, hoy) for r, f, p in FIJAS]
    urls[1:1] = [(SITIO + s + '/', 'monthly', '0.9', hoy) for s in sorted(slugs)]
    cuerpo = '\n'.join(
        '  <url>\n    <loc>%s</loc>\n    <lastmod>%s</lastmod>\n'
        '    <changefreq>%s</changefreq>\n    <priority>%s</priority>\n  </url>'
        % (u, m, f, p) for u, f, p, m in urls)
    escribir(os.path.join(RAIZ, 'sitemap.xml'),
             '<?xml version="1.0" encoding="UTF-8"?>\n'
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s\n</urlset>\n' % cuerpo)
    return len(urls)


# ----------------------------------------------------------------------- main

def cargar_paginas():
    paginas = []
    for ruta in sorted(glob.glob(os.path.join(DIR_PAGINAS, '*.py'))):
        if os.path.basename(ruta).startswith('_'):
            continue
        spec = importlib.util.spec_from_file_location('pagina', ruta)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        if not hasattr(mod, 'PAGINA'):
            sys.exit('build: %s no define PAGINA' % ruta)
        paginas.append(mod.PAGINA)
    return paginas


def main():
    paginas = cargar_paginas()
    if '--listar' in sys.argv:
        for p in paginas:
            print('%-28s %s' % (p['slug'] + '/', p['titulo']))
        print('\n%d paginas' % len(paginas))
        return
    if not paginas:
        sys.exit('build: no hay nada en tools/paginas/')
    chrome = leer_chrome()
    for p in paginas:
        destino = os.path.join(RAIZ, p['slug'], 'index.html')
        escribir(destino, render(p, chrome))
        print('  %-30s %6.0f KB' % (p['slug'] + '/index.html', os.path.getsize(destino) / 1024))
    import version
    version.main()
    n = escribir_sitemap([p['slug'] for p in paginas])
    print('\n%d paginas generadas · sitemap.xml con %d URLs' % (len(paginas), n))


if __name__ == '__main__':
    main()
