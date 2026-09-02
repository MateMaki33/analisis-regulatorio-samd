# Entregables de protección de datos y seguridad — ¿cuál debo generar?

Objetivo del paso: para cada documento, decidir si **este** proyecto **debe**
generarlo, explicar **qué es** y **cómo se genera / quién lo pide**, y marcar su
**estado** en el repo. El informe lleva una fila por documento con veredicto
*obligatorio / recomendado / no aplica* + *presente / parcial / ausente*.

Regla de honestidad: un análisis sobre el repositorio raramente encuentra estos
documentos (son documentales y externos al código). El valor está en decir
**cuáles son obligatorios**, **por qué**, y **cómo se hacen**.

---

## 1. Análisis de calificación como producto sanitario (*borderline determination*)

- **Qué es:** documento que aplica el test de MDCG 2019-11 y concluye, por
  escrito y con justificación, si el software **es o no** producto sanitario
  (y, si lo es, su clase).
- **¿Obligatorio?** **Siempre**, incluso cuando la conclusión es **"NO es
  producto sanitario"**. Es lo primero que pide un organismo notificado o la
  AEMPS en una inspección, y la defensa del fabricante frente a la acusación de
  comercializar un PS sin marcado CE. Un "no es PS" sin análisis escrito = brecha.
- **Quién lo exige:** AEMPS, organismo notificado. Referencia: MDCG 2019-11
  Rev.1, *Manual on Borderline and Classification* de la Comisión.
- **Contenido mínimo:** finalidad prevista **literal** del fabricante; las 3
  condiciones del test (software *per se*; acción sobre datos más allá de
  almacenar/archivar/comunicar/buscar/comprimir; beneficio de paciente individual
  con una finalidad del art. 2.1 MDR); casos frontera considerados; conclusión y
  clase; autor, firma y fecha; disparadores de revisión (cambio de finalidad o de
  funcionalidad).
- **Cómo se genera:** interno; contrastar con el *Manual on Borderline*; en duda,
  consulta a AEMPS. Se archiva en `docs/regulatory/`.
- **Escáner:** `signals.senal_finalidad_medica`, `clinical.*`. Ausencia de este
  análisis en `docs/` = brecha a listar.

## 2. Análisis de riesgos del tratamiento (RGPD arts. 24 y 32)

- **Qué es:** valoración del riesgo para los **derechos y libertades de las
  personas** derivado del tratamiento de datos. **No es** el análisis de riesgos
  del producto (eso es ISO 14971) ni el de ciberseguridad (IEC 81001-5-1); es el
  análisis "de partida" que **siempre** hay que hacer y que decide si además hace
  falta una DPIA.
- **¿Obligatorio?** **Siempre que haya datos personales.** Con datos de salud, el
  resultado casi siempre es "riesgo alto" → escala a DPIA (punto 3).
- **Quién lo exige:** responsabilidad proactiva (arts. 5.2 y 24); la AEPD lo
  revisa en inspección. Metodología: guía AEPD *"Gestión del riesgo y evaluación
  de impacto en tratamientos de datos personales"*.
- **Contenido mínimo:** inventario de tratamientos; tipología de datos y de
  interesados; factores de riesgo (volumen, categorías especiales, menores,
  perfilado, IA/tecnologías innovadoras, cesiones, transferencias
  internacionales); riesgo inherente; medidas; riesgo residual; **decisión
  motivada sobre si procede DPIA**.
- **Cómo se genera:** interno, con el DPO si lo hay; herramienta AEPD
  *Gestiona/EVALÚA*.
- **Escáner:** `signals.trata_pii`, `signals.categorias_especiales_rgpd`,
  `ai_ml.*`, `third_party.*`, `infra_datos.*`.

## 3. DPIA / EIPD — Evaluación de Impacto relativa a la Protección de Datos (art. 35)

- **Qué es:** evaluación **previa** y documentada del impacto de un tratamiento de
  **alto riesgo**, con las medidas para mitigarlo.
