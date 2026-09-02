# -*- coding: utf-8 -*-
"""
Caso de exito: asistente de WhatsApp multi rubro.

Cifras confirmadas por el dueno: alrededor de 80 consultas diarias y una caida
del 50% en las ausencias por olvido de turno. No agregar ninguna otra cifra.
"""

PAGINA = {
    'slug': 'casos-de-exito/chatbot-whatsapp',
    'padre': {'slug': 'casos-de-exito', 'nombre': 'Casos de éxito'},
    'migas': 'Asistente de WhatsApp',
    'icono': 'smart_toy',

    'titulo': 'Caso: un asistente de WhatsApp que atiende 80 consultas por día | Zyntra',
    'descripcion': ('Un asistente de WhatsApp que responde alrededor de 80 consultas diarias, agenda en '
                    'Google Calendar y bajó a la mitad las ausencias por olvido de turno.'),

    'h1': 'Un asistente que atiende 80 consultas por día',
    'bajada': ('Responde, agenda y hace el seguimiento solo. Y con el recordatorio automático, las '
               'ausencias por olvido de turno cayeron a la mitad.'),

    'wa': 'Hola%20Zyntra%2C%20vi%20el%20caso%20del%20chatbot%20y%20quiero%20algo%20as%C3%AD.',

    'servicio': {
        'nombre': 'Asistente de WhatsApp multi rubro',
        'tipo': 'Desarrollo de chatbots y automatización de WhatsApp',
    },

    'secciones': [
        {
            'tipo': 'cifras',
            'h2': 'Los números',
            'intro': 'Medidos sobre el asistente funcionando, no estimados.',
            'numeros': [
                {'cifra': '80', 'titulo': 'Consultas por día',
                 'detalle': 'Atendidas sin que nadie tenga que estar mirando el teléfono.'},
                {'cifra': '50%', 'titulo': 'Menos ausencias',
                 'detalle': 'Caída de las ausencias por olvido, gracias al recordatorio automático.'},
                {'cifra': '24 h', 'titulo': 'Sin horario',
                 'detalle': 'Contesta de noche, los domingos y los feriados igual.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'El problema',
            'parrafos': [
                'Ochenta consultas por día son ochenta interrupciones. Y la mayoría no son complicadas: '
                'cuánto sale, a qué hora abren, si hay lugar el jueves, dónde quedan. Las mismas diez '
                'preguntas, todo el día.',
                'El problema no era contestar, era cuándo. Llegan a las once de la noche, un domingo, o '
                'justo mientras se atiende a alguien que está adelante. Y una consulta contestada seis '
                'horas después ya no es una consulta: es un cliente que mientras tanto le escribió a '
                'otro.',
                'Al mismo tiempo estaba el otro agujero: el turno agendado al que la persona no venía. '
                'Casi nunca por mala fe, casi siempre por olvido.',
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo funciona',
            'pasos': [
                {'titulo': 'Entiende lo que le escriben',
                 'texto': 'Sin menús de números. Un modelo de lenguaje interpreta el mensaje escrito como '
                          'lo escribiría cualquiera.'},
                {'titulo': 'Trabaja sobre la agenda real',
                 'texto': 'Consulta la disponibilidad verdadera y agenda, cancela o reprograma con evento '
                          'creado en Google Calendar.'},
                {'titulo': 'Recuerda antes del turno',
                 'texto': 'El aviso automático del día antes. Es la pieza que explica la mitad de las '
                          'ausencias recuperadas.'},
                {'titulo': 'Pasa a una persona',
                 'texto': 'Cuando la consulta se sale de lo que sabe resolver, deriva con todo el '
                          'contexto de lo que se venía hablando.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Por qué el recordatorio es lo que más rinde',
            'parrafos': [
                'De todo lo que hace el asistente, la función más simple es la que más plata devuelve. '
                'Un turno perdido no se recupera: el horario quedó bloqueado, nadie más lo pudo usar y '
                'el ingreso de esa franja no existió.',
                'Bajar eso a la mitad no requirió inteligencia artificial ni nada sofisticado. Requirió '
                'que el mensaje salga solo, siempre, sin depender de que alguien se acuerde de mandarlo.',
                'Si estás evaluando por dónde empezar, empezá por ahí. El resto suma, pero esto se paga '
                'antes.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'La misma base, otro rubro',
            'parrafos': [
                'El asistente es multi rubro por diseño. La misma base sirve para una peluquería, un '
                'consultorio, un gimnasio, un restaurante o un comercio: cambian los servicios, los '
                'horarios y el tono, no el sistema.',
                'Eso significa que no arrancás de cero: arrancás de algo que ya funciona y lo adaptamos '
                'a cómo trabajás vos, que es donde de verdad se va el tiempo.',
                'La página del servicio es '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@chatbot-whatsapp/">'
                'chatbot de WhatsApp</a>, y si lo que te interesa es solo la parte de la agenda, mirá '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@turnos-online/">'
                'turnos online</a>.',
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero un asistente así',
        'titulo': 'Contanos qué te preguntan todo el día',
        'texto': ('En 20 minutos vemos cuántas de tus consultas se pueden automatizar y cuántos turnos '
                  'estás perdiendo por olvido. El diagnóstico queda para vos aunque no contrates.'),
    },
}
