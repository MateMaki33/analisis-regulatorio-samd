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

## 7. España — autoridades y régimen sancionador nacional

> **Volátil.** La ley nacional de IA está en tramitación; cuantías, tipos
> infractores y reparto de autoridades pueden cambiar. Verificar por web antes
> de concluir (checkpoint 7).

### 7.1 AESIA y el reparto de autoridades de vigilancia

- **AESIA** (Agencia Española de Supervisión de la Inteligencia Artificial),
  creada por el **RD 729/2023** con Estatuto propio; sede en A Coruña; adscrita
  a la Secretaría de Estado de Digitalización e IA (Ministerio para la
  Transformación Digital y de la Función Pública). Operativa desde 2024.
- Funciones bajo el Reglamento (UE) 2024/1689: **autoridad nacional de
  coordinación**, **punto de contacto único** frente a la Comisión / Oficina
  Europea de IA, **representante de España en el Comité Europeo de IA**, y
  autoridad de vigilancia del mercado con carácter **general/residual**.
- **Reparto por sectores** (art. 74 del Reglamento + anteproyecto de ley):
  - **Productos sanitarios con IA → la autoridad de vigilancia del mercado es la
    AEMPS**, no AESIA. El **art. 74.3** del Reglamento atribuye la vigilancia del
    AI Act, para productos cubiertos por la legislación de armonización del
    Anexo I secc. A (incluye MDR e IVDR), a la autoridad ya designada por esa
    legislación. AESIA coordina; **AEMPS vigila e inspecciona** el sistema de IA
    embebido en el SaMD, dentro de su procedimiento de vigilancia del MDR.
  - **AEPD**: identificación y categorización biométrica, migración / asilo /
    gestión de fronteras, y usos en el ámbito policial.
  - **CGPJ**: IA en la Administración de Justicia. **Junta Electoral Central**:
    IA en procesos electorales. **Banco de España / CNMV / DGSFP**: IA de alto
    riesgo en entidades financieras.
- La **evaluación de conformidad** del sistema de IA de alto riesgo la sigue
  haciendo el **organismo notificado del MDR con designación AI Act** (art.
  43.3). Ninguna de estas autoridades "certifica" el producto.

### 7.2 Ley nacional de IA — estado

- **Anteproyecto de Ley para el buen uso y la gobernanza de la Inteligencia
  Artificial**, aprobado en Consejo de Ministros el **11-mar-2025** (primera
  vuelta). Contenido: designación de autoridades competentes, **régimen
  sancionador** propio, refuerzo de la transparencia (etiquetado de contenido
  sintético) y encaje del **sandbox** regulatorio (RD 817/2023).
- Tramitación pendiente: dictámenes (Consejo de Estado, AEPD…), aprobación como
  proyecto de ley y paso por las Cortes. **Verificar si se ha publicado en BOE**
  y su fecha de entrada en vigor.
- Mientras la ley no esté en vigor, AESIA y AEMPS ejercen funciones de
  **vigilancia** (requerir documentación, inspeccionar, ordenar medidas
  correctoras o la retirada), pero la **potestad sancionadora plena** depende de
  la habilitación y el procedimiento que fije la ley nacional.

### 7.3 Cuantías del Reglamento (art. 99) — aplicables desde 2-ago-2026

Multas máximas (la mayor de la cifra o el porcentaje del volumen de negocio
total anual mundial del ejercicio anterior):

| Infracción | Tope |
|---|---|
| Prácticas prohibidas (art. 5) | **35.000.000 € o 7 %** |
| Incumplimiento de obligaciones de operadores u organismos notificados — incluye las de sistemas de **alto riesgo** (arts. 8-17) y de transparencia (art. 50) | **15.000.000 € o 3 %** |
| Información incorrecta, incompleta o engañosa a organismos notificados o autoridades | **7.500.000 € o 1 %** |
| Proveedores de **GPAI** (art. 101, la impone la Comisión) | 15.000.000 € o 3 % |

