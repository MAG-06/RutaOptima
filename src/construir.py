# Junta los mapas de datos/ en la plantilla y genera index.html
# Uso: python src/construir.py
import json, pathlib
raiz = pathlib.Path(__file__).resolve().parent.parent
CIUDADES = [  # archivo, nombre, departamento (el orden es el de la pantalla de inicio)
    ("tulua.json", "Tuluá", "Valle del Cauca"),
    ("armenia.json", "Armenia", "Quindío"),
    ("cali.json", "Cali", "Valle del Cauca"),
]
datos = []
for archivo, nombre, dep in CIUDADES:
    d = json.loads((raiz / "datos" / archivo).read_text(encoding="utf-8"))
    d["city"], d["dept"] = nombre, dep
    datos.append(d)
plantilla = (raiz / "src/plantilla.html").read_text(encoding="utf-8")
html = plantilla.replace("__CITIES__", json.dumps(datos, ensure_ascii=False, separators=(",", ":")))
(raiz / "index.html").write_text(html, encoding="utf-8")
print("index.html generado con", len(datos), "mapas")
