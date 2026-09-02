# Mapa normativo y organismos

Para cada norma: **qué es**, **obligatoriedad**, **qué implica en la práctica**,
**ante qué organismo / cómo se acredita**, **cuándo interviene**.

Convención de obligatoriedad:
- **OBLIGATORIA**: exigible por ley directamente aplicable.
- **DE FACTO**: norma voluntaria, pero sin ella no hay certificación (presunción
  de conformidad).
- **CONDICIONAL**: obliga solo si se da el supuesto (IA, tamaño de entidad, etc.).
- **RECOMENDADA**: buena práctica / exigida por clientes (hospitales, aseguradoras).

---

## 1. Núcleo — producto sanitario

### Reglamento (UE) 2017/745 (MDR) — OBLIGAToria (toda clase)
- **Qué es:** norma matriz de productos sanitarios en la UE, directamente
  aplicable desde 26-may-2021. Define: definición de PS, reglas de clasificación
  (Anexo VIII), Requisitos Generales de Seguridad y Funcionamiento (RGSF, Anexo I),
  documentación técnica (Anexos II–III), procedimientos de evaluación de
  conformidad (Anexos IX–XI), obligaciones de agentes económicos, vigilancia.
- **Implica:** finalidad prevista documentada; clasificación justificada;
  cumplimiento de los RGSF del Anexo I (incluye punto 17: ciberseguridad);
  expediente técnico; SGC; evaluación clínica; declaración UE de conformidad;
  marcado CE; persona responsable del cumplimiento (art. 15, "PRRC").
- **Organismo:** para clase I → **autocertificación** (el fabricante declara).
  Para **IIa/IIb/III → organismo notificado** (en España, CNCps nº 0318; vale
  cualquiera de la UE). Autoridad competente nacional: **AEMPS**.
- **Cuándo:** desde el diseño; el marcado CE es requisito previo a comercializar.

### Real Decreto 192/2023 — OBLIGATORIA (España)
- **Qué es:** desarrollo nacional del MDR (21-mar-2023).
- **Implica:** régimen sancionador; registros ante AEMPS; **requisitos de idioma**
  (información al usuario y etiquetado en español para producto puesto en el
  mercado español); reglas de fabricación *in house* y a medida; venta a
  distancia y **publicidad** de productos sanitarios; figura del **responsable
  técnico** con titulación universitaria superior.
- **Organismo:** AEMPS (y comunidades autónomas en inspección/publicidad).

### Guías MDCG — referencia obligada (no vinculantes pero aplicadas)
- **MDCG 2019-11 Rev.1**: calificación y clasificación de software. (paso 3–4)
- **MDCG 2021-24 Rev.1**: clasificación, incl. función de medición.
- **MDCG 2019-16 Rev.1**: ciberseguridad de productos sanitarios.
- **MDCG 2020-1**: evaluación clínica / de funcionamiento de MDSW.
- **MDCG 2020-3 Rev.1**: cambios significativos (art. 120 MDR).
- **MDCG 2020-5**: evidencia por equivalencia.
- **MDCG 2018-1 / 2019-5**: UDI y Basic UDI-DI para software.
- **Organismo:** las aplican organismos notificados y AEMPS. No se "presentan":
  se siguen y se documenta la conformidad con su criterio.

---

## 2. Normas armonizadas (UNE-EN en España) — DE FACTO para clase IIa+

Cumplirlas da **presunción de conformidad** con los RGSF. Ver detalle de cada una
en `requisitos-tecnicos.md`.

| Norma | Cubre | Obligatoriedad | Se acredita ante |
|---|---|---|---|
| ISO 13485:2016 | Sistema de gestión de calidad de PS | DE FACTO (IIa+); RECOMENDADA (I) | Organismo notificado (auditoría de certificación) |
| ISO 14971:2019 (+ ISO/TR 24971) | Gestión de riesgos | DE FACTO (toda clase con riesgo) | Organismo notificado (revisa el *risk management file*) |
| IEC 62304:2006+A1:2015 | Ciclo de vida del software | DE FACTO (todo MDSW) | Organismo notificado (revisa documentación de proceso) |
| IEC 62366-1:2015+A1:2020 | Ingeniería de usabilidad | DE FACTO (MDSW con interfaz de usuario) | Organismo notificado (revisa *usability engineering file*) |
| IEC 81001-5-1:2021 | Ciberseguridad en el ciclo de vida | DE FACTO (MDSW conectado / con datos) | Organismo notificado |
| IEC 82304-1:2016 | Seguridad de "health software" de producto | CONDICIONAL (software de salud independiente) | — / organismo notificado si es PS |
| ISO 20417:2021 | Información suministrada por el fabricante | DE FACTO (etiquetado / IFU) | Organismo notificado |

