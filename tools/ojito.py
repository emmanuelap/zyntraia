# -*- coding: utf-8 -*-
"""
Ojito, la mascota. Un solo lugar donde se arma el markup.

EL PARPADO ES LA UNICA EXPRESION. No tiene boca, ni nariz, ni cejas, y no
se le agregan. Las cuatro posiciones salen del brandboard:

    abierto      0     sorprendido, buenas noticias
    normal      .16    acompanando, el estado por defecto
    sospechando .42    revisando algo, desconfiando, error
    durmiendo   .8     ironico: "dormi tranquilo, yo no duermo"

Reglas del brandboard que hay que respetar:
  - Un solo Ojito por seccion. Si hay dos a la vista, sobra uno.
  - Siempre mirando algo real de la composicion. En la web eso lo resuelve
    el JS: el iris sigue al cursor.
  - NO aparece en las piezas de pentesting. Ahi va el logotipo solo.

Uso:  from ojito import ojito
      ojito('sospechando', '120px')
"""

EXPRESIONES = {
    'abierto': '0',
    'normal': '.16',
    'sospechando': '.42',
    'durmiendo': '.8',
}

# Cosas que dice Ojito, tal cual estan en el brandboard. Si hace falta una
# leyenda nueva, escribirla con esa voz: frase corta, voseo, un solo chiste.
FRASES = {
    'turno': 'Ojito con el turno de las 15: nunca confirm&#243;.',
    'vi-todo': 'Vi todo. Tres cuotas vencidas y una puerta abierta.',
    'no-duermo': 'Dorm&#237; tranquilo. Yo no duermo.',
}

_MARCO = ('<div class="ojito"{atributos} style="--S:{tam};--lid:{lid}"{estilo}>'
          '<div class="ojito-cuerpo">'
          '<div class="ojito-iris"><div class="ojito-pupila"></div></div>'
          '<div class="ojito-brillo"></div>'
          '<div class="ojito-parpado"></div></div>'
          '<div class="ojito-patas"><span></span><span></span></div>'
          '</div>')


def ojito(expresion='normal', tam='120px', sigue_cursor=True, extra=''):
    if expresion not in EXPRESIONES:
        raise ValueError('ojito: expresion desconocida %r. Hay: %s'
                         % (expresion, ', '.join(EXPRESIONES)))
    return _MARCO.format(
        atributos=' data-ojito' if sigue_cursor else '',
        tam=tam, lid=EXPRESIONES[expresion],
        estilo=(' ' + extra) if extra else '')


def con_leyenda(expresion, tam, leyenda, alinear='center'):
    """Ojito con su frase debajo, en mono. Maximo una frase por seccion."""
    return ('<div class="ojito-bloque" style="text-align:%s">%s'
            '<p class="etiqueta etiqueta--chica ojito-frase">%s</p></div>'
            % (alinear, ojito(expresion, tam), leyenda))
