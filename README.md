# analisis-regulatorio-samd

Skill de [Claude Code](https://claude.com/claude-code) que analiza un proyecto de
software y lo sitúa frente a la normativa de **producto sanitario** (SaMD / MDSW,
incluido diagnóstico in vitro) y de **historia clínica electrónica** en España y
la UE: calificación (MDCG 2019-11) con enrutado **MDR vs. IVDR**, clasificación
de riesgo (Regla 11 MDR o Reglas 1-7 IVDR), clase IEC 62304, mapa normativo con
contraste en fuentes oficiales, veredicto de cumplimiento norma por norma,
vulnerabilidades RGPD y ruta a marcado CE. Dice además **qué entregables de
datos y seguridad debe generar el proyecto y qué es cada uno** (análisis de
calificación como "no producto sanitario", análisis de riesgos del tratamiento,
DPIA/EIPD, RAT, DPA/contratos de encargado, procedimiento de brechas, TIA, nota
de transparencia sobre uso de IA, calificación/marcado CE como sistema EHR bajo
el **Espacio Europeo de Datos Sanitarios (EHDS)**, SBOM y gestión de
vulnerabilidades), analiza las **dependencias** y detecta si los **datos salen
del EEE** (regiones cloud no europeas, proxies, CDNs, APIs de IA) y con qué
cobertura del capítulo V del RGPD. Produce un informe de situación en Markdown.

> Documento orientativo de planificación. No sustituye asesoría legal o
> regulatoria. Contenido normativo a fecha **septiembre 2026**.

---

## Requisitos

- **Claude Code** actualizado (las Agent Skills se cargan automáticamente desde
  `~/.claude/skills/` y `.claude/skills/`).
- **Python 3.8+** en el PATH — solo para el escáner `scripts/scan_repo.py`. No
  tiene dependencias externas. Si no hay Python, la skill hace un análisis por
  patrones equivalente, más lento.

---

## Instalación

```bash
npx skills add MateMaki33/analisis-regulatorio-samd
```

El CLI `skills` te pregunta por la terminal qué skill instalar, para qué agente
y si global o en el proyecto. No hay build ni `npm install`.

---

## Uso

En cualquier proyecto que quieras evaluar, pídeselo a Claude Code en lenguaje
natural, por ejemplo:

- *"Evalúa el estado regulatorio de este proyecto como producto sanitario."*
- *"¿Esto es un SaMD? ¿Qué clase MDR y qué me falta para el marcado CE?"*
- *"Revisa el cumplimiento RGPD y las vulnerabilidades de datos de salud."*
- *"Esta app hace una valoración clínica y genera un informe: ¿es producto
  sanitario, de qué clase, necesito organismo notificado y cumplo RGPD?"*

Claude cargará la skill, te preguntará la **finalidad prevista**, ejecutará el
escáner y entregará el informe `informe-regulatorio-samd-AAAA-MM-DD.md` en la
raíz del proyecto analizado.

---

## Estructura

```
skills/analisis-regulatorio-samd/
  SKILL.md                         Orquestación y flujo (lo que Claude lee primero)
  scripts/scan_repo.py             Escáner estático → JSON compacto (Python 3.8+)
  references/
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
  assets/plantilla-informe.md      Plantilla del informe de situación
```

Ver `skills/analisis-regulatorio-samd/README.md` para el detalle de qué hace cada
paso.

---

## Actualizar y desinstalar

```bash
npx skills update analisis-regulatorio-samd
npx skills remove analisis-regulatorio-samd
```

---

## Limitaciones

Documento orientativo de planificación. No sustituye asesoría legal o
regulatoria. La calificación y clasificación vinculantes, y la evaluación de
conformidad, las confirma la autoridad competente (AEMPS) o un organismo
notificado. La normativa de producto sanitario e IA está en evolución activa: la
skill contrasta el estado vigente en fuentes oficiales, pero verifica siempre los
textos en EUR-Lex, BOE y AEMPS.
