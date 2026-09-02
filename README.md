# analisis-regulatorio-samd

Skill de [Claude Code](https://claude.com/claude-code) que analiza un proyecto de
software y lo sitúa frente a la normativa de **producto sanitario** (SaMD / MDSW)
en España y la UE: calificación (MDCG 2019-11), clasificación de riesgo
(Regla 11 MDR), clase IEC 62304, mapa normativo con contraste en fuentes
oficiales, veredicto de cumplimiento norma por norma, vulnerabilidades RGPD y
ruta a marcado CE. Produce un informe de situación en Markdown.

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

Una skill de Claude Code es **una carpeta con un `SKILL.md` dentro**. La forma
recomendada de instalarla es el CLI `skills` (`npx skills`), que descarga la
skill del repo y la enlaza en el directorio de skills del agente. No hay build
ni `npm install`.

### Opción 1 — Skill personal, disponible en todos tus proyectos (recomendada)

```bash
npx skills add matemaki33/analisis-regulatorio-samd \
  --skill analisis-regulatorio-samd --agent claude-code --global
```

Con `--global` la skill queda enlazada en `~/.claude/skills/` y está disponible
en todos tus proyectos. Añade `--yes` para saltarte las confirmaciones.

> `npx skills` acepta el atajo `usuario/repo`, la URL completa de GitHub
> (`https://github.com/matemaki33/analisis-regulatorio-samd`) o cualquier URL
> git. Por defecto crea un symlink a una copia cacheada (fuente única, fácil de
> actualizar); usa `--copy` si prefieres una copia independiente.

### Opción 2 — Skill de un solo proyecto (se versiona con el repo)

Lo mismo sin `--global`: se instala en `.claude/skills/` del proyecto actual.

```bash
npx skills add matemaki33/analisis-regulatorio-samd \
  --skill analisis-regulatorio-samd --agent claude-code
```

Queda disponible solo cuando abres Claude Code en ese proyecto. Si usas `--copy`
puedes commitear la carpeta para el equipo.

### Opción 3 — Copia manual (repo privado, sin red, u offline)

```bash
git clone https://github.com/matemaki33/analisis-regulatorio-samd.git
cp -r analisis-regulatorio-samd/skills/analisis-regulatorio-samd \
  ~/.claude/skills/
```

O descarga el ZIP y copia la carpeta `skills/analisis-regulatorio-samd` dentro
de `~/.claude/skills/`. En Windows (PowerShell):

```powershell
Copy-Item -Recurse .\skills\analisis-regulatorio-samd "$HOME\.claude\skills\"
```

### Comprobar la instalación

La ruta final debe ser:

```
~/.claude/skills/analisis-regulatorio-samd/SKILL.md      (personal)
.claude/skills/analisis-regulatorio-samd/SKILL.md        (proyecto)
```

Comprueba lo instalado con `npx skills list`. Luego abre una sesión nueva de
Claude Code y pídele: *"¿tienes disponible la skill analisis-regulatorio-samd?"*
— debería listarla.

---

## Uso

En cualquier proyecto que quieras evaluar, pídeselo a Claude Code en lenguaje
natural, por ejemplo:

- *"Evalúa el estado regulatorio de este proyecto como producto sanitario."*
- *"¿Esto es un SaMD? ¿Qué clase MDR y qué me falta para el marcado CE?"*
- *"Revisa el cumplimiento RGPD y las vulnerabilidades de datos de salud."*

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
    calificacion-clasificacion.md  Test MDCG 2019-11 + Regla 11 + clase 62304
    normativa-y-organismos.md      Todas las normas y quién es cada organismo
    requisitos-tecnicos.md         Qué exige cada norma y cómo se acredita
    evaluacion-cumplimiento.md     Rúbrica: veredicto por norma + cómo se gestiona
    rgpd-datos.md                  Obligaciones RGPD + catálogo de vulnerabilidades
    ia-aiact.md                    Reglamento (UE) 2024/1689 para SaMD con IA
    checkpoints-volatiles.md       Lista de contraste web (qué verificar y dónde)
  assets/plantilla-informe.md      Plantilla del informe de situación
```

Ver `skills/analisis-regulatorio-samd/README.md` para el detalle de qué hace cada
paso.

---

## Actualizar

```bash
npx skills update analisis-regulatorio-samd
```

(o `npx skills update -y` para todo). Si instalaste por copia manual, repite la
copia sobre la carpeta existente.

## Desinstalar

```bash
npx skills remove analisis-regulatorio-samd --agent claude-code --global
```

Instalación manual: `rm -rf ~/.claude/skills/analisis-regulatorio-samd`.

---

## Limitaciones

Documento orientativo de planificación. No sustituye asesoría legal o
regulatoria. La calificación y clasificación vinculantes, y la evaluación de
conformidad, las confirma la autoridad competente (AEMPS) o un organismo
notificado. La normativa de producto sanitario e IA está en evolución activa: la
skill contrasta el estado vigente en fuentes oficiales, pero verifica siempre los
textos en EUR-Lex, BOE y AEMPS.
