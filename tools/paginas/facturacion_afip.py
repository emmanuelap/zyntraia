# -*- coding: utf-8 -*-
"""Pagina de servicio: facturacion electronica AFIP."""

PAGINA = {
    'slug': 'facturacion-afip',
    'migas': 'Facturación AFIP',
    'icono': 'receipt_long',

    'titulo': 'Facturación electrónica AFIP integrada a tu sistema | Zyntra',
    'descripcion': ('Facturación electrónica AFIP con CAE real desde tu propio sistema. Facturas A, B y C '
                    'emitidas donde cargás la venta, sin volver a tipear en el portal.'),

    'h1': 'Facturación electrónica AFIP desde tu propio sistema',
    'bajada': ('Facturás en el momento de la venta, con CAE real, sin cargar dos veces los mismos datos '
               'ni entrar al portal. Integrado donde ya trabajás.'),

    'wa': 'Hola%20Zyntra%2C%20quiero%20integrar%20la%20facturaci%C3%B3n%20AFIP%20a%20mi%20sistema.',

    'servicio': {
        'nombre': 'Integración de facturación electrónica AFIP',
        'tipo': 'Desarrollo de software de facturación electrónica',
    },

    'secciones': [
        {
            'tipo': 'texto',
            'h2': 'El problema es la doble carga',
            'parrafos': [
                'La venta ya está cargada en algún lado: en tu sistema, en una planilla, en el cuaderno. '
                'Y después alguien la vuelve a tipear en el portal de AFIP, uno por uno, con el cliente '
                'esperando o al final del día.',
                'Ahí pasan las dos cosas de siempre. Se tipea mal un número y sale una factura que hay '
                'que anular con nota de crédito. O se juntan tres días de comprobantes y se factura todo '
                'junto, tarde y con fecha que no coincide con la venta.',
                'Integrar la facturación no es tener otro programa más. Es que el comprobante salga del '
                'mismo lugar donde ya cargaste la venta, en el mismo momento.',
            ],
        },
        {
            'tipo': 'lista',
            'fondo': True,
            'h2': 'Qué incluye la integración',
            'items': [
                {'icono': 'receipt_long', 'titulo': 'Facturas A, B y C',
                 'texto': 'Con el tipo de comprobante que corresponde según tu condición y la del cliente, '
                          'resuelto por el sistema y no de memoria.'},
                {'icono': 'check_circle', 'titulo': 'CAE real de AFIP',
                 'texto': 'El comprobante se autoriza contra el servicio de AFIP y vuelve con su código y '
                          'su vencimiento. No es un PDF que parece una factura.'},
                {'icono': 'cancel', 'titulo': 'Notas de crédito y débito',
                 'texto': 'Para cuando hay que anular o corregir, que es cuando más se complica hacerlo a '
                          'mano.'},
                {'icono': 'shopping_bag', 'titulo': 'Conectada al stock',
                 'texto': 'La venta descuenta inventario y emite el comprobante en la misma operación, '
                          'sin dos cargas.'},
                {'icono': 'phonelink_lock', 'titulo': 'Desde donde estés',
                 'texto': 'Emisión desde la computadora del mostrador o desde el celular, según cómo '
                          'trabajes.'},
                {'icono': 'analytics', 'titulo': 'Libro de comprobantes',
                 'texto': 'Todo lo emitido queda registrado y exportable, para vos y para tu contador.'},
            ],
        },
        {
            'tipo': 'pasos',
            'h2': 'Cómo se conecta con AFIP',
            'pasos': [
                {'titulo': 'Certificado digital',
                 'texto': 'Se genera un certificado a nombre de tu CUIT y se le da permiso para facturar. '
                          'Es un trámite que se hace una vez y te acompañamos a hacerlo.'},
                {'titulo': 'Autenticación',
                 'texto': 'El sistema pide un ticket de acceso al servicio de autenticación de AFIP y lo '
                          'renueva solo cuando vence. Vos no ves nada de esto.'},
                {'titulo': 'Solicitud del comprobante',
                 'texto': 'Al confirmar la venta, el sistema envía los datos al servicio de facturación y '
                          'espera la autorización.'},
                {'titulo': 'CAE y entrega',
                 'texto': 'AFIP devuelve el código de autorización y su vencimiento. Con eso se arma el '
                          'comprobante final, que se imprime o se manda por WhatsApp o email.'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'FactuApp, y por qué importa que sea real',
            'parrafos': [
                'FactuApp es nuestro sistema de facturación electrónica de escritorio, en producción, '
                'trabajando contra los servicios reales de AFIP con CAE real. No es una maqueta ni un '
                'simulador.',
                'La diferencia importa más de lo que parece. Conectarse a AFIP tiene sus particularidades: '
                'certificados que vencen, tickets de acceso con duración limitada, numeración que tiene '
                'que ser correlativa sin saltos, y un entorno de homologación que se comporta distinto al '
                'de producción. Todo eso ya lo pasamos.',
                'El mismo motor está integrado dentro de Stratos Admin, así que la facturación no vive '
                'aparte del sistema de gestión: es parte de la misma operación. Podés ver las capturas en '
                'la <a class="text-primary underline-offset-4 hover:underline" href="../#proyectos">sección '
                'de proyectos</a>.',
            ],
        },
        {
            'tipo': 'faq',
            'fondo': True,
            'h2': 'Preguntas sobre facturación electrónica',
            'preguntas': [
                {'q': '¿Puedo facturar desde mi propio sistema en vez del portal de AFIP?',
                 'a': 'Sí. AFIP publica servicios web justamente para eso: tu sistema pide la autorización '
                      'y recibe el CAE, igual que si cargaras la factura en el portal. Lo que cambia es que '
                      'los datos salen de donde ya están, no de alguien tipeando. Hace falta un certificado '
                      'digital a nombre de tu CUIT con permiso para facturar, que es un trámite de una sola '
                      'vez.'},
                {'q': '¿Qué pasa si me equivoco al emitir una factura?',
                 'a': 'Una factura electrónica autorizada no se borra: se corrige con una nota de crédito '
                      'que la anula, y después se emite la correcta. Por eso conviene que el sistema valide '
                      'antes de mandar, sobre todo el tipo de comprobante y los datos del cliente, que son '
                      'donde más se equivoca la carga manual. Igual las notas de crédito son parte normal '
                      'del circuito, no un desastre.'},
                {'q': '¿Necesito un sistema si facturo poco?',
                 'a': 'Si emitís tres facturas por mes, el portal de AFIP te alcanza y no vale la pena '
                      'integrar nada. La cuenta cambia cuando facturás todos los días, cuando la carga '
                      'manual te está generando errores, o cuando el comprobante tiene que salir en el '
                      'momento de la venta con el cliente adelante. Te decimos en cuál de los dos casos '
                      'estás.'},
                {'q': '¿Qué pasa si AFIP cambia algo?',
                 'a': 'Pasa seguido: cambian formatos, se agregan campos obligatorios, aparecen regímenes '
                      'nuevos. Es parte del mantenimiento de cualquier sistema que facture, y conviene '
                      'tenerlo previsto desde el principio en vez de descubrirlo el día que deja de andar. '
                      'Nosotros ya venimos siguiendo esos cambios para nuestros propios sistemas.'},
                {'q': '¿Los comprobantes quedan míos?',
                 'a': 'Sí, y quedan también en AFIP, que es el registro que vale. Tu sistema guarda el '
                      'libro completo exportable para vos y para tu contador. Es algo que conviene '
                      'confirmar con cualquier proveedor: si el día que te vas no te podés llevar el '
                      'historial de comprobantes, tenés un problema.'},
            ],
            'mas': [
                ('que-es-la-facturacion-electronica-de-afip-y-quienes-tienen-que-usarla',
                 '¿Qué es la facturación electrónica de AFIP y quiénes tienen que usarla?'),
                ('que-es-el-cae-de-afip-y-para-que-sirve', '¿Qué es el CAE de AFIP y para qué sirve?'),
                ('puedo-facturar-automaticamente-en-afip-desde-mi-propio-sistema',
                 '¿Puedo facturar automáticamente en AFIP desde mi propio sistema?'),
                ('que-diferencia-hay-entre-factura-a-b-y-c', '¿Qué diferencia hay entre factura A, B y C?'),
                ('se-puede-integrar-la-facturacion-con-el-control-de-stock',
                 '¿Se puede integrar la facturación con el control de stock?'),
                ('puedo-emitir-comprobantes-desde-el-celular', '¿Puedo emitir comprobantes desde el celular?'),
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero facturar desde mi sistema',
        'titulo': 'Contanos cómo facturás hoy',
        'texto': ('En 20 minutos vemos cuánto tiempo se te va en carga manual y qué haría falta para '
                  'integrar la emisión. El diagnóstico queda para vos aunque no contrates.'),
    },
}
