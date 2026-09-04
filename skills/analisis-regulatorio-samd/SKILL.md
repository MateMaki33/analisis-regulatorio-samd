---
name: analisis-regulatorio-samd
description: >-
  Analiza un proyecto de software frente a la normativa de producto sanitario de
  la UE: si es producto sanitario (SaMD / MDSW) bajo el Reglamento (UE) 2017/745
  (MDR) o bajo el Reglamento (UE) 2017/746 (IVDR, diagnóstico in vitro), su clase
  de riesgo (I/IIa/IIb/III en MDR, A/B/C/D en IVDR), la clase de seguridad IEC
  62304, la normativa aplicable (MDR/IVDR, RGPD/LOPDGDD, AI Act, EHDS/EHR,
  ciberseguridad, evaluación clínica o del funcionamiento), los organismos
  implicados y, norma por norma, qué cumple y cómo se gestiona. Indica qué
  entregables de datos y seguridad debe generar y qué es cada uno (calificación,
  análisis de riesgos del tratamiento, DPIA, RAT, contratos de encargado,
  brechas, TIA, transparencia de IA, calificación/marcado CE como sistema EHR
  bajo el EHDS, SBOM), analiza las dependencias y detecta si los datos salen del
  EEE (regiones no europeas, proxies, CDNs, APIs de IA) y con qué cobertura del
  capítulo V del RGPD. Contrasta la normativa vigente en fuentes oficiales y
  produce un informe en Markdown. Úsala para evaluar el estado regulatorio de un
  proyecto en España / UE: calificación como producto sanitario y clasificación,
  cumplimiento MDR/IVDR/RGPD/IA/EHDS, ruta a marcado CE, entregables de
  protección de datos, transferencias internacionales o SBOM.
---

# Análisis regulatorio de software sanitario (SaMD) — España / UE

Convierte un repositorio + la finalidad prevista declarada por el usuario en un
**informe de situación regulatoria** que responde, de forma explícita:

- ¿Es producto sanitario? ¿En qué clase entra?
- ¿Qué normas le aplican y cuáles son **obligatorias sí o sí**?
- **Norma por norma: ¿la cumple, la cumple en parte o no la cumple?** ¿con qué
  evidencia? ¿qué le falta?
- **¿Cómo se gestiona cada norma?** — ante qué organismo, con qué trámite, qué
  entregable, en qué plazo.
- ¿Dónde están los riesgos, incluidas vulnerabilidades de RGPD y datos sensibles?

Fecha de referencia del contenido incorporado: **septiembre 2026**. La normativa de
producto sanitario e IA está en evolución activa; por eso el paso 5 **contrasta en
internet** el estado vigente antes de concluir.

## Principios de eficiencia (respetar siempre)

- **No leas el repositorio entero.** Ejecuta el escáner y trabaja sobre su JSON.
  Lee, como mucho, ~10 ficheros: README/manifiestos + los ficheros citados en
  `findings` que sean decisivos para clasificar o para una vulnerabilidad. Para
  el análisis de transferencias internacionales puedes añadir 3-5 ficheros de
  configuración de infraestructura (`.env` / `.env.example`, `docker-compose*`,
  IaC `*.tf`, `config/`, `helm/`).
- **Dependencias:** trabaja sobre `manifests` y `supply_chain` del JSON (cuentas
  y ficheros ya detectados). **No** instales herramientas ni ejecutes escaneos de
  SBOM/CVE — recomiéndalos en el informe.
- **Carga cada fichero de `references/` solo al llegar a su paso.** No los
  precargues todos.
- **Web: sí, pero acotada.** El estado normativo cambia rápido, así que hay que
  contrastarlo (paso 5). Reglas: usa la lista cerrada de consultas de
  `references/checkpoints-volatiles.md`, **una búsqueda por punto**, prioriza
  fuentes oficiales (EUR-Lex, BOE, AEMPS, health.ec.europa.eu, AEPD, CCN-CNI,
  AESIA), y **cita URL + fecha de consulta** en el informe. No abras más de ~10
  búsquedas en total. Si una consulta no aporta nada más reciente, usa el dato
  incorporado y decláralo como "sin cambios verificados a {fecha}".
- Si el escáner no encuentra ninguna señal clínica/de salud y el usuario no
  declara finalidad médica: dilo en 2–3 líneas, indica que solo aplica normativa
  horizontal (RGPD si hay datos personales) y termina.

