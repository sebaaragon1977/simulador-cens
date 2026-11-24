# Simulador de Cirugía Endoscópica Nasosinusal (CENS)

Simulador docente para residentes de primer año de Otorrinolaringología: visión endoscópica de la fosa nasal derecha o izquierda, anatomía del meato medio, receso frontal, etmoides y seno esfenoidal, con márgenes de seguridad (órbita, base de cráneo, arterias etmoidales, nervio óptico, carótida).

Autor: Dr. Sebastián Aragón — Servicio de ORL, Hospital Italiano de Buenos Aires.

## Cómo usarlo
Abrí `index.html` en un navegador moderno (Chrome, Edge o el navegador del Meta Quest). Si GitHub Pages está activado, se puede abrir directamente desde la web del repositorio.

### Modo de práctica
- **Libre:** exploración y cirugía sin restricciones, con recorrido guiado de 28 vistas.
- **Cirugía guiada:** elegís el procedimiento (CENS completa, Draf I, IIa, IIb y III, esfenoidotomía, esfenoidotomía bilateral, septoplastia, colgajo nasoseptal de Hadad, abordaje transesfenoidal a la silla turca, fosa pterigopalatina, control de sangrado de la etmoidal anterior). Cada paso señala la estructura objetivo, indica el instrumento y avanza solo cuando el paso se cumplió (identificación, resección, medialización, hemostasia, incisiones, colgajo). Al final muestra tiempo y complicaciones.

### Modelos
- **Genérico (bilateral):** anatomía esquemática de ambas fosas con recorrido guiado de 19 pasos: secuencia CENS, **Draf I, IIa, IIb y III** (septectomía superior y tabique intersinusal frontal fresables) y **esfenoidotomía ampliada y bilateral** (septectomía posterior, tabique intersinusal esfenoidal, arteria septal posterior). Incluye **abordaje a la silla turca** (piso selar, duramadre, hipófisis, carótida por segmentos, seno cavernoso con pares III, IV, V1, V2 y VI), **fosa pterigopalatina** (maxilar interna y ramas, ganglio, V2, agujero redondo, conducto vidiano) y **fosa infratemporal** (pterigoideos, agujero oval, V3), además de **septoplastia y colgajos** (monopolar en corte, elevación con Freer, colgajo de Hadad y cierre de perforación).
- **Casos guardados:** biblioteca compartida (carpeta `casos/`), "Mis casos" guardados en el dispositivo y 37 TC reales del dataset CT-SCOPE (CC BY-NC-ND 4.0) que se descargan de su repositorio original. El botón **Guardar caso** exporta un caso anonimizado (sin encabezados DICOM y sin piel de la cara).
- **TC del paciente:** cargá una carpeta DICOM o un `.zip` con la serie. Todo se procesa localmente en el navegador; las imágenes no se suben a ningún lado. Usar siempre estudios **anonimizados**. En `ejemplo/tc_fantoma.zip` hay una TC sintética de prueba.

### Controles (computadora)
- `W`/`S` o rueda: avanzar/retroceder hacia donde mira la óptica · `A`/`D` lateral · `R`/`F` arriba/abajo
- Flechas o arrastre: orientar · `Z`/`X`: rotar óptica angulada · `O`: cambiar óptica (0°/30°/45°/70°)
- Modo *Explorar*: clic sobre un punto → el endoscopio viaja hasta ahí · `T`: viajar al centro de la cruz
- `M`: monopolar en modo corte/coagulación
- Instrumentos (`1`–`0`, `U`): explorar, pinza cortante, drill, bipolar, monopolar, aspirador, espátula de Freer, pinza de agarre, pinza retrógrada, palpador bolita y porta-agujas con aguja curva (sutura)
- Colgajos: incisiones con monopolar en corte → la Freer despega la mucosa progresivamente (queda unida por el pedículo) → la pinza de agarre toma el colgajo y lo mueve (simulación de lámina blanda); botones para rotar a base de cráneo, a una perforación o reposicionar
- Perforaciones septales (algoritmo de Alobid): elegir sitio/tamaño → guía de incisiones (verde) y pedículo (naranja): <1 cm avance bipediculado, 1–2 cm colgajo de arteria etmoidal anterior, anterior extrema colgajo de palatina mayor, >2 cm etmoidal anterior extendido; grande anterior racket-on-donut (palatina mayor modificado + bordes invertidos); grande colgajo pediculado de pared lateral (piso, meato y cornete inferior). Llevar el colgajo a la perforación y fijarlo con puntos (porta-agujas)
- Receso frontal: bulla adelantada con lamela bullar (llega a la base o deja receso suprabullar, cubre la arteria etmoidal anterior), pico frontal, inserción superior de la unciforme (lámina papirácea / base de cráneo / cornete medio) con su vía de drenaje (meato medio o infundíbulo); barra vertical de Stamm (unciforme como pared medial del agger), variantes IFAC (agger, supra agger, supra agger frontal, supra bulla, supra bulla frontal, supraorbitaria, septal frontal) con vía de drenaje
- Lesionar la etmoidal anterior/posterior o la esfenopalatina produce un sangrado pulsátil: coagular con bipolar (o monopolar, con riesgo térmico cerca de órbita y base de cráneo) y aspirar
- Freer: apoyar sobre el cornete medio o inferior y arrastrar a los lados para medializar/lateralizar · `Espacio`: lavado-aspiración general

### Meta Quest 2
Botón **Entrar en VR**. Control izquierdo = endoscopio (gatillo: viajar al punto · stick: avanzar y rotar óptica · X: óptica · grip: mover maqueta). Control derecho = instrumento activo (gatillo: cortar, fresar, coagular, aspirar o mover el cornete con la Freer · A: cambiar instrumento · B: estructuras de riesgo). Para la TC usar la malla **Quest 2 (liviana)**.

