# -*- coding: utf-8 -*-
"""
Presupuesto de sitio web.

Este NO esta enlazado desde el sitio: se manda a mano cuando una consulta ya
avanzo. Por eso lleva precios cerrados sin conflicto con la regla de no
publicar precios en la web.
"""

TITULO = 'Sitio web para tu comercio'
SUBTITULO = ('Tres opciones, precios cerrados y plazos escritos. Para negocios '
             'que ya tienen redes y todavía no tienen web.')
ROTULO = 'Presupuesto'
PIE = 'Presupuesto de sitio web'


def construir(Documento, C):
    d = Documento('presupuesto-sitio-web', TITULO, SUBTITULO,
                  rotulo=ROTULO, pie=PIE, lid=0)
    d.portada(['Importes en dólares estadounidenses. Validez: 15 días.'])

    d.seccion('', 'Ya tenés Instagram. ¿Para qué una web?',
              'Es la primera pregunta que nos hacen, y es una buena pregunta. Si tus '
              'redes funcionan, algo estás haciendo bien. Pero hay cuatro cosas que tu '
              'Instagram no puede hacer, y ninguna es menor.')
    d.vinetas([
        '<b>No aparecés en Google.</b> Cuando alguien busca tu rubro en tu zona, Google '
        'muestra sitios web y fichas de negocio. Tu perfil de Instagram, salvo '
        'excepciones, no compite ahí. Ese cliente no te descartó: nunca te vio.',
        '<b>El alcance no es tuyo.</b> Vos no decidís a cuántos seguidores les llega cada '
        'publicación. Lo decide un algoritmo que cambia sin avisar.',
        '<b>Tu catálogo se hunde en el feed.</b> Lo que publicaste hace tres semanas está '
        'enterrado. En una web, el producto sigue en su lugar, ordenado y buscable, '
        'para siempre.',
        '<b>La cuenta es prestada.</b> Si mañana te la bloquean por error, perdiste todo '
        'de golpe: catálogo, contactos y años de trabajo. Una web es tuya y no te la '
        'puede cerrar nadie.'])
    d.importante(
        'La web no reemplaza a tus redes: las ordena. Las redes atraen a quien ya te '
        'conoce; la web te consigue al que te está buscando y todavía no sabe que '
        'existís. Por eso los tres planes conectan las dos cosas: tu web lleva a tus '
        'redes, y tus redes y tu ficha de Google llevan a tu web.')

    d.salto()

    # ------------------------------------------------------------------ 01
    d.seccion('01', 'Las tres opciones de un vistazo',
              'Los precios son cerrados: lo que figura acá es lo que pagás. No hay '
              'costos que aparecen después.')
    d.tabla(
        ['', 'Presencia', 'Catálogo', 'Sistema'],
        [['<b>Precio final</b>', '<b>USD 500</b>', '<b>USD 850</b>', '<b>USD 1.200</b>'],
         ['En 2 pagos mensuales', '2 × USD 250', '2 × USD 425', '2 × USD 600'],
         ['Plazo de entrega', '7 días', '12 a 15 días', '20 a 25 días'],
         ['Secciones del sitio', '1 página', '4 a 5', 'hasta 8'],
         ['Redes + mapa + cómo llegar', 'Sí', 'Sí', 'Sí'],
         ['Ficha de Google Business', 'Sí', 'Sí', 'Sí'],
         ['Fotos incluidas', 'hasta 12', 'hasta 40', 'sin tope'],
         ['Redacción de los textos', '—', 'Sí', 'Sí'],
         ['Catálogo con consulta por producto', '—', 'Sí', 'Sí'],
         ['Catálogo que edita el cliente', '—', '—', 'Sí'],
         ['Circuito de reseñas', '—', 'QR', 'QR + NFC'],
         ['Rondas de cambios', '1', '2', '3'],
         ['Soporte posterior incluido', '—', '—', '1 mes']],
        anchos=[40, 20, 20, 20])
    d.importante(
        'El más elegido es <b>Catálogo</b>. Presencia resuelve el problema de no existir '
        'en Google; Catálogo agrega lo que hace falta para que además te compren sin '
        'tener que preguntarte todo por mensaje privado.',
        'LA RECOMENDACIÓN')

    d.salto()

    # ------------------------------------------------------------------ 02
    d.seccion('02', 'Lo que incluyen los tres planes',
              'Sin importar cuál elijas, esto va siempre. Es la base sin la cual una web '
              'no sirve de nada.')
    d.titulo3('Conexión con tus redes y tu ubicación')
    d.vinetas([
        'Sección "Seguinos en nuestras redes" con acceso directo a Instagram, Facebook, '
        'TikTok y las que uses, bien visible y no escondida en el pie.',
        'Sección "Dónde encontrarnos" con el mapa de Google incrustado, tu dirección y '
        'tus horarios.',
        'Botón "Cómo llegar" que abre Google Maps con la ruta desde donde esté parada la '
        'persona.',
        'Botón para dejar una reseña en tu ficha de Google, de un toque.',
        'La conexión en los dos sentidos: cargamos el enlace de tu web en tu ficha de '
        'Google y en la biografía de tus redes. Sin este paso, la web queda aislada y no '
        'llega nadie desde donde ya te siguen.'])
    d.titulo3('Base técnica')
    d.vinetas([
        'Diseño propio, adaptado a tu negocio. No usamos plantillas prearmadas.',
        'Funcionamiento real en celular, tablet y computadora, probado en los tres.',
        'Botón flotante de WhatsApp con el mensaje ya escrito.',
        'Formulario de contacto que te llega al correo, sin costo mensual.',
        'Vista previa al compartir: cuando alguien pasa el enlace por WhatsApp aparece tu '
        'imagen y tu descripción, en vez de una dirección pelada.',
        'Configuración para buscadores: título, descripción, ícono, mapa del sitio y '
        'ficha de negocio.',
        'Publicación, conexión del dominio y certificado de seguridad.'])

    d.salto()

    # ------------------------------------------------------------------ 03
    d.seccion('03', 'Presencia · USD 500',
              'Para el comercio que necesita existir en Google y tener un lugar propio '
              'adonde mandar a la gente. O 2 pagos mensuales de USD 250.')
    d.titulo3('Qué se hace')
    d.vinetas([
        'Sitio de una página con portada, qué vendés, sobre el negocio, ubicación y '
        'contacto.',
        'Galería de hasta 12 fotos, seleccionadas de tu propio material.',
        'Todo lo listado en la base común: redes, mapa, cómo llegar, reseñas y ficha de '
        'Google.',
        'Maquetamos los textos que vos nos pasás.',
        '1 ronda de cambios sobre la primera entrega.'])
    d.titulo3('Qué no incluye')
    d.parrafo(
        'Redacción de los textos, catálogo de productos ni sistema de reseñas con QR. Si '
        'necesitás mostrar y ordenar lo que vendés, el plan que corresponde es Catálogo.')

    # ------------------------------------------------------------------ 04
    d.seccion('04', 'Catálogo · USD 850',
              'Para el comercio que quiere mostrar todo lo que vende, ordenado, y dejar '
              'de contestar el mismo precio veinte veces por día. O 2 pagos mensuales '
              'de USD 425. Todo lo del plan Presencia, más:')
    d.vinetas([
        'Sitio de 4 a 5 secciones en lugar de una sola página.',
        'Catálogo navegable por categorías, con foto, descripción y precio si querés '
        'mostrarlo.',
        'Botón "Consultar" en cada producto, que abre WhatsApp con el nombre de ese '
        'producto ya escrito. El cliente no tiene que explicar cuál era.',
        'Redacción profesional de todos los textos. Los escribimos nosotros, pensados '
        'para que el que entra entienda y consulte.',
        'Galería de hasta 40 fotos, organizadas por categoría.',
        'Sección de preguntas frecuentes preparada para que Google la use en sus '
        'respuestas.',
        'Circuito de reseñas con código QR hacia tu ficha de Google, listo para imprimir.',
        'Capacitación grabada de 30 minutos sobre cómo aprovechar el sitio.',
        '2 rondas de cambios.'])

    d.salto()

    # ------------------------------------------------------------------ 05
    d.seccion('05', 'Sistema · USD 1.200',
              'Para el comercio que además quiere manejar su catálogo solo, sin depender '
              'de nadie para cambiar un precio. O 2 pagos mensuales de USD 600, también '
              'en 3 de USD 400. Todo lo del plan Catálogo, más:')
    d.vinetas([
        'Sitio de hasta 8 secciones y fotos sin tope.',
        'Catálogo autoadministrable: editás productos y precios desde una planilla y la '
        'web se actualiza sola. Sin costo mensual de sistema y sin depender de nosotros.',
        'Tarjeta NFC de reseñas, diseñada y entregada física: el cliente apoya el celular '
        'y cae directo en la pantalla para calificarte.',
        'Página adicional para promociones o campañas puntuales.',
        'Medición de visitas configurada, con un informe explicado al primer mes.',
        '1 mes de soporte incluido después de la entrega.',
        '3 rondas de cambios.'])

    # ------------------------------------------------------------------ 06
    d.seccion('06', 'Adicionales, si los necesitás',
              'Se cotizan por separado porque dependen de tu rubro y de tu volumen. Se '
              'pueden sumar a cualquiera de los tres planes, en el momento o más '
              'adelante.')
    d.tabla(
        ['Adicional', 'Qué resuelve', 'Precio'],
        [['Turnos y reservas online', 'Tus clientes reservan solos las 24 horas, con '
          'recordatorio automático antes del turno.', 'A consultar'],
         ['Chatbot de WhatsApp', 'Responde consultas y deriva a una persona cuando hace '
          'falta, sin que tengas que estar.', 'A consultar']],
        anchos=[26, 56, 18])
    d.parrafo(
        'Los cotizamos después de entender tu operación, porque un sistema de turnos '
        'para un consultorio y otro para un salón con cinco profesionales no son el '
        'mismo trabajo. Presupuestarlos a ciegas sería inventarte un número.', 'chico')

    d.salto()

    # ------------------------------------------------------------------ 07
    d.seccion('07', 'Plan de mantenimiento, opcional',
              'Los tres planes se entregan funcionando y son tuyos. El mantenimiento es '
              'opcional: no lo necesitás para que el sitio siga andando.')
    d.dato('USD 60', 'por mes, para el que prefiere no ocuparse de nada y que alguien '
                     'esté mirando.')
    d.vinetas([
        'Cambios menores: precios, fotos, horarios, textos y productos nuevos.',
        'Respaldos periódicos del sitio.',
        'Monitoreo de que la web esté en línea y funcionando.',
        'Actualizaciones de seguridad.',
        'Informe mensual de visitas y de por dónde llega la gente.',
        'Atención prioritaria ante cualquier problema.'])
    d.parrafo(
        'Sin este plan, los cambios se cotizan por trabajo puntual. Con el plan, están '
        'incluidos mientras entren dentro de un alcance razonable. Se puede dar de baja '
        'cuando quieras.')

    # ------------------------------------------------------------------ 08
    d.seccion('08', 'Dominio y hosting: lo contratás vos',
              'Son los dos únicos costos que no van dentro del presupuesto, y es a '
              'propósito: quedan a tu nombre, con tu tarjeta y bajo tu control. Nadie te '
              'puede tomar de rehén tu propio sitio.')
    d.parrafo(
        'Nosotros te acompañamos en la contratación y dejamos todo configurado. Para que '
        'tengas una referencia, estos son valores aproximados de Hostinger, una de las '
        'opciones más económicas del mercado:')
    d.tabla(
        ['Concepto', 'Referencia', 'Aclaración'],
        [['Hosting, plan de entrada', 'Desde USD 3 por mes',
          'Ese precio requiere contratar 48 meses por adelantado.'],
         ['Hosting, precio de renovación', 'Alrededor de USD 11 por mes',
          'Es el valor una vez terminado el período promocional.'],
         ['Dominio, primer año', 'Sin costo',
          'Incluido en la mayoría de los planes de hosting.'],
         ['Dominio, años siguientes', 'Se abona aparte',
          'Varía según la terminación que elijas.']],
        anchos=[28, 26, 46])
    d.importante(
        'Leé bien esta parte antes de contratar. Los precios promocionales que se '
        'publican siempre corresponden al plan más largo, pagado por adelantado, y la '
        'renovación cuesta bastante más. No es una trampa de Hostinger, es cómo funciona '
        'todo el rubro, pero conviene saberlo antes y no cuando llega el segundo cobro.')
    d.parrafo(
        'Son valores de referencia relevados en agosto de 2026 y pueden cambiar. El '
        'costo real lo verificás en el momento de contratar.', 'chico')

    d.salto()

    # ------------------------------------------------------------------ 09
    d.seccion('09', 'Cómo trabajamos',
              'El proceso es el mismo en los tres planes. Lo escribimos para que sepas '
              'qué esperar y cuándo.')
    d.tabla(
        ['Etapa', 'Qué pasa'],
        [['1 · Charla inicial', 'Media hora para entender qué vendés, a quién y qué '
                                'querés lograr.'],
         ['2 · Material', 'Nos pasás fotos, textos si corresponde, logo y accesos a tus '
                          'redes.'],
         ['3 · Primera entrega', 'Te mostramos el sitio funcionando, en una dirección de '
                                 'prueba.'],
         ['4 · Cambios', 'Aplicamos tus correcciones, dentro de las rondas del plan.'],
         ['5 · Publicación', 'Conectamos el dominio y dejamos todo en línea.'],
         ['6 · Cierre', 'Te entregamos los accesos y la capacitación si el plan la '
                        'incluye.']],
        anchos=[26, 74])
    d.titulo3('Formas de pago')
    d.vinetas([
        '50% para comenzar y 50% contra entrega, antes de publicar. En la práctica eso '
        'ya es pagarlo en dos pagos mensuales sin interés, sin recargo de ningún tipo.',
        'El plan Sistema también se puede abonar en 3 pagos mensuales de USD 400.',
        'Los precios están expresados en dólares estadounidenses.',
        'El presupuesto tiene una validez de 15 días desde la fecha de envío.'])
    d.titulo3('Sobre las rondas de cambios')
    d.parrafo(
        'Una ronda es una tanda de correcciones juntas, no un cambio suelto. Nos mandás '
        'todo lo que querés ajustar y lo aplicamos de una vez. Está numerado para que el '
        'proyecto tenga un final claro: sin eso, un sitio se puede estirar meses y a '
        'ninguno de los dos nos conviene.')

    d.salto()

    # ------------------------------------------------------------------ 10
    d.seccion('10', 'Preguntas frecuentes',
              'Las que más nos hacen, contestadas de frente.')
    d.tabla(
        ['Pregunta', 'Respuesta'],
        [['¿La web es mía?',
          'Sí. El dominio y el hosting quedan a tu nombre, y te entregamos todos los '
          'accesos al cerrar. No quedás atado a nosotros para nada.'],
         ['¿Y si no tengo fotos buenas?',
          'Trabajamos con las de tus redes, que suelen alcanzar. Si hacen falta fotos '
          'nuevas, te decimos cuáles y te damos indicaciones para sacarlas con el celular.'],
         ['¿Puedo empezar por el plan chico y ampliar después?',
          'Sí, y es lo que recomendamos si tenés dudas. Al ampliar se descuenta lo ya '
          'invertido en la parte que se reutiliza.'],
         ['¿Aparezco primero en Google al día siguiente?',
          'No, y desconfiá de quien te lo prometa. Dejamos el sitio preparado para que '
          'Google lo encuentre y entienda, pero el posicionamiento lleva meses y depende '
          'de tu competencia.'],
         ['¿Cuánto tengo que saber de tecnología?',
          'Nada. Te explicamos todo sin términos técnicos y te dejamos el sitio andando.'],
         ['¿Qué pasa si me quiero ir?',
          'Te llevás todo. No retenemos accesos ni cobramos por entregar lo que ya '
          'pagaste.']],
        anchos=[32, 68])

    d.cierre(
        'El siguiente paso no cuesta nada',
        'Miramos tus redes y tu ficha de Google, y te decimos en concreto qué te conviene '
        'y por qué. Si no te sirve ninguno de los tres planes, te lo decimos también.')
    return d.guardar()
