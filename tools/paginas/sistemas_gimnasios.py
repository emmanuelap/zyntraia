# -*- coding: utf-8 -*-
"""Pagina de servicio: software de administracion para gimnasios."""

PAGINA = {
    'slug': 'sistemas-gimnasios',
    'migas': 'Sistemas para gimnasios',
    'icono': 'fitness_center',

    'titulo': 'Software de gestión para gimnasios y centros fitness | Zyntra',
    'descripcion': ('Sistema de administración para gimnasios: socios, planes, cuotas, reservas de clases, '
                    'check-in por QR y facturación AFIP en un solo panel.'),

    'h1': 'Software de gestión para gimnasios y centros fitness',
    'bajada': ('Socios, planes, vencimientos y reservas de clases en un panel. Con app propia para el '
               'socio y check-in por QR en la puerta.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20un%20sistema%20para%20mi%20gimnasio.',

    'servicio': {
        'nombre': 'Sistema de administración para gimnasios',
        'tipo': 'Software de gestión para centros deportivos',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'La plata que se pierde no se ve',
            'parrafos': [
                'En un gimnasio la pérdida más grande casi nunca es un robo ni un gasto grande. Son los '
                'vencimientos que nadie miró: el socio que dejó de pagar hace seis semanas y sigue '
                'entrando, el plan que venció y no se renovó porque nadie le avisó.',
                'Con planillas eso no se ve, porque para verlo alguien tiene que sentarse a revisarlas. Y '
                'cuando el mostrador está lleno, nadie se sienta a revisar nada.',
                'La otra pérdida es la baja silenciosa. El socio que dejó de venir hace tres semanas '
                'todavía es recuperable; el que dejó hace tres meses ya no. La diferencia es tener el dato '
                'a tiempo.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Qué maneja el sistema',
            'items': [
                {'icono': 'badge', 'titulo': 'Socios y planes',
                 'texto': 'Estado de cuenta, plan activo, créditos disponibles y vencimiento a la vista. '
                          'Quién pagó, quién debe y a quién le vence esta semana.'},
                {'icono': 'apps', 'titulo': 'Disciplinas y horarios',
                 'texto': 'Musculación, pilates, yoga, funcional, artes marciales, natación. Cada '
                          'disciplina con su grilla, su cupo y su profesor, sin superposiciones.'},
                {'icono': 'event_available', 'titulo': 'Reserva de clases',
                 'texto': 'El socio reserva desde el celular sobre el cupo real, con lista de espera '
                          'cuando la clase se llena.'},
                {'icono': 'qr_code_2', 'titulo': 'Check-in por QR',
                 'texto': 'Entrada por código en la puerta, con validación del estado de cuota. También '
                          'soporta huella biométrica.'},
                {'icono': 'payments', 'titulo': 'Cobros y vencimientos',
                 'texto': 'Cuotas con recordatorio automático antes de vencer, que es cuando todavía se '
                          'recupera al socio.'},
                {'icono': 'receipt_long', 'titulo': 'Facturación AFIP',
                 'texto': 'Comprobantes con CAE real emitidos desde el mismo sistema donde cobrás.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Stratos, en producción',
            'pasos': [
                {'titulo': 'Stratos Admin',
                 'texto': 'El panel de administración: socios, planes por disciplina, reservas, cobros, '
                          'facturación y analytics. Multi-gimnasio y multi-idioma.'},
                {'titulo': 'Stratos Mobile',
                 'texto': 'App nativa para iOS y Android para el socio: plan activo, créditos en tiempo '
                          'real, reserva de clases y check-in por QR.'},
                {'titulo': 'Rutinas y nutrición',
                 'texto': 'Rutinas de entrenamiento asignadas por el profesor, calculadores de nutrición y '
                          'cronómetro de entrenamiento con historial.'},
                {'titulo': 'Comunidad',
                 'texto': 'Chat grupal, eventos y avisos, para que la comunicación con los socios no viva '
                          'en un grupo de WhatsApp de doscientas personas.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'No hace falta cambiar todo de golpe',
            'parrafos': [
                'Casi nadie empieza usando el sistema completo. Se arranca por donde más duele, que '
                'normalmente es el control de socios y vencimientos, y el resto se suma después.',
                'Migramos lo que ya tenés cargado: el padrón de socios, los planes vigentes, los pagos al '
                'día. Empezar de cero es la forma más rápida de que el equipo del mostrador vuelva a la '
                'planilla en dos semanas.',
                'Podés ver las capturas del panel y de la app en la '
                '<a class="text-primary underline-offset-4 hover:underline" href="../#proyectos">sección de '
                'proyectos</a>, y si tu caso no es un gimnasio pero se parece, mirá '
                '<a class="text-primary underline-offset-4 hover:underline" href="../software-gestion/">software '
                'de gestión a medida</a>.',
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre sistemas para gimnasios',
            'preguntas': [
                {'q': '¿Sirve para un gimnasio chico?',
                 'a': 'Depende de cuántos socios lleves y de cómo. Con treinta socios y una planilla que '
                      'mirás todos los días, quizás no lo necesitás todavía. Con ciento cincuenta, la '
                      'planilla ya te está costando plata en vencimientos que nadie vio. El punto de '
                      'quiebre suele estar en cuando ya no podés recordar de memoria quién debe.'},
                {'q': '¿Los socios tienen que descargarse una app?',
                 'a': 'Es opcional. La app suma bastante para reservar clases y ver el estado de cuenta, '
                      'pero el sistema funciona igual sin ella: el mostrador carga todo y el check-in puede '
                      'hacerse con un QR impreso o con huella. Conviene no forzar la app el primer mes, '
                      'porque el socio que la instala obligado la borra.'},
                {'q': '¿Puedo cobrar las cuotas automáticamente?',
                 'a': 'Sí, con link de pago y recordatorio automático antes del vencimiento. El '
                      'recordatorio es lo que más recupera: buena parte de la morosidad en gimnasios no es '
                      'falta de plata, es que la persona se olvidó y le da vergüenza aparecer debiendo.'},
                {'q': '¿Maneja varias sedes?',
                 'a': 'Sí, está pensado multi-gimnasio desde el diseño. Cada sede con sus disciplinas, sus '
                      'horarios y su equipo, y una vista consolidada arriba. Si tenés una sola sede no '
                      'molesta, y el día que abrís la segunda no hay que rehacer nada.'},
                {'q': '¿Qué pasa con los datos de mis socios?',
                 'a': 'Son tuyos y la base es exportable. Vale la pena preguntarlo en cualquier plataforma '
                      'de gimnasios antes de contratar: varias se quedan con la relación con el socio, y el '
                      'día que querés cambiar de proveedor descubrís que no te llevás ni los teléfonos.'},
            ],
            'mas': [
                ('como-llevo-el-control-de-socios-de-mi-gimnasio',
                 '¿Cómo llevo el control de socios de mi gimnasio?'),
                ('puedo-cobrar-cuotas-mensuales-automaticamente',
                 '¿Puedo cobrar cuotas mensuales automáticamente?'),
                ('que-es-un-sistema-de-gestion-a-medida', '¿Qué es un sistema de gestión a medida?'),
                ('como-hago-un-sistema-de-turnos-online-para-mi-negocio',
                 '¿Cómo hago un sistema de turnos online para mi negocio?'),
                ('que-es-un-panel-de-indicadores-y-para-que-sirve',
                 '¿Qué es un panel de indicadores y para qué sirve?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero el sistema para mi gimnasio',
        'titulo': 'Contanos cómo llevás los socios hoy',
        'texto': ('En 20 minutos vemos cuántos vencimientos se te están pasando y qué haría falta para '
                  'controlarlos. El diagnóstico queda para vos aunque no contrates.'),
    },
}
