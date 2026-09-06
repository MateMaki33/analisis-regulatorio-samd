# SBOM y gestión de vulnerabilidades de dependencias

Objetivo del paso: (a) decir si **este** proyecto **debe** generar un SBOM y
mantener una gestión de vulnerabilidades, y **por qué**; (b) explicar **qué es
cada cosa**; (c) inventariar las **dependencias** del repo y comprobar qué hay ya
hecho; (d) recomendar **cómo generarlo** para el stack detectado.

---

## 1. Qué es cada cosa

**SBOM (Software Bill of Materials)** — inventario legible por máquina de **todos
los componentes** de software que forman el producto: dependencias directas y
**transitivas**, librerías del sistema, imágenes base de contenedor; con nombre,
versión, editor, licencia, *hash* y, a ser posible, procedencia (identificadores
**PURL** / **CPE**). Es la "lista de ingredientes" del software. En **IEC 62304**
el concepto equivalente es el inventario **SOUP** (*Software of Unknown
Provenance*); el SBOM es su materialización moderna y verificable.

- Formatos estándar: **CycloneDX** (OWASP; `bom.json` / `*.cdx.json`) y **SPDX**
  (Linux Foundation; ISO/IEC 5962). Cualquiera vale; CycloneDX es el más habitual
  en seguridad y el que mejor integra VEX.

**Gestión de vulnerabilidades (SCA, *Software Composition Analysis*)** — proceso
**continuo** de cruzar el SBOM contra bases de vulnerabilidades (NVD, **OSV**,
GitHub Advisories, avisos del proveedor) para detectar componentes con
**CVE conocidos**, evaluarlos frente a la seguridad del paciente y de los datos,
**priorizarlos** (CVSS + explotabilidad + alcance real en el producto) y
**remediarlos**: actualizar, mitigar, o aceptar con justificación documentada.

