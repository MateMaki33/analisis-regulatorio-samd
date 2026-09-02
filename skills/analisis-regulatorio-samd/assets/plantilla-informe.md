# Informe de situación regulatoria — {NOMBRE_PROYECTO}

- **Fecha del análisis:** {AAAA-MM-DD}
- **Ámbito de comercialización asumido:** España / UE
- **Fuentes normativas de referencia:** MDR (UE) 2017/745, RD 192/2023, guías MDCG,
  normas UNE-EN/ISO/IEC, RGPD (UE) 2016/679 + LOPDGDD, AI Act (UE) 2024/1689.
- **Fecha del contraste normativo en internet:** {AAAA-MM-DD}
- **Puntos verificados en internet:** {lista: EUDAMED, normas armonizadas DOUE, guías MDCG, AI Act, AEPD apps salud, NIS2 España… con URL}. {o "ninguno: producto sin datos personales ni finalidad sanitaria"}

> **Aviso.** Documento orientativo de planificación. No sustituye asesoría legal o
> regulatoria. La clasificación vinculante y la evaluación de conformidad las
> confirma un organismo notificado. Antes de decisiones de inversión o diseño,
> verificar los textos vigentes en EUR-Lex, BOE y AEMPS.

---

## 1. Resumen ejecutivo

- **¿Es producto sanitario (MDSW)?** {SÍ / NO / FRONTERA} — {1-2 frases}
- **Clase MDR (Regla 11):** {I / IIa / IIb / III} — confianza {alta/media/baja}
- **Clase de seguridad IEC 62304:** {A / B / C}
- **¿Sistema de IA de alto riesgo (AI Act)?** {sí / no / n. a.}
- **Vía de evaluación de conformidad:** {autocertificación / organismo notificado}
- **Nivel de madurez regulatoria estimado:** {inicial / parcial / avanzado} — {%
  aproximado de elementos cubiertos}
- **Los 3-5 riesgos más urgentes:** {lista corta}

---

## 2. Descripción del producto analizada

- **Finalidad prevista declarada:** {texto}
- **Usuarios y entorno de uso:** {profesional / paciente / investigación; entorno}
- **Qué hace con los datos:** {registra / muestra / calcula / interpreta / predice / decide}
- **Stack y componentes** (del escáner): {lenguajes, frameworks, IA, terceros}
- **Evidencia clave del repositorio:** {fichero:línea → qué demuestra}

---

## 3. Calificación como producto sanitario (MDCG 2019-11)

- Aplicación del test de calificación: {las 3 condiciones, cumplida/no}
- Casos frontera considerados: {…}
- **Conclusión:** {…} 
- Si NO es PS: normativa que sigue aplicando → {RGPD, ISO/IEC 82304-1, directrices
  AEPD apps de salud}. **Fin del análisis de producto sanitario.**

---

## 4. Clasificación por riesgo (Regla 11, Anexo VIII MDR)

- Eje "importancia de la información": {informa / orienta decisión / diagnostica-trata}
- Eje "criticidad del cuadro / paciente": {no grave / grave / crítico-vital}
- Regla(s) aplicada(s) y subregla: {…}
- **Clase resultante:** {…}
- **Datos que faltan para cerrar la clasificación:** {…}
- Clase de seguridad IEC 62304 y justificación del daño posible: {…}

---

## 5. Cumplimiento norma por norma

**Leyenda de veredicto:** ✅ Cumple · 🟡 Cumple parcialmente · ❌ No cumple ·
⬜ No evaluable (sin evidencia).

