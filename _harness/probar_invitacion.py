"""
Harness de la invitación de Ivanna Eliette.
Abre index.html en un navegador real (Chromium) y comprueba que la
información del evento esté completa y que la página se vea bien en teléfono.

Uso:  python _harness\probar_invitacion.py
Requiere: pip install playwright  +  python -m playwright install chromium
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parent.parent
PAGINA = (RAIZ / "index.html").as_uri()
CAPTURAS = pathlib.Path(__file__).resolve().parent / "capturas"
CAPTURAS.mkdir(exist_ok=True)

# Texto que SIEMPRE debe estar visible en la página (comparado en minúsculas,
# porque el título va en versalitas por CSS).
TEXTO_OBLIGATORIO = [
    "bautizo y presentación",
    "padrinos",
    "beatriz hernández suárez",
    "juan carlos ruiz ayala",
    "reyna pérez guzmán",
    "ivanna eliette lavín cabrera",
    "parroquia de santo tomás",
    "salón la ermita",
    "traje típico istmeño",
]

fallas = []


def revisar(condicion, descripcion):
    print(("  OK    " if condicion else "  FALLA ") + descripcion)
    if not condicion:
        fallas.append(descripcion)


with sync_playwright() as p:
    navegador = p.chromium.launch()
    pagina = navegador.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2)
    pagina.goto(PAGINA)
    pagina.wait_for_timeout(1500)

    print("\n1) Contenido visible")
    texto = pagina.inner_text("body").lower()
    for esperado in TEXTO_OBLIGATORIO:
        revisar(esperado in texto, "aparece: " + esperado)

    print("\n2) La foto de la papelería carga")
    cargo = pagina.eval_on_selector("img.foto", "i => i.complete && i.naturalWidth > 0")
    revisar(cargo, "foto.jpg se muestra")
    revisar("presentación" in pagina.get_attribute("img.foto", "alt").lower(),
            "el texto alterno menciona la presentación")

    print("\n3) Mensaje de WhatsApp")
    frase = pagina.evaluate(
        "() => document.documentElement.innerHTML.match(/frase:\\s*\"([^\"]+)\"/)[1]"
    )
    revisar("bautizo y presentación" in frase.lower(),
            "la confirmación dice 'bautizo y presentación': " + frase)

    print("\n4) Enlaces de mapas")
    mapas = pagina.eval_on_selector_all("a.boton-mapa", "a => a.map(x => x.href)")
    revisar(len(mapas) == 2, "hay 2 botones de 'Cómo llegar'")
    revisar(all(m.startswith("https://www.google.com/maps/") for m in mapas),
            "ambos apuntan a Google Maps")

    print("\n5) Presentación en pantalla chica")
    for ancho in (320, 390, 430):
        pagina.set_viewport_size({"width": ancho, "height": 800})
        pagina.wait_for_timeout(300)
        desborde = pagina.evaluate(
            "() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1"
        )
        revisar(not desborde, "sin barra horizontal a " + str(ancho) + " px")

    pagina.set_viewport_size({"width": 390, "height": 844})
    pagina.wait_for_timeout(400)
    pagina.locator("section.panel").first.screenshot(path=str(CAPTURAS / "tarjeta_padrinos.png"))
    pagina.screenshot(path=str(CAPTURAS / "pagina_completa.png"), full_page=True)
    navegador.close()

print("\nCapturas en: " + str(CAPTURAS))
if fallas:
    print("\n" + str(len(fallas)) + " FALLA(S):")
    for f in fallas:
        print("  - " + f)
    sys.exit(1)
print("\nTodo en orden.")