**VEX (*Vulnerability Exploitability eXchange*)** — documento que acompaña al
SBOM y declara, para cada CVE que afecta a un componente incluido, si el producto
está **afectado / no afectado / en investigación / corregido**, con la
justificación (p. ej. "el código vulnerable no se invoca en nuestra
configuración"). Evita que cada CVE de una transitiva dispare una alarma y una
retirada innecesaria.

**CVD (*Coordinated Vulnerability Disclosure*)** — política y canal **públicos**
para que terceros reporten vulnerabilidades del producto: `SECURITY.md` /
`security.txt`, dirección de contacto, clave PGP, plazos de respuesta y de
parcheo. Para producto sanitario, coordinación con **INCIBE-CERT** (CSIRT de
referencia en España) y, cuando aplique, con el CSIRT del cliente hospitalario.
IEC 81001-5-1 y MDCG 2019-16 la exigen.

---

## 2. ¿Debo generar SBOM? ¿Y gestión de vulnerabilidades?

| Situación del producto | SBOM | Gestión de vulnerabilidades |
|---|---|---|
| **MDSW (cualquier clase) conectado a red o que procesa datos** | **Obligatorio de facto.** MDCG 2019-16 Rev.1 e IEC 81001-5-1 (§4 diseño seguro, §7 cadena de suministro) lo exigen; el RGSF **Anexo I punto 17 del MDR** lo hace vinculante. El organismo notificado lo pide en el expediente técnico, **por versión**. | **Obligatoria de facto**, durante **todo el ciclo de vida**, incluida la poscomercialización (vigilancia CVE + parcheo). |
| MDSW aislado, sin red, sin datos personales | SBOM recomendado (el **SOUP** sigue siendo exigido por IEC 62304). | Cribado de anomalías conocidas del SOUP sí; vigilancia CVE proporcional al riesgo. |
| **Componente que NO califica como PS y se distribuye por separado** | Puede caer bajo el **Cyber Resilience Act (UE) 2024/2847**: SBOM y gestión de vulnerabilidades **obligatorios por ley** (no solo de facto), con **notificación de vulnerabilidades explotadas activamente** a ENISA/CSIRT (plazos de 24 h / 72 h). Aplicación escalonada; obligación de notificación **desde 11-sep-2026**, resto **desde 11-dic-2027**. *Verificar.* | Ídem. |
| Software **sin finalidad médica** pero con datos personales | No hay obligación explícita de SBOM, pero el **art. 32 RGPD** (seguridad del tratamiento) exige gestionar las vulnerabilidades de las dependencias; el SBOM es el medio práctico de demostrarlo. | Sí, como medida del art. 32. |
| Cliente hospitalario / contratación pública | Suele exigirse **SBOM + informe SCA** en el pliego, con independencia de lo anterior. | Ídem. |

**Regla operativa para el informe:** si el producto es **MDSW**, o si
`signals.trata_pii` / `signals.parece_dominio_clinico` → el informe **debe
declarar "SBOM obligatorio" y "gestión de vulnerabilidades obligatoria"**,
indicar su **estado** (presente / parcial / ausente según `supply_chain.*`) y
explicar **cómo generarlo**.

---

## 3. Inventario de dependencias (a partir del repo)

Ejecuta `scripts/scan_repo.py <ruta> --json-out <scratch>/deps.json` y trabaja
sobre `manifests` y `supply_chain` de su JSON — **no** leas árboles de
dependencias completos a mano:

1. **Enumerar dependencias directas** por manifiesto: `package.json`
   (`dependencies` + `devDependencies`), `requirements.txt` / `pyproject.toml`,
   `pom.xml`, `build.gradle`, `go.mod`, `Gemfile`, `composer.json`, `Cargo.toml`,
   `pubspec.yaml`. Usa `supply_chain.dependency_counts` como resumen.
2. **¿Versiones fijadas?** Presencia de *lockfile*
   (`supply_chain.lockfiles`): sin él, el *build* no es reproducible → brecha
   de IEC 62304 (gestión de configuración) además de riesgo de suministro.
3. **Marcar dependencias sensibles:** las que tocan datos de salud, cripto,
   autenticación, serialización, parsers, o son APIs de terceros
   (`third_party.*`, `ai_ml.llm_apis`).
4. **¿Hay SBOM ya?** `supply_chain.sbom_files` (`bom.xml`, `*.cdx.json`,
   `*.spdx.json`).
5. **¿Hay SCA/gestión?** `supply_chain.sca_config` /
   `supply_chain.sca_ci` (Dependabot, Renovate, Trivy, Grype, `osv-scanner`,
   Snyk, OWASP Dependency-Check/Track en CI).
6. **¿Hay CVD?** `supply_chain.cvd_policy` (`SECURITY.md` / `security.txt`).

---

## 4. Cómo se genera y se mantiene

**Generar el SBOM** (elegir según `languages` / `manifests`):

| Stack | Herramienta sugerida |
|---|---|
| Multi-lenguaje / contenedores / repo entero | `syft <dir\|imagen> -o cyclonedx-json` · `trivy sbom -f cyclonedx` |
| Node.js | `npm sbom --sbom-format cyclonedx` (npm ≥ 10) · `cdxgen` |
| Python | `cyclonedx-py` · `cdxgen` |
| Java (Maven/Gradle) | `cyclonedx-maven-plugin` · `cyclonedx-gradle-plugin` |
| Go | `cyclonedx-gomod` |
| Rust | `cargo cyclonedx` (+ `cargo auditable` para embeber) |
| PHP (Composer) | `cyclonedx-php-composer` |
| .NET | `dotnet CycloneDX` |

Regenerar **en cada *release*** y versionar el SBOM junto al artefacto; el SBOM
que se entrega al organismo notificado corresponde a la **versión concreta**
puesta en el mercado.

**Cribar vulnerabilidades (SCA):**
- **En CI (continuo):** Dependabot o Renovate (PRs de actualización),
  `osv-scanner`, **Trivy**, **Grype**, OWASP **Dependency-Check**;
  **Dependency-Track** como servidor que ingiere SBOM y monitoriza en el tiempo.
- **Auditoría puntual:** `npm audit`, `pip-audit`, `govulncheck`, `cargo audit`,
  `bundler-audit`, `dotnet list package --vulnerable`, `composer audit`.
- **Registrar** cada hallazgo: componente, versión, CVE, CVSS, vector, ¿código
  alcanzable?, decisión (actualizar / mitigar / aceptar), fecha objetivo. Enlazar
  con el **Risk Management File (ISO 14971)** cuando el impacto pueda llegar al
  paciente, y emitir **VEX** para los CVE no explotables.

**Poscomercialización:** vigilancia continua de CVE de **todo el SBOM** mientras
el producto esté en el mercado; procedimiento de **parcheo** con plazos por
severidad; **CVD** publicada; notificación a **AEMPS** (NotificaPS) si una
vulnerabilidad deriva en incidente grave del producto, y a la **AEPD** (72 h) si
hay brecha de datos personales.

**Cómo lo evalúa el organismo notificado:** revisa el plan de gestión de
ciberseguridad, muestrea el SBOM frente a la versión, comprueba que hay proceso
de vigilancia CVE y de parcheo, y que la información de seguridad para el usuario
(MDS2 o equivalente) está.

---

## 5. Señales de `scan_repo.py`

- `manifests` → base del inventario; `supply_chain.dependency_counts` → nº de
  dependencias directas por manifiesto.
- `supply_chain.lockfiles` → versiones fijadas (a favor de reproducibilidad
  IEC 62304).
- `supply_chain.sbom_files` → SBOM ya presente en el repo.
- `supply_chain.sca_config` / `supply_chain.sca_ci` → gestión de vulnerabilidades
  ya iniciada (Dependabot / Renovate / Trivy / osv-scanner / Snyk…).
- `supply_chain.cvd_policy` → `SECURITY.md` / `security.txt` presente.
- `signals.tiene_sbom`, `signals.tiene_gestion_dependencias`,
  `signals.fija_versiones_dependencias` → resumen para el veredicto.
- Ausencia de todo lo anterior en un producto conectado o con datos → **brecha
  crítica** en la sección de ciberseguridad (IEC 81001-5-1) y en la de datos
  (RGPD art. 32).

---

## 6. Salida esperada del paso

1. **Veredicto:** ¿SBOM obligatorio? ¿Gestión de vulnerabilidades obligatoria?
   ¿Por qué (regla del §2)?
2. **Inventario resumido:** nº de dependencias directas por manifiesto,
   ¿versiones fijadas?, dependencias sensibles y de terceros.
3. **Estado:** ¿hay SBOM?, ¿hay SCA en CI?, ¿hay CVD? — con `fichero` como
   evidencia.
4. **Recomendación concreta:** comando de generación de SBOM para el stack
   detectado + herramienta de cribado CVE + `SECURITY.md` si falta.
5. Brechas priorizadas para la sección 5 y la 6.5 del informe. **No** ejecutes
   escaneos ni instales herramientas salvo que el usuario lo pida.
