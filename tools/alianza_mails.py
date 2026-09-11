# -*- coding: utf-8 -*-
"""
Arma el texto de cada mail de la propuesta de sociedad, y deja el PDF que va
adjunto en base64 listo para el conector de Gmail.

Texto plano a proposito: sin HTML, sin imagenes y sin pixel de seguimiento.
Un mail en frio con maquetado y tracking entra mucho mas facil a spam, y
ademas se lee peor. Aca importa que llegue y que parezca escrito a mano,
que es lo que es.

Uso:  python tools/alianza_mails.py                  lista los destinatarios
      python tools/alianza_mails.py --texto cielo    imprime un mail entero
      python tools/alianza_mails.py --b64 cielo      imprime el PDF en base64
"""
import base64
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

from alianza_pdf import archivo_de  # noqa: E402

RAIZ = os.path.dirname(AQUI)
CARPETA = os.path.join(RAIZ, 'salida-alianza')

# Agencia -> (mail, angulo en texto plano para el cuerpo del mensaje).
# Adviline y Buffalo no publican correo: van por LinkedIn, no por aca.
DESTINOS = [
    ('El Cielo Digital', 'elcielo@elcielo.digital',
     'tienen más de cien clientes PyME con el sitio hecho por ustedes sobre WordPress'),
    ('Point Web', 'proyectos@pointwebglobal.com',
     'con trescientos cincuenta clientes activos entre gastronomía, hoteles, salones y '
     'constructoras, la consulta de reserva por WhatsApp ya les debe estar llegando'),
    ('Pragmativa', 'hablemos@pragmativa.com',
     'trabajan B2B con industria, IT y servicios profesionales, y ese tipo de cliente ya '
     'compra software: el salto desde la generación de demanda es corto'),
    ('Zlatan Advertising', 'info@zlatanadvertising.com',
     'ya arman equipos por proyecto en vez de sostener plantel fijo, así que sumar un frente '
     'técnico tercerizado no les cambia la forma de trabajar'),
    ('Muffin', 'hola@muffin.com.ar',
     'son Google Premier Partner con más de cien PyMEs gestionadas, y el clic que hoy pagan '
     'por traer se pierde cuando llega al WhatsApp y nadie contesta'),
    ('Relevant', 'hola@relevantmkt.com',
     'manejan cuentas con presupuestos de hasta diez mil dólares por mes, y en ese rango un '
     'sistema de gestión a medida no es un gasto extra sino la próxima línea del contrato'),
    ('The Marketing Trip', 'hola@themarketingtrip.com',
     'trabajan viajes y consumo masivo, donde la consulta repetida por WhatsApp —precios, '
     'disponibilidad, horarios— es el cuello de botella de casi todos los clientes'),
    ('Agencia Deimon', 'consultas@estudiodmg.com.ar',
     'tienen veinticinco años de cartera en zona sur, y el comercio de barrio es justo el '
     'que pierde turnos por no contestar a tiempo'),
    ('Bianchi Desarrollo Web', 'info@bianchi.com.ar',
     'venden soporte humano directo como diferencial y trabajan con PyMEs, que es el cliente '
     'que pide facturación automática apenas empieza a facturar en serio'),
    ('BacchisWork', 'bacchiswork@gmail.com',
     'su cartera son contadores, clínicas, estudios jurídicos e inmobiliarias: literalmente '
     'los rubros que necesitan facturación AFIP y turnos automáticos'),
    ('WASD', 'info@wasd.com.ar',
     'son full service en estrategia, web, SEO, pauta y audiovisual, y lo técnico es el único '
     'pedido al que hoy hay que contestarle que no'),
    ('Multiclics', 'agencia@multiclics.com',
     'viven de Google y Meta Ads, y cuando el clic que el cliente pagó llega al WhatsApp y '
     'nadie contesta, el número que se mide es el de ustedes'),
    ('Cayo Agencia', 'info@cayoagency.com',
     'trabajan moda, donde el catálogo navegable con carrito y cobro por WhatsApp es el '
     'frente que rinde'),
    ('Cuarto Enfoque', 'info@cuartoenfoque.com',
     'son productora audiovisual y sus clientes suelen tener agencia digital aparte, así que '
     'lo que les propongo arranca por la vía más liviana de las dos'),
    ('DHNN Creative Network', 'info@dhnn.com',
     'tienen equipo propio de producto, así que esto no viene a reemplazar nada: es capacidad '
     'de desborde para cuando entran dos proyectos juntos'),
    ('Club de Marketing', 'info@e-clubdemarketing.com.ar',
     'vienen del B2B desde 1999, y antes de proponerles algo concreto prefiero confirmar '
     'qué están haciendo hoy del lado técnico para no ofrecerles algo que ya tengan'),
]

