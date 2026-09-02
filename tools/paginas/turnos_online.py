# -*- coding: utf-8 -*-
"""Pagina de servicio: sistema de turnos y reservas online."""

PAGINA = {
    'slug': 'turnos-online',
    'migas': 'Turnos online',
    'icono': 'event_available',

    'titulo': 'Sistema de turnos online para tu negocio | Zyntra',
    'descripcion': ('Sistema de turnos y reservas online a medida: tus clientes reservan solos las 24 horas, '
                    'con recordatorios automáticos y agenda conectada a Google Calendar. Argentina.'),

    'h1': 'Sistema de turnos y reservas online',
    'bajada': ('Tus clientes reservan solos, a cualquier hora, sin que nadie tenga que atender el teléfono. '
               'Con recordatorio automático, que es lo que de verdad baja las ausencias.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20un%20sistema%20de%20turnos%20online.',

    'servicio': {
        'nombre': 'Sistema de turnos y reservas online',
        'tipo': 'Desarrollo de software de turnos y reservas',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'Los turnos se pierden en dos lugares',
            'parrafos': [
                'El primero es el horario. La persona decide sacar turno a las once de la noche, te '
                'escribe, y para cuando contestás a la mañana siguiente ya resolvió en otro lado. Ese '
                'turno no se perdió por precio ni por calidad: se perdió por doce horas de demora.',
                'El segundo es la ausencia. El turno quedó agendado, el horario quedó bloqueado, y la '
                'persona no vino. No suele ser mala fe: se olvidó. Un recordatorio el día antes '
                'recupera buena parte de eso, y es lo primero que dejamos automático.',
                'Un sistema de turnos no es una agenda más linda. Es sacar esas dos pérdidas del medio.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Qué resuelve',
            'items': [
                {'icono': 'event_available', 'titulo': 'Reserva sin intermediarios',
                 'texto': 'El cliente entra, ve la disponibilidad real y elige. No hay ida y vuelta de '
                          'mensajes para acordar un horario.'},
                {'icono': 'campaign', 'titulo': 'Recordatorio automático',
                 'texto': 'Aviso antes del turno por WhatsApp o email, sin que nadie tenga que acordarse '
                          'de mandarlo. Es la función que más se nota.'},
                {'icono': 'apps', 'titulo': 'Varios profesionales o cabinas',
                 'texto': 'Cada uno con su agenda, sus servicios y sus horarios. La disponibilidad se '
                          'calcula por recurso, no para todo el negocio junto.'},
                {'icono': 'autorenew', 'titulo': 'Cancelación y reprogramación',
                 'texto': 'El cliente puede mover su turno solo, dentro de las reglas que definas, y el '
                          'horario se libera para otro.'},
                {'icono': 'event_available', 'titulo': 'Google Calendar',
                 'texto': 'Cada reserva crea el evento real en el calendario donde ya trabajás. No hay '
                          'dos agendas que se contradicen.'},
                {'icono': 'payments', 'titulo': 'Seña opcional',
                 'texto': 'Cobro de una seña al reservar para los rubros donde la ausencia duele. '
                          'Se conecta con Mercado Pago.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo lo armamos',
            'pasos': [
                {'titulo': 'Mapeamos tu agenda real',
                 'texto': 'Duración de cada servicio, descansos, feriados, quién atiende qué. Acá se '
                          'define casi todo: un sistema que no respeta cómo trabajás no se usa.'},
                {'titulo': 'Reglas de reserva',
                 'texto': 'Con cuánta anticipación se puede sacar turno, hasta cuándo se puede cancelar, '
                          'si hace falta seña, cuántos turnos por persona.'},
                {'titulo': 'Conexión con lo que ya usás',
                 'texto': 'Google Calendar, WhatsApp para los avisos y Mercado Pago si va seña. Sin '
                          'obligarte a mudar todo a una herramienta nueva.'},
                {'titulo': 'Prueba con turnos reales',
                 'texto': 'Arranca funcionando en paralelo unos días antes de reemplazar el método viejo. '
                          'Así los errores aparecen sin costo.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Ya lo tenemos andando',
            'parrafos': [
                'Mini Turnos App es nuestro sistema de turnos personalizable por rubro, en producción. '
                'Y el módulo de reservas de Stratos Admin maneja clases con cupo, lista de espera y '
                'check-in por QR para gimnasios.',
                'Los dos casos enseñan lo mismo: el problema nunca es mostrar un calendario. Es que la '
                'disponibilidad que muestra sea la verdadera, con todas las excepciones del negocio '
                'adentro. Podés ver las capturas en la '
                '<a class="text-primary underline-offset-4 hover:underline" href="../#proyectos">sección '
                'de proyectos</a>.',
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre turnos online',
            'preguntas': [
                {'q': '¿Sirve si atiendo pocos clientes por día?',
                 'a': 'Depende de dónde se te va el tiempo, no de cuántos turnos das. Si atendés diez '
                      'personas por día pero coordinás cada una por chat, el sistema te devuelve tiempo '
                      'igual. Si tenés tres turnos por semana y los agendás sin esfuerzo, no te hace falta '
                      'y te lo decimos.'},
                {'q': '¿Qué pasa si un cliente no sabe usar el sistema?',
                 'a': 'Sigue existiendo el camino de siempre. La reserva online no reemplaza al teléfono '
                      'ni al WhatsApp: convive. Vos cargás ese turno a mano y ocupa el mismo lugar en la '
                      'agenda. Lo que cambia es que ahora hay una sola agenda, no dos.'},
                {'q': '¿Puedo bloquear horarios cuando se me complica?',
                 'a': 'Sí, y es lo que más se usa en la práctica. Podés bloquear un rato, un día entero o '
                      'una franja fija todas las semanas, y podés hacerlo desde el celular. Si el bloqueo '
                      'sale del calendario que ya usás, mejor todavía: se hace donde ya tenés la costumbre.'},
                {'q': '¿Se puede cobrar una seña al reservar?',
                 'a': 'Sí, con Mercado Pago. Conviene pensarlo bien igual: la seña baja mucho las '
                      'ausencias pero también frena a algunos clientes nuevos. En varios rubros funciona '
                      'mejor pedir seña solo en los horarios más buscados o a quien ya faltó una vez.'},
                {'q': '¿Los datos de mis clientes quedan míos?',
                 'a': 'Sí. El sistema es tuyo y la base también, exportable cuando quieras. Es algo que '
                      'conviene revisar antes de contratar cualquier plataforma de turnos: varias se '
                      'quedan con la relación con tu cliente, y el día que te vas no te llevás nada.'},
            ],
            'mas': [
                ('como-hago-un-sistema-de-turnos-online-para-mi-negocio',
                 '¿Cómo hago un sistema de turnos online para mi negocio?'),
                ('como-evito-que-los-clientes-falten-al-turno',
                 '¿Cómo evito que los clientes falten al turno?'),
                ('como-tomo-reservas-si-tengo-varios-profesionales-o-cabinas',
                 '¿Cómo tomo reservas si tengo varios profesionales o cabinas?'),
                ('puedo-conectar-los-turnos-con-mi-google-calendar',
                 '¿Puedo conectar los turnos con mi Google Calendar?'),
                ('se-pueden-tomar-turnos-automaticamente-por-whatsapp',
                 '¿Se pueden tomar turnos automáticamente por WhatsApp?'),
                ('sirve-un-sistema-de-turnos-si-atiendo-pocos-clientes',
                 '¿Sirve un sistema de turnos si atiendo pocos clientes?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero turnos online',
        'titulo': 'Contanos cómo llevás la agenda hoy',
        'texto': ('En 20 minutos vemos cuántos turnos estás perdiendo por horario y por ausencias, y qué '
                  'costaría resolverlo. El diagnóstico queda para vos aunque no contrates.'),
    },
}
