# -*- coding: utf-8 -*-
"""Pagina de servicio: chatbot de WhatsApp."""

PAGINA = {
    'slug': 'chatbot-whatsapp',
    'migas': 'Chatbot de WhatsApp',
    'icono': 'smart_toy',

    'titulo': 'Chatbot de WhatsApp para empresas | Zyntra',
    'descripcion': ('Chatbots de WhatsApp que atienden, agendan turnos y hacen seguimiento las 24 horas. '
                    'Entienden lenguaje natural, sin menús de números. Desarrollo a medida en Argentina.'),

    'h1': 'Chatbot de WhatsApp para empresas en Argentina',
    'bajada': ('Un asistente que contesta al instante, agenda sobre tu disponibilidad real y hace el '
               'seguimiento solo. No es un menú de números: entiende lo que le escriben.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20un%20chatbot%20de%20WhatsApp%20para%20mi%20negocio.',

    'servicio': {
        'nombre': 'Chatbot de WhatsApp a medida',
        'tipo': 'Desarrollo de chatbots y automatización de WhatsApp',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'El problema no es contestar. Es cuándo.',
            'parrafos': [
                'La mayoría de las consultas que llegan por WhatsApp no son complicadas: cuánto sale, '
                'a qué hora abren, si hay lugar el jueves, dónde quedan. Son las mismas diez preguntas '
                'todos los días.',
                'El problema es el horario. Llegan a las once de la noche, un domingo, o justo cuando '
                'estás atendiendo a alguien adelante tuyo. Y una consulta contestada seis horas después '
                'ya no es una consulta: es un cliente que mientras tanto le escribió a otro.',
                'Un chatbot bien armado no reemplaza a nadie. Se come esas diez preguntas repetidas y te '
                'deja las conversaciones que sí necesitan una persona, con el cliente ya calificado.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Qué automatizamos',
            'intro': 'Se arma por partes. No hace falta empezar con todo.',
            'items': [
                {'icono': 'chat', 'titulo': 'Atención de consultas',
                 'texto': 'Precios, horarios, ubicación, servicios, formas de pago. Contesta con la '
                          'información real de tu negocio, no con respuestas genéricas.'},
                {'icono': 'event_available', 'titulo': 'Turnos y reservas',
                 'texto': 'Agenda, cancela y reprograma trabajando sobre tu disponibilidad real, con '
                          'evento creado en Google Calendar. Sin dobles turnos.'},
                {'icono': 'shopping_bag', 'titulo': 'Toma de pedidos',
                 'texto': 'Arma el pedido conversando, confirma el detalle antes de cerrar y te lo deja '
                          'listo para preparar.'},
                {'icono': 'campaign', 'titulo': 'Recordatorios',
                 'texto': 'Aviso automático el día antes del turno. Es lo que más reduce las ausencias, '
                          'y no depende de que alguien se acuerde de mandarlo.'},
                {'icono': 'autorenew', 'titulo': 'Post-venta y reactivación',
                 'texto': 'Seguimiento después de la compra o del servicio, y contacto con el cliente '
                          'que hace meses no vuelve.'},
                {'icono': 'badge', 'titulo': 'Derivación a una persona',
                 'texto': 'Cuando la consulta se sale del libreto, pasa la conversación a un humano con '
                          'todo el contexto de lo que se venía hablando.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo funciona por dentro',
            'pasos': [
                {'titulo': 'WhatsApp Cloud API',
                 'texto': 'La conexión oficial de Meta. Tu número queda verificado, con perfil de '
                          'empresa, y no depende de un celular prendido en un rincón.'},
                {'titulo': 'Comprensión del mensaje',
                 'texto': 'Un modelo de lenguaje interpreta lo que la persona quiso decir, escrito como '
                          'lo escribiría cualquiera. Sin "marque 1 para turnos".'},
                {'titulo': 'Acción sobre tus sistemas',
                 'texto': 'Consulta la agenda, reserva el horario, arma el pedido o busca el dato. Lee y '
                          'escribe donde ya trabajás: Google Calendar, tu base, tu planilla.'},
                {'titulo': 'Respuesta y registro',
                 'texto': 'Contesta en segundos y deja la conversación registrada, para que puedas ver '
                          'qué se preguntó y qué se resolvió.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'La base es la misma, el negocio cambia',
            'parrafos': [
                'Tenemos un asistente multi rubro andando en producción. La misma base sirve para una '
                'peluquería, un consultorio, un gimnasio, un restaurante o un comercio: cambian los '
                'servicios, los horarios y el tono, no el sistema.',
                'Eso significa que no arrancás de cero. Arrancás de algo que ya funciona y lo adaptamos '
                'a cómo trabajás vos, que es donde se va el tiempo de verdad.',
                'Podés ver las capturas del asistente funcionando en la '
                '<a class="text-primary underline-offset-4 hover:underline" href="../#proyectos">sección '
                'de proyectos</a>.',
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre chatbots de WhatsApp',
            'preguntas': [
                {'q': '¿Cuánto cuesta tener un chatbot de WhatsApp funcionando?',
                 'a': 'Hay dos costos distintos y conviene no mezclarlos. Uno es el desarrollo, que se '
                      'presupuesta cerrado según qué tenga que hacer el bot. El otro es lo que cobra Meta '
                      'por usar la API oficial, que se paga por conversación y va directo a tu cuenta, sin '
                      'intermediarios ni comisión nuestra. Las conversaciones que inicia el cliente '
                      'escribiéndote tienen una ventana gratuita; las que inicia tu negocio, como un '
                      'recordatorio, se cobran. Te mostramos el cálculo con tu volumen real antes de que '
                      'decidas nada.'},
                {'q': '¿Se nota que es un bot?',
                 'a': 'Se nota si está mal hecho. Los que responden con menús numerados y se traban cuando '
                      'les escribís algo fuera del libreto se notan a los tres mensajes. Un asistente que '
                      'entiende lenguaje natural, que responde con la información real del negocio y que '
                      'pasa a una persona cuando la consulta se complica, no molesta. Nosotros además '
                      'aclaramos que es un asistente: mentir sobre eso arruina la confianza más rápido de '
                      'lo que la construye.'},
                {'q': '¿Puedo seguir contestando yo cuando quiera?',
                 'a': 'Sí, y es la forma en que conviene usarlo. El bot toma lo repetido y te avisa cuando '
                      'alguien pide hablar con una persona o cuando la conversación se sale de lo que sabe '
                      'resolver. Vos entrás en el mismo chat, con todo lo que se venía hablando a la vista.'},
                {'q': '¿Sirve si mi negocio es muy particular?',
                 'a': 'Depende de cuántas de tus consultas son realmente particulares. Casi siempre el '
                      '70 u 80 por ciento son las mismas preguntas de siempre, y ese es el trabajo que se '
                      'puede sacar de encima. El 20 por ciento raro sigue siendo tuyo, y así tiene que ser. '
                      'Si tu caso es de los que no cierra, te lo decimos en la primera charla.'},
                {'q': '¿Qué pasa si Meta cambia las reglas?',
                 'a': 'Es un riesgo real y conviene tenerlo claro desde el principio. Por eso trabajamos '
                      'sobre la API oficial y no sobre soluciones que automatizan WhatsApp por la puerta de '
                      'atrás: esas funcionan hasta que Meta te bloquea el número, y ahí perdés la cuenta y '
                      'los contactos. La API oficial cambia de precios y de políticas, pero no te deja sin '
                      'línea de un día para el otro.'},
            ],
            'mas': [
                ('que-es-un-chatbot-de-whatsapp-y-como-funciona',
                 '¿Qué es un chatbot de WhatsApp y cómo funciona?'),
                ('que-diferencia-hay-entre-un-chatbot-y-una-respuesta-automatica',
                 '¿Qué diferencia hay entre un chatbot y una respuesta automática?'),
                ('un-chatbot-reemplaza-a-una-persona-atendiendo',
                 '¿Un chatbot reemplaza a una persona atendiendo?'),
                ('se-pueden-tomar-turnos-automaticamente-por-whatsapp',
                 '¿Se pueden tomar turnos automáticamente por WhatsApp?'),
                ('se-pueden-mandar-recordatorios-automaticos-por-whatsapp',
                 '¿Se pueden mandar recordatorios automáticos por WhatsApp?'),
                ('como-tomo-pedidos-por-whatsapp-sin-equivocarme',
                 '¿Cómo tomo pedidos por WhatsApp sin equivocarme?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero un chatbot para mi negocio',
        'titulo': 'Contanos qué te preguntan todo el día',
        'texto': ('En 20 minutos vemos qué parte de tus consultas se puede automatizar y qué te costaría. '
                  'El diagnóstico queda para vos aunque no contrates.'),
    },
}