| Norma / Reglamento | Obligatoriedad | Veredicto | Evidencia (`fichero:línea` o "no encontrado") | Brecha concreta | Cómo se gestiona (proceso · organismo · entregable · hito) | Fuente verificada (URL · fecha) |
|---|---|---|---|---|---|---|
| MDR (UE) 2017/745 | Obligatoria | {} | {} | {} | Evaluación de conformidad por la vía de la clase → declaración UE + marcado CE · {autocertificación / organismo notificado}; autoridad AEMPS · expediente técnico + DoC · antes de comercializar | {} |
| RD 192/2023 | Obligatoria (ES) | {} | {} | {} | IFU/etiquetado en español + responsable técnico titulado + alta en registro AEMPS · AEMPS · registro CCPS / Responsables · previo al mercado ES | {} |
| ISO 13485:2016 | {De facto IIa+ / Recom. I} | {} | {} | {} | Implantar SGC → auditoría de certificación · organismo notificado · certificado ISO 13485 (~3 años) · antes de la evaluación de conformidad | {} |
| ISO 14971:2019 | De facto | {} | {} | {} | Proceso de gestión de riesgos continuo enlazado a 62304/62366-1/ciberseg. · el ON audita · Risk Management File · revisión antes de cada liberación | {} |
| IEC 62304 (clase {A/B/C}) | De facto | {} | {} | {} | Procesos de ciclo de vida en el tooling + doc. de proceso · el ON muestrea trazabilidad · expediente de desarrollo + SBOM · durante el desarrollo | {} |
| IEC 62366-1 | De facto | {} | {} | {} | Ingeniería de usabilidad + estudios con usuarios (formativa + sumativa) · el ON revisa · Usability Engineering File · antes de la evaluación de conformidad | {} |
| IEC 81001-5-1 + MDCG 2019-16 | De facto | {} | {} | {} | Seguridad en el ciclo de vida + SBOM + SAST/SCA/pentest + gestión de parches y CVE · el ON audita; divulgación con INCIBE-CERT · plan de ciberseguridad + informes · ciclo de vida completo | {} |
| Evaluación clínica (MDCG 2020-1) | Obligatoria | {} | {} | {} | CEP → evidencia (validez científica + validación analítica + validación clínica) → CER + PMCF · el ON revisa el CER; investigación clínica ante AEMPS + CEIm · CER · antes de CE y continuo | {} |
| EUDAMED + UDI | Obligatoria | {} | {} | {} | Alta de actor (SRN) + registro de producto (Basic UDI-DI / UDI-DI) · EUDAMED + AEMPS; emisor de UDI (GS1/HIBCC/ICCBBA) · registros + etiqueta UDI · antes de comercializar {verificar calendario} | {} |
| PMS / PSUR (Anexo III) | Obligatoria | {} | {} | {} | Plan de PMS + recogida de datos → PMS report (I) / PSUR (IIa-III); notificación de incidentes y FSCA · AEMPS (NotificaPS); el ON supervisa · plan PMS + PSUR + FSN · poscomercialización permanente | {} |
| RGPD + LOPDGDD | Obligatoria | {} | {ver sección 7} | {} | Responsabilidad proactiva: bases jurídicas art. 6+9, DPIA, RAT, contratos art. 28, medidas art. 32 · AEPD (consulta previa solo si riesgo alto no mitigable) · RAT + DPIA + contratos · desde el diseño | {} |
| AI Act (UE) 2024/1689 | {Condicional — IA} | {} | {ver sección 8} | {} | Obligaciones arts. 8-17 integradas en la evaluación de conformidad del MDR · organismo notificado con designación AI Act; vigilancia AESIA · doc. técnica ampliada + registro UE · {fecha de exigibilidad verificada} | {} |
| Cyber Resilience Act | {Condicional} | {} | {} | {} | Solo para componentes que no califican como PS (fuera del MDR) · — · — · — | {} |
| NIS2 (nivel organización) | {Condicional} | {} | {} | {} | Medidas de gestión de riesgos + notificación de incidentes si el operador es entidad esencial/importante de salud · CCN-CERT / INCIBE-CERT / Centro Nacional de Ciberseguridad · políticas + registro de incidentes · tras transposición ES {verificar} | {} |
| ISO/IEC 27001 (+ 27799) | Recomendada | {} | {} | {} | SGSI certificado por entidad acreditada; apoya RGPD art. 32 y NIS2; suele exigirlo el cliente hospitalario · entidad de certificación · certificado · — | {} |

**Obligatorio "sí o sí" para este proyecto:** {lista destilada}.

**Frase de cierre por norma** ("Para pasar a ✅ Cumple: …"):
- MDR: {…}
- ISO 14971: {…}
- IEC 62304: {…}
- IEC 81001-5-1: {…}
- RGPD: {…}
- {resto}

---

## 6. Requisitos técnicos: en qué acierta y qué falta

Detalle que sustenta los veredictos de la sección 5. Para cada bloque:
**veredicto** (✅ / 🟡 / ❌ / ⬜) + evidencia (`fichero:línea`) + brecha + acción
+ cómo se gestiona.

### 6.1 Sistema de gestión de calidad (ISO 13485)
{…}

### 6.2 Gestión de riesgos (ISO 14971)
{…}

