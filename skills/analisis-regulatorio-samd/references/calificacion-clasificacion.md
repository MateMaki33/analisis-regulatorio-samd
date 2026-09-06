# Calificación y clasificación de software sanitario

Fuente base: MDCG 2019-11 Rev.1, Anexo VIII MDR (Regla 11), MDCG 2021-24 Rev.1,
MDCG 2019-15 rev.1 (clase I), MDCG 2020-16 rev.4 (clasificación IVDR), Manual on
Borderline and Classification de la Comisión.

---

## Parte A — ¿Es producto sanitario? (calificación, MDCG 2019-11)

El filtro es la **finalidad prevista** (*intended purpose*) que declara el
fabricante, no la tecnología. Es MDSW (Medical Device Software) si se cumplen las
tres condiciones:

1. **Es software** por sí mismo (no un mero soporte de otro software genérico).
2. **Realiza una acción sobre datos distinta de** almacenar, archivar, comunicar,
   hacer búsqueda simple o compresión sin pérdida. Es decir: calcula, interpreta,
   analiza, crea o modifica información clínica.
3. **En beneficio de pacientes individuales** y con una de estas finalidades del
   art. 2.1 MDR: diagnóstico, prevención, monitorización, predicción, pronóstico,
   tratamiento o alivio de enfermedad; diagnóstico/monitorización/tratamiento/
   alivio/compensación de una lesión o discapacidad; investigación, sustitución o
   modificación de la anatomía o de un proceso/estado fisiológico; regulación de
   la concepción.

### Árbol de decisión rápido

- ¿El software solo almacena/muestra/transmite/organiza datos sin
  interpretarlos? → **NO es PS** (p. ej. EHR pura, PACS de solo archivo, agenda).
- ¿Realiza cálculo/interpretación pero con finalidad **no médica** (bienestar,
  fitness, administración, facturación, investigación no clínica)? → **NO es PS**
  (puede ser "health software": ISO/IEC 82304-1; si es app de salud/bienestar de
  consumo, aplican las directrices AEPD).
- ¿Realiza cálculo/interpretación con una finalidad médica del art. 2.1 para un
  paciente concreto? → **SÍ es MDSW**.
- ¿Módulo dentro de un producto mayor? Se califica **cada módulo** por separado;
  el módulo con finalidad médica es PS aunque el resto no lo sea.

### Casos frontera habituales (documéntalos)
Calculadoras clínicas, motores de reglas / CDSS, apps de adherencia con ajuste de
pauta, triaje sintomático, alertas sobre constantes, software que "prepara" datos
para otro PS. Ante duda → contrastar con el *Manual on Borderline* y con el
organismo notificado, y **redactar un análisis de calificación por escrito**
(es lo primero que se pide en evaluación de conformidad).

### Señales de la exploración (paso 2) → interpretación
- `signals.senal_finalidad_medica` / `clinical.diagnostico` / `clinical.soporte_decision`
  / `clinical.tratamiento_dosis` / `clinical.pronostico_riesgo` → indicio fuerte de MDSW.
- `clinical.estandares_salud` (HL7/FHIR/DICOM/SNOMED) → contexto clínico, pero por
  sí solo puede ser interoperabilidad/almacenamiento (no basta para calificar).
- Solo `clinical.dominio_clinico` sin acciones de cálculo/interpretación →
  probablemente NO es PS (verificar finalidad).
- `signals.posible_diagnostico_in_vitro` / `ivd.*` → antes de aplicar la Regla 11
  (Parte B), comprueba si en realidad encaja en **IVDR** en vez de MDR (ver
  "¿MDR o IVDR?" más abajo).
- `signals.posible_ehr_o_ehds` / `ehds.*` → además de calificar como PS o no,
  evalúa si es también **sistema EHR** bajo el EHDS (norma horizontal adicional,
  no sustituye la calificación MDR/IVDR) — carga `references/ehds-espacio-datos-salud.md`.

### Árbol de decisión (MDCG 2019-11 Rev.1, Figura 1 — resumen operativo)

