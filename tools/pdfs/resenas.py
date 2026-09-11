# -*- coding: utf-8 -*-
"""
Propuesta de resenas y reputacion en Google Maps.

El contenido es el de la version anterior, que estaba bien escrito y no se
toca: cambia el diseno. Las cuentas de las tablas son verificables con una
calculadora, y esa es a proposito la gracia del documento.
"""

TITULO = 'Reseñas y reputación en Google Maps'
SUBTITULO = ('Por qué las reseñas deciden quién consigue al cliente nuevo, '
             'y cómo ganarlas sin perseguir a nadie.')
PIE = 'Reseñas y reputación en Google Maps'


def construir(Documento, C):
    d = Documento('propuesta-resenas-google', TITULO, SUBTITULO, pie=PIE, lid=.42)
    d.portada()

    d.seccion('', 'De qué se trata esta propuesta')
    d.parrafo(
        'Hay una parte de tu negocio que trabaja las veinticuatro horas y que '
        'probablemente nunca revisaste: lo que aparece cuando alguien te busca en '
        'Google. No la publicidad que pagás, ni tus redes. Tu ficha en Google Maps, '
        'con su estrellita y su número de reseñas al lado.')
    d.parrafo(
        'Esa ficha es, para la mayoría de los negocios locales, el primer contacto '
        'real con un cliente nuevo. Y a diferencia de una vidriera, no la decorás '
        'vos: la escriben tus clientes.')
    d.parrafo(
        'Este documento explica, con números que podés verificar, por qué las '
        'reseñas pesan tanto, qué te cuesta no tenerlas y cómo hacemos para que '
        'entren solas, sin que tengas que pedirle un favor a nadie.')

    # ------------------------------------------------------------------ 01
    d.seccion('01', 'Cómo decide Google a quién mostrar primero',
              'Cuando alguien busca un rubro cerca suyo, Google no muestra todos los '
              'negocios: muestra tres en un recuadro destacado, arriba de los '
              'resultados comunes. Estar o no estar en esos tres cambia por completo '
              'el volumen de gente que te encuentra.')
    d.parrafo('Google explica públicamente que ese orden se arma con tres criterios:')
    d.tabla(
        ['Criterio', 'Qué significa', '¿Podés influir?'],
        [['<b>Relevancia</b>', 'Qué tan bien tu ficha responde a lo que la persona buscó.',
          'Sí: completando bien categorías, servicios y descripción.'],
         ['<b>Distancia</b>', 'Qué tan lejos estás del punto desde donde se busca.',
          'No. Tu dirección es la que es.'],
         ['<b>Prominencia</b>', 'Qué tan conocido y confiable resulta tu negocio. Google '
          'indica que la cantidad de reseñas y la puntuación entran acá.',
          'Sí, y es donde más margen tenés.']],
        anchos=[16, 46, 38])
    d.importante(
        'De los tres criterios, uno no se puede cambiar y otro se completa una sola '
        'vez. La prominencia es el único que se construye todos los días, y las '
        'reseñas son su materia prima.')
    d.parrafo(
        'Dicho simple: la distancia y los datos de tu ficha te ponen en la carrera. '
        'Las reseñas definen en qué puesto salís.')

    d.salto()

    # ------------------------------------------------------------------ 02
    d.seccion('02', 'La aritmética de tu calificación',
              'Acá no hay opinión ni estadística de nadie: es una cuenta que podés '
              'rehacer en una calculadora. Y explica por qué el volumen de reseñas '
              'importa tanto como la nota.')
    d.titulo3('Qué le hace una sola reseña de 1 estrella a tu promedio')
    d.parrafo(
        'Supongamos que tenés 4,8 de promedio y aparece un cliente enojado. Lo que '
        'pasa después depende de una única cosa: cuántas reseñas tenías acumuladas '
        'antes.')
    d.tabla(
        ['Si tenías...', 'Tu promedio queda en', 'Caída', 'Efecto real'],
        [['10 reseñas', '4,45', '0,35 puntos', 'Golpe fuerte y visible'],
         ['25 reseñas', '4,65', '0,15 puntos', 'Se nota'],
         ['50 reseñas', '4,73', '0,07 puntos', 'Casi imperceptible'],
         ['100 reseñas', '4,76', '0,04 puntos', 'Casi imperceptible'],
         ['200 reseñas', '4,78', '0,02 puntos', 'Casi imperceptible']],
        anchos=[20, 24, 18, 38])
    d.parrafo(
        'El mismo cliente enojado, el mismo comentario, el mismo día. Con 10 reseñas '
        'te tira el promedio de 4,8 a 4,45. Con 200, lo deja en 4,78. No cambió la '
        'reseña: cambió tu capacidad de absorberla.')

    d.titulo3('Cuántas reseñas buenas hacen falta para compensar una mala')
    d.parrafo(
        'Esta es la cuenta que más sorprende. Si tu objetivo es sostener un promedio '
        'de 4,8, cada reseña de 5 estrellas aporta apenas 0,2 puntos por encima de '
        'ese objetivo, mientras que una de 1 estrella se lleva 3,8 puntos por debajo. '
        'Dividiendo una cosa por la otra:')
    d.dato('19', 'reseñas de 5 estrellas para neutralizar <b>una</b> de 1 estrella, si '
                 'querés mantener un promedio de 4,8.')
    d.tabla(
        ['Si tu objetivo es...', 'Cada reseña de 1 estrella te cuesta'],
        [['Promedio 4,9', '39 reseñas de 5 estrellas'],
         ['Promedio 4,8', '19 reseñas de 5 estrellas'],
         ['Promedio 4,5', '7 reseñas de 5 estrellas'],
         ['Promedio 4,0', '3 reseñas de 5 estrellas']],
        anchos=[38, 62])
    d.importante(
        'Cuanto más alto es tu promedio, más caro te sale cada tropiezo. Por eso la '
        'estrategia no puede ser solamente atender bien: hay que generar volumen de '
        'reseñas de forma constante, para tener espalda cuando llegue la mala. Y '
        'siempre llega.')

    d.salto()

    # ------------------------------------------------------------------ 03
    d.seccion('03', 'Lo que cuesta no pedirlas',
              'La mayoría de los clientes contentos no deja reseña. No por '
              'desagradecidos: porque nadie se las pidió, porque no saben cómo, o '
              'porque cuando se acuerdan ya están en otra cosa. El que sí se toma el '
              'trabajo de escribir sin que le pidan nada suele ser el que está '
              'enojado.')
    d.parrafo(
        'Tomemos un negocio que atiende 40 clientes por semana. Son 2.080 personas '
        'por año pasando por tu mostrador. Lo único que cambia entre un escenario y '
        'otro es qué porcentaje deja su opinión:')
    d.tabla(
        ['Escenario', 'Deja reseña...', 'Reseñas por año', 'En dos años'],
        [['Sin pedir nada', '1 de cada 100', '20', '41'],
         ['Pedido manual, cuando alguien se acuerda', '1 de cada 50', '41', '83'],
         ['Pedido automático por WhatsApp', '1 de cada 20', '104', '208'],
         ['<b>Pedido automático + tarjeta NFC</b>', '1 de cada 10', '<b>208</b>', '<b>416</b>']],
        anchos=[42, 22, 18, 18])
    d.parrafo(
        'Los porcentajes son escenarios, no promesas: dependen de tu rubro y de tu '
        'trato. Pero la diferencia entre la primera y la última fila no es de grado, '
        'es de categoría. Un negocio con 20 reseñas y otro con 208 no compiten en la '
        'misma liga, aunque atiendan exactamente igual.')
    d.parrafo(
        'Fijate lo que significa la primera fila combinada con la cuenta anterior: si '
        'generás 20 reseñas al año y recibís una sola de 1 estrella, necesitás casi '
        'todo un año de clientes contentos para volver al promedio que tenías.')

    # ------------------------------------------------------------------ 04
    d.seccion('04', 'Qué perdés cuando no estás arriba',
              'Las consecuencias de tener pocas reseñas no se ven, y eso es justamente '
              'lo peligroso: no hay un cartel que avise cuánta gente te descartó sin '
              'que te enteraras.')
    d.vinetas([
        '<b>Quedás fuera del recuadro de los tres primeros.</b> La mayoría elige entre '
        'esos tres y no sigue mirando. No es que te comparen y te descarten: '
        'directamente no te ven.',
        '<b>Desaparecés de las búsquedas filtradas.</b> Google Maps permite filtrar por '
        'calificación. Si el que busca activa el filtro de 4 estrellas o más y vos no '
        'llegás, dejás de existir para esa búsqueda.',
        '<b>Perdés la comparación cara a cara.</b> Entre dos negocios parecidos, uno con '
        '12 reseñas y otro con 180, la decisión se toma en un segundo.',
        '<b>Tus reseñas viejas juegan en contra.</b> Una ficha cuya última opinión es de '
        'hace tres años transmite que el negocio dejó de moverse.',
        '<b>Una sola mala reseña te define.</b> Si es la única que hay, es toda la '
        'información disponible sobre vos. Con volumen, pasa a ser la excepción '
        'evidente.'])
    d.importante(
        'Ninguno de estos costos aparece en una planilla. Nadie te llama para decirte '
        '"te iba a comprar pero elegí al de la otra cuadra porque tenía más '
        'estrellas". Es plata que no entra, y por eso no se nota.')

    d.salto()

    # ------------------------------------------------------------------ 05
    d.seccion('05', 'Cómo lo resolvemos',
              'El problema real nunca fue que tus clientes no quieran recomendarte. '
              'Fue la fricción: entre el cliente contento y la reseña publicada hay '
              'seis o siete pasos, y cada paso pierde gente.')
    d.tabla(
        ['Canal', 'Cómo funciona', 'Dónde rinde mejor'],
        [['<b>Tarjeta o cartel NFC</b>',
          'El cliente apoya el celular sobre la tarjeta y cae directo en la pantalla '
          'de calificación de Google. Sin apps, sin escanear, sin buscar tu negocio. '
          'Diseñamos la pieza nosotros.',
          'En el mostrador, la mesa o la recepción, en el momento en que el cliente '
          'está contento.'],
         ['<b>Código QR</b>',
          'Mismo destino, escaneando con la cámara. Va impreso en el ticket, la mesa, '
          'la bolsa o la puerta.',
          'Donde el cliente ya mira algo impreso.'],
         ['<b>Pedido automático por WhatsApp</b>',
          'Mensaje enviado solo, un rato después de la compra o del turno, con el '
          'enlace directo.',
          'Cuando el cliente ya se fue y querés alcanzarlo igual.']],
        anchos=[22, 46, 32])
    d.importante(
        'La clave de los tres es la misma: el cliente llega a la pantalla de escribir '
        'la reseña de un toque. Sin ese atajo, la mayoría abandona en el camino, y no '
        'porque no quisiera ayudarte.')
    d.titulo3('Y algo que suele olvidarse: responder')
    d.parrafo(
        'Google recomienda expresamente responder las reseñas, y el que las lee no '
        'está evaluando la queja, está evaluando cómo reaccionaste. Una respuesta '
        'serena a un reclamo vende más confianza que diez felicitaciones sin '
        'contestar. Dejamos el circuito armado para que responder sea cuestión de un '
        'minuto por día.')

    # ------------------------------------------------------------------ 06
    d.seccion('06', 'El circuito, paso a paso',
              'Así queda funcionando una vez implementado. La idea es que no dependa '
              'de que alguien se acuerde.')
    d.tabla(
        ['Paso', 'Qué pasa', 'Quién lo hace'],
        [['1', 'Preparamos y verificamos tu ficha de Google: categorías, servicios, '
               'horarios y fotos.', 'Nosotros'],
         ['2', 'Generamos tu enlace directo a la pantalla de reseña y lo probamos en '
               'varios teléfonos.', 'Nosotros'],
         ['3', 'Diseñamos y entregamos la tarjeta o el cartel NFC, y el QR impreso.',
          'Nosotros'],
         ['4', 'Conectamos el envío automático por WhatsApp después de la compra o el '
               'turno.', 'Nosotros'],
         ['5', 'El cliente apoya el celular o escanea, y deja su calificación.',
          'Tu cliente'],
         ['6', 'Te avisamos de cada reseña nueva y te dejamos respuestas listas para '
               'adaptar.', 'Nosotros y vos'],
         ['7', 'Revisamos el ritmo cada mes y ajustamos dónde se está perdiendo gente.',
          'Nosotros']],
        anchos=[8, 66, 26])

    d.salto()

    # ------------------------------------------------------------------ 07
    d.seccion('07', 'Lo que no hacemos, y por qué te conviene',
              'En este rubro circulan atajos que funcionan un mes y después salen '
              'carísimos. Queremos ser explícitos sobre dónde está el límite.')
    d.vinetas([
        '<b>No compramos reseñas ni las inventamos.</b> Google las detecta y sanciona el '
        'perfil. Para un negocio que depende del mapa, perder la ficha es desaparecer '
        'de un día para el otro.',
        '<b>No filtramos a quién se le pide.</b> Mandar el pedido solo a los clientes que '
        'sabemos contentos va contra las políticas de Google. Se le pide a todos, igual.',
        '<b>No denunciamos reseñas de la competencia</b> ni jugamos a bajarle el promedio '
        'a nadie.',
        '<b>No prometemos borrar las malas.</b> El dueño de un negocio no puede eliminar '
        'una reseña: solo puede reportarla si viola una política, y una crítica genuina '
        'no se saca aunque duela. Lo que sí funciona es diluirla con volumen y '
        'responderla bien.'])
    d.parrafo(
        'Si alguien te ofrece eliminación garantizada de reseñas o paquetes de reseñas '
        'positivas, es humo o es un riesgo serio para tu ficha. Preferimos decírtelo '
        'aunque no nos contrates.')

    # ------------------------------------------------------------------ 08
    d.seccion('08', 'Comprobalo vos mismo en tres minutos',
              'No hace falta que nos creas nada de lo anterior. Hacé esta prueba antes '
              'de decidir:')
    d.vinetas([
        'Abrí Google Maps en el celular y buscá tu rubro más tu barrio, como lo '
        'buscaría un cliente que no te conoce.',
        'Mirá los tres primeros resultados. Anotá cuántas reseñas tiene cada uno y qué '
        'promedio.',
        'Buscá dónde aparecés vos y anotá lo mismo.',
        'Activá el filtro de calificación de 4 estrellas o más y fijate si seguís '
        'apareciendo.',
        'Mirá la fecha de la última reseña de los tres primeros, y la de la tuya.'])
    d.parrafo(
        'Esa diferencia que acabás de ver es, exactamente, el trabajo que hay por '
        'delante. Si después de la prueba te quedan dudas, mandanos una captura y te '
        'decimos con qué empezaríamos.')

    d.salto()

    # ------------------------------------------------------------------ 09
    d.seccion('09', 'Preguntas que nos hacen siempre',
              'Las que más se repiten, contestadas de frente.')
    d.tabla(
        ['Pregunta', 'Respuesta'],
        [['¿En cuánto tiempo se ven resultados?',
          'Las primeras reseñas entran la misma semana en que se instala el circuito. '
          'El movimiento en el ranking es más lento y depende de tu competencia: '
          'hablamos de meses, no de días. Cualquiera que te prometa el primer puesto '
          'en dos semanas te está mintiendo.'],
         ['¿Y si me dejan una mala?',
          'Va a pasar, tarde o temprano. Por eso el objetivo es volumen: para que '
          'cuando llegue, sea una entre muchas y no la única que se lee. Y te dejamos '
          'preparado cómo responderla.'],
         ['¿Funciona el NFC en cualquier celular?',
          'En la enorme mayoría de los teléfonos actuales, apoyando la parte de atrás. '
          'Para los que no, la misma pieza lleva el QR impreso como alternativa.'],
         ['¿Sirve si recién empiezo?',
          'Es cuando más sirve. Arrancar de cero es la única etapa en la que cada '
          'reseña mueve el promedio de verdad, y es cuando más barato sale construir '
          'la base.'],
         ['¿Tengo que hacer algo todos los días?',
          'No. El pedido es automático. Lo único que te pedimos es responder las '
          'reseñas, y eso lleva un minuto.']],
        anchos=[30, 70])

    d.cierre(
        'El próximo paso es gratis',
        'Miramos tu ficha, la comparamos con la de los tres primeros de tu zona y te '
        'decimos qué te separa de ellos y en qué orden lo resolveríamos. Te queda el '
        'informe aunque no trabajes con nosotros.')
    return d.guardar()
