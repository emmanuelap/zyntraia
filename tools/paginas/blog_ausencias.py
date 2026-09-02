# -*- coding: utf-8 -*-
"""Nota: como reducir las ausencias a los turnos."""

PAGINA = {
    'slug': 'blog/reducir-ausencias-turnos',
    'padre': {'slug': 'blog', 'nombre': 'Blog'},
    'migas': 'Reducir ausencias',
    'icono': 'event_available',
    'articulo': {'fecha': '2026-09-02'},

    'titulo': 'Cómo reducir las ausencias a los turnos | Zyntra',
    'descripcion': ('Qué hacer para que los clientes no falten al turno: recordatorios, confirmación, '
                    'seña y lista de espera. Qué funciona y qué te espanta clientes.'),

    'h1': 'Cómo lograr que no te falten al turno',
    'bajada': ('Un turno perdido no se recupera: el horario quedó bloqueado y nadie más lo pudo usar. '
               'Esto es lo que funciona, en orden de lo más simple a lo más drástico.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20reducir%20las%20ausencias%20a%20los%20turnos.',

    'servicio': {'nombre': 'Sistema de turnos', 'tipo': 'Turnos y reservas'},

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'Primero: casi nadie falta por maldad',
            'parrafos': [
                'Vale la pena arrancar por acá porque cambia toda la estrategia. La enorme mayoría de las '
                'ausencias no son gente que decidió no ir: es gente que se olvidó, que anotó mal el día, '
                'o que sacó turno con tres semanas de anticipación y para cuando llegó la fecha ya tenía '
                'otra cosa.',
                'Si el problema es el olvido, la solución no es castigar. Es recordar. Y eso explica por '
                'qué la medida más simple es también la que más recupera.',
                'En los sistemas donde pusimos el recordatorio automático, las ausencias por olvido '
                'bajaron a la mitad.',
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Las cuatro medidas, en orden',
            'pasos': [
                {'titulo': 'Recordatorio automático',
                 'texto': 'El día antes, por WhatsApp. Es lo más barato de implementar y lo que más '
                          'devuelve. Si hacés una sola cosa, que sea esta.'},
                {'titulo': 'Confirmación en un toque',
                 'texto': 'Que el recordatorio traiga "confirmo" o "no voy". El que avisa que no va te '
                          'libera el horario a tiempo para dárselo a otro.'},
                {'titulo': 'Lista de espera',
                 'texto': 'Cuando alguien cancela, el sistema le ofrece el lugar al siguiente '
                          'automáticamente. Convierte una cancelación en un turno ocupado.'},
                {'titulo': 'Seña',
                 'texto': 'La medida más efectiva y la más riesgosa. Dejala para el final y leé abajo '
                          'antes de aplicarla.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Por qué la seña no siempre conviene',
            'parrafos': [
                'La seña baja las ausencias muchísimo, eso es cierto. Pero también frena a los clientes '
                'nuevos, que son justamente los que todavía no confían en vos lo suficiente como para '
                'poner plata antes de conocerte.',
                'La cuenta que hay que hacer es esta: cuántos turnos perdés por ausencia contra cuántos '
                'clientes nuevos perdés por pedir seña. En rubros donde el cliente prueba antes de '
                'quedarse, el segundo número suele ser peor.',
                'Lo que funciona mejor en la práctica es aplicarla selectivamente: seña solo en los '
                'horarios más buscados, o solo a quien ya faltó una vez sin avisar. El cliente de '
                'siempre nunca se entera de que existe.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Dos errores comunes',
            'parrafos': [
                '<strong class="text-on-surface">Mandar el recordatorio demasiado temprano.</strong> Tres '
                'días antes se olvida igual. El día anterior, o unas horas antes si el turno es a la '
                'tarde, es lo que funciona.',
                '<strong class="text-on-surface">Depender de que alguien se acuerde de mandarlo.</strong> '
                'Un recordatorio que sale cuando el mostrador tiene tiempo no sale los días complicados, '
                'que son justamente los días con más turnos. Tiene que salir solo.',
                'Y una advertencia sobre la política de cancelación: sirve tenerla escrita, pero solo si '
                'la vas a aplicar. Una regla que anunciás y nunca ejecutás enseña que no pasa nada, y '
                'termina siendo peor que no tener ninguna.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Por dónde empezar',
            'parrafos': [
                'Poné el recordatorio automático y medí un mes. Ese solo cambio suele mover el número lo '
                'suficiente como para que el resto se vuelva opcional.',
                'Si querés ver cómo queda armado, mirá '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@turnos-online/">'
                'el sistema de turnos</a>, o '
                '<a class="text-primary underline-offset-4 hover:underline" '
                'href="@@SUBIR@@casos-de-exito/chatbot-whatsapp/">el caso donde las ausencias bajaron a la '
                'mitad</a>.',
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero reducir las ausencias',
        'titulo': 'Contanos cuántos turnos se te caen por mes',
        'texto': 'En 20 minutos vemos cuánto representa eso y qué haría falta para recuperarlo.',
    },
}
