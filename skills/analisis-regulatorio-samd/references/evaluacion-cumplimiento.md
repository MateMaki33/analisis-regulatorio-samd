# Evaluación de cumplimiento norma por norma

Cómo emitir, para cada norma aplicable, un **veredicto de cumplimiento** con
evidencia y una explicación de **cómo se gestiona** (proceso, organismo,
entregable, plazo).

---

## Escala de veredicto

| Veredicto | Criterio |
|---|---|
| **Cumple** | Hay evidencia verificable de que todos los ítems clave están cubiertos. |
| **Cumple parcialmente** | Algunos ítems cubiertos con evidencia; otros ausentes o incompletos. |
| **No cumple** | Ítems clave ausentes, o hay evidencia de incumplimiento (p. ej. vulnerabilidad activa, dato sensible en claro). |
| **No evaluable** | No hay acceso a la evidencia necesaria (documentación de SGC, RMF, contratos…). Indicar qué habría que aportar. |

Regla: un análisis sobre solo el repositorio **casi nunca** puede dar "Cumple" en
normas de proceso (13485, 14971, evaluación clínica) porque su evidencia es
documental y externa al código. En esos casos, el veredicto honesto suele ser
"No evaluable" o "Cumple parcialmente", y el valor está en la columna *brecha* y
*cómo se gestiona*.

---

## Qué mirar y cómo se gestiona — por norma

Para cada una: **ítems verificables** · **dónde buscar la evidencia** · **cómo se
gestiona** (proceso → organismo → entregable → plazo/hito).

### MDR (UE) 2017/745
- **Ítems:** finalidad prevista documentada; clasificación justificada por escrito;
  análisis de RGSF (Anexo I) con checklist; expediente técnico (Anexos II-III);
  PRRC (art. 15) designada; declaración UE de conformidad; marcado CE.
- **Evidencia:** carpeta `regulatory/`, `docs/`, `quality/`; `README` con
  *intended use*; ausencia total = "No evaluable / No cumple" según contexto.
- **Cómo se gestiona:** proceso = determinación → evaluación de conformidad por la
  vía de la clase (Anexos IX-XI) → declaración + CE. Organismo = **autocertificación
  (clase I)** o **organismo notificado (IIa/IIb/III)**; autoridad = **AEMPS**.
  Entregable = expediente técnico + DoC. Hito = antes de comercializar.

### RD 192/2023 (España)
- **Ítems:** IFU y etiquetado **en español**; responsable técnico con titulación
  universitaria superior; inscripción en el registro AEMPS que corresponda;
  cumplimiento de normas de publicidad.
- **Evidencia:** ficheros de i18n/locales (`es`, `es-ES`), textos legales,
  `docs/ifu`.
- **Cómo se gestiona:** alta en **AEMPS** (Registro de Responsables para clase I /
  Registro de Comercialización — app CCPS — para IIa-III); designación interna de
  responsable técnico. Plazo = previo a puesta en el mercado en España.

### ISO 13485:2016 — SGC
- **Ítems:** manual/mapa de procesos; SOP de diseño y desarrollo (7.3); control
  documental; evaluación de proveedores críticos; CAPA; auditorías internas;
  revisión por la dirección; DHF.
- **Evidencia:** casi nunca en código. Señales indirectas: `docs/qms|sop`,
  plantillas de PR/issue, política de ramas, CI con *gates*, `CODEOWNERS`.
- **Cómo se gestiona:** implantación del SGC → **auditoría de certificación por
  organismo notificado** (obligatoria IIa+). Entregable = certificado ISO 13485
  (~3 años, con auditorías de seguimiento anuales). Clase I: SGC documentado
  equivalente, sin certificado obligatorio.

### ISO 14971:2019 — Gestión de riesgos
- **Ítems:** plan de gestión de riesgos; tabla de análisis (peligros → situaciones
  peligrosas → daños) incl. ciberseguridad, errores de uso y (si IA) rendimiento
  del modelo; criterios de aceptabilidad a priori; controles priorizados
  (diseño > protección > información); verificación de eficacia; riesgo residual
  global; informe de gestión de riesgos; evaluación beneficio-riesgo.
- **Evidencia:** `docs/risk`, `hazard-analysis.xlsx|md`, issues etiquetados
  `risk`. `findings.security.*` y `findings.logging_pii` = peligros ya
  identificables → si no están en ningún RMF, es brecha.
- **Cómo se gestiona:** proceso interno continuo enlazado a IEC 62304, 62366-1 y
  MDCG 2019-16. Entregable = **Risk Management File**. Organismo = el ON lo audita
  en detalle (IIa+). Hito = revisión antes de cada liberación comercial.

