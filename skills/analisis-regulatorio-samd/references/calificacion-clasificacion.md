# Calificación y clasificación de software sanitario

Fuente base: MDCG 2019-11 Rev.1, Anexo VIII MDR (Regla 11), MDCG 2021-24 Rev.1,
Manual on Borderline and Classification de la Comisión.

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

### Señales del escáner → interpretación
- `signals.senal_finalidad_medica` / `clinical.diagnostico` / `clinical.soporte_decision`
  / `clinical.tratamiento_dosis` / `clinical.pronostico_riesgo` → indicio fuerte de MDSW.
- `clinical.estandares_salud` (HL7/FHIR/DICOM/SNOMED) → contexto clínico, pero por
  sí solo puede ser interoperabilidad/almacenamiento (no basta para calificar).
- Solo `clinical.dominio_clinico` sin acciones de cálculo/interpretación →
  probablemente NO es PS (verificar finalidad).

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
