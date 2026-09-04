#!/usr/bin/env python3
"""
scan_repo.py - Escáner estático para análisis regulatorio SaMD.

Recorre un proyecto y emite un JSON compacto con las señales necesarias para
decidir: (a) si el software es un producto sanitario, (b) su clase de riesgo,
(c) qué datos personales/sensibles trata, (d) si usa IA/ML, (e) vulnerabilidades
evidentes de RGPD/seguridad.

Objetivo: que Claude NO tenga que leer todo el repositorio. Lee este JSON y, como
mucho, ~10 ficheros citados en `evidence`.

Uso:
    python scan_repo.py <ruta_proyecto> [--json-out informe.json] [--max-bytes 800000]

Sin dependencias externas. Python 3.8+.
"""
from __future__ import annotations
import argparse
import json
import os
import re
import sys
from pathlib import Path

SKIP_DIRS = {
    ".git", "node_modules", ".venv", "venv", "env", "__pycache__", "dist", "build",
    ".next", ".nuxt", "out", "target", "bin", "obj", ".gradle", ".idea", ".vscode",
    "vendor", "Pods", ".terraform", "coverage", ".mypy_cache", ".pytest_cache",
    "site-packages", ".tox", ".cache", "bower_components", ".dart_tool",
}
# Directorios que empiezan por "." pero SÍ interesa recorrer (CI, config de
# gestión de dependencias, plantillas de seguridad).
KEEP_DOT_DIRS = {".github", ".gitlab", ".circleci", ".azuredevops", ".ci"}

# Ficheros detectados por NOMBRE (no por contenido): fijación de versiones,
# SBOM ya generado, configuración de análisis de composición / CVE.
LOCKFILES = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "poetry.lock", "pipfile.lock",
    "cargo.lock", "composer.lock", "go.sum", "gemfile.lock", "packages.lock.json",
}
SCA_CONFIG_NAMES = {
    "dependabot.yml", "dependabot.yaml", "renovate.json", ".renovaterc",
    ".renovaterc.json", "renovate.json5", "trivy.yaml", ".trivyignore",
    ".snyk", "osv-scanner.toml", "dependency-check.properties",
}
CVD_NAMES = {"security.md", "security.txt"}
SBOM_NAME_RX = re.compile(
    r"(\.cdx\.json$|\.spdx(\.json)?$|^sbom\.json$|^bom\.json$|^bom\.xml$|cyclonedx)",
    re.IGNORECASE,
)
# Ficheros que sí interesa inspeccionar aunque sean grandes.
MANIFESTS = {
    "package.json", "requirements.txt", "pyproject.toml", "pipfile", "poetry.lock",
    "pom.xml", "build.gradle", "build.gradle.kts", "go.mod", "gemfile", "composer.json",
    "pubspec.yaml", "cargo.toml", "environment.yml", "setup.py", "setup.cfg",
}
DOC_NAMES = {"readme", "readme.md", "readme.rst", "readme.txt", "intended_use", "claims"}
# Ficheros de configuración/infra que interesa escanear aunque su extensión no
# esté en CODE_EXT (variables de entorno, compose, IaC, helm...).
CONFIG_NAME_PREFIXES = (".env", "docker-compose", "compose.", "serverless")
CONFIG_NAMES = {
    "dockerfile", "makefile", "procfile", "app.yaml", "app.yml", "vercel.json",
    "netlify.toml", "fly.toml", "render.yaml", "railway.json", "wrangler.toml",
}
CODE_EXT = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".kt", ".go", ".rb", ".php", ".cs",
    ".swift", ".m", ".mm", ".dart", ".c", ".cpp", ".cc", ".h", ".hpp", ".rs", ".scala",
    ".sql", ".sh", ".yaml", ".yml", ".json", ".xml", ".md", ".txt", ".env", ".ini",
    ".toml", ".cfg", ".properties", ".gradle", ".tf", ".conf", ".hcl", ".tfvars",
}
MODEL_EXT = {".pt", ".pth", ".onnx", ".h5", ".hdf5", ".pb", ".tflite", ".pkl", ".joblib",
             ".safetensors", ".ckpt", ".mlmodel", ".caffemodel"}

