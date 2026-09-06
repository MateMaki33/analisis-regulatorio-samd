# analisis-regulatorio-samd

Skill (Agent Skill) para analizar un proyecto de software y situarlo frente a
la normativa de **producto sanitario** (SaMD / MDSW, incluido diagnóstico in
vitro) y de **historia clínica electrónica** (EHDS) en España y la UE. No está
ligada a un agente concreto: sigue el formato estándar de Agent Skills
(`SKILL.md` + `references/` + `scripts/` + `assets/`) y funciona con cualquier
agente de código compatible con ese formato.

## Qué hace

1. Explora el repositorio con lectura completa (no fragmentos): busca por
   categoría (dominio clínico, datos personales y de categoría especial —RGPD
   art. 9—, IA/ML, terceros receptores de datos, vulnerabilidades de
   seguridad, infraestructura y salida de datos del EEE, señales de
   diagnóstico in vitro, señales de historia clínica/EHDS) y **lee entero**
   cada fichero con coincidencias, más siempre entero todo lo que suele
   contener el contexto legal real: README/docs, textos legales
   (`legal/`, `privacy/`, `terms/`), formularios de alta/registro/
   consentimiento/checkout, y configuración de infraestructura. El
   procedimiento (categorías, rutas de lectura obligatoria, límite de 80
   ficheros por hits) está en `references/patrones-busqueda.md`. Aparte,
   `scripts/scan_repo.py` (sin dependencias) inventaría de forma mecánica
   dependencias, lockfiles, SBOM y configuración de SCA/CVD para la sección de
   cadena de suministro.
2. Aplica el test de **calificación** (MDCG 2019-11): ¿es producto sanitario? Si
   lo es, ¿cae bajo el **MDR** (Reglamento (UE) 2017/745) o bajo el **IVDR**
   (Reglamento (UE) 2017/746, diagnóstico in vitro)?
3. **Clasifica** por riesgo: Regla 11 (Anexo VIII MDR) → I / IIa / IIb / III, o
   Reglas 1-7 (Anexo VIII IVDR) → A / B / C / D; asigna la clase de seguridad
   IEC 62304 (A / B / C) y, si es clase I MDR, comprueba los subtipos Is/Im/Ir
   (MDCG 2019-15) que exigen intervención parcial de un organismo notificado.
4. Construye el **mapa normativo**: MDR/IVDR + RD 192/2023, guías MDCG, normas
   armonizadas (13485, 14971, 62304, 62366-1, 81001-5-1), evaluación clínica o
   del funcionamiento, EUDAMED/UDI, PMS, y horizontales (RGPD/LOPDGDD, AI Act,
   EHDS, CRA, NIS2) — con obligatoriedad, implicaciones y organismo para cada una.
5. **Contrasta en internet** (fuentes oficiales: EUR-Lex, DOUE, BOE, AEMPS,
   Comisión, AEPD, CCN, AESIA) el estado vigente de cada norma aplicable: fechas
   de aplicación, edición que da presunción de conformidad, guías MDCG nuevas,
   calendario EUDAMED y AI Act, transposición de NIS2. Búsqueda acotada (~8 máx.),
   con URL y fecha de consulta en el informe.
6. Emite, **norma por norma, un veredicto**: ✅ Cumple / 🟡 Parcial / ❌ No cumple
   / ⬜ No evaluable — con evidencia (`fichero:línea`), brecha concreta y **cómo se
   gestiona** (proceso · organismo · entregable · plazo). Incluye requisitos
   técnicos, RGPD (+ lista de vulnerabilidades) y AI Act.
6b. Determina **qué entregables de datos y seguridad debe generar** el proyecto y
   si son obligatorios (análisis de calificación —incl. "no es PS"—, análisis de
   riesgos del tratamiento, DPIA/EIPD, RAT, DPA/art. 28, procedimiento de brechas,
   TIA, nota de transparencia de IA, DPO, calificación/declaración-marcado CE como
   sistema EHR bajo el EHDS), qué es cada uno y cómo se genera; construye la
   **tabla de flujos de datos** (¿salen del EEE?, mecanismo del cap. V, ¿TIA?); y
   decide si el **SBOM** y la **gestión de vulnerabilidades** son obligatorios,
   con inventario de dependencias y comando de generación.
7. Ordena las brechas en una **ruta a la conformidad** por fases.
8. Redacta un **informe de situación** en Markdown (`assets/plantilla-informe.md`),
   con un **índice de siglas** final (`references/glosario-siglas.md`) que
   explica cada acrónimo usado en el informe, y lo entrega al usuario.

## Estructura

```
SKILL.md                         Orquestación y flujo (lo que Claude lee primero)
scripts/scan_repo.py             Inventario de dependencias/cadena de suministro (paso 6d)
references/
  patrones-busqueda.md           Categorías de búsqueda + rutas de lectura obligatoria (paso 2)
  calificacion-clasificacion.md  Test MDCG 2019-11 (MDR/IVDR) + Regla 11 + clase 62304
  ivdr-diagnostico-in-vitro.md   Calificación y clasificación IVDR (clases A-D)
  ehds-espacio-datos-salud.md    Espacio Europeo de Datos Sanitarios (sistema EHR)
  normativa-y-organismos.md      Todas las normas y quién es cada organismo
  requisitos-tecnicos.md         Qué exige cada norma y cómo se acredita
  evaluacion-cumplimiento.md     Rúbrica: veredicto por norma + cómo se gestiona
  rgpd-datos.md                  Obligaciones RGPD + catálogo de vulnerabilidades
  entregables-datos-y-seguridad.md  Qué documento generar y si es obligatorio
  transferencias-internacionales.md Datos fuera del EEE (Cap. V) + proxies/CDN
  sbom-vulnerabilidades.md       Qué es el SBOM, cuándo obliga, cómo generarlo
  ia-aiact.md                    Reglamento (UE) 2024/1689 para SaMD con IA
  checkpoints-volatiles.md       Lista de contraste web (qué verificar y dónde)
  glosario-siglas.md             Significado de cada sigla/acrónimo usado en el informe
assets/plantilla-informe.md      Plantilla del informe de situación
```

## Eficiencia

- Claude no lee todo el repo a ciegas ni se limita a fragmentos de un JSON: lee
  **entero** cada fichero que puede contener una brecha (formularios,
  consentimiento, textos legales, docs, código con señales relevantes) y
  descarta sin leer lo que es ruido (`node_modules`, `dist`, binarios,
  vendorizado). Ver `references/patrones-busqueda.md`.
- Límite explícito: hasta 80 ficheros de lectura completa por categoría de
  búsqueda (sin límite para README/docs/legal/formularios, que siempre se leen
  enteros); si un repo lo supera, se prioriza por categoría y se declara en el
  informe.
- Cada `references/*.md` se carga solo al llegar a su paso.
- El contraste web es obligatorio pero **acotado**: lista cerrada de consultas
  (`checkpoints-volatiles.md`), una por punto, ~10 máximo, fuentes oficiales, con
  URL y fecha en el informe.

## Limitaciones

Documento orientativo de planificación. No sustituye asesoría legal o regulatoria.
La clasificación vinculante y la evaluación de conformidad las confirma un
organismo notificado. Contenido normativo a fecha **septiembre 2026**.
