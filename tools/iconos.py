# -*- coding: utf-8 -*-
"""
Set de iconos propio de Zyntra.

Por que existe: el sistema nuevo prohibe iconos de librerias de terceros. La
regla del brandboard es "linea pareja, esquinas redondeadas, grilla de 24,
SIEMPRE en tinta con un unico detalle naranja". Material Symbols no cumple
nada de eso y ademas costaba 70 KB de fuente.

Como se usa:
    <svg class="ico"><use href="#i-turnos"></use></svg>

El sprite se INYECTA en cada pagina (no se referencia como archivo externo:
<use href="archivo.svg#id"> no es confiable en todos los navegadores).
build.py llama a sprite() y lo pega apenas abre el <body>.

Como agregar uno nuevo:
    1. sumarlo al dict ICONOS de abajo, respetando el trazo y el punto naranja
    2. correr python tools/build.py  (el sprite se regenera solo)
    3. si lo usas en index.html, correr tambien python tools/iconos.py, que
       reescribe el sprite dentro de index.html

Uso:  python tools/iconos.py        actualiza el sprite dentro de index.html
"""
import io
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Grosor del trazo. El brandboard pide 4px sobre formas de ~26px; llevado a
# una viewBox de 24 eso da 2.75. Mas grueso que esto y los iconos con detalle
# (factura, carta) se empastan.
TRAZO = '2.75'

# El punto naranja se pinta con var(--punto-ico) y no con el hex directo:
# asi un icono sobre fondo naranja puede cambiarlo sin tocar el sprite.
D = 'fill="var(--punto-ico)" stroke="none"'

