# -*- coding: utf-8 -*-
"""
Propuesta de sociedad para agencias de marketing, una por agencia.

No son documentos del sitio: se mandan por mail. Por eso salen a
`salida-alianza/` y no a `docs/`, que es lo que se publica.

Cada PDF lleva el nombre de la agencia en la portada y un parrafo propio
—el "angulo"— que dice por que le escribimos a ella y no a cualquiera.
El resto del documento es igual para todas: las dos vias, los precios y
las condiciones.

Uso:  python tools/alianza_pdf.py
      python tools/alianza_pdf.py elcielo      solo esa
"""
import os
import re
import sys
import unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import pdf_marca  # noqa: E402

CARPETA = 'salida-alianza'

# (nombre, angulo). El angulo es lo unico que cambia entre documentos y es
# lo que justifica el mail: sin eso, es una propuesta generica.
AGENCIAS = [
    ('El Cielo Digital',
     'Tienen m&aacute;s de cien clientes PyME con el sitio hecho por ustedes, sobre WordPress. '
     'El chatbot y la facturaci&oacute;n autom&aacute;tica se montan encima de eso sin tocar '
     'nada de lo que ya funciona, y lo factura la agencia.'),
    ('Point Web',
     'Con trescientos cincuenta clientes activos entre gastronom&iacute;a, hoteles, salones y '
     'constructoras, la consulta de reserva por WhatsApp ya debe estar llegando. Es exactamente '
     'el caso para el que est&aacute; hecho el chatbot.'),
    ('Pragmativa',
     'Trabajan B2B con industria, IT y servicios profesionales. Esos clientes ya compran software: '
     'el salto de la generaci&oacute;n de demanda a un sistema de gesti&oacute;n o a la '
     'facturaci&oacute;n electr&oacute;nica es mucho m&aacute;s corto que en una cuenta de consumo.'),
    ('Zlatan Advertising',
     'Ya arman equipos por proyecto en vez de sostener plantel fijo. Sumar un frente t&eacute;cnico '
     'tercerizado no les cambia la forma de trabajar: es la forma en que trabajan.'),
    ('Muffin',
     'Son Google Premier Partner con m&aacute;s de cien PyMEs gestionadas. El frente de rese&ntilde;as '
     'de Google encaja justo arriba de lo que ya les venden, y el chatbot atiende el clic que hoy '
     'pagan por traer y despu&eacute;s se pierde sin respuesta.'),
    ('Relevant',
     'Manejan cuentas con presupuestos de hasta diez mil d&oacute;lares por mes. En ese rango un '
     'sistema de gesti&oacute;n a medida no es un gasto extra: es la pr&oacute;xima l&iacute;nea del '
     'contrato, con margen propio.'),
    ('Adviline',
     'Ya ofrecen desarrollos personalizados sin tener equipo de desarrollo propio. Es el hueco m&aacute;s '
     'directo de toda la lista: pueden seguir vendiendo lo mismo, con alguien atr&aacute;s que lo ejecute.'),
    ('The Marketing Trip',
     'Trabajan viajes y consumo masivo, donde la consulta repetida por WhatsApp —precios, '
     'disponibilidad, horarios— es el cuello de botella de casi todos los clientes.'),
    ('Agencia Deimon',
     'Veinticinco a&ntilde;os de cartera en zona sur. Son comercios y servicios de barrio, que es '
     'justo el negocio que pierde turnos por no contestar a tiempo y que no tiene con qui&eacute;n '
     'resolverlo.'),
    ('Bianchi Desarrollo Web',
     'Venden soporte humano directo como diferencial, y trabajan con PyMEs. La facturaci&oacute;n '
     'AFIP automatizada es lo primero que ese cliente pide apenas empieza a facturar en serio.'),
    ('BacchisWork',
     'Su cartera son contadores, cl&iacute;nicas, estudios jur&iacute;dicos e inmobiliarias: '
     'literalmente los rubros que necesitan facturaci&oacute;n AFIP y turnos autom&aacute;ticos. '
     'El encaje es directo.'),
    ('WASD',
     'Son full service en estrategia, web, SEO, pauta y audiovisual. Lo t&eacute;cnico es el '
     '&uacute;nico pedido al que hoy hay que contestarle que no.'),
    ('Multiclics',
     'Viven de Google y Meta Ads. Cuando el clic que el cliente pag&oacute; llega al WhatsApp y '
     'nadie contesta, la campa&ntilde;a se pierde ah&iacute;, y el n&uacute;mero que se mide es el de ustedes.'),
    ('Cayo Agencia',
     'En moda, el cat&aacute;logo navegable con carrito y cobro por WhatsApp es el frente que rinde. '
     'Es el que proponemos empezar; el resto del paquete encaja menos en el rubro y lo decimos de entrada.'),
    ('Cuarto Enfoque',
     'Son productora audiovisual, no agencia de performance: sus clientes suelen tener agencia '
     'digital aparte. Por eso la propuesta arranca por la v&iacute;a de derivaci&oacute;n, que no '
     'les cambia nada de c&oacute;mo trabajan.'),
    ('DHNN Creative Network',
     'Tienen equipo propio de producto, as&iacute; que esto no es para reemplazar nada: es '
     'capacidad de desborde para cuando entran dos proyectos juntos y uno hay que sostenerlo igual.'),
    ('Club de Marketing',
     'Vienen del B2B desde 1999. Antes de proponer nada concreto preferimos confirmar en una charla '
     'qu&eacute; est&aacute;n haciendo hoy del lado t&eacute;cnico, para no ofrecerles algo que ya tengan.'),
    ('Buffalo',
     'Trabajan marcas con presencia digital armada, donde el pr&oacute;ximo paso suele ser '
     'automatizar la atenci&oacute;n antes que sumar m&aacute;s pauta.'),
]

