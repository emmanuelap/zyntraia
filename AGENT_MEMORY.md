# Memoria de trabajo

## Reglas activas
- Leer este archivo en cada inicio de sesion.
- No romper codigo que ya funciona.
- Escribir codigo simple, limpio y funcional.
- Pedir recursos externos cuando hagan falta.
- Preguntar lo que no sea seguro asumir.
- Sugerir mejoras utiles cuando aparezcan.
- Podes sugerir mejoras visuales o de estructura. Yo te las confirmaria antes de que las ejecutes
pero tenes que recordar siempre la regla de no romper codigo que ya funciona.

## Errores a no repetir
- Revisar caracteres rotos de codificacion antes de cerrar cambios en HTML.
- Verificar enlaces de WhatsApp con formato internacional antes de publicarlos.
- Incluir opcion de reducir movimiento cuando agregue animaciones nuevas.
- Revisar padding, botones y grillas en mobile y tablet antes de cerrar cambios visuales.

## Estructura actual de index.html
Orden de secciones: hero -> #senales -> #calculadora -> #services -> #proyectos ->
prueba objetiva -> industrias -> #faq -> #contact-form -> #contact -> #about.

- El sitio se publica solo en GitHub Pages con cada push a main (https://emmanuelap.github.io/zyntraia/).
- Los 16 servicios viven en #services, agrupados en 4 frentes. Cada servicio es una card
  SIEMPRE VISIBLE con icono, descripcion, "Con esto:" / "Sin esto:" y micro-CTA a WhatsApp.
  Si agrego servicios, respetar ese patron.
  OJO: se probo esconderlos en acordeones <details> y el dueno pidio volver atras porque
  el copy de venta quedaba oculto. No volver a colapsarlos.
- Jerarquia de color (medida por area en pantalla, no a ojo):
  cyan = acciones (botones y links), ambar-400 = numeros y datos (calculadora, franja
  de prueba), emerald-400/70 = "Con esto", error/70 = "Sin esto", zinc = decorativo.
  El verde y el rojo van con opacidad a proposito: si se ponen a full le ganan al cyan
  y la pagina se lee como semaforo. No volver a pintar todo de cyan ni subirles el peso.
- Contraste: no usar text-zinc-500 ni zinc-600 para texto (dan 3.99:1 y 2.6:1 sobre el
  fondo, no pasan WCAG AA). El minimo del sitio es zinc-400.
- La base es calida a proposito (#100f0d, no gris neutro) y los fondos oscuros usan
  #0a0908 en vez de zinc-950, que es frio y desentona.
- Sin imagenes generadas por IA: las capturas son reales, de la carpeta portfolio/.
- docs/ guarda los PDF descargables del sitio. Hoy vive ahi
  docs/propuesta-chatbot-zyntra.pdf (8 paginas, planes USD 400 / 700 / 1.000).
  Se ofrece con la pastilla .doc-download ("Lee nuestra propuesta" + icono de
  descarga + peso del archivo), presente en dos lugares: la card "Chatbots
  Inteligentes" de #services y el proyecto "Chat Bot Multi Rubro" de #proyectos.
  Si se regenera el PDF hay que actualizar el peso escrito en el HTML (dos lugares).
  En pantallas menores a 480px se oculta el peso (.doc-download-size) porque la
  pastilla no entraba en una linea dentro de la card de proyecto.
- La calculadora de perdidas y el menu mobile son JS vanilla al final del archivo.
- gracias.html es la pagina de destino del formulario (FormSubmit, campo _next).
- privacidad.html y terminos.html son las paginas legales. Copian el <head> de
  gracias.html (config de Tailwind + fuentes) y usan la clase .legal para la
  columna de lectura de 68ch. El texto describe el sitio REAL: sin cookies, sin
  analytics, y con FormSubmit / GitHub Pages / Google Fonts / Tailwind CDN como
  unicos terceros. Si se agrega alguna herramienta de medicion hay que corregir
  el punto 4 de privacidad.html, que hoy afirma que no existe ninguna.
- El footer de index.html y el de gracias.html llevan "CEO - Pavon Emmanuel" y
  los enlaces a las dos paginas legales.
- Identidad legal, igual en las dos paginas: Zyntra, EMPRESA de Emmanuel Pavon
  (no "emprendimiento" ni "proyecto"), CUIT 20-35971857-9, domicilio en Villa
  Urquiza, CABA. Sin altura de calle a pedido del dueno.

## Estructura del sitio (paso 4)
- La home dejo de ser la unica pagina comercial: ahora es el hub. Hay 12
  paginas de servicio y 57 enlaces internos desde index.html hacia ellas.
- Las 16 tarjetas de #services enlazan a su pagina en dos lugares: el titulo
  h4 y un "Ver el servicio en detalle" debajo del CTA de WhatsApp. Cuatro
  tarjetas todavia no tienen pagina propia (cobros, embudos, paneles,
  renovacion, fidelizacion) y apuntan a la mas cercana.
- Las 12 puertas de #industrias ya NO saltan a una tarjeta de la misma home:
  van a la pagina del servicio. El JS que resaltaba la tarjeta de destino sigue
  ahi y funciona si se llega con un hash #svc-x, pero las puertas ya no lo usan.
- El H1 de la home es "Automatizacion con IA y sistemas a medida". La frase de
  marca "Creacion con vision e inteligencia artificial" quedo como renglon
  chico arriba del H1: describe la marca pero no sirve como H1 para buscar.
- El footer tiene un bloque de 12 enlaces de servicio. Como build.py lee el
  footer de index.html, ese bloque se replica solo en las 12 paginas con las
  rutas corregidas a ../

## Paginas de servicio (generadas, NO editar a mano)
- Las carpetas de servicio como chatbot-whatsapp/ las escribe tools/build.py.
  Si editas <slug>/index.html directamente, el proximo build te lo pisa.
- El contenido de cada pagina vive en tools/paginas/<nombre>.py, un archivo por
  pagina, cada uno con un dict PAGINA. El nombre del archivo usa guion bajo, el
  slug de la URL usa guion medio.
- El header, el footer, los botones flotantes, la config de Tailwind y los
  <link> de fuentes se LEEN de index.html en cada build. index.html es la unica
  fuente de verdad del chrome; si cambias el menu ahi, correr el build y las
  paginas quedan iguales solas. Eso incluye el subset de iconos.
- build.py reescribe las rutas relativas sumando ../ porque las paginas viven un
  nivel mas abajo. Las que empiezan con http, mailto, tel o / quedan intactas.
- El build tambien reescribe sitemap.xml entero. No editarlo a mano.
- Comandos: python tools/build.py  |  python tools/build.py --listar
- tools/verificar.py revisa TODO el sitio: que cada enlace interno exista,
  que cada ancla exista de verdad en la pagina destino, que el JSON-LD sea
  valido y que ninguna <img> quede sin alt. Correrlo despues de cada build;
  devuelve 1 si encuentra algo. Una ancla mal escrita no rompe nada visible,
  por eso hace falta el chequeo.

## Rendimiento (paso 1 de la reestructuracion)
- El font de iconos se pide RECORTADO con &icon_names= en las 6 paginas. La
  fuente completa pesa 1.1 MB y el subset 70 KB. TRAMPA: si agregas un icono
  nuevo tenes que sumarlo a icon_names en TODAS las paginas o se ve como texto
  plano. La lista actual tiene 62 iconos.
- Las capturas de portfolio/ estan en WebP, con ancho maximo 1400 px (el ancho
  real que se muestra es 698 px CSS) y nombres en kebab-case sin acentos.
  3.48 MB -> 1.36 MB. Todas las <img> del portfolio llevan loading="lazy".
- El CSS y el JS de index.html viven en assets/zyntra.css y assets/zyntra.js
  para que se cacheen entre paginas. Siguen inline a proposito: la config de
  Tailwind (tiene que correr apenas carga el CDN) y los bloques JSON-LD.
- Quedan 19 imagenes sin usar en portfolio/ (4.4 MB). No las sirve nadie, solo
  pesan en el repo. Preguntar al dueno antes de borrarlas.

## Cifras reales (confirmadas por el dueno, NO inventar otras)
- Stratos: 72 gimnasios y alrededor de 8.900 usuarios en total.
- Asistente de WhatsApp: alrededor de 80 consultas por dia.
- Recordatorio automatico: las ausencias por olvido de turno bajaron un 50%.
- Estas son las UNICAS cifras publicables. Cualquier otra hay que pedirsela a el.

## PRECIOS: no se publica ninguno
- Pedido explicito del dueno: no va ningun precio en el sitio. Se saco el bloque
  "$XXX.XXX" que estaba PUBLICADO con las X literales, y las menciones a los
  3 dolares mensuales de hosting (home, FAQ, JSON-LD y desarrollo-web).
- La unica cifra en pesos que queda es el resultado de la calculadora de
  perdidas, que estima lo que pierde el visitante y no es un precio nuestro.

## Pendientes que necesitan datos del dueno
- Precio real de entrada: hay un bloque con $XXX.XXX marcado con TODO en #services.
- Testimonios reales: hay una plantilla comentada despues de la seccion de proyectos.
  No inventar testimonios ni estadisticas.
- Logo real de Zyntra (hoy hay un monograma "Z" hecho con CSS) y foto propia para #about.

## Uso
- Actualizar este archivo al crear, editar o borrar codigo.
- Mantenerlo corto y concreto.
