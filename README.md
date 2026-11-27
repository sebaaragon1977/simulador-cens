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

## Fantoma Human Atlas (`?fantoma=4`)
- **Base**: la fosa del Fantoma 2 (proporciones calibradas con TC). Mismas cirugías guiadas, variantes y recorrido.
- **Calibración con Z-Anatomy** (modelo masculino detallado de [Human Atlas](https://github.com/ctzurcanu/human-atlas), derivado de BodyParts3D): el globo ocular, los cuatro rectos, el oblicuo superior, el nervio óptico (intraorbitario y en el canal), la carótida interna y la basilar siguen los trayectos medidos en Z-Anatomy. Las alertas de lesión usan esos trayectos.
  - Registro por dos transformaciones de similitud (escala ≈1): órbita y techo etmoidal (AEA y PEA en la papirácea, pared lateral del etmoides, conducto nasolagrimal) y esfenoides y silla (esquinas del seno, hipófisis, basilar), mezcladas entre la cara del esfenoides y el etmoides posterior. Error en los puntos de registro: 2–10 mm.
  - Cambios respecto del Fantoma 2: el globo queda ~29 mm más atrás (centro a la altura de la bulla) y la carótida paraclinoidea en el tercio posterior de la pared lateral del esfenoides (receso opticocarotídeo ~8 mm más atrás).
  - La AEA y la PEA no se modificaron porque son puntos de registro (no son una medición independiente). Como dato: en Z-Anatomy la distancia AEA–PEA es de ~10 mm (regla 24-12-6: 12 mm; Fantoma 2: ~18 mm; Genérico: 25 mm).
- **Capa Human Atlas**: 37 mallas reales de Z-Anatomy de ambos lados (carótidas, oftálmicas, etmoidales, maxilar interna, palatina descendente, vidiana, cerebrales anterior y media, basilar, senos cavernosos e intercavernosos, venas oftálmicas, nervio óptico, quiasma y cintillas, III, IV, VI, V1 y V2, hipófisis, giro recto, globo, músculos extraoculares, tróclea, glándula lagrimal), en `humanatlas/za_capa.json`. Se prende y apaga en el panel; con "Estructuras de riesgo" se ven por transparencia. No intervienen en colisiones.
- Scripts del registro y la exportación en `humanatlas/scripts/`.
- **Licencia de la capa**: Z-Anatomy, CC BY-SA 4.0 (BodyParts3D © DBCLS, CC BY 4.0). Las mallas derivadas (`humanatlas/za_capa.json`) se distribuyen con la misma licencia.

## Fístula de LCR y herniación de grasa orbitaria
- **Fístula de LCR**: al lesionar la base de cráneo (fóvea etmoidal, lámina cribosa, pared posterior del frontal, diafragma selar o dura del clivus) gotea líquido claro como agua: una gota colgante crece con el latido y cae con la gravedad real (también en VR, con el paciente acostado) y lava la sangre acumulada. No se cierra con bipolar; se sella rotando el colgajo nasoseptal a la base de cráneo sobre el defecto.
- **Herniación de grasa orbitaria**: al perforar la lámina papirácea la grasa protruye hacia medial sobre el etmoides y el meato medio. Se indica coagular su superficie con bipolar y se retrae; resecarla con pinza o drill cuenta como complicación.

## Fantoma septum desviado (`?fantoma=5`) y septoplastia
- Desviación septal en C hacia la fosa derecha (máx. ~3,4 mm) y **espolón** óseo macizo en la unión condrovomeriana que toca el cornete inferior.
- **Bisturí** (nuevo instrumento): incisión de Killian/hemitransfixión; sobre el cartílago hace la condrotomía, que sirve para despegar el colgajo contralateral.
- Colgajos mucopericóndricos con **espesor** (~0,8 mm, con cara profunda de pericondrio y borde), despegables con Freer de ambos lados, también sobre el espolón.
- Botón **"Separar colgajos (espéculo)"**; resección del espolón y del cartílago desviado con pinza o bisturí (el tabique se endereza); **"Reposicionar colgajo"** devuelve ambos colgajos sobre el tabique recto.
- Alertas: morder el espolón sin despegar la mucosa (desgarro/perforación) y cortar la L de soporte. Cirugía guiada "Septoplastia: desviación y espolón".

## Fantoma poliposis (`?fantoma=6`) y shaver
- Base: Fantoma Human Atlas (fosa calibrada con TC + órbita y base de cráneo de Z-Anatomy).
- ~70 pólipos pediculados en meato medio, receso frontal, celdas etmoidales anteriores y posteriores (se ven al abrirlas), hendidura olfatoria y receso esfenoetmoidal.
- **Shaver / microdebridador** (nuevo instrumento): hoja recta de 4 mm con ventana dentada y cuchilla interna oscilante, vástago con la marca XOMED. Reseca sólo pólipos y mucosa (no hueso) y aspira la sangre. En la órbita es una complicación grave.
- También se resecan con pinza cortante (de a trozos) o con pinza de agarre (avulsión, sangra más). Contador de pólipos y cirugía guiada "Poliposis: polipectomía y CENS".

## Cornetes macizos y reducción del cornete inferior
- Los cornetes son macizos: al cortarlos o fresarlos la superficie de corte muestra submucosa con el hueso en el centro.
- Bipolar o monopolar en coagulación achican el cornete inferior localmente (reducción del volumen submucoso).

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

## Controles Quest 2 (v24)
- **Izquierdo (endoscopio):** mover el control orienta la óptica. Stick ↑↓ avanza o retrocede dentro de la nariz y stick ←→ rota la óptica. **El gatillo cambia de instrumento.** X cambia el ángulo de la óptica, Y muestra u oculta la maqueta y el grip mueve la maqueta. Manteniendo apretado el clic del stick, el endoscopio viaja al punto de la cruz.
- **Derecho (instrumento):** mover el control lo dirige. Stick ↑↓ avanza o retrae el instrumento sobre su eje (−6 a +12 cm) y el clic del stick lo vuelve al inicio. **El gatillo acciona** el instrumento: pinza, drill, bipolar, monopolar, aspirador, etc. A pasa al instrumento anterior y B muestra las estructuras de riesgo.

## Endoscopio 3D en VR (v25)
En VR el monitor del endoscopio se ve en estéreo: cada ojo recibe una imagen tomada desde una cámara corrida a un costado, como en un endoscopio 3D. Las dos imágenes convergen a 16 mm. Se prende y apaga con el **grip derecho** o con el botón "3D en VR" del panel. La separación entre cámaras ("Profundidad 3D", de 0,4 a 3 mm; 1,4 mm por defecto) se ajusta en el panel y queda guardada. En monopolar, el cambio entre corte y coagulación pasó al clic del stick derecho.

## VR v26: límite de fosa, suavizado, paciente y torre
- **Una fosa / ambas fosas:** con una sola fosa elegida, en VR la óptica y el instrumento no cruzan el plano del tabique. Al llegar al límite, el mando vibra y aparece un aviso. Con **"Ambas fosas en VR"** (panel) se puede cruzar el tabique para septectomía, Draf III o esfenoidotomía bilateral. Ese modo se activa solo al iniciar las guiadas Draf III, esfenoidotomía bilateral, silla turca y septoplastia. En TC el límite es la línea media.
- **Suavizado:** filtro "one euro" sobre la posición y la rotación de cada mando. Quieto filtra mucho y en movimientos rápidos responde. Se ajusta con el slider "Suavizado VR" (60% por defecto). Los sticks tienen respuesta fina cerca del centro y velocidades más bajas.
- **La óptica se desliza sobre su eje** (stick izquierdo) en lugar de mover la maqueta, y el instrumento igual (stick derecho, hasta 10 cm reales). Por eso el paciente queda quieto.
- **Paciente esquemático:** cabeza, cuello y hombros bajo el campo, con cabezal. Está a la misma escala que la maqueta (×4) y la sigue. Se ve translúcido mientras la maqueta está visible y opaco al ocultarla (Y).
- **Torre de endoscopía:** carro con cámara, fuente de luz, shaver, electrobisturí y aspiración. Arriba, el monitor 3D, alto para verlo por encima de la cabeza del paciente.
- Arreglo: la luz del quirófano ya no se apaga al ocultar la maqueta.
- **v27, paciente acostado:** en VR el paciente está boca arriba, mirando al techo, con la cabeza rotada 15° hacia la derecha. El cirujano queda a la derecha de la cabeza. La narina está delante del cirujano, a la altura de las manos (x −0,15, y 1,06, z −0,5). La torre con el monitor 3D está en diagonal a la izquierda (45°), casi de frente. A escala ×4 el tórax no entra en la sala: se dibujan cabeza, cuello, un campo y la camilla con cabezal. La TC usa la misma orientación.
- **Salir de VR:** mantener apretado **Y** (mando izquierdo) 1,5 s; el aviso muestra la cuenta regresiva y si se suelta antes se cancela. Un toque corto de Y sigue mostrando u ocultando la maqueta. También se sale con el botón Meta (mando derecho) → Salir.

## Fantoma 7 · TC real con referencias (`?fantoma=7`)
- **Base**: la TC real **CT-SCOPE P13** (paciente adulto), que se descarga en el navegador desde el repositorio original del dataset. Licencia CC BY-NC-ND 4.0: la TC no se guarda ni se redistribuye; en el repositorio sólo hay parámetros y medidas (`casos/fantoma7_P13.json`).
- **Cornetes inferior y medio afinados** para entrar cómodo con el endoscopio: fila por fila se comprime el tejido hacia la pared lateral (el cornete conserva su forma, con mucosa y hueso, pero más angosto) y queda un corredor junto al tabique. Espacio libre en el meato común: de 0,6–1,4 mm de radio en la TC original a 2,3–3 mm. Los cortes de TC también muestran los cornetes afinados.
- **Referencias reales**: las marcas del Dr. Aragón sobre P13 (`anotaciones/CT-SCOPE_P13_seba_v1.json`): arteria etmoidal anterior, bulla, lamela basal, ostium maxilar, esfenopalatina, ostium esfenoidal, carótida, óptico, lámina cribosa, fóvea y lámina papirácea. Las de riesgo dan alerta y sangrado; cribosa y fóvea suman alertas de base de cráneo. Son de la fosa derecha; en la izquierda se espejan (sólo las de riesgo) en el plano de simetría de la cabeza.
- **Capa Human Atlas en la TC**: las 37 mallas de Z-Anatomy se llevan a P13 con una spline de placa delgada ajustada a esas marcas, al centro del globo ocular medido en la TC y a la línea media (error medio 1,2 mm, máximo 4 mm en los puntos de ajuste). Se ve con "Estructuras de riesgo" o al resecar.
