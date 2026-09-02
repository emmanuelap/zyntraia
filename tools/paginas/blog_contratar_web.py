# -*- coding: utf-8 -*-
"""Nota: que preguntarle a quien te hace la pagina web."""

PAGINA = {
    'slug': 'blog/que-preguntar-antes-de-contratar-una-web',
    'padre': {'slug': 'blog', 'nombre': 'Blog'},
    'migas': 'Antes de contratar una web',
    'icono': 'gavel',
    'articulo': {'fecha': '2026-09-02'},

    'titulo': 'Seis preguntas antes de contratar una página web | Zyntra',
    'descripcion': ('Qué preguntarle a quien te va a hacer la web para no quedar atrapado: a nombre de '
                    'quién queda el dominio, quién puede editarla y qué te llevás si te vas.'),

    'h1': 'Seis preguntas antes de contratar una página web',
    'bajada': ('Ninguna es sobre diseño. Son las que determinan si dentro de dos años la web es tuya o '
               'seguís dependiendo de alguien.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20consultar%20por%20una%20p%C3%A1gina%20web.',

    'servicio': {'nombre': 'Desarrollo web', 'tipo': 'Desarrollo de sitios web'},

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'El problema no aparece al principio',
            'parrafos': [
                'Cuando contratás una web mirás el diseño, el precio y el plazo. Es razonable: es lo que '
                'se ve.',
                'Los problemas reales aparecen dos años después, y siempre son los mismos. Querés cambiar '
                'un precio y no podés. Te peleás con quien te la hizo y descubrís que el dominio está a '
                'nombre de él. Querés cambiar de proveedor y no hay forma de llevarse nada.',
                'Estas seis preguntas se hacen en cinco minutos y evitan todo eso.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Las seis',
            'items': [
                {'icono': 'gavel', 'titulo': '¿A nombre de quién queda el dominio?',
                 'texto': 'Tiene que quedar al tuyo, registrado con tu cuenta. Es la más importante de '
                          'todas: el dominio es la dirección de tu negocio y todo lo que Google acumula '
                          'queda pegado a ella.'},
                {'icono': 'autorenew', 'titulo': '¿Qué puedo cambiar yo?',
                 'texto': 'Precios, fotos, horarios y productos tienen que ser editables por vos. Si cada '
                          'cambio depende de mandar un mensaje, en tres meses está desactualizada.'},
                {'icono': 'download', 'titulo': '¿Qué me llevo si me voy?',
                 'texto': 'El sitio, los accesos y los contenidos. Si la respuesta es que no te llevás '
                          'nada, ahí tenés la respuesta a todo lo demás.'},
                {'icono': 'language', 'titulo': '¿Queda conectada a Google?',
                 'texto': 'Sitemap enviado, Search Console configurada, ficha de Maps vinculada. Es el '
                          'paso que más se saltea y sin él la web no la encuentra nadie.'},
                {'icono': 'phonelink_lock', 'titulo': '¿Cómo se ve en el celular?',
                 'texto': 'Pedí ver un trabajo anterior desde tu teléfono, no en la computadora del que '
                          'te la vende. La mayoría de tus visitas van a entrar desde ahí.'},
                {'icono': 'security', 'titulo': '¿Tiene certificado de seguridad?',
                 'texto': 'Sin él el navegador avisa "no segura" antes de que la persona vea nada. Hoy es '
                          'gratis, así que no hay excusa para que falte.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'La del dominio merece un párrafo aparte',
            'parrafos': [
                'Es la que más problemas causa y la que casi nadie pregunta. El dominio se registra a '
                'nombre de alguien, con una cuenta y una tarjeta, y quien figura ahí es el dueño real.',
                'Si figura tu proveedor, el día que se termina la relación tenés dos opciones: negociar '
                'para que te lo transfiera, o empezar de cero con otra dirección. Empezar de cero '
                'significa perder toda la antigüedad y toda la posición que Google le había dado.',
                'La forma de evitarlo es simple: registrás vos el dominio, con tu cuenta y tu tarjeta, y '
                'le das acceso al que te hace la web. Cuesta lo mismo y el control queda de tu lado.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Dos respuestas que son señal de alarma',
            'parrafos': [
                '<strong class="text-on-surface">"Te la posiciono primero en Google."</strong> Nadie puede '
                'garantizar eso. Se puede trabajar para mejorar la posición, y lleva meses. El que te '
                'promete el primer puesto en dos semanas te está mintiendo o va a usar métodos que '
                'después te penalizan.',
                '<strong class="text-on-surface">Un precio cerrado sin preguntarte nada.</strong> Una web '
                'de una página informativa y una con turnos, cobros y catálogo no cuestan lo mismo ni de '
                'cerca. Quien te cotiza sin preguntar qué tiene que lograr el sitio, está cotizando otra '
                'cosa.',
                'Si querés ver cómo respondemos nosotros estas seis, están contestadas en '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@desarrollo-web/">'
                'la página de desarrollo web</a>.',
            ],
        },
    ],

    'cta': {
        'boton': 'Consultar por una web',
        'titulo': 'Hacenos estas seis preguntas a nosotros',
        'texto': 'Están contestadas arriba, pero si querés te las respondemos en persona y sin compromiso.',
    },
}
