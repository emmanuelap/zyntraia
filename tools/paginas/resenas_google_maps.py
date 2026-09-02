# -*- coding: utf-8 -*-
"""Pagina de servicio: resenas y reputacion en Google Maps."""

PAGINA = {
    'slug': 'resenas-google-maps',
    'migas': 'Reseñas en Google Maps',
    'icono': 'reviews',

    'titulo': 'Más reseñas en Google Maps para tu negocio | Zyntra',
    'descripcion': ('Sistema para conseguir reseñas en Google Maps: pedido automático por WhatsApp, QR y '
                    'tarjeta NFC. Mejorá tu posición en las búsquedas locales.'),

    'h1': 'Más reseñas en Google Maps, sin perseguir a nadie',
    'bajada': ('El cliente apoya el celular en una tarjeta NFC y cae directo en la pantalla para calificar. '
               'Sin buscar tu negocio, sin links largos, justo cuando está contento.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20conseguir%20m%C3%A1s%20rese%C3%B1as%20en%20Google%20Maps.',

    'servicio': {
        'nombre': 'Sistema de captación de reseñas en Google Maps',
        'tipo': 'Reputación online y SEO local',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'Cómo decide Google a quién muestra primero',
            'parrafos': [
                'Google explica que el orden en los resultados locales sale de tres cosas: relevancia, '
                'distancia y prominencia. Sobre la distancia no podés hacer nada. Sobre la relevancia, '
                'algo: completar bien la ficha, las categorías, los servicios.',
                'La prominencia es donde se juega el partido, y las reseñas pesan ahí. No solo cuántas '
                'tenés: también cuán recientes son y qué tan seguido llegan. Una ficha con cuarenta '
                'reseñas de hace tres años transmite algo distinto a una con veinte de este mes.',
                'Por eso el problema no es "conseguir reseñas" una vez. Es que lleguen todo el tiempo sin '
                'que vos tengas que pedirlas de a una.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'La aritmética de una estrella',
            'parrafos': [
                'Vale la pena entender el número. Si querés sostener un promedio de 4,8, cada reseña de '
                'una estrella que recibís necesita diecinueve de cinco estrellas para compensarla y volver '
                'al mismo promedio.',
                'Esa es toda la explicación de por qué conviene pedir reseñas siempre y no solo cuando '
                'algo salió mal. Un negocio que junta reseñas de forma constante absorbe una mala sin '
                'moverse. Uno que tiene seis reseñas en total se desploma con una.',
                'El otro lado de la cuenta: responder. Google recomienda contestar las reseñas, y una '
                'respuesta buena a una crítica convence más a quien la lee que diez elogios sueltos.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Las tres formas de pedirla',
            'intro': 'Todas llevan al mismo lugar: la pantalla de calificación de tu ficha, ya abierta.',
            'items': [
                {'icono': 'qr_code_2', 'titulo': 'Tarjeta o cartel NFC',
                 'texto': 'El cliente apoya el celular y se le abre la pantalla para calificar. Sin '
                          'aplicaciones, sin buscar, sin tipear. Es lo que mejor funciona en el mostrador '
                          'porque el momento es ahora.'},
                {'icono': 'chat', 'titulo': 'WhatsApp después del turno',
                 'texto': 'Mensaje automático un rato después de la visita, cuando la experiencia todavía '
                          'está fresca pero la persona ya no está apurada.'},
                {'icono': 'qr_code_2', 'titulo': 'QR impreso',
                 'texto': 'En el ticket, en la mesa, en la bolsa o en la vidriera. Es la opción más barata '
                          'y la que sirve para lugares donde no hay contacto directo.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo lo armamos',
            'pasos': [
                {'titulo': 'Revisamos tu ficha',
                 'texto': 'Categoría principal y secundarias, horarios, servicios, fotos. Una categoría '
                          'mal elegida te deja afuera de búsquedas enteras y no te enterás nunca.'},
                {'titulo': 'Armamos el enlace directo',
                 'texto': 'El link que abre la pantalla de calificación de tu negocio, no la ficha. Cada '
                          'paso extra que le pedís al cliente pierde gente.'},
                {'titulo': 'Diseñamos el soporte',
                 'texto': 'Tarjeta NFC, cartel o QR con tu marca. Lo diseñamos nosotros; la tarjeta física '
                          'la comprás vos y cuesta muy poco.'},
                {'titulo': 'Automatizamos el pedido',
                 'texto': 'El mensaje sale solo después de la compra o del turno, con el tono de tu '
                          'negocio y sin repetirle a quien ya dejó su reseña.'},
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre reseñas de Google',
            'preguntas': [
                {'q': '¿Se pueden comprar reseñas?',
                 'a': 'Se pueden, y es una de las peores ideas disponibles. Google prohíbe expresamente '
                      'las reseñas falsas o incentivadas y las detecta cada vez mejor: te las borra, y si '
                      'insistís puede sancionar la ficha entera. Además se notan, porque llegan todas '
                      'juntas, dicen lo mismo y vienen de cuentas sin historial. Perdés la ficha que tardaste '
                      'años en construir por veinte reseñas que no convencen a nadie.'},
                {'q': '¿Puedo borrar una reseña negativa?',
                 'a': 'Vos no. Podés reportarla si viola las políticas de Google, por ejemplo si tiene '
                      'insultos, si es spam o si es claramente de alguien que nunca fue tu cliente, y en '
                      'esos casos a veces la sacan. Si simplemente es una opinión mala pero legítima, se '
                      'queda. Lo que sí controlás es la respuesta, y ahí es donde se recupera la mayor '
                      'parte del daño.'},
                {'q': '¿Cuántas reseñas necesito?',
                 'a': 'No hay un número mágico, pero sí una referencia práctica: mirá cuántas tienen los '
                      'tres o cuatro competidores que aparecen arriba tuyo en el mapa. Ese es tu objetivo '
                      'real, y suele estar bastante más cerca de lo que uno cree. Importa más el ritmo que '
                      'el total: llegar a treinta en seis meses vale más que tener cincuenta de hace cuatro '
                      'años.'},
                {'q': '¿Cómo pido reseñas sin resultar molesto?',
                 'a': 'Tres reglas que funcionan. Pedila una sola vez y nunca insistas. Pedila en el mejor '
                      'momento, que es cuando la persona acaba de tener la experiencia, no tres semanas '
                      'después. Y hacé que sea de un toque: cada paso extra, buscar el negocio, entrar a '
                      'la ficha, encontrar el botón, pierde una parte de la gente que sí quería dejarla.'},
                {'q': '¿Qué es exactamente una tarjeta NFC de reseñas?',
                 'a': 'Es una tarjeta o un cartel con un chip adentro. El cliente apoya el celular encima y '
                      'se le abre directamente la pantalla para calificar tu negocio, sin instalar nada. '
                      'Funciona en la mayoría de los teléfonos actuales, y los que no tienen NFC pueden '
                      'usar el QR impreso en la misma tarjeta. Nosotros diseñamos el arte; la tarjeta '
                      'física la comprás vos.'},
            ],
            'mas': [
                ('como-consigo-mas-resenas-de-google-para-mi-negocio',
                 '¿Cómo consigo más reseñas de Google para mi negocio?'),
                ('las-resenas-influyen-en-el-posicionamiento', '¿Las reseñas influyen en el posicionamiento?'),
                ('como-respondo-una-resena-negativa', '¿Cómo respondo una reseña negativa?'),
                ('que-hago-si-me-dejan-una-resena-falsa', '¿Qué hago si me dejan una reseña falsa?'),
                ('que-es-google-business-profile', '¿Qué es Google Business Profile?'),
                ('como-verifico-mi-negocio-en-google', '¿Cómo verifico mi negocio en Google?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero más reseñas',
        'titulo': 'Miremos tu ficha y la de tus competidores',
        'texto': ('En 20 minutos comparamos tu ficha con la de los que aparecen arriba tuyo y definimos qué '
                  'te falta. El diagnóstico queda para vos aunque no contrates.'),
    },
}
