# Transferencias internacionales de datos (Capítulo V RGPD)

Objetivo del paso: determinar **si algún dato personal sale del Espacio Económico
Europeo (EEE)** —de forma directa o a través de **proxies, CDNs, subencargados o
APIs**— y, si sale, **qué mecanismo del capítulo V lo legitima** y si hace falta
un **TIA**.

**EEE** = 27 Estados de la UE + Islandia, Liechtenstein y Noruega. Todo lo demás
es "tercer país", incluido el Reino Unido (con decisión de adecuación propia).

---

## 1. Hay transferencia internacional si…

- el **responsable o el encargado** está establecido fuera del EEE; o
- un **subencargado** (hosting, *backup*, soporte, monitorización, CDN) trata los
  datos desde fuera del EEE; o
- los datos se **almacenan, procesan o enrutan** por infraestructura fuera del
  EEE: **región cloud no europea**, **CDN con PoP fuera del EEE**, **proxy inverso
  / WAF / balanceador / API gateway** terminado fuera del EEE, **réplica de base
  de datos o *backup*** en otra región, cola de mensajes gestionada fuera; o
- hay **acceso remoto** desde un tercer país (equipo de soporte o de desarrollo
  con acceso a producción fuera del EEE) — esto también es transferencia.
- Según el EDPB, incluso el **tránsito** de datos por un tercer país puede
  constituir transferencia si un importador fuera del EEE tiene **acceso**; el
  cifrado en tránsito reduce el riesgo pero no elimina por sí solo la
  calificación.

### Caso "proxies / servidores fuera de EU" (lo que suele preguntarse)

Si la aplicación enruta peticiones a través de un **proxy directo**, un
**reverse proxy**, un **API gateway** o un **servicio SaaS** cuyo endpoint
resuelve fuera del EEE, los datos personales de esas peticiones (cabeceras,
cuerpo, **IP del paciente**, identificadores, contenido clínico) se transfieren a
ese país. **Se trata como transferencia y se aplica el capítulo V, aunque la
empresa esté en España.** Lo mismo para: DNS gestionado fuera, `X-Forwarded-For`
que expone IPs a un tercero, *edge functions* en PoP no europeos, y captchas /
fuentes / mapas / *analytics* servidos desde fuera del EEE.

---

## 2. Mecanismos que legitiman la transferencia (en orden de preferencia)

1. **Decisión de adecuación (art. 45).** La Comisión ha declarado adecuados (a
   **sep-2026**, *verificar por web*): Andorra, Argentina, Canadá (entidades
   comerciales), Islas Feroe, Guernsey, Israel, Isla de Man, Japón, Jersey,
   Nueva Zelanda, República de Corea, Suiza, **Reino Unido**, Uruguay; y
   **EE. UU. solo para entidades adheridas al EU-US Data Privacy Framework
   (DPF)** (Decisión de la Comisión de 10-jul-2023). El DPF está bajo recurso
   ante el TGUE (asunto *Latombe*) y sujeto a revisiones periódicas →
   **verificar vigencia y comprobar que el proveedor concreto está listado en
   `dataprivacyframework.gov`** y que cubre la categoría de datos.
2. **Garantías adecuadas (art. 46):** Cláusulas Contractuales Tipo (**CCT/SCC**,
   Decisión 2021/914), Normas Corporativas Vinculantes (**BCR**), códigos de
   conducta o mecanismos de certificación aprobados. Con CCT/BCR: **TIA
   obligatorio** (ver §3).
3. **Excepciones para situaciones específicas (art. 49):** consentimiento
   explícito e informado del riesgo; necesidad para la ejecución de un contrato
   con el interesado; interés público importante; intereses vitales. Son
   **excepcionales y no estructurales**: no valen para un flujo continuo y
   sistemático (p. ej. hosting o *analytics*).

Sin ninguno de los tres, la transferencia es **ilícita**: hay que **repatriar**
el tratamiento a un proveedor del EEE o a una **región europea** del mismo
proveedor, o suprimir el flujo.

---

## 3. TIA — Transfer Impact Assessment (evaluación de las transferencias)

Obligatorio tras **Schrems II** (STJUE C-311/18) siempre que la transferencia se
apoye en el art. 46. Metodología: **Recomendaciones EDPB 01/2020**. Contenido
mínimo:

1. **Mapear** la transferencia: datos, finalidad, destinatarios, país,
   subencargados, toda la cadena.
2. Identificar el **instrumento del art. 46** utilizado.
3. Evaluar la **legislación y las prácticas del país de destino**: ¿permiten a
   sus autoridades un acceso a los datos que no supere el test de necesidad y
   proporcionalidad de la UE? (para EE. UU.: FISA 702, EO 12333, CLOUD Act).
4. Definir **medidas suplementarias**:
   - **técnicas:** cifrado de extremo a extremo con claves retenidas en el EEE,
     seudonimización robusta que impida al importador reidentificar, computación
     en *enclave* / cifrado homomórfico, *split processing*;
   - **contractuales:** transparencia sobre requerimientos recibidos, obligación
     de notificar, cláusulas de impugnación, auditoría;
   - **organizativas:** política de gestión de requerimientos de autoridades,
     registro y publicación de estadísticas, formación.
