# -*- coding: utf-8 -*-
"""
Sistema de diseno de Zyntra para PDF.

Es la traduccion a papel del mismo sistema que usa la web: misma paleta,
mismas tipografias, mismos radios, sin sombras y sin degradados. Lo que
cambia es el soporte, no la identidad.

Por que existe: los PDF descargables (propuestas, metodologia) son la pieza
que el cliente guarda y reenvia. Si tienen otra cara que el sitio, la marca
se parte al medio.

TRAMPA DE LAS TIPOGRAFIAS: Bricolage Grotesque e Instrument Sans son fuentes
VARIABLES. ReportLab solo sabe leer la instancia por defecto de una variable,
que es el peso normal, asi que los titulos en 800 salian finitos. Aca se
genera una instancia estatica de cada peso con fontTools y se registra esa.

Dependencias, que no las tiene el resto del repo: reportlab y fonttools.
Solo hacen falta para generar los PDF, no para el sitio.

Uso:  from pdf_marca import Documento
      d = Documento('propuesta-x', 'Titulo', 'Bajada')
      d.portada(...); d.seccion(...); d.parrafo(...); d.guardar()
"""
import io
import os
import sys

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont as RLFont
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import marca  # noqa: E402  (de ahi sale el descargador de Google Fonts)

# ------------------------------------------------------------------ paleta

TINTA = HexColor('#171310')
ACENTO = HexColor('#E4572E')
ACENTO_TEXTO = HexColor('#B93A15')
ACENTO2 = HexColor('#2F6B4F')
ARENA = HexColor('#E3D8C4')
CREMA = HexColor('#F5F0E6')
SUPERFICIE = HexColor('#EDE6D8')
TEXTO = HexColor('#4A423A')
TEXTO_2 = HexColor('#6B6155')
MONO_CLARO = HexColor('#6E6357')
SOBRE_TINTA = HexColor('#9A8F82')
SOBRE_TINTA_3 = HexColor('#90857A')
BORDE = HexColor('#DDD2BE')
DIVISOR_TINTA = HexColor('#2E2822')

# ------------------------------------------------------------- tipografias

CACHE = os.path.join(os.environ.get('TEMP', '/tmp'), 'zyntra-fuentes')

# nombre en ReportLab -> (familia Google, ejes, archivo, peso a fijar)
#
# OJO: cada cara necesita su PROPIO archivo de cache. Antes las dos de
# Instrument Sans compartian 'instrument.ttf', y como el descargador cachea
# por nombre de archivo, la segunda se quedaba con el archivo de la primera:
# la "negrita" era en realidad la redonda, y ningun <b> se veia.
CARAS = {
    'Bric-800': ('Bricolage+Grotesque', 'opsz,wght@12..96,800', 'bricolage-800.ttf', 800),
    'Bric-600': ('Bricolage+Grotesque', 'opsz,wght@12..96,600', 'bricolage-600.ttf', 600),
    'Inst-400': ('Instrument+Sans', 'wght@400', 'instrument-400.ttf', 400),
    'Inst-600': ('Instrument+Sans', 'wght@600', 'instrument-600.ttf', 600),
    'Mono-600': ('JetBrains+Mono', 'wght@600', 'jetbrains-600.ttf', 600),
}

# ReportLab resuelve <b> por FAMILIA, no por nombre de cara suelto: sin esto,
# todos los <b> del contenido se renderizaban en redonda y no se notaba.
FAMILIAS = [
    ('Inst-400', 'Inst-400', 'Inst-600'),
    ('Bric-600', 'Bric-600', 'Bric-800'),
    ('Bric-800', 'Bric-800', 'Bric-800'),
    ('Mono-600', 'Mono-600', 'Mono-600'),
]

_registradas = False