## Flujo de trabajo

### 1. Recoger la finalidad prevista
Pregunta al usuario (o extrae del README/docs) en 1 mensaje breve:
- ¿Qué hace el software y para quién (profesional sanitario, paciente, investigación)?
- ¿Qué afirma el fabricante que hace? (¿diagnostica, monitoriza, calcula dosis,
  prioriza, predice, solo registra/muestra?)
- ¿Se comercializa en España/UE? ¿Incluye IA/ML?
Si el usuario ya lo ha dado, no repreguntes.

### 2. Escanear el proyecto
```
python skills/analisis-regulatorio-samd/scripts/scan_repo.py <ruta> --json-out <scratch>/scan.json
```
(en Windows usa `python`; si no hay Python, haz grep dirigido con los patrones de
`scripts/scan_repo.py` como guía). Lee el JSON: `signals`, `counts`,
`hits_by_category`, `findings`, `manifests`, `model_files`, `supply_chain`.
Señales relevantes para los pasos nuevos: `posible_transferencia_internacional`,
`menciona_region_no_eu`, `menciona_proxy_o_cdn`, `tiene_sbom`,
`tiene_gestion_dependencias`, `fija_versiones_dependencias`,
`total_dependencias_directas_aprox`, `posible_diagnostico_in_vitro`,
`posible_ehr_o_ehds`; y los grupos `infra_datos.*`, `supply_chain.*`, `ivd.*` y
`ehds.*` en `findings` / `hits_by_category`.

### 3. ¿Es producto sanitario? ¿MDR o IVDR?
Carga `references/calificacion-clasificacion.md`. Aplica el test MDCG 2019-11
combinando la finalidad prevista (paso 1) con las señales del escáner.
Resultado: **SÍ / NO / FRONTERA (borderline)** + justificación.

- **NO** → evalúa solo normativa horizontal: RGPD/LOPDGDD (paso 6b), EHDS si
  trata categorías prioritarias de datos de salud (paso 6c-bis) y los
  entregables de datos y transferencias (paso 6d), y si es "health software" sin
  finalidad médica menciona ISO/IEC 82304-1 y las directrices AEPD de apps de
  salud/bienestar. **Deja constancia de que el "análisis de calificación" es un
  entregable obligatorio aunque la conclusión sea NO** (es lo primero que exige
  una inspección de AEMPS). Salta al paso 8 (informe reducido, pero mantén la
  tabla de cumplimiento RGPD, el catálogo de entregables, las transferencias
  internacionales y el contraste web de RGPD).
- **SÍ / FRONTERA** → aplica el árbol "¿MDR o IVDR?" de la misma referencia. Si
  el resultado es **IVDR** (el software interpreta datos de un examen de
  muestra humana: `signals.posible_diagnostico_in_vitro` / `ivd.*`), carga
  además `references/ivdr-diagnostico-in-vitro.md` — sustituye el paso 4 (Regla
  11 MDR) por la clasificación IVDR (clases A-D) de esa referencia y ajusta el
  resto del informe (evaluación del funcionamiento en vez de clínica, PER/PMPF
  en vez de CER/PMCF). Si es **MDR**, continúa con el paso 4 normal.

### 4. Clasificar
Con la misma referencia (o con `ivdr-diagnostico-in-vitro.md` si es IVDR):
aplica la **Regla 11** (Anexo VIII MDR) → clase **I / IIa / IIb / III** + vía de
evaluación (autocertificación vs organismo notificado); o las **Reglas 1-7**
(Anexo VIII IVDR) → clase **A / B / C / D**. Si es MDR clase I, comprueba
también los subtipos **Is/Im/Ir** (MDCG 2019-15 rev.1) por si hace falta
intervención parcial de un organismo notificado. Asigna también la **clase de
seguridad IEC 62304 (A / B / C)** (aplica igual en MDR e IVDR). Indica el nivel
de confianza y qué datos faltan para cerrarlo.

### 5. Mapa normativo + CONTRASTE EN INTERNET
1. Carga `references/normativa-y-organismos.md`. Construye la lista de normas
   aplicables a esta clase/perfil: para cada una — **obligatoria / de facto /
   condicional / recomendada**, **qué implica**, **ante qué organismo**,
   **cuándo interviene**.