FIRMA = (
    'Emmanuel Pavón\n'
    'Zyntra — zyntraexperts.com\n'
    'zyntraconsultoraia@gmail.com · WhatsApp +54 9 11 6643-9309'
)


def asunto(nombre):
    return 'Propuesta para %s — ustedes facturan, yo desarrollo' % nombre


def cuerpo(nombre, angulo):
    return """Hola, buen día.

Soy Emmanuel Pavón, de Zyntra. Desarrollo chatbots de WhatsApp, sistemas de gestión, facturación AFIP y sitios web para PyMEs, acá en Buenos Aires.

Les escribo puntualmente por esto: %s.

Cuando uno de esos clientes pregunta si no se puede automatizar la atención o la facturación, la respuesta suele ser que no. Y el cliente lo busca afuera igual. El que se lo resuelve entra a la cuenta por la puerta técnica, y bastantes veces termina llevándose también la pauta.

Lo que les propongo es poder contestar que sí sin contratar a nadie. Hay dos formas, y eligen ustedes proyecto por proyecto:

1) Derivación. Pasan el contacto y se olvidan. Yo cierro y ejecuto con mi marca, y ustedes se llevan el 20%% del proyecto y el 20%% del abono mensual mientras el cliente siga activo.

2) Marca blanca. Facturan ustedes y ponen el precio que quieran. Yo ejecuto como parte de su equipo y no aparezco en ningún lado. La lista mayorista está un 35%% por debajo de mi precio de venta directa, así que el margen es de ustedes y ese 35%% es el piso, no el techo.

Tres cosas que van firmadas antes de empezar, porque son las que importan:

- No contacto ni le vendo a ningún cliente de ustedes, ni durante ni después.
- Si el cliente final no aprueba la entrega, no me pagan. El riesgo del desarrollo lo corro yo.
- Me pagan recién cuando el cliente les pagó a ustedes. Nunca ponen plata propia.

Adjunto el detalle en PDF: las dos vías, la lista de precios completa y las condiciones.

¿Tenés veinte minutos esta semana? En la llamada te muestro un chatbot funcionando y miramos juntos en qué cliente de ustedes entraría primero.

Gracias por leer hasta acá.

%s""" % (angulo, FIRMA)


def pdf_de(nombre):
    return os.path.join(CARPETA, archivo_de(nombre) + '.pdf')


def buscar(clave):
    for nombre, mail, angulo in DESTINOS:
        if clave.lower() in archivo_de(nombre):
            return nombre, mail, angulo
    sys.exit('alianza_mails: no hay ninguna agencia que coincida con "%s"' % clave)


def main():
    if len(sys.argv) > 2 and sys.argv[1] == '--texto':
        nombre, mail, angulo = buscar(sys.argv[2])
        print('PARA: %s' % mail)
        print('ASUNTO: %s' % asunto(nombre))
        print('ADJUNTO: %s' % os.path.basename(pdf_de(nombre)))
        print('-' * 70)
        print(cuerpo(nombre, angulo))
        return

    if len(sys.argv) > 2 and sys.argv[1] == '--b64':
        nombre, _, _ = buscar(sys.argv[2])
        ruta = pdf_de(nombre)
        if not os.path.exists(ruta):
            sys.exit('alianza_mails: falta %s, correr antes tools/alianza_pdf.py' % ruta)
        sys.stdout.write(base64.b64encode(open(ruta, 'rb').read()).decode())
        return

    faltan = [n for n, _, _ in DESTINOS if not os.path.exists(pdf_de(n))]
    for nombre, mail, _ in DESTINOS:
        print('%-24s %-34s %s' % (nombre, mail, os.path.basename(pdf_de(nombre))))
    print('\n%d destinatarios.' % len(DESTINOS))
    if faltan:
        print('FALTAN PDF: %s' % ', '.join(faltan))


if __name__ == '__main__':
    main()
