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
        'header':    entre(h, '<header class="site-header', '</header>'),
        'footer':    entre(h, '<footer class="w-full border-t', '</footer>'),
        'tailwind':  entre(h, '<script src="https://cdn.tailwindcss.com', '</script>'),
        'config':    entre(h, '<script id="tailwind-config">', '</script>'),
        'flotantes': entre(h, '<a aria-label="Telegram', '</a>\n<script src='
                     ).rsplit('<script src=', 1)[0].rstrip(),
    }
    fuentes = re.findall(r'<link href="https://fonts\.googleapis\.com[^"]*" rel="stylesheet"/>', h)
    if len(fuentes) != 2:
        sys.exit('build: esperaba 2 <link> de fuentes en index.html, hay %d' % len(fuentes))
    chrome['fuentes'] = '\n'.join(fuentes)
    aviso = re.search(r'<!-- El font de iconos[^>]*?-->', h, re.S)
    chrome['aviso_iconos'] = aviso.group(0) if aviso else ''
    return chrome


# ------------------------------------------------------------- render de HTML

def bloque_texto(s):
    p = '\n'.join('<p class="mt-4 text-on-surface-variant">%s</p>' % x for x in s['parrafos'])
    return ('<div class="max-w-3xl reveal">\n'
            '<h2 class="text-2xl font-bold sm:text-3xl">%s</h2>\n%s\n</div>' % (s['h2'], p))


def bloque_lista(s):
    tarjetas = []
    for i, it in enumerate(s['items']):
        tarjetas.append(
            '<div class="reveal flex flex-col rounded-[20px] border border-outline-variant/10 '
            'bg-surface-container p-6" style="transition-delay:%dms">\n'
            '<span class="material-symbols-outlined mb-3 text-3xl text-primary">%s</span>\n'
            '<h3 class="mb-2 text-lg font-bold">%s</h3>\n'
            '<p class="text-sm leading-relaxed text-on-surface-variant">%s</p>\n</div>'
            % (i * 60, it.get('icono', 'check_circle'), it['titulo'], it['texto']))
    intro = ('<p class="mt-4 max-w-3xl text-on-surface-variant">%s</p>' % s['intro']) if s.get('intro') else ''
    return ('<div class="reveal">\n<h2 class="text-2xl font-bold sm:text-3xl">%s</h2>\n%s\n</div>\n'
            '<div class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s\n</div>'
            % (s['h2'], intro, '\n'.join(tarjetas)))


def bloque_pasos(s):
    filas = []
    for i, p in enumerate(s['pasos'], 1):
        filas.append(
            '<div class="reveal glass-panel rounded-2xl border border-outline-variant/10 p-6" '
            'style="transition-delay:%dms">\n'
            '<span class="hc-rotulo">Paso %02d</span>\n'
            '<h3 class="mb-2 mt-1 text-lg font-bold">%s</h3>\n'
            '<p class="text-sm leading-relaxed text-on-surface-variant">%s</p>\n</div>'
            % ((i - 1) * 70, i, p['titulo'], p['texto']))
    return ('<div class="reveal">\n<h2 class="text-2xl font-bold sm:text-3xl">%s</h2>\n</div>\n'
            '<div class="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-4">\n%s\n</div>'
            % (s['h2'], '\n'.join(filas)))


def bloque_faq(s):
    items = []
    for q in s['preguntas']:
        items.append(
            '<details class="faq-item" id="%s">\n'
            '<summary><h3 class="faq-q">%s</h3>'
            '<span class="material-symbols-outlined faq-mas">add</span></summary>\n'
            '<div class="faq-a"><p>%s</p></div>\n</details>'
            % (slug_de(q['q']), q['q'], q['a']))
    extra = ''
    if s.get('mas'):
        enlaces = '\n'.join(
            '<li><a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@preguntasfrecuentes/#%s">%s</a></li>'
            % (a, t) for a, t in s['mas'])
        extra = ('\n<div class="mt-8 rounded-2xl border border-outline-variant/10 bg-surface-container-low p-6">\n'
                 '<p class="mb-3 text-sm font-semibold text-on-surface">Mas preguntas sobre esto</p>\n'
                 '<ul class="space-y-2 text-sm text-on-surface-variant">\n%s\n</ul>\n</div>' % enlaces)
    return ('<div class="reveal">\n<h2 class="text-2xl font-bold sm:text-3xl">%s</h2>\n</div>\n'
            '<div class="mt-6 max-w-3xl">\n%s\n</div>%s' % (s['h2'], '\n'.join(items), extra))


