# HISTORIAL — Invitación al bautizo de Ivanna Eliette

Registro fechado del proceso. Documentos en español.

## Antecedentes (antes de agosto de 2026)
- Se construyó la invitación digital como página única (`index.html`) con foto de la
  invitación, sección "¿Cómo llegar?" (botones a Google Maps) y confirmación de
  asistencia por WhatsApp (adultos + niños).
- Decisión DEFINITIVA de publicación: GitHub Pages público (este repositorio,
  `bautizo-ivanna`) con enlace corto `ulvis.net/InvitacionIvanna`.
  - Se descartaron los Artifacts de claude.ai porque piden cuenta al visitante.
  - Gotcha conocido: `wa.me` corrompe emojis dentro de `?text=`; el mensaje de
    confirmación se mantiene sin emojis.
- Evento: sábado 29 de agosto de 2026. Ceremonia 12:00 en la Parroquia de Santo Tomás
  (Barrio de Xochimilco, Oaxaca de Juárez); recepción 14:30 en el Salón la Ermita
  (Carretera Monte Albán #126, San Juan Chapultepec).

## 2026-08-01 — Código de vestimenta
- Se agregó la sección **"Código de vestimenta"** entre "¿Cómo llegar?" y
  "Confirma tu asistencia", con su propio separador de diamante:
  - **Riguroso istmeño**: hombres, guayabera; mujeres, traje regional y su jicalpestle.
  - Nota para invitados de otros estados o de fuera: que vengan como se sientan a gusto.
- Estilos nuevos (`.vestimenta-titulo`, `.vestimenta`, `.vestimenta-quien`,
  `.vestimenta-detalle`) reutilizan la paleta y tipografías ya incrustadas.
- Se creó la carpeta `bitacora/` con los tres documentos vivos.
- Estado actual: página publicada en GitHub Pages; confirmaciones llegando por WhatsApp.

## 2026-08-01 — Sincronización de archivos fuente (bucle de mejora continua)
- La sección de vestimenta se había agregado solo aquí (`index.html`); los archivos
  fuente de `C:\Proyectos\invitacion-evento` quedaron atrás. Se sincronizaron
  (`invitacion.html` e `invitacion.template.html`) para que regenerar desde la
  plantilla no pierda la sección.
- Verificado en vivo: link corto 301 correcto, página HTTP 200 idéntica byte a byte a
  este repositorio, harness de 35 asserts en verde. **El `index.html` publicado no
  cambió** — los invitados no notan nada.