def _estatica(origen, peso, destino):
    """
    Genera una instancia estatica del peso pedido. Sin esto ReportLab usa la
    instancia por defecto de la variable (peso normal) y los titulos en 800
    salen igual de finos que el cuerpo.
    """
    if os.path.exists(destino):
        return destino
    f = TTFont(origen)
    if 'fvar' in f:
        ejes = {a.axisTag: a.defaultValue for a in f['fvar'].axes}
        if 'wght' in ejes:
            ejes['wght'] = peso
        if 'opsz' in ejes:
            ejes['opsz'] = 14      # tamano optico de texto, no de display
        f = instantiateVariableFont(f, ejes, inplace=True, updateFontNames=False)
    f.save(destino)
    return destino


def registrar_fuentes():
    global _registradas
    if _registradas:
        return
    os.makedirs(CACHE, exist_ok=True)
    for nombre, (familia, ejes, archivo, peso) in CARAS.items():
        variable = marca.fuente(familia, ejes, archivo)
        estatica = os.path.join(CACHE, '%s.ttf' % nombre)
        pdfmetrics.registerFont(RLFont(nombre, _estatica(variable, peso, estatica)))
    for familia, normal, negrita in FAMILIAS:
        pdfmetrics.registerFontFamily(familia, normal=normal, bold=negrita,
                                      italic=normal, boldItalic=negrita)
    _registradas = True


# ---------------------------------------------------------------- estilos

def estilos():
    registrar_fuentes()
    def e(nombre, **kw):
        base = dict(name=nombre, alignment=TA_LEFT, textColor=TEXTO,
                    fontName='Inst-400', fontSize=10, leading=15.5)
        base.update(kw)
        return ParagraphStyle(**base)

    return {
        'display':   e('display', fontName='Bric-800', fontSize=34, leading=35,
                       textColor=CREMA),
        'portada-baja': e('portada-baja', fontName='Inst-400', fontSize=12.5,
                          leading=19, textColor=SOBRE_TINTA),
        'h2':        e('h2', fontName='Bric-800', fontSize=17, leading=20,
                       textColor=TINTA, spaceBefore=0, spaceAfter=0),
        'h3':        e('h3', fontName='Bric-600', fontSize=12, leading=16,
                       textColor=TINTA, spaceBefore=10, spaceAfter=3),
        'cuerpo':    e('cuerpo', spaceAfter=7),
        'cuerpo-tinta': e('cuerpo-tinta', textColor=SOBRE_TINTA, spaceAfter=7),
        'chico':     e('chico', fontSize=9, leading=13.5, textColor=TEXTO_2),
        'mono':      e('mono', fontName='Mono-600', fontSize=7, leading=11,
                       textColor=MONO_CLARO),
        'mono-tinta': e('mono-tinta', fontName='Mono-600', fontSize=7, leading=11,
                        textColor=SOBRE_TINTA_3),
        'vineta':    e('vineta', leftIndent=14, spaceAfter=5),
        'celda':     e('celda', fontSize=8.5, leading=12.5),
        'celda-cab': e('celda-cab', fontName='Mono-600', fontSize=6.8, leading=10,
                       textColor=CREMA),
        'dato':      e('dato', fontName='Bric-800', fontSize=30, leading=32,
                       textColor=ACENTO),
    }


# ----------------------------------------------------------------- Ojito

