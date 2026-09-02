# -*- coding: utf-8 -*-
"""Pagina de servicio: menus digitales con QR."""

PAGINA = {
    'slug': 'menus-digitales-qr',
    'migas': 'Menús digitales QR',
    'icono': 'restaurant_menu',

    'titulo': 'Menú digital con QR para restaurantes y bares | Zyntra',
    'descripcion': ('Menú digital con código QR para restaurantes, bares y cafeterías: cambiás precios en '
                    'segundos, con fotos y disponibilidad al día. Sin volver a imprimir.'),

    'h1': 'Menú digital con QR para tu local',
    'bajada': ('El cliente escanea y ve la carta actualizada al instante, con fotos y precios de hoy. '
               'Cambiás un precio en segundos y ya está en todas las mesas.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20un%20men%C3%BA%20digital%20con%20QR%20para%20mi%20local.',

    'servicio': {
        'nombre': 'Menú digital con código QR',
        'tipo': 'Desarrollo de menús digitales para gastronomía',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'La carta impresa nace desactualizada',
            'parrafos': [
                'El problema de la carta de papel no es que sea fea. Es que el día que aumenta un '
                'proveedor tenés dos opciones malas: cobrar distinto a lo que dice la carta, o mandar a '
                'imprimir de nuevo.',
                'La primera genera el reclamo en la mesa, que es la peor forma de arrancar una cuenta. La '
                'segunda es un gasto que vuelve cada dos o tres meses, y que además tarda: entre que '
                'mandás el archivo y te llegan las cartas pasa una semana en la que seguís con las '
                'viejas.',
                'Y está el plato que se terminó a las nueve de la noche. En papel no hay forma de decirlo '
                'salvo que el mozo lo repita en cada mesa.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Qué resuelve',
            'items': [
                {'icono': 'payments', 'titulo': 'Precios al día',
                 'texto': 'Cambiás uno desde el celular y queda actualizado en todas las mesas al '
                          'instante. Sin imprenta y sin espera.'},
                {'icono': 'cancel', 'titulo': 'Sin stock, sin problema',
                 'texto': 'Marcás el plato como no disponible y deja de mostrarse. El cliente no pide algo '
                          'que no hay.'},
                {'icono': 'restaurant', 'titulo': 'Fotos que venden',
                 'texto': 'La foto sube el ticket promedio más que cualquier descripción. En papel no '
                          'entran; acá sí.'},
                {'icono': 'apps', 'titulo': 'Cartas por momento',
                 'texto': 'Desayuno, almuerzo, happy hour y cena, cada una mostrándose sola en su horario.'},
                {'icono': 'language', 'titulo': 'Varios idiomas',
                 'texto': 'Si recibís turistas, la misma carta en otro idioma sin imprimir una segunda '
                          'versión.'},
                {'icono': 'analytics', 'titulo': 'Qué mira la gente',
                 'texto': 'Qué secciones se abren más y qué platos se miran y no se piden. Es información '
                          'que la carta de papel nunca te dio.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo se pone en marcha',
            'pasos': [
                {'titulo': 'Cargamos tu carta',
                 'texto': 'Nos pasás la que tenés, en el formato que sea, y la cargamos nosotros. No te '
                          'dejamos con una planilla vacía y suerte.'},
                {'titulo': 'Diseño con tu marca',
                 'texto': 'La carta se ve como tu local, no como una plantilla genérica con tu logo '
                          'arriba.'},
                {'titulo': 'QR para las mesas',
                 'texto': 'Diseñamos el soporte: adhesivo, cartelito de mesa o el QR impreso en la carta '
                          'física si querés tener las dos.'},
                {'titulo': 'Vos la editás',
                 'texto': 'Precios, platos, fotos y disponibilidad los cambiás vos desde el celular. Si '
                          'depende de mandarnos un mensaje, en dos meses está desactualizada.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Un aviso honesto sobre el QR',
            'parrafos': [
                'El menú digital no le gusta a todo el mundo. Hay clientes, sobre todo de más edad, que '
                'prefieren el papel, y hay locales donde la señal adentro es mala y el QR termina siendo '
                'una molestia.',
                'Por eso lo que mejor funciona casi nunca es reemplazar: es convivir. Unas pocas cartas '
                'impresas para quien las pida y el QR para el resto. Vos seguís cambiando precios sin '
                'reimprimir, porque las cartas de papel que quedan son pocas y las cambiás cuando toca.',
                'Si alguien te dice que el QR reemplaza el papel siempre y en todos los casos, no estuvo '
                'nunca un sábado a la noche en un salón lleno.',
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre menús digitales',
            'preguntas': [
                {'q': '¿El cliente tiene que instalar algo?',
                 'a': 'No. Apunta la cámara del celular al QR y se le abre la carta en el navegador, como '
                      'una página web cualquiera. Cualquier teléfono de los últimos años lo hace desde la '
                      'cámara, sin aplicación aparte.'},
                {'q': '¿Puedo cambiar los precios yo mismo?',
                 'a': 'Sí, y es lo más importante de todo. Una carta digital donde cada cambio depende de '
                      'escribirle a alguien es peor que la de papel, porque encima da la sensación de estar '
                      'al día cuando no lo está. Los precios, las fotos y la disponibilidad los manejás vos '
                      'desde el celular.'},
                {'q': '¿Sirve para tomar pedidos también?',
                 'a': 'Se puede sumar, pero conviene pensarlo. El pedido desde la mesa funciona muy bien '
                      'en locales de alto volumen y rotación rápida, y funciona bastante mal donde la '
                      'atención del mozo es parte de lo que la gente viene a buscar. Arrancá por la carta, '
                      'medí, y después decidís.'},
                {'q': '¿Qué pasa si se cae internet?',
                 'a': 'La carta no se ve, así de simple. Por eso siempre recomendamos tener algunas '
                      'impresas de respaldo, y por eso el QR conviene que apunte a algo liviano que cargue '
                      'rápido incluso con mala señal. Una carta digital de diez megabytes en fotos es '
                      'inservible en un sótano.'},
                {'q': '¿Me sirve si tengo un local chico?',
                 'a': 'Si tu carta casi no cambia, quizás no lo necesitás. Si cambiás precios seguido, si '
                      'tenés platos del día o si se te terminan cosas a mitad del servicio, ahí rinde '
                      'enseguida y el ahorro de imprenta solo ya lo justifica.'},
            ],
            'mas': [
                ('como-hago-un-menu-digital-con-qr-para-mi-restaurante',
                 '¿Cómo hago un menú digital con QR para mi restaurante?'),
                ('como-cambio-los-precios-de-mi-web-sin-depender-de-nadie',
                 '¿Cómo cambio los precios de mi web sin depender de nadie?'),
                ('como-hago-para-que-mi-web-se-vea-bien-en-el-celular',
                 '¿Cómo hago para que mi web se vea bien en el celular?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero mi menú digital',
        'titulo': 'Pasanos tu carta actual',
        'texto': ('La cargamos nosotros y te mostramos cómo queda antes de que decidas nada. El '
                  'diagnóstico queda para vos aunque no contrates.'),
    },
}