```
¿Es "software" según MDCG 2019-11?
  No → no cubierto por MDR/IVDR
  Sí ↓
¿Es un dispositivo del Anexo XVI MDR, un accesorio (art. 2(2) MDR/IVDR),
o software que dirige/influye en el uso de un producto (hardware)?
  Sí → hereda el régimen (MDR o IVDR) y la clase del producto/accesorio
  No ↓
¿Realiza una acción sobre datos distinta de almacenar, archivar,
comunicar, búsqueda simple o compresión sin pérdida?
  No → NO cubierto por MDR/IVDR (ni por MDCG 2019-11)
  Sí ↓
¿Esa acción es en beneficio de un paciente individual?
  No → NO cubierto por MDR/IVDR
  Sí ↓
Es MDSW según MDCG 2019-11 → decide MDR vs. IVDR (siguiente árbol)
```

### ¿MDR o IVDR? (MDCG 2019-11 Rev.1, Figura 2 — resumen operativo)

```
¿La información que da el software está dentro del alcance de la
definición de IVD (examina una muestra humana para dar información
sobre un proceso/estado fisiológico o patológico, discapacidad congénita,
predisposición, compatibilidad de receptores, respuesta a tratamiento,
o para definir/monitorizar medidas terapéuticas)?
  No → cubierto por el MDR (Reglamento (UE) 2017/745) → sigue por la Regla 11 (Parte B)
  Sí ↓
¿La información se basa EXCLUSIVAMENTE en datos obtenidos de productos IVD?
  Sí → cubierto por el IVDR (Reglamento (UE) 2017/746)
  No ↓
¿La finalidad prevista está sustancialmente impulsada por fuentes de datos IVD
(aunque combine otras fuentes: imagen, constantes, historia clínica)?
  Sí → cubierto por el IVDR
  No → cubierto por el MDR
```

Si el resultado es **IVDR**, carga `references/ivdr-diagnostico-in-vitro.md` y
sustituye la Parte B (Regla 11 MDR) por la clasificación IVDR (clases A-D,
Reglas 1-7 IVDR) de esa referencia. El resto del flujo de la skill (RGPD, IA,
ciberseguridad, entregables, SBOM) es el mismo para ambos casos.

---

## Parte B — Clasificación por riesgo (Regla 11, Anexo VIII MDR)

Si es MDSW independiente, la clase la fija la **Regla 11**. Si el software
**controla o influye en el uso de otro producto**, hereda la clase de ese
producto (mínimo la que le corresponda por Regla 11).

**Regla 11 — texto operativo:**

El software destinado a **proporcionar información utilizada para tomar decisiones
con fines diagnósticos o terapéuticos** es:

| Situación | Clase |
|---|---|
| Regla general (decisiones diagnósticas/terapéuticas) | **IIa** |
| …salvo que esas decisiones puedan causar **muerte o deterioro irreversible** del estado de salud | **III** |
| …o un **deterioro grave** del estado de salud o una **intervención quirúrgica** | **IIb** |
| Software destinado a **monitorizar procesos fisiológicos** | **IIa** |
| …salvo que monitorice **parámetros fisiológicos vitales** y su variación pueda causar **peligro inmediato** para el paciente | **IIb** |
| **Todos los demás casos** (software que no encaja arriba: no orienta decisiones diagnósticas/terapéuticas ni monitoriza) | **I** |

### Cómo aplicarla (MDCG 2019-11, criterio del "estado de la información")
Cruzar dos ejes:
1. **Importancia de la información** para la decisión clínica: *informa* /
   *drive* (orienta) una decisión / *trata o diagnostica directamente*.
2. **Situación del paciente / criticidad del cuadro**: no grave · grave ·
   crítico / vital.

Cuanto más determinante la información y más grave la condición, más sube la
clase. "Muerte o deterioro irreversible" → III; "deterioro grave o cirugía" →
IIb; impacto menor → IIa; sin impacto en decisión diagnóstica/terapéutica → I.

### Ejemplos orientativos
- **I**: registro/diario de síntomas sin interpretación; software que solo
  presenta datos; herramientas de cálculo administrativo.
- **IIa**: sugerencia de ajuste de medicación no crítica; ayuda a la
  interpretación de pruebas rutinarias; monitorización de procesos no vitales;
  la mayoría de CDSS "de apoyo".
- **IIb**: cálculo de dosis de fármacos de alto riesgo (anticoagulantes,
  quimioterapia, insulina en bomba); monitorización de constantes vitales con
  alarma; software que prioriza pacientes en cuadros graves (triaje de urgencias).
