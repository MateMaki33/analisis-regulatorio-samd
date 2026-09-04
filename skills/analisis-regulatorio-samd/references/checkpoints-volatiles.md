# Contraste en internet — qué verificar antes de concluir

El estado normativo de producto sanitario e IA cambia con frecuencia (fechas de
aplicación, revisiones de guías MDCG, lista de normas armonizadas en el DOUE,
transposiciones nacionales, tasas). El paso 5 de la skill **debe contrastar** los
puntos aplicables de esta lista.

## Reglas del contraste

- **Una búsqueda por punto.** No más de ~10 búsquedas en total.
- **Fuentes por orden de preferencia:** EUR-Lex, DOUE/BOE, AEMPS
  (`aemps.gob.es`), Comisión Europea (`health.ec.europa.eu`), AEPD (`aepd.es`),
  CCN-CNI / INCIBE, AESIA. Consultoras solo como pista, nunca como única fuente.
- **Anota siempre:** dato encontrado · URL · fecha de consulta.
- Si no hay nada más reciente y fiable que el "último dato conocido": úsalo y
  escribe en el informe *"sin cambios verificados a {fecha}"*.

## Puntos a verificar (elige los aplicables al producto)

| # | Aplica si… | Qué verificar | Búsqueda sugerida | Último dato conocido (sep-2026) |
|---|---|---|---|---|
| 1 | Siempre (PS) | **Lista de normas armonizadas del MDR** publicada en el DOUE (qué ediciones dan presunción de conformidad) | `harmonised standards MDR 2017/745 Official Journal implementing decision` | Decisión de Ejecución (UE) 2021/1182 y sucesivas enmiendas; comprobar la última (p. ej. 2026/193). Ediciones citadas: ISO 13485:2016, ISO 14971:2019, IEC 62304:2006+A1, IEC 62366-1:2015+A1, IEC 81001-5-1:2021. |
| 2 | Siempre (PS) | **Guías MDCG** nuevas o revisadas sobre software, clasificación, ciberseguridad, evaluación clínica | `MDCG guidance software medical device latest revision 2026` | Vigentes: MDCG 2019-11 Rev.1, 2021-24 Rev.1, 2019-16 Rev.1, 2020-1. Comprobar revisiones. |
| 3 | Siempre (PS) | **EUDAMED — obligatoriedad de módulos** | `EUDAMED mandatory modules date Regulation 2024/1860` | 4 módulos obligatorios desde **28-may-2026** (Actores, UDI/Productos, ON/Certificados, Vigilancia del mercado). Prórroga registro UDI/DEV a 28-nov-2026 para productos ya en mercado. Módulo de investigaciones clínicas aún voluntario. |
| 4 | Clase IIa+ | **Revisión selectiva MDR/IVDR** (reclasificaciones, cargas) | `MDR IVDR targeted revision Commission proposal reclassification 2026 2027` | Propuesta de la Comisión de 16-dic-2025. No adoptada; no antes de Q2-2027. Tratar como incertidumbre, no aplicar. |
| 5 | Clase IIa+ | **Organismo notificado: tasas y plazos** (CNCps u otro) | `CNCps organismo notificado productos sanitarios tasas plazos` o `[nombre del ON] fees medical device software` | Tasas CNCps orientativas ~22.000–27.000 €; proyecto total ~200.000–800.000 € (cifras de mercado, no oficiales). |
| 6 | Usa IA/ML | **Calendario AI Act para productos sanitarios** (vía art. 6.1) y estado del *Digital Omnibus* | `AI Act medical devices high-risk application date Digital Omnibus 2027 2028` | Aplicación general 2-ago-2026; alto riesgo del Anexo I (PS) **diferido**: referencias del sector a 2-ago-2027 (IIb/III) / 2-ago-2028 (IA embebida). No cerrado. |
| 7 | Usa IA/ML | **Estándares armonizados de IA** (CEN-CENELEC JTC 21) y **ley nacional española de IA / AESIA** | `AI Act harmonised standards JTC 21 status` + `AESIA ley IA España estado` | Estándares en desarrollo; su disponibilidad condiciona la exigibilidad efectiva. Ley nacional de IA en tramitación. |
| 8 | Trata datos personales | **Directrices AEPD vigentes** para apps de salud/bienestar y derechos en sanidad; novedades RGPD (p. ej. Reglamento de procedimiento) | `AEPD directrices apps salud bienestar` + `AEPD guía derechos pacientes sanidad` | Directrices AEPD para apps móviles de salud/bienestar y guía de derechos en sanidad publicadas; comprobar actualizaciones. |
| 9 | Organización = entidad de salud esencial/importante | **NIS2 — transposición en España** | `NIS2 España Ley Coordinación Gobernanza Ciberseguridad BOE estado` | Anteproyecto aprobado en Consejo de Ministros 14-ene-2025; en tramitación; **no publicado en BOE** a mediados de 2026; procedimiento de infracción de la Comisión en curso. |
| 10 | Historia clínica / consentimiento | **Ley 41/2002 y normativa autonómica** de historia clínica | `Ley 41/2002 historia clínica modificación` | Vigente; comprobar desarrollos autonómicos aplicables al despliegue. |
| 11 | Datos salen fuera del EEE (regiones no UE, proxies, CDNs, APIs de IA) | **Decisiones de adecuación vigentes** + **estado del EU-US Data Privacy Framework** (recursos judiciales, revisiones periódicas) | `European Commission adequacy decisions list` + `EU-US Data Privacy Framework status legal challenge 2026` | A sep-2026: adecuación para Andorra, Argentina, Canadá (comercial), Feroe, Guernsey, Israel, Isla de Man, Japón, Jersey, Nueva Zelanda, Corea, Suiza, Reino Unido, Uruguay; EE. UU. **solo vía DPF** (Decisión 10-jul-2023), pendiente del recurso *Latombe* ante el TGUE. Comprobar si el proveedor concreto está en `dataprivacyframework.gov`. |
| 12 | MDSW conectado, o hay componente que no es PS | **SBOM y gestión de vulnerabilidades**: revisión de MDCG 2019-16, calendario del **Cyber Resilience Act** | `MDCG 2019-16 revision cybersecurity SBOM` + `Cyber Resilience Act application dates SBOM vulnerability reporting` | CRA (UE) 2024/2847 en vigor 10-dic-2024; notificación de vulnerabilidades explotadas activamente desde **11-sep-2026**; resto de obligaciones desde **11-dic-2027**. MDCG 2019-16 Rev.1 vigente; comprobar revisiones. |
| 13 | El software califica como IVD (IVDR, no MDR) | **Normas armonizadas IVDR** y revisiones de MDCG 2020-16 | `harmonised standards IVDR 2017/746 Official Journal` + `MDCG 2020-16 classification IVDR revision` | MDCG 2020-16 rev.4 (marzo 2025) vigente; comprobar revisión posterior y lista de normas armonizadas IVDR en el DOUE. |
| 14 | El software trata categorías prioritarias de datos de salud (posible sistema EHR) | **Calendario de aplicación del EHDS** (actos de ejecución sobre EEHRxF y componentes armonizados) y **autoridad española** de vigilancia de sistemas EHR / organismo de acceso a datos de salud | `EHDS Regulation 2025/327 implementing acts EEHRxF timeline` + `EHDS España autoridad competente designación historia clínica electrónica` | Reglamento (UE) 2025/327 en vigor 2025; componentes armonizados obligatorios desde **principios de 2029** (1er grupo de categorías) y **principios de 2031** (2º grupo) — sujeto a actos de ejecución aún no cerrados. Designación de autoridades españolas: **no consolidada** a la fecha de referencia — verificar. |

## Cómo reflejarlo en el informe

Cada fila de la tabla de cumplimiento (sección 5) lleva una columna
**"Fuente verificada (URL · fecha)"**. Si un punto no se verificó, escribir
*"no verificado — dato incorporado sep-2026"* en esa celda. En el encabezado del
informe, listar los puntos consultados y la fecha del contraste.