MAX_FILE_BYTES = 1_500_000          # no leer ficheros de código mayores que esto
MATCHES_PER_CATEGORY = 25           # límite de evidencias por categoría
CONTEXT_CHARS = 140

# --- Patrones de señal ------------------------------------------------------
# Cada entrada: nombre -> (regex compilada, descripción corta)
def _rx(p): return re.compile(p, re.IGNORECASE)

CLINICAL_PATTERNS = {
    "finalidad_medica": _rx(r"\b(intended\s+use|finalidad\s+prevista|indicaci[oó]n\s+de\s+uso|indication\s+for\s+use|contraindicaci|uso\s+previsto|prop[oó]sito\s+m[eé]dico)\b"),
    "diagnostico": _rx(r"\b(diagn[oó]stic|diagnos(is|e|tic)|cribado|screening|deteccci|detección\s+de\s+(lesion|tumor|patolog))\b"),
    "tratamiento_dosis": _rx(r"\b(dosis|dosage|posolog|mg/kg|mg\s*/\s*kg|UI/kg|bolus|pauta\s+de\s+medicaci|ajuste\s+de\s+(dosis|insulin)|treatment\s+plan)\b"),
    "monitorizacion": _rx(r"\b(monitoriz|signos\s+vitales|vital\s+signs|frecuencia\s+card|heart\s+rate|SpO2|saturaci[oó]n\s+de\s+ox|glucem|glucos|presi[oó]n\s+arterial|blood\s+pressure|arritmia|arrhythmi)\b"),
    "pronostico_riesgo": _rx(r"\b(pron[oó]stic|prognos|estratificaci[oó]n\s+de\s+riesgo|risk\s+scor|predicci[oó]n\s+cl[ií]nic|early\s+warning\s+score|sepsis\s+risk)\b"),
    "soporte_decision": _rx(r"\b(soporte\s+a\s+la?\s+decisi[oó]n|clinical\s+decision\s+support|CDSS|recomendaci[oó]n\s+cl[ií]nic|alerta\s+diagn[oó]stic)\b"),
    "estandares_salud": _rx(r"\b(HL7|FHIR|DICOM|SNOMED(\s*CT)?|LOINC|ICD-?10|CIE-?10|openEHR|IHE\s+profile)\b"),
    "dominio_clinico": _rx(r"\b(paciente|patient|historia\s+cl[ií]nic|electronic\s+health\s+record|EHR|EMR|s[ií]ntoma|symptom|enfermedad|disease|hospital|cl[ií]nic|m[eé]dic|physician|facultativo|anamnesis|triaje|triage)\b"),
    "imagen_medica": _rx(r"\b(radiolog|resonancia|CT\s+scan|tomograf|mamograf|ecograf|ultrasound|segmentaci[oó]n\s+de\s+imagen|PACS)\b"),
}

SPECIAL_CATEGORY_PATTERNS = {  # RGPD art. 9
    "datos_salud": _rx(r"\b(dato[s]?\s+de\s+salud|health\s+data|historial\s+m[eé]dic|diagn[oó]stic|medicaci[oó]n|patolog|discapacidad|disability|mental\s+health|salud\s+mental)\b"),
    "geneticos": _rx(r"\b(gen[oó]mic|genetic|ADN|DNA\s+sequence|variant\s+calling|mutaci[oó]n\s+gen)\b"),
    "biometricos": _rx(r"\b(biometr|huella\s+dactilar|fingerprint|reconocimiento\s+facial|face\s+recognition|iris\s+scan|voiceprint)\b"),
    "otros_9": _rx(r"\b(origen\s+[eé]tnic|ethnic\s+origin|afiliaci[oó]n\s+sindical|trade\s+union|creencia\s+religios|religious\s+belief|orientaci[oó]n\s+sexual|sexual\s+orientation|opini[oó]n\s+pol[ií]tic)\b"),
}

