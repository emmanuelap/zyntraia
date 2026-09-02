# -*- coding: utf-8 -*-
"""Nota: WhatsApp Business vs WhatsApp Cloud API."""

PAGINA = {
    'slug': 'blog/whatsapp-business-vs-cloud-api',
    'padre': {'slug': 'blog', 'nombre': 'Blog'},
    'migas': 'WhatsApp Business vs Cloud API',
    'icono': 'chat',
    'articulo': {'fecha': '2026-09-02'},

    'titulo': 'WhatsApp Business o Cloud API: cuál te conviene | Zyntra',
    'descripcion': ('Diferencias reales entre WhatsApp Business, la app Business y la Cloud API oficial '
                    'de Meta: qué puede hacer cada una y cuándo conviene cambiar.'),

    'h1': 'WhatsApp Business o Cloud API: cuál te conviene',
    'bajada': ('Hay tres cosas distintas que se llaman parecido, y elegir la equivocada te puede costar '
               'el número. Esta es la diferencia, sin vueltas.'),

    'wa': 'Hola%20Zyntra%2C%20le%C3%AD%20la%20nota%20de%20WhatsApp%20y%20tengo%20una%20consulta.',

    'servicio': {'nombre': 'Automatización de WhatsApp', 'tipo': 'Chatbots y WhatsApp'},

    'secciones': [
        {
            'tipo': 'lista',
            'h2': 'Las tres opciones',
            'intro': 'Se llaman parecido y hacen cosas muy distintas.',
            'items': [
                {'icono': 'chat', 'titulo': 'WhatsApp normal',
                 'texto': 'El de siempre, personal. No tiene perfil de empresa, ni catálogo, ni respuestas '
                          'guardadas, ni forma de automatizar nada.'},
                {'icono': 'work', 'titulo': 'App WhatsApp Business',
                 'texto': 'Gratis y se baja del store. Suma perfil de negocio, catálogo, etiquetas, '
                          'mensaje de bienvenida y respuestas rápidas. Vive en un celular.'},
                {'icono': 'hub', 'titulo': 'WhatsApp Cloud API',
                 'texto': 'La conexión oficial de Meta para que un sistema hable por vos. No depende de '
                          'ningún teléfono prendido y permite automatizar de verdad.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Cuándo alcanza la app Business',
            'parrafos': [
                'Más seguido de lo que se cree. Si una sola persona atiende, si el volumen es manejable y '
                'si las respuestas rápidas te resuelven las preguntas repetidas, la app gratuita está '
                'bien y no necesitás nada más.',
                'Sus límites aparecen en tres momentos. Cuando necesitás que atiendan varias personas a '
                'la vez y se pisan. Cuando querés que el sistema haga algo real, como consultar la agenda '
                'y reservar un horario. Y cuando el volumen supera lo que una persona puede leer.',
                'Si no estás en ninguno de esos tres, quedate donde estás. Cambiar antes de tiempo es '
                'gasto sin beneficio.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Qué cambia con la Cloud API',
            'parrafos': [
                'La diferencia de fondo es que deja de haber un teléfono en el medio. Tu número queda '
                'verificado con perfil de empresa y un sistema puede leer los mensajes, entenderlos y '
                'contestar, o consultar tu base de datos antes de responder.',
                'Eso es lo que habilita cosas que la app no puede hacer: agendar sobre disponibilidad '
                'real, mandar el recordatorio del día antes solo, derivar a una persona con el contexto '
                'de la conversación, o atender ochenta consultas al día sin que nadie mire el teléfono.',
                'También cambia el modelo de costo. La app es gratis; la Cloud API la cobra Meta por '
                'conversación, con una ventana gratuita para las que inicia el cliente y cargo para las '
                'que inicia tu negocio. Ese costo va directo a tu cuenta de Meta.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'La opción que conviene evitar',
            'parrafos': [
                'Existe un cuarto camino que aparece bastante y que no recomendamos: las herramientas que '
                'automatizan WhatsApp por la puerta de atrás, simulando ser un celular en vez de usar la '
                'conexión oficial.',
                'Suelen ser más baratas y arrancan rápido. El problema es que van contra los términos de '
                'Meta, y cuando lo detectan bloquean el número. Ahí no perdés una herramienta: perdés la '
                'línea con la que te escriben tus clientes y todos los contactos que tenía.',
                'Si alguien te ofrece automatizar WhatsApp sin pasar por la API oficial y sin verificar '
                'tu número, esa es la señal para preguntar exactamente cómo lo hace.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Cómo decidirlo en dos minutos',
            'parrafos': [
                'Contestá tres preguntas. ¿Se te pisan dos personas contestando el mismo chat? ¿Querés '
                'que el sistema haga algo, no solo que responda un texto fijo? ¿Hay consultas que se '
                'quedan sin contestar porque llegan fuera de horario?',
                'Si respondiste que no a las tres, la app Business te alcanza. Si respondiste que sí a '
                'alguna, ahí empieza a tener sentido la Cloud API.',
                'Si querés ver cómo queda funcionando, mirá '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@chatbot-whatsapp/">'
                'el servicio de chatbot</a> o '
                '<a class="text-primary underline-offset-4 hover:underline" '
                'href="@@SUBIR@@casos-de-exito/chatbot-whatsapp/">el caso de las 80 consultas diarias</a>.',
            ],
        },
    ],

    'cta': {
        'boton': 'Consultar por WhatsApp',
        'titulo': '¿No sabés en cuál de los dos casos estás?',
        'texto': 'Contanos cómo atendés hoy y te decimos si te conviene cambiar o quedarte donde estás.',
    },
}
