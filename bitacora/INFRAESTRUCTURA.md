# INFRAESTRUCTURA — Invitación al bautizo de Ivanna Eliette

Toda la infraestructura digital de conexión del proyecto. No hay servidor propio,
base de datos, variables de entorno ni colas: es una página estática.

## Hosting y URLs
- **GitHub Pages** (repositorio público `bautizo-ivanna`, rama `master`):
  - URL pública: `https://desarrolloiacuentasaccesos-creator.github.io/bautizo-ivanna/`
  - Publicar = hacer `git push` a `master`; GitHub Pages se actualiza solo
    (puede tardar 1–2 minutos y el navegador puede cachear la versión anterior).
- **Enlace corto** que se comparte a los invitados: `ulvis.net/InvitacionIvanna`
  (redirige a la URL de GitHub Pages; si la URL base cambiara, habría que
  generar un enlace corto nuevo — ulvis.net no permite editar el destino).

## Servicios externos (salientes, desde el navegador del invitado)
- **WhatsApp (wa.me)** — confirmación de asistencia:
  - `https://wa.me/5219512283887?text=<mensaje-codificado>`
  - El número receptor está en `index.html`, bloque `EVENTO.whatsapp`
    (formato México celular: 521 + 10 dígitos).
  - Gotcha: no incluir emojis en `?text=` (se corrompen).
- **Google Maps** — botones "Cómo llegar":
  - `https://www.google.com/maps/search/?api=1&query=<lugar-o-coordenadas>`
  - Parroquia de Santo Tomás: búsqueda por nombre.
  - Salón la Ermita: coordenadas `17.051311,-96.736430`.
- **Open Graph** — la vista previa al compartir usa
  `https://desarrolloiacuentasaccesos-creator.github.io/bautizo-ivanna/portada.png`
  (WhatsApp cachea la vista previa; cambiarla no se refleja de inmediato).

## Flujo de datos
1. El invitado abre el enlace corto → redirige a GitHub Pages → carga `index.html`
   (todo incrustado: tipografías, estilos, lógica; solo pide `foto.jpg`).
2. Llena nombre + número de adultos y niños → botón "Confirmar por WhatsApp"
   construye el mensaje y abre `wa.me` hacia el número del anfitrión.
3. La confirmación llega como mensaje normal de WhatsApp; no hay backend que
   registre nada.

## Configuración editable
- Todo lo personalizable vive en `index.html`, constante `EVENTO`
  (frase, fecha, lugares/mapas y número de WhatsApp).