PII_PATTERNS = {
    "email_field": _rx(r"\b(e-?mail|correo)\b\s*[:=]|\"email\"|'email'"),
    "telefono": _rx(r"\b(tel[eé]fono|phone_?number|mobile_?number|m[oó]vil)\b"),
    "nombre_apellidos": _rx(r"\b(first_?name|last_?name|nombre|apellidos?|full_?name|surname)\b\s*[:=\"']"),
    "dni_nif": _rx(r"\b(DNI|NIF|NIE|documento\s+de\s+identidad|national\s+id|SSN|social\s+security\s+number|n[uú]mero\s+de\s+seguridad\s+social|tarjeta\s+sanitaria|CIP)\b"),
    "fecha_nacimiento": _rx(r"\b(fecha_?de_?nacimiento|birth_?date|date_?of_?birth|dob|fdn)\b"),
    "direccion": _rx(r"\b(direcci[oó]n\s+postal|street_?address|c[oó]digo\s+postal|zip_?code|postal_?code)\b"),
    "geolocalizacion": _rx(r"\b(geoloc|latitude|longitude|lat_?lon|gps_?coord|ubicaci[oó]n\s+del\s+usuario)\b"),
}

SECURITY_PATTERNS = {
    "secreto_hardcoded": _rx(r"(api[_-]?key|secret[_-]?key|access[_-]?token|client[_-]?secret|password|passwd|pwd)\s*[:=]\s*[\"'][A-Za-z0-9_\-\/\+=]{8,}[\"']"),
    "clave_privada": _rx(r"-----BEGIN\s+(RSA|EC|OPENSSH|PGP|DSA)?\s*PRIVATE\s+KEY-----"),
    "aws_key": _rx(r"\bAKIA[0-9A-Z]{16}\b"),
    "jwt_literal": _rx(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{6,}\b"),
    "hash_debil": _rx(r"\b(md5|sha1)\s*\(|hashlib\.(md5|sha1)|MessageDigest\.getInstance\(\s*[\"'](MD5|SHA-1)"),
    "http_inseguro": _rx(r"http://(?!localhost|127\.0\.0\.1|0\.0\.0\.0|example\.)"),
    "tls_desactivado": _rx(r"(verify\s*=\s*False|rejectUnauthorized:\s*false|InsecureSkipVerify:\s*true|CURLOPT_SSL_VERIFYPEER\s*,\s*(0|false)|trustAllCerts|ALLOW_ALL_HOSTNAME_VERIFIER)"),
    "sql_concat": _rx(r"(execute|query|rawQuery)\s*\(\s*[\"'].*(SELECT|INSERT|UPDATE|DELETE).*[\"']\s*\+|f[\"'].*(SELECT|INSERT|UPDATE|DELETE).*\{"),
    "eval_dinamico": _rx(r"\b(eval|exec)\s*\(|new\s+Function\s*\(|child_process\.exec\s*\("),
    "cifrado_reposo": _rx(r"\b(AES|Fernet|libsodium|nacl|crypto\.subtle|encrypt_at_rest|SSE-KMS|TransparentDataEncryption|pgcrypto|BitLocker)\b"),
}

LOGGING_PII_PATTERNS = {
    "log_datos": _rx(r"(log(ger)?\.(info|debug|warn|error|trace)|console\.(log|info|debug)|print|System\.out\.println)\s*\(.*(patient|paciente|password|token|dni|nif|health|salud|diagn[oó]stic|email|ssn)"),
}

AI_PATTERNS = {
    "frameworks_ml": _rx(r"\b(tensorflow|keras|torch|pytorch|scikit-?learn|sklearn|xgboost|lightgbm|onnxruntime|onnx|jax|paddlepaddle|transformers)\b"),
    "llm_apis": _rx(r"\b(openai|anthropic|langchain|llama[_-]?index|cohere|mistralai|vertexai|bedrock-runtime|azure-?openai|huggingface_hub|ollama)\b"),
    "entrenamiento": _rx(r"\b(model\.fit|\.train\(\)|train_test_split|DataLoader|epochs\s*=|loss\.backward|fine-?tun|gradient_descent)\b"),
    "inferencia_clinica": _rx(r"\b(model\.predict|\.predict_proba|inference|predicci[oó]n\s+del\s+modelo|classifier\.predict|softmax|argmax)\b"),
    "explicabilidad": _rx(r"\b(shap|lime|grad-?cam|feature_importance|explainab|interpretab|captum)\b"),
    "dataset_sesgo": _rx(r"\b(bias|sesgo|fairness|equidad|class_?weight|imbalanced|oversampl|undersampl|data\s+drift|deriva\s+de\s+datos)\b"),
}

THIRD_PARTY_PATTERNS = {
    "analitica": _rx(r"\b(google-?analytics|gtag|firebase[_-]?analytics|mixpanel|amplitude|segment\.com|hotjar|posthog|matomo)\b"),
    "crash_repo": _rx(r"\b(sentry|crashlytics|bugsnag|rollbar|datadog|new_?relic|appcenter)\b"),
    "publicidad": _rx(r"\b(admob|facebook[_-]?ads|doubleclick|applovin|unity[_-]?ads|adjust\.com|appsflyer)\b"),
    "nube_datos": _rx(r"\b(s3\.amazonaws|blob\.core\.windows|storage\.googleapis|firebasestorage|supabase|mongodb\+srv|rds\.amazonaws)\b"),
}

CONSENT_PATTERNS = {
    "consentimiento": _rx(r"\b(consentimiento\s+(informado|expl[ií]cito)|informed\s+consent|opt-?in|acepta[r]?\s+t[eé]rminos|privacy\s+policy|pol[ií]tica\s+de\s+privacidad|GDPR|RGPD|data\s+protection|DPIA|EIPD|derecho\s+de\s+supresi|right\s+to\s+erasure|anonimizaci|seud[oó]nim|pseudonym)\b"),
}

# Diagnóstico in vitro (posible encaje en IVDR (UE) 2017/746 en vez de / además
# del MDR): especímenes, ensayos de laboratorio, marcadores, resultados crudos
# de instrumentos de laboratorio que el software interpreta.
IVD_PATTERNS = {
    "especimen_ensayo": _rx(r"\b(esp[eé]cimen|specimen|muestra\s+(de\s+)?(sangre|orina|saliva|tejido|suero|plasma)|blood\s+sample|urine\s+sample|assay|ensayo\s+(cl[ií]nico|de\s+laboratorio)|reactivo|reagent|analito|analyte|biomarcador|biomarker|marcador\s+tumoral|tumor\s+marker|companion\s+diagn|diagn[oó]stico\s+ac[oó]mpañante|in\s*[- ]?vitro\s+diagnos|dispositivo\s+de\s+diagn[oó]stico\s+in\s*vitro)\b"),
    "instrumento_laboratorio": _rx(r"\b(ELISA|PCR|qPCR|RT-?PCR|citometr[ií]a\s+de\s+flujo|flow\s+cytometry|espectrofot[oó]metro|spectrophotomet|inmunoensayo|immunoassay|hemograma|blood\s+count|cultivo\s+microbiol|microbiological\s+culture|antibiograma|susceptibility\s+testing|patolog[ií]a\s+anat[oó]mica|histopatolog|blot\s+pattern|optical\s+density|densidad\s+[oó]ptica|Ct\s+value|umbral\s+de\s+ciclo)\b"),
    "genetica_secuenciacion": _rx(r"\b(secuenciaci[oó]n|sequencing|NGS|next[- ]generation\s+sequencing|panel\s+gen[eé]tico|genetic\s+panel|variant\s+calling|cariotipo|karyotyp|HLA\s+typing|tipaje\s+HLA)\b"),
}

# Espacio Europeo de Datos Sanitarios (EHDS) — Reglamento (UE) 2025/327:
# categorías prioritarias de datos (art. 14) que convierten al software en
# "sistema EHR" a efectos del cap. III, y componentes armonizados (EEHRxF,
# registro de accesos).
EHDS_PATTERNS = {
    "categoria_prioritaria": _rx(r"\b(resumen\s+de\s+paciente|patient\s+summary|receta\s+electr[oó]nica|electronic\s+prescription|e-?prescription|dispensaci[oó]n\s+electr[oó]nica|e-?dispensation|informe\s+de\s+alta|discharge\s+(report|summary)|informe\s+de\s+imagen\s+m[eé]dica|imaging\s+report|resultado(s)?\s+de\s+laboratorio|laboratory\s+results?)\b"),
    "interoperabilidad_ehr": _rx(r"\b(EEHRxF|European\s+Electronic\s+Health\s+Record\s+Exchange\s+Format|formato\s+europeo\s+de\s+intercambio|historia\s+cl[ií]nica\s+electr[oó]nica|electronic\s+health\s+record\s+system|sistema\s+(de\s+)?EHR|MyHealth@EU|IPS\s+(HL7\s+)?International\s+Patient\s+Summary)\b"),
    "registro_acceso_ehr": _rx(r"\b(access\s+log|registro\s+de\s+accesos?\s+a\s+(la\s+)?historia\s+cl[ií]nica|audit\s+log.*(historia\s+cl[ií]nic|health\s+record)|log\s+de\s+auditor[ií]a\s+cl[ií]nic)\b"),
}

# Infraestructura y salida de datos del EEE (transferencias internacionales).
INFRA_DATOS_PATTERNS = {
    "region_no_eu": _rx(
        r"\b(us-(east|west|gov)-\d|us-central\d|ap-(south|southeast|northeast|east)-\d|"
        r"sa-east-\d|ca-central-\d|af-south-\d|me-(south|central)-\d|"
        r"us-central1|us-east[145]|us-west[1-4]|northamerica-northeast\d|southamerica-east\d|"
        r"asia-(east|south|southeast|northeast)\d|australia-southeast\d|"
        r"eastus\d?|westus\d?|centralus|southcentralus|northcentralus|"
        r"australiaeast|australiasoutheast|brazilsouth|southeastasia|eastasia|"
        r"japaneast|japanwest|koreacentral|koreasouth|centralindia|southindia|westindia|"
        r"uaenorth|canadacentral|canadaeast|southafricanorth)\b"
    ),
    "proxy_cdn": _rx(
        r"\b(HTTPS?_PROXY|NO_PROXY|proxy_pass|upstream\s+[\w.-]+\s*\{|X-Forwarded-For|"
        r"cloudfront\.net|fastly\.net|akamai(hd|edge)?\.net|[\w.-]*\.cloudflare\.com|"
        r"fastly\.com|akamai\.com|edgekey\.net|b-cdn\.net)\b|\.pac\b"
    ),
    "data_residency": _rx(
        r"\b(data[_-]?residency|AWS_REGION|AWS_DEFAULT_REGION|GOOGLE_CLOUD_REGION|"
        r"GCP_REGION|AZURE_REGION|CLOUDSDK_COMPUTE_REGION|DEFAULT_REGION)\b|"
        r"\bregion\s*[:=]\s*[\"']?(us|ap|sa|ca|af|me|eastus|westus|australia|japan|korea|india|uae|brazil|canada)"
    ),
    "region_eu": _rx(
        r"\b(eu-(west|central|south|north)-\d|europe-(west|north|central|southwest)\d|"
        r"westeurope|northeurope|francecentral|germanywestcentral|spaincentral|"
        r"swedencentral|switzerlandnorth|norwayeast|polandcentral|italynorth|uksouth|ukwest)\b"
    ),
}

# Cadena de suministro de software: fijación de versiones, SBOM, SCA, CVD.
SUPPLY_CHAIN_PATTERNS = {
    "sca_ci": _rx(
        r"\b(dependabot|renovate(bot)?|snyk|trivy|grype|osv-scanner|"
        r"dependency-check|dependency-track|govulncheck|cargo\s+audit|"
        r"bundler-audit|pip-audit|npm\s+audit|composer\s+audit)\b"
    ),
    "sbom_ref": _rx(r"\b(cyclonedx|spdx|\bsbom\b|software\s+bill\s+of\s+materials|bill\s+of\s+materials)\b"),
    "vex_ref": _rx(r"\b(VEX|vulnerability[- ]exploitability|openvex|csaf)\b"),
    "cvd_ref": _rx(
        r"\b(coordinated\s+(vulnerability\s+)?disclosure|responsible\s+disclosure|"
        r"vulnerability\s+disclosure\s+policy|security\.txt|report\s+a\s+vulnerability)\b"
    ),
    "soup": _rx(r"\b(SOUP|software\s+of\s+unknown\s+provenance)\b"),
}

ALL_GROUPS = {
    "clinical": CLINICAL_PATTERNS,
    "special_category": SPECIAL_CATEGORY_PATTERNS,
    "pii": PII_PATTERNS,
    "security": SECURITY_PATTERNS,
    "logging_pii": LOGGING_PII_PATTERNS,
    "ai_ml": AI_PATTERNS,
    "third_party": THIRD_PARTY_PATTERNS,
    "privacy_controls": CONSENT_PATTERNS,
    "infra_datos": INFRA_DATOS_PATTERNS,
    "supply_chain": SUPPLY_CHAIN_PATTERNS,
    "ivd": IVD_PATTERNS,
    "ehds": EHDS_PATTERNS,
}


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d.lower() not in SKIP_DIRS
            and (not d.startswith(".") or d.lower() in KEEP_DOT_DIRS)
        ]
        for fn in filenames:
            yield Path(dirpath) / fn


