# EHDS — Espacio Europeo de Datos Sanitarios (Reglamento (UE) 2025/327)

Cárgalo cuando el proyecto **almacene, importe, exporte, convierta, edite o
muestre** datos de salud personales de alguna de las **categorías
prioritarias** del art. 14 EHDS (resumen del paciente, receta/dispensación
electrónica, imagen médica y su informe, resultado de laboratorio, informe de
alta), o cuando `signals.posible_ehr_o_ehds` sea true, o el usuario declare que
el software es (o incluye) un **sistema de historia clínica electrónica**, o
que comparte datos de salud con fines de investigación/estadística
(uso secundario). Es una norma **horizontal adicional**: se aplica **en
paralelo** al MDR/IVDR (no lo sustituye) y también a software que **no** es
producto sanitario.

**Volátil.** El EHDS entró en vigor en 2025 y sus calendarios de aplicación y
actos de ejecución están en desarrollo. **Antes de concluir, contrasta por web**
(ver `checkpoints-volatiles.md`): estado de los actos de ejecución de la
Comisión sobre especificaciones comunes (art. 36) y sobre el EEHRxF, y qué
autoridad española asume las funciones de organismo de acceso a los datos de
salud (art. 65) y de vigilancia del mercado de sistemas EHR.

---

## 1. ¿Es tu software un "sistema EHR" a efectos del EHDS?

**Definición (art. 2):** un sistema EHR es **cualquier sistema** (aplicación o
software) que permite **almacenar, intermediar, exportar, importar, convertir,
editar o visualizar** datos sanitarios electrónicos personales que pertenezcan
a las **categorías prioritarias** de datos personales de salud, y que el
fabricante destina a ser usado por **profesionales sanitarios** en la
prestación de asistencia (p. ej. para registrar notas clínicas, resultados de
pruebas… hasta un sistema completo de gestión de pacientes) o por **pacientes**
para acceder a sus propios datos de salud electrónicos (p. ej. una app que se
conecta al servicio de acceso a los datos de salud electrónicos del paciente).

**Categorías prioritarias de datos (art. 14):** resumen del paciente
(*patient summary*), receta electrónica, dispensación electrónica, imágenes
médicas y sus informes, resultados de laboratorio, informes de alta. **Un
sistema que solo trata otro tipo de datos (p. ej. una app de citas) NO es un
sistema EHR** a efectos del EHDS, aunque trate datos de salud a otros efectos
(RGPD sigue aplicando igual).

**Quién es "fabricante" de un sistema EHR:** el EHDS no lo define y remite al
Reglamento (UE) 2019/1020: quien fabrica el sistema, o lo manda diseñar/
fabricar, y lo comercializa bajo su nombre o marca.

### Señales de la exploración (paso 2) → interpretación
- `signals.posible_ehr_o_ehds`, `ehds.categoria_prioritaria`,
  `ehds.interoperabilidad_ehr`, `ehds.registro_acceso_ehr` → indicio de sistema
  EHR.
- `clinical.estandares_salud` (HL7/FHIR/DICOM/SNOMED/LOINC/openEHR) +
  `clinical.dominio_clinico` juntos → el software probablemente almacena o
  intercambia historia clínica estructurada: candidato fuerte a sistema EHR.
- El caso típico del enunciado del usuario ("app que hace una valoración
  clínica y genera un informe"): si el informe generado se **almacena,
  exporta o pone a disposición del profesional/paciente** como parte de una
  categoría prioritaria (p. ej. se guarda como "informe" reutilizable, se
  exporta en un formato estructurado, se integra en la historia clínica del
  centro) → **es candidato a sistema EHR** además de MDSW. Si el informe es
  una **salida efímera, no persistida ni exportable**, de un cálculo puntual,
  el encaje como sistema EHR es más débil — documentar el razonamiento.

---

## 2. Qué exige el EHDS a los fabricantes de sistemas EHR (Capítulo III, arts. 30-49)

Un sistema EHR **solo puede comercializarse o ponerse en servicio** si cumple
el Capítulo III. Obligaciones del fabricante:

1. **Requisitos esenciales (Anexo II)** — tres bloques:
   - **a) Generales:** el sistema funciona según lo previsto y mantiene la
     seguridad del paciente en uso normal; diseño para suministro, instalación
     y funcionamiento correctos según las instrucciones, sin comprometer sus
     características.
   - **b) Interoperabilidad:** todo sistema destinado a almacenar, intermediar
     o dar acceso a datos sanitarios electrónicos personales debe permitir el
     **acceso y la recepción de esos datos en el EEHRxF** (formato europeo de
     intercambio de historia clínica electrónica — ver §3); no puede incluir
     funciones que **restrinjan** el acceso, la compartición, el uso o la
     exportación autorizados de esos datos (prohibición de "lock-in").
   - **c) Seguridad y registro de accesos:** mecanismos fiables de
     identificación y autenticación de profesionales sanitarios; herramientas
     para **revisar y analizar el registro de accesos** (o soporte para
     conectar software externo que lo haga).
