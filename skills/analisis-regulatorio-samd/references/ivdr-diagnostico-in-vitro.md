# IVDR — Productos sanitarios para diagnóstico in vitro (Reglamento (UE) 2017/746)

Cárgalo cuando, en el paso 3, el software **interprete, calcule o analice datos
producidos por un ensayo/instrumento de laboratorio** sobre una muestra humana
(sangre, orina, tejido, saliva, ácidos nucleicos…): `signals.posible_diagnostico_in_vitro`,
o el usuario declara que el producto trabaja con resultados de laboratorio,
biomarcadores, secuenciación, anatomía patológica o pruebas de autodiagnóstico.
Fuentes: MDCG 2019-11 Rev.1 (calificación MDR/IVDR conjunta), MDCG 2020-16 rev.4
(clasificación IVDR).

**Por qué importa distinguirlo del MDR:** si el software encaja en IVDR en vez
de en MDR, **cambian** las clases de riesgo (A/B/C/D, no I/IIa/IIb/III), las
reglas de clasificación (Anexo VIII IVDR, no Regla 11 MDR), el tipo de
evaluación (evaluación del **funcionamiento** — *performance evaluation* — no
evaluación clínica), y en ciertos casos el organismo notificado necesita una
designación IVDR específica (no basta la del MDR). El resto del marco horizontal
(RGPD, AI Act, ciberseguridad, SBOM) se mantiene igual.

---

## 1. ¿MDR o IVDR? — pasos de calificación (MDCG 2019-11 Rev.1, Figura 2)

Aplica **después** de confirmar que el software es MDSW (Parte A de
`calificacion-clasificacion.md`: es software, actúa sobre datos más allá de
almacenar/comunicar/buscar, y beneficia a un paciente concreto con una
finalidad del art. 2.1 MDR o del art. 2 IVDR).

1. **¿La información que da el software está dentro del alcance de la
   definición de IVD** (art. 2.2 IVDR)? Es decir, ¿sirve para examinar
   muestras humanas (sangre, orina, tejido, saliva…) con el fin de dar
   información sobre: **(a)** un proceso o estado fisiológico o patológico;
   **(b)** discapacidades físicas o mentales congénitas; **(c)**
   predisposición a una afección o enfermedad; **(d)** seguridad y
   compatibilidad con receptores potenciales (p. ej. compatibilidad
   transfusional); **(e)** predicción de la respuesta o reacciones a un
   tratamiento; **(f)** definición o seguimiento de medidas terapéuticas? →
   si **sí**, es **IVD MDSW** (sigue al punto 3).
2. Si **no** entra en la definición de IVD pero cumple la definición general de
   producto sanitario del art. 2.1 MDR → **MD MDSW** (sigue por
   `calificacion-clasificacion.md`, Regla 11 MDR).
3. **¿El software toma los datos de entrada exclusivamente de un producto IVD?**
   (p. ej. procesa la señal cruda de un lector ELISA, un analizador de PCR, un
   citómetro, o interpreta el patrón de bandas de un *blot*) → confirma **IVD
   MDSW**.
4. **¿La finalidad prevista está sustancialmente impulsada por datos de fuentes
   IVD** aunque combine también otras fuentes (imagen, constantes, historia
   clínica)? → sigue siendo **IVD MDSW** si el componente IVD es determinante
   para la conclusión diagnóstica/pronóstica.
5. **Software que dirige o influye en el uso de un producto (hardware)**: se
   clasifica **en la misma clase** que ese producto — si el producto que
   dirige es un IVD (p. ej. software embebido de un analizador de laboratorio),
   el software hereda su clase IVDR.

**Ejemplos frecuentes de IVD MDSW:**
- Software que analiza la densidad óptica de un lector ELISA o el patrón de un
  *western blot* y aplica un algoritmo clínico para dar un resultado
  diagnóstico/pronóstico.
- Software que interpreta un panel genético/NGS y da un informe de variantes
  con relevancia clínica (predisposición, farmacogenómica).
- Software que calcula un **score de riesgo** a partir de biomarcadores de
  laboratorio (p. ej. combinación de marcadores tumorales).
