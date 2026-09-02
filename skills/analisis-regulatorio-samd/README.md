# analisis-regulatorio-samd

Skill de Claude Code para analizar un proyecto de software y situarlo frente a la
normativa de **producto sanitario** (SaMD / MDSW) en España y la UE.

## Qué hace

1. Escanea el repositorio (script sin dependencias) y produce un JSON de señales:
   dominio clínico, datos personales y de categoría especial (RGPD art. 9), uso de
   IA/ML, terceros receptores de datos y vulnerabilidades de seguridad.
2. Aplica el test de **calificación** (MDCG 2019-11): ¿es producto sanitario?
3. **Clasifica** por riesgo (Regla 11, Anexo VIII MDR): I / IIa / IIb / III, y
   asigna la clase de seguridad IEC 62304 (A / B / C).
4. Construye el **mapa normativo**: MDR + RD 192/2023, guías MDCG, normas
   armonizadas (13485, 14971, 62304, 62366-1, 81001-5-1), evaluación clínica,
   EUDAMED/UDI, PMS, y horizontales (RGPD/LOPDGDD, AI Act, CRA, NIS2) — con
   obligatoriedad, implicaciones y organismo para cada una.
5. **Contrasta en internet** (fuentes oficiales: EUR-Lex, DOUE, BOE, AEMPS,
   Comisión, AEPD, CCN, AESIA) el estado vigente de cada norma aplicable: fechas
   de aplicación, edición que da presunción de conformidad, guías MDCG nuevas,
   calendario EUDAMED y AI Act, transposición de NIS2. Búsqueda acotada (~8 máx.),
   con URL y fecha de consulta en el informe.
6. Emite, **norma por norma, un veredicto**: ✅ Cumple / 🟡 Parcial / ❌ No cumple
   / ⬜ No evaluable — con evidencia (`fichero:línea`), brecha concreta y **cómo se
   gestiona** (proceso · organismo · entregable · plazo). Incluye requisitos
   técnicos, RGPD (+ lista de vulnerabilidades) y AI Act.
7. Ordena las brechas en una **ruta a la conformidad** por fases.
8. Redacta un **informe de situación** en Markdown (`assets/plantilla-informe.md`)
   y lo entrega al usuario.

## Estructura

```
SKILL.md                         Orquestación y flujo (lo que Claude lee primero)
scripts/scan_repo.py             Escáner estático → JSON compacto
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

## Eficiencia

- Claude nunca lee el repositorio completo: trabaja sobre el JSON del escáner y un
  puñado de ficheros citados como evidencia.
- Cada `references/*.md` se carga solo al llegar a su paso.
- El contraste web es obligatorio pero **acotado**: lista cerrada de consultas
  (`checkpoints-volatiles.md`), una por punto, ~8 máximo, fuentes oficiales, con
  URL y fecha en el informe.

## Limitaciones

Documento orientativo de planificación. No sustituye asesoría legal o regulatoria.
La clasificación vinculante y la evaluación de conformidad las confirma un
organismo notificado. Contenido normativo a fecha **septiembre 2026**.
