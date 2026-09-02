# -*- coding: utf-8 -*-
"""Pagina de servicio: control de accesos por QR."""

PAGINA = {
    'slug': 'accesos-qr',
    'migas': 'Accesos por QR',
    'icono': 'qr_code_2',

    'titulo': 'Control de acceso por QR para gimnasios y edificios | Zyntra',
    'descripcion': ('Control de ingreso con código QR único por persona: gimnasios, oficinas, eventos y '
                    'edificios. Con registro automático y bloqueo por cuota vencida.'),

    'h1': 'Control de acceso por QR',
    'bajada': ('Un código único por persona, sin llaves ni tarjetas. Con registro de cada ingreso y '
               'bloqueo automático de quien tiene la cuota vencida.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20control%20de%20acceso%20por%20QR.',

    'servicio': {
        'nombre': 'Control de acceso por código QR',
        'tipo': 'Sistemas de control de ingreso',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'La puerta es donde se pierde el control',
            'parrafos': [
                'En cualquier lugar con socios o personal, la puerta es el punto donde se juntan dos '
                'problemas: no queda registro de quién entró, y entra quien no debería.',
                'Lo segundo suele ser sin mala intención. La persona con la cuota vencida hace tres '
                'semanas sigue entrando porque el de la puerta no tiene cómo saberlo, y a nadie le gusta '
                'frenar a alguien que viene todos los días.',
                'Lo primero se nota el día que hace falta: un incidente, un reclamo, una discusión sobre '
                'si alguien estuvo o no. Sin registro no hay conversación posible.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Dónde se usa',
            'items': [
                {'icono': 'fitness_center', 'titulo': 'Gimnasios y centros deportivos',
                 'texto': 'Ingreso con validación del estado de cuota en el momento. El que debe no entra '
                          'y nadie tuvo que decírselo en la cara.'},
                {'icono': 'work', 'titulo': 'Oficinas y coworking',
                 'texto': 'Acceso por persona con horarios permitidos, y registro de entrada y salida sin '
                          'reloj de fichar.'},
                {'icono': 'campaign', 'titulo': 'Eventos',
                 'texto': 'Entrada única por asistente, imposible de usar dos veces, con control de aforo '
                          'en vivo.'},
                {'icono': 'apps', 'titulo': 'Edificios y consorcios',
                 'texto': 'Acceso para residentes y códigos temporales para visitas o proveedores, con '
                          'vencimiento automático.'},
                {'icono': 'school', 'titulo': 'Instituciones',
                 'texto': 'Control de ingreso con registro por persona y por horario, útil para asistencia '
                          'y para seguridad.'},
                {'icono': 'loyalty', 'titulo': 'Fidelización',
                 'texto': 'El mismo código puede sumar puntos o beneficios en cada visita, sin app ni '
                          'tarjeta de plástico.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo funciona',
            'pasos': [
                {'titulo': 'Código único por persona',
                 'texto': 'Se genera con la identidad de cada uno. Vive en el celular o impreso, según '
                          'cómo trabajes.'},
                {'titulo': 'Lectura en la puerta',
                 'texto': 'Con un lector, una tablet o el celular de quien atiende. No hace falta hardware '
                          'caro para arrancar.'},
                {'titulo': 'Validación en el momento',
                 'texto': 'El sistema chequea si esa persona puede entrar ahora: cuota al día, horario '
                          'permitido, código no vencido.'},
                {'titulo': 'Registro automático',
                 'texto': 'Queda quién entró y cuándo, sin que nadie anote nada. Ese registro es la mitad '
                          'del valor del sistema.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Qué hardware hace falta',
            'parrafos': [
                'Menos del que la gente imagina. Se puede empezar con una tablet o un celular en el '
                'mostrador leyendo los códigos, sin instalar molinetes ni cerraduras electrónicas.',
                'Si más adelante querés que la puerta se abra sola, eso se suma después conectando el '
                'sistema a una cerradura o un molinete. Pero no es por donde conviene empezar: primero '
                'que el control funcione y que el registro sirva, después la automatización física.',
                'En gimnasios esto ya está andando dentro de '
                '<a class="text-primary underline-offset-4 hover:underline" href="../sistemas-gimnasios/">Stratos</a>, '
                'con check-in por QR y también por huella.',
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre control de acceso',
            'preguntas': [
                {'q': '¿Se puede copiar el código de otra persona?',
                 'a': 'Un QR estático impreso se puede fotografiar, sí. Por eso para los casos donde eso '
                      'importa se usan códigos que cambian cada pocos segundos en la app, o se combina con '
                      'un segundo factor como la huella. La decisión depende de cuánto duele que alguien '
                      'entre de más: en un gimnasio es un problema menor, en un evento pago es central.'},
                {'q': '¿Qué pasa si alguien se queda sin batería?',
                 'a': 'Tiene que haber siempre una salida manual, y la definimos desde el principio: el '
                      'de la puerta busca a la persona por nombre o documento y la deja pasar, y queda '
                      'registrado igual. Un sistema de acceso sin plan B genera más problemas de los que '
                      'resuelve.'},
                {'q': '¿Necesito internet en la puerta?',
                 'a': 'Conviene, porque la validación en tiempo real es lo que hace que el bloqueo por '
                      'cuota vencida funcione. Se puede armar con un modo de contingencia que registre los '
                      'ingresos y los sincronice después, pero durante ese rato el control es más flojo. '
                      'Si tu conexión es mala, hay que preverlo antes.'},
                {'q': '¿Puedo dar accesos temporales?',
                 'a': 'Sí, y es de lo que más se usa: un código para un proveedor que viene el martes, un '
                      'pase de prueba de una semana, la visita de un residente. Se genera con fecha de '
                      'vencimiento y se apaga solo, sin que nadie tenga que acordarse de darlo de baja.'},
                {'q': '¿Qué pasa con los datos de quién entra y sale?',
                 'a': 'Son datos personales y hay que tratarlos como tales. Se guardan por el tiempo que '
                      'tenga sentido, se accede solo desde los roles que corresponda, y las personas '
                      'tienen que saber que el registro existe. Es una obligación legal y además es lo '
                      'correcto.'},
            ],
            'mas': [
                ('como-controlo-el-ingreso-de-gente-con-qr', '¿Cómo controlo el ingreso de gente con QR?'),
                ('como-llevo-el-control-de-socios-de-mi-gimnasio',
                 '¿Cómo llevo el control de socios de mi gimnasio?'),
                ('puedo-cobrar-cuotas-mensuales-automaticamente',
                 '¿Puedo cobrar cuotas mensuales automáticamente?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero control de acceso',
        'titulo': 'Contanos cómo se controla la puerta hoy',
        'texto': ('En 20 minutos vemos qué hace falta para tu caso y con qué podés empezar sin comprar '
                  'hardware. El diagnóstico queda para vos aunque no contrates.'),
    },
}