Para **clase I** por autocertificación: 14971 y 62304 siguen siendo el estándar
esperado; 13485 no es obligatorio pero sí muy recomendable.

---

## 3. Evaluación clínica — OBLIGATORIA (toda clase)

- **Qué es:** demostración de que el producto alcanza su finalidad prevista con
  seguridad y beneficio clínico. Para software, tres pilares (MDCG 2020-1):
  **validez científica** (la asociación clínica es válida), **validación
  analítica/técnica** (el software procesa bien las entradas y produce la salida
  correcta), **validación clínica** (rendimiento en la población y uso previstos).
- **Implica:** Plan de Evaluación Clínica (CEP), búsqueda y valoración de
  literatura, posible investigación clínica propia, Informe de Evaluación Clínica
  (CER), y su actualización periódica con datos poscomercialización (PMCF).
  Metodología: MEDDEV 2.7/1 Rev.4 sigue usándose como referencia.
- **Organismo:** el organismo notificado revisa el CER (IIa+). Investigaciones
  clínicas: autorización/notificación a **AEMPS** + dictamen de **CEIm** (comité
  de ética). Clase III y algunos IIb: posible consulta a panel de expertos UE
  (procedimiento de escrutinio, *CECP*).

---

## 4. Registro y trazabilidad

### EUDAMED + UDI — OBLIGATORIO (calendario en curso)
- **Qué es:** base de datos europea. Registro de **agentes económicos** (SRN), de
  **productos** (Basic UDI-DI / UDI-DI) y de **certificados**; módulos de
  vigilancia y de vigilancia del mercado.
- **Estado (sep-2026):** 4 módulos obligatorios desde **28-may-2026** (Actores;
  UDI/Productos; Organismos Notificados y Certificados; Vigilancia del mercado),
  por el Reglamento (UE) 2024/1860. Módulo de investigaciones clínicas aún
  voluntario. Prórroga de registro UDI/DEV hasta 28-nov-2026 para productos ya en
  el mercado antes de 28-may-2026. **Verificar calendario vigente** (checkpoints).
- **Software:** asignación de UDI-DI; nueva UDI-DI ante cambios que alteren
  identificación/seguridad/finalidad; UDI en pantalla "Acerca de" (no en unidad
  física). Reglas: MDCG 2018-1.
- **Organismo:** EUDAMED (Comisión) + AEMPS.

### Registros AEMPS (España)
- **Licencia previa de funcionamiento**: si hay fabricación/importación/
  esterilización en España.
- **Registro de Comercialización (CCPS)**: productos clase IIa, IIb, III.
- **Registro de Responsables**: productos clase I y a medida.
- **Responsable técnico** titulado, designado por el fabricante.

---

## 5. Vigilancia poscomercialización — OBLIGATORIA (toda clase)

- **Plan de PMS** (Anexo III MDR), proporcional a la clase.
- **Informe:** *PMS report* (clase I) o **PSUR** (IIa/IIb/III), con frecuencia de
  actualización creciente según la clase.
- **PMCF**: seguimiento clínico poscomercialización, alimenta el CER.
- **Notificación de incidentes graves y FSCA** a la AEMPS (art. 87 MDR), plazos
  breves diferenciados por gravedad. Portal **NotificaPS**. Avisos de seguridad
  (FSN) a usuarios.
- **Organismo:** AEMPS; el organismo notificado supervisa el sistema PMS en
  auditorías de seguimiento.

---

## 6. Normativa horizontal (se aplica EN PARALELO al MDR)

### RGPD (UE 2016/679) + LOPDGDD (LO 3/2018) — OBLIGATORIA si hay datos personales
Detalle y detección de vulnerabilidades en `rgpd-datos.md`. Entregables y su
obligatoriedad (calificación, análisis de riesgos, DPIA, RAT, DPA, brechas, TIA,
transparencia de IA, DPO) en `entregables-datos-y-seguridad.md`. Transferencias
fuera del EEE (regiones cloud, proxies, CDNs, APIs de IA) en
`transferencias-internacionales.md`.
- **Implica (datos de salud = art. 9):** base jurídica del art. 6 + levantamiento
  de la prohibición del art. 9 (normalmente 9.2.a consentimiento explícito o
  9.2.h asistencia sanitaria por profesional sujeto a secreto); **EIPD/DPIA**
  (art. 35) casi siempre exigible; Registro de Actividades de Tratamiento;
  contratos de encargado (art. 28); análisis de transferencias internacionales;
  privacidad desde el diseño y por defecto (art. 25); brechas (art. 33-34);
  **DPO** si hay tratamiento a gran escala de categorías especiales (art. 37.1.c).
- **Organismo:** **AEPD** (autoridad de control; consulta previa art. 36 si el
  DPIA arroja riesgo alto no mitigable). Autoridades autonómicas donde apliquen.