ICONOS = {
    # ---------------------------------------------------------- servicios
    'chatbot': '<rect x="3" y="4" width="18" height="12.5" rx="4"/>'
               '<path d="M8 16.5v4l4.5-4"/>'
               '<circle cx="12" cy="10.2" r="1.9" %s/>' % D,

    'turnos': '<rect x="3" y="5" width="18" height="16" rx="3"/>'
              '<path d="M3 10h18M8 3v4M16 3v4"/>'
              '<circle cx="12" cy="15.4" r="1.9" %s/>' % D,

    'embudo': '<path d="M3 5h18l-7 8v6l-4-2v-4z"/>'
              '<circle cx="19.5" cy="18.5" r="2" %s/>' % D,

    'mapa': '<path d="M12 21.2s7.2-6.4 7.2-11.2a7.2 7.2 0 1 0-14.4 0c0 4.8 7.2 11.2 7.2 11.2z"/>'
            '<circle cx="12" cy="10" r="2.2" %s/>' % D,

    'gestion': '<path d="M5 20.5V11M12 20.5V6.5M19 20.5v-6"/>'
               '<circle cx="19" cy="4.6" r="2" %s/>' % D,

    'automatizacion': '<path d="M20 12a8 8 0 1 1-3.4-6.5"/>'
                      '<path d="M20.8 3.6V9h-5.4"/>'
                      '<circle cx="12" cy="12" r="2.1" %s/>' % D,

    # sin las pesas exteriores: a 20px, cinco trazos se empastan en una mancha
    'mancuerna': '<rect x="2.4" y="8.6" width="4" height="6.8" rx="1.4"/>'
                 '<rect x="17.6" y="8.6" width="4" height="6.8" rx="1.4"/>'
                 '<path d="M6.4 12h11.2"/>'
                 '<circle cx="12" cy="12" r="2.1" %s/>' % D,

    'qr': '<rect x="3" y="3" width="7" height="7" rx="2"/>'
          '<rect x="14" y="3" width="7" height="7" rx="2"/>'
          '<rect x="3" y="14" width="7" height="7" rx="2"/>'
          '<rect x="14" y="14" width="7" height="7" rx="2" %s/>' % D,

    'tablero': '<path d="M3.8 18a8.2 8.2 0 1 1 16.4 0"/>'
               '<path d="M12 18l4.2-5.4"/>'
               '<circle cx="12" cy="18" r="1.9" %s/>' % D,

    'cobros': '<rect x="2.5" y="6" width="19" height="12" rx="3"/>'
              '<path d="M6 12h.01M18 12h.01"/>'
              '<circle cx="12" cy="12" r="2.6" %s/>' % D,

    'factura': '<path d="M6 3h8l4 4v14H6z"/>'
               '<path d="M14 3v4h4"/>'
               '<path d="M9.5 13.5h5M9.5 17h3.5"/>'
               '<circle cx="9.6" cy="9.6" r="1.6" %s/>' % D,

    'medalla': '<circle cx="12" cy="9" r="5.8"/>'
               '<path d="M8.4 14.2L7 21l5-2.6L17 21l-1.4-6.8"/>'
               '<circle cx="12" cy="9" r="2" %s/>' % D,

    'web': '<rect x="2.5" y="4" width="19" height="16" rx="3"/>'
           '<path d="M2.5 9h19"/>'
           '<circle cx="6.2" cy="6.5" r="1.4" %s/>' % D,

    'renovar': '<path d="M3.6 12a8.4 8.4 0 0 1 14.4-5.9"/><path d="M18.6 3v4h-4"/>'
               '<path d="M20.4 12a8.4 8.4 0 0 1-14.4 5.9"/><path d="M5.4 21v-4h4"/>'
               '<circle cx="12" cy="12" r="2.1" %s/>' % D,

    'gota': '<path d="M12 3.4c4 4.3 6 7 6 9.6a6 6 0 0 1-12 0c0-2.6 2-5.3 6-9.6z"/>'
            '<circle cx="12" cy="14" r="2.1" %s/>' % D,

    'carta': '<rect x="4" y="3" width="16" height="18" rx="3"/>'
             '<path d="M8 9h8M8 13h5"/>'
             '<circle cx="16" cy="16.6" r="1.8" %s/>' % D,

    'escudo': '<path d="M12 3l7.4 3v5.5c0 4.6-3 8.2-7.4 9.5-4.4-1.3-7.4-4.9-7.4-9.5V6z"/>'
              '<circle cx="12" cy="11.4" r="2.2" %s/>' % D,

    'candado': '<rect x="4" y="10" width="16" height="11" rx="3"/>'
               '<path d="M8 10V7a4 4 0 0 1 8 0v3"/>'
               '<circle cx="12" cy="15.5" r="1.9" %s/>' % D,

    # --------------------------------------------------------- industrias
    'plato': '<path d="M2.8 16h18.4"/>'
             '<path d="M4.6 16a7.4 7.4 0 0 1 14.8 0"/>'
             '<circle cx="12" cy="6.6" r="1.8" %s/>' % D,

    'salud': '<rect x="3" y="3" width="18" height="18" rx="5"/>'
             '<path d="M12 8v8M8 12h8" stroke="var(--punto-ico)"/>',

    'hoja': '<path d="M4.6 19.4c0-8 5-14.8 14.8-14.8 0 8-5.4 14.8-14.8 14.8z"/>'
            '<circle cx="10.6" cy="13.4" r="1.9" %s/>' % D,

    'bolsa': '<path d="M4.6 7.6h14.8l-1 12.8H5.6z"/>'
             '<path d="M8.6 7.6V6a3.4 3.4 0 0 1 6.8 0v1.6"/>'
             '<circle cx="12" cy="13.6" r="1.9" %s/>' % D,

    'credencial': '<rect x="2.5" y="5" width="19" height="14" rx="3"/>'
                  '<path d="M13.4 10h5M13.4 14h3"/>'
                  '<circle cx="8" cy="12" r="2.4" %s/>' % D,

    'fabrica': '<path d="M3 20.5V11l6 3.4V11l6 3.4V5.5h6v15z"/>'
               '<circle cx="18" cy="15.4" r="1.8" %s/>' % D,

    'escuadra': '<path d="M4 3.6v16.8h16.8"/>'
                '<path d="M4 3.6l16.8 16.8"/>'
                '<circle cx="9" cy="16" r="1.9" %s/>' % D,

    'birrete': '<path d="M2.4 9L12 4.4 21.6 9 12 13.6z"/>'
               '<path d="M6.6 11.2v4.6c0 1.7 2.4 3 5.4 3s5.4-1.3 5.4-3v-4.6"/>'
               '<circle cx="20.6" cy="14.6" r="1.8" %s/>' % D,

    'huella': '<circle cx="12" cy="15.4" r="4.2"/>'
              '<circle cx="5.8" cy="10.4" r="2.1"/>'
              '<circle cx="11.4" cy="6.4" r="2.1"/>'
              '<circle cx="18.2" cy="10.4" r="2.1" %s/>' % D,

    'auto': '<path d="M3.2 15.4v-2.6l2-5.2h13.6l2 5.2v2.6"/>'
            '<path d="M2.6 15.4h18.8"/>'
            '<circle cx="7.4" cy="18.2" r="1.9"/>'
            '<circle cx="16.6" cy="18.2" r="1.9" %s/>' % D,

    'corazon': '<path d="M12 20.4S3.6 14.9 3.6 9.3A4.6 4.6 0 0 1 12 6.5a4.6 4.6 0 0 1 8.4 2.8c0 5.6-8.4 11.1-8.4 11.1z"/>',

    'regalo': '<rect x="3" y="9.2" width="18" height="11.4" rx="2.5"/>'
              '<path d="M2.2 9.2h19.6M12 9.2v11.4"/>'
              '<circle cx="12" cy="5.6" r="2.2" %s/>' % D,

    # ------------------------------------------------------------- chrome
    'check':        '<path d="M4.5 12.6l5 5 10-11"/>',
    'flecha':       '<path d="M4 12h15M13 6l6 6-6 6"/>',
    'flecha-abajo': '<path d="M12 4v15M6 13l6 6 6-6"/>',
    'menu':         '<path d="M4 7h16M4 12h16M4 17h16"/>',
    'cerrar':       '<path d="M6 6l12 12M18 6L6 18"/>',
    'descarga':     '<path d="M12 3v12M7 11l5 5 5-5M4 20.5h16"/>',
    'externo':      '<path d="M14 3.8h6.2V10"/><path d="M20.2 3.8L11 13"/>'
                    '<path d="M18 14v5.2a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 4 18.7v-11A1.5 1.5 0 0 1 5.5 6.2H10"/>',
    'mail':         '<rect x="2.5" y="5" width="19" height="14" rx="3"/>'
                    '<path d="M3.6 7.6L12 13.2l8.4-5.6"/>',
    'lupa':         '<circle cx="10.8" cy="10.8" r="6.4"/><path d="M15.6 15.6l5 5"/>',
    'reloj':        '<circle cx="12" cy="12" r="8.4"/><path d="M12 6.8V12.4l3.6 2.2"/>',
    'calculadora':  '<rect x="4" y="2.5" width="16" height="19" rx="3"/><path d="M8 7h8"/>'
                    '<circle cx="9" cy="12.2" r="1.4" %s/>'
                    '<circle cx="15" cy="12.2" r="1.4" fill="currentColor" stroke="none"/>'
                    '<circle cx="9" cy="17" r="1.4" fill="currentColor" stroke="none"/>'
                    '<circle cx="15" cy="17" r="1.4" fill="currentColor" stroke="none"/>' % D,
    'idiomas':      '<circle cx="12" cy="12" r="8.4"/>'
                    '<path d="M3.6 12h16.8"/>'
                    '<path d="M12 3.6a13 13 0 0 1 0 16.8 13 13 0 0 1 0-16.8"/>',
    'personas':     '<circle cx="9" cy="8.4" r="3.4"/>'
                    '<path d="M3 20.4c0-3.3 2.7-6 6-6s6 2.7 6 6"/>'
                    '<circle cx="17.6" cy="8" r="2.4" %s/>' % D,
    'bloques':      '<circle cx="7" cy="7" r="3.2"/><circle cx="17" cy="7" r="3.2"/>'
                    '<circle cx="7" cy="17" r="3.2"/><circle cx="17" cy="17" r="3.2" %s/>' % D,
    'maletin':      '<rect x="2.6" y="7" width="18.8" height="13" rx="3"/>'
                    '<path d="M8.6 7V5.4a2 2 0 0 1 2-2h2.8a2 2 0 0 1 2 2V7"/>'
                    '<circle cx="12" cy="13.6" r="1.9" %s/>' % D,
    'balanza':      '<path d="M12 5.6v14.8M6.4 20.4h11.2M4 9.2h16"/>'
                    '<path d="M4 9.2l-2.4 5.2h4.8zM20 9.2l-2.4 5.2h4.8z"/>'
                    '<circle cx="12" cy="4" r="1.8" %s/>' % D,
    'check-circulo': '<circle cx="12" cy="12" r="8.6"/>'
                     '<path d="M8.2 12.2l2.6 2.6 5-5.4" stroke="var(--punto-ico)"/>',
    'equis-circulo': '<circle cx="12" cy="12" r="8.6"/>'
                     '<path d="M9.2 9.2l5.6 5.6M14.8 9.2l-5.6 5.6" stroke="var(--punto-ico)"/>',
}