- **III**: soporte a decisión en situaciones vitales agudas; algoritmos cuyo
  fallo lleva a decisión terapéutica con riesgo de muerte/daño irreversible
  (p. ej. dosificación de radioterapia, selección de tratamiento oncológico de
  alto impacto).

### Notas
- Función de **medición** con requisitos metrológicos → ver MDCG 2021-24 Rev.1.
- La **revisión selectiva MDR/IVDR** (propuesta de la Comisión de 16-dic-2025)
  plantea reclasificaciones a la baja para ciertos productos; no adoptada (no
  antes de 2027). Mencionar como incertidumbre, no aplicar aún.

---

## Parte C — Clase de seguridad IEC 62304 (A / B / C)

Independiente de la clase MDR; describe el **daño posible por un fallo del
software** tras considerar medidas de mitigación externas (hardware, alarmas,
procedimiento clínico):

- **Clase A**: no es posible lesión ni daño a la salud.
- **Clase B**: es posible una lesión **no grave**.
- **Clase C**: es posible **muerte o lesión grave**.

Regla práctica: MDR I → normalmente 62304 A/B; IIa → B; IIb → B/C; III → C.
La clase 62304 determina qué procesos del ciclo de vida son exigibles
(ver `requisitos-tecnicos.md`).

---

## Parte D — Subtipos de clase I con intervención parcial del organismo notificado (MDCG 2019-15 rev.1)

La clase I es, por defecto, autocertificación pura — **salvo** que el producto
tenga alguna de estas tres características, en cuyo caso hace falta
**intervención limitada de un organismo notificado** (solo para el aspecto
señalado, no una evaluación de conformidad completa):

| Subtipo | Qué es | Relevancia para software |
|---|---|---|
| **Is** — estéril | Se comercializa en condición estéril | No aplica a software puro |
| **Im** — función de medición | El producto tiene una **función de medición** con relevancia metrológica | **Sí puede aplicar**: software que calcula/asigna un **valor cuantificado** con pretensión de exactitud metrológica (p. ej. estima un parámetro fisiológico, un índice, una dosis con unidades verificables) puede considerarse "con función de medición". Revísalo si el software declara márgenes de error, unidades de medida o pretende sustituir a un instrumento de medida |
| **Ir** — instrumental quirúrgico reutilizable | Instrumental físico reutilizable | No aplica a software puro |

Si el software cae en **Im**: sigue siendo **clase I** globalmente (Regla 11
no lo sube de clase salvo que ya lo haga por su finalidad), pero el fabricante
debe acudir a un **organismo notificado con código MDS 1010** ("Devices with a
measuring function") para que audite **solo** los aspectos de conformidad
metrológica — el resto del expediente (RGSF general, evaluación clínica, SGC)
sigue siendo autocertificado. Verificar con el organismo notificado si el
cálculo concreto del software se considera "función de medición" a efectos del
MDR (no todo cálculo numérico lo es).

### Pasos para poner en el mercado un producto de clase I (MDCG 2019-15 rev.1) — checklist operativo
0. Integrar el MDR en el sistema de gestión de calidad (aunque no sea
   obligatorio certificar ISO 13485, sí un SGC documentado equivalente).
1. Confirmar que es producto sanitario (Parte A).
2. Confirmar que es clase I (Parte B) y si tiene subtipo Is/Im/Ir (Parte D).
3. Antes de comercializar: cumplir los RGSF del Anexo I; realizar la
   evaluación clínica (MDCG 2020-1); preparar la documentación técnica (Anexos
   II-III); solicitar intervención del organismo notificado **si** Is/Im/Ir;
   preparar IFU y etiquetado (en español para España — RD 192/2023).
4. Comprobar el cumplimiento de las obligaciones generales del fabricante
   (art. 10 MDR): sistema de gestión de riesgos, PRRC designado (art. 15),
   seguro de responsabilidad civil si procede.
5. Redactar la **Declaración UE de Conformidad**.
6. Colocar el **marcado CE**.
7. Registrar el producto y al fabricante en **EUDAMED** (SRN, Basic UDI-DI).
8. Vigilancia poscomercialización: recoger experiencia de PMS, sistema de
   vigilancia (incidentes graves, FSCA), gestión de no conformidades.