2. Carga `references/checkpoints-volatiles.md` y **ejecuta el contraste web**:
   una búsqueda por punto de la lista que sea pertinente a este producto
   (siempre: EUDAMED, lista de normas armonizadas en el DOUE, RGPD/AEPD apps de
   salud; si IIa+: fees y procedimiento del organismo notificado, revisión MDR;
   si IA: calendario AI Act; si la organización es entidad de salud grande: NIS2
   España; **si hay transferencias fuera del EEE: decisiones de adecuación
   vigentes + estado del EU-US Data Privacy Framework**; **si es MDSW conectado o
   hay componente no-PS: SBOM/MDCG 2019-16 + calendario del Cyber Resilience
   Act**; **si es IVD (IVDR): normas armonizadas IVDR y revisiones de MDCG
   2020-16**; **si trata categorías prioritarias de datos de salud (posible
   sistema EHR): calendario de actos de ejecución del EHDS y autoridad
   española**). Para cada norma anota: **versión/edición vigente, fechas de
   aplicación, guía MDCG más reciente, URL, fecha de consulta**.
3. Corrige la tabla del paso 5.1 con lo verificado. Marca explícitamente lo que
   **no** has podido verificar.

### 6. Evaluación de cumplimiento norma por norma
Carga `references/evaluacion-cumplimiento.md`. Para **cada norma aplicable**
produce una fila con:
- **Veredicto:** `Cumple` / `Cumple parcialmente` / `No cumple` / `No evaluable
  (sin evidencia)`.
- **Evidencia:** qué del repo/docs/escáner respalda el veredicto (`fichero:línea`
  o "no encontrado").
- **Brecha:** qué falta concretamente para pasar a `Cumple`.
- **Cómo se gestiona:** proceso operativo (paso a paso resumido), **organismo**,
  **entregable/registro**, **plazo o hito**.

Sub-pasos temáticos (usa las referencias específicas para el detalle):
- **6a. Requisitos técnicos** — `references/requisitos-tecnicos.md`: SGC (ISO
  13485), riesgos (ISO 14971), ciclo de vida (IEC 62304 — cómo se hace y qué
  exige por clase A/B/C), usabilidad (IEC 62366-1), ciberseguridad (IEC 81001-5-1
  + MDCG 2019-16).
- **6b. RGPD y datos** — `references/rgpd-datos.md`: mapea `findings` →
  obligaciones RGPD/LOPDGDD y **lista priorizada de vulnerabilidades** (datos
  sensibles en claro, secretos hardcodeados, TLS desactivado, logs con PII,
  terceros sin base, IA como servicio con datos de paciente) con `fichero:línea`
  y remediación. Contrasta con las directrices AEPD vigentes (verificadas en el
  paso 5).
- **6c. IA** (solo si `signals.usa_ia_ml` o el usuario lo indica) —
  `references/ia-aiact.md`: ¿alto riesgo por art. 6.1?, obligaciones arts. 8-17
  con veredicto de cumplimiento, ¿el organismo notificado necesita designación
  AI Act?, fecha de exigibilidad **verificada por web** en el paso 5.
- **6c-bis. EHDS / sistema EHR** (si `signals.posible_ehr_o_ehds`, `ehds.*`, o
  el usuario declara que el software almacena/exporta/muestra resumen de
  paciente, receta/dispensación electrónica, imagen médica e informe, resultado
  de laboratorio o informe de alta) — `references/ehds-espacio-datos-salud.md`:
  ¿es "sistema EHR"?, requisitos esenciales del Anexo II (interoperabilidad
  EEHRxF, seguridad y registro de accesos), declaración/marcado CE propios del
  EHDS, calendario **verificado por web** en el paso 5, y si hay reutilización
  de datos con fines de investigación/IA, el régimen de uso secundario
  (permiso de datos). Recuerda que el EHDS **no sustituye** al MDR/IVDR ni al
  RGPD: se suma.
