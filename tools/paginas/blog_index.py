# -*- coding: utf-8 -*-
"""
Indice del blog.

Al agregar una nota nueva hay que sumarla ACA en la lista, arriba de todo,
y crear su archivo tools/paginas/blog_*.py. El build no la descubre solo.
"""

PAGINA = {
    'slug': 'blog',
    'migas': 'Blog',
    'icono': 'campaign',

    'titulo': 'Blog de Zyntra: automatización, turnos y presencia digital',
    'descripcion': ('Notas prácticas sobre chatbots de WhatsApp, turnos online, reseñas en Google Maps y '
                    'qué mirar antes de contratar una página web.'),

    'h1': 'Notas sobre lo que nos preguntan seguido',
    'bajada': ('Sin relleno y sin promesas. Lo que sirve para decidir, incluso cuando la respuesta es que '
               'no necesitás contratarnos.'),

    'wa': 'Hola%20Zyntra%2C%20le%C3%AD%20una%20nota%20del%20blog%20y%20tengo%20una%20consulta.',

    'servicio': {'nombre': 'Consultoría en automatización e IA', 'tipo': 'Consultoría tecnológica'},

    'secciones': [
        {
            'tipo': 'articulos',
            'h2': 'Últimas notas',
            'articulos': [
                {'slug': 'blog/conseguir-resenas-google', 'fecha': '2026-09-02',
                 'titulo': 'Cómo conseguir reseñas en Google sin que te las borren',
                 'resumen': 'De dónde salen las primeras reseñas cuando todavía no tenés clientes nuevos, '
                            'y qué prácticas te hacen perder la ficha entera.'},
                {'slug': 'blog/reducir-ausencias-turnos', 'fecha': '2026-09-02',
                 'titulo': 'Cómo lograr que no te falten al turno',
                 'resumen': 'Las cuatro medidas en orden, por qué la seña no siempre conviene y los dos '
                            'errores que arruinan un recordatorio.'},
                {'slug': 'blog/whatsapp-business-vs-cloud-api', 'fecha': '2026-09-02',
                 'titulo': 'WhatsApp Business o Cloud API: cuál te conviene',
                 'resumen': 'Tres cosas que se llaman parecido y hacen cosas distintas. Cuándo alcanza la '
                            'app gratis y cuál es la opción que te puede costar el número.'},
                {'slug': 'blog/que-preguntar-antes-de-contratar-una-web', 'fecha': '2026-09-02',
                 'titulo': 'Seis preguntas antes de contratar una página web',
                 'resumen': 'Ninguna es sobre diseño. Son las que deciden si dentro de dos años la web es '
                            'tuya o seguís dependiendo de alguien.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Cómo escribimos esto',
            'parrafos': [
                'Cada nota tiene que servirle a alguien que no nos va a contratar. Si el texto solo tiene '
                'sentido como excusa para vender, no lo publicamos.',
                'Por eso vas a encontrar seguido la parte donde decimos que no hace falta contratar nada: '
                'que la app gratuita de WhatsApp te alcanza, que con treinta socios no necesitás un '
                'sistema, que si facturás tres veces por mes el portal de AFIP está bien.',
                'Y no vas a encontrar cifras inventadas. Los únicos números que publicamos son los que '
                'podemos sostener, y están en '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@casos-de-exito/">'
                'los casos</a>.',
            ],
        },
    ],

    'cta': {
        'boton': 'Escribinos',
        'titulo': '¿Hay algo que te gustaría que expliquemos?',
        'texto': 'Contanos qué duda tenés y si da para una nota, la escribimos.',
    },
}