- **¿Obligatoria?** Sí si se da **alguno** de estos supuestos (art. 35.3 + lista
  AEPD de tratamientos que requieren DPIA):
  - tratamiento a **gran escala de categorías especiales** (datos de salud);
  - **observación sistemática**;
  - **tecnologías innovadoras** (IA/ML);
  - elaboración de **perfiles** con efectos significativos;
  - combinación o cruce de conjuntos de datos;
  - datos de **colectivos vulnerables** (menores, pacientes).
  → En una app sanitaria con datos de pacientes: **casi siempre obligatoria**.
- **Quién lo exige:** AEPD. Si el **riesgo residual sigue alto** tras las
  medidas → **consulta previa a la AEPD** (art. 36) **antes** de iniciar el
  tratamiento (la AEPD responde en 8 semanas, ampliables 6).
- **Contenido mínimo (art. 35.7):** descripción sistemática del tratamiento y sus
  fines; evaluación de **necesidad y proporcionalidad**; evaluación de **riesgos**
  para los derechos y libertades; **medidas** previstas (garantías, seguridad,
  mecanismos) para afrontar los riesgos y demostrar cumplimiento. Recabar parecer
  del DPO y, cuando proceda, de los interesados.
- **Cómo se genera:** interno + DPO; plantillas AEPD y EDPB (WP248 rev.01).
  Revisar cuando cambie el tratamiento.
- **Escáner:** categorías especiales + escala + IA → marca "DPIA exigible".

## 4. RAT — Registro de Actividades de Tratamiento (art. 30)

- **Qué es:** inventario documentado de todas las actividades de tratamiento del
  responsable (art. 30.1) y, en su caso, del encargado (art. 30.2).
- **¿Obligatorio?** En la práctica **siempre** en este dominio: la excepción para
  organizaciones de <250 empleados **no aplica** cuando se tratan categorías
  especiales o el tratamiento no es ocasional — que es el caso de cualquier
  software de salud.
- **Quién lo exige:** AEPD (debe poder aportarse a requerimiento).
- **Contenido mínimo (art. 30.1):** identidad y contacto del responsable /
  corresponsables / representante / DPO; fines del tratamiento; categorías de
  interesados y de datos; categorías de destinatarios; **transferencias
  internacionales** y garantías aplicadas; plazos de supresión; descripción
  general de las medidas de seguridad del art. 32.
- **Cómo se genera:** interno; plantilla AEPD; se mantiene vivo.
- **Escáner:** `pii.*`, `special_category.*`, `third_party.*`, `infra_datos.*`
  alimentan las columnas de datos, destinatarios y transferencias.

## 5. DPA — Contrato de encargado del tratamiento (art. 28)

- **Qué es:** contrato (o acto jurídico) vinculante entre responsable y cada
  **encargado** que trata datos por su cuenta. En inglés, *Data Processing
  Agreement (DPA)*.
- **¿Obligatorio?** Uno por **cada** proveedor que acceda o trate datos
  personales por cuenta del responsable: hosting/cloud, correo transaccional, SMS,
  analítica de producto, *crash reporting*, **IA como servicio**, soporte
  externo, *backups* gestionados, CRM, firma electrónica, mensajería,
  observabilidad/APM.
- **Quién lo exige:** RGPD art. 28.3; la AEPD lo comprueba.
- **Contenido mínimo (art. 28.3):** objeto, duración, naturaleza y finalidad del
  tratamiento; tipo de datos y categorías de interesados; y obligaciones del
  encargado: tratar **solo según instrucciones** (incluidas transferencias),
  confidencialidad, seguridad del art. 32, régimen de **subencargados** (art.
  28.4, autorización + traslado de obligaciones *back-to-back*), asistencia al
  responsable con los derechos y con los arts. 32-36, **supresión o devolución**
  al terminar, y someterse a **auditorías**. Anexos: descripción del tratamiento,
  medidas de seguridad, y **lista de subencargados con su país**.
- **Cómo se genera:** normalmente el DPA estándar del proveedor + revisión. Para
  proveedores fuera del EEE, incorporar **Cláusulas Contractuales Tipo (CCT)** y
  **TIA** (ver `transferencias-internacionales.md`).