class Ojito(Flowable):
    """
    La mascota, dibujada como vector. Mismas proporciones que en la web y en
    el favicon: ojo 0.63 de la caja, iris 0.458 del ojo, pupila 0.455 del
    iris, parpado 0.167.

    lid: 0 abierto | .16 normal | .42 sospechando | .8 durmiendo
    EL PARPADO ES LA UNICA EXPRESION.
    """

    def __init__(self, lado=28 * mm, lid=.16, sobre_tinta=False):
        Flowable.__init__(self)
        self.lado = lado
        self.lid = lid
        self.oscuro = sobre_tinta
        self.width = lado
        self.height = lado * 1.26

    def draw(self):
        c = self.canv
        n = self.lado
        cuerpo = CREMA
        borde = CREMA if self.oscuro else TINTA
        patas = CREMA if self.oscuro else TINTA

        cx, cy, r = n / 2, self.height - n / 2, n / 2

        # patas, primero: van detras del cuerpo
        c.setFillColor(patas)
        anchoP, altoP = n * .11, n * .26
        for dx in (-n * .125, n * .125):
            c.rect(cx + dx - anchoP / 2, cy - r - altoP + n * .08, anchoP, altoP,
                   stroke=0, fill=1)
            c.rect(cx + dx - n * .14, cy - r - altoP + n * .08, n * .28, n * .09,
                   stroke=0, fill=1)

        # el ojo se recorta contra su propio circulo: el parpado es un arco
        # cuyos extremos caen donde el circulo no tiene ancho
        c.saveState()
        p = c.beginPath()
        p.circle(cx, cy, r)
        c.clipPath(p, stroke=0, fill=0)

        c.setFillColor(cuerpo)
        c.circle(cx, cy, r, stroke=0, fill=1)
        c.setFillColor(ACENTO)
        c.circle(cx, cy, r * .458, stroke=0, fill=1)
        c.setFillColor(TINTA)
        c.circle(cx, cy, r * .458 * .455, stroke=0, fill=1)
        c.setFillColor(cuerpo)
        c.circle(cx + r * .28, cy + r * .32, r * .146, stroke=0, fill=1)

        if self.lid > 0:
            c.setFillColor(TINTA)
            alto = n * self.lid
            c.rect(cx - r, cy + r - alto, 2 * r, alto + r, stroke=0, fill=1)
        c.restoreState()

        c.setStrokeColor(borde)
        c.setLineWidth(n * .045)
        c.circle(cx, cy, r, stroke=1, fill=0)




class Punto(Flowable):
    """El punto naranja del sistema, como vineta. Dibujado, no escrito."""

    def __init__(self, color=None, radio=1.7, sangria=3):
        Flowable.__init__(self)
        self.color = color or ACENTO
        self.radio = radio
        self.sangria = sangria
        self.width = 7 * mm
        self.height = 11

    def draw(self):
        self.canv.setFillColor(self.color)
        # alineado con la primera linea de texto, no con el tope de la celda
        self.canv.circle(self.sangria + self.radio, self.height - 6,
                         self.radio, stroke=0, fill=1)


class Isotipo(Flowable):
    """
    El isotipo de marca: cuadrado blando con la Z y el punto naranja. Se usa
    donde NO va Ojito, que hoy es solo pentesting.
    """

    def __init__(self, lado=26 * mm, sobre_tinta=True):
        Flowable.__init__(self)
        self.lado = lado
        self.oscuro = sobre_tinta
        self.width = self.height = lado

    def draw(self):
        c = self.canv
        n = self.lado
        fondo = CREMA if self.oscuro else TINTA
        letra = TINTA if self.oscuro else CREMA

        c.setFillColor(fondo)
        c.roundRect(0, 0, n, n, n * .34, stroke=0, fill=1)

        # la Z como poligono: mismas diez esquinas que el favicon, pero con
        # el eje Y al reves, que es como mide reportlab
        Z = [(20, 22), (80, 22), (80, 34), (38, 66), (80, 66),
             (80, 78), (20, 78), (20, 66), (62, 34), (20, 34)]
        p = c.beginPath()
        for i, (x, y) in enumerate(Z):
            px, py = x * n / 100, n - y * n / 100
            p.moveTo(px, py) if i == 0 else p.lineTo(px, py)
        p.close()
        c.setFillColor(letra)
        c.drawPath(p, stroke=0, fill=1)

        cx, cy = n * .84, n * .16
        c.setFillColor(fondo)
        c.circle(cx, cy, n * .145, stroke=0, fill=1)
        c.setFillColor(ACENTO)
        c.circle(cx, cy, n * .11, stroke=0, fill=1)