def count_deps(name: str, text: str) -> "int | None":
    """Cuenta aproximada de dependencias DIRECTAS declaradas en un manifiesto.

    Best-effort y tolerante a errores: devuelve None si no sabe interpretarlo.
    """
    n = name.lower()
    try:
        if n == "package.json":
            data = json.loads(text)
            return len(data.get("dependencies", {}) or {}) + len(data.get("devDependencies", {}) or {})
        if n == "composer.json":
            data = json.loads(text)
            return len(data.get("require", {}) or {}) + len(data.get("require-dev", {}) or {})
        if n in ("requirements.txt", "constraints.txt"):
            return sum(
                1 for ln in text.splitlines()
                if ln.strip() and not ln.strip().startswith(("#", "-r", "--"))
            )
        if n == "pyproject.toml":
            # cuenta líneas dentro de [tool.poetry.dependencies] / [project].dependencies
            return len(re.findall(r"^\s*[A-Za-z0-9_.\-]+\s*=\s*[\"'{]", text, re.MULTILINE)) or None
        if n in ("go.mod",):
            return len(re.findall(r"^\s+[\w.\-/]+\s+v\d", text, re.MULTILINE)) or None
        if n in ("cargo.toml", "pipfile"):
            return len(re.findall(r"^\s*[A-Za-z0-9_.\-]+\s*=", text, re.MULTILINE)) or None
        if n in ("build.gradle", "build.gradle.kts"):
            return len(re.findall(r"\b(implementation|api|compile|testImplementation|runtimeOnly)\b[\s(]", text)) or None
        if n == "pom.xml":
            return text.count("<dependency>") or None
        if n == "gemfile":
            return len(re.findall(r"^\s*gem\s+[\"']", text, re.MULTILINE)) or None
        if n in ("pubspec.yaml", "environment.yml"):
            return None
    except Exception:
        return None
    return None