- Software de apoyo a diagnóstico anatomopatológico (patología digital) que
  interpreta imágenes de biopsias con fines diagnósticos.
- Software de **autodiagnóstico** que interpreta el resultado de una prueba de
  detección (p. ej. antígeno, embarazo, glucosa) para el propio usuario lego.

**No es IVD (queda fuera de IVDR y MDR):** software de gestión de flujo de
trabajo de laboratorio (LIS) que solo enruta/almacena resultados sin
interpretarlos; control de calidad de instrumentos sin dar resultado clínico;
materiales de referencia certificados y de evaluación externa de la calidad
(excluidos expresamente por el art. 1.3(c)-(d) IVDR).

---

## 2. Clasificación por riesgo (Anexo VIII IVDR, Reglas 1-7)

A diferencia del MDR (4 clases), el IVDR tiene **4 clases de riesgo creciente
A → D**, y las reglas se aplican en **orden** (si el producto encaja en una
regla específica 1-5, esa clase prevalece; si no, caen en la regla general 6).

| Clase | Riesgo | Vía de evaluación de conformidad |
|---|---|---|
| **A** | Riesgo individual bajo, riesgo de salud pública bajo | Autocertificación (salvo función de esterilidad → NB parcial, análogo al Class I *sterile* del MDR) |
| **B** | Riesgo individual moderado y/o riesgo de salud pública bajo | Organismo notificado (auditoría de SGC + revisión de documentación técnica muestral) |
| **C** | Riesgo individual alto y/o riesgo de salud pública moderado | Organismo notificado (revisión de documentación técnica más profunda, por familia de producto representativa) |
| **D** | Riesgo individual alto **y** riesgo de salud pública alto | Organismo notificado + **verificación por lote** + consulta a laboratorio de referencia de la UE cuando exista |

### Resumen de las reglas (MDCG 2020-16 rev.4)

| Regla | Qué cubre | Clase típica |
|---|---|---|
| **Regla 1** | Detección de agentes transmisibles en sangre/tejidos/órganos para transfusión/trasplante; enfermedades de alto riesgo de propagación con peligro vital; carga infecciosa de enfermedades de riesgo vital en seguimiento del paciente | **D** |
| **Regla 2** | Determinación de grupo sanguíneo, Rh, fenotipos eritrocitarios relevantes para transfusión/trasplante | **C** (o **D** si hay riesgo directo de incompatibilidad grave) |
| **Regla 3** | Cribado/diagnóstico de enfermedades de transmisión sexual, infecciones con riesgo moderado, estado infeccioso/inmune con impacto en decisiones vitales, cribado prenatal, cribado genético, monitorización terapéutica de fármacos de estrecho margen, gestión de pacientes oncológicos, tipaje HLA, marcadores tumorales, cribado de anomalías congénitas en el feto | **C** (mayoría); algunos supuestos → **D** si el riesgo individual es alto |
| **Regla 4** | Autodiagnóstico (near-patient / *self-testing*) — la clase depende de qué se detecte (glucosa, embarazo, fertilidad → normalmente **B/C**; VIH/hepatitis en autotest → **D** por Regla 1) |
| **Regla 5** | Productos de uso general de laboratorio, instrumentos, reactivos sin finalidad de examen específica, materiales de control sin valor asignado | **A** (o **B** para controles con valor asignado, vía regla 1.6) |
| **Regla 6** | **Catch-all**: cualquier IVD no cubierto por las reglas 1-5 (bioquímica clínica de hormonas, vitaminas, enzimas, electrolitos, sustratos, la mayoría de inmunohistoquímica, agentes infecciosos de riesgo moderado) | **B** |
| **Regla 7** | Controles **sin** valor cuantitativo o cualitativo asignado (el valor lo pone el usuario, no el fabricante) | **B** |

### Cómo aplicarla
1. Confirma la finalidad prevista literal.
2. Recorre las reglas 1-6 **en orden** y detente en la primera que aplique
   (regla 6 es el residual — si nada más encaja, clase B).
