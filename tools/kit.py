# -*- coding: utf-8 -*-
"""
Genera kit/index.html: la pagina interna del sistema de diseno.

Es la referencia viva del rebrand: paleta, tipografia, botones, campos,
iconos, bloques, Ojito y patrones, todo renderizado con el CSS real del
sitio. Si algo se ve mal aca, esta mal en assets/zyntra.css.

Lleva noindex y no aparece en el menu ni en el sitemap: es para nosotros.

Uso:  python tools/kit.py
"""
import io
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, 'tools'))
import iconos  # noqa: E402

FUENTES = (
    '<link rel="preconnect" href="https://fonts.googleapis.com"/>\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800'
    '&amp;family=Instrument+Sans:wght@400;500;600&amp;family=JetBrains+Mono:wght@400;600&amp;display=swap" rel="stylesheet"/>'
)

OJITO = ('<div class="ojito"{attrs}><div class="ojito-cuerpo">'
         '<div class="ojito-iris"><div class="ojito-pupila"></div></div>'
         '<div class="ojito-brillo"></div><div class="ojito-parpado"></div></div>'
         '<div class="ojito-patas"><span></span><span></span></div></div>')


def caja(nombre):
    return ('<div style="text-align:center">'
            '<div class="caja-ico caja-ico--crema" style="margin:0 auto">%s</div>'
            '<div class="etiqueta etiqueta--chica" style="margin-top:8px">%s</div></div>'
            % (iconos.ico(nombre, 'ico ico--grande'), nombre))


