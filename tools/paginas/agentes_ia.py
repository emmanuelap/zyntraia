# -*- coding: utf-8 -*-
"""
Pagina de servicio: agentes de IA multi rubro, con la ficha tecnica, y el CRM
de WhatsApp a medida.

Todo lo que dice sale de los agentes que ya estan armados (el de estetica y el
de la muebleria) y del CRM. Sin nombres de clientes ni de socios, sin precios
y sin cifras: las unicas publicables estan en AGENT_MEMORY.md.

El CRM se presenta como servicio, sin nombre de producto y sin capturas,
hasta que tenga nombre definitivo (es una sociedad). Solo se nombran funciones
que ya estan hechas; la conexion con Google Ads queda afuera hasta que este
andando con una cuenta real.

No copiar frases de chatbot_whatsapp.py: Google deja afuera una de las dos
paginas si se parecen (ya paso con el caso del chatbot).
"""

PAGINA = {
    'slug': 'agentes-ia',
    'migas': 'Agentes de IA',
    'icono': 'hub',
    'ojito': 'abierto',

    'titulo': 'Agentes de IA multi rubro para WhatsApp y CRM a medida | Zyntra',
    'descripcion': ('Agentes de IA para WhatsApp que atienden, filtran, agendan y venden. Ficha técnica '
                    'completa: Claude, n8n, Supabase y la API oficial de Meta. Y CRM a medida.'),

    'h1': 'Agentes de IA multi rubro, con la ficha técnica a la vista',
    'bajada': ('Un agente no es un contestador: lee la conversación, decide qué hacer y lo hace sobre '
               'tus sistemas. Acá está cómo está construido, pieza por pieza, para que sepas qué estás '
               'contratando.'),

    'wa': 'Hola%20Zyntra%2C%20me%20interesa%20un%20agente%20de%20IA%20para%20mi%20negocio.',

    'servicio': {
        'nombre': 'Agentes de IA multi rubro',
        'tipo': 'Desarrollo de agentes de inteligencia artificial',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'Qué cambia entre un chatbot y un agente',
            'parrafos': [
                'Un chatbot contesta. Un agente además actúa: busca el horario libre y lo reserva, arma '
                'el pedido con el total, manda el catálogo cuando se lo piden y le avisa a una persona '
                'cuando la venta está lista para cerrar.',
                'La diferencia no está en lo que dice, sino en lo que puede tocar. Por eso un agente se '
                'diseña empezando por los permisos: qué puede leer, qué puede escribir y qué tiene '
                'prohibido.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Ficha técnica',
            'intro': ('Las piezas con las que está armado hoy. Si tu caso pide otra, se cambia esa pieza '
                      'sin rehacer el resto.'),
            'items': [
                {'icono': 'automatizacion', 'titulo': 'Cerebro: Claude, de Anthropic',
                 'texto': 'Interpreta el mensaje y redacta la respuesta. El modelo es un valor de '
                          'configuración: se cambia por uno más rápido o más potente sin tocar el código.'},
                {'icono': 'whatsapp', 'titulo': 'Canal: API oficial de WhatsApp',
                 'texto': 'WhatsApp Cloud API de Meta, con número verificado. Si querés seguir usando la '
                          'app en ese mismo número, se conecta en modo coexistencia.'},
                {'icono': 'bloques', 'titulo': 'Orquestación: n8n',
                 'texto': 'Cada paso del agente es un nodo a la vista: qué recibió, qué decidió y qué '
                          'mandó. Si algo falla, se ve en qué paso.'},
                {'icono': 'candado', 'titulo': 'Datos: Supabase y PostgreSQL',
                 'texto': 'Catálogo, precios, preguntas frecuentes y conversaciones viven en una base con '
                          'seguridad por fila desde el primer día. Cambiar un precio no obliga a reescribir '
                          'el agente.'},
                {'icono': 'turnos', 'titulo': 'Agenda: Google Calendar',
                 'texto': 'Lee la disponibilidad real y crea el evento al reservar. Tu equipo sigue '
                          'mirando el mismo calendario de siempre.'},
                {'icono': 'personas', 'titulo': 'Avisos: Telegram y bandeja web',
                 'texto': 'Cuando un cliente está listo para comprar, te llega su ficha con lo que pidió y '
                          'un enlace que abre su chat directo.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Qué hace con cada mensaje',
            'pasos': [
                {'titulo': 'Filtra',
                 'texto': 'Antes de guardar nada, decide si le toca contestar. En un número que también '
                          'es personal, deja pasar el "hola" de un conocido sin meterse.'},
                {'titulo': 'Arma el contexto',
                 'texto': 'Junta la charla previa, el catálogo y las reglas del negocio, y recién ahí le '
                          'pregunta al modelo.'},
                {'titulo': 'Responde y actúa',
                 'texto': 'Contesta, reserva, manda el PDF o toma el pedido, según lo que pida esa '
                          'conversación.'},
                {'titulo': 'Avisa o deriva',
                 'texto': 'Si la venta está madura o la consulta lo excede, la pasa a una persona con la '
                          'ficha ya armada.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Multi rubro de verdad',
            'parrafos': [
                'El mismo armazón se adaptó a negocios que no se parecen en nada: un centro de estética '
                'que vive de turnos y una mueblería que vende piezas por catálogo y trabajos a medida. '
                'Lo que cambia es la base de conocimiento y las reglas: qué se agenda, qué se cotiza y '
                'qué va siempre a una persona.',
                'Esas reglas son decisiones de negocio, no técnicas. En un mueble a medida no hay precio '
                'de lista, así que el agente no inventa un número: junta medidas, material y plazo, y se '
                'lo pasa a quien cotiza. Un número mal tirado espanta al cliente o compromete al taller.',
            ],
        },
        {
            'tipo': 'lista',
            'id': 'crm',
            'fondo': True,
            'h2': 'CRM de WhatsApp a medida',
            'intro': ('Cuando el volumen pasa de un número y una persona, el agente necesita dónde vivir: '
                      'un CRM donde todo el equipo ve las mismas conversaciones.'),
            'items': [
                {'icono': 'personas', 'titulo': 'Bandeja compartida',
                 'texto': 'Varias personas atienden el mismo número, cada chat con su responsable '
                          'asignado.'},
                {'icono': 'embudo', 'titulo': 'Embudos de venta',
                 'texto': 'Cada conversación avanza por etapas que definís vos, y se ve cuántas hay '
                          'trabadas en cada una.'},
                {'icono': 'mail', 'titulo': 'Campañas con plantillas',
                 'texto': 'Envíos a listas filtradas con plantillas aprobadas por Meta, sin copiar y '
                          'pegar contacto por contacto.'},
                {'icono': 'tablero', 'titulo': 'De qué anuncio vino cada cliente',
                 'texto': 'Atribución de fuentes y anuncios, para saber qué campaña trae ventas y cuál '
                          'solo trae mensajes.'},
                {'icono': 'automatizacion', 'titulo': 'IA con supervisión',
                 'texto': 'Los agentes de IA atienden adentro del CRM, y lo que dijeron y decidieron '
                          'queda registrado para revisarlo y ajustarlo.'},
                {'icono': 'bloques', 'titulo': 'Se instala como app',
                 'texto': 'Funciona en la computadora y se instala en el celular, sin pasar por ninguna '
                          'tienda de aplicaciones.'},
            ],
        },
        {
            'tipo': 'faq',
            'h2': 'Preguntas sobre agentes de IA',
            'preguntas': [
                {'q': '¿Qué modelo de inteligencia artificial usan?',
                 'a': 'Hoy, Claude de Anthropic, por la fluidez con que escribe y el equilibrio entre '
                      'calidad y costo en conversaciones de WhatsApp. Está puesto como configuración: si '
                      'mañana conviene otro modelo, se cambia sin rehacer el agente.'},
                {'q': '¿A nombre de quién quedan las cuentas?',
                 'a': 'De tu negocio. El número de WhatsApp, la cuenta de Meta y la del modelo de IA se '
                      'dan de alta a tu nombre, y el consumo se paga desde tus cuentas, no desde las '
                      'nuestras. Si un día dejás de trabajar con nosotros, todo sigue siendo tuyo.'},
                {'q': '¿Puedo seguir usando WhatsApp en mi celular?',
                 'a': 'Sí. Meta permite conectar la API en el mismo número que usás en la app, y lo llama '
                      'coexistencia. El agente contesta lo que le corresponde y vos seguís viendo y '
                      'escribiendo desde el teléfono.'},
                {'q': '¿Qué pasa si la IA no entiende un mensaje?',
                 'a': 'Pide que se lo digan con otras palabras en vez de suponer. Y si la consulta se sale '
                      'de lo que sabe resolver, la pasa a una persona.'},
            ],
            'mas': [
                ('que-diferencia-hay-entre-un-chatbot-y-una-respuesta-automatica',
                 '¿Qué diferencia hay entre un chatbot y una respuesta automática?'),
                ('un-chatbot-reemplaza-a-una-persona-atendiendo',
                 '¿Un chatbot reemplaza a una persona atendiendo?'),
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Por dónde seguir',
            'parrafos': [
                'Si lo tuyo es sobre todo contestar consultas y dar turnos, empezá por la página del '
                '<a class="enlace" href="@@SUBIR@@chatbot-whatsapp/">chatbot de WhatsApp</a>. Para ver '
                'un agente funcionando con números reales, está el '
                '<a class="enlace" href="@@SUBIR@@casos-de-exito/chatbot-whatsapp/">caso del asistente '
                'que atiende 80 consultas por día</a>.',
                'Y si lo que te come el día son tareas repetidas entre sistemas, mirá '
                '<a class="enlace" href="@@SUBIR@@automatizacion-procesos/">automatización de '
                'procesos</a>.',
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero un agente para mi negocio',
        'titulo': 'Contanos qué tendría que hacer tu agente',
        'texto': ('En 20 minutos vemos qué conversaciones se pueden delegar, qué pieza de la ficha cambia '
                  'en tu caso y si conviene sumar un CRM.'),
    },
}
