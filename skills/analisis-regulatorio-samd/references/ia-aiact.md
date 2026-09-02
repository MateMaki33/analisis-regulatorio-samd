# Inteligencia artificial — Reglamento (UE) 2024/1689 (AI Act)

> **Volátil.** El calendario y el encaje con el MDR están cambiando (Digital
> Omnibus 2025-2026). **Antes de concluir, haz 1 búsqueda web** (ver
> `checkpoints-volatiles.md`) para confirmar: (a) fecha de aplicación de las
> obligaciones de alto riesgo para productos del Anexo I (productos sanitarios),
> (b) estado del Digital Omnibus, (c) estándares armonizados de IA disponibles.

Solo se ejecuta este paso si `signals.usa_ia_ml` es true o el usuario declara IA.

---

## 1. ¿Aplica el AI Act? ¿Como qué?

- **¿Es un "sistema de IA"?** (definición art. 3.1: sistema basado en máquina,
  con autonomía, que infiere de las entradas cómo generar salidas —
  predicciones, contenido, recomendaciones, decisiones). Modelos ML entrenados
  (`ai_ml.frameworks_ml`, `ai_ml.inferencia_clinica`, `model_files`) → sí.
  Reglas deterministas puras → normalmente no.
- **Rol:** ¿el proyecto es **proveedor** (desarrolla/comercializa el sistema de
  IA con su nombre) o **responsable del despliegue** (lo usa)? El fabricante de
  SaMD con IA es proveedor.

## 2. Clasificación de riesgo (AI Act)

| Categoría | Encaje típico de un SaMD |
|---|---|
| **Prohibido** (art. 5) | Poco habitual; revisar si hay scoring social, manipulación, categorización biométrica sensible |
| **Alto riesgo** (art. 6) | **Vía art. 6.1**: el producto es PS que requiere **evaluación de conformidad por tercero (organismo notificado)** bajo el MDR → **automáticamente alto riesgo**. Esto cubre, de facto, IIa, IIb y III. |
| Alto riesgo vía Anexo III | Menos relevante (el encaje suele ser 6.1 vía MDR) |
| **Riesgo limitado** (transparencia, art. 50) | Chatbots, IA generativa de contenido → informar al usuario de que interactúa con IA |
| **Riesgo mínimo** | Clase I MDR sin evaluación por tercero puede quedar aquí, salvo que aplique Anexo III |

**Conclusión práctica:** SaMD clase **IIa+ con IA = sistema de IA de alto riesgo**.
Clase I con IA → generalmente no alto riesgo por el AI Act, pero mantiene las
obligaciones del MDR y las de transparencia si aplica.

## 3. Obligaciones para IA de alto riesgo (arts. 8-17)

1. **Sistema de gestión de riesgos de IA** (art. 9), continuo, **integrado con
   ISO 14971** (no duplicar): riesgos por sesgo, error del modelo, uso indebido,
   deriva.
2. **Gobernanza de datos** (art. 10): conjuntos de entrenamiento/validación/prueba
   relevantes, representativos, sin errores y completos en la medida de lo
   posible; examen de sesgos; trazabilidad del origen de los datos; base jurídica
   para datos personales (ver `rgpd-datos.md` C.4).
3. **Documentación técnica** (art. 11 + Anexo IV): puede combinarse con la
   documentación técnica del MDR.
4. **Registro y logging automáticos** (art. 12): trazabilidad de eventos durante
   el ciclo de vida, suficiente para poscomercialización y para investigar
   incidentes.
5. **Transparencia e instrucciones de uso** (art. 13): capacidades y
   limitaciones, nivel de exactitud esperado, condiciones que pueden degradar el
   rendimiento, supervisión humana necesaria.
6. **Supervisión humana** (art. 14): medidas para que una persona pueda
   entender, vigilar, anular o detener el sistema; evitar el sesgo de
   automatización.
7. **Exactitud, robustez y ciberseguridad** (art. 15): métricas declaradas,
   resistencia a errores/fallos y a intentos de manipulación (adversarial,
   *data poisoning*).
8. **Sistema de gestión de calidad** (art. 17): se solapa con ISO 13485.
9. **Vigilancia poscomercialización de IA** (art. 72) + notificación de
   **incidentes graves** (art. 73): se coordina con la vigilancia del MDR.
10. **Registro** en la base de datos UE de sistemas de IA de alto riesgo (con
    matices para productos sanitarios).

## 4. Evaluación de conformidad — no hay doble certificación

Cuando el producto ya requiere organismo notificado por el MDR, la evaluación de
conformidad del AI Act se **integra en el procedimiento del MDR** (art. 43.3 AI
Act). Condición: el **organismo notificado debe tener designación específica para
el AI Act**. Comprobar que el ON elegido la tiene.

## 5. GPAI / modelos fundacionales

Si el proyecto **usa** un modelo de propósito general de terceros
(`ai_ml.llm_apis`): el proveedor del GPAI tiene sus propias obligaciones
(documentación, política de copyright, resumen de datos de entrenamiento; los
GPAI con riesgo sistémico, más). El fabricante del SaMD sigue siendo responsable
del sistema de alto riesgo que construye encima y debe obtener del proveedor la
información necesaria para cumplir los arts. 8-17.

## 6. Calendario (confirmar por web — estado sep-2026)

- 2-feb-2025: prohibiciones (art. 5) y alfabetización en IA.
- 2-ago-2025: obligaciones de GPAI; gobernanza; autoridades notificantes.
- 2-ago-2026: aplicación general; obligaciones de transparencia (art. 50);
  régimen de alto riesgo del **Anexo III** (sistemas autónomos).
- **Alto riesgo del Anexo I (productos sanitarios con IA): diferido.** El paquete
  *Digital Omnibus* (propuesta dic-2025) retrasa esta obligación —referencias del
  sector apuntan a **2 de agosto de 2027** para la vía art. 6.1 en IIb/III y hasta
  **2 de agosto de 2028** para IA embebida en productos regulados. **No está
  cerrado: verificar.**
- Estándares armonizados de IA (CEN-CENELEC JTC 21): en desarrollo; su
  disponibilidad condiciona la fecha efectiva de exigibilidad.

## 7. España

- **AESIA** (Agencia Española de Supervisión de la Inteligencia Artificial):
  autoridad de vigilancia del mercado para IA.
- Para SaMD, la vigilancia se coordina con **AEMPS**.
- Anteproyecto de ley nacional de "buen uso y gobernanza de la IA" en tramitación
  (régimen sancionador, sandbox regulatorio). Verificar estado.

## 8. Salida esperada del paso

- ¿Es sistema de IA? ¿Rol del proyecto?
- Categoría AI Act (con justificación art. 6.1 vía MDR).
- Lista de obligaciones arts. 8-17 con estado (según escáner: ¿hay logging?
  ¿explicabilidad `ai_ml.explicabilidad`? ¿control de sesgo `ai_ml.dataset_sesgo`?
  ¿supervisión humana en el flujo?).
- Requisito de designación AI Act del organismo notificado.
- Fecha de exigibilidad aplicable (la confirmada por web) y qué hacer ya.