# Que icono nuevo reemplaza a cada Material Symbol del sitio viejo. Lo usan
# build.py (el campo 'icono' de cada PAGINA sigue escrito con el nombre viejo)
# y los scripts de migracion. Si una pagina pide un nombre que no esta aca,
# build.py corta: mejor eso que servir un icono equivocado.
EQUIV = {
    # servicios
    'smart_toy': 'chatbot', 'event_available': 'turnos', 'campaign': 'embudo',
    'reviews': 'mapa', 'analytics': 'gestion', 'hub': 'automatizacion',
    'fitness_center': 'mancuerna', 'qr_code_2': 'qr', 'insights': 'tablero',
    'payments': 'cobros', 'receipt_long': 'factura', 'loyalty': 'medalla',
    'web': 'web', 'autorenew': 'renovar', 'palette': 'gota',
    'restaurant_menu': 'carta', 'security': 'escudo', 'shield': 'escudo',
    'phonelink_lock': 'candado', 'shield_lock': 'escudo',
    # industrias y causas
    'restaurant': 'plato', 'medical_services': 'salud', 'spa': 'hoja',
    'shopping_bag': 'bolsa', 'badge': 'credencial', 'factory': 'fabrica',
    'construction': 'escuadra', 'school': 'birrete', 'pets': 'huella',
    'directions_car': 'auto', 'recycling': 'hoja', 'volunteer_activism': 'plato',
    'sports_soccer': 'personas', 'add_circle': 'corazon', 'handshake': 'personas',
    'diversity_3': 'personas', 'volunteer': 'corazon',
    # chrome
    'apps': 'bloques', 'work': 'maletin', 'gavel': 'balanza',
    'language': 'idiomas', 'chat': 'chatbot', 'search': 'lupa',
    'search_off': 'lupa', 'cancel': 'equis-circulo', 'check_circle': 'check-circulo',
    'check': 'check', 'check_small': 'check', 'location_on': 'mapa',
    'download': 'descarga', 'mail': 'mail', 'menu': 'menu', 'close': 'cerrar',
    'arrow_forward': 'flecha', 'arrow_back': 'flecha', 'open_in_new': 'externo',
    'expand_more': 'flecha-abajo', 'add': 'flecha-abajo', 'tune': 'tablero',
    'calculate': 'calculadora', 'radio_button_unchecked': 'check-circulo',
}