SUB = ('C&oacute;mo funcionar&iacute;a la sociedad: las dos formas de trabajar, los precios '
       'mayoristas y las condiciones, escritas antes de empezar.')

ARGUMENTO = (
    'Una agencia como la suya cobra un abono mensual por pauta, redes y contenido. Cuando el '
    'cliente pregunta si no se puede automatizar la atenci&oacute;n por WhatsApp, emitir las '
    'facturas solo o tener un sistema propio, hoy la respuesta suele ser que no.')

ARGUMENTO_2 = (
    'Ese cliente lo busca afuera y lo encuentra. El que se lo resuelve entra a la cuenta por la '
    'puerta t&eacute;cnica, se queda con la relaci&oacute;n operativa, y en bastantes casos '
    'termina llev&aacute;ndose tambi&eacute;n la pauta. <b>Esta propuesta no es para agregarles '
    'un servicio: es para que no tengan que decir que no.</b>')

FRENTES = [
    ('Chatbot de WhatsApp', 'Atiende, responde precios y horarios, toma turnos, cobra con Mercado '
     'Pago y hace seguimiento. Sobre la API oficial de WhatsApp, no sobre el celular de nadie.'),
    ('Sistemas de gesti&oacute;n', 'Software a medida para administrar el negocio: clientes, '
     'turnos, stock, cobros y reportes. Web, con acceso desde cualquier dispositivo.'),
    ('Facturaci&oacute;n AFIP', 'Emisi&oacute;n electr&oacute;nica integrada al sistema del '
     'cliente, con certificados propios y CAE autom&aacute;tico.'),
    ('Rese&ntilde;as de Google', 'Trabajo sostenido sobre el perfil de empresa para subir '
     'cantidad y promedio de rese&ntilde;as, que es lo que mueve el mapa.'),
    ('Sitios web', 'Desde una p&aacute;gina de presencia hasta un cat&aacute;logo '
     'autoadministrable con carrito.'),
]

VIA1 = [
    'La agencia pasa el contacto y no hace nada m&aacute;s.',
    'Zyntra cotiza, cierra y ejecuta con su propia marca.',
    '<b>20% del proyecto y 20% del abono mensual</b>, mientras el cliente siga activo.',
    'La agencia no factura, no coordina y no responde consultas t&eacute;cnicas.',
    'La comisi&oacute;n se liquida cuando el cliente paga.',
]

VIA2 = [
    'La agencia factura al cliente y define su propio precio de venta.',
    'Zyntra cobra el precio mayorista de la tabla y no aparece en ning&uacute;n lado.',
    'El margen de la tabla es el <b>piso</b>, no el techo: si la agencia cobra m&aacute;s, la '
    'diferencia es suya.',
    'Zyntra participa de las reuniones t&eacute;cnicas presentado como parte del equipo de la '
    'agencia, con su casilla de correo si hace falta.',
    'Toda la documentaci&oacute;n que ve el cliente sale con la marca de la agencia.',
]

