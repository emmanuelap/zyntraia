# -*- coding: utf-8 -*-
"""
Caso de exito: asistente de WhatsApp multi rubro.

Cifras confirmadas por el dueno: alrededor de 80 consultas diarias y una caida
del 50% en las ausencias por olvido de turno. No agregar ninguna otra cifra.

Esta pagina tiene que decir cosas que la de servicio (chatbot_whatsapp.py) no
dice: Google la dejo sin indexar mientras compartia un 30% de frases con esa
pagina. Antes de copiar un parrafo de alla para aca, reescribirlo.

La conversacion de muestra NO es de un cliente real y lo dice arriba. Esa
aclaracion no se saca: sin ella se lee como testimonio, y no se inventan
testimonios.
"""

PAGINA = {
    'slug': 'casos-de-exito/chatbot-whatsapp',
    'padre': {'slug': 'casos-de-exito', 'nombre': 'Casos de éxito'},
    'migas': 'Asistente de WhatsApp',
    'icono': 'smart_toy',
    'ojito': 'normal',

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
            'h2': 'Antes del asistente',
            'parrafos': [
                'Ochenta mensajes por día no parecen tantos hasta que se reparten a lo largo de la '
                'jornada: uno cada pocos minutos, cada uno cortando lo que se estaba haciendo. El costo '
                'no está en cada respuesta, que lleva segundos. Está en la interrupción, y en volver a '
                'concentrarse después.',
                'Del otro lado estaba la agenda. Un turno confirmado no garantiza que la persona venga, '
                'y cada hueco que queda vacío es una hora que se pagó igual: el local abierto, el '
                'profesional esperando, nadie en la silla.',
                'Eran dos problemas distintos con la misma raíz: todo dependía de que alguien estuviera '
                'libre para agarrar el teléfono en el momento justo.',
            ],
        },
        {
            'tipo': 'texto',
            'fondo': True,
            'h2': 'Una conversación de principio a fin',
            'parrafos': [
                '<em>Conversación de muestra, armada para mostrar el recorrido completo. No es de un '
                'cliente real.</em>',
                '<strong>Cliente, martes 23:40:</strong> hola, ¿tienen lugar el jueves a la tarde para '
                'corte?',
                '<strong>Asistente:</strong> ¡Hola! El jueves a la tarde tengo libre a las 16:00 y a las '
                '17:30. ¿Te reservo alguno?',
                '<strong>Cliente:</strong> el de 17:30',
                '<strong>Asistente:</strong> Listo, quedó reservado el jueves a las 17:30. El miércoles '
                'te escribo para recordártelo.',
                '<strong>Asistente, miércoles 10:00:</strong> Te recuerdo tu turno de mañana jueves a '
                'las 17:30. Si no podés venir, avisame por acá y lo cambiamos.',
                'Nadie del negocio tocó el teléfono, y el turno ya figura en el calendario con nombre y '
                'horario. El mensaje de las once y cuarenta de la noche, que antes se contestaba recién '
                'a la mañana siguiente, quedó resuelto en el momento.',
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Qué pasa por detrás de esa conversación',
            'pasos': [
                {'titulo': 'Lee el mensaje como viene',
                 'texto': 'Con errores de tipeo, sin signos, todo en una línea. Nadie tiene que aprender '
                          'a hablarle a un bot.'},
                {'titulo': 'Mira la agenda antes de ofrecer',
                 'texto': 'Los horarios que propone salen del calendario en ese momento, no de una lista '
                          'fija. Por eso no ofrece un turno que ya se dio.'},
                {'titulo': 'Deja el turno escrito',
                 'texto': 'Cada reserva crea su evento en Google Calendar. El negocio la ve en el mismo '
                          'calendario que ya usaba, sin abrir otro sistema.'},
                {'titulo': 'Vuelve a escribir el día antes',
                 'texto': 'El recordatorio sale solo. Si la persona avisa que no puede, el turno se mueve '
                          'o queda libre para otro.'},
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
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Lo que el asistente no hace',
            'intro': 'Los límites también son parte del diseño.',
            'items': [
                {'icono': 'check', 'titulo': 'No adivina',
                 'texto': 'Lo que dice sale de la información que cargó el negocio: servicios, horarios '
                          'y precios. Lo que no está ahí no lo completa de memoria.'},
                {'icono': 'personas', 'titulo': 'No se hace pasar por persona',
                 'texto': 'Se presenta como asistente. Esconderlo sale caro el día que alguien se da '
                          'cuenta.'},
                {'icono': 'chatbot', 'titulo': 'No se queda con lo difícil',
                 'texto': 'Un reclamo o un caso especial va a una persona del negocio, que entra al mismo '
                          'chat y lee todo lo anterior antes de contestar.'},
                {'icono': 'candado', 'titulo': 'No usa atajos que Meta bloquea',
                 'texto': 'Corre sobre la API oficial de WhatsApp. Las herramientas no oficiales andan '
                          'hasta el día en que suspenden el número.'},
            ],
        },
        {
            'tipo': 'faq',
            'h2': 'Preguntas sobre este caso',
            'preguntas': [
                {'q': '¿Puedo empezar solo por el recordatorio?',
                 'a': 'Sí. Es la parte más chica y la que antes se paga, así que muchas veces conviene '
                      'arrancar por ahí y sumar la atención de consultas después. Si lo que buscás es '
                      'sobre todo ordenar la agenda, mirá '
                      '<a class="enlace" href="@@SUBIR@@turnos-online/">turnos online</a>.'},
                {'q': '¿Qué hace falta de mi lado?',
                 'a': 'Un número de WhatsApp para el negocio, la agenda donde ya la llevás (Google '
                      'Calendar, una planilla o tu sistema) y la información que el asistente va a usar: '
                      'servicios, horarios, precios y las respuestas a las preguntas de siempre. La '
                      'conexión y el armado quedan de nuestro lado.'},
                {'q': '¿Los recordatorios tienen algún costo aparte?',
                 'a': 'Sí, y conviene saberlo desde el principio: Meta cobra los mensajes que inicia el '
                      'negocio, y el recordatorio es uno de ellos. Se paga directo a Meta desde tu '
                      'cuenta, sin pasar por nosotros. Antes de arrancar te mostramos cuánto da con tu '
                      'cantidad de turnos.'},
            ],
            'mas': [
                ('se-pueden-mandar-recordatorios-automaticos-por-whatsapp',
                 '¿Se pueden mandar recordatorios automáticos por WhatsApp?'),
                ('se-pueden-tomar-turnos-automaticamente-por-whatsapp',
                 '¿Se pueden tomar turnos automáticamente por WhatsApp?'),
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Si tu negocio es otro',
            'parrafos': [
                'Este asistente se pensó para cualquier rubro que viva de turnos y de consultas '
                'repetidas. De un negocio a otro cambia la información que usa y la forma de hablar; '
                'el mecanismo es el mismo.',
                'Todo lo que puede hacer, incluida la toma de pedidos, está en la página de '
                '<a class="enlace" href="@@SUBIR@@chatbot-whatsapp/">chatbot de WhatsApp</a>. '
                'Si te interesa solo la agenda, mirá '
                '<a class="enlace" href="@@SUBIR@@turnos-online/">turnos online</a>.',
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero un asistente así',
        'titulo': '¿Cuántos turnos se te caen por olvido?',
        'texto': ('En 20 minutos miramos tus consultas y tu agenda, y te decimos qué conviene '
                  'automatizar primero. Si la respuesta es "todavía nada", también te lo decimos.'),
    },
}