### IEC 62304:2006+A1:2015 — Ciclo de vida del software
- **Ítems (según clase A/B/C):** plan de desarrollo; SRS con IDs trazables;
  arquitectura (B/C); diseño detallado (C); verificación de unidades con criterios
  (B/C); pruebas de integración (B/C); pruebas de sistema; procedimiento de
  liberación; gestión de configuración (SCM); gestión de problemas; plan de
  mantenimiento; **inventario SOUP / SBOM** con análisis de anomalías conocidas.
- **Evidencia (sí visible en repo):** control de versiones con historia trazable;
  carpeta de tests + cobertura; pipeline CI reproducible; `CHANGELOG`;
  versionado semántico; fichero de requisitos / matriz de trazabilidad;
  `manifests` (base del SOUP) y su fijación de versiones; issues enlazados a
  commits.
- **Cómo se gestiona:** se materializa en el tooling del proyecto + documentación
  de proceso. Organismo = el ON revisa la documentación y muestrea trazabilidad
  requisito→código→prueba→riesgo. Entregable = expediente de desarrollo + SBOM.
- **Veredicto típico:** aquí sí se puede dar "Cumple parcialmente" con evidencia
  concreta del repo (p. ej. "hay tests y CI y changelog, falta SRS trazable y
  SBOM").

### IEC 62366-1:2015+A1:2020 — Usabilidad
- **Ítems:** especificación de uso (usuarios, entorno, UI relacionada con la
  seguridad); análisis de errores de uso y escenarios peligrosos; requisitos de
  UI; evaluación formativa; **evaluación sumativa** con usuarios representativos.
- **Evidencia:** ficheros de UI (`.tsx/.jsx/.vue/.swift/.kt` de vistas); textos de
  alertas y de dosis en la interfaz (`clinical.tratamiento_dosis` en vistas =
  superficie crítica); carpeta `research/usability`.
- **Cómo se gestiona:** proceso de ingeniería de usabilidad → estudios con
  usuarios (n según riesgo, típicamente ≥15/grupo en sumativa). Entregable =
  **Usability Engineering File**. Organismo = el ON lo revisa; enlaza con ISO
  14971 y con la IFU.

### IEC 81001-5-1:2021 + MDCG 2019-16 Rev.1 — Ciberseguridad
- **Ítems:** requisitos de seguridad; modelado de amenazas (STRIDE); autenticación
  y autorización; cifrado en tránsito y en reposo; gestión de secretos;
  actualización firmada; **SBOM** + evaluación de componentes; SAST/SCA/DAST/
  pentest; proceso de gestión de vulnerabilidades y parches poscomercialización
  (vigilancia CVE, divulgación coordinada); información de seguridad al usuario
  (MDS2 o equivalente).
- **Evidencia (muy visible en repo):** `findings.security.*` es la entrada
  principal —
  `secreto_hardcoded`/`aws_key`/`clave_privada`/`jwt_literal` → **No cumple** en
  gestión de secretos;
  `tls_desactivado`/`http_inseguro` → **No cumple** en cifrado en tránsito;
  `hash_debil` → criptografía obsoleta;
  `sql_concat`/`eval_dinamico` → validación de entrada;
  `cifrado_reposo` presente → indicio a favor.
  `manifests` → base del SBOM y del cribado CVE.
  Config de seguridad en CI (dependabot/renovate, SAST) → a favor.
- **Cómo se gestiona:** actividades integradas en el ciclo de vida IEC 62304;
  exigible por el RGSF Anexo I punto 17 del MDR. Organismo = el ON audita el plan
  de ciberseguridad; divulgación coordinada con **INCIBE-CERT / CSIRT**.
  Entregable = plan de gestión de ciberseguridad + SBOM + informes de pruebas.

### Evaluación clínica (MDCG 2020-1)
- **Ítems:** Plan de Evaluación Clínica (CEP); demostración de validez científica,
  validación analítica/técnica y validación clínica; Informe de Evaluación
  Clínica (CER); plan de PMCF.
- **Evidencia:** normalmente externa al repo. En el repo puede haber: informes de
  validación del modelo/algoritmo, métricas (sensibilidad/especificidad/AUC),
  datasets de test → cuenta como validación analítica parcial.
- **Cómo se gestiona:** proceso interno + literatura + posible investigación
  clínica propia (autorización/notificación a **AEMPS** + dictamen de **CEIm**).
  Organismo = el ON revisa el CER (IIa+); clase III y ciertos IIb → posible
  escrutinio de panel de expertos UE (CECP). Entregable = CER + PMCF, actualizado
  periódicamente.

### EUDAMED + UDI
- **Ítems:** SRN del agente económico; Basic UDI-DI y UDI-DI del producto; UDI en
  la pantalla "Acerca de"; registro del producto; procedimiento para emitir nueva
  UDI-DI ante cambios sustanciales.
- **Evidencia:** cadena "version"/"build" en el código; pantalla *About*;
  documentación de release.
- **Cómo se gestiona:** alta en **EUDAMED** (módulos Actores y UDI/Productos,
  obligatorios — verificar calendario vigente en el paso 5) + registro **AEMPS**.
  Emisor de UDI (GS1, HIBCC, ICCBBA). Entregable = registros EUDAMED + etiqueta
  UDI. Hito = antes de comercializar.

### PMS / Vigilancia (Anexo III MDR)
- **Ítems:** plan de PMS; sistema de recogida y análisis de datos
  poscomercialización; PMS report (clase I) o **PSUR** (IIa/IIb/III);
  procedimiento de notificación de incidentes graves y FSCA; canal de
  reclamaciones.
- **Evidencia:** `SECURITY.md` con contacto de vigilancia; sistema de tickets;
  telemetría de errores (`findings.third_party.crash_repo`).
- **Cómo se gestiona:** proceso interno permanente. Organismo = **AEMPS** (portal
  **NotificaPS**, plazos del art. 87 según gravedad); el ON supervisa el sistema
  PMS en auditorías de seguimiento. Entregable = plan PMS + PSUR + FSN cuando
  proceda.

### RGPD (UE) 2016/679 + LOPDGDD
Ver `references/rgpd-datos.md` para el detalle. Ítems clave para el veredicto:
base jurídica art. 6 + art. 9 definida; **EIPD/DPIA** hecha si es exigible; RAT;
contratos de encargado (art. 28) con todos los proveedores que tratan datos;
análisis de transferencias internacionales; medidas del art. 32 (cifrado,
control de acceso, registro de accesos); procedimiento de brechas; DPO si procede;
información en capas y canal de derechos.
- **Evidencia (visible en repo):** `findings.pii`, `findings.special_category`,
  `findings.logging_pii`, `findings.third_party`, `findings.security`,
  `findings.privacy_controls`. Presencia de política de privacidad, endpoints de
  borrado/exportación, seudonimización, cifrado.
- **Cómo se gestiona:** cumplimiento interno bajo responsabilidad proactiva
  (*accountability*). Organismo = **AEPD** (consulta previa art. 36 solo si el
  DPIA da riesgo alto no mitigable; inspección y sanción; directrices de apps de
  salud — verificar versión vigente en el paso 5). Entregable = RAT + DPIA +
  contratos + registro de brechas.

### AI Act (UE) 2024/1689
Ver `references/ia-aiact.md`. Ítems: clasificación de riesgo justificada (art.
6.1 vía MDR); obligaciones arts. 8-17 (gestión de riesgos de IA, gobernanza de
datos, doc. técnica Anexo IV, logging art. 12, transparencia art. 13, supervisión
humana art. 14, exactitud/robustez/ciberseguridad art. 15, SGC art. 17);
vigilancia poscomercialización de IA (art. 72) e incidentes (art. 73); registro
UE; designación AI Act del organismo notificado.
- **Evidencia (repo):** `findings.ai_ml.*` — `explicabilidad` (SHAP/LIME/GradCAM)
  a favor de art. 13/14; `dataset_sesgo` a favor de art. 10/15; `entrenamiento` +
  `special_category` → gobernanza de datos con base jurídica; logging estructurado
  → art. 12; `model_files` en repo → riesgo de memorización de datos personales.
- **Cómo se gestiona:** evaluación de conformidad **integrada en la del MDR**
  (art. 43.3 AI Act), sin doble certificación, pero el **organismo notificado
  debe tener designación específica para el AI Act**. Autoridad de vigilancia en
  España = **AESIA**, coordinada con AEMPS. Entregable = documentación técnica
  ampliada + registro. Hito = fecha de exigibilidad **verificada por web** (muy
  volátil).

### Horizontales condicionales
- **Cyber Resilience Act (UE) 2024/2847:** solo relevante para componentes que
  **no** califican como PS (fuera del MDR). Veredicto normalmente "No aplica" para
  el producto sanitario; señalar si hay un componente separable.
- **NIS2 (UE) 2022/2555:** nivel organización, no producto. Aplica si el
  fabricante/operador es entidad esencial o importante del sector salud por
  tamaño. Gestión = medidas de gestión de riesgos + notificación de incidentes a
  **CCN-CERT / INCIBE-CERT** / futuro Centro Nacional de Ciberseguridad. Estado de
  la transposición española = **verificar en el paso 5**.
- **ISO/IEC 27001 (+ 27799):** recomendada; se gestiona con certificación por
  entidad acreditada; a menudo exigida contractualmente por hospitales.

---

## Formato de salida del paso 6 (para la sección 5 del informe)

| Norma | Obligatoriedad | Veredicto | Evidencia (`fichero:línea` o "no encontrado") | Brecha concreta | Cómo se gestiona (proceso · organismo · entregable · hito) | Fuente verificada (URL · fecha) |
|---|---|---|---|---|---|---|

Y una frase de cierre por norma: *"Para pasar a Cumple: …"*.