### 6.3 Ciclo de vida del software (IEC 62304) — clase {A/B/C}
- Procesos exigibles por la clase vs. lo observado en el repo (control de
  versiones, trazabilidad de requisitos, tests, CI, changelog, SOUP/SBOM): {…}

### 6.4 Usabilidad (IEC 62366-1)
{…}

### 6.5 Ciberseguridad (IEC 81001-5-1 / MDCG 2019-16)
{…}

### 6.6 Información al usuario (ISO 20417 / RD 192/2023)
{…}

---

## 7. Protección de datos (RGPD / LOPDGDD) y vulnerabilidades

### 7.1 Bases jurídicas propuestas
| Finalidad | Base art. 6 | Excepción art. 9 |
|---|---|---|
| {…} | {…} | {…} |

### 7.2 Checklist de obligaciones
| Obligación | Estado | Nota |
|---|---|---|
| EIPD/DPIA | {exigible: sí/no} · {hecha/no} | {…} |
| RAT | {…} | |
| Contratos de encargado (art. 28) | {…} | {proveedores: …} |
| Transferencias internacionales | {…} | {…} |
| Privacidad desde el diseño/por defecto | {…} | |
| Seguridad (art. 32) | {…} | |
| Gestión de brechas (33-34) | {…} | |
| DPO | {obligatorio: sí/no} | |
| Información y derechos | {…} | |
| Menores / investigación en salud | {…} | |
| Ley 41/2002 (si historia clínica) | {…} | |

### 7.3 Vulnerabilidades detectadas (priorizadas)
| # | Severidad | Categoría | Ubicación | Descripción | Norma afectada | Remediación |
|---|---|---|---|---|---|---|
| 1 | {Crítica/Alta/Media} | {secreto / TLS / log PII / inyección / tercero / cifrado reposo} | {fichero:línea} | {…} | {RGPD 32 / IEC 81001-5-1 / …} | {…} |

### 7.4 Conclusión de datos
- ¿DPIA exigible? {sí/no + motivo}. ¿Consulta previa AEPD? {…}
- Datos de salud a terceros / IA como servicio: {…}

---

## 8. Inteligencia artificial (AI Act) — {aplica / no aplica}

- ¿Sistema de IA? Rol: {proveedor / desplegador}
- Categoría: {alto riesgo por art. 6.1 vía MDR / limitado / mínimo}
- Fecha de exigibilidad aplicable (verificada {fecha}): {…}
- Obligaciones (arts. 8-17) y estado:
  | Obligación | Estado | Evidencia / brecha |
  |---|---|---|
  | Gestión de riesgos de IA (integrada con 14971) | {…} | {…} |
  | Gobernanza de datos de entrenamiento | {…} | {…} |
  | Documentación técnica (Anexo IV) | {…} | |
  | Registro y logging (art. 12) | {…} | {ai_ml.* / logging} |
  | Transparencia e IFU (art. 13) | {…} | |
  | Supervisión humana (art. 14) | {…} | |
  | Exactitud / robustez / ciberseguridad (art. 15) | {…} | {ai_ml.dataset_sesgo, explicabilidad} |
- Organismo notificado: ¿tiene designación AI Act? {verificar}
- GPAI de terceros usados: {…}

---

## 9. Ruta a la conformidad — plan por fases

| Fase | Acción | Entregable | Organismo | Prioridad |
|---|---|---|---|---|
| 0 | Congelar finalidad prevista y clasificación por escrito | Documento de determinación | interno | Inmediata |
| 1 | {…} | {…} | {…} | {…} |
| … | | | | |

**Estimación de coste/tiempo** (orientativa de mercado, confirmar con CNCps/
consultora): {clase I → interno; IIa-III → tasas CNCps ~22-27 k€, proyecto total
~200-800 k€, 12-24 meses}.

---

## 10. Conclusiones

- **En qué acierta el proyecto:** {…}
- **En qué grupo/clase entra:** {…}
- **A falta de qué está (brechas):** {…}
- **Dónde están los riesgos:** {regulatorios, de datos, de seguridad, de plazos}
- **Siguientes 3 pasos recomendados:** {…}

---

*Generado con la skill `analisis-regulatorio-samd`. Contenido normativo a fecha
{AAAA-MM-DD}; verificar cambios en EUR-Lex / BOE / AEMPS antes de decisiones
vinculantes.*
