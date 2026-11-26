# Capa Human Atlas (Fantoma 4)

- `za_capa.json`: 37 mallas de Z-Anatomy registradas al espacio del Fantoma 2 (mm; x lateral, y cefálico, z anterior). Posiciones int16 en centésimas de mm, índices uint16, en base64.
- Fuente: Z-Anatomy, a través del modelo masculino detallado de Human Atlas (https://github.com/ctzurcanu/human-atlas). Z-Anatomy deriva de BodyParts3D (© The Database Center for Life Science, CC BY 4.0).
- Licencia: CC BY-SA 4.0. Este archivo es una obra derivada (registro y recorte) y se distribuye con la misma licencia.

## Scripts (`scripts/`)
Necesitan una copia de `public/models/atlas-z-anatomy.json` y sus `.bin` del repo de Human Atlas (rutas en `dec.py`).
- `dec.py`: lee las mallas. `cl.py`: línea central por camino geodésico.
- `fit.py`: deformación WZ del Fantoma 2. `reg2.py`: registro (dos similitudes, puntos de referencia).
- `build.py`: trayectos para el simulador (`overrides.json`, se pegan en `HA` dentro de index.html).
- `export.py`: genera `za_capa.json`.
