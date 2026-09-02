---
name: analisis-regulatorio-samd
description: >-
  Analiza un proyecto de software para determinar si es un producto sanitario
  (SaMD / MDSW) bajo el Reglamento (UE) 2017/745 (MDR), su clase de riesgo (I,
  IIa, IIb, III), la clase de seguridad IEC 62304, la normativa aplicable (MDR,
  RGPD/LOPDGDD, AI Act, ciberseguridad, evaluación clínica), los organismos
  implicados (AEMPS, CNCps/organismo notificado, AEPD, EUDAMED) y, norma por
  norma, cuáles cumple, cuáles no y cómo se gestiona cada una. Detecta además
  vulnerabilidades de datos sensibles y RGPD. Contrasta el estado normativo
  vigente en internet (fuentes oficiales) porque cambia con frecuencia. Produce
  un informe de situación en Markdown. Úsala cuando el usuario pida evaluar el
  estado regulatorio, la clasificación como producto sanitario, el cumplimiento
  MDR / RGPD / Reglamento de IA, la ruta a marcado CE, o los riesgos de datos de
  salud de un proyecto (España / UE).
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
  `findings` que sean decisivos para clasificar o para una vulnerabilidad.
- **Carga cada fichero de `references/` solo al llegar a su paso.** No los
  precargues todos.
- **Web: sí, pero acotada.** El estado normativo cambia rápido, así que hay que
  contrastarlo (paso 5). Reglas: usa la lista cerrada de consultas de
  `references/checkpoints-volatiles.md`, **una búsqueda por punto**, prioriza
  fuentes oficiales (EUR-Lex, BOE, AEMPS, health.ec.europa.eu, AEPD, CCN-CNI,
  AESIA), y **cita URL + fecha de consulta** en el informe. No abras más de ~8
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
`hits_by_category`, `findings`, `manifests`, `model_files`.

### 3. ¿Es producto sanitario?
Carga `references/calificacion-clasificacion.md`. Aplica el test MDCG 2019-11
combinando la finalidad prevista (paso 1) con las señales del escáner.
Resultado: **SÍ / NO / FRONTERA (borderline)** + justificación.

- **NO** → evalúa solo normativa horizontal: RGPD/LOPDGDD (paso 6b), y si es
  "health software" sin finalidad médica menciona ISO/IEC 82304-1 y las
  directrices AEPD de apps de salud/bienestar. Salta al paso 8 (informe reducido,
  pero mantén la tabla de cumplimiento RGPD y el contraste web de RGPD).
- **SÍ / FRONTERA** → continúa.

### 4. Clasificar
Con la misma referencia: aplica la **Regla 11** (Anexo VIII MDR) → clase
**I / IIa / IIb / III** + vía de evaluación (autocertificación vs organismo
notificado). Asigna también la **clase de seguridad IEC 62304 (A / B / C)**.
Indica el nivel de confianza y qué datos faltan para cerrarlo.

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
   España). Para cada norma anota: **versión/edición vigente, fechas de
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

### 7. Ruta a la conformidad
Con `references/normativa-y-organismos.md` (sección de organismos y costes) y
`references/requisitos-tecnicos.md` (matriz por clase): ordena las brechas del
paso 6 en fases, con entregable, organismo, prioridad y estimación
orientativa de coste/tiempo.

### 8. Redactar el informe
Usa `assets/plantilla-informe.md`. Rellena todas las secciones, en especial la
**tabla de cumplimiento norma por norma** (sección 5) con la columna "Cómo se
gestiona" y la columna "Fuente verificada (URL + fecha)". Guarda como
`informe-regulatorio-samd-AAAA-MM-DD.md` en la raíz del proyecto analizado y
envíalo con SendUserFile. El informe debe responder explícitamente: en qué
acierta el proyecto, en qué grupo/clase entra, a falta de qué está, y dónde
están los riesgos.

## Aviso obligatorio en el informe
Incluir siempre: *documento orientativo de planificación, no sustituye asesoría
legal/regulatoria; la clasificación vinculante la confirma un organismo
notificado; verificar textos vigentes en EUR-Lex, BOE y AEMPS. Fecha del
contraste normativo: {AAAA-MM-DD}.*
