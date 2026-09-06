# Requisitos técnicos — qué exige cada norma, cómo se cumple, ante quién

Para cada norma: **en qué consiste**, **entregables**, **cómo se hace / ante qué
organismo**, y **señales de la exploración (paso 2)** que permiten presumir cumplimiento parcial.

---

## ISO 13485:2016 — Sistema de Gestión de la Calidad

- **En qué consiste:** SGC específico de producto sanitario. Procesos: control de
  diseño y desarrollo (7.3), control de documentos y registros, gestión de
  proveedores/compras, producción y prestación del servicio, medición y mejora,
  **CAPA** (acciones correctivas y preventivas), auditorías internas, revisión por
  la dirección, gestión de riesgos transversal.
- **Entregables:** Manual de calidad / listado de procesos, procedimientos
  documentados (SOP), Design History File (DHF), Device Master Record, registros
  de formación, lista de proveedores críticos y sus evaluaciones, plan y registros
  de auditoría interna, actas de revisión por dirección.
- **Cómo / ante quién:** implantación interna; **auditoría de certificación por
  organismo notificado** (obligatoria IIa+). Certificado ISO 13485 válido ~3 años
  con auditorías de seguimiento anuales. Clase I: no obliga certificado pero sí
  tener un SGC equivalente documentado.
- **Escáner:** normalmente no visible en código. Señales indirectas: existencia de
  `CONTRIBUTING`, plantillas de PR/issue, carpeta `docs/qms|sop|quality`, CI/CD
  con gates. Su ausencia total = brecha organizativa a señalar.

---

## ISO 14971:2019 (+ ISO/TR 24971) — Gestión de riesgos

- **En qué consiste:** proceso iterativo durante todo el ciclo de vida:
  1. Plan de gestión de riesgos.
  2. Análisis: identificación de peligros, situaciones peligrosas y secuencias de
     eventos (incluye uso previsto, uso indebido razonablemente previsible,
     características relacionadas con la seguridad, errores de uso, ciberseguridad).
  3. Estimación y evaluación del riesgo (probabilidad × severidad; criterios de
     aceptabilidad definidos a priori).
  4. Control del riesgo: por diseño → por medidas de protección → por información
     de seguridad (en ese orden de prioridad). Verificación de implementación y
     eficacia.
  5. Evaluación del riesgo residual global.
  6. Revisión de la gestión de riesgos antes de la liberación comercial.
  7. Actividades de producción y poscomercialización (retroalimentación).
- **Entregables:** **Risk Management File (RMF)**: plan, matriz/tabla de análisis
  (FMEA o equivalente), trazabilidad peligro→control→verificación, informe de
  gestión de riesgos, evaluación beneficio-riesgo.
- **Cómo / ante quién:** metodología interna; el organismo notificado **audita el
  RMF en detalle** (IIa+). Debe enlazar con IEC 62304 (riesgos de software), IEC
  62366-1 (errores de uso) y MDCG 2019-16 (ciberseguridad).
- **Escáner:** `findings.security.*` y `findings.logging_pii` alimentan la lista
  de peligros de ciberseguridad/privacidad. `signals.usa_ia_ml` → añadir peligros
  de rendimiento del modelo (falsos negativos/positivos, deriva, sesgo).

---

## IEC 62304:2006 + AMD1:2015 — Ciclo de vida del software

- **En qué consiste:** procesos exigidos **según la clase de seguridad A/B/C**
  (ver `calificacion-clasificacion.md`, Parte C):

  | Proceso | A | B | C |
  |---|---|---|---|
  | Plan de desarrollo de software | ✔ | ✔ | ✔ |
  | Análisis de requisitos de software | ✔ | ✔ | ✔ |
  | Diseño arquitectónico | — | ✔ | ✔ |
  | Diseño detallado | — | — | ✔ |
  | Implementación y verificación de unidades | ✔* | ✔ | ✔ |
  | Integración y pruebas de integración | — | ✔ | ✔ |
  | Pruebas de sistema de software | ✔ | ✔ | ✔ |
  | Liberación de software | ✔ | ✔ | ✔ |
  | Gestión de configuración (SCM) | ✔ | ✔ | ✔ |
  | Gestión de problemas (defectos) | ✔ | ✔ | ✔ |
  | Proceso de mantenimiento | ✔ | ✔ | ✔ |
  | Gestión de riesgos de software (enlace ISO 14971) | ✔ | ✔ | ✔ |

  \* En clase A el rigor de verificación de unidad es menor; en B/C se exige
  documentar criterios de aceptación y cobertura.

