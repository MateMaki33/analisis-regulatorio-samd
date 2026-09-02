# RGPD / LOPDGDD y detección de vulnerabilidades de datos

Objetivo del paso: (a) mapear las obligaciones de protección de datos que aplican
al proyecto y (b) producir una **lista de vulnerabilidades concretas** con
`fichero:línea` a partir del JSON del escáner.

---

## A. ¿Qué régimen aplica?

1. **¿Hay datos personales?** (`signals.trata_pii` o `findings.pii`). Si no → RGPD
   no aplica; revisar solo si hay datos que puedan reidentificar.
2. **¿Categorías especiales (art. 9 RGPD)?** (`signals.categorias_especiales_rgpd`,
   `findings.special_category`). Datos de **salud**, genéticos, biométricos de
   identificación, vida/orientación sexual, origen étnico, opiniones, creencias,
   afiliación sindical. Un software sanitario casi siempre trata datos de salud →
   régimen reforzado.
3. **LOPDGDD (LO 3/2018):** desarrollo español. Relevante para: consentimiento de
   **menores** (14 años en España), tratamiento con fines de **investigación en
   salud** (Disp. Adic. 17ª), videovigilancia, y el régimen sancionador nacional.

---

## B. Obligaciones cuando se tratan datos de salud

| Obligación | Qué implica | Artículo |
|---|---|---|
| **Base jurídica doble** | Base del art. 6 (normalmente 6.1.a consentimiento, 6.1.b contrato, 6.1.e misión de interés público en sanidad pública) **+** excepción del art. 9.2: típicamente **9.2.a** (consentimiento explícito) o **9.2.h** (asistencia sanitaria por profesional sujeto a secreto, con contrato/norma de por medio) | 6, 9 |
| **EIPD / DPIA** | Evaluación de impacto **previa**. Obligatoria en tratamiento a gran escala de categorías especiales, observación sistemática, o uso de tecnologías innovadoras (IA). En apps de salud con pacientes: casi siempre exigible. Si el riesgo residual es alto → **consulta previa a la AEPD** (art. 36) | 35, 36 |
| **RAT** | Registro de Actividades de Tratamiento documentado | 30 |
| **Encargados del tratamiento** | Contrato del art. 28 con todo proveedor que trate datos por cuenta del responsable (hosting, analítica, IA como servicio, soporte). `findings.third_party` y `findings.security.nube_datos` marcan candidatos | 28 |
| **Transferencias internacionales** | Si hay proveedores fuera del EEE (nube US, APIs de IA): mecanismo del cap. V (decisión de adecuación, CCT + *Transfer Impact Assessment*, BCR) | 44-49 |
| **Privacidad desde el diseño y por defecto** | Minimización, seudonimización temprana, cifrado, control de acceso por rol, retención limitada y borrado, no recoger campos no necesarios | 25 |
| **Seguridad del tratamiento** | Medidas técnicas y organizativas apropiadas: cifrado en tránsito y reposo, control de acceso, registro de accesos, copias, pruebas periódicas | 32 |
| **Notificación de brechas** | A la AEPD en 72 h; a los interesados si alto riesgo | 33, 34 |
| **DPO** | Obligatorio si el tratamiento a gran escala de categorías especiales es actividad principal | 37-39 |
| **Información y derechos** | Cláusulas informativas en capas; canal para acceso, rectificación, supresión, oposición, portabilidad, limitación | 12-22 |
| **Menores** | Consentimiento a partir de 14 años (España); si no, de titulares de la patria potestad | LOPDGDD 7 |
| **Investigación en salud** | Reutilización de datos para investigación biomédica bajo garantías (seudonimización, comité de ética, información) | LOPDGDD DA 17ª |

**Ley 41/2002** (si hay historia clínica / consentimiento informado): derechos de
información asistencial, formato y contenido del consentimiento, plazos de
conservación de la documentación clínica (mínimo 5 años desde el alta de cada
proceso), acceso del paciente a su historia.

**Directrices AEPD aplicables:** "Directrices para apps móviles educativas, de
actividad física, bienestar y salud" y "Guía de derechos de protección de datos
de pacientes y usuarios de la sanidad".