def bloque_cifras(s):
    """Numeros de un caso real. Solo se usan cifras que el dueno pueda defender."""
    celdas = []
    for i, c in enumerate(s['numeros']):
        celdas.append(
            '<div class="reveal rounded-2xl border border-outline-variant/10 bg-surface-container '
            'p-6 text-center" style="transition-delay:%dms">\n'
            '<p class="font-headline text-4xl font-black text-primary sm:text-5xl">%s</p>\n'
            '<p class="mt-2 text-sm font-semibold text-on-surface">%s</p>\n'
            '<p class="mt-1 text-xs leading-relaxed text-zinc-400">%s</p>\n</div>'
            % (i * 70, c['cifra'], c['titulo'], c.get('detalle', '')))
    intro = ('<p class="mt-4 max-w-3xl text-on-surface-variant">%s</p>' % s['intro']) if s.get('intro') else ''
    return ('<div class="reveal">\n<h2 class="text-2xl font-bold sm:text-3xl">%s</h2>\n%s\n</div>\n'
            '<div class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-%d">\n%s\n</div>'
            % (s['h2'], intro, min(len(s['numeros']), 4), '\n'.join(celdas)))


def bloque_casos(s):
    """Grilla de casos que enlaza a cada ficha."""
    fichas = []
    for i, c in enumerate(s['casos']):
        fichas.append(
            '<a class="reveal flex flex-col rounded-[20px] border border-outline-variant/10 '
            'bg-surface-container p-6 transition-colors hover:bg-surface-container-high" '
            'href="@@SUBIR@@%s/" style="transition-delay:%dms">\n'
            '<span class="material-symbols-outlined mb-3 text-3xl text-primary">%s</span>\n'
            '<h3 class="mb-2 text-lg font-bold">%s</h3>\n'
            '<p class="mb-4 text-sm leading-relaxed text-on-surface-variant">%s</p>\n'
            '<span class="mt-auto inline-flex items-center gap-1.5 text-sm font-semibold text-primary">'
            '%s<span class="material-symbols-outlined text-base">arrow_forward</span></span>\n</a>'
            % (c['slug'], i * 70, c.get('icono', 'work'), c['titulo'], c['texto'],
               c.get('cta', 'Ver el caso')))
    return ('<div class="reveal">\n<h2 class="text-2xl font-bold sm:text-3xl">%s</h2>\n</div>\n'
            '<div class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s\n</div>'
            % (s['h2'], '\n'.join(fichas)))


MESES = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')


def fecha_larga(iso):
    a, m, d = iso.split('-')
    return '%d de %s de %s' % (int(d), MESES[int(m) - 1], a)


def bloque_articulos(s):
    """Listado del blog. Cada nota enlaza a su pagina."""
    filas = []
    for i, a in enumerate(s['articulos']):
        filas.append(
            '<a class="reveal flex flex-col rounded-[20px] border border-outline-variant/10 '
            'bg-surface-container p-6 transition-colors hover:bg-surface-container-high" '
            'href="@@SUBIR@@%s/" style="transition-delay:%dms">\n'
            '<time class="hc-rotulo" datetime="%s">%s</time>\n'
            '<h3 class="mb-2 mt-2 text-lg font-bold leading-snug">%s</h3>\n'
            '<p class="mb-4 text-sm leading-relaxed text-on-surface-variant">%s</p>\n'
            '<span class="mt-auto inline-flex items-center gap-1.5 text-sm font-semibold text-primary">'
            'Leer<span class="material-symbols-outlined text-base">arrow_forward</span></span>\n</a>'
            % (a['slug'], i * 60, a['fecha'], fecha_larga(a['fecha']), a['titulo'], a['resumen']))
    return ('<div class="reveal">\n<h2 class="text-2xl font-bold sm:text-3xl">%s</h2>\n</div>\n'
            '<div class="mt-8 grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">\n%s\n</div>'
            % (s['h2'], '\n'.join(filas)))


RENDER = {'texto': bloque_texto, 'lista': bloque_lista, 'pasos': bloque_pasos,
          'faq': bloque_faq, 'cifras': bloque_cifras, 'casos': bloque_casos,
          'articulos': bloque_articulos}


def render_secciones(secciones):
    fuera = []
    for s in secciones:
        f = RENDER.get(s['tipo'])
        if not f:
            sys.exit('build: tipo de seccion desconocido: %r' % s['tipo'])
        fondo = ' bg-surface-container-low' if s.get('fondo') else ''
        fuera.append('<section class="py-16%s">\n<div class="container mx-auto px-4 sm:px-6 lg:px-8">\n%s\n</div>\n</section>'
                     % (fondo, f(s)))
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
<html class="dark" lang="es">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>@@TITULO@@</title>
<meta content="@@DESC@@" name="description"/>
<meta content="Zyntra" name="author"/>
<meta content="#100f0d" name="theme-color"/>
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
@@TAILWIND@@
@@CONFIG@@
@@FUENTES@@
<link href="@@SUBIR@@assets/zyntra.css" rel="stylesheet"/>
@@SCHEMA@@
</head>
<body class="bg-background text-on-surface selection:bg-primary/30 selection:text-primary">
<div class="scroll-progress" id="scroll-progress"></div>
@@HEADER@@
<main>