- **Escáner:** `third_party.*`, `infra_datos.*`, `ai_ml.llm_apis` → lista de
  candidatos a DPA.

## 6. Procedimiento de gestión y notificación de brechas (arts. 33-34)

- **Qué es:** procedimiento interno **escrito y previo** para detectar, contener,
  evaluar, notificar y **registrar** una violación de seguridad de datos
  personales.
- **¿Obligatorio?** **Siempre.** No basta con "notificar si pasa": hay que tener
  el procedimiento definido de antemano y un **registro de todas las brechas**
  (art. 33.5), se notifiquen o no.
- **Quién lo exige:** AEPD. Notificación a la AEPD **en 72 h** desde el
  conocimiento si hay riesgo para los interesados (formulario NBD de la sede
  electrónica AEPD); **comunicación a los interesados** sin dilación indebida si
  el riesgo es **alto**.
- **Contenido mínimo:** roles y escalado; criterios de evaluación del riesgo;
  árbol de decisión de notificación; plantillas (AEPD e interesados); plazos;
  registro de brechas; **enganche con el plan de respuesta a incidentes de
  ciberseguridad** (IEC 81001-5-1) y con la **vigilancia MDR** (AEMPS/NotificaPS
  si además hay incidente grave del producto).
- **Cómo se genera:** interno; guía AEPD *"Gestión y notificación de brechas de
  seguridad"*.
- **Escáner:** `SECURITY.md`, `docs/incident*`, *runbooks*. Ausencia = brecha
  organizativa.

## 7. TIA — Transfer Impact Assessment

Ver `references/transferencias-internacionales.md` §3. Resumen: **obligatorio**
cuando alguna transferencia a un tercer país se apoya en el art. 46 (CCT, BCR…).
**No** se necesita si el destino tiene **decisión de adecuación** o si el
proveedor está adherido al **EU-US Data Privacy Framework** para esa transferencia
concreta (verificar por web).

## 8. Cláusulas informativas / política de privacidad en capas (arts. 12-14)

- **Qué es:** información a los interesados sobre el tratamiento, en capas
  (capa breve + capa detallada).
- **¿Obligatoria?** Siempre que se recojan datos, del interesado o de terceros.
- **Contenido:** identidad del responsable y del DPO; **fines y base jurídica**
  (art. 6 y, para salud, excepción del art. 9); destinatarios; **transferencias
  internacionales** y garantías; plazos de conservación; **derechos** y cómo
  ejercerlos; derecho a reclamar ante la AEPD; origen de los datos si no se
  obtienen del interesado; existencia de **decisiones automatizadas / perfilado**
  y lógica aplicada.
- **Escáner:** `privacy_controls.*`, textos legales, endpoints de derechos
  (acceso / borrado / portabilidad / oposición).

## 9. Nota de transparencia sobre uso de IA

- **Qué es:** documento/aviso que explica a usuarios y afectados que el producto
  usa IA, para qué, con qué limitaciones y con qué supervisión humana. Cubre tres
  planos que se solapan (no duplicar, referenciar):
  - **RGPD arts. 13-14 y 22:** si hay decisiones automatizadas o perfilado con
    efecto significativo → informar de su existencia, la **lógica aplicada** y las
    consecuencias previstas; garantizar intervención humana.
  - **AI Act art. 50 (transparencia):** si el sistema **interactúa con personas**
    (chatbot), **genera contenido sintético**, o hace reconocimiento de
    emociones / categorización biométrica → informar de que es IA y marcar el
    contenido generado.
  - **AI Act art. 13 (IFU de alto riesgo) + art. 14 (supervisión humana):**
    capacidades y limitaciones, exactitud esperada y su contexto, condiciones que
    **degradan el rendimiento**, medidas de supervisión humana. Para el
    **responsable del despliegue** sanitario: arts. 26 y 86 (derecho a explicación
    de decisiones individuales).
- **¿Obligatoria?** Si `signals.usa_ia_ml` **y** (hay interacción con personas, o
  contenido generado, o impacto en decisiones clínicas). En un SaMD con IA de
  alto riesgo → **sí**.