PRECIOS = [
    ['Chatbot WhatsApp &middot; Esencial', 'USD 400', '<b>USD 260</b>', 'USD 140 &middot; 35%'],
    ['Chatbot WhatsApp &middot; Profesional', 'USD 700', '<b>USD 450</b>', 'USD 250 &middot; 36%'],
    ['Chatbot WhatsApp &middot; Completo', 'USD 1.000', '<b>USD 650</b>', 'USD 350 &middot; 35%'],
    ['Mantenimiento del chatbot', 'USD 50 / mes', '<b>USD 30 / mes</b>', 'USD 20 &middot; por mes'],
    ['Sitio web &middot; Presencia', 'USD 500', '<b>USD 325</b>', 'USD 175 &middot; 35%'],
    ['Sitio web &middot; Cat&aacute;logo', 'USD 850', '<b>USD 550</b>', 'USD 300 &middot; 35%'],
    ['Sitio web &middot; Sistema', 'USD 1.200', '<b>USD 780</b>', 'USD 420 &middot; 35%'],
    ['Mantenimiento del sitio', 'USD 60 / mes', '<b>USD 38 / mes</b>', 'USD 22 &middot; por mes'],
    ['Gesti&oacute;n, AFIP, rese&ntilde;as y seguridad', 'a cotizar',
     '<b>&minus;35%</b>', 'mismo criterio'],
]

CONDICIONES = [
    ('No competencia',
     'Zyntra no contacta, no cotiza y no le vende a ning&uacute;n cliente de la agencia, ni '
     'durante la sociedad ni despu&eacute;s de terminarla. Se firma antes del primer proyecto.'),
    ('El riesgo del desarrollo lo corre Zyntra',
     'Si el cliente final no aprueba la entrega, la agencia no paga. Se rehace hasta que apruebe '
     'o no se factura. La agencia no queda nunca en el medio.'),
    ('Se paga despu&eacute;s de cobrar',
     'La agencia le paga a Zyntra reci&eacute;n cuando el cliente le pag&oacute; a ella. En '
     'ning&uacute;n momento pone dinero propio.'),
    ('Zyntra va a las reuniones como parte del equipo',
     'Con la marca, el discurso y el correo de la agencia. Ellos manejan la relaci&oacute;n '
     'comercial; nosotros respondemos lo t&eacute;cnico. El material de venta va armado.'),
    ('Exclusividad para el que arranca',
     'La agencia que cierre los primeros tres proyectos se queda con la exclusividad de su zona '
     'o de su rubro por doce meses.'),
]

PASOS = [
    ('01', 'Una llamada de veinte minutos',
     'Sin presentaci&oacute;n ni PowerPoint: se mira la cartera de la agencia y se marca en '
     'qu&eacute; clientes esto entra primero.'),
    ('02', 'Se firma el acuerdo',
     'No competencia, confidencialidad, precios y forma de pago. Dos p&aacute;ginas, antes de '
     'tocar nada.'),
    ('03', 'Un primer proyecto',
     'Se elige un cliente concreto y se ejecuta. Zyntra cobra contra aprobaci&oacute;n de la '
     'entrega, as&iacute; que la agencia no arriesga la cuenta.'),
    ('04', 'Se repite o no',
     'Si funcion&oacute;, se arma el circuito para el resto de la cartera. Si no, no hay '
     'permanencia ni nada que cancelar.'),
]


def archivo_de(nombre):
    base = unicodedata.normalize('NFKD', nombre).encode('ascii', 'ignore').decode()
    base = re.sub(r'[^a-z0-9]+', '-', base.lower()).strip('-')
    return 'zyntra-sociedad-' + base


