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
- Los 16 servicios viven agrupados en 4 familias dentro de #services, cada uno en un
  <details class="svc"> con el patron "Con esto:" / "Sin esto:" y un micro-CTA a WhatsApp.
  Si agrego servicios, respetar ese patron.
- Jerarquia de color: el cyan (primary/secondary) queda reservado para acciones
  (botones y links). Los checks van en emerald-400, los contras en text-error y los
  iconos decorativos en zinc. No volver a pintar todo de cyan.
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
