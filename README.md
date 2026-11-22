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
- Receso frontal: barra vertical de Stamm (unciforme como pared medial del agger), variantes IFAC (agger, supra agger, supra agger frontal, supra bulla, supra bulla frontal, supraorbitaria, septal frontal) con vía de drenaje
- Lesionar la etmoidal anterior/posterior o la esfenopalatina produce un sangrado pulsátil: coagular con bipolar (o monopolar, con riesgo térmico cerca de órbita y base de cráneo) y aspirar
- Freer: apoyar sobre el cornete medio o inferior y arrastrar a los lados para medializar/lateralizar · `Espacio`: lavado-aspiración general

### Meta Quest 2
Botón **Entrar en VR**. Control izquierdo = endoscopio (gatillo: viajar al punto · stick: avanzar y rotar óptica · X: óptica · grip: mover maqueta). Control derecho = instrumento activo (gatillo: cortar, fresar, coagular, aspirar o mover el cornete con la Freer · A: cambiar instrumento · B: estructuras de riesgo). Para la TC usar la malla **Quest 2 (liviana)**.

## Aviso
Herramienta de docencia. No es un sistema de navegación quirúrgica ni de diagnóstico.