def construir(nombre, angulo):
    d = pdf_marca.Documento(
        archivo_de(nombre),
        'Trabajemos juntos',
        SUB,
        rotulo='PROPUESTA DE SOCIEDAD PARA ' + nombre.upper(),
        # OJO: el pie y las cabeceras de tabla pasan por .upper() y por
        # drawString, que NO parsean entidades: van con acentos literales.
        pie='Propuesta de sociedad · ' + nombre,
        carpeta=CARPETA)
    d.portada()

    d.seccion('01', 'Por qu&eacute; les escribimos a ustedes', angulo)
    d.parrafo(ARGUMENTO)
    d.parrafo(ARGUMENTO_2)

    d.seccion('02', 'Qu&eacute; hace Zyntra',
              'Desarrollo para PyMEs, desde Buenos Aires. Estos son los cinco frentes que la '
              'agencia podr&iacute;a ofrecer sin contratar a nadie.')
    for titulo, texto in FRENTES:
        d.titulo3(titulo)
        d.parrafo(texto)
        d.espacio(2)

    d.salto()

    d.seccion('03', 'V&iacute;a 1 &middot; Derivaci&oacute;n',
              'La forma m&aacute;s liviana de empezar. Sirve para probar sin comprometer nada.')
    d.vinetas(VIA1)
    d.importante(
        'La agencia no asume ninguna responsabilidad t&eacute;cnica ni comercial. Solo presenta '
        'y cobra una comisi&oacute;n mientras el cliente siga activo.',
        'EN UNA L&Iacute;NEA')

    d.seccion('04', 'V&iacute;a 2 &middot; Marca blanca',
              'La agencia suma el servicio a su propuesta como si fuera suyo. Zyntra ejecuta '
              'por detr&aacute;s y no existe para el cliente.')
    d.vinetas(VIA2)

    d.salto()

    d.titulo3('Lista mayorista')
    d.parrafo(
        'La columna <b>Precio Zyntra</b> es la lista vigente de venta directa. La columna '
        '<b>Precio agencia</b> es lo que Zyntra factura en marca blanca. Lo que la agencia le '
        'cobre al cliente lo decide la agencia.', 'chico')
    d.tabla(['Servicio', 'Precio Zyntra', 'Precio agencia', 'Margen mínimo'],
            PRECIOS, anchos=[40, 19, 19, 22])
    d.parrafo(
        'Precios en d&oacute;lares estadounidenses. Los abonos mensuales son opcionales y '
        'tambi&eacute;n dejan margen recurrente. Las piezas a cotizar —sistemas de gesti&oacute;n, '
        'facturaci&oacute;n AFIP, rese&ntilde;as y evaluaciones de seguridad— siguen el mismo '
        'criterio: treinta y cinco por ciento debajo de la venta directa.', 'chico')

    d.seccion('05', 'Las condiciones, por escrito',
              'Ninguna sociedad de este tipo se cae por el margen. Se cae por estas cinco cosas, '
              'as&iacute; que est&aacute;n resueltas de entrada.')
    for titulo, texto in CONDICIONES:
        d.titulo3(titulo)
        d.parrafo(texto)
        d.espacio(2)

    d.seccion('06', 'C&oacute;mo empieza')
    for num, titulo, texto in PASOS:
        d.titulo3('<font color="#B93A15">%s</font>&nbsp;&nbsp;%s' % (num, titulo))
        d.parrafo(texto)
        d.espacio(2)

    d.importante(
        'No hay exclusividad obligatoria, ni permanencia, ni m&iacute;nimo de proyectos. La '
        'agencia puede usar la v&iacute;a 1 con un cliente y la v&iacute;a 2 con el siguiente.')

    d.cierre(
        'Veinte minutos y lo vemos',
        'Si te interesa, respondeme este correo con dos horarios que te sirvan y coordinamos. '
        'En la llamada te muestro un chatbot funcionando y miramos juntos en qu&eacute; cliente '
        'de ustedes entrar&iacute;a primero.')
    return d.guardar()


def main():
    filtro = sys.argv[1].lower() if len(sys.argv) > 1 else None
    pendientes = AGENCIAS
    if filtro:
        pendientes = [a for a in AGENCIAS if filtro in archivo_de(a[0])]
    if not pendientes:
        sys.exit('alianza_pdf: no hay nada que generar con ese filtro')

    for nombre, angulo in pendientes:
        archivo, paginas, kb = construir(nombre, angulo)
        print('  %-44s %2d paginas  %6.1f KB' % (archivo, paginas, kb))
    print('\n%d PDF en %s/' % (len(pendientes), CARPETA))


if __name__ == '__main__':
    main()