- **6d. Entregables de datos y seguridad, transferencias internacionales y SBOM**
  — carga `references/entregables-datos-y-seguridad.md`,
  `references/transferencias-internacionales.md` y
  `references/sbom-vulnerabilidades.md` (este último si hay `manifests` o el
  producto es MDSW / trata datos). Produce **tres bloques**:
  1. **Catálogo de entregables.** Para cada documento (análisis de calificación
     —incl. "no es PS"—, análisis de riesgos del tratamiento, DPIA/EIPD, RAT,
     DPA por proveedor, procedimiento de brechas, TIA, cláusulas informativas,
     nota de transparencia de IA, designación de DPO, calificación como sistema
     EHR + declaración/marcado CE EHDS si procede): veredicto **obligatorio /
     recomendado / no aplica** para este proyecto **con el criterio de decisión
     explícito**, estado **presente / parcial / ausente** según el repo, y 1-2
     frases de **qué es** y **cómo se genera / quién lo pide**. Rellena la tabla
     resumen de esa referencia.
  2. **Transferencias internacionales.** Con `infra_datos.*`, `third_party.*`,
     `ai_ml.llm_apis` y 3-5 ficheros de configuración, construye la **tabla de
     flujos de datos**: por flujo → proveedor, país/región, ¿sale del EEE?,
     mecanismo del cap. V, ¿falta TIA?, estado. Señala explícitamente **proxies,
     CDNs y endpoints fuera del EEE**. Marca como **brecha crítica** cualquier
     flujo sin base legal del cap. V. Verifica por web (paso 5) la lista de
     decisiones de adecuación y el estado del **EU-US Data Privacy Framework**.
  3. **SBOM y vulnerabilidades.** Di si el **SBOM** y la **gestión de
     vulnerabilidades** son obligatorios aquí y **por qué** (regla de
     `sbom-vulnerabilidades.md` §2). Inventaria dependencias directas por
     manifiesto (`supply_chain.dependency_counts`), ¿versiones fijadas?
     (`lockfiles`), ¿SBOM ya presente? (`sbom_files`), ¿SCA en CI?
     (`sca_config` / `supply_chain.sca_ci`), ¿CVD? (`cvd_policy`). Recomienda el
     **comando de generación de SBOM** para el stack detectado y las herramientas
     de cribado CVE. No ejecutes nada.

### 7. Ruta a la conformidad
Con `references/normativa-y-organismos.md` (sección de organismos y costes) y
`references/requisitos-tecnicos.md` (matriz por clase): ordena las brechas del
paso 6 en fases, con entregable, organismo, prioridad y estimación
orientativa de coste/tiempo.

### 8. Redactar el informe
Usa `assets/plantilla-informe.md`. Rellena todas las secciones, en especial la
**tabla de cumplimiento norma por norma** (sección 5) con la columna "Cómo se
gestiona" y la columna "Fuente verificada (URL + fecha)", la **tabla de
entregables de datos y seguridad** (sección 7.2: ¿obligatorio aquí?, por qué,
estado, cómo se genera), la **tabla de flujos de datos / transferencias
internacionales** (sección 7.5) y el bloque **SBOM y vulnerabilidades** (sección
6.7). Si el producto es IVD, incluye la sección **3b (clasificación IVDR)** en
vez de/además de la 4 (Regla 11 MDR); si trata categorías prioritarias de datos
de salud, incluye la sección **8b (EHDS / sistema EHR)**. Guarda como
`informe-regulatorio-samd-AAAA-MM-DD.md` en la raíz del proyecto analizado y
envíalo con SendUserFile. El informe debe responder explícitamente: en qué
acierta el proyecto, en qué grupo/clase entra (MDR o IVDR), a falta de qué
está, qué documentos debe generar y por qué, si los datos salen de Europa y con
qué cobertura, si es también sistema EHR bajo el EHDS, y dónde están los
riesgos.

**Índice de siglas (obligatorio, última sección del informe).** Carga
`references/glosario-siglas.md`. Repasa el informe ya redactado y anota cada
sigla/acrónimo que aparece en el texto (MDR, IVDR, RGPD, DPIA, SBOM, EHDS...).
Genera la tabla del **Anexo A** de la plantilla con esas siglas **en orden
alfabético**, copiando el significado del glosario. Si el informe usa una
sigla que no está en el glosario (propia del repo/dominio analizado), añádela
igualmente con el significado que se deduzca del contexto — el índice debe
cubrir el 100% de las siglas del informe, no solo las del glosario.

## Aviso obligatorio en el informe
Incluir siempre: *documento orientativo de planificación, no sustituye asesoría
legal/regulatoria; la clasificación vinculante la confirma un organismo
notificado; verificar textos vigentes en EUR-Lex, BOE y AEMPS. Fecha del
contraste normativo: {AAAA-MM-DD}.*