class Linea(Flowable):
    """Divisor de 1pt, del ancho del marco."""

    def __init__(self, color=BORDE, arriba=6, abajo=6):
        Flowable.__init__(self)
        self.color = color
        self.height = arriba + abajo
        self.arriba = arriba

    def wrap(self, w, h):
        self.width = w
        return w, self.height

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(.7)
        y = self.height - self.arriba
        self.canv.line(0, y, self.width, y)


class Caja(Flowable):
    """Un rectangulo de color detras de un bloque, con radio del sistema."""

    def __init__(self, contenido, fondo=SUPERFICIE, pad=9, radio=6, ancho=None):
        Flowable.__init__(self)
        self.contenido = contenido
        self.fondo = fondo
        self.pad = pad
        self.radio = radio
        self._ancho = ancho

    def wrap(self, w, h):
        self.width = self._ancho or w
        interior = self.width - 2 * self.pad
        self.alturas = []
        total = 0
        for f in self.contenido:
            _, fh = f.wrap(interior, h)
            self.alturas.append(fh)
            total += fh
        self.height = total + 2 * self.pad
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(self.fondo)
        c.roundRect(0, 0, self.width, self.height, self.radio, stroke=0, fill=1)
        y = self.height - self.pad
        for f, fh in zip(self.contenido, self.alturas):
            y -= fh
            f.drawOn(c, self.pad, y)


# ------------------------------------------------------------- documento

ANCHO, ALTO = A4
MARGEN = 20 * mm
SITIO = 'zyntraexperts.com'
CONTACTO = 'zyntraconsultoraia@gmail.com  ·  WhatsApp +54 9 11 6643-9309'


