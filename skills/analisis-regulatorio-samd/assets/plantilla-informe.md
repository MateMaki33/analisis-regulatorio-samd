# Informe de situación regulatoria — {NOMBRE_PROYECTO}

- **Fecha del análisis:** {AAAA-MM-DD}
- **Ámbito de comercialización asumido:** España / UE
- **Fuentes normativas de referencia:** MDR (UE) 2017/745 {o IVDR (UE) 2017/746 si
  aplica}, RD 192/2023, guías MDCG, normas UNE-EN/ISO/IEC, RGPD (UE) 2016/679 +
  LOPDGDD, AI Act (UE) 2024/1689, EHDS (UE) 2025/327 {si aplica}.
- **Fecha del contraste normativo en internet:** {AAAA-MM-DD}
- **Puntos verificados en internet:** {lista: EUDAMED, normas armonizadas DOUE, guías MDCG, AI Act, AEPD apps salud, NIS2 España, decisiones de adecuación + EU-US Data Privacy Framework, SBOM/MDCG 2019-16 + Cyber Resilience Act, normas armonizadas IVDR/MDCG 2020-16, calendario EHDS + autoridad española… con URL}. {o "ninguno: producto sin datos personales ni finalidad sanitaria"}

> **Aviso.** Documento orientativo de planificación. No sustituye asesoría legal o
> regulatoria. La clasificación vinculante y la evaluación de conformidad las
> confirma un organismo notificado. Antes de decisiones de inversión o diseño,
> verificar los textos vigentes en EUR-Lex, BOE y AEMPS.

---

## 1. Resumen ejecutivo

- **¿Es producto sanitario (MDSW)?** {SÍ / NO / FRONTERA} — {1-2 frases}
- **¿MDR o IVDR?** {MDR / IVDR / n. a.} — {1 frase de justificación si es IVDR}
- **Clase MDR (Regla 11) o IVDR (Reglas 1-7):** {I / IIa / IIb / III · o · A / B / C / D} — confianza {alta/media/baja}
- **Clase de seguridad IEC 62304:** {A / B / C}
- **¿Sistema de IA de alto riesgo (AI Act)?** {sí / no / n. a.}
- **¿Es también "sistema EHR" (EHDS)?** {sí / no / n. a.} — {1 frase}
- **Vía de evaluación de conformidad:** {autocertificación / organismo notificado}
- **Nivel de madurez regulatoria estimado:** {inicial / parcial / avanzado} — {%
  aproximado de elementos cubiertos}
- **Los 3-5 riesgos más urgentes:** {lista corta}

---

## 2. Descripción del producto analizada

- **Finalidad prevista declarada:** {texto}
- **Usuarios y entorno de uso:** {profesional / paciente / investigación; entorno}
- **Qué hace con los datos:** {registra / muestra / calcula / interpreta / predice / decide}
- **Stack y componentes** (de la exploración del repo): {lenguajes, frameworks, IA, terceros}
- **Evidencia clave del repositorio:** {fichero:línea → qué demuestra}
- **Cobertura de la exploración:** {nº de ficheros leídos íntegramente, carpetas
  excluidas (`node_modules`, `dist`...), y si se alcanzó el límite de 80
  ficheros por categoría — en ese caso, qué se priorizó y qué quedó fuera}

---

## 3. Calificación como producto sanitario (MDCG 2019-11)

- Aplicación del test de calificación: {las 3 condiciones, cumplida/no}
- Casos frontera considerados: {…}
- **Conclusión:** {…} 
- **Entregable:** análisis de calificación por escrito — **obligatorio aunque la
  conclusión sea NO** (lo exige una inspección de AEMPS / el organismo
  notificado). Estado en el repo: {presente / ausente en `docs/regulatory/`}.
- Si NO es PS: normativa que sigue aplicando → {RGPD, ISO/IEC 82304-1, directrices
  AEPD apps de salud} + secciones 7.2-7.5 de este informe (entregables de datos,
  transferencias, SBOM si hay datos personales). **Fin del análisis de producto
  sanitario.**

---

