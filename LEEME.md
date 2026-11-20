# Ruta Óptima — Colombia

Juego web: escoge una ciudad, traza la ruta más corta entre dos puntos y al comprobar te dice si ganaste o perdiste, mostrando la ruta óptima (Dijkstra).

Mapas incluidos: Tuluá (fácil), Armenia (medio) y Cali (difícil).

## Cómo abrirlo
Doble clic en `index.html`.

## Estructura
- `index.html` — el juego completo, listo para usar.
- `datos/*.json` — un archivo por ciudad: puntos, tramos (km por vía), contorno y vías principales.
- `src/plantilla.html` — código del juego sin datos (busca `__CITIES__`).
- `src/construir.py` — junta los JSON de `datos/` y regenera `index.html`. Para agregar una ciudad: pon su JSON en `datos/` y agrégala a la lista `CIUDADES`.

## Formato del JSON de una ciudad
- `nodes`: `{id, name, x, y}` (coordenadas del mapa, ~1000 unidades de ancho).
- `edges`: `[índice_a, índice_b, km]`.
- `outline`: polígonos del contorno de la ciudad.
- `roads`: `[tipo, puntos]` con tipo `t` (troncal), `p` (primaria), `s` (secundaria).

Distancias calculadas sobre la red vial de OpenStreetMap (© colaboradores de OpenStreetMap).
