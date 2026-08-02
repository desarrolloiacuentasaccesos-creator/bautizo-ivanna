# STACK — Invitación al bautizo de Ivanna Eliette

Proyecto de archivo único, sin proceso de build ni dependencias externas.

## Lenguajes y tecnologías
- **HTML5 + CSS3 + JavaScript** (vanilla, sin frameworks) en un solo archivo: `index.html`.
- **Tipografías incrustadas** en el propio archivo como `@font-face` base64
  (subconjunto latino, sin peticiones externas):
  - Great Vibes (caligráfica) — títulos decorativos.
  - Cormorant Garamond (serif) — títulos y acentos.
  - Respaldo del sistema: Georgia / system-ui.
- **Recursos estáticos**: `foto.jpg` (invitación principal), `portada.png`
  (imagen Open Graph para la vista previa en WhatsApp).

## Registro automático de confirmaciones (preparado, apagado)
- `index.html` incluye `EVENTO.registro` / `EVENTO.registroClave` y la función
  `registrarConfirmacion()`, que envía cada confirmación con `navigator.sendBeacon`
  (respaldo `fetch` con `keepalive`) a una aplicación web de **Google Apps Script**
  antes de abrir WhatsApp.
- **Con `registro: ""` no se envía nada** y la página se comporta como siempre.
- El programa de Apps Script, la guía de instalación y el dashboard viven en el
  proyecto `invitacion-evento` (carpetas `registro-en-linea\` y `confirmaciones\`);
  aquí solo está la parte pública.

## Herramientas
- **Git + GitHub** (repositorio público `bautizo-ivanna`, rama `master`).
- **GitHub Pages** como hosting (publica la rama directamente; sin build).
- **Pruebas automatizadas** (viven en el proyecto `invitacion-evento`):
  - `harness-invitacion.js` — ejercita el JavaScript real con Node portable
    (v20.17.0) sobre un DOM simulado: 58 asserts (mapas, mensajes de WhatsApp,
    payload del registro, que WhatsApp no se bloquee si el registro falla).
  - Playwright (Chromium) para la verificación visual y de interacción.
  - Verificación en vivo tras cada push: la página publicada debe quedar
    **idéntica byte a byte** al archivo del repositorio.