2. **No interferencia entre componentes:** los componentes armonizados
   (interoperabilidad, registro de accesos) no pueden verse afectados
   negativamente por otros componentes del mismo sistema.
3. **Documentación técnica** (art. 37), elaborada **antes** de comercializar y
   mantenida actualizada.
4. **Información al usuario e instrucciones de uso** (art. 38), gratuitas, en
   lenguaje claro.
5. **Declaración UE de conformidad** (art. 39) y **marcado CE** (art. 41) —
   **un régimen de marcado CE propio del EHDS**, distinto (aunque puede
   coexistir) del marcado CE del MDR si el sistema es también producto
   sanitario.
6. Identificación del fabricante, datos de contacto y **punto de contacto
   único**, en lenguaje accesible al usuario.
7. **Registro en la base de datos UE** de sistemas EHR (art. 49), con los
   resultados de la evaluación de los componentes armonizados, **antes** de
   comercializar o poner en servicio.
8. **Acciones correctivas, retirada o recuperación** de sistemas no
   conformes, con notificación a las autoridades nacionales.
9. Informar a distribuidores, representantes, importadores y usuarios de
   no conformidades, acciones correctivas, retiradas y mantenimiento
   preventivo obligatorio.
10. Facilitar a las **autoridades de vigilancia del mercado** toda la
    información necesaria para demostrar conformidad con el Anexo II.
11. Establecer y mantener **canales de reclamaciones** y un registro de
    reclamaciones y de sistemas no conformes.

**Pruebas antes de comercializar (art. 40):** el fabricante debe **probar los
componentes armonizados** antes de poner el sistema en el mercado e incluir
los resultados en la documentación técnica pública. Los Estados miembro deben
crear **entornos de pruebas digitales europeos** para verificar de forma
automatizada esta conformidad.

---

## 3. EEHRxF — Formato Europeo de Intercambio de Historia Clínica Electrónica