<section class="relative overflow-hidden px-0 pt-32 pb-16">
<div class="soft-grid absolute inset-0 z-0 opacity-[0.07]"></div>
<div class="mesh-glow absolute inset-0 z-0 opacity-40"></div>
<div class="container relative z-10 mx-auto px-4 sm:px-6 lg:px-8">
<nav aria-label="Ruta de navegación" class="mb-6 flex items-center gap-2 text-sm text-zinc-400">
<a class="hover:text-primary" href="@@SUBIR@@">Inicio</a>
<span class="material-symbols-outlined text-base">chevron_right</span>@@PADRE@@
<span class="text-on-surface">@@MIGAS@@</span>
</nav>
<div class="max-w-3xl">
<span class="material-symbols-outlined mb-4 text-4xl text-primary">@@ICONO@@</span>
<h1 class="text-3xl font-bold leading-tight tracking-tighter sm:text-4xl md:text-5xl">@@H1@@</h1>
@@FECHA@@
<p class="mt-5 text-lg font-light text-on-surface-variant sm:text-xl">@@BAJADA@@</p>
<div class="mt-8 flex flex-col gap-3 sm:flex-row sm:flex-wrap sm:gap-4">
<a class="inline-flex w-full items-center justify-center rounded-full bg-gradient-to-r from-primary to-secondary px-8 py-4 text-base font-bold text-on-primary-fixed shadow-xl shadow-primary/20 transition-transform hover:scale-105 sm:w-auto" href="@@WA@@" rel="noopener noreferrer" target="_blank">@@CTA_BOTON@@</a>
<a class="inline-flex w-full items-center justify-center gap-2 rounded-full border border-outline-variant/30 px-8 py-4 font-medium text-on-surface transition-colors hover:bg-white/5 sm:w-auto" href="@@SUBIR@@#contact-form">Pedir diagnóstico gratuito</a>
</div>
</div>
</div>
</section>

@@SECCIONES@@

<section class="relative overflow-hidden border-t border-outline-variant/10 bg-[#0a0908] py-20">
<div class="container mx-auto px-4 text-center sm:px-6 lg:px-8">
<h2 class="text-2xl font-bold sm:text-3xl">@@CTA_TITULO@@</h2>
<p class="mx-auto mt-3 max-w-xl text-on-surface-variant">@@CTA_TEXTO@@</p>
<div class="mt-7 flex flex-col justify-center gap-3 sm:flex-row">
<a class="inline-flex items-center justify-center gap-2 rounded-full bg-gradient-to-r from-primary to-secondary px-8 py-4 font-bold text-on-primary-fixed shadow-xl shadow-primary/20 transition-transform hover:scale-105" href="@@WA@@" rel="noopener noreferrer" target="_blank">
<span class="material-symbols-outlined text-xl">chat</span>@@CTA_BOTON@@</a>
<a class="inline-flex items-center justify-center gap-2 rounded-full border border-outline-variant/30 px-8 py-4 font-medium text-on-surface transition-colors hover:bg-white/5" href="@@SUBIR@@preguntasfrecuentes/">Ver las preguntas frecuentes</a>
</div>
</div>
</section>

</main>
@@FOOTER@@
@@FLOTANTES@@
<script src="@@SUBIR@@assets/zyntra.js"></script>
</body>
</html>
'''


def render(p, chrome):
    url = SITIO + p['slug'] + '/'
    wa = WA + p['wa']
    niveles = p['slug'].count('/') + 1
    reemplazos = {
        '@@TITULO@@': esc(p['titulo']),
        '@@DESC@@': esc(p['descripcion']),
        '@@URL@@': url,
        '@@SITIO@@': SITIO,
        '@@MIGAS@@': p['migas'],
        '@@PADRE@@': (
            '\n<a class="hover:text-primary" href="%s%s/">%s</a>\n'
            '<span class="material-symbols-outlined text-base">chevron_right</span>'
            % ('../' * niveles, p['padre']['slug'], p['padre']['nombre'])
        ) if p.get('padre') else '',
        '@@ICONO@@': p['icono'],
        '@@H1@@': p['h1'],
        '@@BAJADA@@': p['bajada'],
        '@@FECHA@@': ('<time class="mt-4 block text-sm text-zinc-400" datetime="%s">'
                      'Publicado el %s</time>'
                      % (p['articulo']['fecha'], fecha_larga(p['articulo']['fecha']))
                      ) if p.get('articulo') else '',
        '@@WA@@': wa,
        '@@CTA_BOTON@@': p['cta']['boton'],
        '@@CTA_TITULO@@': p['cta']['titulo'],
        '@@CTA_TEXTO@@': p['cta']['texto'],
        '@@TAILWIND@@': chrome['tailwind'],
        '@@CONFIG@@': chrome['config'],
        '@@FUENTES@@': chrome['aviso_iconos'] + '\n' + chrome['fuentes'],
        '@@HEADER@@': subir(chrome['header'], niveles),
        '@@FOOTER@@': subir(chrome['footer'], niveles),
        '@@FLOTANTES@@': subir(chrome['flotantes'], niveles),
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
    n = escribir_sitemap([p['slug'] for p in paginas])
    print('\n%d paginas generadas · sitemap.xml con %d URLs' % (len(paginas), n))


if __name__ == '__main__':
    main()
