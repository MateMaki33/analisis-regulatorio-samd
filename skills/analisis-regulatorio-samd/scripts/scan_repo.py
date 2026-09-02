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
# Ficheros que sí interesa inspeccionar aunque sean grandes.
MANIFESTS = {
    "package.json", "requirements.txt", "pyproject.toml", "pipfile", "poetry.lock",
    "pom.xml", "build.gradle", "build.gradle.kts", "go.mod", "gemfile", "composer.json",
    "pubspec.yaml", "cargo.toml", "environment.yml", "setup.py", "setup.cfg",
}
DOC_NAMES = {"readme", "readme.md", "readme.rst", "readme.txt", "intended_use", "claims"}
CODE_EXT = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".kt", ".go", ".rb", ".php", ".cs",
    ".swift", ".m", ".mm", ".dart", ".c", ".cpp", ".cc", ".h", ".hpp", ".rs", ".scala",
    ".sql", ".sh", ".yaml", ".yml", ".json", ".xml", ".md", ".txt", ".env", ".ini",
    ".toml", ".cfg", ".properties", ".gradle", ".tf",
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

ALL_GROUPS = {
    "clinical": CLINICAL_PATTERNS,
    "special_category": SPECIAL_CATEGORY_PATTERNS,
    "pii": PII_PATTERNS,
    "security": SECURITY_PATTERNS,
    "logging_pii": LOGGING_PII_PATTERNS,
    "ai_ml": AI_PATTERNS,
    "third_party": THIRD_PARTY_PATTERNS,
    "privacy_controls": CONSENT_PATTERNS,
}


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d.lower() not in SKIP_DIRS and not d.startswith(".")]
        for fn in filenames:
            yield Path(dirpath) / fn


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
    }

    per_cat_seen = {}

    for p in iter_files(root):
        name = p.name.lower()
        ext = p.suffix.lower()

        if ext in MODEL_EXT:
            result["model_files"].append(rel(root, p))
            continue

        is_manifest = name in MANIFESTS
        is_doc = name in DOC_NAMES or (ext == ".md" and "readme" in name)

        if ext in CODE_EXT:
            result["languages"][ext] = result["languages"].get(ext, 0) + 1

        if not (is_manifest or is_doc or ext in CODE_EXT):
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