- **SOUP (Software of Unknown Provenance):** inventariar toda dependencia de
  terceros (nombre, versión, propósito), definir requisitos funcionales y de
  rendimiento que se le exigen, y analizar sus anomalías conocidas
  (CVE/bug trackers) frente a la seguridad del paciente. → **SBOM**. Formatos
  (CycloneDX / SPDX), herramientas de generación y de cribado, VEX y CVD en
  `references/sbom-vulnerabilidades.md`.
- **Entregables:** Plan de desarrollo; especificación de requisitos de software
  (SRS) con trazabilidad a requisitos de sistema y a riesgos; descripción de
  arquitectura (B/C); descripción de diseño detallado (C); registros de revisión
  de código y pruebas unitarias (B/C); plan y resultados de pruebas de integración
  y de sistema; lista SOUP/SBOM; notas de versión y registro de anomalías;
  procedimiento de gestión de configuración y de cambios; plan de mantenimiento.
- **Cómo / ante quién:** se materializa en el **repositorio y el tooling**:
  control de versiones con historia trazable, issues/defectos enlazados a
  commits, requisitos con ID trazables (matriz de trazabilidad), pipeline de
  build reproducible, pruebas automatizadas con informe, versionado semántico y
  changelog. El **organismo notificado revisa la documentación de proceso** y
  muestrea trazabilidad requisito→código→prueba→riesgo.
- **Exploración (paso 2) / `scan_repo.py`:** `languages` (stack), `manifests`
  (dependencias = base del inventario SOUP/SBOM), `model_files`. Comprueba en el repo: ¿hay carpeta de
  tests?, ¿CI?, ¿changelog?, ¿fichero de requisitos? Su ausencia = brechas
  concretas de 62304 a listar por clase.

---

## IEC 62366-1:2015 + AMD1:2020 — Ingeniería de usabilidad

- **En qué consiste:** proceso formal para minimizar **errores de uso** que
  puedan causar daño:
  1. Especificación de uso: usuarios previstos, entorno de uso, contexto clínico,
     parte de la UI relacionada con la seguridad.
  2. Identificación de funciones relacionadas con la seguridad y de posibles
     errores de uso; escenarios de uso peligrosos.
  3. Especificación de requisitos de la interfaz de usuario.
  4. **Evaluación formativa** (iterativa, durante el diseño).
  5. **Evaluación sumativa** (validación con usuarios representativos en
     condiciones realistas; sin errores de uso peligrosos no mitigados).
- **Entregables:** **Usability Engineering File (UEF)**: plan, especificación de
  uso, análisis de errores de uso, protocolo y resultados de evaluación
  formativa y sumativa, trazabilidad a gestión de riesgos.
- **Cómo / ante quién:** estudios con usuarios (n según riesgo, típicamente ≥15
  por grupo en sumativa); el organismo notificado revisa el UEF. Vincular con
  ISO 14971 (errores de uso = peligros) y con la IFU (ISO 20417).
- **Escáner:** poco visible. Señales: presencia de UI (`.tsx/.jsx/.vue/.swift/`
  layouts), textos de alertas/dosis en la UI (`clinical.tratamiento_dosis` en
  ficheros de vista) = superficies críticas de usabilidad a evaluar.

---

## IEC 81001-5-1:2021 — Ciberseguridad en el ciclo de vida (+ MDCG 2019-16 Rev.1)