def rel(root: Path, p: Path) -> str:
    try:
        return str(p.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(p).replace("\\", "/")


def snippet(text: str, m: re.Match) -> str:
    start = max(0, m.start() - 30)
    end = min(len(text), m.end() + CONTEXT_CHARS)
    s = text[start:end].replace("\n", " ").replace("\r", " ").strip()
    return re.sub(r"\s{2,}", " ", s)[:CONTEXT_CHARS + 40]


def line_of(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--max-bytes", type=int, default=MAX_FILE_BYTES)
    args = ap.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(json.dumps({"error": f"ruta no encontrada: {root}"}))
        sys.exit(1)

    result = {
        "root": str(root),
        "files_scanned": 0,
        "bytes_scanned": 0,
        "languages": {},
        "manifests": {},          # nombre -> texto (recortado)
        "model_files": [],
        "doc_files": [],
        "findings": {g: [] for g in ALL_GROUPS},
        "counts": {g: 0 for g in ALL_GROUPS},
        "hits_by_category": {},   # categoria -> nº de coincidencias
        "supply_chain": {         # detectado por NOMBRE de fichero
            "lockfiles": [],
            "sca_config": [],     # dependabot / renovate / trivy / snyk...
            "sbom_files": [],
            "cvd_policy": [],     # SECURITY.md / security.txt
            "dependency_counts": {},  # ruta de manifiesto -> nº aprox. de deps directas
        },
    }

    per_cat_seen = {}

    for p in iter_files(root):
        name = p.name.lower()
        ext = p.suffix.lower()

        if ext in MODEL_EXT:
            result["model_files"].append(rel(root, p))
            continue

        # Detección por NOMBRE (no se escanea el contenido de estos ficheros).
        if name in LOCKFILES:
            result["supply_chain"]["lockfiles"].append(rel(root, p))
        if name in SCA_CONFIG_NAMES:
            result["supply_chain"]["sca_config"].append(rel(root, p))
        if name in CVD_NAMES:
            result["supply_chain"]["cvd_policy"].append(rel(root, p))
        if SBOM_NAME_RX.search(name):
            result["supply_chain"]["sbom_files"].append(rel(root, p))

        is_manifest = name in MANIFESTS
        is_doc = name in DOC_NAMES or (ext == ".md" and "readme" in name)
        is_config = (
            name in CONFIG_NAMES
            or name.startswith(CONFIG_NAME_PREFIXES)
        )

        if ext in CODE_EXT:
            result["languages"][ext] = result["languages"].get(ext, 0) + 1

        if not (is_manifest or is_doc or is_config or ext in CODE_EXT):
            continue

        try:
            size = p.stat().st_size
        except OSError:
            continue
        if size > args.max_bytes and not is_manifest:
            continue

        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except (OSError, UnicodeError):
            continue

        result["files_scanned"] += 1
        result["bytes_scanned"] += len(text)
        rp = rel(root, p)

        if is_manifest:
            result["manifests"][rp] = text[:6000]
            dc = count_deps(p.name, text)
            if dc is not None:
                result["supply_chain"]["dependency_counts"][rp] = dc
        if is_doc:
            result["doc_files"].append(rp)

        for gname, patterns in ALL_GROUPS.items():
            for cat, rx in patterns.items():
                key = f"{gname}.{cat}"
                for m in rx.finditer(text):
                    result["hits_by_category"][key] = result["hits_by_category"].get(key, 0) + 1
                    seen = per_cat_seen.get(key, 0)
                    if seen >= MATCHES_PER_CATEGORY:
                        continue
                    per_cat_seen[key] = seen + 1
                    result["findings"][gname].append({
                        "category": cat,
                        "file": rp,
                        "line": line_of(text, m.start()),
                        "match": snippet(text, m),
                    })
                    result["counts"][gname] += 1

    # Señales derivadas para acelerar el razonamiento de Claude.
    hbc = result["hits_by_category"]
    def any_hit(prefix):
        return any(k.startswith(prefix) and v > 0 for k, v in hbc.items())

    result["signals"] = {
        "parece_dominio_clinico": any_hit("clinical."),
        "senal_finalidad_medica": hbc.get("clinical.finalidad_medica", 0) > 0
            or hbc.get("clinical.soporte_decision", 0) > 0
            or hbc.get("clinical.diagnostico", 0) > 0,
        "trata_datos_salud": hbc.get("special_category.datos_salud", 0) > 0
            or hbc.get("clinical.dominio_clinico", 0) > 0,
        "categorias_especiales_rgpd": any_hit("special_category."),
        "trata_pii": any_hit("pii."),
        "usa_ia_ml": any_hit("ai_ml."),
        "entrena_modelos": hbc.get("ai_ml.entrenamiento", 0) > 0,
        "posibles_vulnerabilidades_seguridad": any(
            hbc.get(f"security.{c}", 0) > 0 for c in
            ("secreto_hardcoded", "clave_privada", "aws_key", "jwt_literal",
             "hash_debil", "tls_desactivado", "sql_concat", "http_inseguro")
        ),
        "posible_log_de_datos_sensibles": hbc.get("logging_pii.log_datos", 0) > 0,
        "terceros_receptores_datos": any_hit("third_party."),
        "menciona_controles_privacidad": any_hit("privacy_controls."),
        "hay_modelos_entrenados_en_repo": len(result["model_files"]) > 0,
        # --- Transferencias internacionales (Cap. V RGPD) ---
        "posible_transferencia_internacional": (
            hbc.get("infra_datos.region_no_eu", 0) > 0
            or hbc.get("infra_datos.proxy_cdn", 0) > 0
            or hbc.get("ai_ml.llm_apis", 0) > 0
            or any_hit("third_party.")
        ),
        "menciona_region_no_eu": hbc.get("infra_datos.region_no_eu", 0) > 0,
        "menciona_region_eu": hbc.get("infra_datos.region_eu", 0) > 0,
        "menciona_proxy_o_cdn": hbc.get("infra_datos.proxy_cdn", 0) > 0,
        # --- Cadena de suministro / SBOM ---
        "fija_versiones_dependencias": len(result["supply_chain"]["lockfiles"]) > 0,
        "tiene_sbom": len(result["supply_chain"]["sbom_files"]) > 0
            or hbc.get("supply_chain.sbom_ref", 0) > 0,
        "tiene_gestion_dependencias": len(result["supply_chain"]["sca_config"]) > 0
            or hbc.get("supply_chain.sca_ci", 0) > 0,
        "tiene_politica_divulgacion": len(result["supply_chain"]["cvd_policy"]) > 0
            or hbc.get("supply_chain.cvd_ref", 0) > 0,
        "total_dependencias_directas_aprox": sum(
            result["supply_chain"]["dependency_counts"].values()
        ) or None,
        # --- IVDR (diagnóstico in vitro) y EHDS (historia clínica / interoperabilidad) ---
        "posible_diagnostico_in_vitro": any_hit("ivd."),
        "posible_ehr_o_ehds": any_hit("ehds.") or (
            hbc.get("clinical.estandares_salud", 0) > 0
            and hbc.get("clinical.dominio_clinico", 0) > 0
        ),
    }

    out = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(out, encoding="utf-8")
        print(f"Escrito: {args.json_out}")
        print(json.dumps({"signals": result["signals"],
                          "counts": result["counts"],
                          "files_scanned": result["files_scanned"]},
                         ensure_ascii=False, indent=2))
    else:
        print(out)


if __name__ == "__main__":
    main()
