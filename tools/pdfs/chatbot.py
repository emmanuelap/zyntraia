# -*- coding: utf-8 -*-
"""
Propuesta del chatbot de WhatsApp.

Es el unico documento del sitio que lleva precios, y el dueno decidio
mantenerlos: quien lo descarga ya mostro interes, no es una lista de precios
en una pagina. La regla de "ningun precio en el sitio" sigue valiendo para
el HTML.

En la matriz de planes se usa "Si" y la raya, no un tilde: el glifo del tilde
no esta en las instancias estaticas que genera pdf_marca y saldria el
cuadradito de caracter faltante.
"""

TITULO = 'Chatbot de WhatsApp con IA'
SUBTITULO = ('Turnos, atención y seguimiento automáticos para negocios que '
             'trabajan con agenda.')
PIE = 'Chatbot de WhatsApp con IA'

SI, NO = 'Sí', '—'

FUNCIONES = [
    ('Agenda de turnos con disponibilidad real', SI, SI, SI),
    ('Evento automático en Google Calendar', SI, SI, SI),
    ('Recordatorios 24 h y 2 h antes', SI, SI, SI),
    ('Cancelar y reprogramar desde el chat', SI, SI, SI),
    ('Menú de botones y listas interactivas', SI, SI, SI),
    ('Carga inicial y puesta en marcha', SI, SI, SI),
    ('Conversación con IA en lenguaje natural', NO, SI, SI),
    ('Recomienda servicios según lo que pide', NO, SI, SI),
    ('Recuerda el hilo de la conversación', NO, SI, SI),
    ('Ficha del cliente y saludo por su nombre', NO, SI, SI),
    ('Seguimiento posterior al servicio', NO, SI, SI),
    ('Reactivación de clientes inactivos', NO, SI, SI),
    ('Derivación automática a una persona', NO, SI, SI),
    ('Catálogo, carrito y toma de pedidos', NO, NO, SI),
    ('Control de stock', NO, NO, SI),
    ('Lista de espera por cancelaciones', NO, NO, SI),
    ('Planes de sesiones y paquetes', NO, NO, SI),
    ('Cobros con Mercado Pago', NO, NO, SI),
]


