# -*- coding: utf-8 -*-
"""Pagina de servicio: software de gestion a medida."""

PAGINA = {
    'slug': 'software-gestion',
    'migas': 'Software de gestión',
    'icono': 'analytics',

    'titulo': 'Software de gestión a medida para pymes | Zyntra',
    'descripcion': ('Desarrollo de software de gestión a medida: clientes, stock, cobros, facturación y '
                    'paneles en un solo lugar. Para pymes y comercios en Argentina.'),

    'h1': 'Software de gestión a medida para tu negocio',
    'bajada': ('Cuando cada área tiene su Excel, nadie sabe cuál es el dato bueno. Centralizamos la '
               'operación en una herramienta hecha para cómo trabajás vos.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20un%20sistema%20de%20gesti%C3%B3n%20a%20medida.',

    'servicio': {
        'nombre': 'Software de gestión a medida',
        'tipo': 'Desarrollo de software de gestión para pymes',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'El Excel no es el problema. Las copias sí.',
            'parrafos': [
                'Casi todo negocio arranca con una planilla, y está bien: es rápida, es gratis y la '
                'entiende cualquiera. El problema aparece después, cuando son cinco planillas, cada una '
                'con su versión de la verdad, y alguien pregunta cuánto stock hay realmente.',
                'Ahí empiezan los síntomas conocidos. Se factura algo que no había. Dos personas cargan '
                'el mismo cobro. Nadie puede decir cuánto se vendió el mes pasado sin sentarse una tarde '
                'a cruzar archivos.',
                'Un sistema a medida no es una planilla con más botones. Es que el dato se cargue una '
                'sola vez y que todos miren el mismo.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Qué solemos incluir',
            'intro': 'No hace falta arrancar con todo. Se empieza por el módulo que más duele.',
            'items': [
                {'icono': 'badge', 'titulo': 'Clientes y contactos',
                 'texto': 'Ficha con historial completo: qué compró, qué se le hizo, cuándo fue la última '
                          'vez. Sin buscar en el chat.'},
                {'icono': 'shopping_bag', 'titulo': 'Stock e inventario',
                 'texto': 'Entradas, salidas y alertas de faltante. Con el stock descontándose solo cuando '
                          'se vende, que es donde se rompe el control manual.'},
                {'icono': 'payments', 'titulo': 'Cobros y cuentas corrientes',
                 'texto': 'Quién debe qué y desde cuándo. Con recordatorio automático antes de que la '
                          'deuda se haga vieja.'},
                {'icono': 'receipt_long', 'titulo': 'Facturación AFIP',
                 'texto': 'Comprobantes con CAE real, emitidos desde el mismo sistema donde cargás la '
                          'venta. Sin volver a tipear todo en el portal.'},
                {'icono': 'insights', 'titulo': 'Panel de indicadores',
                 'texto': 'Los cuatro o cinco números que de verdad usás para decidir, actualizados solos '
                          'y a la vista.'},
                {'icono': 'apps', 'titulo': 'Roles y permisos',
                 'texto': 'Que cada persona vea lo suyo. El mostrador no necesita ver la rentabilidad, y '
                          'vos no querés que la toque.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo trabajamos',
            'pasos': [
                {'titulo': 'Miramos cómo trabajás hoy',
                 'texto': 'Con las planillas y los cuadernos reales a la vista. Un sistema que ignora las '
                          'excepciones del negocio termina abandonado a los dos meses.'},
                {'titulo': 'Elegimos por dónde empezar',
                 'texto': 'Un solo módulo, el que más horas te come. Salir con algo chico que funcione es '
                          'mejor que esperar seis meses el sistema completo.'},
                {'titulo': 'Migramos tus datos',
                 'texto': 'Lo que ya tenés cargado entra al sistema. Empezar de cero es la forma más '
                          'rápida de que nadie lo use.'},
                {'titulo': 'Entrega documentada',
                 'texto': 'El sistema es tuyo, con la base exportable y la documentación de cómo está '
                          'hecho. Sin quedar atado a nosotros.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Stratos Admin, nuestro caso más grande',
            'parrafos': [
                'Stratos Admin es un sistema de gestión completo que está en producción: socios, planes '
                'por disciplina, reservas con check-in por QR, cobros, facturación AFIP con CAE real y '
                'panel de analytics. Es multi-gimnasio y multi-idioma.',
                'Está pensado para gimnasios, pero la arquitectura es la misma que usamos para cualquier '
                'negocio con socios, turnos, stock y cobros. Cambia el vocabulario, no el sistema.',
                'Podés ver las capturas del panel en la '
                '<a class="text-primary underline-offset-4 hover:underline" href="../#proyectos">sección '
                'de proyectos</a>, y si tenés un gimnasio mirá '
                '<a class="text-primary underline-offset-4 hover:underline" href="../#svc-gimnasios">el '
                'servicio armado para ese caso</a>.',
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre software de gestión',
            'preguntas': [
                {'q': '¿Conviene un sistema a medida o uno ya hecho?',
                 'a': 'Si lo que hacés se parece a lo que hacen todos en tu rubro, un sistema ya hecho es '
                      'más barato y sale mañana. El a medida se justifica cuando tu forma de trabajar es '
                      'la ventaja competitiva y ningún producto la contempla, o cuando terminás pagando '
                      'tres suscripciones que no se hablan entre sí. Te decimos honestamente en cuál de '
                      'los dos casos estás, aunque sea el primero.'},
                {'q': '¿Cuánto tarda?',
                 'a': 'Un módulo acotado y bien definido suele estar andando en semanas. El sistema '
                      'completo lleva meses, y por eso no lo hacemos de una: entregamos por partes para '
                      'que empieces a usar lo primero mientras se construye el resto. Lo que más alarga '
                      'los plazos no es programar, es que el negocio no tenga decidido cómo quiere '
                      'trabajar.'},
                {'q': '¿Qué pasa con los datos que ya tengo cargados?',
                 'a': 'Los migramos. Si están en Excel, en Google Sheets o en otro sistema con '
                      'exportación, entran. Suele ser el paso que más tiempo lleva y el que más se '
                      'subestima, porque los datos viejos siempre tienen inconsistencias que hay que '
                      'resolver una por una.'},
                {'q': '¿Necesito saber de computación para usarlo?',
                 'a': 'No, y si hace falta es que está mal diseñado. La prueba real es si la persona que '
                      'menos se lleva con la tecnología en tu equipo puede cargar una venta sin '
                      'preguntar. Eso lo probamos antes de entregar, no después.'},
                {'q': '¿Qué pasa si mañana no quiero trabajar más con ustedes?',
                 'a': 'Te quedás con todo: el código, la base de datos y la documentación. Es la pregunta '
                      'que más conviene hacer antes de contratar a cualquiera, y la respuesta debería ser '
                      'siempre esta. Si un proveedor no te la puede dar, ahí tenés la respuesta.'},
            ],
            'mas': [
                ('que-es-un-sistema-de-gestion-a-medida', '¿Qué es un sistema de gestión a medida?'),
                ('conviene-un-sistema-a-medida-o-uno-ya-hecho', '¿Conviene un sistema a medida o uno ya hecho?'),
                ('puedo-dejar-de-usar-excel-para-administrar-mi-negocio',
                 '¿Puedo dejar de usar Excel para administrar mi negocio?'),
                ('como-controlo-el-stock-de-mi-comercio', '¿Cómo controlo el stock de mi comercio?'),
                ('que-es-un-panel-de-indicadores-y-para-que-sirve',
                 '¿Qué es un panel de indicadores y para qué sirve?'),
                ('se-puede-integrar-la-facturacion-con-el-control-de-stock',
                 '¿Se puede integrar la facturación con el control de stock?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero ordenar mi operación',
        'titulo': 'Mostranos tus planillas',
        'texto': ('En 20 minutos identificamos qué tarea manual te está comiendo más horas por semana y '
                  'qué costaría automatizarla. El diagnóstico queda para vos aunque no contrates.'),
    },
}