## 3b. ¿MDR o IVDR? {incluir solo si el producto es SÍ/FRONTERA en la sección 3}

- Aplicación del árbol MDR/IVDR (MDCG 2019-11 Rev.1, Figura 2): {pasos y resultado}
- **Conclusión:** {MDR / IVDR} — {justificación}
- Si es **IVDR**: la sección 4 de este informe se sustituye por la
  clasificación IVDR (clases A-D, Reglas 1-7 Anexo VIII IVDR — ver
  `references/ivdr-diagnostico-in-vitro.md`), y en la sección 5 "evaluación
  clínica (CER)" se sustituye por "evaluación del funcionamiento (PER + PMPF)".

---

## 4. Clasificación por riesgo (Regla 11, Anexo VIII MDR — o Reglas 1-7 IVDR si aplica)

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
| MDR (UE) 2017/745 {o IVDR si aplica} | Obligatoria | {} | {} | {} | Evaluación de conformidad por la vía de la clase → declaración UE + marcado CE · {autocertificación / organismo notificado}; autoridad AEMPS · expediente técnico + DoC · antes de comercializar | {} |
| RD 192/2023 | Obligatoria (ES) | {} | {} | {} | IFU/etiquetado en español + responsable técnico titulado + alta en registro AEMPS · AEMPS · registro CCPS / Responsables · previo al mercado ES | {} |
| EHDS (UE) 2025/327 {si es sistema EHR; si no, omitir fila} | Condicional | {} | {} | {} | Requisitos esenciales Anexo II (interoperabilidad EEHRxF + seguridad/registro de accesos) → declaración + marcado CE EHDS → registro en base de datos UE · autoridad de vigilancia EHR (a designar) · documentación técnica + declaración · componentes armonizados desde 2029/2031 {verificar} | {} |
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

### 6.7 SBOM y gestión de vulnerabilidades de dependencias
- **¿SBOM obligatorio aquí?** {sí de facto — MDCG 2019-16 + IEC 81001-5-1 + RGSF Anexo I.17 / sí por CRA / sí por RGPD 32 / recomendado} — **motivo:** {…}
- **¿Gestión de vulnerabilidades obligatoria?** {sí/…} — **motivo:** {…}
- **Inventario de dependencias** (de `supply_chain.dependency_counts` / `manifests`):
  | Manifiesto | Nº deps directas (aprox.) | ¿Versiones fijadas (lockfile)? |
  |---|---|---|
  | {…} | {…} | {sí/no} |
- **Estado actual:**
  | Elemento | Estado | Evidencia (`fichero`) |
  |---|---|---|
  | SBOM generado (CycloneDX/SPDX) | {presente/ausente} | {supply_chain.sbom_files} |
  | SCA / cribado CVE en CI (Dependabot, Renovate, Trivy, osv-scanner…) | {…} | {supply_chain.sca_config} |
  | Política de divulgación coordinada (CVD) | {…} | {SECURITY.md / security.txt} |
  | VEX | {…} | {…} |
- **Recomendación concreta:** generar SBOM con `{comando según stack}`; cribar con `{herramienta}`; añadir `SECURITY.md` si falta. Regenerar el SBOM por *release* y entregarlo al organismo notificado por versión.
- **Brechas:** {…}

---

## 7. Protección de datos (RGPD / LOPDGDD), entregables, transferencias y vulnerabilidades

### 7.1 Bases jurídicas propuestas
| Finalidad | Base art. 6 | Excepción art. 9 |
|---|---|---|
| {…} | {…} | {…} |

### 7.2 Entregables de datos y seguridad — ¿cuál debe generar este proyecto?
**Leyenda:** obligatorio 🔴 · recomendado 🟠 · no aplica ⚪ · estado: presente / parcial / ausente.

