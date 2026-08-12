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
- La calculadora de perdidas y el menu mobile son JS vanilla al final del archivo.
- gracias.html es la pagina de destino del formulario (FormSubmit, campo _next).

## Pendientes que necesitan datos del dueno
- Precio real de entrada: hay un bloque con $XXX.XXX marcado con TODO en #services.
- Testimonios reales: hay una plantilla comentada despues de la seccion de proyectos.
  No inventar testimonios ni estadisticas.
- Logo real de Zyntra (hoy hay un monograma "Z" hecho con CSS) y foto propia para #about.

## Uso
- Actualizar este archivo al crear, editar o borrar codigo.
- Mantenerlo corto y concreto.
