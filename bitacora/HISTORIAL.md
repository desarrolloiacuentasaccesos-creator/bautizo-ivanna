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

## 2026-08-01 — Corrección del código de vestimenta (pedido del usuario)
- El título pasa de "Riguroso istmeño" a **"Traje típico istmeño"** y se elimina el
  jicalpestle: mujeres queda solo **"Traje regional"**. Hombres sigue "Guayabera" y la
  nota para invitados de fuera queda intacta.
- Cambio aplicado idéntico a los TRES archivos (este `index.html` + los dos fuente de
  `invitacion-evento`), harness de 37 asserts en verde en los tres, y verificación en
  vivo tras el push. El link enviado por WhatsApp no cambia.
- **Verificación en vivo confirmada:** despliegue en ~10 segundos; página en vivo
  37/37 en el harness, idéntica byte a byte a este repositorio; link corto 301 correcto.
- Estado actual: versión vigente publicada con "Traje típico istmeño" (hombres
  Guayabera, mujeres Traje regional); confirmaciones llegando al 9512283887.

## 2026-08-01 — Registro automático de confirmaciones (preparado, apagado)
- `index.html` ahora puede mandar cada confirmación a una hoja de Google (Apps
  Script) además de abrir WhatsApp: campos `EVENTO.registro` / `EVENTO.registroClave`
  y función `registrarConfirmacion()` con `navigator.sendBeacon`.
- **Se publica con `registro: ""`, es decir APAGADO**: la página se comporta
  exactamente igual que antes hasta que el usuario entregue el URL de su aplicación
  web. Verificado con 58 asserts que sin endpoint no se envía nada y que, aun con
  endpoint caído, WhatsApp se abre igual.
- El aviso de transparencia al invitado solo aparece cuando el registro está activo.
- El dashboard vive en el proyecto `invitacion-evento`
  (`confirmaciones\dashboard-confirmaciones.html`), no aquí: no es público.

## 2026-08-15 (sábado) — Padrinos completos: se agrega la madrina de presentación
- **El error:** la fotografía de la papelería (`foto.jpg`) solo nombra a los padrinos de
  bautizo. Faltaba la madrina de **presentación** y faltaba decir que la celebración es
  **bautizo Y presentación**. La imagen impresa no se puede reescribir sin dañar el
  diseño bordado, así que la corrección se hace **en la página**.
- **Lo que se agregó:** una tarjeta nueva justo debajo de la foto, con la misma paleta
  (marfil / oro / frambuesa) y las mismas tipografías (Great Vibes + Cormorant), que dice:
  - "Bautizo y Presentación · Ivanna Eliette"
  - Padrinos — **Bautizo:** Beatriz Hernández Suárez y Juan Carlos Ruiz Ayala.
    **Presentación:** Reyna Pérez Guzmán.
  - "Con todo nuestro cariño los invitamos a celebrar el bautizo de nuestra hija
    Ivanna Eliette Lavín Cabrera 💗"
- **Otros ajustes del mismo cambio:**
  - Texto alterno de la foto: ahora distingue padrinos de bautizo y madrina de presentación.
  - `og:title` (vista previa de WhatsApp): "Invitación · Bautizo y Presentación de Ivanna Eliette".
  - `EVENTO.frase`: el mensaje de confirmación ahora dice "al bautizo **y presentación** de
    Ivanna Eliette". Sin emojis en ese texto (wa.me los corrompe en `?text=`).
- **Detalle de diseño:** la paloma se escribe con el selector de variación de texto
  (`&#x1F54A;&#xFE0E;`) para que salga monocroma en dorado y no como emoji gris deslavado.
  El corazón sí va a color porque combina con la paleta.
- **Verificación:** harness nuevo `_harness\probar_invitacion.py` (Playwright + Chromium),
  17 comprobaciones en verde: textos obligatorios, carga de la foto, texto alterno, mensaje
  de WhatsApp, los 2 botones de mapas y ausencia de barra horizontal a 320/390/430 px.
  Capturas en `_harness\capturas\`.
- **Sincronización:** el mismo cambio se aplicó a los dos archivos fuente del proyecto
  `C:\Proyectos\invitacion-evento` (`invitacion.html` e `invitacion.template.html`) y se
  verificó ahí también. El `og:title` no existe en esos dos archivos, por eso ese ajuste
  solo va en el `index.html` publicado.
- Sistema de diseño: no se generó uno nuevo. La fuente de verdad visual sigue siendo la
  papelería fotografiada y los tokens ya definidos en el `<style>` de `index.html`; la
  habilidad `ui-ux-pro-max` confirmó el par tipográfico (Great Vibes + Cormorant) y la
  familia de color rosa+oro que ya se usaban.

### Mismo día — la papelería corregida sustituye a la anterior
- El usuario ya tenía la imagen rehecha (`Downloads\Invitacion_Ivanna_Eliette_CORREGIDA.png`,
  editada en otra sesión). Ya trae **"Acompáñanos a celebrar el Bautizo y Presentación"** y
  la tarjeta chica dice **"Padrinos de Bautizo"** (Beatriz y Juan Carlos) y **"Madrina de
  Presentación"** (Reyna Pérez Guzmán). Con eso, la tarjeta HTML deja de ser una corrección
  y queda como refuerzo legible: en el teléfono la letra de la tarjeta fotografiada es diminuta.
- `foto.jpg` se regeneró desde ese PNG (JPEG progresivo, calidad 88 → 393 KB en vez de los
  2.3 MB del PNG: importa porque la invitación se abre con datos móviles). 1159×1356 px.
- `portada.png` (la vista previa que arma WhatsApp) se rehizo con el **mismo encuadre** que la
  anterior, tomado ahora de la imagen corregida; antes decía "el Bautizo de nuestra Hija" a secas.
- **Rompe-caché:** `foto.jpg?v=2` y `og:image ...portada.png?v=2`, para que a quien ya abrió
  la invitación no le siga apareciendo la imagen vieja guardada en su teléfono.
- El archivo original queda recuperable en el historial de git (no se guardó copia extra
  para no ensuciar el repositorio, que es público).
