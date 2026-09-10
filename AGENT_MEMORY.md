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

## Sistema de diseno (rebrand, septiembre 2026)
- El sitio dejo de usar Tailwind CDN y Material Symbols. Todo el diseno vive
  en assets/zyntra.css con custom properties. NO volver a meter Tailwind:
  eran 127 KB y 780 ms de bloqueo, mas 70 KB de fuente de iconos.
- La fuente de verdad del sistema es
  "rediseno total de Zyntra/design_handoff_zyntra_rebrand/README.md".
  Ante cualquier duda de medida o color manda ese archivo.
- Paleta: --tinta #171310 (texto y fondos oscuros), --acento #E4572E (el
  naranja, unico acento), --acento2 #2F6B4F (verde de apoyo y zyntra causas),
  --arena #E3D8C4 (fondo del body), --crema #F5F0E6 (superficies).
- Tipografias: Bricolage Grotesque 600/800 (titulos), Instrument Sans
  400/500/600 (cuerpo), JetBrains Mono 600 (etiquetas, SIEMPRE mayuscula con
  tracking de .18em a .3em).
- Reglas duras, no negociables:
    * SIN box-shadow. Ninguna. La jerarquia se resuelve con color y radio.
    * Sin degradados. Sin sombras de color.
    * Un solo acento por pieza, maximo dos fondos.
    * El naranja nunca de fondo en una superficie larga (si en tarjetas).
    * Hover = solo cambio de color, 180 ms. Sin scale, sin elevacion.
    * Foco visible siempre: outline 2px naranja con offset 2px.
    * Nada de texto por debajo de 15px.
    * Los botones primarios llevan texto TINTA sobre naranja, no crema.
- El layout es una pila de paneles redondeados (radio 24) sobre arena,
  separados 14px. La clase es .panel; .panel--tinta / --naranja / --verde
  cambian el fondo. Adentro, .tarjeta (radio 18) y .tarjeta-caso.
- Las grillas son todas repeat(auto-fit, minmax(X, 1fr)) con --min: no hay
  breakpoints fijos salvo el del menu (900px) y el de las dos columnas.
- kit/index.html es la referencia viva del sistema, renderizada con el CSS
  real. Lo genera tools/kit.py. Lleva noindex y esta fuera del sitemap.
  Si algo se ve mal ahi, esta mal en assets/zyntra.css.

## Iconos (propios, sin librerias)
- tools/iconos.py tiene los iconos del sistema mas 3 marcas de terceros
  (WhatsApp, Telegram, LinkedIn, que van rellenas y no se redibujan). Se
  inyectan como sprite <symbol> en cada pagina: pesan ~2 KB con gzip.
- Regla del brandboard: linea pareja sobre grilla de 24, esquinas
  redondeadas, SIEMPRE en tinta con un unico detalle naranja (un punto).
  Nada de iconos rellenos ni de otra libreria.
- Se usan asi:  <svg class="ico"><use href="#i-turnos"></use></svg>
- TRAMPA: build.py corrige las rutas relativas de las paginas generadas, y el
  href="#i-algo" del sprite apunta a la MISMA pagina, no a la home. subir()
  lo saltea a proposito. Si eso se rompe, no se ve un solo icono.