5. **Concluir:** ¿las medidas dejan la protección "esencialmente equivalente" a
   la del EEE? Si no → **no transferir**.
6. **Reevaluar** periódicamente y ante cambios normativos en el país de destino.

Si el proveedor está adherido al **DPF** y la transferencia a EE. UU. se ampara
en ese marco, **no** hacen falta CCT ni TIA para esa transferencia (equivale a
adecuación); documentar la comprobación de que la entidad concreta está
certificada y cubre la categoría de datos tratada.

---

## 4. Cadena de encargados y subencargados (art. 28)

- Todo proveedor que trate datos por cuenta del responsable necesita **contrato
  de encargado / DPA (art. 28.3)** — ver `entregables-datos-y-seguridad.md` §5.
- El encargado solo puede **subcontratar** con **autorización** del responsable y
  trasladando **las mismas obligaciones** al subencargado (art. 28.4), incluidas
  las de transferencia internacional.
- Pedir a cada proveedor su **lista de subprocesadores** y su **ubicación**:
  muchos SaaS "europeos" subcontratan soporte, CDN o *backup* fuera del EEE.

---

## 5. Cómo detectarlo en el repositorio

De la exploración del paso 2 (`infra_datos.*`, `third_party.*`, `ai_ml.llm_apis`)
y de los ficheros de configuración ya leídos enteros por ser de lectura
obligatoria (`.env` / `.env.example`, `docker-compose*.yml`, `*.tf` / IaC,
`config/`, `helm/`, `serverless.yml`). **Estos ficheros suelen tener secretos
reales del usuario** (contraseñas, API keys) junto a la señal de región que
buscas: sigue la regla de manejo seguro de `patrones-busqueda.md` — cita el
nombre de variable y el host/región, nunca el valor de nada que parezca
credencial.

- **`infra_datos.region_no_eu`** — regiones cloud no europeas en código, config o
  IaC: `us-east-1`, `us-west-2`, `ap-southeast-1`, `sa-east-1`, `us-central1`,
  `eastus`, `australiaeast`… Europeo = prefijos `eu-`, `europe-`, `westeurope`,
  `northeurope`, `francecentral`, `germanywestcentral`, `spaincentral`,
  `swedencentral`, `switzerlandnorth`.
- **`infra_datos.proxy_cdn`** — `HTTP_PROXY` / `HTTPS_PROXY`, `proxy_pass` /
  `upstream` (nginx), Cloudflare, Fastly, Akamai, CloudFront, `*.pac`, API
  gateways, `X-Forwarded-For`.
- **`infra_datos.data_residency`** — `AWS_REGION`, `AWS_DEFAULT_REGION`,
  `GOOGLE_CLOUD_REGION`, `AZURE_REGION`, claves `region:` / `location:`.
- **`third_party.*`** — analítica, *crash reporting*, publicidad, `nube_datos`:
  casi todos con infraestructura global; comprobar **residencia de datos**
  configurada y el DPA del proveedor.
- **`ai_ml.llm_apis`** — OpenAI, Anthropic, Cohere, Vertex, Bedrock: salvo
  endpoint/región europea **y** addendum de tratamiento de datos, asumir
  **transferencia a EE. UU.**; si se envían datos de paciente, además
  **comunicación de datos de salud a un tercero** (RGPD art. 9) y posible uso
  para entrenamiento (revisar términos).
- **Otros servicios frecuentes que implican salida del EEE:** correo
  transaccional (SendGrid, Mailgun, SES), SMS (Twilio), mapas (Google Maps),
  fuentes (Google Fonts), captcha (reCAPTCHA), *push* (FCM/APNs), observabilidad
  (Datadog, New Relic).

---

## 6. Salida esperada del paso — tabla de flujos de datos

| Flujo | Datos personales implicados | Proveedor / componente | Rol | País / región | ¿Sale del EEE? | Mecanismo cap. V | ¿TIA? | Estado / brecha |
|---|---|---|---|---|---|---|---|---|
| Hosting de la aplicación | Todos | {} | Encargado | {} | {sí/no} | {adecuación / CCT+TIA / DPF} | {sí/no/hecho/n.a.} | {} |
| Base de datos / almacenamiento | Todos | {} | Encargado | {} | {} | {} | {} | {} |
| *Backup* / réplica | Todos | {} | Subencargado | {} | {} | {} | {} | {} |
| API de IA / LLM | {campos enviados} | {} | Encargado | EE. UU. (asumido) | {} | {} | {} | {} |
| Analítica de producto | Identificadores, uso, IP | {} | Encargado | {} | {} | {} | {} | {} |
| *Crash reporting* / APM | Trazas, IP, ¿PII en *payloads*? | {} | Encargado | {} | {} | {} | {} | {} |
| CDN / proxy / WAF | IP, cabeceras, contenido | {} | Encargado | {} | {} | {} | {} | {} |
| Correo / SMS / *push* | Contacto, contenido | {} | Encargado | {} | {} | {} | {} | {} |

**Conclusión del paso:** ¿hay transferencias **sin cobertura** del capítulo V?
¿Qué flujos **repatriar** o **re-contratar** (región europea del proveedor)?
¿Qué **TIA faltan**? ¿Qué **DPA** hay que firmar o revisar (art. 28)? Marcar los
flujos sin base legal como **brecha crítica** en la sección 5 del informe.