Para **pymes y empresas emergentes** se aplica el **menor** de la cifra o el
porcentaje. Graduación: gravedad y duración de la infracción, tamaño del
operador, reincidencia, cooperación con la autoridad, medidas correctoras
adoptadas.

### 7.4 Régimen sancionador nacional (anteproyecto — cifras a verificar)

La ley española tipifica infracciones **propias** (adicionales a las del art. 99)
y las clasifica en leves / graves / muy graves. Según el texto difundido:

- **Muy graves:** uso de un sistema de IA incurso en prácticas prohibidas (art.
  5); incumplir el requerimiento de retirada o cese ordenado por la autoridad;
  no comunicar un **incidente grave** cuando exista obligación.
- **Graves:** no implantar el sistema de gestión de riesgos de IA; incumplir la
  **supervisión humana**; no conservar la documentación técnica ni los registros
  (logs); no **registrar** el sistema de alto riesgo en la base de datos UE;
  incumplir el **marcado / etiquetado de contenido generado o manipulado con
  IA** (deepfakes, contenido sintético); incumplir las instrucciones de
  transparencia hacia el usuario.
- **Leves:** desatención no sustancial de requerimientos de la autoridad;
  defectos formales en la información.

Horquillas propuestas para las infracciones propias (no las que ya derivan del
art. 99): del orden de **hasta 500.000 € (leves)**, **500.001 – 7.500.000 € o
2 % (graves)** y hasta las cuantías del art. 99 para las muy graves. **Estas
cifras y tipos no son definitivos — confirmar el texto vigente.**

Sanciones no pecuniarias posibles: **retirada del mercado** o prohibición de
comercialización del sistema, orden de puesta en conformidad en plazo,
publicidad de la sanción.

### 7.5 Otras obligaciones nacionales en la órbita de AESIA

- **Alfabetización en IA** (art. 4 del Reglamento, exigible desde 2-feb-2025): el
  operador debe garantizar competencia suficiente del personal que maneja el
  sistema. Documentar la formación impartida.
- **Sandbox** regulatorio de IA (RD 817/2023): entorno controlado de pruebas
  gestionado por AESIA; participar da acompañamiento pero **no exime** de
  cumplir ni blinda frente a sanción.

### 7.6 Qué reflejar en el informe

- Autoridad de vigilancia aplicable al producto (**AEMPS** para SaMD con IA;
  AESIA como coordinadora) y organismo notificado con designación AI Act.
- Estado de la ley nacional (en tramitación / en vigor), con URL y fecha de
  consulta.
- Exposición sancionadora: qué tope del art. 99 aplicaría al incumplimiento
  detectado (normalmente **15 M€ / 3 %** por obligaciones de alto riesgo;
  35 M€ / 7 % solo si hubiera práctica prohibida).
- Si el software **genera contenido** (texto, informes, imágenes) con IA:
  verificar la obligación de etiquetado del art. 50 y su tipificación como
  infracción grave en la ley nacional.

## 8. Salida esperada del paso

- ¿Es sistema de IA? ¿Rol del proyecto?
- Categoría AI Act (con justificación art. 6.1 vía MDR).
- Lista de obligaciones arts. 8-17 con estado (según la exploración: ¿hay logging?
  ¿explicabilidad `ai_ml.explicabilidad`? ¿control de sesgo `ai_ml.dataset_sesgo`?
  ¿supervisión humana en el flujo?).
- Requisito de designación AI Act del organismo notificado.
- Autoridad de vigilancia aplicable (**AEMPS** para SaMD con IA; AESIA coordina) y
  exposición sancionadora del incumplimiento detectado según el art. 99
  (15 M€ / 3 % por obligaciones de alto riesgo; 35 M€ / 7 % por prácticas
  prohibidas), más el estado —verificado por web— de la ley nacional de
  gobernanza de la IA.
- Fecha de exigibilidad aplicable (la confirmada por web) y qué hacer ya.
