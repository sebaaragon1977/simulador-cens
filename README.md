# Simulador de Cirugía Endoscópica Nasosinusal (CENS)

Simulador docente para residentes de primer año de Otorrinolaringología: visión endoscópica de la fosa nasal derecha o izquierda, anatomía del meato medio, receso frontal, etmoides y seno esfenoidal, con márgenes de seguridad (órbita, base de cráneo, arterias etmoidales, nervio óptico, carótida).

Autor: Dr. Sebastián Aragón — Servicio de ORL, Hospital Italiano de Buenos Aires.

## Cómo usarlo
Abrí `index.html` en un navegador moderno (Chrome, Edge o el navegador del Meta Quest). Si GitHub Pages está activado, se puede abrir directamente desde la web del repositorio.

### Modelos
- **Genérico:** anatomía esquemática con recorrido guiado de 13 pasos (secuencia CENS).
- **TC del paciente:** cargá una carpeta DICOM o un `.zip` con la serie. Todo se procesa localmente en el navegador; las imágenes no se suben a ningún lado. Usar siempre estudios **anonimizados**. En `ejemplo/tc_fantoma.zip` hay una TC sintética de prueba.

### Controles (computadora)
- `W`/`S` o rueda: avanzar/retroceder hacia donde mira la óptica · `A`/`D` lateral · `R`/`F` arriba/abajo
- Flechas o arrastre: orientar · `Z`/`X`: rotar óptica angulada · `O`: cambiar óptica (0°/30°/45°/70°)
- Modo *Explorar*: clic sobre un punto → el endoscopio viaja hasta ahí · `T`: viajar al centro de la cruz
- Instrumentos (`1`–`7`): explorar, pinza cortante, drill, bipolar, monopolar, aspirador y espátula de Freer
- Lesionar la etmoidal anterior/posterior o la esfenopalatina produce un sangrado pulsátil: coagular con bipolar (o monopolar, con riesgo térmico cerca de órbita y base de cráneo) y aspirar
- Freer: apoyar sobre el cornete medio o inferior y arrastrar a los lados para medializar/lateralizar · `Espacio`: lavado-aspiración general

### Meta Quest 2
Botón **Entrar en VR**. Control izquierdo = endoscopio (gatillo: viajar al punto · stick: avanzar y rotar óptica · X: óptica · grip: mover maqueta). Control derecho = instrumento activo (gatillo: cortar, fresar, coagular, aspirar o mover el cornete con la Freer · A: cambiar instrumento · B: estructuras de riesgo). Para la TC usar la malla **Quest 2 (liviana)**.

## Aviso
Herramienta de docencia. No es un sistema de navegación quirúrgica ni de diagnóstico.