def main():
    rejilla = '\n'.join(caja(n) for n in iconos.ICONOS)
    marcas = '\n'.join(caja(n) for n in iconos.MARCAS)

    ojitos = []
    for rotulo, lid in [('abierto', '0'), ('normal', '.16'),
                        ('sospechando', '.42'), ('durmiendo', '.8')]:
        ojitos.append(
            '<div style="text-align:center">%s'
            '<div class="etiqueta etiqueta--chica" style="margin-top:12px">%s</div></div>'
            % (OJITO.format(attrs=' style="--S:90px;--lid:%s"' % lid), rotulo))

    partes = []
    A = partes.append

    A('<!DOCTYPE html>')
    A('<html lang="es">')
    A('<head>')
    A('<meta charset="utf-8"/>')
    A('<meta name="viewport" content="width=device-width, initial-scale=1.0"/>')
    A('<meta name="robots" content="noindex, nofollow"/>')
    A('<title>Kit de diseño · Zyntra</title>')
    A(FUENTES)
    A('<link href="../assets/zyntra.css" rel="stylesheet"/>')
    A('</head>')
    A('<body>')
    A(iconos.sprite())
    A('<div class="envoltorio">')

    # portada
    A('<div class="panel panel--tinta panel--primero">')
    A('<div class="logo logo--crema" style="--fondo-pieza:var(--tinta);font-size:34px">'
      '<span class="isotipo"></span><span class="logotipo">zyntra</span></div>')
    A('<p class="etiqueta" style="margin-top:22px">Kit de diseño · página interna, no indexada</p>')
    A('<h1 class="display" style="color:var(--crema);margin-top:12px">Sistema de<br/>diseño</h1>')
    A('</div>')

    # paleta
    A('<div class="panel"><p class="etiqueta">Paleta</p>')
    A('<div class="rejilla rejilla--4" style="margin-top:20px">')
    for var, nom, borde in [('--tinta', 'tinta #171310', ''),
                            ('--acento', 'acento #E4572E', ''),
                            ('--acento2', 'acento2 #2F6B4F', ''),
                            ('--arena', 'arena #E3D8C4', ';border:1px solid var(--borde-3)'),
                            ('--crema', 'crema #F5F0E6', ';border:1px solid var(--borde-3)'),
                            ('--superficie-2', 'superficie #EDE6D8', ';border:1px solid var(--borde-3)')]:
        A('<div><div style="height:80px;border-radius:14px;background:var(%s)%s"></div>'
          '<div class="etiqueta etiqueta--chica" style="margin-top:8px">%s</div></div>' % (var, borde, nom))
    A('</div></div>')

    # tipografia
    A('<div class="panel"><p class="etiqueta">Tipografía</p>')
    A('<div style="margin-top:22px;display:flex;flex-direction:column;gap:18px">')
    A('<div class="display">Display · Bricolage 800</div>')
    A('<div class="h-seccion">Título de sección · Bricolage 800</div>')
    A('<div class="subtitulo">Subtítulo · Bricolage 600</div>')
    A('<p class="cuerpo">Cuerpo · Instrument Sans 400 a 17px. Tu cuaderno de turnos no escala. Nosotros sí.</p>')
    A('<p class="cuerpo-chico">Cuerpo chico · 15px, el mínimo legible del sistema.</p>')
    A('<div class="etiqueta">Etiqueta · JetBrains Mono 600</div>')
    A('<div class="dato">$4.680.000</div>')
    A('</div></div>')

    # botones
    A('<div class="panel"><p class="etiqueta">Botones</p>')
    A('<div class="fila-botones" style="margin-top:20px">')
    A('<a class="btn btn--primario" href="#">Pedir diagnóstico gratis</a>')
    A('<a class="btn btn--secundario" href="#">Ver el servicio</a>')
    A('<a class="btn btn--contorno" href="#">Escribinos</a>')
    A('<a class="btn btn--enlace" href="#">Leé la propuesta →</a>')
    A('<button class="btn" disabled>Enviando…</button>')
    A('</div>')
    A('<div class="tarjeta tarjeta--tinta sobre-tinta" style="margin-top:20px"><div class="fila-botones">')
    A('<a class="btn btn--primario" href="#">Quiero esto en mi negocio</a>')
    A('<a class="btn btn--contorno" href="#">Ver casos reales</a>')
    A('<span class="etiqueta etiqueta--chica" style="margin-left:auto">Sobre fondo tinta</span>')
    A('</div></div></div>')

    # campos
    A('<div class="panel"><p class="etiqueta">Campos y etiquetas</p>')
    A('<div class="rejilla rejilla--2" style="margin-top:20px">')
    A('<div class="campo"><label for="k1">Campo de texto</label><input id="k1" placeholder="Nombre completo"/></div>')
    A('<div class="campo"><label for="k2">Con valor</label><input id="k2" value="emmanuel@zyntra.com.ar"/></div>')
    A('<div class="campo"><label for="k3">Selector</label><select id="k3">'
      '<option>Turnos online</option><option>Chatbot de WhatsApp</option></select></div>')
    A('<div><div class="etiqueta etiqueta--chica" style="margin-bottom:10px">Etiquetas</div><div class="fila-chips">'
      '<span class="chip">En producción</span><span class="chip chip--verde">AFIP real</span>'
      '<span class="chip chip--naranja">Nuevo</span><span class="chip chip--contorno">React</span></div></div>')
    A('</div></div>')

    # iconos
    A('<div class="panel"><p class="etiqueta">Iconografía · %d propios</p>' % len(iconos.ICONOS))
    A('<div style="margin-top:22px;display:grid;grid-template-columns:repeat(auto-fill,minmax(96px,1fr));gap:18px">')
    A(rejilla)
    A('</div><hr class="divisor" style="margin:26px 0"/>')
    A('<p class="etiqueta etiqueta--chica">Marcas de terceros (rellenas, no se redibujan)</p>')
    A('<div style="margin-top:16px;display:grid;grid-template-columns:repeat(auto-fill,minmax(96px,1fr));gap:18px">')
    A(marcas)
    A('</div></div>')

    # bloques
    A('<div class="panel"><p class="etiqueta">Bloques</p><div class="rejilla" style="margin-top:20px">')
    A('<div class="tarjeta">')
    A('<div class="caja-ico">%s</div>' % iconos.ico('turnos'))
    A('<div><h3>Turnos y reservas online</h3><p>Tus clientes reservan solos, las 24 horas, '
      'sin depender de que alguien conteste.</p></div>')
    A('<div class="con-sin">'
      '<div><span class="punto punto--verde"></span><span><strong>Con esto:</strong> menos ausencias, '
      'agenda que se llena sola de noche.</span></div>'
      '<div><span class="punto"></span><span><strong>Sin esto:</strong> reservas perdidas por '
      'línea ocupada.</span></div></div>')
    A('<a class="btn btn--enlace" href="#">Quiero esto en mi negocio →</a>')
    A('</div>')

    A('<div class="tarjeta-caso">')
    A('<div class="cabecera"><span class="etiqueta etiqueta--chica">Caso · Fitness</span>'
      '<span class="chip chip--verde">En producción</span></div>')
    A('<div class="hueco" style="min-height:120px"><span>captura del dashboard</span></div>')
    A('<div><h3>Stratos Admin</h3><p>Socios, reservas con QR y facturación AFIP en una sola plataforma.</p></div>')
    A('<div class="metricas"><div><div class="cifra">72</div><div class="rotulo">Gimnasios</div></div>'
      '<div><div class="cifra">CAE</div><div class="rotulo">AFIP real</div></div></div>')
    A('</div>')

    A('<div class="bloque-cta"><div class="fila">')
    A('<h3>Veinte minutos y te decimos qué automatizar primero.</h3>')
    A(OJITO.format(attrs=' style="--S:54px" data-ojito'))
    A('</div><div><a class="btn btn--secundario" href="#">Pedir el diagnóstico</a>'
      '<div class="nota">Gratis · el informe te queda igual</div></div></div>')
    A('</div></div>')

    # ojito
    A('<div class="panel"><p class="etiqueta">Ojito · el párpado es la única expresión</p>')
    A('<div style="margin-top:26px;display:flex;gap:34px;flex-wrap:wrap;align-items:flex-end">')
    A('\n'.join(ojitos))
    A('</div></div>')

    # patrones
    A('<div class="panel"><p class="etiqueta">Patrones</p><div class="rejilla rejilla--4" style="margin-top:20px">')
    A('<div class="patron-puntos" style="height:120px;border-radius:14px"></div>')
    A('<div class="patron-diagonal" style="height:120px;border-radius:14px"></div>')
    A('<div class="patron-lunares" style="height:120px;border-radius:14px"></div>')
    A('<div class="hueco" style="min-height:120px"><span>local real, luz de día</span></div>')
    A('</div></div>')

    A('<div style="height:64px"></div>')
    A('</div>')
    A('<script defer src="../assets/zyntra.js"></script>')
    A('</body>')
    A('</html>')

    salida = '\n'.join(partes)
    destino = os.path.join(RAIZ, 'kit', 'index.html')
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    io.open(destino, 'w', encoding='utf-8', newline='').write(salida)
    print('kit/index.html  %.1f KB' % (len(salida) / 1024))


if __name__ == '__main__':
    main()
