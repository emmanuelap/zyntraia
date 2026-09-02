# -*- coding: utf-8 -*-
"""Indice de casos de exito. Solo cifras confirmadas por el dueno."""

PAGINA = {
    'slug': 'casos-de-exito',
    'migas': 'Casos de éxito',
    'icono': 'insights',

    'titulo': 'Casos de éxito: sistemas de Zyntra en producción | Zyntra',
    'descripcion': ('Sistemas de Zyntra funcionando: 72 gimnasios con 8.900 usuarios, un asistente de '
                    'WhatsApp que atiende 80 consultas diarias y facturación AFIP con CAE real.'),

    'h1': 'Sistemas nuestros, funcionando',
    'bajada': ('No mostramos maquetas. Todo lo que está acá está en producción, con gente usándolo todos '
               'los días.'),

    'wa': 'Hola%20Zyntra%2C%20vi%20los%20casos%20y%20quiero%20consultar%20por%20un%20proyecto.',

    'servicio': {
        'nombre': 'Desarrollo de sistemas a medida',
        'tipo': 'Desarrollo de software',
    },

    'secciones': [
        {
            'tipo': 'cifras',
            'h2': 'Lo que hay hoy en producción',
            'numeros': [
                {'cifra': '72', 'titulo': 'Gimnasios administrados',
                 'detalle': 'Con Stratos, multi-sede y multi-idioma.'},
                {'cifra': '8.900', 'titulo': 'Usuarios',
                 'detalle': 'Socios gestionados entre todas las sedes.'},
                {'cifra': '80', 'titulo': 'Consultas diarias',
                 'detalle': 'Atendidas por el asistente de WhatsApp.'},
                {'cifra': '50%', 'titulo': 'Menos ausencias',
                 'detalle': 'Caída de las ausencias por olvido de turno.'},
            ],
        },
        {
            'tipo': 'casos',
            'fondo': True,
            'h2': 'Los casos en detalle',
            'casos': [
                {'slug': 'casos-de-exito/stratos-gimnasios', 'icono': 'fitness_center',
                 'titulo': 'Stratos: 72 gimnasios, 8.900 usuarios',
                 'texto': 'Socios, planes, reservas con check-in por QR, cobros y facturación AFIP con '
                          'CAE real. Con app nativa para el socio.',
                 'cta': 'Ver el caso'},
                {'slug': 'casos-de-exito/chatbot-whatsapp', 'icono': 'smart_toy',
                 'titulo': '80 consultas por día, sin nadie mirando',
                 'texto': 'Un asistente de WhatsApp que entiende lenguaje natural, agenda en Google '
                          'Calendar y bajó las ausencias a la mitad.',
                 'cta': 'Ver el caso'},
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Otros trabajos publicados',
            'parrafos': [
                '<strong class="text-on-surface">Marroquinería Victoria.</strong> Sitio y catálogo, en '
                'línea y funcionando: podés verlo en '
                '<a class="text-primary underline-offset-4 hover:underline" '
                'href="https://marroquineriavictoria.com/" rel="noopener noreferrer" target="_blank">'
                'marroquineriavictoria.com</a>.',
                '<strong class="text-on-surface">FactuApp.</strong> Facturación electrónica de escritorio '
                'trabajando contra los servicios reales de AFIP, con CAE real. El mismo motor está '
                'integrado dentro de Stratos.',
                '<strong class="text-on-surface">Mini Turnos App.</strong> Gestión de turnos online '
                'personalizable por rubro.',
                'Las capturas de todos están en la '
                '<a class="text-primary underline-offset-4 hover:underline" href="@@SUBIR@@#proyectos">'
                'sección de proyectos</a> de la home.',
            ],
        },
        {
            'tipo': 'texto',
            'h2': 'Sobre estos números',
            'parrafos': [
                'Son los que podemos sostener. No vas a encontrar acá porcentajes de retorno de '
                'inversión ni promesas de cuánto vas a vender, porque eso depende de tu negocio y no de '
                'nuestro software.',
                'Lo que sí podemos decirte es cuántos gimnasios administra el sistema, cuántas consultas '
                'contesta el asistente y cuánto bajaron las ausencias donde se puso el recordatorio '
                'automático. Si te sirve como referencia, bien; si tu caso es distinto, te lo decimos en '
                'la primera charla.',
            ],
        },
    ],

    'cta': {
        'boton': 'Quiero consultar por un proyecto',
        'titulo': 'Contanos qué necesitás resolver',
        'texto': ('En 20 minutos vemos si algo de lo que ya construimos aplica a tu caso o si hay que '
                  'hacerlo desde cero. El diagnóstico queda para vos aunque no contrates.'),
    },
}