class Documento(object):
    """
    Un PDF del sistema. Se arma llamando a los metodos en orden y al final
    guardar(). La portada va en tinta y el interior en arena, con el texto
    sobre un panel crema: el mismo ritmo que la web.
    """

    def __init__(self, archivo, titulo, subtitulo, rotulo='PROPUESTA DE SERVICIO',
                 pie=None, lid=.16, ojito=True, carpeta='docs'):
        # ojito=False es para pentesting: el brandboard prohibe la mascota
        # ahi, va el logotipo solo.
        #
        # carpeta: 'docs' son los PDF que se publican en el sitio. Las piezas
        # que se mandan por mano (propuestas a medida, por ejemplo) van a otra
        # carpeta para no terminar servidas en zyntraexperts.com sin querer.
        destino = os.path.join(RAIZ, carpeta)
        if not os.path.isdir(destino):
            os.makedirs(destino)
        self.ruta = os.path.join(destino, archivo + '.pdf')
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.rotulo = rotulo
        self.pie = pie or titulo
        self.lid = lid
        self.ojito = ojito
        self.E = estilos()
        self.flujo = []

        self.doc = BaseDocTemplate(
            self.ruta, pagesize=A4,
            leftMargin=MARGEN, rightMargin=MARGEN,
            topMargin=MARGEN, bottomMargin=18 * mm,
            title=titulo, author='Zyntra', subject=subtitulo, creator='Zyntra')

        marco = Frame(MARGEN, 18 * mm, ANCHO - 2 * MARGEN,
                      ALTO - MARGEN - 18 * mm, id='cuerpo',
                      leftPadding=0, rightPadding=0,
                      topPadding=0, bottomPadding=0)

        self.doc.addPageTemplates([
            PageTemplate(id='portada', frames=[marco], onPage=self._fondo_portada),
            PageTemplate(id='interior', frames=[marco], onPage=self._fondo_interior),
        ])

    # ------------------------------------------------------------ fondos

    def _fondo_portada(self, canvas, doc):
        canvas.setFillColor(TINTA)
        canvas.rect(0, 0, ANCHO, ALTO, stroke=0, fill=1)
        # el contacto se ancla al pie: si va en el flujo queda colgando del
        # titulo y deja media pagina vacia
        canvas.setStrokeColor(DIVISOR_TINTA)
        canvas.setLineWidth(.7)
        canvas.line(MARGEN, 34 * mm, ANCHO - MARGEN, 34 * mm)
        canvas.setFont('Mono-600', 7)
        canvas.setFillColor(SOBRE_TINTA_3)
        canvas.drawString(MARGEN, 27 * mm, CONTACTO)
        canvas.setFillColor(ACENTO)
        canvas.drawString(MARGEN, 21 * mm, SITIO.upper())

    def _fondo_interior(self, canvas, doc):
        canvas.setFillColor(ARENA)
        canvas.rect(0, 0, ANCHO, ALTO, stroke=0, fill=1)
        canvas.setFillColor(CREMA)
        canvas.roundRect(MARGEN - 7 * mm, 13 * mm,
                         ANCHO - 2 * (MARGEN - 7 * mm), ALTO - 23 * mm,
                         8, stroke=0, fill=1)
        canvas.setFont('Mono-600', 6.5)
        canvas.setFillColor(MONO_CLARO)
        canvas.drawString(MARGEN, 8 * mm, ('Zyntra  ·  %s' % self.pie).upper()[:80])
        canvas.setFillColor(ACENTO_TEXTO)
        canvas.drawRightString(ANCHO - MARGEN, 8 * mm, '%d' % doc.page)

    # ---------------------------------------------------------- contenido

    def portada(self, parrafos=()):
        A = self.flujo.append
        A(Spacer(1, 26 * mm))
        if self.ojito:
            A(Ojito(30 * mm, self.lid, sobre_tinta=True))
            A(Spacer(1, 15 * mm))
        else:
            A(Isotipo(26 * mm))
            A(Spacer(1, 15 * mm))
        A(Paragraph(self.rotulo.upper(), self.E['mono-tinta']))
        A(Spacer(1, 5 * mm))
        A(Paragraph(self.titulo, self.E['display']))
        A(Spacer(1, 7 * mm))
        A(Paragraph(self.subtitulo, self.E['portada-baja']))
        for p in parrafos:
            A(Spacer(1, 3 * mm))
            A(Paragraph(p, self.E['portada-baja']))
        A(NextPageTemplate('interior'))
        A(PageBreak())

    def seccion(self, numero, titulo, intro=None):
        """Encabezado de seccion: el numero en naranja, como en el sitio."""
        A = self.flujo.append
        if str(numero).strip():
            filas = [[Paragraph(str(numero), self.E['mono']),
                      Paragraph(titulo, self.E['h2'])]]
            anchos = [11 * mm, None]
        else:
            filas = [[Paragraph(titulo, self.E['h2'])]]
            anchos = [None]
        t = Table(filas, colWidths=anchos)
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 1),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
            ('TEXTCOLOR', (0, 0), (0, 0), ACENTO),
        ]))
        A(Spacer(1, 7 * mm))
        A(t)
        A(Spacer(1, 1.5 * mm))
        A(Linea(BORDE, 0, 5))
        if intro:
            A(Paragraph(intro, self.E['cuerpo']))

    def titulo3(self, texto):
        self.flujo.append(Paragraph(texto, self.E['h3']))

    def parrafo(self, texto, estilo='cuerpo'):
        self.flujo.append(Paragraph(texto, self.E[estilo]))

    def vinetas(self, items, color=None):
        """
        Lista con el punto naranja del sistema como vineta.

        El punto se DIBUJA, no se escribe: ni Instrument Sans ni las
        instancias estaticas que genera este modulo traen el glifo U+25CF, y
        salia el cuadradito de caracter faltante.
        """
        col = color or ACENTO
        util = ANCHO - 2 * MARGEN
        for it in items:
            t = Table([[Punto(col), Paragraph(it, self.E['cuerpo'])]],
                      colWidths=[7 * mm, util - 7 * mm])
            t.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                ('LEFTPADDING', (0, 0), (-1, -1), 0),
                ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                ('TOPPADDING', (0, 0), (-1, -1), 0),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ]))
            self.flujo.append(t)

    def tabla(self, cabeceras, filas, anchos=None):
        datos = [[Paragraph(c.upper(), self.E['celda-cab']) for c in cabeceras]]
        for f in filas:
            datos.append([Paragraph(str(c), self.E['celda']) for c in f])
        util = ANCHO - 2 * MARGEN
        if anchos:
            total = float(sum(anchos))
            anchos = [util * a / total for a in anchos]
        t = Table(datos, colWidths=anchos, repeatRows=1, hAlign='LEFT')
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), TINTA),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 7),
            ('RIGHTPADDING', (0, 0), (-1, -1), 7),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [CREMA, SUPERFICIE]),
            ('LINEBELOW', (0, 1), (-1, -1), .5, BORDE),
        ]))
        self.flujo.append(Spacer(1, 2 * mm))
        self.flujo.append(t)
        self.flujo.append(Spacer(1, 3 * mm))

    def importante(self, texto, rotulo='LO IMPORTANTE'):
        """El bloque destacado. Va sobre superficie, nunca sobre naranja."""
        c = Caja([Paragraph(rotulo, self.E['mono']),
                  Spacer(1, 2.5 * mm),
                  Paragraph(texto, self.E['cuerpo'])], SUPERFICIE, pad=10)
        self.flujo.append(Spacer(1, 3 * mm))
        self.flujo.append(c)
        self.flujo.append(Spacer(1, 3 * mm))

    def dato(self, numero, texto):
        """Un numero grande con su explicacion al lado."""
        t = Table([[Paragraph(numero, self.E['dato']),
                    Paragraph(texto, self.E['cuerpo'])]],
                  colWidths=[34 * mm, None])
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (-1, -1), 0),
            ('TOPPADDING', (0, 0), (-1, -1), 4),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ]))
        self.flujo.append(Spacer(1, 2 * mm))
        self.flujo.append(t)
        self.flujo.append(Spacer(1, 2 * mm))

    def cierre(self, titulo, texto, lid=.0):
        """El bloque final, en tinta, con Ojito."""
        self.flujo.append(Spacer(1, 8 * mm))
        util = ANCHO - 2 * MARGEN
        izq = [Paragraph(titulo, ParagraphStyle(
                   'cierre-t', parent=self.E['h2'], textColor=CREMA,
                   fontSize=15, leading=19)),
               Spacer(1, 3 * mm),
               Paragraph(texto, self.E['cuerpo-tinta']),
               Spacer(1, 4 * mm),
               Paragraph(CONTACTO, self.E['mono-tinta'])]
        derecha = Ojito(19 * mm, lid, sobre_tinta=True) if self.ojito else Isotipo(17 * mm)
        t = Table([[izq, derecha]], colWidths=[util - 36 * mm, 32 * mm])
        t.setStyle(TableStyle([
            ('VALIGN', (0, 0), (0, 0), 'TOP'),
            ('VALIGN', (1, 0), (1, 0), 'MIDDLE'),
            ('BACKGROUND', (0, 0), (-1, -1), TINTA),
            ('LEFTPADDING', (0, 0), (-1, -1), 11),
            ('RIGHTPADDING', (0, 0), (-1, -1), 11),
            ('TOPPADDING', (0, 0), (-1, -1), 11),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 11),
        ]))
        self.flujo.append(KeepTogether(t))

    def salto(self):
        self.flujo.append(PageBreak())

    def espacio(self, mm_=4):
        self.flujo.append(Spacer(1, mm_ * mm))

    def guardar(self):
        self.doc.build(self.flujo)
        from pypdf import PdfReader
        n = len(PdfReader(self.ruta).pages)
        return os.path.basename(self.ruta), n, os.path.getsize(self.ruta) / 1024