| # | Documento | ¿Obligatorio aquí? | Base | Estado | Cómo se genera / quién lo pide |
|---|---|---|---|---|---|
| 1 | Análisis de calificación (incl. "no es PS") | {} | MDCG 2019-11 | {} | Interno · AEMPS / ON |
| 2 | Análisis de riesgos del tratamiento | {} | RGPD 24, 32 | {} | Interno + DPO · guía/herramienta AEPD |
| 3 | DPIA / EIPD | {} | RGPD 35 | {} | Interno + DPO · consulta previa AEPD (36) si riesgo alto no mitigable |
| 4 | RAT | {} | RGPD 30 | {} | Interno · plantilla AEPD |
| 5 | DPA / contrato de encargado (uno por proveedor) | {} | RGPD 28 | {} | Contrato con cada encargado (+ CCT/TIA si fuera del EEE) — proveedores: {…} |
| 6 | Procedimiento + registro de brechas | {} | RGPD 33-34 | {} | Interno · AEPD (formulario NBD, 72 h) |
| 7 | TIA (una por transferencia vía art. 46) | {} | Schrems II · EDPB 01/2020 | {} | Interno — ver 7.5 |
| 8 | Cláusulas informativas / privacidad en capas | {} | RGPD 12-14 | {} | Interno |
| 9 | Nota de transparencia sobre uso de IA | {} | RGPD 13-14/22 · AI Act 13/50 | {} | Interno · integrada en IFU · AESIA/AEPD |
| 10 | Designación de DPO | {} | RGPD 37-39 · LOPDGDD 34 | {} | Nombramiento + comunicación a la AEPD |
| 11 | SBOM | {} | MDCG 2019-16 · IEC 81001-5-1 · (CRA) | {} | Ver 6.7 |
| 12 | Gestión de vulnerabilidades + VEX + CVD | {} | ídem · RGPD 32 | {} | Ver 6.7 |

Para cada documento 🔴: *"Qué es: … · Cómo se genera: …"*.

### 7.3 Checklist de obligaciones RGPD (detalle)
| Obligación | Estado | Nota |
|---|---|---|
| Análisis de riesgos del tratamiento | {hecho/no} | {nivel de riesgo → ¿escala a DPIA?} |
| EIPD/DPIA | {exigible: sí/no} · {hecha/no} | {motivo de exigibilidad} |
| RAT | {…} | |
| Contratos de encargado / DPA (art. 28) | {…} | {proveedores sin DPA: …} |
| Transferencias internacionales | {…} | {ver 7.5} |
| Privacidad desde el diseño/por defecto | {…} | |
| Seguridad (art. 32) | {…} | |
| Gestión de brechas (33-34) — procedimiento previo + registro | {…} | |
| DPO | {obligatorio: sí/no} | |
| Información y derechos | {…} | |
| Transparencia sobre IA (13-14/22) | {…} | {si hay IA} |
| Menores / investigación en salud | {…} | |
| Ley 41/2002 (si historia clínica) | {…} | |

### 7.4 Vulnerabilidades detectadas (priorizadas)
*Descripción = qué es el hallazgo, nunca el valor literal del secreto o dato
personal (p. ej. "API key de Stripe en texto plano", no la clave en sí).*

| # | Severidad | Categoría | Ubicación | Descripción | Norma afectada | Remediación |
|---|---|---|---|---|---|---|
| 1 | {Crítica/Alta/Media} | {secreto / TLS / log PII / inyección / tercero / cifrado reposo / dependencia con CVE} | {fichero:línea} | {…} | {RGPD 32 / IEC 81001-5-1 / …} | {…} |

### 7.5 Transferencias internacionales y flujos de datos
**¿Salen datos personales del EEE?** {sí/no} — {resumen: regiones no europeas, proxies/CDNs, APIs de IA, terceros}.

| Flujo | Datos personales | Proveedor / componente | Rol | País / región | ¿Sale del EEE? | Mecanismo cap. V | ¿TIA? | Estado / brecha |
|---|---|---|---|---|---|---|---|---|
| Hosting de la aplicación | Todos | {} | Encargado | {} | {sí/no} | {adecuación / CCT+TIA / DPF} | {sí/no/hecho/n.a.} | {} |
| Base de datos / almacenamiento | Todos | {} | Encargado | {} | {} | {} | {} | {} |
| *Backup* / réplica | Todos | {} | Subencargado | {} | {} | {} | {} | {} |
| API de IA / LLM | {campos enviados} | {} | Encargado | {EE. UU. asumido} | {} | {} | {} | {} |
| Analítica / *crash reporting* / APM | Identificadores, IP, trazas | {} | Encargado | {} | {} | {} | {} | {} |
| CDN / proxy / WAF | IP, cabeceras, contenido | {} | Encargado | {} | {} | {} | {} | {} |
| Correo / SMS / *push* | Contacto, contenido | {} | Encargado | {} | {} | {} | {} | {} |