- **Quién lo exige:** AESIA / autoridad de vigilancia de IA; AEPD (vertiente
  RGPD); organismo notificado (como parte de la IFU). La AEPD ha publicado
  orientaciones sobre transparencia e IA.
- **Contenido mínimo:** propósito del sistema de IA; tipo de modelo y, a alto
  nivel, datos de entrenamiento; métricas de rendimiento y su contexto;
  **limitaciones** y poblaciones donde el rendimiento baja; papel del profesional
  (la IA **asiste**, no sustituye); cómo se ejerce la supervisión humana; canal
  para impugnar o pedir revisión; **versión del modelo**.
- **Cómo se genera:** interno; se integra en la IFU y en la política de
  privacidad; se **actualiza con cada versión del modelo**.
- **Escáner:** `ai_ml.*`, `ai_ml.explicabilidad`, `ai_ml.llm_apis`.

## 10. Registro de designación del DPO (arts. 37-39)

- **¿Obligatorio?** Sí si el tratamiento a **gran escala de categorías
  especiales** es actividad principal (art. 37.1.c) — habitual en software
  sanitario. También si lo impone la **LOPDGDD art. 34** (p. ej. centros
  sanitarios obligados por ley a llevar historia clínica).
- **Entregable:** nombramiento; publicación de los datos de contacto del DPO;
  **comunicación a la AEPD** (sede electrónica).

## 11. SBOM · 12. Gestión de vulnerabilidades + VEX + CVD

Ver `references/sbom-vulnerabilidades.md`. Resumen de decisión:
- **MDSW conectado o que procesa datos → SBOM y gestión de vulnerabilidades
  obligatorios de facto** (MDCG 2019-16 Rev.1 + IEC 81001-5-1 + RGSF Anexo I.17
  MDR).
- **Componente que no califica como PS y se distribuye por separado →** posible
  **Cyber Resilience Act** (obligación legal, no solo de facto).
- **Software sin finalidad médica pero con datos personales →** el art. 32 RGPD
  obliga a gestionar vulnerabilidades de dependencias; el SBOM es el medio.

---

## Tabla resumen para el informe

| # | Documento | ¿Obligatorio aquí? | Base | Estado en el repo | Cómo se genera / quién lo pide |
|---|---|---|---|---|---|
| 1 | Análisis de calificación (incl. "no es PS") | {} | MDCG 2019-11 | {} | Interno · AEMPS / ON |
| 2 | Análisis de riesgos del tratamiento | {} | RGPD 24, 32 | {} | Interno + DPO · AEPD |
| 3 | DPIA / EIPD | {} | RGPD 35 | {} | Interno + DPO · consulta previa AEPD (36) si riesgo alto |
| 4 | RAT | {} | RGPD 30 | {} | Interno · AEPD |
| 5 | DPA / contrato de encargado (uno por proveedor) | {} | RGPD 28 | {} | Contrato con cada encargado (+ CCT/TIA si fuera del EEE) |
| 6 | Procedimiento + registro de brechas | {} | RGPD 33-34 | {} | Interno · AEPD (NBD 72 h) |
| 7 | TIA (una por transferencia vía art. 46) | {} | Schrems II · EDPB 01/2020 | {} | Interno |
| 8 | Cláusulas informativas / privacidad en capas | {} | RGPD 12-14 | {} | Interno |
| 9 | Nota de transparencia sobre uso de IA | {} | RGPD 13-14/22 · AI Act 13/50 | {} | Interno · IFU · AESIA/AEPD |
| 10 | Designación de DPO | {} | RGPD 37-39 · LOPDGDD 34 | {} | Nombramiento + comunicación a la AEPD |
| 11 | SBOM (CycloneDX / SPDX) | {} | MDCG 2019-16 · IEC 81001-5-1 · (CRA) | {} | Herramienta por stack; entregar al ON por versión |
| 12 | Gestión de vulnerabilidades + VEX + CVD | {} | ídem · RGPD 32 | {} | SCA en CI + vigilancia CVE poscomercialización |

Rellenar y añadir una frase por documento obligatorio: *"Qué es: … · Cómo se
genera: …"*.