## Aviso
Herramienta de docencia. No es un sistema de navegación quirúrgica ni de diagnóstico.

## Fantoma 2 (promedio de TC normales)
Botón **Fantoma 2** en "Modelo anatómico" (o el link con `?fantoma=2`). Mismas estructuras, cirugías guiadas y variantes que el genérico, con las proporciones anteroposteriores medidas en TC normales del dataset CT-SCOPE (P31, P36, P33, P35) y la regla 24-12-6 para las arterias etmoidales: etmoides más corto, bulla grande con receso retrobullar corto, lamela basal oblicua a ~11 mm de la cara del esfenoides, y esfenoides, silla y fosas adelantados 14,5 mm. Se usan sólo medidas, no imágenes del dataset. Arranca con **colores de atlas** (celdas y lamelas por color), que también se pueden activar en el genérico.

## Fantoma 1 (básico), DCR y órbita
- **Fantoma 1 · básico** (`basico.html`): el fantoma original, accesible desde el selector de modelo junto al Genérico, el Fantoma 2 y la TC del paciente.
- **Vía lagrimal**: saco lagrimal por delante de la axila del cornete medio, conducto nasolagrimal hasta la válvula de Hasner y canalículo común. Mucosa resecable, hueso lagrimal (fino, con pinza) y apófisis frontal del maxilar (gruesa, con drill).
- **DCR endoscópica** como cirugía guiada (7 pasos) y parada 29 del recorrido.
- **Órbita**: grasa resecable, recto medial, inferior, superior y lateral, oblicuo superior, globo y nervio óptico intraorbitario continuo con su prominencia en el seno esfenoidal. Alertas por lesión de músculos, nervio óptico o globo.
- Cirugía guiada "Órbita: recto medial y nervio óptico (anatomía)" y paradas 30–31 del recorrido.
- **Modo TC: "Marcar receso frontal (guiado)"**: se marcan axila, agger, barra vertical, ostium frontal y bulla sobre la TC del paciente y se dibuja la vía de drenaje animada, medial o lateral a la unciforme.

## Hueso sobre carótida y óptico, drill de a capas y Fantoma 3
- Dentro del seno esfenoidal, la **carótida y el nervio óptico** están cubiertos por una lámina ósea fina (se ven sus improntas). Se puede fresar o resecar; la lesión se avisa recién al atravesarla.
- **Drill**: gasta de a capas finas (~0,1 mm por pasada); hay que insistir sobre la zona para profundizar.
- **Fantoma 3 · angiofibroma** (`?fantoma=3`): angiofibroma juvenil nasofaríngeo derecho en la fosa nasal posterior y la rinofaringe. Pasa por el foramen esfenopalatino a la fosa pterigopalatina (irrigado por la maxilar interna) e invade el basiesfenoides.
- Cirugía guiada "Angiofibroma juvenil: resección endoscópica" (9 pasos): antrostomía amplia, pared posterior del seno maxilar, fosa pterigopalatina, control de la maxilar interna, resección pterigopalatina y nasal, fresado del basiesfenoides y del remanente. Si se reseca sin controlar la maxilar interna, sangra mucho.

## Apariencia
- **Mucosa húmeda**: capa brillante con película de moco (reflejos puntuales donde pega la luz) y translucidez suave en los bordes.
- **Relieve por tejido** (mapas de normales generados en el navegador): mucosa ondulada con puntillado glandular, hueso poroso, tumor lobulado; grasa, nervios, duramadre y vasos con su propio brillo.
- **Corte con aspecto de tejido**: el hueso fresado muestra trabéculas esponjosas con puntos hemorrágicos; la mucosa resecada deja un borde crudo, rojo y húmedo.
- **Luz del endoscopio en cono**: más luz al centro y caída hacia la periferia, con un relleno tenue.
- En el **Quest** se pasa solo a un modo liviano (sin capa húmeda ni translucidez) para mantener la fluidez.


## Modo anotación de TC (protocolo)
En **TC del paciente → Modo anotación (protocolo)** se marcan, lado por lado, 16 estructuras en orden fijo: axila, agger, barra vertical, ostium frontal, AEA, bulla, lamela basal, ostium maxilar, esfenopalatina, ostium esfenoidal, carótida, óptico, receso opticocarotídeo, lámina cribosa, fóvea y lámina papirácea. Cada paso tiene su definición y el corte sugerido. Se puede saltar o volver atrás, y la app no deja marcar del lado equivocado. Al final se cargan las variantes (Onodi, Haller, concha bullosa, inserción de la unciforme, dehiscencias) y el Keros se calcula solo. **Descargar anotaciones** baja un JSON con coordenadas LPS en mm. Para CT-SCOPE solo se exportan marcas, no imágenes.

### Estación de marcado (TC)
- **Cortes en pantalla principal**: axial, coronal y sagital grandes. A la derecha quedan la lista del protocolo y las herramientas; Esc vuelve a la endoscopia.
- **Nombre de cada marca**: después de cada clic aparece una ventanita para confirmar o cambiar la estructura. El nombre también se cambia desde la lista de marcas. El protocolo es una lista que se puede recorrer en cualquier orden.
- **Trayectos**: con "➕ Seguir marcando su trayecto" una estructura junta varios puntos (por ejemplo, la arteria etmoidal anterior de lado a lado). Se dibuja como un tubo en 3D y una línea en los cortes. Las alertas de riesgo usan la distancia a todo el trayecto. La exportación incluye cada punto con sus UH y la longitud en mm.
- **Unidades Hounsfield**: al pasar el mouse sobre los cortes se ven las UH y el tejido orientativo. Cada marca guarda sus UH (punto y media ± desvío en un cubo de 3×3×3 vóxeles).