def construir(Documento, C):
    d = Documento('propuesta-chatbot-zyntra', TITULO, SUBTITULO, pie=PIE, lid=.16)
    d.portada(['Tres planes, pago único. Importes en dólares estadounidenses.'])

    d.seccion('', 'Qué es')
    d.parrafo(
        'Un asistente que atiende el WhatsApp del negocio las 24 horas, todos los '
        'días. Responde consultas, agenda turnos con disponibilidad real, envía '
        'recordatorios y hace seguimiento, sin intervención humana.')
    d.parrafo(
        'No es un menú de opciones con respuestas fijas. Entiende lo que el cliente '
        'escribe en sus propias palabras, recuerda lo que venían hablando y sabe '
        'cuándo dejar de responder y avisar a una persona.')
    d.espacio(2)
    d.dato('24/7', 'Atiende siempre, también de madrugada.')
    d.dato('&lt; 5 s', 'Tiempo de respuesta a cada mensaje.')
    d.dato('0', 'Turnos perdidos por no contestar a tiempo.')

    d.seccion('', 'Para qué rubros',
              'Cualquier negocio que trabaje con agenda: peluquerías y barberías, '
              'consultorios médicos y odontológicos, centros de estética, kinesiología '
              'y nutrición, estudios de tatuajes, gimnasios y entrenadores, talleres '
              'mecánicos, veterinarias, estudios contables y jurídicos.')
    d.parrafo(
        'El sistema no está atado a un rubro: los servicios, precios, horarios y '
        'profesionales se cargan al configurarlo.')

    d.salto()

    # ------------------------------------------------------------------ 01
    d.seccion('01', 'Cómo funciona',
              'El sistema conecta cuatro piezas. El cliente sólo ve WhatsApp; todo lo '
              'demás ocurre por detrás, en menos de cinco segundos.')
    d.titulo3('El recorrido de un mensaje')
    d.tabla(
        ['Paso', 'Qué pasa'],
        [['1', '<b>El cliente escribe.</b> Manda un mensaje al WhatsApp del negocio, en '
               'sus propias palabras.'],
         ['2', '<b>El sistema entiende.</b> Interpreta qué necesita: un turno, un precio, '
               'un producto o una consulta.'],
         ['3', '<b>Busca la información real.</b> Consulta la agenda, el catálogo y el '
               'historial de ese cliente.'],
         ['4', '<b>Responde y ejecuta.</b> Contesta, agenda el turno y crea el evento en '
               'Google Calendar.'],
         ['5', '<b>Hace el seguimiento.</b> Manda recordatorios y mensajes posteriores, '
               'sin que nadie los dispare.']],
        anchos=[9, 91])
    d.titulo3('Las piezas que intervienen')
    d.tabla(
        ['Pieza', 'Qué hace'],
        [['WhatsApp Business API', 'El número dedicado del bot, provisto por Meta.'],
         ['Motor de automatización', 'Entiende, decide y responde.'],
         ['Base de datos', 'Clientes, turnos, pedidos e historial.'],
         ['Google Calendar', 'La agenda real, por persona o por recurso.'],
         ['Inteligencia artificial', 'Interpreta el pedido y recomienda.']],
        anchos=[30, 70])

    d.salto()

    # ------------------------------------------------------------------ 02
    d.seccion('02', 'Planes y precios',
              'Tres alcances posibles. Todos incluyen la puesta en marcha, la carga '
              'inicial de datos y las pruebas junto al equipo. Se paga una sola vez.')
    d.tabla(
        ['Plan', 'Pago único', 'Para quién es'],
        [['<b>Esencial</b>', '<b>USD 400</b>',
          'El negocio que sólo quiere dejar de perder turnos por no contestar a tiempo. '
          'El cliente elige de un menú de botones y reserva. Rápido, prolijo y sin vueltas.'],
         ['<b>Profesional</b>', '<b>USD 700</b>',
          'El que quiere que parezca una persona. El cliente escribe como habla, el bot '
          'entiende, recomienda, lo llama por su nombre y le hace seguimiento después. '
          'Además recupera a los que dejaron de venir.'],
         ['<b>Completo</b>', '<b>USD 1.000</b>',
          'El que además vende productos y cobra por WhatsApp. Suma catálogo, carrito, '
          'control de stock, lista de espera, paquetes de sesiones y cobros con '
          'Mercado Pago.']],
        anchos=[15, 15, 70])
    d.importante(
        'El plan <b>Profesional</b> es el que recomendamos para la mayoría de los '
        'negocios: es el que convierte al bot en algo que parece una persona, y no en '
        'un menú telefónico.',
        'LA RECOMENDACIÓN')
    d.titulo3('Se puede empezar por abajo y subir después')
    d.parrafo(
        'Los planes son acumulativos. Si arrancás con el Esencial y más adelante '
        'querés pasar al Profesional, se abona únicamente la diferencia. No se rehace '
        'nada ni se pierde lo configurado.')

    d.salto()

    d.seccion('', 'Qué incluye cada plan')
    d.tabla(
        ['Función', 'Esencial', 'Profesional', 'Completo'],
        [[f, a, b, c] for f, a, b, c in FUNCIONES],
        anchos=[58, 14, 14, 14])

    d.salto()

    # ------------------------------------------------------------------ 03
    d.seccion('03', 'Mantenimiento y soporte',
              'WhatsApp cambia políticas, las plataformas rotan credenciales y los '
              'negocios cambian precios y horarios. El abono mensual cubre que todo '
              'eso no rompa el sistema.')
    d.tabla(
        ['Concepto', 'Modalidad', 'USD'],
        [['Monitoreo, actualizaciones, ajustes de textos, cambios de precios y '
          'horarios, y resolución de incidentes con prioridad',
          'Mensual · opcional', '<b>50</b>']],
        anchos=[62, 26, 12])
    d.titulo3('Si no se contrata el mantenimiento mensual')
    d.parrafo(
        'Cada intervención se cotiza por separado, y la tarifa depende de la índole '
        'del problema: no es lo mismo un ajuste de texto que una caída del servicio o '
        'un cambio de políticas de WhatsApp que obligue a rehacer una integración. El '
        'abono mensual cubre todo eso sin costo adicional y con prioridad de atención.')

    # ------------------------------------------------------------------ 04
    d.seccion('04', 'Requisitos para funcionar',
              'Son condiciones de las plataformas, no decisiones nuestras. Conviene '
              'resolverlas antes de empezar la implementación.')
    d.titulo3('La línea de WhatsApp debe ser exclusiva del chatbot')
    d.parrafo(
        'El número que se conecte al sistema queda dedicado únicamente al chatbot. Al '
        'registrarlo en la API de WhatsApp, ese número deja de poder usarse con la '
        'aplicación normal: no se pueden leer ni enviar mensajes desde el celular.')
    d.parrafo(
        'Por eso no puede ser el número personal ni el que el negocio usa hoy para '
        'hablar con los clientes. Hay que dar de alta una línea nueva, destinada sólo '
        'a esto.')
    d.vinetas([
        'Línea telefónica nueva, que nunca haya tenido WhatsApp instalado.',
        'Cuenta de Meta Business con verificación de empresa: CUIT y constancia de '
        'inscripción.',
        'Cuenta de Google para el calendario donde se agendan los turnos.',
        'Tarjeta de crédito internacional para las plataformas que se abonan en dólares.'])
    d.importante(
        'Meta demora entre 1 y 15 días hábiles en verificar una empresa. Sin ese '
        'trámite el número queda limitado y no puede escribirle a cualquier cliente. '
        'Es el paso que conviene iniciar primero, porque no depende de nosotros.',
        'LA VERIFICACIÓN LLEVA TIEMPO')

    d.salto()

    # ------------------------------------------------------------------ 05
    d.seccion('05', 'Costos de funcionamiento',
              'Además del desarrollo, el sistema necesita servicios de terceros para '
              'funcionar. Los contrata y abona directamente el negocio, a nombre '
              'propio. Hay dos formas de resolverlo.')
    d.titulo3('Opción A · Servidor propio')
    d.parrafo(
        'El motor de automatización corre en un servidor privado (VPS) a nombre del '
        'negocio. Es la opción más económica a largo plazo y sin límites de uso.')
    d.tabla(
        ['Concepto', 'Detalle', 'USD / mes'],
        [['Servidor VPS', '8 GB RAM · uso ilimitado', '9'],
         ['WhatsApp Business API', 'Meta · según volumen de mensajes', '24'],
         ['Inteligencia artificial', 'Claude API · procesamiento de mensajes', '7'],
         ['Base de datos', 'Plan gratuito', '0'],
         ['Meta Business', 'Cuenta de empresa', '0'],
         ['Dominio', 'Subdominio propio del negocio', '1'],
         ['<b>Total mensual</b>', '', '<b>USD 41</b>']],
        anchos=[30, 55, 15])
    d.parrafo('Costo único adicional: línea telefónica nueva, aproximadamente USD 8.',
              'chico')

    d.titulo3('Opción B · Plataforma en la nube')
    d.parrafo(
        'Sin servidor propio: el motor corre en la nube y se contrata como un servicio '
        'mensual más. No requiere mantener un servidor, pero se paga por volumen de uso.')
    d.tabla(
        ['Concepto', 'Detalle', 'USD / mes'],
        [['Plataforma en la nube', 'Plan según volumen de operaciones', '60 – 120'],
         ['WhatsApp Business API', 'Meta · según volumen de mensajes', '24'],
         ['Inteligencia artificial', 'Claude API · procesamiento de mensajes', '7'],
         ['Base de datos', 'Plan gratuito', '0'],
         ['Meta Business', 'Cuenta de empresa', '0'],
         ['<b>Total mensual</b>', '', '<b>USD 91 – 151</b>']],
        anchos=[30, 55, 15])
    d.importante(
        'La Opción A cuesta menos de la mitad y no tiene techo de uso: la diferencia es '
        'de USD 600 a 1.320 por año, con exactamente las mismas funciones. La Opción B '
        'tiene sentido sólo si el negocio prefiere no tener ningún servidor a su nombre.',
        'LA RECOMENDACIÓN')

    d.salto()

    # ------------------------------------------------------------------ 06
    d.seccion('06', 'Cómo cobra Meta los mensajes',
              'Meta no cobra una mensualidad por WhatsApp: cobra por mensaje enviado, y '
              'el precio cambia según la categoría del mensaje. La categoría no la '
              'elige el negocio: la asigna Meta al revisar cada plantilla.')
    d.tabla(
        ['Categoría', 'Cuándo se usa', 'Costo'],
        [['<b>Servicio</b>', 'Todo lo que el chatbot responde dentro de las 24 h desde '
          'que el cliente escribió', 'Sin cargo'],
         ['<b>Utilidad</b>', 'Confirmaciones, recordatorios y avisos sobre algo que el '
          'cliente ya hizo', 'Bajo'],
         ['<b>Marketing</b>', 'Promociones, reactivación de clientes inactivos y '
          'pedidos de reseña', 'El más alto']],
        anchos=[18, 62, 20])
    d.importante(
        'La ventana de 24 horas es lo que define la factura. Mientras la conversación '
        'la inicie el cliente, todo lo que el chatbot conteste durante las 24 horas '
        'siguientes no tiene costo por mensaje. El cargo aparece únicamente cuando el '
        'negocio escribe primero: un recordatorio de turno, una promoción, un aviso de '
        'pedido listo.')
    d.parrafo(
        'Por eso la mayor parte del uso diario de un chatbot de atención es gratuita: '
        'el cliente pregunta y el bot responde. Lo que se paga son los mensajes que '
        'salen por iniciativa del negocio.')

    d.salto()

    d.seccion('', 'Cosas que conviene saber de antemano')
    d.vinetas([
        '<b>La clasificación la decide Meta y puede cambiarla después.</b> Una plantilla '
        'enviada como utilidad puede quedar como marketing, y su costo sube sin que el '
        'negocio haya modificado nada. Ya nos pasó durante el desarrollo: dos plantillas '
        'de seguimiento post-tratamiento fueron reclasificadas.',
        '<b>Los mensajes de marketing exigen consentimiento.</b> Sólo se le pueden enviar '
        'a quien lo aceptó de forma explícita. El sistema ya lo controla: si no hay '
        'consentimiento, el envío se cancela solo en vez de mandarse. El cliente puede '
        'darse de baja respondiendo BAJA.',
        '<b>Si el cliente no responde, la ventana se cierra.</b> Pasadas las 24 horas '
        'desde su último mensaje, para volver a escribirle hace falta una plantilla '
        'paga. Por eso el chatbot está pensado para resolver la consulta mientras la '
        'conversación está viva.',
        '<b>La tarifa depende del país del cliente.</b> Argentina tiene la suya. Y los '
        'descuentos por volumen de Meta aplican sólo a los mensajes de utilidad: los de '
        'marketing pagan tarifa plena siempre.',
        '<b>Meta anunció un cambio para el 1 de octubre de 2026:</b> los mensajes de '
        'servicio y de utilidad dentro de la ventana de 24 horas dejarían de ser '
        'gratuitos. Conviene reconfirmar la tarifa vigente al momento de contratar.'])

    d.seccion('', 'Cada mensaje automático necesita aprobación')
    d.parrafo(
        'Todo mensaje que el negocio envíe por iniciativa propia —recordatorios, '
        'confirmaciones, promociones— tiene que estar aprobado por Meta antes de poder '
        'usarse. Se envía el texto a revisión una sola vez y queda habilitado para '
        'siempre.')
    d.parrafo(
        'Los tiempos habituales son de 30 minutos a 2 horas para los mensajes de '
        'utilidad y de 2 a 6 horas para los de marketing. Si la revisión automática no '
        'alcanza, pasa a revisión humana y puede demorar hasta 48 horas. El chatbot '
        'atiende consultas desde el primer día, pero los mensajes automáticos se '
        'habilitan cuando Meta termina de revisar.')
    d.parrafo(
        'Un rechazo no es un problema: se corrige y se reenvía sin costo ni penalidad. '
        'El motivo más común es haber elegido la categoría equivocada.', 'chico')

    d.salto()

    # ------------------------------------------------------------------ 07
    d.seccion('07', 'Sobre la inteligencia artificial',
              'En los planes Profesional y Completo, la IA se puede desactivar y eso '
              'baja el costo mensual en USD 7. Conviene saber qué se pierde antes de '
              'decidirlo.')
    d.tabla(
        ['Con inteligencia artificial', 'Sin inteligencia artificial'],
        [['Entiende lo que el cliente escribe en sus propias palabras',
          'Sólo funciona con menús de botones'],
         ['Recomienda servicios según el problema que le cuenta', 'No puede recomendar nada'],
         ['Responde consultas de precios y de cómo trabaja el negocio',
          'Deriva a una persona todo lo que no sea un botón'],
         ['Recuerda lo que venían hablando', 'Cada mensaje arranca de cero'],
         ['Detecta casos delicados y deriva sola',
          'El cliente tiene que pedir hablar con alguien']],
        anchos=[50, 50])
    d.parrafo(
        'Sin IA el chatbot sigue agendando, cancelando y tomando pedidos correctamente. '
        'Lo que pierde es la conversación: deja de parecer una persona y pasa a ser un '
        'menú telefónico. Por USD 7 al mes, recomendamos mantenerla.')

    # ------------------------------------------------------------------ 08
    d.seccion('08', 'Funciones que se cotizan aparte',
              'No están incluidas en ningún plan. Se pueden sumar cuando el negocio las '
              'necesite.')
    d.tabla(
        ['Función', 'En qué consiste'],
        [['Chatbot en Instagram', 'El mismo asistente respondiendo los mensajes directos '
                                  'de Instagram, con la misma agenda.'],
         ['Varias sucursales', 'Manejo de más de un local, con agendas, profesionales y '
                               'catálogos independientes.'],
         ['Panel web para el equipo', 'Pantalla propia para ver y gestionar turnos, '
                                      'clientes y pedidos sin usar Google Calendar.'],
         ['Integración con sistemas propios', 'Conexión con el sistema de gestión, '
                                              'facturación o CRM que el negocio ya use.']],
        anchos=[30, 70])

    d.seccion('', 'Sobre los costos de terceros')
    d.parrafo(
        'Los servicios de terceros —servidor, WhatsApp Business API, inteligencia '
        'artificial, base de datos y línea telefónica— se contratan y abonan '
        'directamente por el negocio, a nombre propio. Zyntra no interviene en esos '
        'pagos ni los intermedia.')
    d.parrafo(
        'En el plan Completo, Mercado Pago cobra además una comisión aproximada del '
        '6,29% + IVA sobre cada operación cobrada. Los importes de esta propuesta son '
        'estimaciones según las tarifas vigentes y pueden variar si las plataformas '
        'actualizan sus precios.', 'chico')

    d.cierre(
        '¿Avanzamos?',
        'Quedamos a disposición para resolver cualquier duda y coordinar la puesta en '
        'marcha. Si querés, arrancamos por una llamada de veinte minutos para ver qué '
        'plan te conviene según lo que te preguntan todos los días.')
    return d.guardar()