- **Decisiones de adecuación / EU-US Data Privacy Framework** (verificado {fecha} · {URL}): {…}
- **Flujos sin cobertura del cap. V (brecha crítica):** {…}
- **Acciones:** {repatriar a región europea / firmar CCT + TIA / verificar adhesión al DPF del proveedor X / suprimir flujo}.

### 7.6 Conclusión de datos
- ¿DPIA exigible? {sí/no + motivo}. ¿Consulta previa AEPD? {…}
- Datos de salud a terceros / IA como servicio: {…}
- Documentos que faltan y son obligatorios: {lista destilada de 7.2}.

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

## 8b. EHDS — sistema EHR (Reglamento (UE) 2025/327) — {aplica / no aplica}

- **¿Es "sistema EHR"?** {sí/no} — categorías prioritarias tratadas:
  {resumen del paciente / receta-dispensación electrónica / imagen médica e
  informe / resultado de laboratorio / informe de alta} — rol del software:
  {almacena / intermedia / exporta / importa / convierte / edita / visualiza}
- **Requisitos esenciales (Anexo II):**
  | Requisito | Estado | Evidencia / brecha |
  |---|---|---|
  | Generales (funciona según lo previsto, seguridad del paciente) | {…} | {…} |
  | Interoperabilidad (EEHRxF, sin restricciones de acceso/exportación) | {…} | {ehds.interoperabilidad_ehr} |
  | Seguridad y registro de accesos | {…} | {ehds.registro_acceso_ehr} |
- **Declaración UE de conformidad + marcado CE EHDS:** {obligatorio/no} — estado {…}
- **Registro en la base de datos UE de sistemas EHR:** {hecho/pendiente}
- **Calendario de exigibilidad** (verificado {fecha} · {URL}): componentes
  armonizados desde {principios de 2029 / 2031 según categoría — o "verificar"}
- **Uso secundario de datos de salud** (investigación / entrenamiento de IA con
  datos reutilizados): {aplica/no} — {permiso de datos pendiente/obtenido}
- **Relación con MDR/IVDR y RGPD:** el EHDS se **suma**, no sustituye

---

## 9. Ruta a la conformidad — plan por fases

| Fase | Acción | Entregable | Organismo | Prioridad |
|---|---|---|---|---|
| 0 | Congelar finalidad prevista y clasificación por escrito | Análisis de calificación + determinación de clase | interno | Inmediata |
| 0 | Cerrar brechas de datos obligatorias sin coste de certificación | RAT, análisis de riesgos del tratamiento, DPA pendientes, procedimiento de brechas, cláusulas informativas | interno / AEPD | Inmediata |
| 0 | Resolver transferencias fuera del EEE sin cobertura | TIA / CCT / repatriación de flujos | interno | Inmediata |
| 1 | {DPIA si exigible} | {EIPD + consulta previa AEPD si procede} | {AEPD} | {Alta} |
| 1 | {Generar SBOM + activar SCA en CI + CVD} | {SBOM CycloneDX + informe SCA + SECURITY.md} | {interno; el ON lo audita} | {Alta} |
| … | {…} | {…} | {…} | {…} |

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

## Anexo A. Índice de siglas

Todas las siglas y acrónimos usados en este informe, en orden alfabético.

| Sigla | Significado |
|---|---|
| {…} | {…} |

---

*Generado con la skill `analisis-regulatorio-samd`. Contenido normativo a fecha
{AAAA-MM-DD}; verificar cambios en EUR-Lex / BOE / AEMPS antes de decisiones
vinculantes.*