---

## C. Catálogo de vulnerabilidades → cómo reportarlas

Recorre el JSON del escáner y clasifica cada hallazgo. Para cada uno reporta:
`categoría · fichero:línea · extracto · riesgo · norma afectada · remediación`.

### C.1 Datos sensibles expuestos / mal tratados
| Señal escáner | Vulnerabilidad | Riesgo | Norma |
|---|---|---|---|
| `logging_pii.log_datos` | PII / datos de salud / credenciales escritos en logs | Persistencia no controlada, acceso indebido, retención | RGPD 5.1.f, 32; IEC 81001-5-1 |
| `special_category.*` en ficheros de test/seed/fixtures | Datos reales de salud en datos de prueba o en el repo | Exposición en control de versiones | RGPD 5, 32; 25 |
| `pii.*` en respuestas de API sin filtrado / campos de más | Sobreexposición, incumple minimización | RGPD 5.1.c, 25 | 
| Ausencia de `privacy_controls.*` en todo el repo | Sin evidencia de consentimiento, política de privacidad, borrado o seudonimización | RGPD 7, 13-14, 17, 25 |

### C.2 Seguridad (también alimentan ISO 14971 + IEC 81001-5-1)
| Señal escáner | Vulnerabilidad | Norma |
|---|---|---|
| `security.secreto_hardcoded`, `security.aws_key`, `security.clave_privada`, `security.jwt_literal` | Secretos/credenciales en el código o en el repo | RGPD 32; IEC 81001-5-1; buenas prácticas OWASP |
| `security.tls_desactivado`, `security.http_inseguro` | Datos (posiblemente de salud) en claro por la red | RGPD 32; MDR Anexo I.17 |
| `security.hash_debil` | MD5/SHA-1 para contraseñas o integridad | RGPD 32 |
| `security.sql_concat` | Inyección SQL → acceso masivo a datos de pacientes | RGPD 32; ISO 14971 (peligro) |
| `security.eval_dinamico` | Ejecución de código / RCE | IEC 81001-5-1 |
| Ausencia de `security.cifrado_reposo` con datos de salud persistidos | Sin cifrado en reposo | RGPD 32; MDCG 2019-16 |

### C.3 Terceros y transferencias
| Señal escáner | Vulnerabilidad | Norma |
|---|---|---|
| `third_party.analitica`, `third_party.crash_repo`, `third_party.publicidad` | SDKs que exfiltran datos de uso/dispositivo; en apps de salud el `analitica`+`publicidad` suele ser incompatible con art. 9 | RGPD 6, 9, 28, 44; Directrices AEPD apps de salud |
| `third_party.nube_datos` / endpoints fuera del EEE | Encargado sin contrato art. 28 / transferencia internacional sin garantías | RGPD 28, 44-49 |
| `ai_ml.llm_apis` (OpenAI/Anthropic/etc.) tratando datos de paciente | Comunicación de datos de salud a un tercero, posible transferencia internacional y uso para entrenamiento | RGPD 9, 28, 44; AI Act |

### C.4 IA y datos
- `ai_ml.entrenamiento` + `special_category.*` → gobernanza de datos de
  entrenamiento (AI Act art. 10): representatividad, sesgos, calidad, base
  jurídica para usar datos de pacientes en entrenamiento (a menudo requiere
  anonimización real o consentimiento/DA 17ª LOPDGDD).
- `model_files` en el repo → ¿el modelo memoriza datos personales? Riesgo de
  inferencia/extracción. Evaluar.

---

## D. Salida esperada del paso

1. **Tabla de bases jurídicas** propuestas (art. 6 + art. 9) para cada finalidad.
2. **Checklist de obligaciones** con estado: cubierto / parcial / ausente / no sé.
3. **Lista priorizada de vulnerabilidades** (crítica / alta / media) con
   `fichero:línea` y remediación concreta.
4. **DPIA: ¿exigible?** (sí/no + por qué) y si procede consulta previa a la AEPD.
5. Nota sobre **DPO** (¿obligatorio?) y sobre **transferencias internacionales**.