3. Software que **dirige o influye** en otro IVD hereda su clase; **calibradores**
   y **controles con valor asignado** heredan la clase del producto con el que
   se usan (implementing rule 1.6); software **independiente** se clasifica por
   su propia finalidad prevista (Anexo VIII IVDR §1.4).
4. Documenta el razonamiento igual que para el MDR: **análisis de calificación y
   clasificación por escrito**, con la regla aplicada y la justificación.

---

## 3. Qué cambia frente al camino MDR

| Elemento | MDR (SaMD) | IVDR (IVD MDSW) |
|---|---|---|
| Clases | I / IIa / IIb / III | A / B / C / D |
| Regla de clasificación software independiente | Regla 11 (Anexo VIII MDR) | Reglas 1-7 (Anexo VIII IVDR), por finalidad — no hay una "regla 11 IVDR" específica de software |
| Evaluación | **Clínica** (MDCG 2020-1): validez científica + validación analítica + validación clínica | **Del funcionamiento** (*performance evaluation*, art. 56-60 IVDR): validez científica + **rendimiento analítico** (sensibilidad/especificidad analítica, exactitud, precisión, límite de detección) + **rendimiento clínico** (sensibilidad/especificidad clínica, valor predictivo) |
| Documento de evaluación | CER (Clinical Evaluation Report) | **PER** (*Performance Evaluation Report*) + **PMPF** (*Post-Market Performance Follow-up*, equivalente al PMCF) |
| SGC de referencia | ISO 13485 (igual) | ISO 13485 (igual) |
| Gestión de riesgos | ISO 14971 (igual) | ISO 14971 (igual) |
| Ciclo de vida software | IEC 62304 (igual) | IEC 62304 (igual) |
| Organismo notificado | Designación MDR | **Designación IVDR específica** — comprobar en NANDO que el organismo elegido cubre IVDR, no solo MDR (frecuentemente son designaciones distintas) |
| Autoridad competente España | AEMPS | AEMPS (misma autoridad, distinto reglamento) |
| Base de datos | EUDAMED (módulos compartidos MDR/IVDR) | EUDAMED (mismos módulos) |
| Vigilancia | PMS + PSUR (Anexo III MDR) | PMS + PSUR (Anexo III IVDR, régimen equivalente) |

**Laboratorios que desarrollan su propio ensayo (LDT — *lab-developed test*):**
si el software de interpretación se desarrolla y usa **dentro de un único
laboratorio clínico** de una institución sanitaria de la UE, sin ponerse en el
mercado, puede acogerse a la excepción del art. 5.5 IVDR ("productos
fabricados y utilizados únicamente dentro de instituciones sanitarias
establecidas en la Unión") si cumple **todas** las condiciones del artículo
(no transferencia a otra entidad legal, justificación de que no hay producto
equivalente en el mercado, SGC ISO 15189, información pública sobre su uso,
etc.). Si el software se distribuye a **otras** instituciones o se
comercializa, la excepción **no aplica** y hay que seguir la vía IVDR
completa.

---

## 4. Salida esperada del paso

1. **¿MDR o IVDR?** — con la justificación de los pasos de la sección 1.
2. **Clase IVDR (A/B/C/D)** con la regla aplicada y ejemplos comparables.
3. **Vía de evaluación de conformidad** por clase (tabla §1) y si el organismo
   notificado necesita designación IVDR específica.
4. **Evaluación del funcionamiento**: qué evidencia de rendimiento analítico y
   clínico existe ya en el repositorio (métricas, validaciones, datasets de
   test) — cuenta como validación analítica parcial, igual que en MDR.
5. Si aplica la excepción de **producto de institución sanitaria** (art. 5.5):
   señalarlo como vía alternativa y sus condiciones pendientes de acreditar.
6. Todo lo demás del informe (RGPD, IA, ciberseguridad, SBOM, entregables de
   datos) se mantiene **igual** que para un MDSW bajo MDR — usa las mismas
   referencias (`rgpd-datos.md`, `ia-aiact.md`, `entregables-datos-y-seguridad.md`,
   `sbom-vulnerabilidades.md`), sustituyendo "MDR" por "IVDR" y "CER/PMCF" por
   "PER/PMPF" donde corresponda en la tabla de cumplimiento.
