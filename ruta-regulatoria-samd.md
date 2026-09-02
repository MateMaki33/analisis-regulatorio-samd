# Ruta regulatoria para software sanitario (SaMD) en España

Mapa de normativa española y europea para diseñar, certificar y comercializar una aplicación o software como producto sanitario (clase I, IIa, IIb o III).

> **Nota de uso.** Documento orientativo de planificación, construido a partir de fuentes oficiales (AEMPS, Comisión Europea/MDCG, BOE, AEPD, ISO/IEC). No sustituye asesoría legal ni regulatoria específica: antes de decisiones vinculantes, verifica el texto vigente en [EUR-Lex](https://eur-lex.europa.eu), [BOE](https://www.boe.es) y la web de la [AEMPS](https://www.aemps.gob.es), y confirma con un organismo notificado o consultora regulatoria la clasificación real de tu producto.

---

## Índice

1. [Jerarquía normativa](#1-jerarquía-normativa)
2. [¿Es tu software un producto sanitario?](#2-es-tu-software-un-producto-sanitario)
3. [Clasificación por riesgo](#3-clasificación-por-riesgo)
4. [Ruta a la conformidad, paso a paso](#4-ruta-a-la-conformidad-paso-a-paso)
5. [Sistema de gestión de calidad](#5-sistema-de-gestión-de-calidad)
6. [Gestión de riesgos](#6-gestión-de-riesgos)
7. [Ciclo de vida del software](#7-ciclo-de-vida-del-software)
8. [Usabilidad](#8-usabilidad)
9. [Ciberseguridad](#9-ciberseguridad)
10. [Evaluación clínica](#10-evaluación-clínica)
11. [Inteligencia artificial](#11-inteligencia-artificial)
12. [Protección de datos](#12-protección-de-datos)
13. [Registro y trazabilidad](#13-registro-y-trazabilidad)
14. [Organismo notificado en España](#14-organismo-notificado-en-españa)
15. [Vigilancia poscomercialización](#15-vigilancia-poscomercialización)
16. [Normas técnicas complementarias](#16-normas-técnicas-complementarias)
17. [Todas las fuentes consultadas](#17-todas-las-fuentes-consultadas)

---

## 1. Jerarquía normativa

Un software sanitario en España queda sujeto a capas superpuestas de normativa. Así se ordenan de la más vinculante a la más orientativa:

1. **Reglamento (UE) 2017/745 (MDR)** — Directamente aplicable en toda la UE desde el 26 de mayo de 2021, sin necesidad de trasposición. Sustituye a las directivas 90/385/CEE y 93/42/CEE. Es la norma matriz: clasificación, requisitos generales de seguridad y funcionamiento (Anexo I), evaluación de conformidad, marcado CE.
2. **Real Decreto 192/2023** — Desarrollo nacional del MDR en España (21 marzo 2023): régimen sancionador, registros AEMPS, requisitos de idioma, fabricación "in house" y a medida, venta y publicidad.
3. **Guías MDCG y documentos de la Comisión Europea** — Sin valor jurídico vinculante per se, pero de referencia obligada: fijan el criterio que aplican organismos notificados y autoridades (AEMPS incluida) para calificación de software, clasificación, ciberseguridad, evaluación clínica.
4. **Normas armonizadas ISO/IEC (UNE-EN en España)** — Voluntarias en sentido estricto, pero cumplirlas genera "presunción de conformidad" con los requisitos esenciales del MDR. En la práctica, ningún organismo notificado certifica sin ellas: ISO 13485, ISO 14971, IEC 62304, IEC 62366-1, IEC 81001-5-1.
5. **Normativa horizontal (no específica de producto sanitario)** — Se aplica en paralelo, no en sustitución del MDR: RGPD y LOPDGDD (datos de salud), Reglamento de IA (si hay algoritmos de IA), Reglamento de Ciberresiliencia y Directiva NIS2 (ciberseguridad de productos y de la organización).
6. **Normativa sanitaria general española** — Ley 41/2002 (autonomía del paciente e historia clínica) y Ley 14/1986 General de Sanidad, relevantes si el software trata historia clínica, apoya decisiones clínicas o requiere consentimiento informado.

**Fuentes:** [AEMPS — Legislación sobre productos sanitarios](https://www.aemps.gob.es/la-aemps/legislacion/legislacion-sobre-productos-sanitarios/) · [EUR-Lex — Reglamento (UE) 2017/745](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32017R0745) · [BOE — Real Decreto 192/2023](https://www.boe.es/buscar/doc.php?id=BOE-A-2023-7038)

---

## 2. ¿Es tu software un producto sanitario?

El primer filtro no es técnico sino de **"finalidad prevista"** (intended purpose). Según la guía `MDCG 2019-11`, un software es producto sanitario (MDSW, Medical Device Software) cuando su fabricante le atribuye, explícitamente, una finalidad médica específica recogida en la definición del art. 2.1 MDR.

### Test de calificación (MDCG 2019-11)

Se considera MDSW cuando el software realiza una acción sobre datos distinta del mero almacenamiento, archivo, comunicación o búsqueda simple, y esa acción persigue uno de estos fines: diagnóstico, prevención, monitorización, tratamiento o alivio de una enfermedad; predicción o pronóstico de una enfermedad; compensación de una lesión o discapacidad; investigación o sustitución de un proceso o estado fisiológico; o control de la concepción.

### Dentro y fuera del ámbito

| Sí es producto sanitario | Normalmente no lo es |
|---|---|
| App que calcula dosis de insulina a partir de datos del paciente | App de gestión de citas o facturación hospitalaria |
| Software de ayuda al diagnóstico por imagen (detección de lesiones) | Diario de síntomas de uso puramente personal sin recomendación clínica |
| Algoritmo que estratifica riesgo clínico para orientar tratamiento | App de bienestar general (fitness, mindfulness) sin finalidad médica declarada |
| Sistema de soporte a decisión clínica con alertas diagnósticas | Historia clínica electrónica que solo almacena y muestra datos sin interpretarlos |

La frontera real depende de la finalidad prevista declarada por el fabricante y de casos límite recogidos en el *Manual on Borderline and Classification* de la Comisión Europea (PACS, calculadoras clínicas, apps de estilo de vida). Ante la duda, documenta el análisis de calificación: es lo primero que pide un organismo notificado.

**Fuentes:** [MDCG 2019-11 Rev.1 — Qualification and classification of software (PDF, Comisión Europea)](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=md_mdcg_2019_11_guidance_qualification_classification_software_en.pdf) · [Consultoría de producto sanitario — MDCG 2019-11 Rev.1](https://productosanitario.es/producto-sanitario-software-mdcg-2019-11/)

---

## 3. Clasificación por riesgo

Una vez calificado como producto sanitario, el software se clasifica en I, IIa, IIb o III según el riesgo que representa. La **Regla 11** del Anexo VIII MDR es específica para software y decide la clase según la gravedad de la información que aporta y el estado del paciente.

| Clase | Regla 11 — criterio | Vía de evaluación | Ejemplos orientativos |
|---|---|---|---|
| **I** | Decisiones que no influyen directamente en el diagnóstico/tratamiento, o software para situaciones no críticas | Autocertificación del fabricante | Software de registro de síntomas sin interpretación clínica |
| **IIa** | Aporta información usada para decisiones con impacto diagnóstico/terapéutico menor, o monitoriza procesos fisiológicos no vitales | Organismo notificado | App que sugiere ajustes de medicación no crítica |
| **IIb** | Decisiones con impacto grave en el estado de salud, o monitorización de parámetros fisiológicos vitales | Organismo notificado | Software que calcula dosis de fármacos de alto riesgo; monitorización de signos vitales críticos |
| **III** | Decisiones con impacto que puede causar la muerte o un deterioro irreversible del estado de salud | Organismo notificado (máximo escrutinio) | Software de soporte a decisión en situaciones vitales agudas (p. ej. algoritmos oncológicos de alto impacto) |

**Regla general de clasificación de software (MDCG 2019-11):** primero se aplican las reglas de clasificación estándar del Anexo VIII; si el software controla o influye en otro producto sanitario, hereda su clase; si es independiente, se clasifica según la Regla 11 según el destino de la información que genera y la gravedad de la condición del paciente al que se dirige.

La clasificación exacta requiere leer la Regla 11 completa y, en casos límite, contrastarla con la `MDCG 2021-24 Rev.1` (que aclara, entre otros puntos, el software con función de medición) y con el organismo notificado.

**Fuentes:** [MDCG 2021-24 Rev.1 — Guidance on classification of medical devices (PDF)](https://health.ec.europa.eu/system/files/2021-10/mdcg_2021-24_en_0.pdf) · [AEMPS — Guía para la comercialización de productos sanitarios (2025, PDF)](https://www.aemps.gob.es/productosSanitarios/docs/2025/guia-comercializacion-ps-2025.pdf)

---

## 4. Ruta a la conformidad, paso a paso

Secuencia operativa recogida por la AEMPS para llevar un producto sanitario (incluido software) desde el diseño hasta el mercado.

1. **Determinación** — Fija producto, finalidad prevista y clasificación (secciones 2–3). Documéntalo por escrito: es la base de todo lo demás.
2. **Elección de procedimiento** — Autocertificación (clase I) o intervención de organismo notificado (IIa, IIb, III), según Anexos IX-XI del MDR.
3. **Sistema de gestión de calidad** — Implanta un SGC conforme a ISO 13485, ajustado a la clase de riesgo (sección 5).
4. **Documentación técnica** — Prepárala conforme a los Anexos II y III del MDR: descripción del producto, especificaciones de diseño, gestión de riesgos, verificación y validación, información suministrada al usuario.
5. **Identificación y trazabilidad** — Asigna UDI-DI y registra el producto y los agentes económicos en EUDAMED (sección 13).
6. **Evaluación clínica** — Genera evidencia de seguridad y funcionamiento conforme a `MDCG 2020-1` (sección 10).
7. **Declaración UE de conformidad y marcado CE** — Se emite tras completar la evaluación de conformidad correspondiente a la clase de riesgo.
8. **Vigilancia poscomercialización** — Plan de PMS activo, informes periódicos (PSUR en IIa/IIb/III) y notificación de incidentes graves a la AEMPS (sección 15).

**Fuentes:** [AEMPS — Guía para la comercialización de productos sanitarios (2025, PDF)](https://www.aemps.gob.es/productosSanitarios/docs/2025/guia-comercializacion-ps-2025.pdf) · [Ministerio de Sanidad — Guía del proceso de marcado CE en España (PDF)](https://www.sanidad.gob.es/areas/saludDigital/estrategiaIASNS/doc/IASNS_Guia_ProcesoMarcadoCE_Espana_PS.pdf)

---

## 5. Sistema de gestión de calidad

Obligatorio para cualquier clase de riesgo, aunque con exigencias crecientes según la clase.

**`ISO 13485:2016`** — Sistemas de gestión de la calidad — Productos sanitarios. Es el estándar de referencia para el SGC de un fabricante de software sanitario: control de diseño y desarrollo, control documental, gestión de proveedores, CAPA (acciones correctivas y preventivas), auditorías internas. Ningún organismo notificado certificará un producto de clase IIa o superior sin un SGC certificado o auditado bajo esta norma.

**Fuente:** [Visure Solutions — ISO Standards for Medical Devices](https://visuresolutions.com/medtech-and-pharma-guide/ultimate-iso-compliance-guide/)

---

## 6. Gestión de riesgos

**`ISO 14971:2019`** — Aplicación de la gestión de riesgos a los productos sanitarios. Marco de identificación, evaluación, control y seguimiento de riesgos durante todo el ciclo de vida. Se complementa con la guía técnica `ISO/TR 24971` para su aplicación práctica. Su archivo de gestión de riesgos (risk management file) es un documento que el organismo notificado audita en detalle.

**Fuente:** [Visure Solutions — ISO Standards for Medical Devices](https://visuresolutions.com/medtech-and-pharma-guide/ultimate-iso-compliance-guide/)

---

## 7. Ciclo de vida del software

**`IEC 62304:2006 + AMD1:2015`** — Software de productos sanitarios — Procesos del ciclo de vida. Norma central para desarrollo de SaMD: exige clasificar el software en clase de seguridad **A** (sin lesión posible), **B** (lesión no grave posible) o **C** (lesión grave o muerte posible), y define los procesos exigidos según esa clase — planificación, análisis de requisitos, arquitectura, diseño detallado, implementación, integración, verificación, liberación y mantenimiento. Es la norma que más condiciona la arquitectura de desarrollo (control de versiones, trazabilidad de requisitos, pruebas unitarias e de integración documentadas).

**Fuentes:** [Visure Solutions — IEC 62304 Software Lifecycle Standard](https://visuresolutions.com/medtech-and-pharma-guide/iec-62304) · [SG Systems — IEC 62304, ciclo de vida del software](https://sgsystemsglobal.com/glossary/iec-62304/)

---

## 8. Usabilidad

**`IEC 62366-1:2015 + AMD1:2020`** — Aplicación de la ingeniería de usabilidad a los productos sanitarios. Exige un proceso formal de ingeniería de usabilidad: especificación de usuarios, entornos de uso y escenarios críticos; evaluación formativa y sumativa de la interfaz; identificación de errores de uso que puedan causar daño. Es especialmente relevante en software clínico, donde un error de interfaz (unidad de dosis mal mostrada, alerta ignorada) es una vía de daño real.

**Fuente:** [Attract Group — Medical Device Software Standards](https://attractgroup.com/blog/iso-and-iec-standards-for-samd-breakdown-of-medical-devices/)

---

## 9. Ciberseguridad

Requisito explícito del MDR (Anexo I, punto 17) y con desarrollo propio a través de una norma técnica, una guía MDCG y dos normas horizontales de la UE.

**`IEC 81001-5-1:2021`** — Seguridad de software y sistemas de TI sanitarios — Actividades de seguridad en el ciclo de vida del producto. Norma armonizada específica de ciberseguridad para software sanitario: seguridad por diseño, gestión de vulnerabilidades, gestión de parches durante el ciclo de vida completo (incluida la fase de mantenimiento poscomercialización).

**`MDCG 2019-16 Rev.1`** — Guidance on Cybersecurity for medical devices. Interpreta los requisitos de ciberseguridad del MDR: gestión del riesgo de ciberseguridad integrada en ISO 14971, requisitos de diseño seguro, gestión de la cadena de suministro de software (incluidas librerías de terceros y SBOM), plan de gestión de vulnerabilidades poscomercialización.

### Normativa horizontal de ciberseguridad

- **Reglamento de Ciberresiliencia — Cyber Resilience Act, (UE) 2024/2847.** Aplica a productos con elementos digitales en general. Los productos sanitarios ya cubiertos por requisitos de ciberseguridad del MDR/IVDR quedan, en principio, fuera de su alcance directo para evitar duplicidad regulatoria — pero conviene revisar caso por caso, especialmente si parte del software (por ejemplo, un componente que no califica como producto sanitario) queda fuera del MDR.
- **Directiva NIS2 — (UE) 2022/2555.** Obliga a gestión de riesgos de ciberseguridad y notificación de incidentes a nivel organizativo (no de producto) a entidades del sector salud consideradas esenciales o importantes según su tamaño. Su trasposición a derecho español está en curso/avanzada; conviene verificar el estado actualizado en el Centro Criptológico Nacional (CCN) o INCIBE-CERT antes de fijar el alcance exacto para tu organización.

**Fuentes:** [MDCG 2019-16 Rev.1 — Guidance on Cybersecurity for medical devices (PDF)](https://health.ec.europa.eu/system/files/2022-01/md_cybersecurity_en.pdf) · [Johner Institute — IEC 81001-5-1](https://blog.johner-institute.com/iec-62304-medical-software/iec-81001-5-1/) · [QC Analytics — Cyber Resilience Act and MDR Medical Software](https://qc-analytics.com/blog/cyber-resilience-act-and-mdr-medical-software/) · [INCIBE-CERT — Cómo afecta NIS2 al sector salud](https://www.incibe.es/incibe-cert/blog/como-afecta-la-directiva-europea-nis2-al-sector-salud) · [CCN-CNI — Directiva NIS2](https://www.ccn.cni.es/es/normativa/directiva-nis2)

---

## 10. Evaluación clínica

Todo producto sanitario, incluido el software, necesita evidencia de que cumple su finalidad prevista con seguridad. Para software, la guía de referencia es la `MDCG 2020-1` (evaluación clínica / de funcionamiento del software), que admite tres vías de evidencia: validación clínica (rendimiento en la población destino), validación analítica/técnica (el software procesa correctamente los datos de entrada) y evidencia científica de la literatura. Para software de mayor riesgo suele exigirse combinar las tres.

La metodología general de evaluación clínica sigue apoyándose en `MEDDEV 2.7/1 Rev.4`, guía preexistente al MDR pero todavía usada como referencia metodológica por organismos notificados. Los cambios significativos posteriores a la certificación se valoran conforme a `MDCG 2020-3` (art. 120 MDR); el uso de un producto "equivalente" como evidencia, conforme a `MDCG 2020-5`.

**Fuente:** [MD101 Consulting — The essential list of guidances for software medical devices](https://blog.cm-dm.com/pages/The-essential-list-of-guidances-for-software-medical-devices)

---

## 11. Inteligencia artificial

Si tu software incorpora IA/machine learning con función diagnóstica, de tratamiento o de soporte a decisión clínica, se le suma el Reglamento de IA europeo sobre el marco del MDR — no lo sustituye.

**Reglamento (UE) 2024/1689 (AI Act)**, en vigor desde agosto de 2024 con aplicación escalonada hasta 2027. Un sistema de IA que sea, a la vez, un producto sanitario sujeto a evaluación de conformidad por tercero (organismo notificado) bajo el MDR — es decir, típicamente clase IIa y superiores — se considera automáticamente sistema de IA de **alto riesgo** (art. 6.1 y Anexo I, sección A, que remite al MDR).

### Obligaciones adicionales para IA de alto riesgo

- Sistema de gestión de riesgos de IA, integrado con el de ISO 14971
- Gobernanza y calidad de los datos de entrenamiento, validación y prueba
- Documentación técnica y registro/logging automático (trazabilidad de decisiones del sistema)
- Transparencia e información clara al usuario sobre el funcionamiento y limitaciones del sistema
- Supervisión humana efectiva
- Exactitud, robustez y ciberseguridad demostrables

La evaluación de conformidad de IA de alto riesgo se integra, cuando el producto ya requiere organismo notificado por el MDR, en el mismo procedimiento — evitando una doble certificación, pero exigiendo que el organismo notificado tenga también designación para IA.

**Fuentes:** [EUR-Lex — Reglamento (UE) 2024/1689 (Reglamento de IA)](https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX%3A32024R1689) · [BOE — Reglamento (UE) 2024/1689](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-81079) · [Ministerio de Sanidad — Guía del proceso de marcado CE en España (PDF, incluye requisitos de IA)](https://www.sanidad.gob.es/areas/saludDigital/estrategiaIASNS/doc/IASNS_Guia_ProcesoMarcadoCE_Espana_PS.pdf)

---

## 12. Protección de datos

Un software sanitario casi siempre trata datos de salud: categoría especial de datos bajo el RGPD, con obligaciones reforzadas independientes del MDR.

### RGPD y LOPDGDD

Los datos de salud son "categoría especial" (art. 9 RGPD): su tratamiento está prohibido salvo que concurra una excepción — típicamente consentimiento explícito (art. 9.2.a) o finalidad de asistencia sanitaria por profesional sujeto a secreto (art. 9.2.h). La **LO 3/2018 (LOPDGDD)** desarrolla el régimen español, incluyendo reglas específicas sobre consentimiento de menores y tratamiento con fines de investigación en salud. Una Evaluación de Impacto en Protección de Datos (EIPD/DPIA, art. 35 RGPD) es, en la práctica, casi siempre exigible para una app de salud que trate datos de pacientes a escala.

La AEPD ha publicado directrices específicas sobre **apps móviles de salud y bienestar** y una guía sobre los **derechos de protección de datos de pacientes y usuarios de la sanidad**, con criterios prácticos sobre bases jurídicas, encargados de tratamiento y transferencias.

### Ley 41/2002 — autonomía del paciente

Relevante si el software gestiona historia clínica, apoya decisiones clínicas o requiere consentimiento informado del paciente: fija los derechos de información asistencial, el régimen del consentimiento informado y las obligaciones de conservación y acceso a la documentación clínica.

**Fuentes:** [AEPD — Directrices para apps móviles educativas, de actividad física, bienestar y salud](https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-publica-unas-directrices-orientadas-aplicaciones) · [AEPD — Guía de derechos de protección de datos de pacientes y usuarios de la sanidad](https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-publica-una-guia-en-la-que-recoge-los-derechos-de) · [Iberley — Categorías especiales de datos en el RGPD y la LOPDGDD](https://www.iberley.es/temas/categorias-especiales-datos-rgpd-lopdgdd-62726) · [BOE — Ley 41/2002, autonomía del paciente](https://www.boe.es/buscar/doc.php?id=BOE-A-2002-22188)

---

## 13. Registro y trazabilidad

### EUDAMED (base de datos europea)

Registro obligatorio de agentes económicos (con número único SRN), de productos (con identificador UDI-DI) y de certificados. Su implantación es progresiva por módulos; el **Reglamento (UE) 2024/1860** ajusta el calendario de obligatoriedad conforme se activan los distintos módulos, con hitos relevantes previstos hacia 2026-2027. Conviene revisar el calendario vigente en la AEMPS antes de planificar el lanzamiento.

### Registros AEMPS en España

- **Licencia previa de funcionamiento** — exigible para actividades de fabricación, importación o esterilización de productos sanitarios.
- **Registro de Comercialización** (aplicación CCPS) — para productos de clase IIa, IIb y III.
- **Registro de Responsables** — para productos de clase I y productos a medida.
- **Responsable técnico con titulación universitaria superior**, designado por el fabricante.

La trazabilidad documental (UDI-DI, número de serie/lote, agentes económicos de la cadena) debe mantenerse por cada agente económico que comercialice en España; los productos implantables de clase III exigen además UDI completo en cada unidad.

**Fuentes:** [AEMPS — Guía para la comercialización de productos sanitarios (2025, PDF)](https://www.aemps.gob.es/productosSanitarios/docs/2025/guia-comercializacion-ps-2025.pdf) · [Cuatrecasas — Módulos de EUDAMED obligatorios](https://www.cuatrecasas.com/es/spain/farmaceutico-sanitario/art/eudamed-productos-sanitarios-modulos-obligatorios) · [AEMPS — Puesta en marcha de nuevos módulos EUDAMED](https://www.aemps.gob.es/informa/informacion-sobre-la-puesta-en-marcha-de-dos-nuevos-modulos-de-la-base-de-datos-eudamed/)

---

## 14. Organismo notificado en España

Para clases IIa, IIb y III, la evaluación de conformidad la realiza un organismo notificado (cualquiera designado en la UE, no necesariamente español). En España, el único organismo notificado designado es el **Centro Nacional de Certificación de Productos Sanitarios (CNCps, nº 0318)**.

### Procedimiento CNCps

Evaluación preliminar → examen y aceptación a trámite de la solicitud → evaluación de la documentación técnica → auditoría del sistema de calidad → emisión del certificado (validez máxima 5 años). La documentación debe presentarse en español (los textos científicos suelen admitirse en inglés).

> Coste orientativo citado por consultoras del sector: entre 22.000 € y 27.000 € solo en tasas de certificación CNCps para clases IIa-III; el coste total del proyecto (documentación, consultoría, ensayos) suele situarse, según estimaciones del sector, entre 200.000 € y 800.000 €. Son cifras orientativas de mercado, no tarifas oficiales: confírmalas directamente con el CNCps y con tu consultora.

**Fuente:** [Ministerio de Sanidad — Guía del proceso de marcado CE en España (PDF)](https://www.sanidad.gob.es/areas/saludDigital/estrategiaIASNS/doc/IASNS_Guia_ProcesoMarcadoCE_Espana_PS.pdf)

---

## 15. Vigilancia poscomercialización

El marcado CE no cierra el expediente: el MDR exige vigilancia activa durante toda la vida comercial del producto.

- **Plan de vigilancia poscomercialización (PMS)** — Anexo III MDR, proporcional a la clase de riesgo.
- **Informe PMS** (clase I) o **PSUR** — informe periódico de seguridad, actualizado con mayor frecuencia cuanto mayor sea la clase (IIa, IIb, III).
- **Notificación de incidentes graves** a la AEMPS, con plazos breves diferenciados según gravedad (art. 87 MDR): más cortos ante riesgo grave para la salud pública o muerte/deterioro grave del estado de salud, algo más amplios para el resto de incidentes graves.
- **Portal NotificaPS** — canal de la AEMPS por el que también profesionales sanitarios y pacientes pueden notificar incidentes.
- **Acciones correctivas de seguridad de campo (FSCA)** comunicadas mediante avisos de seguridad (FSN, Field Safety Notice) a usuarios y autoridades.

**Fuentes:** [AEMPS — Guía para la comercialización de productos sanitarios (2025, PDF)](https://www.aemps.gob.es/productosSanitarios/docs/2025/guia-comercializacion-ps-2025.pdf) · [Thema — El Plan de Vigilancia Post-Mercado (PMSP)](https://www.thema-med.com/es/2023/07/27/el-plan-de-vigilancia-post-mercado-pmsp/)

---

## 16. Normas técnicas complementarias

Según el perfil exacto del producto, pueden sumarse estas normas.

| Norma | Cubre | Cuándo aplica |
|---|---|---|
| `ISO/IEC 82304-1:2016` | Requisitos generales de seguridad de producto para "health software" | Software de salud independiente, incluido el que no llega a calificar como producto sanitario bajo MDR |
| `ISO/IEC 27001` | Sistema de gestión de seguridad de la información (SGSI), de alcance general | Buena práctica transversal para cualquier organización que trate datos de salud; a menudo exigida por hospitales y aseguradoras como cliente |
| `ISO 27799:2016` | Gestión de seguridad de la información en el sector salud, aplicando ISO/IEC 27002 al contexto sanitario | Organizaciones sanitarias y proveedores que gestionan información clínica |
| `ISO 20417:2021` | Información suministrada por el fabricante (etiquetado, instrucciones de uso) | Requisitos de etiquetado e IFU de cualquier producto sanitario |
| `IEC 60601-1` | Seguridad básica y funcionamiento esencial de equipos electromédicos | Solo si el software se integra con hardware médico propio (no aplica a software puro) |

**Fuentes:** [ISO — IEC 82304-1:2016, Health software](https://www.iso.org/standard/59543.html) · [PMG SSI — ISO 27001 e ISO 27799 en el sector salud](https://www.pmg-ssi.com/2016/06/norma-iso-27001-iso-27799-sector-salud/)

---

## 17. Todas las fuentes consultadas

### Fuentes oficiales españolas

- [AEMPS — Legislación sobre productos sanitarios](https://www.aemps.gob.es/la-aemps/legislacion/legislacion-sobre-productos-sanitarios/)
- [AEMPS — Guía para la comercialización de productos sanitarios (2025)](https://www.aemps.gob.es/productosSanitarios/docs/2025/guia-comercializacion-ps-2025.pdf)
- [Ministerio de Sanidad — Guía del proceso de marcado CE en España](https://www.sanidad.gob.es/areas/saludDigital/estrategiaIASNS/doc/IASNS_Guia_ProcesoMarcadoCE_Espana_PS.pdf)
- [BOE — Real Decreto 192/2023](https://www.boe.es/buscar/doc.php?id=BOE-A-2023-7038)
- [BOE — Ley 41/2002](https://www.boe.es/buscar/doc.php?id=BOE-A-2002-22188)
- [BOE — Reglamento (UE) 2024/1689 (IA)](https://www.boe.es/buscar/doc.php?id=DOUE-L-2024-81079)
- [AEPD — Directrices apps de salud y bienestar](https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-publica-unas-directrices-orientadas-aplicaciones)
- [AEPD — Guía de derechos de protección de datos en sanidad](https://www.aepd.es/prensa-y-comunicacion/notas-de-prensa/la-aepd-publica-una-guia-en-la-que-recoge-los-derechos-de)
- [CCN-CNI — Directiva NIS2](https://www.ccn.cni.es/es/normativa/directiva-nis2)
- [INCIBE-CERT — NIS2 y sector salud](https://www.incibe.es/incibe-cert/blog/como-afecta-la-directiva-europea-nis2-al-sector-salud)

### Fuentes UE / Comisión Europea

- [EUR-Lex — Reglamento (UE) 2017/745 (MDR)](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32017R0745)
- [EUR-Lex — Reglamento (UE) 2024/1689 (AI Act)](https://eur-lex.europa.eu/legal-content/ES/ALL/?uri=CELEX%3A32024R1689)
- [MDCG 2019-11 Rev.1](https://health.ec.europa.eu/document/download/b45335c5-1679-4c71-a91c-fc7a4d37f12b_en?filename=md_mdcg_2019_11_guidance_qualification_classification_software_en.pdf)
- [MDCG 2021-24 Rev.1](https://health.ec.europa.eu/system/files/2021-10/mdcg_2021-24_en_0.pdf)
- [MDCG 2019-16 Rev.1 (ciberseguridad)](https://health.ec.europa.eu/system/files/2022-01/md_cybersecurity_en.pdf)

### Normas técnicas y análisis del sector

- [ISO — IEC 82304-1:2016](https://www.iso.org/standard/59543.html)
- [Visure Solutions — IEC 62304](https://visuresolutions.com/medtech-and-pharma-guide/iec-62304)
- [Visure Solutions — Guía de cumplimiento ISO](https://visuresolutions.com/medtech-and-pharma-guide/ultimate-iso-compliance-guide/)
- [Johner Institute — IEC 81001-5-1](https://blog.johner-institute.com/iec-62304-medical-software/iec-81001-5-1/)
- [MD101 Consulting — Guidances for software medical devices](https://blog.cm-dm.com/pages/The-essential-list-of-guidances-for-software-medical-devices)
- [Consultoría de producto sanitario — Software MDCG 2019-11](https://productosanitario.es/producto-sanitario-software-mdcg-2019-11/)
- [QC Analytics — Cyber Resilience Act y MDR](https://qc-analytics.com/blog/cyber-resilience-act-and-mdr-medical-software/)
- [PMG SSI — ISO 27001/27799 en salud](https://www.pmg-ssi.com/2016/06/norma-iso-27001-iso-27799-sector-salud/)
- [Iberley — Categorías especiales de datos](https://www.iberley.es/temas/categorias-especiales-datos-rgpd-lopdgdd-62726)

---

*Documento de referencia elaborado a partir de fuentes públicas citadas en cada sección. La normativa de productos sanitarios y de IA está en evolución activa (calendario EUDAMED, trasposición de NIS2, aplicación escalonada del AI Act): antes de tomar decisiones de inversión o de diseño regulatorio, verifica la versión vigente de cada norma.*