- **En qué consiste:** actividades de seguridad integradas en el ciclo de vida
  IEC 62304:
  - **Diseño seguro:** requisitos de seguridad, modelado de amenazas (p. ej.
    STRIDE), superficie de ataque mínima, autenticación/autorización, cifrado en
    tránsito y en reposo, gestión de secretos, registro de auditoría, actualización
    segura (firma de artefactos).
  - **Gestión de la cadena de suministro:** SBOM (CycloneDX/SPDX), evaluación de
    componentes de terceros, verificación de integridad, VEX. Detalle,
    herramientas y criterio de obligatoriedad en
    `references/sbom-vulnerabilidades.md`.
  - **Verificación de seguridad:** pruebas estáticas (SAST), análisis de
    composición (SCA), pruebas dinámicas / pentest, gestión de configuración
    endurecida.
  - **Poscomercialización:** vigilancia de vulnerabilidades (CVE) de todos los
    componentes SOUP, proceso de divulgación coordinada (CVD), **gestión y
    despliegue de parches** durante toda la vida del producto, plan de respuesta a
    incidentes.
- **Entregables:** plan de gestión de ciberseguridad; documento de requisitos de
  seguridad; informe de modelado de amenazas y análisis de riesgos de seguridad
  (enlazado a ISO 14971); SBOM; informes SAST/SCA/DAST/pentest; procedimiento de
  gestión de vulnerabilidades y parches; **información de seguridad para el
  usuario** (requisitos de entorno, endurecimiento, gestión de cuentas — MDS2 o
  equivalente).
- **Cómo / ante quién:** interno + auditoría del organismo notificado; el RGSF
  Anexo I punto 17 del MDR lo hace exigible. Coordinar divulgación con
  INCIBE-CERT / CSIRT.
- **Escáner (directo):** `findings.security.*` es la entrada principal —
  `secreto_hardcoded`, `clave_privada`, `aws_key`, `jwt_literal` → gestión de
  secretos deficiente; `hash_debil` → criptografía obsoleta; `tls_desactivado`,
  `http_inseguro` → cifrado en tránsito; `sql_concat`, `eval_dinamico` →
  validación de entrada; `cifrado_reposo` (presencia) → indicio positivo.
  `manifests` → base del SBOM y del cribado de CVE. `findings.third_party` →
  superficie de cadena de suministro.

---

## ISO 20417:2021 — Información suministrada por el fabricante

- **En qué consiste:** contenido mínimo de etiquetado e **instrucciones de uso
  (IFU)**: identificación del fabricante y del producto, UDI, finalidad prevista,
  indicaciones/contraindicaciones, advertencias, requisitos de instalación y
  entorno, versión de software, datos de contacto de vigilancia.
- **España (RD 192/2023):** IFU y etiquetado **en español** para el mercado
  español; posibilidad de IFU electrónica según Reglamento (UE) 2021/2226 para
  ciertos productos y usuarios profesionales.
- **Escáner:** buscar `README`, `docs/`, pantallas "Acerca de"/"Ayuda", textos
  legales. Ausencia de IFU estructurada = brecha.

---

## Matriz rápida "qué necesito según la clase"

| Elemento | Clase I (autocert.) | IIa | IIb | III |
|---|---|---|---|---|
| SGC ISO 13485 certificado | Recomendado | Sí | Sí | Sí |
| RMF ISO 14971 | Sí | Sí | Sí | Sí |
| IEC 62304 nivel | A/B | B | B/C | C |
| UEF IEC 62366-1 | Sí (proporcional) | Sí | Sí | Sí (sumativa robusta) |
| Ciberseguridad IEC 81001-5-1 | Sí (si conectado) | Sí | Sí | Sí |
| Evaluación clínica (CER) | Sí | Sí | Sí + PMCF intenso | Sí + posible CECP |
| Organismo notificado | No | Sí | Sí | Sí (máx. escrutinio) |
| PSUR | PMS report | Sí (periódico) | Sí (más frecuente) | Sí (anual) |
| Registro AEMPS | Responsables | Comercialización | Comercialización | Comercialización |