### Ley 41/2002 (autonomía del paciente) — CONDICIONAL
Aplica si el software gestiona **historia clínica**, apoya decisiones clínicas o
recaba **consentimiento informado**: derechos de información asistencial, régimen
del consentimiento, conservación y acceso a la documentación clínica.

### Reglamento (UE) 2024/1689 (AI Act) — CONDICIONAL (si hay IA/ML)
Detalle y calendario en `ia-aiact.md`. Resumen: un sistema de IA que además es PS
sujeto a evaluación por organismo notificado (típicamente IIa+) es **alto riesgo**
por el art. 6.1 → obligaciones de gestión de riesgos de IA, gobernanza de datos,
documentación y logging, transparencia, supervisión humana, exactitud/robustez/
ciberseguridad. La evaluación de conformidad de IA se **integra** en la del MDR
(el organismo notificado debe tener designación también para IA).
- **Organismo:** organismo notificado (integrado con MDR) + autoridad nacional de
  vigilancia de IA (en España se articula en torno a **AESIA**) + AI Office (UE).

### Reglamento (UE) 2024/2847 (Cyber Resilience Act) — CONDICIONAL
Productos con elementos digitales. Los PS ya cubiertos por los requisitos de
ciberseguridad del MDR quedan, en principio, **fuera** del alcance directo para
evitar duplicidad. Revisar si algún componente NO califica como PS (queda fuera
del MDR y podría caer bajo el CRA): en ese caso, **SBOM y gestión de
vulnerabilidades pasan a ser obligación legal** (no solo de facto), con
notificación de vulnerabilidades explotadas activamente a ENISA/CSIRT. Fechas de
aplicación escalonadas hasta **11-dic-2027** (verificar — checkpoint 12). Detalle
en `sbom-vulnerabilidades.md`.

### Directiva (UE) 2022/2555 (NIS2) — CONDICIONAL (nivel organización, no producto)
Obliga a **entidades esenciales/importantes** del sector salud (según tamaño y
criticidad) a: medidas de gestión de riesgos de ciberseguridad, notificación
escalonada de incidentes, responsabilidad de la dirección.
- **Estado España (sep-2026):** anteproyecto de Ley de Coordinación y Gobernanza
  de la Ciberseguridad aprobado en Consejo de Ministros (14-ene-2025), aún en
  tramitación, **no publicado en BOE**; procedimiento de infracción de la Comisión
  en curso. **Verificar estado** (checkpoints).
- **Organismo:** CCN-CERT / INCIBE-CERT / futuro Centro Nacional de
  Ciberseguridad; autoridades sectoriales.

### ISO/IEC 27001 (+ ISO 27799 para salud) — RECOMENDADA
SGSI de alcance organizativo. No obligatoria por ley, pero habitualmente exigida
por hospitales y aseguradoras en contratación, y facilita el cumplimiento de
NIS2 y de las medidas de seguridad del RGPD.

---

## 7. Organismos — quién es quién

| Organismo | Rol | Interviene en |
|---|---|---|
| **AEMPS** | Autoridad competente de PS en España | Registros, licencias, vigilancia, incidentes (NotificaPS), inspección, investigaciones clínicas |
| **CNCps (Centro Nacional de Certificación de PS), nº 0318** | Único organismo notificado español | Evaluación de conformidad IIa/IIb/III: evaluación preliminar → admisión → evaluación de doc. técnica → auditoría del SGC → certificado (≤ 5 años). Documentación en español |
| **Organismo notificado (cualquiera UE)** | Evaluación de conformidad | Alternativa al CNCps; para IA debe tener designación específica |
| **AEPD** | Autoridad de control de protección de datos | DPIA de alto riesgo (consulta previa), inspección, sanción, directrices de apps de salud |
| **CEIm** | Comité de ética de la investigación con medicamentos | Dictamen de investigaciones clínicas |
| **Comisión Europea / EUDAMED** | Gestión de la base de datos y guías MDCG | Registro UE, SRN, UDI, certificados |
| **AESIA** | Agencia Española de Supervisión de la IA | Vigilancia del AI Act en España |
| **CCN-CNI / INCIBE** | Ciberseguridad nacional | NIS2, notificación de incidentes de ciberseguridad, esquemas de certificación |
| **Panel de expertos UE (MDCG/Comisión)** | Escrutinio clínico (CECP) | Determinados productos IIb y clase III |

### Coste orientativo de certificación (clase IIa–III)
Cifras de mercado citadas por consultoras (no tarifas oficiales; confirmar con
CNCps): **tasas CNCps ~22.000–27.000 €**; **coste total de proyecto ~200.000–
800.000 €** (documentación técnica, consultoría, ensayos, SGC, evaluación
clínica). Clase I: coste dominado por documentación interna y SGC.