def equivalente(viejo):
    """Nombre nuevo para un icono viejo de Material Symbols."""
    if viejo in ICONOS or viejo in MARCAS:
        return viejo
    if viejo not in EQUIV:
        sys.exit('iconos: no hay equivalente para %r. Agregalo a EQUIV.' % viejo)
    return EQUIV[viejo]

# Marcas de terceros: van tal cual, rellenas. Son logos registrados, no se
# redibujan con la grilla del sistema.
MARCAS = {
    'whatsapp': '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.872.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884a9.82 9.82 0 016.99 2.898 9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>',
    'telegram': '<path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.893-.663 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/>',
    'linkedin': '<path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM2.9 21h4.2V9.4H2.9V21zM9.5 9.4h4v1.6h.06c.56-1.06 1.93-2.18 3.97-2.18 4.25 0 5.03 2.8 5.03 6.43V21h-4.2v-5.05c0-1.2-.02-2.75-1.68-2.75-1.68 0-1.94 1.31-1.94 2.66V21H9.5V9.4z"/>',
}

INICIO = '<!-- iconos: los genera tools/iconos.py, no editar a mano -->'
FIN = '<!-- /iconos -->'


def sprite():
    """El sprite completo, listo para pegar apenas abre el <body>."""
    partes = [INICIO,
              '<svg xmlns="http://www.w3.org/2000/svg" style="display:none" aria-hidden="true">']
    for nombre, cuerpo in ICONOS.items():
        partes.append(
            '<symbol id="i-%s" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</symbol>'
            % (nombre, TRAZO, cuerpo))
    for nombre, cuerpo in MARCAS.items():
        partes.append(
            '<symbol id="i-%s" viewBox="0 0 24 24" fill="currentColor">%s</symbol>'
            % (nombre, cuerpo))
    partes.append('</svg>')
    partes.append(FIN)
    return '\n'.join(partes)


def ico(nombre, clase='ico'):
    """<svg class="ico"><use href="#i-nombre"></use></svg>"""
    if nombre not in ICONOS and nombre not in MARCAS:
        sys.exit('iconos: no existe %r' % nombre)
    return '<svg class="%s" aria-hidden="true"><use href="#i-%s"></use></svg>' % (clase, nombre)


def actualizar_index():
    ruta = os.path.join(RAIZ, 'index.html')
    h = io.open(ruta, encoding='utf-8').read()
    nuevo = sprite()
    if INICIO in h:
        h = re.sub(re.escape(INICIO) + r'.*?' + re.escape(FIN), lambda m: nuevo, h, flags=re.S)
    else:
        h = h.replace('<body>', '<body>\n' + nuevo, 1)
    io.open(ruta, 'w', encoding='utf-8', newline='').write(h)
    return ruta


if __name__ == '__main__':
    r = actualizar_index()
    print('%d iconos + %d marcas -> %s (%.1f KB de sprite)'
          % (len(ICONOS), len(MARCAS), os.path.relpath(r, RAIZ), len(sprite()) / 1024))