- Los archivos tools/paginas/*.py siguen escribiendo el nombre VIEJO de
  Material Symbols en su clave 'icono'. iconos.EQUIV los traduce. Si aparece
  uno sin equivalente el build corta: hay que sumarlo a EQUIV.
- Para ver todos juntos: python tools/kit.py y abrir kit/index.html.

## Ojito, la mascota
- Es un ojo con patas, hecho con divs y custom properties. --S es el diametro
  y --lid el parpado: 0 abierto, .16 normal, .42 sospechando, .8 durmiendo.
- EL PARPADO ES LA UNICA EXPRESION. No tiene boca, ni nariz, ni cejas.
- Un solo Ojito por pieza, y siempre mirando algo real de la composicion.
- No aparece en las paginas de pentesting: ahi va el logotipo solo.
- En la web parpadea cada 4-7 s y el iris sigue al cursor. Las dos cosas se
  apagan con prefers-reduced-motion (assets/zyntra.js).
- Sobre fondo tinta el cuerpo sigue crema y el parpado sigue tinta: se lee
  como un mordisco arriba del ojo. Lo unico que cambia son las patas, que
  pasan a crema para no perderse contra el fondo.
- Donde esta hoy: hero de la home (grande), bloque CTA de cada pagina de
  servicio (chico), 404 sospechando y gracias bien abierto.

## Estructura actual de index.html
Orden de secciones: hero -> #senales -> #calculadora -> #services -> #proyectos ->
franja de datos -> #industrias -> #causas -> #faq -> #contact-form -> #about.
OJO: la seccion del programa sin fines de lucro se llamaba #impacto y ahora
es #causas ("zyntra causas", la unica excepcion de color del sistema: verde).

- El sitio se publica solo en GitHub Pages con cada push a main (https://emmanuelap.github.io/zyntraia/).
- Los 18 servicios viven en #services, agrupados en 5 frentes. Cada servicio es una card
  SIEMPRE VISIBLE con icono, descripcion, "Con esto:" / "Sin esto:" y micro-CTA a WhatsApp.
  Si agrego servicios, respetar ese patron.
  OJO: se probo esconderlos en acordeones <details> y el dueno pidio volver atras porque
  el copy de venta quedaba oculto. No volver a colapsarlos.
- Jerarquia de color: el naranja es el UNICO acento y se reserva para acciones,
  numeros grandes y el punto. El verde (--acento2) es apoyo: "Con esto", estados
  OK y zyntra causas. Todo lo demas es tinta, crema y arena. Si algo empieza a
  tener tres colores, sobra uno.
- Las vinetas de "Con esto / Sin esto" son puntos de 8px: verde el que suma,
  naranja el que resta. No van iconos ahi.
- Sin imagenes generadas por IA: las capturas son reales, de la carpeta portfolio/.
- docs/ guarda los PDF descargables del sitio. Hoy vive ahi
  docs/propuesta-chatbot-zyntra.pdf (8 paginas, planes USD 400 / 700 / 1.000).
  Se ofrece con la pastilla .doc-download ("Lee nuestra propuesta" + icono de
  descarga + peso del archivo), presente en dos lugares: la card "Chatbots
  Inteligentes" de #services y el proyecto "Chat Bot Multi Rubro" de #proyectos.
  Si se regenera el PDF hay que actualizar el peso escrito en el HTML (dos lugares).
  En pantallas menores a 480px se oculta el peso (.doc-download-size) porque la
  pastilla no entraba en una linea dentro de la card de proyecto.
- La calculadora de perdidas, el menu mobile, los carruseles y Ojito viven en
  assets/zyntra.js. Vanilla, con defer, y todo lo que anima respeta
  prefers-reduced-motion.
- gracias.html es la pagina de destino del formulario (FormSubmit, campo _next).
- privacidad.html y terminos.html son las paginas legales. Usan la clase .legal
  para la columna de lectura de 68ch. El texto describe el sitio REAL: sin
  cookies, sin analytics, y con FormSubmit / GitHub Pages / Google Fonts como
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
- Las 18 tarjetas de #services enlazan a su pagina en dos lugares: el titulo
  h4 y un "Ver el servicio en detalle" debajo del CTA de WhatsApp. Cuatro
  tarjetas todavia no tienen pagina propia (cobros, embudos, paneles,
  renovacion, fidelizacion) y apuntan a la mas cercana.
- Las 12 puertas de #industrias ya NO saltan a una tarjeta de la misma home:
  van a la pagina del servicio. El JS que resaltaba la tarjeta de destino sigue
  ahi y funciona si se llega con un hash #svc-x, pero las puertas ya no lo usan.
- El H1 de la home es "Automatizacion con IA y sistemas a medida". Arriba va una
  etiqueta mono, "Automatizacion e IA - Buenos Aires": ubica la marca sin robarle
  el lugar al H1, que es el que trabaja para buscar.
- El footer tiene un bloque de 12 enlaces de servicio. Como build.py lee el
  footer de index.html, ese bloque se replica solo en las 12 paginas con las
  rutas corregidas a ../

## Paginas de servicio (generadas, NO editar a mano)
- Las carpetas de servicio como chatbot-whatsapp/ las escribe tools/build.py.
  Si editas <slug>/index.html directamente, el proximo build te lo pisa.
- El contenido de cada pagina vive en tools/paginas/<nombre>.py, un archivo por
  pagina, cada uno con un dict PAGINA. El nombre del archivo usa guion bajo, el
  slug de la URL usa guion medio.
- El header, el footer, los botones flotantes, los preconnect y el <link> de
  fuentes se LEEN de index.html en cada build. index.html es la unica fuente de
  verdad del chrome; si cambias el menu ahi, correr el build y las paginas
  quedan iguales solas. El sprite de iconos NO sale de ahi: lo genera
  tools/iconos.py, que es la unica fuente de verdad del set.
- build.py reescribe las rutas relativas sumando ../ porque las paginas viven un
  nivel mas abajo. Las que empiezan con http, mailto, tel o / quedan intactas.
- El build tambien reescribe sitemap.xml entero. No editarlo a mano.
- Comandos: python tools/build.py  |  python tools/build.py --listar
- tools/verificar.py revisa TODO el sitio: que cada enlace interno exista,
  que cada ancla exista de verdad en la pagina destino, que el JSON-LD sea
  valido y que ninguna <img> quede sin alt. Correrlo despues de cada build;
  devuelve 1 si encuentra algo. Una ancla mal escrita no rompe nada visible,
  por eso hace falta el chequeo.

## Cache de assets (TRAMPA de GitHub Pages)
- Pages sirve assets/ con ~10 min de cache y no deja tocar cabeceras. Al
  publicar un cambio de diseno, el visitante que ya estuvo recibe el HTML
  NUEVO con el CSS VIEJO cacheado y ve la pagina rota hasta que expire.
  Paso de verdad al subir el rebrand.
- Por eso los <link> y <script> llevan ?v=<hash del contenido>. Lo pone
  tools/version.py, que corre solo al final de build.py. El hash cambia
  solo cuando el archivo cambia: si no tocaste el CSS, la URL no se mueve
  y el cache sigue sirviendo.
- Si editas assets/zyntra.css o assets/zyntra.js A MANO y no corres el
  build, hay que correr  python tools/version.py  antes de publicar. Si no,
  el cambio no le llega a nadie que ya haya entrado.
- verificar.py ignora el ?v= al resolver rutas. Si algun dia se versiona
  otro archivo, revisar que siga ignorandolo.

## Rendimiento
- Se saco lo que bloqueaba el renderizado: Tailwind CDN (127,4 KiB / 780 ms)
  y el font de iconos de Material Symbols (70 KB). Quedan tres pedidos: el
  CSS de Google Fonts (con preconnect), assets/zyntra.css y assets/zyntra.js
  (con defer).
- Las capturas de portfolio/ estan en WebP, ancho maximo 1400 px, en
  kebab-case sin acentos, todas con loading="lazy". 3,48 MB -> 1,36 MB.
- El CSS y el JS viven en assets/ para que se cacheen entre paginas. Los
  bloques JSON-LD siguen inline a proposito.
- Quedan 19 imagenes sin usar en portfolio/ (4,4 MB). No las sirve nadie.
  Preguntar al dueno antes de borrarlas.
- NO se puede arreglar en GitHub Pages: los tiempos de cache y las cabeceras
  HSTS, COOP, XFO, CSP y Trusted Types. Pages no deja configurar cabeceras.
  No perder tiempo ahi.
- Hay que volver a medir con PageSpeed despues del rebrand. Los numeros de
  septiembre (movil 80, escritorio 69 con CLS 0,177) son del sitio viejo.

## Logo
- El logotipo es una composicion HTML/CSS, no un archivo: la palabra "zyntra"
  en Bricolage 800 minuscula con letter-spacing -.045em, precedida del
  isotipo, que es un cuadrado de radio 34% en tinta con una Z crema y el
  punto naranja abajo a la derecha.
- El punto naranja lleva borde del color del FONDO de la pieza. En CSS eso
  se pasa con --fondo-pieza (por defecto arena). Sobre un panel tinta hay
  que setearlo o el borde queda mal.
- Prohibido: rotarlo, abrir el tracking, colorearlo fuera de la paleta o
  rehacerlo con otra tipografia.
- favicon.svg, apple-touch-icon.png y og-zyntra.jpg los genera tools/marca.py.
  La Z va como poligono de 10 puntos (no como texto): un favicon se dibuja
  sin webfonts. Las fuentes para la imagen OG se bajan de Google Fonts a una
  carpeta temporal, no al repo.
- PENDIENTE del handoff: vectorizar el logotipo y el Ojito como SVG
  (horizontal, apilado, isotipo, monograma y las 6 expresiones). Eso pide un
  editor vectorial.
- Quedan en assets/ los archivos de la marca VIEJA que subio el dueno
  (Zyntra-logo-vector.svg, logo.png, Zyntra-logo-fondo-oscuro.png,
  logo-zyntra-100x100.png). No los usa nadie. Preguntarle antes de borrarlos.

## Paginas hechas a mano (las 5 que no genera build.py)
- 404.html, gracias.html, privacidad.html, terminos.html y
  preguntasfrecuentes/index.html se escriben a mano, pero su header, footer y
  botones flotantes son COPIA del de index.html. Si cambias el menu ahi,
  hay que copiarlo tambien a estas cinco.
- TRAMPA de las paginas de la raiz: el header trae href="#senales", que en
  404.html apunta a un ancla de 404.html, no de la home. En esas paginas las
  anclas van como ./#senales.
- preguntasfrecuentes tiene 130 preguntas, buscador y "abrir todas", con su
  propio <style> y su propio <script> al final. Los estilos de esa pagina son
  los unicos que no estan en assets/zyntra.css.

## Blog
- Notas en tools/paginas/blog_*.py, con slug blog/<lo-que-sea> y la clave
  'articulo': {'fecha': 'AAAA-MM-DD'}. Esa clave hace que el schema salga
  Article en vez de Service y que aparezca la fecha bajo el H1.
- El indice del blog NO descubre las notas solo: al agregar una hay que
  sumarla a mano en la lista de tools/paginas/blog_index.py, arriba de todo.
- Regla de contenido: cada nota tiene que servirle a alguien que no nos va a
  contratar. Si solo tiene sentido como excusa para vender, no se publica.

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
