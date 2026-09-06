#!/usr/bin/env python3
"""
scan_repo.py - Inventario de dependencias y cadena de suministro para el
análisis regulatorio SaMD.

La calificación (¿es producto sanitario?), el tratamiento de datos y las
vulnerabilidades de RGPD/seguridad se detectan **leyendo el repositorio**
(ver `references/patrones-busqueda.md`), no con este script. Este script solo
cubre la parte mecánica que sí conviene automatizar: contar dependencias
declaradas en manifiestos, y detectar por NOMBRE de fichero si hay lockfiles,
SBOM ya generado, configuración de SCA (análisis de composición) y política de
divulgación de vulnerabilidades (CVD). Se usa en el paso 6d (SBOM).

Uso:
    python scan_repo.py <ruta_proyecto> [--json-out informe.json]

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
KEEP_DOT_DIRS = {".github", ".gitlab", ".circleci", ".azuredevops", ".ci"}

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
MANIFESTS = {
    "package.json", "requirements.txt", "pyproject.toml", "pipfile", "poetry.lock",
    "pom.xml", "build.gradle", "build.gradle.kts", "go.mod", "gemfile", "composer.json",
    "pubspec.yaml", "cargo.toml", "environment.yml", "setup.py", "setup.cfg",
}
MODEL_EXT = {".pt", ".pth", ".onnx", ".h5", ".hdf5", ".pb", ".tflite", ".pkl", ".joblib",
             ".safetensors", ".ckpt", ".mlmodel", ".caffemodel"}
CODE_EXT = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".kt", ".go", ".rb", ".php", ".cs",
    ".swift", ".m", ".mm", ".dart", ".c", ".cpp", ".cc", ".h", ".hpp", ".rs", ".scala",
}


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


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames
            if d.lower() not in SKIP_DIRS
            and (not d.startswith(".") or d.lower() in KEEP_DOT_DIRS)
        ]
        for fn in filenames:
            yield Path(dirpath) / fn


def rel(root: Path, p: Path) -> str:
    try:
        return str(p.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(p).replace("\\", "/")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(json.dumps({"error": f"ruta no encontrada: {root}"}))
        sys.exit(1)

    result = {
        "root": str(root),
        "languages": {},
        "manifests": [],
        "model_files": [],
        "supply_chain": {
            "lockfiles": [],
            "sca_config": [],
            "sbom_files": [],
            "cvd_policy": [],
            "dependency_counts": {},
        },
    }

    for p in iter_files(root):
        name = p.name.lower()
        ext = p.suffix.lower()

        if ext in MODEL_EXT:
            result["model_files"].append(rel(root, p))
            continue
        if ext in CODE_EXT:
            result["languages"][ext] = result["languages"].get(ext, 0) + 1

        if name in LOCKFILES:
            result["supply_chain"]["lockfiles"].append(rel(root, p))
        if name in SCA_CONFIG_NAMES:
            result["supply_chain"]["sca_config"].append(rel(root, p))
        if name in CVD_NAMES:
            result["supply_chain"]["cvd_policy"].append(rel(root, p))
        if SBOM_NAME_RX.search(name):
            result["supply_chain"]["sbom_files"].append(rel(root, p))

        if name in MANIFESTS:
            rp = rel(root, p)
            result["manifests"].append(rp)
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except (OSError, UnicodeError):
                continue
            dc = count_deps(p.name, text)
            if dc is not None:
                result["supply_chain"]["dependency_counts"][rp] = dc

    sc = result["supply_chain"]
    result["signals"] = {
        "fija_versiones_dependencias": len(sc["lockfiles"]) > 0,
        "tiene_sbom": len(sc["sbom_files"]) > 0,
        "tiene_gestion_dependencias": len(sc["sca_config"]) > 0,
        "tiene_politica_divulgacion": len(sc["cvd_policy"]) > 0,
        "total_dependencias_directas_aprox": sum(sc["dependency_counts"].values()) or None,
        "hay_modelos_entrenados_en_repo": len(result["model_files"]) > 0,
    }

    out = json.dumps(result, ensure_ascii=False, indent=2)
    if args.json_out:
        Path(args.json_out).write_text(out, encoding="utf-8")
        print(f"Escrito: {args.json_out}")
        print(json.dumps({"signals": result["signals"]}, ensure_ascii=False, indent=2))
    else:
        print(out)


if __name__ == "__main__":
    main()
