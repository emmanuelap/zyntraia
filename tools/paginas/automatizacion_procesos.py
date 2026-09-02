# -*- coding: utf-8 -*-
"""Pagina de servicio: automatizacion de procesos."""

PAGINA = {
    'slug': 'automatizacion-procesos',
    'migas': 'Automatización de procesos',
    'icono': 'hub',

    'titulo': 'Automatización de procesos para empresas | Zyntra',
    'descripcion': ('Automatización de tareas repetitivas: conectamos formularios, WhatsApp, correo, '
                    'planillas y sistemas para que el trabajo manual se ejecute solo. Argentina.'),

    'h1': 'Automatización de procesos con IA para empresas',
    'bajada': ('Todo lo que hoy alguien copia de un lado a otro se puede ejecutar solo. Sin olvidos, sin '
               'errores de tipeo y sin depender de que esa persona esté.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20automatizar%20procesos%20de%20mi%20empresa.',

    'servicio': {
        'nombre': 'Automatización de procesos e integraciones',
        'tipo': 'Automatización de procesos de negocio',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'El trabajo que no se ve en ningún reporte',
            'parrafos': [
                'Hay una categoría de tareas que nadie mide porque están repartidas: pasar un dato de un '
                'formulario a una planilla, copiar un pedido del WhatsApp al sistema, armar el mismo '
                'informe todos los lunes, mandar el mismo mensaje de seguimiento.',
                'Cada una lleva pocos minutos, y por eso nunca es urgente arreglarlas. Pero se hacen '
                'todos los días, y sumadas suelen equivaler a varias horas semanales de alguien a quien '
                'le estás pagando por otra cosa.',
                'El costo real no es el tiempo, igual. Es el error: el dato que se copió mal, el '
                'seguimiento que no se mandó, el pedido que se traspapeló. Eso no se recupera con horas '
                'extra.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Qué se automatiza más seguido',
            'intro': 'No es una lista cerrada. Es lo que más nos piden y lo que más rápido se paga solo.',
            'items': [
                {'icono': 'hub', 'titulo': 'Formularios que van a algún lado',
                 'texto': 'Lo que entra por la web cae directo en tu sistema, con aviso al que tiene que '
                          'responder. Sin revisar una casilla que nadie revisa.'},
                {'icono': 'chat', 'titulo': 'Seguimiento comercial',
                 'texto': 'El contacto que consultó y no volvió recibe el mensaje en el momento correcto, '
                          'sin que nadie lleve la cuenta.'},
                {'icono': 'campaign', 'titulo': 'Recordatorios y avisos',
                 'texto': 'Turnos, vencimientos, renovaciones, entregas. Todo lo que hoy depende de que '
                          'alguien se acuerde.'},
                {'icono': 'autorenew', 'titulo': 'Sincronización entre sistemas',
                 'texto': 'Que la venta cargada en un lado aparezca en el otro. Es el clásico "copiar y '
                          'pegar entre pestañas".'},
                {'icono': 'insights', 'titulo': 'Informes recurrentes',
                 'texto': 'El reporte de todos los lunes armado y enviado solo, con los números al día.'},
                {'icono': 'smart_toy', 'titulo': 'Clasificación con IA',
                 'texto': 'Leer un mensaje y decidir de qué se trata, a quién va y con qué urgencia. Es lo '
                          'que antes no se podía automatizar.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo lo encaramos',
            'pasos': [
                {'titulo': 'Buscamos la tarea, no la herramienta',
                 'texto': 'Primero identificamos qué se hace, cuántas veces por semana y quién lo hace. '
                          'Elegir la herramienta antes de entender la tarea es el error más caro.'},
                {'titulo': 'Empezamos por una sola',
                 'texto': 'La que más se repite o la que más errores genera. Una automatización andando '
                          'convence más que un plan de diez.'},
                {'titulo': 'La dejamos observable',
                 'texto': 'Tenés que poder ver qué hizo y cuándo. Una automatización que trabaja a ciegas '
                          'da más miedo del que saca.'},
                {'titulo': 'Con salida manual',
                 'texto': 'Siempre queda la forma de hacerlo a mano y de frenarla. Nada que no puedas '
                          'apagar un día que se complique.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Dónde la automatización no conviene',
            'parrafos': [
                'Vale la pena decirlo porque casi nadie lo dice. Automatizar un proceso que está mal '
                'diseñado lo único que hace es que las cosas salgan mal más rápido y a mayor escala. Si '
                'la tarea está desordenada, primero se ordena.',
                'Tampoco conviene automatizar lo que pasa tres veces al año. El costo de armarlo y '
                'mantenerlo se come cualquier ahorro, y encima el día que se usa nadie se acuerda de cómo '
                'funcionaba.',
                'Y hay decisiones que tienen que seguir siendo de una persona. La automatización sirve '
                'para juntar la información y dejarla lista; apretar el botón, en algunos casos, tiene '
                'que ser humano.',
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre automatización',
            'preguntas': [
                {'q': '¿Por dónde empiezo a automatizar mi negocio?',
                 'a': 'Por la tarea más repetida, no por la más molesta. Hacé el ejercicio una semana: '
                      'anotá cada vez que copiás un dato de un lugar a otro. La que más aparezca en esa '
                      'lista es por donde conviene arrancar, casi siempre. Y elegí una sola: diez '
                      'automatizaciones a medias no sirven para nada.'},
                {'q': '¿Sirve para un negocio chico?',
                 'a': 'Justamente ahí suele rendir más, porque en un negocio chico la persona que hace el '
                      'trabajo repetitivo sos vos. La diferencia es que en una empresa grande automatizás '
                      'para ahorrar sueldos y en una chica automatizás para recuperar tus propias horas, '
                      'que son las que necesitás para vender.'},
                {'q': '¿Qué pasa con mis datos?',
                 'a': 'Es la pregunta correcta y conviene hacerla siempre. Los datos siguen siendo tuyos y '
                      'viven donde ya viven; una automatización los mueve entre tus sistemas, no los sube a '
                      'ningún lado que no acuerdes. Cuando interviene un modelo de IA te decimos '
                      'exactamente qué información ve y qué no, antes de armar nada.'},
                {'q': '¿Cuánto tiempo se ahorra realmente?',
                 'a': 'No te vamos a tirar un porcentaje inventado, porque depende enteramente de tu caso. '
                      'Lo que sí se puede hacer es la cuenta con tus números: cuántas veces por semana se '
                      'hace la tarea, cuánto lleva cada vez, cuánto vale esa hora. Eso lo calculamos juntos '
                      'en el diagnóstico y te queda a vos, contrates o no.'},
                {'q': '¿Qué pasa si la automatización falla?',
                 'a': 'Falla en algún momento: cambia una API, se cae un servicio, alguien modifica un '
                      'formulario. Por eso las dejamos con aviso cuando algo no salió y con el camino '
                      'manual siempre disponible. Una automatización que falla en silencio es peor que no '
                      'tenerla, porque te enterás tarde.'},
            ],
            'mas': [
                ('que-tareas-de-mi-negocio-se-pueden-automatizar',
                 '¿Qué tareas de mi negocio se pueden automatizar?'),
                ('como-creo-una-automatizacion-para-mi-negocio',
                 '¿Cómo creo una automatización para mi negocio?'),
                ('la-automatizacion-sirve-para-un-negocio-chico',
                 '¿La automatización sirve para un negocio chico?'),
                ('cuanto-tiempo-se-ahorra-automatizando-tareas-administrativas',
                 '¿Cuánto tiempo se ahorra automatizando tareas administrativas?'),
                ('que-pasa-con-mis-datos-si-automatizo', '¿Qué pasa con mis datos si automatizo?'),
                ('cuanto-cuesta-automatizar-un-negocio-chico',
                 '¿Cuánto cuesta automatizar un negocio chico?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero automatizar',
        'titulo': 'Contanos qué hacés todos los días a mano',
        'texto': ('En 20 minutos hacemos la cuenta con tus números: cuántas horas se van, cuánto valen y '
                  'qué costaría sacarlas. El cálculo queda para vos aunque no contrates.'),
    },
}