Formato estandarizado y legible por máquina para el intercambio seguro e
interoperable de datos sanitarios en toda la UE. Según el EHDS debe incluir:
**conjuntos de datos armonizados** (estructuras de datos — campos y grupos —
para representar el contenido clínico), **sistemas de codificación y valores**
(consistencia terminológica: SNOMED CT, LOINC, ICD-10/CIE-10…), y
**especificaciones técnicas de interoperabilidad** (representación del
contenido, estándares, perfiles — p. ej. HL7 FHIR, IPS/*International Patient
Summary*). Permite a los ciudadanos acceder y compartir su historial de salud,
en particular al consultar especialistas o recibir tratamiento de urgencia en
otro país de la UE (vía **MyHealth@EU**).

---

## 4. Calendario de aplicación (verificar por web — muy volátil)

- El Reglamento entró en vigor en 2025. Los dos **componentes armonizados**
  (interoperabilidad y registro de accesos) son obligatorios en los sistemas
  EHR **desde principios de 2029** para el primer grupo de categorías
  prioritarias, y **desde principios de 2031** para el segundo grupo — **estas
  fechas dependen de los actos de ejecución** de la Comisión que aún deben
  detallar las especificaciones técnicas (art. 36) del EEHRxF y de los
  componentes armonizados; **confirmar el estado exacto por web** antes de
  concluir plazos vinculantes.
- Aunque la exigibilidad plena esté diferida, **recomienda empezar ya**: el
  diseño de un sistema que almacena/exporta categorías prioritarias sin poder
  producir/consumir EEHRxF es una brecha de arquitectura cara de corregir
  tarde.

---

## 5. Relación con el MDR/IVDR y con el RGPD

- **No son excluyentes.** Un software puede ser a la vez: (a) **MDSW/IVD MDSW**
  bajo MDR/IVDR (si califica como producto sanitario por su finalidad
  diagnóstica/terapéutica — ver `calificacion-clasificacion.md` e
  `ivdr-diagnostico-in-vitro.md`), y (b) **sistema EHR** bajo EHDS (si además
  almacena/intermedia/exporta categorías prioritarias). En ese caso hay **dos
  regímenes de marcado CE y dos declaraciones de conformidad** que conviven,
  cada uno con su base legal, su documentación técnica y (si aplica) su
  organismo notificado.
- El EHDS **no sustituye** al RGPD: el uso primario de los datos (asistencia
  al paciente) sigue bajo RGPD/LOPDGDD íntegramente (ver `rgpd-datos.md`); el
  EHDS añade requisitos de **interoperabilidad y seguridad técnica** del
  propio sistema, no una nueva base jurídica de tratamiento para uso primario.
- **Uso secundario (Capítulo IV EHDS):** si el proyecto **reutiliza** datos de
  salud (propios o agregados de terceros) con fines de investigación,
  innovación, políticas públicas o formación de modelos de IA, entra en juego
  el régimen de **organismos de acceso a los datos de salud** (*Health Data
  Access Bodies*, art. 65) y el **permiso de datos** (*data permit*): solicitud
  motivada, evaluación por el organismo de acceso, entorno seguro de
  tratamiento, y prohibiciones expresas (p. ej. no reidentificar, no usar para
  decisiones perjudiciales sobre el individuo, no usar para publicidad dirigida
  a profesionales o pacientes). Aplica **además** de la base jurídica RGPD del
  tratamiento primario. Señalar como aplicable si `signals.usa_ia_ml` +
  `ai_ml.entrenamiento` sobre datos de salud reutilizados, o si el usuario
  declara finalidad de investigación/estadística con datos de terceros.
- **Organismo/autoridad:** a nivel UE, la Comisión y el futuro **Consejo del
  EHDS**; a nivel nacional, cada Estado debe designar **autoridades de
  vigilancia del mercado** para sistemas EHR (probablemente coordinadas con
  AEMPS/Ministerio de Sanidad en España — **verificar designación española por
  web**, aún no consolidada a la fecha de referencia) y un **organismo de
  acceso a los datos de salud** para uso secundario. No confundir con la AEPD
  (que sigue siendo la autoridad de protección de datos para el uso primario).

---

## 6. Entregables si aplica el EHDS

Además del catálogo de `entregables-datos-y-seguridad.md`, para un sistema EHR
añade en la sección de cumplimiento:

| Documento | ¿Obligatorio? | Contenido mínimo |
|---|---|---|
| Análisis de calificación como "sistema EHR" | Siempre que se traten categorías prioritarias — documentarlo aunque la conclusión sea "no aplica" | Categorías prioritarias tratadas, rol del software (almacena/intermedia/exporta/importa/convierte/edita/visualiza), usuarios (profesional/paciente) |
| Documentación técnica EHDS (art. 37) | Si es sistema EHR | Descripción del sistema, componentes armonizados, resultados de las pruebas del art. 40, evidencia de cumplimiento del Anexo II |
| Declaración UE de conformidad EHDS (art. 39) + marcado CE EHDS (art. 41) | Si es sistema EHR | Análoga en estructura a la del MDR pero bajo el EHDS; puede coexistir con la del MDR si también es producto sanitario |
| Registro en la base de datos UE de sistemas EHR (art. 49) | Si es sistema EHR, antes de comercializar | Datos del fabricante, resultados de evaluación de componentes armonizados |
| Solicitud de permiso de datos (*data permit*) ante el organismo de acceso | Si hay uso secundario de datos de salud (investigación, entrenamiento de IA con datos reutilizados) | Finalidad, entorno seguro de tratamiento, medidas de minimización/anonimización |

---

## 7. Salida esperada del paso

1. **¿Es sistema EHR?** — con la justificación (categorías prioritarias +
   rol del software).
2. **Requisitos esenciales del Anexo II**: estado (cubierto/parcial/ausente)
   de interoperabilidad (¿exporta/importa en un formato estándar tipo
   HL7 FHIR/IPS, antecedente práctico del EEHRxF?) y de seguridad/registro de
   accesos (¿hay `access log` de quién consulta qué historia clínica?).
3. **Fecha de exigibilidad aplicable** (verificada por web) y qué hacer ya
   aunque esté diferida.
4. **¿Hay uso secundario de datos de salud?** (investigación, entrenamiento de
   IA reutilizando datos de terceros) → régimen de permiso de datos.
5. Entregables pendientes de la tabla §6, con estado y cómo se generan.
6. Aclarar que el EHDS **no sustituye** ni al MDR/IVDR ni al RGPD: se suman.
