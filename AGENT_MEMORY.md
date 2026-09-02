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

## Pendientes que necesitan datos del dueno
- Precio real de entrada: hay un bloque con $XXX.XXX marcado con TODO en #services.
- Testimonios reales: hay una plantilla comentada despues de la seccion de proyectos.
  No inventar testimonios ni estadisticas.
- Logo real de Zyntra (hoy hay un monograma "Z" hecho con CSS) y foto propia para #about.

## Uso
- Actualizar este archivo al crear, editar o borrar codigo.
- Mantenerlo corto y concreto.
