# -*- coding: utf-8 -*-
"""
Caso de exito: Stratos.

Cifras confirmadas por el dueno: 72 gimnasios y alrededor de 8.900 usuarios.
No agregar ninguna otra cifra sin que el la confirme.
"""

PAGINA = {
    'slug': 'casos-de-exito/stratos-gimnasios',
    'padre': {'slug': 'casos-de-exito', 'nombre': 'Casos de éxito'},
    'migas': 'Stratos',
    'icono': 'fitness_center',

    'titulo': 'Caso Stratos: 72 gimnasios y 8.900 usuarios | Zyntra',
    'descripcion': ('Cómo Stratos administra 72 gimnasios y alrededor de 8.900 usuarios: socios, planes, '
                    'reservas con check-in por QR, cobros y facturación AFIP en un solo sistema.'),

    'h1': 'Stratos: 72 gimnasios y 8.900 usuarios en un solo sistema',
    'bajada': ('Un sistema de gestión que arrancó resolviendo el control de socios de un gimnasio y hoy '
               'administra 72, con app propia para el socio y facturación AFIP integrada.'),

    'wa': 'Hola%20Zyntra%2C%20vi%20el%20caso%20de%20Stratos%20y%20quiero%20algo%20as%C3%AD.',

    'servicio': {
        'nombre': 'Stratos, sistema de administración para gimnasios',
        'tipo': 'Software de gestión para centros deportivos',
    },

    'secciones': [
        {
            'tipo': 'cifras',
            'h2': 'Los números',
            'intro': 'Datos reales del sistema en producción, no proyecciones.',
            'numeros': [
                {'cifra': '72', 'titulo': 'Gimnasios',
                 'detalle': 'Cada uno con sus disciplinas, sus horarios, sus planes y su equipo.'},
                {'cifra': '8.900', 'titulo': 'Usuarios',
                 'detalle': 'Socios administrados en total entre todas las sedes.'},
                {'cifra': 'CAE real', 'titulo': 'Facturación AFIP',
                 'detalle': 'Comprobantes autorizados contra los servicios reales de AFIP.'},
                {'cifra': 'iOS + Android', 'titulo': 'App del socio',
                 'detalle': 'Aplicación nativa con reserva de clases y check-in por QR.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'El problema',
            'parrafos': [
                'Un gimnasio con varios cientos de socios pierde plata en un lugar que no aparece en '
                'ningún reporte: los vencimientos que nadie miró. El socio que dejó de pagar hace seis '
                'semanas y sigue entrando, el plan que venció sin que nadie avisara, la baja silenciosa '
                'del que hace un mes que no aparece.',
                'Con planillas eso no se ve, porque para verlo alguien tiene que sentarse a revisarlas. Y '
                'cuando el mostrador está lleno, nadie se sienta a revisar nada.',
                'A eso se sumaba lo de siempre: la grilla de clases en un cuaderno, los cupos negociados '
                'por WhatsApp, y la facturación cargada a mano en el portal de AFIP al final del día.',
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Qué construimos',
            'pasos': [
                {'titulo': 'Socios y planes',
                 'texto': 'Estado de cuenta, plan activo, créditos y vencimiento a la vista. Quién pagó, '
                          'quién debe y a quién le vence esta semana.'},
                {'titulo': 'Reservas y check-in',
                 'texto': 'Clases con cupo real y lista de espera, y entrada por QR con validación del '
                          'estado de cuota. También por huella.'},
                {'titulo': 'Cobros y facturación',
                 'texto': 'Cuotas con recordatorio antes del vencimiento, y comprobantes con CAE real '
                          'emitidos desde el mismo sistema donde se cobra.'},
                {'titulo': 'App del socio',
                 'texto': 'Nativa para iOS y Android: plan activo, créditos en tiempo real, reserva de '
                          'clases, rutinas y cronómetro de entrenamiento.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Por qué llegó a 72 gimnasios',
            'parrafos': [
                'Porque se diseñó multi-sede desde el primer día, no después. Cada gimnasio tiene sus '
                'disciplinas, sus horarios, sus planes y su equipo, con una vista consolidada arriba. Ese '
                'es el motivo de que sumar la sede número setenta no requiera rehacer nada.',
                'Y porque es multi-idioma, lo que abrió la puerta a instalaciones fuera del país sin '
                'tocar el código.',
                'El aprendizaje que nos llevamos es sobre la migración. Ningún gimnasio arranca de cero: '
                'llega con su padrón, sus planes vigentes y sus pagos al día en una planilla que hay que '
                'importar. Esa etapa es la que más se subestima y la que decide si el equipo del '
                'mostrador adopta el sistema o vuelve al cuaderno en dos semanas.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Lo mismo, para otro rubro',
            'parrafos': [
                'La arquitectura de Stratos sirve para cualquier negocio con socios, turnos, cupos, '
                'cobros recurrentes y facturación. Cambia el vocabulario, no el sistema: donde dice '
                'disciplina puede decir servicio, y donde dice socio puede decir cliente.',
                'Si tenés un gimnasio, la página del servicio es '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@sistemas-gimnasios/">'
                'sistemas para gimnasios</a>. Si tu caso se parece pero no es un gimnasio, mirá '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@software-gestion/">'
                'software de gestión a medida</a>.',
                'Podés ver las capturas del panel y de la app en la '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@#proyectos">'
                'sección de proyectos</a>.',
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero algo así para mi negocio',
        'titulo': 'Contanos cómo llevás tus socios hoy',
        'texto': ('En 20 minutos vemos qué parte de Stratos aplica a tu caso y qué habría que construir '
                  'desde cero. El diagnóstico queda para vos aunque no contrates.'),
    },
}
