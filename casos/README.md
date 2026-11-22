# Biblioteca de casos

- `index.json`: lista de casos compartidos que aparecen en el simulador ("Biblioteca compartida").
- Cada caso es un archivo `.cens.zip` generado con el botón **Guardar caso** del simulador: volumen recortado a fosas, senos y base de cráneo, sin encabezados DICOM y sin piel ni partes blandas superficiales de la cara, más las marcas de riesgo.
- Para agregar un caso: copiar el `.cens.zip` a esta carpeta y sumar una línea en `index.json` (`name`, `desc`, `file` y, si corresponde, `credit`).
- Subir sólo estudios anonimizados y revisados por el responsable docente.

## Biblioteca externa
`ctscope.json` lista las TC del dataset **CT-SCOPE** (BYO-UPM, Universidad Politécnica de Madrid; licencia CC BY-NC-ND 4.0). El simulador las descarga directamente del repositorio original (github.com/BYO-UPM/Craneal_CT) y las procesa en el navegador: no se redistribuyen ni se suben versiones modificadas a este repositorio.

Cita: Sun Y, Guerrero-López A, Arias-Londoño JD, Godino-Llorente JI. CT-SCOPE: annotated dataset of CT scans for the automatic semantic segmentation of the osseous structures of the paranasal sinuses. Data in Brief 2025;62:111962.
